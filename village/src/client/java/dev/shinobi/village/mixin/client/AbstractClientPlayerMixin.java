package dev.shinobi.village.mixin.client;

import dev.shinobi.village.client.PlayerSkins;
import net.minecraft.client.player.AbstractClientPlayer;
import net.minecraft.world.entity.player.PlayerSkin;
import org.spongepowered.asm.mixin.Mixin;
import org.spongepowered.asm.mixin.injection.At;
import org.spongepowered.asm.mixin.injection.Inject;
import org.spongepowered.asm.mixin.injection.callback.CallbackInfoReturnable;

/** A player who made a character wears their look instead of the account skin. */
@Mixin(AbstractClientPlayer.class)
abstract class AbstractClientPlayerMixin {
    @Inject(method = "getSkin", at = @At("RETURN"), cancellable = true)
    private void narutominecraft$look(CallbackInfoReturnable<PlayerSkin> cir) {
        var skin = PlayerSkins.skin((AbstractClientPlayer) (Object) this, cir.getReturnValue());
        if (skin != null) cir.setReturnValue(skin);
    }
}
