package dev.shinobi.core;

import net.fabricmc.api.ModInitializer;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

/** Shinobi Core's entrypoint. The shared contracts (ROADMAP.md, "Code by mod") arrive with their first callers. */
public final class ShinobiCore implements ModInitializer {
    public static final String MOD_ID = "shinobi_core";
    public static final Logger LOG = LoggerFactory.getLogger("Shinobi Core");

    @Override
    public void onInitialize() {
        LOG.info("Shinobi Core loaded");
    }
}
