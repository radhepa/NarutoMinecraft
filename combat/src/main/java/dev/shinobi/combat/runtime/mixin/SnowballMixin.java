package dev.shinobi.combat.runtime.mixin;

import dev.shinobi.combat.runtime.ShinobiCombat;
import net.minecraft.world.entity.projectile.throwableitemprojectile.Snowball;
import org.spongepowered.asm.mixin.Mixin;
import org.spongepowered.asm.mixin.injection.At;
import org.spongepowered.asm.mixin.injection.ModifyArg;

/** A thrown practice kunai or shuriken (a snowball carrying the tool) deals the tool's damage. */
@Mixin(Snowball.class)
abstract class SnowballMixin {
    @ModifyArg(method = "onHitEntity", at = @At(value = "INVOKE",
            target = "Lnet/minecraft/world/entity/Entity;hurt(Lnet/minecraft/world/damagesource/DamageSource;F)V"), index = 1)
    private float shinobi_combat$practiceDamage(float amount) {
        var damage = ShinobiCombat.THROWN.get(((Snowball) (Object) this).getItem().getItem());
        return damage == null ? amount : damage.floatValue();
    }
}
