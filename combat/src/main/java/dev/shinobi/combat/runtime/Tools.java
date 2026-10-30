package dev.shinobi.combat.runtime;

import dev.shinobi.combat.Chakra;
import net.minecraft.core.particles.ParticleTypes;
import net.minecraft.server.level.ServerLevel;
import net.minecraft.server.level.ServerPlayer;
import net.minecraft.sounds.SoundEvents;
import net.minecraft.sounds.SoundSource;
import net.minecraft.tags.BlockTags;
import net.minecraft.world.effect.MobEffectInstance;
import net.minecraft.world.effect.MobEffects;
import net.minecraft.world.entity.Entity;
import net.minecraft.world.entity.LivingEntity;
import net.minecraft.world.entity.Mob;
import net.minecraft.world.level.Level;
import net.minecraft.world.phys.AABB;
import net.minecraft.world.phys.Vec3;

/**
 * The Academy tools and roof hopping in the world (P06): the smoke bomb's burst, the wire's trip and the hop off a
 * roof. The numbers are data/combat/weapons/tools.json's and techniques/movement.json's.
 */
public final class Tools {
    static final double SMOKE_RADIUS = 4, HOP_CHAKRA = 1, HOP_SPEED = .8;
    static final int SMOKE_TICKS = 120, TRIP_TICKS = 40;

    private Tools() {}

    /** A smoke bomb bursts: mobs inside lose their target, everyone else inside is blinded, and its thrower, if inside (one dropped at their feet), leaves their tracking. */
    public static void smoke(ServerLevel level, Vec3 at, Entity owner) {
        level.sendParticles(ParticleTypes.CAMPFIRE_COSY_SMOKE, at.x, at.y + 1, at.z, 40, SMOKE_RADIUS / 2, 1, SMOKE_RADIUS / 2, .01);
        level.playSound(null, at.x, at.y, at.z, SoundEvents.FIRE_EXTINGUISH, SoundSource.PLAYERS, 1, .8F);
        for (var e : level.getEntitiesOfClass(LivingEntity.class, new AABB(at, at).inflate(SMOKE_RADIUS), e -> e.position().closerThan(at, SMOKE_RADIUS))) {
            if (e instanceof Mob m) m.setTarget(null);
            // Invisibility is what vanilla targeting reads (a hunter's range shrinks to a few blocks); blindness only darkens a player's screen.
            e.addEffect(new MobEffectInstance(e == owner ? MobEffects.INVISIBILITY : MobEffects.BLINDNESS, SMOKE_TICKS));
        }
    }

    /**
     * A mob walking into a wire is tripped: held down for 2 s. Every tripwire trips, string's too.
     * shortcut: tripwire mode only, one wire per item and no bomb triggers; the tether and binding modes come with the Genin tools.
     */
    public static void trip(Level level, Entity e) {
        if (!(level instanceof ServerLevel server) || !(e instanceof Mob m)) return;
        var held = m.getEffect(MobEffects.SLOWNESS);
        if (held != null && held.getAmplifier() >= 9) return;   // already tripped
        m.addEffect(new MobEffectInstance(MobEffects.SLOWNESS, TRIP_TICKS, 9));
        m.getNavigation().stop();
        server.sendParticles(ParticleTypes.CRIT, m.getX(), m.getY() + .3, m.getZ(), 8, .3, .1, .3, .1);
        server.playSound(null, m.getX(), m.getY(), m.getZ(), SoundEvents.TRIPWIRE_CLICK_ON, SoundSource.HOSTILE, 1, 1.2F);
    }

    /**
     * Roof hopping: a sprint jump off leaves, logs or a roof (stairs, slabs) with a point of chakra to spare pushes on
     * forward. The server runs it from the jump packet: it charges the chakra and sends the push, as a dodge does.
     * shortcut: every player hops; the instructor's lesson gates it once movement is taught (P07 lessons).
     */
    public static void hop(LivingEntity e) {
        if (!(e instanceof ServerPlayer p) || !p.isSprinting() || p.isSpectator()) return;
        var under = p.level().getBlockState(p.getOnPos());
        if (!(under.is(BlockTags.LEAVES) || under.is(BlockTags.LOGS) || under.is(BlockTags.STAIRS) || under.is(BlockTags.SLABS))) return;
        var f = Fighter.of(p);
        if (!f.chakra.spend(Chakra.cost(HOP_CHAKRA, Fighter.CONTROL, false, 1), false).ok()) return;
        var look = Vec3.directionFromRotation(0, p.getYRot());
        p.setDeltaMovement(look.x * HOP_SPEED, p.getDeltaMovement().y + .1, look.z * HOP_SPEED);
        p.syncVelocity = true;
        f.play("combat.move.roof_hop", p.level().getGameTime());
        p.level().sendParticles(ParticleTypes.CLOUD, p.getX(), p.getY() + .1, p.getZ(), 4, .2, .05, .2, .02);
    }
}
