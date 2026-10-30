package dev.shinobi.combat.runtime;

import dev.shinobi.combat.CombatData;
import dev.shinobi.combat.Json;
import net.minecraft.core.component.DataComponents;
import net.minecraft.core.particles.ParticleTypes;
import net.minecraft.server.MinecraftServer;
import net.minecraft.server.level.ServerLevel;
import net.minecraft.server.level.ServerPlayer;
import net.minecraft.sounds.SoundEvents;
import net.minecraft.sounds.SoundSource;
import net.minecraft.world.effect.MobEffectInstance;
import net.minecraft.world.effect.MobEffects;
import net.minecraft.world.entity.Display;
import net.minecraft.world.entity.Entity;
import net.minecraft.world.entity.EntityTypes;
import net.minecraft.world.entity.Mob;
import net.minecraft.world.entity.decoration.Mannequin;
import net.minecraft.world.item.ItemStack;
import net.minecraft.world.item.Items;
import net.minecraft.world.item.component.ResolvableProfile;
import net.minecraft.world.phys.Vec3;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.UUID;

/**
 * The Academy techniques in the world (P06-2): Clone's decoys, Transformation's disguise and Substitution's log. Each
 * is a short-lived entity this class tracks and removes; one left in a save is removed when it loads.
 */
final class Jutsu {
    public static final String DECOY = "shinobi_combat.decoy", PROP = "shinobi_combat.prop";
    static final int LOG_TICKS = 40, AGGRO_RANGE = 24;
    private record Timed(Entity entity, long until) {}
    private static final List<Timed> TIMED = new ArrayList<>();
    private static final Map<UUID, Display.ItemDisplay> DISGUISES = new HashMap<>();

    private Jutsu() {}

    /**
     * Clone: copies of the player stand around them for the technique's ticks, and each mob hunting the player turns on
     * one at the technique's chance. A hit pops a copy.
     * shortcut: the copies wear the account skin (not the made look), stand still, and fool only mobs already hunting the
     * player, until clones run off and the look reaches the combat mod.
     */
    static void clone(ServerPlayer p, CombatData.Technique t) {
        var level = p.level();
        int count = t.count(), ticks = Json.integer(t.shape(), "ticks", 100);
        double chance = t.effects().isEmpty() ? 0 : Json.num(t.effects().getFirst(), "retarget_chance", 0);
        var decoys = new ArrayList<Mannequin>();
        for (int i = 1; i <= count; i++) {
            // Spread around the player, never straight ahead of them.
            double a = Math.toRadians(p.getYRot()) + i * 2 * Math.PI / (count + 1);
            var m = new Mannequin(EntityTypes.MANNEQUIN, level);
            m.setComponent(DataComponents.PROFILE, ResolvableProfile.createResolved(p.getGameProfile()));
            m.snapTo(p.getX() - 1.5 * Math.sin(a), p.getY(), p.getZ() + 1.5 * Math.cos(a), p.getYRot(), 0);
            m.addTag(DECOY);
            spawn(level, m, ticks);
            smoke(level, m.position(), 10);
            decoys.add(m);
        }
        level.playSound(null, p.getX(), p.getY(), p.getZ(), SoundEvents.ILLUSIONER_MIRROR_MOVE, SoundSource.PLAYERS, 1, 1);
        for (var mob : level.getEntitiesOfClass(Mob.class, p.getBoundingBox().inflate(AGGRO_RANGE), m -> m.getTarget() == p))
            if (level.getRandom().nextDouble() < chance) mob.setTarget(decoys.get(level.getRandom().nextInt(decoys.size())));
    }

    /**
     * Transformation: the player hides as a log until they attack or are hurt; mobs hunting them lose them.
     * shortcut: always a log (an item display following the player, the player invisible), until the picker of a resident's look or an object.
     */
    static void disguise(ServerPlayer p) {
        if (DISGUISES.containsKey(p.getUUID())) return;
        var d = new Display.ItemDisplay(EntityTypes.ITEM_DISPLAY, p.level());
        d.getSlot(0).set(new ItemStack(Items.OAK_LOG));
        d.setPos(p.getX(), p.getY() + .5, p.getZ());
        d.addTag(PROP);
        DISGUISES.put(p.getUUID(), d);
        p.level().addFreshEntity(d);
        hide(p);
        for (var mob : p.level().getEntitiesOfClass(Mob.class, p.getBoundingBox().inflate(AGGRO_RANGE), m -> m.getTarget() == p)) mob.setTarget(null);
        smoke(p.level(), p.position(), 16);
    }

    public static boolean disguised(ServerPlayer p) { return DISGUISES.containsKey(p.getUUID()); }

    static void undisguise(ServerPlayer p) {
        var d = DISGUISES.remove(p.getUUID());
        if (d == null) return;
        d.discard();
        p.removeEffect(MobEffects.INVISIBILITY);
        smoke(p.level(), p.position(), 16);
    }

    // A short effect kept topped up: a disguise lost to a crash wears off by itself.
    private static void hide(ServerPlayer p) { p.addEffect(new MobEffectInstance(MobEffects.INVISIBILITY, 40, 0, false, false)); }

    /** Substitution's log, standing where the player was for two seconds. */
    static void log(ServerLevel level, Vec3 at) {
        var d = new Display.ItemDisplay(EntityTypes.ITEM_DISPLAY, level);
        d.getSlot(0).set(new ItemStack(Items.OAK_LOG));
        d.setPos(at.x, at.y + .5, at.z);
        d.addTag(PROP);
        spawn(level, d, LOG_TICKS);
        smoke(level, at, 16);
        level.playSound(null, at.x, at.y, at.z, SoundEvents.WOOD_BREAK, SoundSource.PLAYERS, 1, 1);
    }

    static void pop(Mannequin m) {
        smoke((ServerLevel) m.level(), m.position(), 10);
        m.discard();
    }

    static void smoke(ServerLevel level, Vec3 at, int count) {
        level.sendParticles(ParticleTypes.POOF, at.x, at.y + 1, at.z, count, .3, .5, .3, .02);
    }

    private static void spawn(ServerLevel level, Entity e, int ticks) {
        TIMED.add(new Timed(e, level.getGameTime() + ticks));
        level.addFreshEntity(e);
    }

    /** Each tick: timed entities run out and disguises follow their players. */
    static void tick(MinecraftServer server) {
        TIMED.removeIf(t -> {
            if (!t.entity().isRemoved() && t.entity().level().getGameTime() < t.until()) return false;
            if (t.entity() instanceof Mannequin m && !m.isRemoved()) pop(m);
            else t.entity().discard();
            return true;
        });
        DISGUISES.entrySet().removeIf(e -> {
            var p = server.getPlayerList().getPlayer(e.getKey());
            var d = e.getValue();
            if (p == null || d.isRemoved() || p.level() != d.level()) { d.discard(); return true; }
            d.setPos(p.getX(), p.getY() + .5, p.getZ());
            if (!p.hasEffect(MobEffects.INVISIBILITY) || p.getEffect(MobEffects.INVISIBILITY).getDuration() < 20) hide(p);
            return false;
        });
    }

    /** ENTITY_LOAD: a decoy or prop this run does not track was left in the save. */
    static void loaded(Entity e) {
        var tags = e.entityTags();
        if ((tags.contains(DECOY) || tags.contains(PROP)) && TIMED.stream().noneMatch(t -> t.entity() == e) && !DISGUISES.containsValue(e)) e.discard();
    }

    static void clear() { TIMED.clear(); DISGUISES.clear(); }
}
