package dev.shinobi.combat.runtime.mixin;

import dev.shinobi.combat.runtime.Fighter;
import dev.shinobi.combat.runtime.Tools;
import net.minecraft.server.level.ServerLevel;
import net.minecraft.server.level.ServerPlayer;
import net.minecraft.world.damagesource.DamageSource;
import net.minecraft.world.entity.LivingEntity;
import org.spongepowered.asm.mixin.Mixin;
import org.spongepowered.asm.mixin.injection.At;
import org.spongepowered.asm.mixin.injection.Inject;
import org.spongepowered.asm.mixin.injection.ModifyArg;
import org.spongepowered.asm.mixin.injection.callback.CallbackInfo;

/**
 * A guarding player takes less from a melee hit that lands: the amount hurtServer passes on past its cooldown (Fighter.guard).
 * A jump may be a roof hop (Tools.hop; the server calls jumpFromGround from the player's movement packet).
 */
@Mixin(LivingEntity.class)
abstract class LivingEntityMixin {
    @ModifyArg(method = "hurtServer", index = 2, at = @At(value = "INVOKE",
            target = "Lnet/minecraft/world/entity/LivingEntity;actuallyHurt(Lnet/minecraft/server/level/ServerLevel;Lnet/minecraft/world/damagesource/DamageSource;F)V"))
    private float shinobi_combat$guard(ServerLevel level, DamageSource source, float amount) {
        return (Object) this instanceof ServerPlayer p ? Fighter.guard(p, source, amount) : amount;
    }

    @Inject(method = "jumpFromGround", at = @At("TAIL"))
    private void shinobi_combat$roofHop(CallbackInfo ci) {
        Tools.hop((LivingEntity) (Object) this);
    }
}
