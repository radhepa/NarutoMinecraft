package dev.shinobi.core;

import net.fabricmc.fabric.api.client.gametest.v1.FabricClientGameTest;
import net.fabricmc.fabric.api.client.gametest.v1.context.ClientGameTestContext;
import net.fabricmc.loader.api.FabricLoader;

/** The P01 launch check: the real client loads Shinobi Core with Fabric API, opens a world and saves a screenshot. */
@SuppressWarnings("UnstableApiUsage")
public final class LaunchGameTest implements FabricClientGameTest {
    @Override
    public void runTest(ClientGameTestContext c) {
        for (String id : new String[] {ShinobiCore.MOD_ID, "fabric-api", "minecraft"}) {
            if (FabricLoader.getInstance().getModContainer(id).isEmpty()) throw new AssertionError("Not loaded: " + id);
        }
        c.takeScreenshot("core_title");
        try (var w = c.worldBuilder().create()) {
            w.getConnection().waitForChunksRender();
            c.takeScreenshot("core_world");
        }
    }
}
