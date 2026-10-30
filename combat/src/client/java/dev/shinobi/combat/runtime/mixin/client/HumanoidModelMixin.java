package dev.shinobi.combat.runtime.mixin.client;

import dev.shinobi.combat.runtime.ShinobiCombat;
import dev.shinobi.combat.runtime.client.ShinobiCombatClient;
import net.minecraft.client.model.HumanoidModel;
import net.minecraft.client.model.geom.ModelPart;
import net.minecraft.client.renderer.entity.state.HumanoidRenderState;
import org.spongepowered.asm.mixin.Mixin;
import org.spongepowered.asm.mixin.injection.At;
import org.spongepowered.asm.mixin.injection.Inject;
import org.spongepowered.asm.mixin.injection.callback.CallbackInfo;

/**
 * Poses the parts a keyed clip of animations.json names (the signs, the block, a cast, a dodge) over vanilla's pose.
 * On HumanoidModel, so the worn armour's model (set up from the same render state) follows the player's; PlayerModel's
 * setupAnim ends in this one. Mobs carry no clip and keep their pose.
 */
@Mixin(HumanoidModel.class)
abstract class HumanoidModelMixin {
    private static final String[] NAMES = {"head", "body", "right_arm", "left_arm", "right_leg", "left_leg"};

    @Inject(method = "setupAnim(Lnet/minecraft/client/renderer/entity/state/HumanoidRenderState;)V", at = @At("TAIL"))
    private void shinobi_combat$pose(HumanoidRenderState state, CallbackInfo ci) {
        var clip = ShinobiCombat.data.clips.get(state.getDataOrDefault(ShinobiCombatClient.CLIP, ""));
        if (clip == null) return;
        var m = (HumanoidModel<?>) (Object) this;
        float t = state.getDataOrDefault(ShinobiCombatClient.AGE, 0F);
        ModelPart[] parts = {m.head, m.body, m.rightArm, m.leftArm, m.rightLeg, m.leftLeg};
        for (int i = 0; i < parts.length; i++) {
            var r = clip.rot(NAMES[i], t);
            if (r == null) continue;
            parts[i].xRot = (float) Math.toRadians(r[0]);
            parts[i].yRot = (float) Math.toRadians(r[1]);
            parts[i].zRot = (float) Math.toRadians(r[2]);
        }
    }
}
