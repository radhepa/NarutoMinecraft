package dev.shinobi.combat.runtime;

import dev.shinobi.combat.CombatData;
import net.fabricmc.api.ModInitializer;
import net.fabricmc.fabric.api.event.lifecycle.v1.ServerTickEvents;
import net.fabricmc.fabric.api.event.player.AttackEntityCallback;
import net.fabricmc.fabric.api.networking.v1.ServerPlayConnectionEvents;
import net.fabricmc.loader.api.FabricLoader;
import net.minecraft.server.level.ServerPlayer;
import net.minecraft.world.InteractionResult;
import net.minecraft.world.entity.Mob;

/** Shinobi Combat's entrypoint: the combat data from data/combat and the practice spar. */
public final class ShinobiCombat implements ModInitializer {
    public static final String MOD_ID = "shinobi_combat";
    public static CombatData data;

    @Override
    public void onInitialize() {
        data = new CombatData(FabricLoader.getInstance().getModContainer(MOD_ID).orElseThrow().findPath("data/shinobi_combat/combat").orElseThrow());
        // The client fires this too, with no tags synced: it passes there and the attack reaches the server, which takes it over.
        AttackEntityCallback.EVENT.register((player, level, hand, entity, hit) -> {
            if (!(player instanceof ServerPlayer p) || p.isSpectator() || !(entity instanceof Mob partner) || !entity.entityTags().contains(Spar.PARTNER)) return InteractionResult.PASS;
            Spar.attack(p, partner);
            return InteractionResult.SUCCESS;
        });
        ServerTickEvents.END_SERVER_TICK.register(Spar::tick);
        ServerPlayConnectionEvents.DISCONNECT.register((handler, server) -> Spar.end(handler.getPlayer()));
    }
}
