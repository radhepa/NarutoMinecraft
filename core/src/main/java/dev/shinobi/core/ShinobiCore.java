package dev.shinobi.core;

import net.fabricmc.api.ModInitializer;
import net.fabricmc.fabric.api.attachment.v1.AttachmentRegistry;
import net.fabricmc.fabric.api.attachment.v1.AttachmentSyncPredicate;
import net.fabricmc.fabric.api.attachment.v1.AttachmentType;
import net.fabricmc.fabric.api.event.lifecycle.v1.ServerLifecycleEvents;
import net.fabricmc.fabric.api.gamerule.v1.GameRuleBuilder;
import net.minecraft.network.codec.ByteBufCodecs;
import net.minecraft.resources.Identifier;
import net.minecraft.world.level.gamerules.GameRule;
import net.minecraft.world.level.gamerules.GameRuleCategory;
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
    /** Varied (on) or Classic (off, the default), set on Create World's Game Rules screen and fixed in the save seed at the first start. */
    public static final GameRule<Boolean> VARIED_WORLD = GameRuleBuilder.forBoolean(false).category(GameRuleCategory.MISC).buildAndRegister(id("varied_world"));

    static Identifier id(String path) {
        return Identifier.fromNamespaceAndPath(MOD_ID, path);
    }

    @Override
    public void onInitialize() {
        // A new save takes its seed from the world seed; the creation screen will offer a typed seed.
        ServerLifecycleEvents.SERVER_STARTED.register(SaveSeed::of);
        LOG.info("Shinobi Core loaded");
    }
}
