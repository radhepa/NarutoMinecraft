package dev.shinobi.combat.runtime.mixin.client;

import dev.shinobi.combat.runtime.client.ShinobiCombatClient;
import dev.villagefriends.client.ResidentRenderState;
import net.minecraft.client.model.HumanoidModel;
import org.spongepowered.asm.mixin.Mixin;
import org.spongepowered.asm.mixin.Pseudo;
import org.spongepowered.asm.mixin.injection.At;
import org.spongepowered.asm.mixin.injection.Inject;
import org.spongepowered.asm.mixin.injection.callback.CallbackInfo;

/** Village Friends' residents pose their gait after HumanoidModel's: the clip is posed again on top. Skipped without VF. */
@Pseudo
@Mixin(targets = "dev.villagefriends.client.ResidentModel")
abstract class ResidentModelMixin {
    @Inject(method = "setupAnim(Ldev/villagefriends/client/ResidentRenderState;)V", at = @At("TAIL"))
    private void shinobi_combat$pose(ResidentRenderState state, CallbackInfo ci) {
        ShinobiCombatClient.pose((HumanoidModel<?>) (Object) this, state);
    }
}
