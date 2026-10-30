package dev.shinobi.combat.runtime;

import com.mojang.serialization.Codec;
import com.mojang.serialization.codecs.RecordCodecBuilder;
import dev.shinobi.combat.Chakra;
import dev.shinobi.combat.Cooldowns;
import dev.shinobi.combat.Damage;
import dev.shinobi.combat.HandSign;
import dev.shinobi.combat.Json;
import dev.shinobi.combat.Pool;
import dev.shinobi.combat.SignBook;
import dev.shinobi.combat.Weaver;
import io.netty.buffer.ByteBuf;
import net.minecraft.core.particles.ParticleTypes;
import net.minecraft.network.FriendlyByteBuf;
import net.minecraft.network.chat.Component;
import net.minecraft.network.codec.ByteBufCodecs;
import net.minecraft.network.codec.StreamCodec;
import net.minecraft.network.protocol.common.custom.CustomPacketPayload;
import net.minecraft.resources.Identifier;
import net.minecraft.server.MinecraftServer;
import net.minecraft.server.level.ServerPlayer;
import net.minecraft.sounds.SoundEvent;
import net.minecraft.sounds.SoundEvents;
import net.minecraft.sounds.SoundSource;
import net.minecraft.tags.DamageTypeTags;
import net.minecraft.world.damagesource.DamageSource;
import net.minecraft.world.entity.LivingEntity;
import net.minecraft.world.entity.decoration.Mannequin;
import net.minecraft.world.phys.Vec3;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Objects;
import java.util.UUID;

/**
 * A player's fighting state (P06-2): chakra, stamina and the techniques learned, kept on the player and synced to its
 * owner; the weave, guard, dodge and substitution its client asks for through one payload; and the pose every client
 * draws. The server owns it all: a client only says which key went down.
 * shortcut: fixed starting stats (chakra 53, stamina 110, control 30, ninjutsu rank 1), no mastery, cast time or quick
 * slots, until levels, training and the full controls.
 */
public final class Fighter {
    public static final double CHAKRA = 53, STAMINA = 110;
    public static final String CLONE = "combat:nin.clone", TRANSFORMATION = "combat:nin.transformation", SUBSTITUTION = "combat:nin.substitution";
    // core/resources.json and COMBAT.md, "Dodges": 22 stamina, 6 i-frames, a 1.5 s cooldown, about 4 blocks.
    static final int CONTROL = 30, ARM_TICKS = 10, DODGE_COST = 22, DODGE_IFRAMES = 6, DODGE_COOLDOWN = 30;
    static final double DODGE_SPEED = 1.6, GUARD_REGEN = 0.3;
    static final String DODGE = "dodge";

    /** What is saved with the player and synced to its owner. */
    public record State(double chakra, double stamina, List<String> learned) {
        public static final State NEW = new State(CHAKRA, STAMINA, List.of());
        public static final Codec<State> CODEC = RecordCodecBuilder.create(i -> i.group(
                Codec.DOUBLE.fieldOf("chakra").forGetter(State::chakra),
                Codec.DOUBLE.fieldOf("stamina").forGetter(State::stamina),
                Codec.STRING.listOf().fieldOf("learned").forGetter(State::learned)).apply(i, State::new));
    }
    /** What every client draws: the pose, the signs woven so far, and the clip of animations.json playing ("" for none) since a game tick. */
    public record Stance(int pose, List<String> signs, String clip, long since) {
        public static final int NONE = 0, WEAVING = 1, GUARDING = 2;
        public static final StreamCodec<ByteBuf, Stance> CODEC = StreamCodec.composite(ByteBufCodecs.VAR_INT, Stance::pose,
                ByteBufCodecs.STRING_UTF8.apply(ByteBufCodecs.list()), Stance::signs, ByteBufCodecs.STRING_UTF8, Stance::clip,
                ByteBufCodecs.VAR_LONG, Stance::since, Stance::new);
    }
    /** A key the client pressed: one action and its argument (a sign's index, guard on or off). */
    public record Act(int action, int arg) implements CustomPacketPayload {
        public static final int BEGIN = 0, SIGN = 1, RELEASE = 2, CANCEL = 3, GUARD = 4, DODGE = 5, SUBSTITUTE = 6;
        public static final Type<Act> TYPE = new Type<>(Identifier.fromNamespaceAndPath(ShinobiCombat.MOD_ID, "act"));
        public static final StreamCodec<FriendlyByteBuf, Act> CODEC = StreamCodec.composite(ByteBufCodecs.VAR_INT, Act::action,
                ByteBufCodecs.VAR_INT, Act::arg, Act::new);
        @Override public Type<? extends CustomPacketPayload> type() { return TYPE; }
    }

    private static final Map<UUID, Fighter> ALL = new HashMap<>();

    final Chakra chakra = new Chakra(CHAKRA);
    final Pool stamina = Pool.stamina(STAMINA);
    final Cooldowns cooldowns = new Cooldowns();
    final List<String> learned;
    Weaver weaver;
    boolean guarding;
    long armedUntil = Long.MIN_VALUE, iframesUntil = Long.MIN_VALUE, shotUntil = Long.MIN_VALUE;
    /** A one-shot clip (a cast, a fizzle, a dodge) shown until shotUntil. */
    String shot = "";

    private Fighter(State s) {
        chakra.drain(CHAKRA - s.chakra());
        stamina.spend(STAMINA - s.stamina());
        learned = new ArrayList<>(s.learned());
        weaver = new Weaver(book(learned), Weaver.ticksPerSign(CONTROL, 1));
    }

    static Fighter of(ServerPlayer p) { return ALL.computeIfAbsent(p.getUUID(), u -> new Fighter(p.getAttachedOrCreate(ShinobiCombat.STATE))); }

    /** The sign book for a set of learned ids (the server's weaver and the client's hint). */
    public static SignBook book(List<String> learned) {
        var book = new SignBook();
        for (String id : learned) {
            var t = ShinobiCombat.data.techniques.get(id);
            if (t != null) book.learn(id, t.rank(), t.signs());
        }
        return book;
    }

    boolean teach(ServerPlayer p, String id) {
        if (learned.contains(id) || !ShinobiCombat.data.techniques.containsKey(id)) return false;
        learned.add(id);
        weaver = new Weaver(book(learned), Weaver.ticksPerSign(CONTROL, 1));
        save(p);
        return true;
    }

    /** One action from the client's keys. */
    static void act(ServerPlayer p, Act a) {
        if (p.isSpectator() || !p.isAlive()) return;
        var f = of(p);
        long now = p.level().getGameTime();
        switch (a.action()) {
            case Act.BEGIN -> f.weaver.begin(now);
            // A sign past the longest sequence known already fizzles: more would only grow the weave.
            case Act.SIGN -> { if (a.arg() >= 0 && a.arg() < HandSign.values().length && f.weaver.woven().size() <= f.longest()) f.weaver.input(HandSign.values()[a.arg()], now); }
            case Act.RELEASE -> f.release(p, now);
            case Act.CANCEL -> { if (f.weaver.weaving()) f.weaver.release(now); }
            case Act.GUARD -> f.guarding = a.arg() != 0;
            case Act.DODGE -> f.dodge(p, now);
            case Act.SUBSTITUTE -> f.arm(p, now);
            default -> {}
        }
        // The tick syncs what the action changed, once however many actions came in.
    }

    private int longest() {
        return learned.stream().map(ShinobiCombat.data.techniques::get).filter(Objects::nonNull).mapToInt(t -> t.signs().size()).max().orElse(0);
    }

    /** AFTER_DEATH: a death drops the guard and the weave (a dead player's keys are not heard). */
    static void died(ServerPlayer p) {
        var f = ALL.get(p.getUUID());
        if (f == null) return;
        f.guarding = false;
        if (f.weaver.weaving()) f.weaver.release(p.level().getGameTime());
    }

    private void release(ServerPlayer p, long now) {
        if (!weaver.weaving()) return;
        var r = weaver.release(now);
        switch (r.outcome()) {
            case CAST -> { if (cast(p, r.technique().orElseThrow(), now)) play("combat.cast.push_palms", now); }
            case FIZZLE, INTERRUPTED -> {
                play("combat.sign.fizzle", now);
                boolean fizzle = r.outcome() == Weaver.Outcome.FIZZLE;
                chakra.drain((fizzle ? Weaver.FIZZLE_COST : Weaver.INTERRUPT_COST) * cheapest());
                Jutsu.smoke(p.level(), p.position(), 6);
                tell(p, fizzle ? "fizzle" : "interrupted", SoundEvents.FIRE_EXTINGUISH);
            }
            case EMPTY -> {}
        }
    }

    /** A fizzle's or interruption's share is of the cheapest woven technique known. shortcut: until the weave names the technique it was heading for. */
    private double cheapest() {
        return learned.stream().map(ShinobiCombat.data.techniques::get).filter(t -> t != null && !t.signless())
                .mapToDouble(t -> Chakra.cost(t.chakra(), CONTROL, false, 1)).min().orElse(0);
    }

    /** Casts a known technique if its cooldown is over and the chakra is there. */
    private boolean cast(ServerPlayer p, String id, long now) {
        var t = ShinobiCombat.data.technique(id);
        if (!cooldowns.ready(id, now)) {
            p.sendOverlayMessage(Component.translatable("shinobi_combat.cast.cooldown", t.name(), (cooldowns.remaining(id, now) + 19) / 20));
            return false;
        }
        if (!chakra.spend(Chakra.cost(t.chakra(), CONTROL, false, 1), false).ok()) {
            tell(p, "chakra", SoundEvents.PLAYER_BREATH);
            return false;
        }
        cooldowns.start(id, now, t.cooldownTicks());
        // shortcut: only the Academy techniques have a world effect yet; any other known technique casts as a puff of smoke.
        switch (id) {
            case CLONE -> Jutsu.clone(p, t);
            case TRANSFORMATION -> Jutsu.disguise(p);
            default -> Jutsu.smoke(p.level(), p.position(), 12);
        }
        p.sendOverlayMessage(Component.translatable("shinobi_combat.cast", t.name()));
        ShinobiCombat.CAST.invoker().accept(p, id);
        return true;
    }

    private void arm(ServerPlayer p, long now) {
        if (!learned.contains(SUBSTITUTION)) tell(p, "unknown", SoundEvents.PLAYER_ATTACK_NODAMAGE);
        else if (!cooldowns.ready(SUBSTITUTION, now))
            p.sendOverlayMessage(Component.translatable("shinobi_combat.cast.cooldown", ShinobiCombat.data.technique(SUBSTITUTION).name(),
                    (cooldowns.remaining(SUBSTITUTION, now) + 19) / 20));
        else armedUntil = now + ARM_TICKS;
    }

    private void dodge(ServerPlayer p, long now) {
        if (!cooldowns.ready(DODGE, now)) return;
        if (!stamina.has(DODGE_COST)) { tell(p, "winded", SoundEvents.PLAYER_BREATH); return; }
        stamina.spend(DODGE_COST);
        cooldowns.start(DODGE, now, DODGE_COOLDOWN);
        iframesUntil = Math.max(iframesUntil, now + DODGE_IFRAMES);
        // The keys held, turned by the player's facing (Entity.moveRelative); no direction dodges back.
        var in = p.getLastClientInput();
        double x = (in.left() ? 1 : 0) - (in.right() ? 1 : 0), z = (in.forward() ? 1 : 0) - (in.backward() ? 1 : 0);
        if (x == 0 && z == 0) z = -1;
        play("combat.def.dodge_" + (Math.abs(z) >= Math.abs(x) ? z > 0 ? "forward" : "back" : x > 0 ? "left" : "right"), now);
        double yaw = Math.toRadians(p.getYRot()), len = Math.hypot(x, z);
        var dir = new Vec3((x * Math.cos(yaw) - z * Math.sin(yaw)) / len, 0, (z * Math.cos(yaw) + x * Math.sin(yaw)) / len);
        p.setDeltaMovement(dir.x * DODGE_SPEED, 0.1, dir.z * DODGE_SPEED);
        p.syncVelocity = true;
        p.level().sendParticles(ParticleTypes.CLOUD, p.getX(), p.getY() + .1, p.getZ(), 6, .3, .05, .3, .02);
    }

    private boolean substitutable(long now) {
        return now <= armedUntil && cooldowns.ready(SUBSTITUTION, now) && !chakra.exhausted()
                && chakra.value() >= Chakra.cost(ShinobiCombat.data.technique(SUBSTITUTION).chakra(), CONTROL, false, 1);
    }

    /** Whether this hit never lands: i-frames, or an armed substitution (ALLOW_DAMAGE then takes it). */
    private boolean avoids(DamageSource source, long now) {
        return !source.is(DamageTypeTags.BYPASSES_INVULNERABILITY) && (now < iframesUntil || substitutable(now));
    }

    /** ALLOW_DAMAGE: a decoy pops; a player's i-frames and armed substitution avoid the hit; a hit that lands ends a disguise. */
    static boolean allow(LivingEntity e, DamageSource source) {
        if (e instanceof Mannequin m && m.entityTags().contains(Jutsu.DECOY)) { Jutsu.pop(m); return false; }
        if (!(e instanceof ServerPlayer p)) return true;
        var f = ALL.get(p.getUUID());
        if (f == null) return true;
        long now = p.level().getGameTime();
        if (f.avoids(source, now)) {
            if (now >= f.iframesUntil) f.substitute(p, source, now);
            return false;
        }
        Jutsu.undisguise(p);
        return true;
    }

    /**
     * The guard, from the LivingEntity mixin on a hit that lands (past the hurt cooldown and ALLOW_DAMAGE): a guarded melee hit takes {@link Damage#BLOCK_MELEE} off for
     * {@link Damage#GUARD_STAMINA_PER_DAMAGE} stamina a point stopped, and a guard without the stamina breaks. Any melee
     * hit that lands interrupts a weave.
     */
    public static float guard(ServerPlayer p, DamageSource source, float amount) {
        var f = ALL.get(p.getUUID());
        boolean melee = source.getEntity() != null && source.getEntity() == source.getDirectEntity() && !source.is(DamageTypeTags.IS_PROJECTILE);
        if (f == null || !melee) return amount;
        f.weaver.interrupt();
        if (!f.guarding) return amount;
        boolean held = f.stamina.spend(amount * Damage.BLOCK_MELEE * Damage.GUARD_STAMINA_PER_DAMAGE);
        f.save(p);
        if (!held) {
            f.guarding = false;
            f.stance(p);
            tell(p, "guard_broken", SoundEvents.PLAYER_ATTACK_WEAK);
            return amount;
        }
        p.level().playSound(null, p.getX(), p.getY(), p.getZ(), SoundEvents.PLAYER_ATTACK_NODAMAGE, SoundSource.PLAYERS, 1, 1.4F);
        return (float) (amount * (1 - Damage.BLOCK_MELEE));
    }

    /** Substitution: the chakra paid, a blink back away from the blow, i-frames and a log where the player stood. */
    private void substitute(ServerPlayer p, DamageSource source, long now) {
        var t = ShinobiCombat.data.technique(SUBSTITUTION);
        chakra.spend(Chakra.cost(t.chakra(), CONTROL, false, 1), false);
        cooldowns.start(SUBSTITUTION, now, t.cooldownTicks());
        armedUntil = Long.MIN_VALUE;
        iframesUntil = now + t.statuses().stream().filter(s -> s.getKey().equals("iframes")).mapToInt(Map.Entry::getValue).findFirst().orElse(12);
        var from = p.position();
        var by = source.getSourcePosition();
        var away = by == null ? p.getLookAngle().reverse() : from.subtract(by);
        away = new Vec3(away.x, 0, away.z);
        away = away.lengthSqr() < 1e-4 ? new Vec3(0, 0, 1) : away.normalize();
        // Half-block steps outward, stopping at the first blocked one: the blink never passes through a wall.
        Vec3 to = null;
        for (double d = .5, blink = Json.num(t.shape(), "blink", 5); d <= blink; d += .5) {
            var off = away.scale(d);
            if (!p.level().noCollision(p, p.getBoundingBox().move(off))) break;
            to = off;
        }
        if (to != null) p.teleportTo(from.x + to.x, from.y, from.z + to.z);
        Jutsu.log(p.level(), from);
        save(p);
        p.sendOverlayMessage(Component.translatable("shinobi_combat.cast", t.name()));
        ShinobiCombat.CAST.invoker().accept(p, SUBSTITUTION);
    }

    /** Each tick: chakra and stamina refill (stamina slower while guarding) and the bars and pose sync. */
    static void tick(MinecraftServer server) {
        for (var p : server.getPlayerList().getPlayers()) {
            var f = of(p);
            f.chakra.tick(ShinobiCombat.regen.applyAsDouble(p));
            f.stamina.tick(f.guarding ? GUARD_REGEN : 1);
            f.save(p);
            f.stance(p);
        }
    }

    /** Gives back a share of the player's chakra (a ramen's); the next tick saves it. */
    public static void restore(ServerPlayer p, double share) {
        var f = of(p);
        f.chakra.restore(share * f.chakra.max());
    }

    static void end(ServerPlayer p) {
        var f = ALL.remove(p.getUUID());
        if (f != null) f.save(p);
    }

    static void clear() { ALL.clear(); }

    // A tenth of a point is enough for the bars: it keeps the sync to a packet every other tick while chakra refills.
    private void save(ServerPlayer p) {
        var s = new State(Math.round(chakra.value() * 10) / 10.0, Math.round(stamina.value() * 10) / 10.0, List.copyOf(learned));
        if (!s.equals(p.getAttached(ShinobiCombat.STATE))) p.setAttached(ShinobiCombat.STATE, s);
    }

    void play(String clip, long now) {
        var c = ShinobiCombat.data.clips.get(clip);
        shot = clip;
        shotUntil = now + (c == null ? 0 : c.ticks());
    }

    /** The pose and its clip: the last sign woven (hands together before the first), the block, or a one-shot. */
    private void stance(ServerPlayer p) {
        long now = p.level().getGameTime();
        var woven = weaver.woven();
        int pose = weaver.weaving() ? Stance.WEAVING : guarding ? Stance.GUARDING : Stance.NONE;
        if (pose != Stance.NONE) shotUntil = Long.MIN_VALUE;   // a weave or guard ends a one-shot, which never replays after
        String clip = pose == Stance.WEAVING ? "combat.sign." + (woven.isEmpty() ? "transition" : woven.getLast().id())
                : pose == Stance.GUARDING ? "combat.def.block" : now < shotUntil ? shot : "";
        var signs = woven.stream().map(HandSign::id).toList();
        var had = p.getAttached(ShinobiCombat.STANCE);
        // The clip restarts when it changes or a sign is added (a second Ram plays again).
        long since = had != null && had.clip().equals(clip) && had.signs().equals(signs) ? had.since() : now;
        var s = new Stance(pose, signs, clip, since);
        if (Objects.equals(s, had) || had == null && pose == Stance.NONE && clip.isEmpty()) return;
        p.setAttached(ShinobiCombat.STANCE, s);
    }

    private static void tell(ServerPlayer p, String key, SoundEvent sound) {
        p.sendOverlayMessage(Component.translatable("shinobi_combat.cast." + key));
        p.level().playSound(null, p.getX(), p.getY(), p.getZ(), sound, SoundSource.PLAYERS, .8F, 1);
    }
}
