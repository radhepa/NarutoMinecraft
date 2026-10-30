package dev.shinobi.combat.runtime.mixin.client;

import dev.shinobi.combat.runtime.Fighter;
import dev.shinobi.combat.runtime.client.ShinobiCombatClient;
import net.minecraft.client.model.player.PlayerModel;
import net.minecraft.client.renderer.entity.state.AvatarRenderState;
import org.spongepowered.asm.mixin.Mixin;
import org.spongepowered.asm.mixin.injection.At;
import org.spongepowered.asm.mixin.injection.Inject;
import org.spongepowered.asm.mixin.injection.callback.CallbackInfo;

/** Weaving raises both hands together in front of the chest; guarding crosses the forearms before the face. */
@Mixin(PlayerModel.class)
abstract class PlayerModelMixin {
    @Inject(method = "setupAnim(Lnet/minecraft/client/renderer/entity/state/AvatarRenderState;)V", at = @At("TAIL"))
    private void shinobi_combat$pose(AvatarRenderState state, CallbackInfo ci) {
        int pose = state.getDataOrDefault(ShinobiCombatClient.POSE, Fighter.Stance.NONE);
        if (pose == Fighter.Stance.NONE) return;
        var m = (PlayerModel) (Object) this;
        boolean weave = pose == Fighter.Stance.WEAVING;
        m.rightArm.xRot = m.leftArm.xRot = weave ? -1.1F : -1.6F;
        m.rightArm.yRot = weave ? -0.55F : -0.9F;
        m.leftArm.yRot = -m.rightArm.yRot;
        m.rightArm.zRot = m.leftArm.zRot = 0;
    }
}
