package dev.shinobi.village.mixin;

import com.google.gson.JsonObject;
import dev.shinobi.village.LeafWardrobe;
import dev.villagefriends.outfit.Wardrobe;
import org.spongepowered.asm.mixin.Mixin;
import org.spongepowered.asm.mixin.injection.At;
import org.spongepowered.asm.mixin.injection.Inject;
import org.spongepowered.asm.mixin.injection.callback.CallbackInfoReturnable;

/** VF loads one wardrobe catalog from its own resources; hand it the Leaf catalog instead. */
@Mixin(Wardrobe.class)
abstract class WardrobeMixin {
    @Inject(method = "read", at = @At("RETURN"), cancellable = true)
    private static void narutominecraft$leafCatalog(String path, CallbackInfoReturnable<JsonObject> cir) {
        if (path.equals("catalog.json")) cir.setReturnValue(LeafWardrobe.catalog(cir.getReturnValue()));
    }
}
