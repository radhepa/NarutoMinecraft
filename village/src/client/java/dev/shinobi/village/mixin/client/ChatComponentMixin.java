package dev.shinobi.village.mixin.client;

import dev.shinobi.village.client.LeafChat;
import net.minecraft.client.gui.components.ChatComponent;
import net.minecraft.client.multiplayer.chat.GuiMessage;
import org.spongepowered.asm.mixin.Final;
import org.spongepowered.asm.mixin.Mixin;
import org.spongepowered.asm.mixin.Shadow;
import org.spongepowered.asm.mixin.injection.At;
import org.spongepowered.asm.mixin.injection.Inject;
import org.spongepowered.asm.mixin.injection.callback.CallbackInfo;

import java.util.List;
import java.util.function.Predicate;

/**
 * Swaps Minecraft's chat for the Leaf message scroll. Drawing and the chat screen's click and hover capture share this
 * one method, so both follow LeafChat's layout.
 */
@Mixin(ChatComponent.class)
abstract class ChatComponentMixin {
    @Shadow @Final private List<GuiMessage> allMessages;
    @Shadow private int chatScrollbarPos;
    @Shadow private Predicate<GuiMessage> visibleMessageFilter;

    @Shadow private double getScale() { throw new AssertionError(); }
    @Shadow private int getWidth() { throw new AssertionError(); }
    @Shadow public abstract int getLinesPerPage();
    @Shadow public abstract boolean isChatFocused();

    @Inject(method = "extractRenderState(Lnet/minecraft/client/gui/components/ChatComponent$ChatGraphicsAccess;IILnet/minecraft/client/gui/components/ChatComponent$DisplayMode;)V",
            at = @At("HEAD"), cancellable = true)
    private void narutominecraft$leafScroll(ChatComponent.ChatGraphicsAccess g, int guiHeight, int tick, ChatComponent.DisplayMode mode, CallbackInfo ci) {
        ci.cancel();
        if (!mode.foreground && isChatFocused()) return;
        float scale = (float) getScale();
        LeafChat.draw(g, guiHeight, tick, mode, allMessages, visibleMessageFilter, chatScrollbarPos, scale, (int) Math.ceil(getWidth() / scale), getLinesPerPage());
    }
}
