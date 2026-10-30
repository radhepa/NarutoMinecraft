package dev.shinobi.combat.runtime.mixin;

import dev.shinobi.combat.runtime.Fighter;
import net.minecraft.server.level.ServerLevel;
import net.minecraft.server.level.ServerPlayer;
import net.minecraft.world.damagesource.DamageSource;
import net.minecraft.world.entity.LivingEntity;
import org.spongepowered.asm.mixin.Mixin;
import org.spongepowered.asm.mixin.injection.At;
import org.spongepowered.asm.mixin.injection.ModifyVariable;

/** A guarding player takes less from a melee hit (Fighter.guard). */
@Mixin(LivingEntity.class)
abstract class LivingEntityMixin {
    @ModifyVariable(method = "hurtServer", at = @At("HEAD"), argsOnly = true)
    private float shinobi_combat$guard(float amount, ServerLevel level, DamageSource source) {
        return (Object) this instanceof ServerPlayer p ? Fighter.guard(p, source, amount) : amount;
    }
}
