package dev.shinobi.village.client;

import dev.shinobi.village.PlayerLooks;
import net.fabricmc.api.ClientModInitializer;
import net.fabricmc.fabric.api.client.event.lifecycle.v1.ClientTickEvents;
import net.fabricmc.fabric.api.client.networking.v1.ClientPlayConnectionEvents;
import net.fabricmc.fabric.api.client.networking.v1.ClientPlayNetworking;
import net.fabricmc.fabric.api.client.rendering.v1.LivingEntityRenderLayerRegistrationCallback;
import net.minecraft.client.model.player.PlayerModel;
import net.minecraft.client.renderer.entity.RenderLayerParent;
import net.minecraft.client.renderer.entity.player.AvatarRenderer;
import net.minecraft.client.renderer.entity.state.AvatarRenderState;

/** Shinobi Village's client: the creator on first join and the player's look as their skin and face. */
public final class VillageClient implements ClientModInitializer {
    private static int waited;

    @Override
    public void onInitializeClient() {
        // The look syncs a moment after joining; open the creator every two seconds while the player has none and the server takes one.
        ClientTickEvents.END_CLIENT_TICK.register(mc -> {
            if (mc.player == null) waited = 0;
            else if (mc.gui.screen() == null && !mc.player.hasAttached(PlayerLooks.LOOK)
                    && ClientPlayNetworking.canSend(PlayerLooks.SetLook.TYPE) && ++waited % 40 == 0) mc.setScreenAndShow(new CreatorScreen());
        });
        ClientPlayConnectionEvents.DISCONNECT.register((handler, mc) -> mc.execute(PlayerSkins::clear));
        LivingEntityRenderLayerRegistrationCallback.EVENT.register((type, renderer, helper, context) -> {
            if (renderer instanceof AvatarRenderer<?>) helper.register(new PlayerEyes(face(renderer)));
        });
    }

    @SuppressWarnings("unchecked")
    private static RenderLayerParent<AvatarRenderState, PlayerModel> face(Object renderer) {
        return (RenderLayerParent<AvatarRenderState, PlayerModel>) renderer;
    }
}
