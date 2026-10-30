package dev.shinobi.village.mixin.client;

import com.mojang.renderpearl.api.pipeline.RenderPipeline;
import dev.shinobi.village.client.LeafUi;
import net.minecraft.client.gui.Font;
import net.minecraft.client.gui.GuiGraphicsExtractor;
import net.minecraft.util.FormattedCharSequence;
import org.spongepowered.asm.mixin.Mixin;
import org.spongepowered.asm.mixin.Shadow;
import org.spongepowered.asm.mixin.injection.At;
import org.spongepowered.asm.mixin.injection.Inject;
import org.spongepowered.asm.mixin.injection.ModifyVariable;
import org.spongepowered.asm.mixin.injection.callback.CallbackInfo;

/** Every fill and text colour of the Leaf-skinned screens and the chat input passes through LeafUi (the two funnels all others call). */
@Mixin(GuiGraphicsExtractor.class)
abstract class GuiGraphicsExtractorMixin {
    @Shadow public abstract void fill(RenderPipeline pipeline, int x0, int y0, int x1, int y1, int color);

    @ModifyVariable(method = "fill(Lcom/mojang/renderpearl/api/pipeline/RenderPipeline;IIIII)V", at = @At("HEAD"), argsOnly = true, ordinal = 4)
    private int narutominecraft$fill(int color) { return LeafUi.fill(color); }

    /** The chat input's leaf-green box gets an orange scroll edge. */
    @Inject(method = "fill(Lcom/mojang/renderpearl/api/pipeline/RenderPipeline;IIIII)V", at = @At("TAIL"))
    private void narutominecraft$edge(RenderPipeline pipeline, int x0, int y0, int x1, int y1, int color, CallbackInfo ci) {
        if ((color & 0xFFFFFF) == LeafUi.CHAT) fill(pipeline, x0, y0, Math.min(x1, x0 + 2), y1, color & 0xFF000000 | LeafUi.ORANGE & 0xFFFFFF);
    }

    @ModifyVariable(method = "text(Lnet/minecraft/client/gui/Font;Lnet/minecraft/util/FormattedCharSequence;IIIZ)V", at = @At("HEAD"), argsOnly = true, ordinal = 2)
    private int narutominecraft$text(int color) { return LeafUi.text(color); }
}
