package dev.shinobi.progression;

import dev.shinobi.life.ShinobiLife;
import dev.shinobi.village.PlayerLooks;
import dev.shinobi.village.ShinobiVillage;
import net.fabricmc.fabric.api.client.gametest.v1.FabricClientGameTest;
import net.fabricmc.fabric.api.client.gametest.v1.context.ClientGameTestContext;
import net.fabricmc.fabric.api.client.gametest.v1.context.TestSingleplayerContext;
import net.fabricmc.fabric.api.client.gametest.v1.world.TestWorldSave;
import net.minecraft.core.BlockPos;
import net.minecraft.world.InteractionHand;
import net.minecraft.world.item.Item;
import net.minecraft.world.phys.EntityHitResult;

import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.UUID;

/**
 * P04-1: a player accepts the test errand, walks to the training yard and completes it; the journal survives reopening
 * the save with the street's anchors, and a done quest cannot be taken again.
 * P04-2: the errand casts the tea house keeper and the yard from the map; the player talks to the keeper by using them;
 * a quest whose anchor the map lacks is refused, and the bound residents survive reopening.
 * P04-3: asking the keeper sets a flag, so the yard step branches to the notice board; the flags survive reopening.
 * P04-4/5: the errand pays 20 ryo once on top of the first day's 100; by the keeper the player buys tea (by the shop's
 * command) and a tatami, is refused what the wallet cannot cover and anything away from the keeper; reopening keeps
 * the wallet and the goods, with no second payout.
 * P04-6: a step whose anchor the map has lost is blocked, not crashed, and opens again with the anchor back.
 */
@SuppressWarnings("UnstableApiUsage")
public final class ErrandGameTest implements FabricClientGameTest {
    static final String ERRAND = "errand.test.yard", MISSING = "errand.test.missing";

    @Override
    public void runTest(ClientGameTestContext c) {
        TestWorldSave save;
        try (var w = c.worldBuilder().setUseConsistentSettings(false).create()) {
            w.getConnection().waitForChunksRender();
            // The creator is P05's; here the player takes the opening look.
            check(w.getServer().computeOnServer(s -> PlayerLooks.choose(w.getConnection().getServerPlayer(), PlayerLooks.defaultLook())), "the opening look is allowed");
            for (String cmd : List.of("gamerule advance_time false", "gamerule advance_weather false", "weather clear", "gamerule spawn_mobs false", "time set 3000"))
                w.getServer().runCommand(cmd);
            // The new world's map, pasted at its first start.
            var anchors = w.getServer().computeOnServer(s -> w.getConnection().getServerLevel().getAttachedOrElse(ShinobiVillage.ANCHORS, Map.<String, BlockPos>of()));
            check(w.getServer().computeOnServer(s -> ShinobiProgression.QUESTS.containsKey(ERRAND)), "the test errand loads from the data pack");

            check(!w.getServer().computeOnServer(s -> ShinobiProgression.accept(w.getConnection().getServerPlayer(), MISSING)) && !journal(w).knows(MISSING),
                    "a quest whose anchor the map lacks is refused");
            w.getServer().runCommand("execute as @p run shinobi quest accept " + ERRAND);
            UUID keeper = w.getServer().computeOnServer(s -> w.getConnection().getServerLevel().getAttachedOrElse(ShinobiVillage.ROLES, Map.<String, UUID>of()).get("job:tea_house"));
            check("ask_keeper".equals(journal(w).active().get(ERRAND)) && journal(w).castOf(ERRAND).equals(Map.of("keeper", keeper.toString(), "yard", "anchor:training")),
                    "accepted at its first step, cast on the map: " + journal(w));

            // Using the keeper through the client's game mode: the interaction packet reaches the server's callback.
            // Retried: under load the server can drop a click sent before it has the teleport (out of reach).
            for (int i = 0; i < 3 && !"go_yard".equals(journal(w).active().get(ERRAND)); i++) {
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
            check("go_yard".equals(journal(w).active().get(ERRAND)), "talked to the keeper: " + journal(w));

            BlockPos yard = anchors.get("anchor:training");
            w.getServer().runCommand("tp @p " + yard.getX() + " " + yard.getY() + " " + (yard.getZ() + 1));
            for (int i = 0; i < 20 && !"go_board".equals(journal(w).active().get(ERRAND)); i++) c.waitTicks(10);
            check("go_board".equals(journal(w).active().get(ERRAND)), "the keeper's flag takes the branch to the board: " + journal(w));
            BlockPos board = anchors.get("notice_board");
            w.getServer().runCommand("tp @p " + board.getX() + " " + board.getY() + " " + (board.getZ() + 1));
            for (int i = 0; i < 20 && !journal(w).done().contains(ERRAND); i++) c.waitTicks(10);
            check(journal(w).done().contains(ERRAND) && !journal(w).active().containsKey(ERRAND), "done at the board: " + journal(w));
            check(!w.getServer().computeOnServer(s -> ShinobiProgression.accept(w.getConnection().getServerPlayer(), ERRAND)), "taken once");
            check(ryo(w) == 120, "the errand pays 20 ryo on the first day's 100: " + ryo(w));

            check(!buy(w, "green_tea"), "no trade away from the keeper");
            w.getServer().runOnServer(s -> {
                var v = w.getConnection().getServerLevel().getEntity(keeper);
                w.getConnection().getServerPlayer().teleportTo(v.getX() + 1, v.getY(), v.getZ());
            });
            c.waitTicks(5);
            w.getServer().runCommand("execute as @p run shinobi buy tea_house green_tea");
            check(ryo(w) == 116 && count(w, ShinobiLife.item("green_tea")) == 1, "tea bought by the shop's command: " + ryo(w));
            check(w.getServer().computeOnServer(s -> ShinobiProgression.buy(w.getConnection().getServerPlayer(), "furniture_shop", "tatami")) && ryo(w) == 76,
                    "a tatami for 40 ryo: " + ryo(w));
            check(!w.getServer().computeOnServer(s -> ShinobiProgression.buy(w.getConnection().getServerPlayer(), "furniture_shop", "shoji_screen")) && ryo(w) == 76,
                    "a screen for 80 ryo is refused with 76");
            check(!w.getServer().computeOnServer(s -> ShinobiProgression.buy(w.getConnection().getServerPlayer(), "tea_house", "matcha")) && ryo(w) == 76,
                    "a line with no item yet is refused");
            save = w.getWorldSave();
        }
        try (var w = save.open()) {
            w.getConnection().waitForChunksRender();
            check(journal(w).done().equals(List.of(ERRAND)) && !journal(w).active().containsKey(ERRAND)
                    && journal(w).flags().equals(List.of("test.errand.keeper_asked", "test.errand.board_read")), "the journal after reopening: " + journal(w));
            c.waitTicks(20);
            check(ryo(w) == 76 && count(w, ShinobiLife.item("green_tea")) == 1 && count(w, ShinobiLife.item("tatami")) == 1,
                    "the wallet and goods after reopening, with no second payout: " + ryo(w));
            check(w.getServer().computeOnServer(s -> w.getConnection().getServerLevel().getAttachedOrElse(ShinobiVillage.ANCHORS, Map.of()).containsKey("anchor:training")
                    && w.getConnection().getServerLevel().getAttachedOrElse(ShinobiVillage.ROLES, Map.of()).containsKey("job:tea_house")), "the street's anchors and roles after reopening");

            // P04-6: the training quest, at its spar since the yard visit, waits blocked once the map loses the yard; back with it.
            String training = ShinobiProgression.TRAINING;
            check("spar".equals(journal(w).active().get(training)), "the training quest waits at the spar: " + journal(w));
            var full = w.getServer().computeOnServer(s -> w.getConnection().getServerLevel().getAttachedOrElse(ShinobiVillage.ANCHORS, Map.<String, BlockPos>of()));
            var less = new HashMap<>(full);
            less.remove("anchor:training");
            w.getServer().runOnServer(s -> w.getConnection().getServerLevel().setAttached(ShinobiVillage.ANCHORS, Map.copyOf(less)));
            c.waitTicks(20);
            check("anchor slot:yard (anchor:training)".equals(blocked(w, training)) && "spar".equals(journal(w).active().get(training)),
                    "a step whose anchor is gone is blocked, without a crash: " + blocked(w, training));
            w.getServer().runOnServer(s -> w.getConnection().getServerLevel().setAttached(ShinobiVillage.ANCHORS, full));
            c.waitTicks(20);
            check(blocked(w, training) == null && "spar".equals(journal(w).active().get(training)), "the anchor back, the step is open again");
        }
    }

    static Journal journal(TestSingleplayerContext w) {
        return w.getServer().computeOnServer(s -> w.getConnection().getServerPlayer().getAttachedOrCreate(ShinobiProgression.JOURNAL));
    }

    static String blocked(TestSingleplayerContext w, String quest) {
        return w.getServer().computeOnServer(s -> ShinobiProgression.blocked(w.getConnection().getServerPlayer(), quest));
    }

    static int ryo(TestSingleplayerContext w) {
        return w.getServer().computeOnServer(s -> ShinobiLife.ryo(w.getConnection().getServerPlayer()));
    }

    static boolean buy(TestSingleplayerContext w, String item) {
        return w.getServer().computeOnServer(s -> ShinobiProgression.buy(w.getConnection().getServerPlayer(), "tea_house", item));
    }

    static int count(TestSingleplayerContext w, Item item) {
        return w.getServer().computeOnServer(s -> w.getConnection().getServerPlayer().getInventory().countItem(item));
    }

    static void check(boolean ok, String what) {
        if (!ok) throw new AssertionError("Failed: " + what);
    }
}
