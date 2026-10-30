package dev.shinobi.village.mixin.client;

import dev.shinobi.village.client.LeafUi;
import dev.villagefriends.client.LedgerScreen;
import net.minecraft.client.gui.GuiGraphicsExtractor;
import org.spongepowered.asm.mixin.Mixin;
import org.spongepowered.asm.mixin.Shadow;
import org.spongepowered.asm.mixin.injection.At;
import org.spongepowered.asm.mixin.injection.Inject;
import org.spongepowered.asm.mixin.injection.callback.CallbackInfo;

/** The ledger is bound in Konoha green with the leaf crest on its spine. */
@Mixin(LedgerScreen.class)
abstract class LedgerScreenMixin {
    @Shadow private int x, y, w, h;

    @Inject(method = "extractRenderState", at = @At("TAIL"))
    private void narutominecraft$crest(GuiGraphicsExtractor g, int mouseX, int mouseY, float delta, CallbackInfo ci) {
        LeafUi.crest(g, x + w / 2 - 4, y - 4);
        LeafUi.crest(g, x + w / 2 - 4, y + h - 5);
    }
}
