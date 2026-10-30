package dev.shinobi.combat.runtime.mixin.client;

import dev.shinobi.combat.runtime.client.ShinobiCombatClient;
import net.minecraft.client.model.HumanoidModel;
import net.minecraft.client.renderer.entity.state.HumanoidRenderState;
import org.spongepowered.asm.mixin.Mixin;
import org.spongepowered.asm.mixin.injection.At;
import org.spongepowered.asm.mixin.injection.Inject;
import org.spongepowered.asm.mixin.injection.callback.CallbackInfo;

/**
 * Poses the parts a keyed clip of animations.json names (the signs, the block, a cast, a dodge) over vanilla's pose.
 * On HumanoidModel, so the worn armour's model (set up from the same render state) follows the player's; PlayerModel's
 * setupAnim ends in this one. Mobs carry no clip and keep their pose; residents pose again after VF's gait (ResidentModelMixin).
 */
@Mixin(HumanoidModel.class)
abstract class HumanoidModelMixin {
    @Inject(method = "setupAnim(Lnet/minecraft/client/renderer/entity/state/HumanoidRenderState;)V", at = @At("TAIL"))
    private void shinobi_combat$pose(HumanoidRenderState state, CallbackInfo ci) {
        ShinobiCombatClient.pose((HumanoidModel<?>) (Object) this, state);
    }
}
