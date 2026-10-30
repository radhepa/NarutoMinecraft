package dev.shinobi.core;

import net.fabricmc.api.ModInitializer;
import net.fabricmc.fabric.api.attachment.v1.AttachmentRegistry;
import net.fabricmc.fabric.api.attachment.v1.AttachmentSyncPredicate;
import net.fabricmc.fabric.api.attachment.v1.AttachmentType;
import net.fabricmc.fabric.api.event.lifecycle.v1.ServerLifecycleEvents;
import net.minecraft.network.codec.ByteBufCodecs;
import net.minecraft.resources.Identifier;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

/** Shinobi Core's entrypoint. The shared contracts (ROADMAP.md, "Code by mod") arrive with their first callers. */
@SuppressWarnings("UnstableApiUsage")
public final class ShinobiCore implements ModInitializer {
    public static final String MOD_ID = "shinobi_core";
    public static final Logger LOG = LoggerFactory.getLogger("Shinobi Core");

    /** The player's record, saved with the player, kept through death and synced to its owner (ROADMAP.md, "Saves"). */
    public static final AttachmentType<PlayerRecord> PLAYER = AttachmentRegistry.create(id("player"),
            b -> b.persistent(PlayerRecord.CODEC).copyOnDeath().initializer(() -> PlayerRecord.NEW)
                    .syncWith(ByteBufCodecs.fromCodec(PlayerRecord.CODEC), AttachmentSyncPredicate.targetOnly()));
    /** The save seed, saved with the overworld. */
    public static final AttachmentType<SaveSeed> SEED = AttachmentRegistry.create(id("save_seed"),
            b -> b.persistent(SaveSeed.CODEC));

    static Identifier id(String path) {
        return Identifier.fromNamespaceAndPath(MOD_ID, path);
    }

    @Override
    public void onInitialize() {
        // A new save takes its seed from the world seed in Classic mode; the creation screen will offer a typed seed and Varied.
        ServerLifecycleEvents.SERVER_STARTED.register(s ->
                s.overworld().getAttachedOrCreate(SEED, () -> new SaveSeed(s.overworld().getSeed(), "classic")));
        LOG.info("Shinobi Core loaded");
    }
}
