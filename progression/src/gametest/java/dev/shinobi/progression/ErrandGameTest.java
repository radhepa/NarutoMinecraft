package dev.shinobi.progression;

import dev.shinobi.village.ShinobiVillage;
import dev.shinobi.village.TestStreet;
import net.fabricmc.fabric.api.client.gametest.v1.FabricClientGameTest;
import net.fabricmc.fabric.api.client.gametest.v1.context.ClientGameTestContext;
import net.fabricmc.fabric.api.client.gametest.v1.context.TestSingleplayerContext;
import net.fabricmc.fabric.api.client.gametest.v1.world.TestWorldSave;
import net.minecraft.client.gui.screens.worldselection.WorldCreationUiState;
import net.minecraft.core.BlockPos;
import net.minecraft.core.registries.Registries;
import net.minecraft.world.level.levelgen.presets.WorldPresets;

import java.util.List;
import java.util.Map;

/**
 * P04-1: a player accepts the test errand, walks to the training yard and completes it; the journal survives reopening
 * the save with the street's anchors, and a done quest cannot be taken again.
 */
@SuppressWarnings("UnstableApiUsage")
public final class ErrandGameTest implements FabricClientGameTest {
    static final String ERRAND = "errand.test.yard";

    @Override
    public void runTest(ClientGameTestContext c) {
        TestWorldSave save;
        try (var w = c.worldBuilder().adjustSettings(ui -> {
            var flat = ui.getSettings().worldgenLoadContext().lookupOrThrow(Registries.WORLD_PRESET).getOrThrow(WorldPresets.FLAT);
            ui.setWorldType(new WorldCreationUiState.WorldTypeEntry(flat));
            ui.setGenerateStructures(false);
        }).create()) {
            w.getConnection().waitForChunksRender();
            for (String cmd : List.of("gamerule advance_time false", "gamerule spawn_mobs false", "time set 3000"))
                w.getServer().runCommand(cmd);
            BlockPos player = w.getServer().computeOnServer(s -> w.getConnection().getServerPlayer().blockPosition());
            var built = w.getServer().computeOnServer(s -> TestStreet.build(w.getConnection().getServerLevel(), player.below().offset(-17, 0, -22)));
            check(w.getServer().computeOnServer(s -> ShinobiProgression.QUESTS.containsKey(ERRAND)), "the test errand loads from the data pack");

            w.getServer().runCommand("execute as @p run shinobi quest accept " + ERRAND);
            check(journal(w).active().equals(Map.of(ERRAND, "go_yard")), "accepted, at its first step: " + journal(w));

            BlockPos yard = built.anchors().get("anchor:training");
            w.getServer().runCommand("tp @p " + yard.getX() + " " + yard.getY() + " " + (yard.getZ() + 1));
            for (int i = 0; i < 20 && !journal(w).done().contains(ERRAND); i++) c.waitTicks(10);
            check(journal(w).done().contains(ERRAND) && journal(w).active().isEmpty(), "done at the yard: " + journal(w));
            check(!w.getServer().computeOnServer(s -> ShinobiProgression.accept(w.getConnection().getServerPlayer(), ERRAND)), "taken once");
            save = w.getWorldSave();
        }
        try (var w = save.open()) {
            w.getConnection().waitForChunksRender();
            check(journal(w).done().equals(List.of(ERRAND)) && journal(w).active().isEmpty(), "the journal after reopening: " + journal(w));
            check(w.getServer().computeOnServer(s -> w.getConnection().getServerLevel().getAttachedOrElse(ShinobiVillage.ANCHORS, Map.of()).containsKey("anchor:training")),
                    "the street's anchors after reopening");
        }
    }

    static Journal journal(TestSingleplayerContext w) {
        return w.getServer().computeOnServer(s -> w.getConnection().getServerPlayer().getAttachedOrCreate(ShinobiProgression.JOURNAL));
    }

    static void check(boolean ok, String what) {
        if (!ok) throw new AssertionError("Failed: " + what);
    }
}
