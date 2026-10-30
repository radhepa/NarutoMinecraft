package dev.shinobi.combat.runtime.mixin;

import dev.shinobi.combat.runtime.ShinobiCombat;
import dev.shinobi.combat.runtime.Tools;
import net.minecraft.server.level.ServerLevel;
import net.minecraft.world.entity.projectile.throwableitemprojectile.Snowball;
import org.spongepowered.asm.mixin.Mixin;
import net.minecraft.world.phys.HitResult;
import org.spongepowered.asm.mixin.injection.At;
import org.spongepowered.asm.mixin.injection.Inject;
import org.spongepowered.asm.mixin.injection.ModifyArg;
import org.spongepowered.asm.mixin.injection.callback.CallbackInfo;

/** A thrown practice kunai or shuriken (a snowball carrying the tool) deals the tool's damage; a smoke bomb bursts where it lands. */
@Mixin(Snowball.class)
abstract class SnowballMixin {
    @ModifyArg(method = "onHitEntity", at = @At(value = "INVOKE",
            target = "Lnet/minecraft/world/entity/Entity;hurt(Lnet/minecraft/world/damagesource/DamageSource;F)V"), index = 1)
    private float shinobi_combat$practiceDamage(float amount) {
        var damage = ShinobiCombat.THROWN.get(((Snowball) (Object) this).getItem().getItem());
        return damage == null ? amount : damage.floatValue();
    }

    @Inject(method = "onHit", at = @At("HEAD"))
    private void shinobi_combat$smoke(HitResult hit, CallbackInfo ci) {
        var ball = (Snowball) (Object) this;
        if (ball.level() instanceof ServerLevel level && ball.getItem().is(ShinobiCombat.SMOKE_BOMB)) Tools.smoke(level, ball.position(), ball.getOwner());
    }
}
