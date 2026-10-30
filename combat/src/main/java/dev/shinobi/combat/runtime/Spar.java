package dev.shinobi.combat.runtime;

import dev.shinobi.combat.ComboMachine;
import dev.shinobi.combat.Damage;
import dev.shinobi.combat.Nature;
import dev.shinobi.combat.Pool;
import dev.shinobi.combat.Scaling;
import net.fabricmc.fabric.api.event.Event;
import net.fabricmc.fabric.api.event.EventFactory;
import net.minecraft.core.BlockPos;
import net.minecraft.core.particles.ParticleTypes;
import net.minecraft.network.chat.Component;
import net.minecraft.network.protocol.game.ClientboundSetSubtitleTextPacket;
import net.minecraft.network.protocol.game.ClientboundSetTitleTextPacket;
import net.minecraft.server.MinecraftServer;
import net.minecraft.server.level.ServerLevel;
import net.minecraft.server.level.ServerPlayer;
import net.minecraft.sounds.SoundEvent;
import net.minecraft.sounds.SoundEvents;
import net.minecraft.sounds.SoundSource;
import net.minecraft.world.entity.EntityTypes;
import net.minecraft.world.entity.Mob;
import net.minecraft.world.entity.npc.villager.Villager;
import net.minecraft.world.level.ChunkPos;
import net.minecraft.world.phys.AABB;

import java.util.HashMap;
import java.util.Locale;
import java.util.Map;
import java.util.UUID;
import java.util.function.Consumer;

/**
 * The practice spar (P06-1): the server takes each attack on a spar partner through Academy taijutsu's combo machine,
 * spends its stamina and deals combat-core damage to the bout's own health, and the partner strikes back every two
 * seconds. Nobody is really hurt: a bout ends at zero health, won or lost, and the next hit starts another.
 * shortcut: the hit lands when the input arrives (not after the move's startup), the partner never guards or moves,
 * and sneak-attack is the heavy input, until P06's full fighter and controls.
 */
public final class Spar {
    public static final String PARTNER = "shinobi_combat.spar_partner";
    static final double HEALTH = 20, REACH = 3.5, LEAVE = 12;
    static final int COUNTER_TICKS = 40;
    /** Fired on the server thread when a player wins a bout. */
    @SuppressWarnings("unchecked")
    public static final Event<Consumer<ServerPlayer>> WON = EventFactory.createArrayBacked(Consumer.class, all -> player -> {
        for (var l : all) l.accept(player);
    });
    private static final Map<UUID, Bout> BOUTS = new HashMap<>();

    private Spar() {}

    static final class Bout {
        final Mob partner;
        final ComboMachine combo = new ComboMachine(ShinobiCombat.data.moveset(null));
        final Pool stamina = Pool.stamina(100);
        double partnerHealth = HEALTH, health = HEALTH;
        long counter;

        Bout(Mob partner, long now) { this.partner = partner; counter = now + COUNTER_TICKS; }
    }

    /** One attack on the partner: a move if the combo machine and stamina allow it, with its feedback. */
    static void attack(ServerPlayer player, Mob partner) {
        var level = player.level();
        long now = level.getGameTime();
        var bout = BOUTS.get(player.getUUID());
        if (bout == null || bout.partner != partner) BOUTS.put(player.getUUID(), bout = new Bout(partner, now));
        var started = bout.combo.press(player.isShiftKeyDown() ? "H" : "L", now, ComboMachine.Context.ground(1, 0));
        if (started == null) {
            player.sendOverlayMessage(Component.translatable("shinobi_combat.spar.busy"));
            return;
        }
        var move = started.move();
        if (!bout.stamina.spend(move.stamina())) {
            bout.combo.reset();
            player.sendOverlayMessage(Component.translatable("shinobi_combat.spar.tired"));
            return;
        }
        double hp = Damage.hit(Damage.Attack.player(move.damage(), move.type(), Damage.Delivery.MELEE, 1, Scaling.Pillar.TAIJUTSU, 1, 1),
                Damage.Defence.of(false, 1, 0, 0, Nature.NONE)).hp();
        bout.partnerHealth -= hp;
        level.sendParticles(ParticleTypes.CRIT, partner.getX(), partner.getY(.6), partner.getZ(), 10, .3, .3, .3, .2);
        level.playSound(null, partner.getX(), partner.getY(), partner.getZ(), SoundEvents.PLAYER_ATTACK_STRONG, SoundSource.PLAYERS, 1, 1);
        level.broadcastDamageEvent(partner, level.damageSources().playerAttack(player));
        if (bout.partnerHealth <= 0) {
            BOUTS.remove(player.getUUID());
            title(player, "won", SoundEvents.UI_TOAST_CHALLENGE_COMPLETE);
            WON.invoker().accept(player);
        } else player.sendOverlayMessage(Component.translatable("shinobi_combat.spar.hit", Component.translatable("shinobi_combat.move." + move.id()),
                one(hp), one(bout.partnerHealth), one(bout.health), (int) bout.stamina.value()));
    }

    /** Each tick: stamina refills, the partner strikes back in reach, and a bout ends when its player leaves. */
    static void tick(MinecraftServer server) {
        var it = BOUTS.entrySet().iterator();
        while (it.hasNext()) {
            var e = it.next();
            var bout = e.getValue();
            var player = server.getPlayerList().getPlayer(e.getKey());
            if (player == null || bout.partner.isRemoved() || player.level() != bout.partner.level() || !player.closerThan(bout.partner, LEAVE)) {
                it.remove();
                if (player != null) player.sendOverlayMessage(Component.translatable("shinobi_combat.spar.left"));
                continue;
            }
            bout.stamina.tick(1);
            var level = player.level();
            if (level.getGameTime() < bout.counter || !player.closerThan(bout.partner, REACH)) continue;
            bout.counter = level.getGameTime() + COUNTER_TICKS;
            double hp = Damage.hit(Damage.Attack.enemy(1.5, "physical.blunt", Damage.Delivery.MELEE, 1, 1, 1), Damage.Defence.of(true, 1, 0, 0, Nature.NONE)).hp();
            bout.health -= hp;
            level.broadcastDamageEvent(player, level.damageSources().mobAttack(bout.partner));
            if (bout.health <= 0) {
                it.remove();
                title(player, "lost", SoundEvents.VILLAGER_NO);
            } else player.sendOverlayMessage(Component.translatable("shinobi_combat.spar.struck", one(hp), one(bout.partnerHealth), one(bout.health)));
        }
    }

    static void end(ServerPlayer player) { BOUTS.remove(player.getUUID()); }

    /** The spar partner by {@code at}, spawned there if none stands within eight blocks; null until the spot's entities load. */
    public static Mob partnerAt(ServerLevel level, BlockPos at) {
        if (!level.areEntitiesLoaded(ChunkPos.pack(at))) return null;
        var near = level.getEntitiesOfClass(Villager.class, new AABB(at).inflate(8), v -> v.entityTags().contains(PARTNER));
        if (!near.isEmpty()) return near.getFirst();
        var v = new Villager(EntityTypes.VILLAGER, level);
        v.setPos(at.getX() + .5, at.getY(), at.getZ() + .5);
        v.setNoAi(true);
        v.setPermanentlyInvulnerable(true);
        v.setPersistenceRequired();
        v.addTag(PARTNER);
        v.setCustomName(Component.translatable("shinobi_combat.partner"));
        v.setCustomNameVisible(true);
        level.addFreshEntity(v);
        return v;
    }

    private static void title(ServerPlayer player, String how, SoundEvent sound) {
        player.connection.send(new ClientboundSetTitleTextPacket(Component.translatable("shinobi_combat.spar." + how)));
        player.connection.send(new ClientboundSetSubtitleTextPacket(Component.translatable("shinobi_combat.spar." + how + ".sub")));
        player.level().playSound(null, player.getX(), player.getY(), player.getZ(), sound, SoundSource.PLAYERS, 1, 1);
    }

    private static String one(double v) { return String.format(Locale.ROOT, "%.1f", Math.max(0, v)); }
}
