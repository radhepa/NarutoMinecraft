package dev.shinobi.village.client;

import dev.shinobi.village.PlayerLooks;
import net.fabricmc.api.ClientModInitializer;
import net.fabricmc.fabric.api.client.event.lifecycle.v1.ClientTickEvents;
import net.fabricmc.fabric.api.client.networking.v1.ClientPlayConnectionEvents;
import net.fabricmc.fabric.api.client.networking.v1.ClientPlayNetworking;

/** Shinobi Village's client: the creator on first join and the player's look as their skin. */
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
    }
}
