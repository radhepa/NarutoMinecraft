package dev.shinobi.combat.runtime.mixin.client;

import dev.shinobi.combat.runtime.ShinobiCombat;
import dev.shinobi.combat.runtime.client.ShinobiCombatClient;
import net.minecraft.client.model.geom.ModelPart;
import net.minecraft.client.model.player.PlayerModel;
import net.minecraft.client.renderer.entity.state.AvatarRenderState;
import org.spongepowered.asm.mixin.Mixin;
import org.spongepowered.asm.mixin.injection.At;
import org.spongepowered.asm.mixin.injection.Inject;
import org.spongepowered.asm.mixin.injection.callback.CallbackInfo;

/** Poses the parts a keyed clip of animations.json names (the signs, the block, a cast, a dodge) over vanilla's pose. */
@Mixin(PlayerModel.class)
abstract class PlayerModelMixin {
    @Inject(method = "setupAnim(Lnet/minecraft/client/renderer/entity/state/AvatarRenderState;)V", at = @At("TAIL"))
    private void shinobi_combat$pose(AvatarRenderState state, CallbackInfo ci) {
        var clip = ShinobiCombat.data.clips.get(state.getDataOrDefault(ShinobiCombatClient.CLIP, ""));
        if (clip == null) return;
        var m = (PlayerModel) (Object) this;
        float t = state.getDataOrDefault(ShinobiCombatClient.AGE, 0F);
        ModelPart[] parts = {m.head, m.body, m.rightArm, m.leftArm, m.rightLeg, m.leftLeg};
        String[] names = {"head", "body", "right_arm", "left_arm", "right_leg", "left_leg"};
        for (int i = 0; i < parts.length; i++) {
            var r = clip.rot(names[i], t);
            if (r == null) continue;
            parts[i].xRot = (float) Math.toRadians(r[0]);
            parts[i].yRot = (float) Math.toRadians(r[1]);
            parts[i].zRot = (float) Math.toRadians(r[2]);
        }
    }
}
