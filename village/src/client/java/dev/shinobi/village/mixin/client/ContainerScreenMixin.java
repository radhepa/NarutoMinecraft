package dev.shinobi.village.mixin.client;

import dev.shinobi.village.client.LeafUi;
import net.minecraft.client.gui.GuiGraphicsExtractor;
import net.minecraft.client.gui.screens.inventory.AbstractContainerScreen;
import net.minecraft.client.gui.screens.inventory.ContainerScreen;
import net.minecraft.network.chat.Component;
import net.minecraft.world.entity.player.Inventory;
import net.minecraft.world.inventory.ChestMenu;
import org.spongepowered.asm.mixin.Mixin;
import org.spongepowered.asm.mixin.injection.At;
import org.spongepowered.asm.mixin.injection.Inject;
import org.spongepowered.asm.mixin.injection.callback.CallbackInfo;

/** A shop window (Shinobi Life's ShopMenu) is drawn as the Leaf shop counter over the chest texture. */
@Mixin(ContainerScreen.class)
abstract class ContainerScreenMixin extends AbstractContainerScreen<ChestMenu> {
    private ContainerScreenMixin(ChestMenu menu, Inventory inventory, Component title) { super(menu, inventory, title); }

    @Inject(method = "extractBackground", at = @At("TAIL"))
    private void narutominecraft$counter(GuiGraphicsExtractor g, int mouseX, int mouseY, float delta, CallbackInfo ci) {
        if (!LeafUi.shop(title)) return;
        LeafUi.counter(g, leftPos, topPos, imageWidth, imageHeight, menu.getRowCount() * 18 + 21,
                menu.slots.stream().map(s -> new int[]{s.x, s.y}).toList());
    }
}
