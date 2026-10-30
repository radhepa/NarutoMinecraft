package dev.shinobi.village.mixin.client;

import dev.villagefriends.client.ResidentModel;
import dev.villagefriends.client.ResidentRenderState;
import org.spongepowered.asm.mixin.Mixin;
import org.spongepowered.asm.mixin.gen.Invoker;

/** VF's face animation (blinks, eye style, brows), for the player's face planes. */
@Mixin(ResidentModel.class)
public interface ResidentModelAccess {
    @Invoker("animateFace")
    void narutominecraft$animateFace(ResidentRenderState state);
}
