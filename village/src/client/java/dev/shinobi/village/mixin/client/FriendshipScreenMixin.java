package dev.shinobi.village.mixin.client;

import dev.shinobi.village.client.LeafUi;
import dev.villagefriends.client.FriendshipScreen;
import net.minecraft.client.gui.GuiGraphicsExtractor;
import org.spongepowered.asm.mixin.Mixin;
import org.spongepowered.asm.mixin.Shadow;
import org.spongepowered.asm.mixin.injection.At;
import org.spongepowered.asm.mixin.injection.Inject;
import org.spongepowered.asm.mixin.injection.callback.CallbackInfo;

/** The conversation's dialogue box is an unrolled scroll between two rods; the friendship card wears the leaf crest. */
@Mixin(FriendshipScreen.class)
abstract class FriendshipScreenMixin {
    @Shadow private int boxX, boxY, boxW, boxH, cardX, cardY, cardW;

    @Inject(method = "extractRenderState", at = @At("TAIL"))
    private void narutominecraft$scroll(GuiGraphicsExtractor g, int mouseX, int mouseY, float delta, CallbackInfo ci) {
        LeafUi.rod(g, boxX - 6, boxY + 1, boxH - 2);
        LeafUi.rod(g, boxX + boxW, boxY + 1, boxH - 2);
        LeafUi.crest(g, cardX + cardW - 13, cardY + 4);
    }
}
