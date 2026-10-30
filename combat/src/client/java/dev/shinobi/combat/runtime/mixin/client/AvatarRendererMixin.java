package dev.shinobi.combat.runtime.mixin.client;

import dev.shinobi.combat.runtime.ShinobiCombat;
import dev.shinobi.combat.runtime.client.ShinobiCombatClient;
import net.minecraft.client.renderer.entity.player.AvatarRenderer;
import net.minecraft.client.renderer.entity.state.AvatarRenderState;
import net.minecraft.world.entity.Avatar;
import org.spongepowered.asm.mixin.Mixin;
import org.spongepowered.asm.mixin.injection.At;
import org.spongepowered.asm.mixin.injection.Inject;
import org.spongepowered.asm.mixin.injection.callback.CallbackInfo;

/** Carries a player's synced stance into its render state for PlayerModelMixin. */
@Mixin(AvatarRenderer.class)
abstract class AvatarRendererMixin {
    @Inject(method = "extractRenderState(Lnet/minecraft/world/entity/Avatar;Lnet/minecraft/client/renderer/entity/state/AvatarRenderState;F)V", at = @At("TAIL"))
    private void shinobi_combat$stance(Avatar avatar, AvatarRenderState state, float partialTick, CallbackInfo ci) {
        var stance = avatar.getAttached(ShinobiCombat.STANCE);
        state.setData(ShinobiCombatClient.POSE, stance == null ? 0 : stance.pose());
    }
}
