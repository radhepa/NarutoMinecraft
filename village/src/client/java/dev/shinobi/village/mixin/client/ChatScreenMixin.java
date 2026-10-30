package dev.shinobi.village.mixin.client;

import dev.shinobi.village.client.LeafUi;
import net.minecraft.client.gui.GuiGraphicsExtractor;
import net.minecraft.client.gui.screens.ChatScreen;
import net.minecraft.client.gui.screens.Screen;
import net.minecraft.network.chat.Component;
import org.spongepowered.asm.mixin.Mixin;
import org.spongepowered.asm.mixin.injection.At;
import org.spongepowered.asm.mixin.injection.Inject;
import org.spongepowered.asm.mixin.injection.callback.CallbackInfo;

/** The chat input as a wooden writing bar with a "Speak" plate, under the Leaf message scroll. */
@Mixin(ChatScreen.class)
abstract class ChatScreenMixin extends Screen {
    private static final Component SPEAK = Component.translatable("narutominecraft.chat.speak");

    private ChatScreenMixin() { super(null); }

    @Inject(method = "extractRenderState(Lnet/minecraft/client/gui/GuiGraphicsExtractor;IIF)V", at = @At("HEAD"))
    private void narutominecraft$writingBar(GuiGraphicsExtractor g, int mouseX, int mouseY, float delta, CallbackInfo ci) {
        int w = font.width(SPEAK) + 10;
        g.fill(0, height - 17, width, height, LeafUi.WOOD);
        g.fill(0, height - 17, width, height - 16, LeafUi.ORANGE);
        g.fill(2, height - 28, 2 + w, height - 17, LeafUi.ORANGE);
        g.fill(2, height - 18, 2 + w, height - 17, LeafUi.DEEP);
        LeafUi.crest(g, width - 12, height - 27);
        g.text(font, SPEAK, 7, height - 26, LeafUi.INK, false);
    }
}
