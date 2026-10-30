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
import net.minecraft.world.InteractionHand;
import net.minecraft.world.level.levelgen.presets.WorldPresets;
import net.minecraft.world.phys.EntityHitResult;

import java.util.List;
import java.util.Map;
import java.util.UUID;

/**
 * P04-1: a player accepts the test errand, walks to the training yard and completes it; the journal survives reopening
 * the save with the street's anchors, and a done quest cannot be taken again.
 * P04-2: the errand casts the tea house keeper and the yard from the map; the player talks to the keeper by using them;
 * a quest whose anchor the map lacks is refused, and the bound residents survive reopening.
 * P04-3: asking the keeper sets a flag, so the yard step branches to the notice board; the flags survive reopening.
 */
@SuppressWarnings("UnstableApiUsage")
public final class ErrandGameTest implements FabricClientGameTest {
    static final String ERRAND = "errand.test.yard", MISSING = "errand.test.missing";

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

            check(!w.getServer().computeOnServer(s -> ShinobiProgression.accept(w.getConnection().getServerPlayer(), MISSING)) && !journal(w).knows(MISSING),
                    "a quest whose anchor the map lacks is refused");
            w.getServer().runCommand("execute as @p run shinobi quest accept " + ERRAND);
            UUID keeper = w.getServer().computeOnServer(s -> w.getConnection().getServerLevel().getAttachedOrElse(ShinobiVillage.ROLES, Map.<String, UUID>of()).get("job:tea_house"));
            check(journal(w).active().equals(Map.of(ERRAND, "ask_keeper")) && journal(w).castOf(ERRAND).equals(Map.of("keeper", keeper.toString(), "yard", "anchor:training")),
                    "accepted at its first step, cast on the map: " + journal(w));

            // Using the keeper through the client's game mode: the interaction packet reaches the server's callback.
            // Retried: under load the server can drop a click sent before it has the teleport (out of reach).
            for (int i = 0; i < 3 && !journal(w).active().equals(Map.of(ERRAND, "go_yard")); i++) {
                int id = w.getServer().computeOnServer(s -> {
                    var v = w.getConnection().getServerLevel().getEntity(keeper);
                    w.getConnection().getServerPlayer().teleportTo(v.getX() + 1, v.getY(), v.getZ());
                    return v.getId();
                });
                c.waitTicks(20);
                c.runOnClient(mc -> {
                    var v = mc.level.getEntity(id);
                    mc.gameMode.interact(mc.player, v, new EntityHitResult(v), InteractionHand.MAIN_HAND);
                });
                c.waitTicks(10);
            }
            check(journal(w).active().equals(Map.of(ERRAND, "go_yard")), "talked to the keeper: " + journal(w));

            BlockPos yard = built.anchors().get("anchor:training");
            w.getServer().runCommand("tp @p " + yard.getX() + " " + yard.getY() + " " + (yard.getZ() + 1));
            for (int i = 0; i < 20 && !journal(w).active().equals(Map.of(ERRAND, "go_board")); i++) c.waitTicks(10);
            check(journal(w).active().equals(Map.of(ERRAND, "go_board")), "the keeper's flag takes the branch to the board: " + journal(w));
            BlockPos board = built.anchors().get("notice_board");
            w.getServer().runCommand("tp @p " + board.getX() + " " + board.getY() + " " + (board.getZ() + 1));
            for (int i = 0; i < 20 && !journal(w).done().contains(ERRAND); i++) c.waitTicks(10);
            check(journal(w).done().contains(ERRAND) && journal(w).active().isEmpty(), "done at the board: " + journal(w));
            check(!w.getServer().computeOnServer(s -> ShinobiProgression.accept(w.getConnection().getServerPlayer(), ERRAND)), "taken once");
            save = w.getWorldSave();
        }
        try (var w = save.open()) {
            w.getConnection().waitForChunksRender();
            check(journal(w).done().equals(List.of(ERRAND)) && journal(w).active().isEmpty()
                    && journal(w).flags().equals(List.of("test.errand.keeper_asked", "test.errand.board_read")), "the journal after reopening: " + journal(w));
            check(w.getServer().computeOnServer(s -> w.getConnection().getServerLevel().getAttachedOrElse(ShinobiVillage.ANCHORS, Map.of()).containsKey("anchor:training")
                    && w.getConnection().getServerLevel().getAttachedOrElse(ShinobiVillage.ROLES, Map.of()).containsKey("job:tea_house")), "the street's anchors and roles after reopening");
        }
    }

    static Journal journal(TestSingleplayerContext w) {
        return w.getServer().computeOnServer(s -> w.getConnection().getServerPlayer().getAttachedOrCreate(ShinobiProgression.JOURNAL));
    }

    static void check(boolean ok, String what) {
        if (!ok) throw new AssertionError("Failed: " + what);
    }
}
