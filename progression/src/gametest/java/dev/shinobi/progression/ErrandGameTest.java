package dev.shinobi.progression;

import dev.shinobi.life.ShinobiLife;
import dev.shinobi.life.ShopMenu;
import dev.shinobi.village.PlayerLooks;
import dev.shinobi.village.ShinobiVillage;
import net.fabricmc.fabric.api.client.gametest.v1.FabricClientGameTest;
import net.fabricmc.fabric.api.client.gametest.v1.context.ClientGameTestContext;
import net.fabricmc.fabric.api.client.gametest.v1.context.TestSingleplayerContext;
import net.fabricmc.fabric.api.client.gametest.v1.world.TestWorldSave;
import net.minecraft.client.gui.screens.inventory.ContainerScreen;
import net.minecraft.core.BlockPos;
import net.minecraft.world.InteractionHand;
import net.minecraft.world.entity.animal.feline.Cat;
import net.minecraft.world.entity.item.ItemEntity;
import net.minecraft.world.inventory.ContainerInput;
import net.minecraft.world.item.Item;
import net.minecraft.world.item.ItemStack;
import net.minecraft.world.item.Items;
import net.minecraft.world.phys.AABB;
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
 * P04-4/5: the errand pays 20 ryo once on top of the first day's 100; nothing is sold away from the keeper; reopening
 * keeps the wallet and the goods, with no second payout.
 * P05 shops: at 09:00 on a Moonday using the keeper opens the shop screen on their open shops only (tea house, grocer, weapon shop, Academy supply,
 * shelter; not Ichiraku before 11:00 or the furniture shop on a Moonday); clicks buy a tea and the grocer's six bentos
 * (wallet and stock drop, the goods in the pack), then a seventh is refused sold out and a kitten refused with 26 ryo;
 * at noon a full pack is refused, then an Ichiraku ramen is bought from its seller; at 05:00, every shop shut, the keeper
 * opens no screen; the next morning the bentos are back and a tatami is bought; reopening keeps the shelf's sales, and a
 * week on the furniture shop's weekly lines are full again.
 * P04-6: a step whose anchor the map has lost is blocked, not crashed, and opens again with the anchor back; a cast
 * saved without a slot the quest declares is cast again.
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
            w.getServer().runCommand("execute as @p run shinobi quest accept " + ShinobiProgression.TRAINING);
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

            // P05: the shop screen at 09:00 on a Moonday, the first day.
            openShop(c, w, keeper);
            c.takeScreenshot("shop-screen");
            var ids = w.getServer().computeOnServer(s -> offers(w));
            check(ids.containsAll(List.of("green_tea", "bento", "service.adoption.cat", "practice_kunai", "smoke_powder", "steel_wire")) && !ids.contains("shio_ramen") && !ids.contains("tatami"),
                    "the screen lists the keeper's open shops only: " + ids);
            check(w.getServer().computeOnServer(s -> List.of("smoke_bomb", "ninja_wire").stream().allMatch(r -> s.getRecipeManager().byKey(net.minecraft.resources.ResourceKey.create(
                    net.minecraft.core.registries.Registries.RECIPE, net.minecraft.resources.Identifier.fromNamespaceAndPath("shinobi_combat", r))).isPresent())), "smoke bombs and wire craft from the supply counter's materials");
            click(c, w, "green_tea");
            check(ryo(w) == 116 && count(w, ShinobiLife.item("green_tea")) == 1, "a tea bought on the screen: " + ryo(w));
            click(c, w, "bento");
            check(ryo(w) == 101 && count(w, ShinobiLife.item("bento")) == 1 && left(w, "grocer", "bento") == 5, "a bento: wallet and stock drop: " + ryo(w));
            for (int i = 0; i < 5; i++) click(c, w, "bento");
            check(ryo(w) == 26 && count(w, ShinobiLife.item("bento")) == 6 && left(w, "grocer", "bento") == 0, "the day's six bentos: " + ryo(w));
            click(c, w, "bento");
            check(ryo(w) == 26 && count(w, ShinobiLife.item("bento")) == 6, "a seventh bento is refused, sold out");
            // Nothing leaves the window or goes into it: shift-click, number keys and F, Q, clone, and a shift-click and double-click from the pack.
            int line = offers(w).indexOf("bento"), pack = w.getServer().computeOnServer(s -> {
                var m = w.getConnection().getServerPlayer().containerMenu;
                return m.slots.indexOf(m.slots.stream().filter(sl -> sl.container != ((ShopMenu) m).getContainer() && sl.getItem().is(ShinobiLife.item("bento"))).findFirst().orElseThrow());
            });
            for (var in : List.of(new Object[]{line, 0, ContainerInput.QUICK_MOVE}, new Object[]{line, 0, ContainerInput.SWAP}, new Object[]{line, 40, ContainerInput.SWAP},
                    new Object[]{line, 0, ContainerInput.THROW}, new Object[]{line, 2, ContainerInput.CLONE}, new Object[]{line, 0, ContainerInput.PICKUP_ALL},
                    new Object[]{pack, 0, ContainerInput.QUICK_MOVE}, new Object[]{pack, 0, ContainerInput.PICKUP}, new Object[]{pack, 0, ContainerInput.PICKUP_ALL},
                    new Object[]{pack, 0, ContainerInput.PICKUP}))
                c.runOnClient(mc -> mc.gameMode.handleContainerInput(mc.player.containerMenu.containerId, (int) in[0], (int) in[1], (ContainerInput) in[2], mc.player));
            c.waitTicks(5);
            check(ryo(w) == 26 && count(w, ShinobiLife.item("bento")) == 6 && left(w, "grocer", "bento") == 0 && w.getServer().computeOnServer(s -> {
                var p = w.getConnection().getServerPlayer();
                return p.containerMenu.getCarried().isEmpty() && p.getOffhandItem().isEmpty() && p.containerMenu.getSlot(line).getItem().is(ShinobiLife.item("bento"))
                        && p.level().getEntitiesOfClass(ItemEntity.class, new AABB(p.blockPosition()).inflate(8)).isEmpty();
            }), "no input takes a line from the window or puts a pack item into it");
            click(c, w, "service.adoption.cat");
            check(ryo(w) == 26 && w.getServer().computeOnServer(s -> w.getConnection().getServerLevel().getEntitiesOfClass(Cat.class,
                    new AABB(w.getConnection().getServerPlayer().blockPosition()).inflate(8)).isEmpty()), "a 40-ryo kitten is refused with 26 ryo");
            check(!w.getServer().computeOnServer(s -> ShinobiProgression.buy(w.getConnection().getServerPlayer(), "furniture_shop", "tatami"))
                    && !w.getServer().computeOnServer(s -> ShinobiProgression.buy(w.getConnection().getServerPlayer(), "ichiraku", "shio_ramen"))
                    && !w.getServer().computeOnServer(s -> ShinobiProgression.buy(w.getConnection().getServerPlayer(), "tea_house", "matcha_powder")) && ryo(w) == 26,
                    "shut shops (the furniture shop on a Moonday, Ichiraku before 11:00) and a line with no item yet are refused");
            c.runOnClient(mc -> mc.player.closeContainer());

            // Noon: Ichiraku is open. A full pack is refused first; with room, a ramen comes from its seller.
            w.getServer().runCommand("time set 6000");
            // The street's residents set off for lunch: give the server a moment to catch up.
            c.waitTicks(100);
            openShop(c, w, keeper);
            w.getServer().runOnServer(s -> {
                var inv = w.getConnection().getServerPlayer().getInventory();
                for (int i = 0; i < 36; i++) if (inv.getItem(i).isEmpty()) inv.setItem(i, new ItemStack(Items.DIRT, 64));
            });
            click(c, w, "shio_ramen");
            check(ryo(w) == 26 && count(w, ShinobiLife.item("shio_ramen")) == 0, "a full pack is refused");
            w.getServer().runOnServer(s -> {
                var inv = w.getConnection().getServerPlayer().getInventory();
                for (int i = 0; i < 36; i++) if (inv.getItem(i).is(Items.DIRT)) inv.setItem(i, ItemStack.EMPTY);
            });
            click(c, w, "shio_ramen");
            check(ryo(w) == 16 && count(w, ShinobiLife.item("shio_ramen")) == 1, "an Ichiraku ramen bought from its seller: " + ryo(w));
            c.runOnClient(mc -> mc.player.closeContainer());
            for (int i = 0; i < 10 && w.getServer().computeOnServer(s -> w.getConnection().getServerPlayer().containerMenu instanceof ShopMenu); i++) c.waitTicks(5);

            // 05:00: every shop the keeper keeps is shut; a polite line, no screen.
            w.getServer().runCommand("time set 23000");
            check(!w.getServer().computeOnServer(s -> ShinobiProgression.offer(w.getConnection().getServerPlayer(), s.overworld().getEntity(keeper))),
                    "a shut shop is refused");
            check(w.getServer().computeOnServer(s -> !(w.getConnection().getServerPlayer().containerMenu instanceof ShopMenu)), "a shut shop opens no screen");

            // The next morning, a Fireday: the grocer's daily bentos are back, and the furniture shop opens.
            w.getServer().runCommand("time set 27000");
            for (int i = 0; i < 10 && ryo(w) != 46; i++) c.waitTicks(10);
            check(ryo(w) == 46 && left(w, "grocer", "bento") == 6, "day 2's stipend, and the bentos restocked: " + ryo(w));
            check(w.getServer().computeOnServer(s -> ShinobiProgression.buy(w.getConnection().getServerPlayer(), "furniture_shop", "tatami"))
                    && ryo(w) == 6 && left(w, "furniture_shop", "tatami") == 15, "a tatami for 40 ryo on a Fireday, one of the week's 16: " + ryo(w));
            // Twelve shops' lines fit the 45-line window on a day the furniture shop is open too.
            openShop(c, w, keeper);
            var fireday = offers(w);
            check(fireday.containsAll(List.of("practice_kunai", "smoke_powder", "service.adoption.cat", "tatami")), "every shop's lines on a Fireday (" + fireday.size() + "): " + fireday);
            c.runOnClient(mc -> mc.player.closeContainer());
            save = w.getWorldSave();
        }
        try (var w = save.open()) {
            w.getConnection().waitForChunksRender();
            check(journal(w).done().contains(ERRAND) && !journal(w).active().containsKey(ERRAND)
                    && journal(w).flags().stream().filter(f -> f.startsWith("test.")).toList().equals(List.of("test.errand.keeper_asked", "test.errand.board_read")), "the journal after reopening: " + journal(w));
            c.waitTicks(20);
            check(ryo(w) == 6 && count(w, ShinobiLife.item("green_tea")) == 1 && count(w, ShinobiLife.item("tatami")) == 1
                    && count(w, ShinobiLife.item("bento")) == 6 && count(w, ShinobiLife.item("shio_ramen")) == 1,
                    "the wallet and goods after reopening, with no second payout: " + ryo(w));
            check(left(w, "furniture_shop", "tatami") == 15, "the shelf's sales survive reopening");
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
            // A cast saved before the quest declared its yard slot is cast again, not blocked for good.
            w.getServer().runOnServer(s -> {
                var p = w.getConnection().getServerPlayer();
                var cast = new HashMap<>(p.getAttachedOrCreate(ShinobiProgression.JOURNAL).castOf(training));
                cast.remove("yard");
                p.setAttached(ShinobiProgression.JOURNAL, p.getAttachedOrCreate(ShinobiProgression.JOURNAL).recast(training, cast));
            });
            c.waitTicks(20);
            check(blocked(w, training) == null && journal(w).castOf(training).containsKey("yard"), "a cast without a slot is cast again: " + journal(w));

            // A week on (day 8, a Moonday), the furniture shop's weekly lines are full again.
            w.getServer().runCommand("time set 171000");
            for (int i = 0; i < 10 && ryo(w) != 186; i++) c.waitTicks(10);
            check(ryo(w) == 186 && left(w, "furniture_shop", "tatami") == 16, "the weekly restock: " + ryo(w));
        }
    }

    /** Uses the keeper through the client until the server has the shop screen open (a click can be dropped under load, or the keeper walk on). */
    static void openShop(ClientGameTestContext c, TestSingleplayerContext w, UUID keeper) {
        for (int i = 0; i < 6 && !w.getServer().computeOnServer(s -> w.getConnection().getServerPlayer().containerMenu instanceof ShopMenu); i++) {
            int id = w.getServer().computeOnServer(s -> {
                var v = w.getConnection().getServerLevel().getEntity(keeper);
                w.getConnection().getServerPlayer().teleportTo(v.getX() + 1, v.getY(), v.getZ());
                return v.getId();
            });
            c.waitTicks(20);
            c.runOnClient(mc -> mc.gameMode.interact(mc.player, mc.level.getEntity(id), new EntityHitResult(mc.level.getEntity(id)), InteractionHand.MAIN_HAND));
            c.waitTicks(10);
        }
        c.waitFor(mc -> mc.gui.screen() instanceof ContainerScreen);
        check(w.getServer().computeOnServer(s -> w.getConnection().getServerPlayer().containerMenu instanceof ShopMenu), "using the keeper opens the shop screen");
    }

    /** The ids of the open shop screen's lines (server side). */
    static List<String> offers(TestSingleplayerContext w) {
        return w.getServer().computeOnServer(s -> w.getConnection().getServerPlayer().containerMenu instanceof ShopMenu m
                ? m.offers().stream().map(ShopMenu.Offer::id).toList() : List.<String>of());
    }

    /** Clicks a line of the open shop screen through the client, as a player does. */
    static void click(ClientGameTestContext c, TestSingleplayerContext w, String id) {
        int slot = offers(w).indexOf(id);
        check(slot >= 0, "the shop screen lists " + id + ": " + offers(w));
        c.runOnClient(mc -> mc.gameMode.handleContainerInput(mc.player.containerMenu.containerId, slot, 0, ContainerInput.PICKUP, mc.player));
        c.waitTicks(5);
    }

    /** What a shop has left today of a line on its shelf; -1 if it is not on the shelf. */
    static int left(TestSingleplayerContext w, String shop, String item) {
        return w.getServer().computeOnServer(s -> {
            var p = w.getConnection().getServerPlayer();
            return ShinobiLife.shelf(p, shop).stream().filter(l -> l.item().equals(item)).findFirst().map(l -> ShinobiLife.left(p.level(), shop, l)).orElse(-1);
        });
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
