package dev.shinobi.progression;

import dev.shinobi.combat.runtime.Spar;
import dev.shinobi.combat.runtime.ShinobiCombat;
import dev.shinobi.life.Daily;
import dev.shinobi.life.ShinobiLife;
import dev.shinobi.village.PlayerLooks;
import dev.shinobi.village.ShinobiVillage;
import dev.shinobi.village.TestStreet;
import net.fabricmc.fabric.api.client.gametest.v1.FabricClientGameTest;
import net.fabricmc.fabric.api.client.gametest.v1.context.ClientGameTestContext;
import net.fabricmc.fabric.api.client.gametest.v1.context.TestSingleplayerContext;
import net.fabricmc.fabric.api.client.gametest.v1.world.TestWorldSave;
import net.minecraft.core.BlockPos;
import net.minecraft.client.gui.screens.inventory.ContainerScreen;
import net.minecraft.client.gui.screens.inventory.CraftingScreen;
import net.minecraft.core.Direction;
import net.minecraft.core.registries.BuiltInRegistries;
import net.minecraft.resources.Identifier;
import net.minecraft.world.entity.ai.attributes.Attributes;
import net.minecraft.world.entity.animal.feline.Cat;
import net.minecraft.world.InteractionHand;
import net.minecraft.world.entity.npc.villager.Villager;
import net.minecraft.world.item.BlockItem;
import net.minecraft.world.item.ItemStack;
import net.minecraft.world.item.Items;
import net.minecraft.world.phys.AABB;
import net.minecraft.world.phys.BlockHitResult;
import net.minecraft.world.phys.EntityHitResult;
import net.minecraft.world.phys.Vec3;

import java.util.List;
import java.util.Map;
import java.util.UUID;
import java.util.concurrent.atomic.AtomicBoolean;
import java.util.stream.Stream;

import static dev.shinobi.progression.ErrandGameTest.check;
import static dev.shinobi.progression.ErrandGameTest.journal;
import static dev.shinobi.progression.ErrandGameTest.ryo;

/**
 * M2, the ten-minute play session (ROADMAP.md 13.4): on the test street a new player makes a character in the creator,
 * which starts the story (StoryGameTest plays it); the training quest, taken by command, names each step; the player walks to the yard, loses a first bout (the quest waits,
 * unpaid), then wins a spar by real attacks (each one taken by the server), earns 30 ryo once, talks to the keeper, finds
 * the furniture shop shut on the first day, a Moonday (ErrandGameTest buys the tatami on a Fireday), places a tatami in flat 3a, sleeps in the flat's bed
 * at nightfall into the next morning (day 2's stipend paid), and reopening keeps the look, the finished quest, the wallet
 * and the furnishing. The rest of the ordinary day (P05): awake at 01:00 the player is tired, a lie-down and up again
 * keeps it, and a night in the bed clears it with day 3's stipend; the flat's chest and crafting table open; a defeat at
 * night wakes the player in the flat without the kunai, fatigue cleared and not back; at 13:00 the keeper's shelter line
 * hands over a tamed kitten; a whole night in the flat's bed from 20:00 leaves the player Well Rested by the flat's comfort
 * (Cosy: until 13:00), and a matcha bought from the keeper once the tea house opens at 09:00 and drunk adds its regen; that tea puts the night's fatigue
 * off to 02:00, a bento halves its slowdown, a weaker dango leaves the stronger platter's regen, 03:00 exhausts the
 * player (damage -20%) and 06:00 collapses them, to wake in the flat at noon; a two-day clock jump pays two stipends,
 * and turning it back none.
 * Screenshots: session-creator, session-spar, session-won, session-furnished, session-asleep, session-reopened,
 * session-chest, session-woke, session-kitten, session-collapsed.
 */
@SuppressWarnings("UnstableApiUsage")
public final class SessionGameTest implements FabricClientGameTest {
    static final String TRAINING = ShinobiProgression.TRAINING;

    @Override
    public void runTest(ClientGameTestContext c) {
        TestWorldSave save;
        BlockPos placed;
        String look;
        try (var w = c.worldBuilder().setUseConsistentSettings(false).create()) {
            w.getConnection().waitForChunksRender();
            for (String cmd : List.of("gamerule spawn_mobs false", "gamerule advance_weather false", "weather clear", "gamerule advance_time true", "time set 3000")) w.getServer().runCommand(cmd);

            // The creator lives in Shinobi Village's client classes, which this test does not compile against.
            c.waitFor(mc -> mc.gui.screen() != null && mc.gui.screen().getClass().getSimpleName().equals("CreatorScreen"));
            c.takeScreenshot("session-creator");
            c.clickScreenButton("Done");
            for (int i = 0; i < 20 && !journal(w).knows(ShinobiProgression.OPENING); i++) c.waitTicks(10);
            check(journal(w).knows(ShinobiProgression.OPENING), "the creator's look starts the story: " + journal(w));
            w.getServer().runCommand("execute as @p run shinobi quest accept " + TRAINING);
            for (int i = 0; i < 20 && !"go_yard".equals(step(w)); i++) c.waitTicks(10);
            check("go_yard".equals(step(w)), "the training quest is taken: " + journal(w));
            look = w.getServer().computeOnServer(s -> w.getConnection().getServerPlayer().getAttached(PlayerLooks.LOOK));

            BlockPos yard = anchors(w).get("anchor:training");
            w.getServer().runOnServer(s -> w.getConnection().getServerPlayer().teleportTo(yard.getX() + .5, yard.getY(), yard.getZ() + 3.5));
            for (int i = 0; i < 20 && partner(w) == null; i++) c.waitTicks(10);
            UUID partner = partner(w);
            check("spar".equals(step(w)) && partner != null, "the yard step done, the spar partner waits: " + journal(w));
            // Real attacks through the client's game mode, a little over the combo's rhythm; the server takes each one.
            w.getServer().runCommand("tp @p " + (yard.getX() + .5) + " " + yard.getY() + " " + (yard.getZ() + 2.5) + " facing entity " + partner + " feet");
            c.waitTicks(20);
            int id = w.getServer().computeOnServer(s -> w.getConnection().getServerLevel().getEntity(partner).getId());
            // P04-6: a bout lost first. One hit starts it, then the player stands in reach and takes the partner's blows;
            // the quest waits at the spar with its reward unpaid, and the next hit is the retry.
            var lost = new AtomicBoolean();
            Spar.LOST.register(p -> lost.set(true));
            c.runOnClient(mc -> mc.gameMode.attack(mc.player, mc.level.getEntity(id)));
            for (int i = 0; i < 300 && !lost.get(); i++) c.waitTicks(10);
            check(lost.get() && "spar".equals(step(w)) && ryo(w) == 100, "a lost spar leaves the quest at the spar, unpaid: " + journal(w) + ", " + ryo(w));
            for (int i = 0; i < 80 && "spar".equals(step(w)); i++) {
                c.runOnClient(mc -> mc.gameMode.attack(mc.player, mc.level.getEntity(id)));
                c.waitTicks(i == 3 ? 1 : 12);
                if (i == 3) c.takeScreenshot("session-spar");
            }
            check("shop".equals(step(w)) && ryo(w) == 130, "the retried spar won pays 30 ryo once: " + journal(w) + ", " + ryo(w));
            c.takeScreenshot("session-won");
            check(w.getServer().computeOnServer(s -> Stream.of("clone", "transformation", "substitution", "release", "rope_escape", "first_aid")
                    .allMatch(t -> ShinobiCombat.knows(w.getConnection().getServerPlayer(), "combat:nin." + t))), "the won spar teaches the six Academy techniques");

            UUID keeper = w.getServer().computeOnServer(s -> w.getConnection().getServerLevel().getAttachedOrElse(ShinobiVillage.ROLES, Map.<String, UUID>of()).get("job:tea_house"));
            for (int i = 0; i < 3 && "shop".equals(step(w)); i++) {
                int k = w.getServer().computeOnServer(s -> {
                    var v = w.getConnection().getServerLevel().getEntity(keeper);
                    w.getConnection().getServerPlayer().teleportTo(v.getX() + 1, v.getY(), v.getZ());
                    return v.getId();
                });
                c.waitTicks(20);
                c.runOnClient(mc -> mc.gameMode.interact(mc.player, mc.level.getEntity(k), new EntityHitResult(mc.level.getEntity(k)), InteractionHand.MAIN_HAND));
                c.waitTicks(10);
            }
            check("furnish".equals(step(w)) && !w.getServer().computeOnServer(s -> ShinobiProgression.buy(w.getConnection().getServerPlayer(), "furniture_shop", "tatami"))
                    && ryo(w) == 130, "talked to the keeper; the furniture shop is shut on a Moonday: " + journal(w) + ", " + ryo(w));
            check(w.getServer().computeOnServer(s -> w.getConnection().getServerPlayer().getInventory().countItem(ShinobiLife.item("tatami"))) == 1,
                    "the keeper hands over the first tatami");

            // The tatami goes on the room's floor through the server's game mode, past the street's protection.
            BlockPos room = anchors(w).get(TestStreet.PLAYER_FLAT);
            placed = room.offset(3, 1, 3);
            w.getServer().runCommand("tp @p " + (room.getX() + 3.5) + " " + (room.getY() + 1) + " " + (room.getZ() + 5.5) + " facing " + (placed.getX() + .5) + " " + placed.getY() + " " + (placed.getZ() + .5));
            c.waitTicks(10);
            var floor = placed.below();
            // Only furnishings go down in the room: dirt beside the tatami's spot is refused.
            check(w.getServer().computeOnServer(s -> {
                var p = w.getConnection().getServerPlayer();
                var dirt = new ItemStack(Items.DIRT);
                p.setItemInHand(InteractionHand.MAIN_HAND, dirt);
                p.gameMode.useItemOn(p, p.level(), dirt, InteractionHand.MAIN_HAND, new BlockHitResult(Vec3.atCenterOf(floor.west()).add(0, .5, 0), Direction.UP, floor.west(), false));
                return p.level().getBlockState(placed.west()).isAir();
            }), "the room refuses a block that is not a furnishing");
            check(w.getServer().computeOnServer(s -> {
                var p = w.getConnection().getServerPlayer();
                var tatami = new ItemStack(ShinobiLife.item("tatami"));
                p.getInventory().removeItem(p.getInventory().findSlotMatchingItem(tatami), 1);
                p.setItemInHand(InteractionHand.MAIN_HAND, tatami);
                return p.gameMode.useItemOn(p, p.level(), tatami, InteractionHand.MAIN_HAND, new BlockHitResult(Vec3.atCenterOf(floor).add(0, .5, 0), Direction.UP, floor, false)).consumesAction();
            }), "the tatami goes down in the room");
            for (int i = 0; i < 10 && !"sleep".equals(step(w)); i++) c.waitTicks(10);
            check("sleep".equals(step(w)) && w.getServer().computeOnServer(s -> w.getConnection().getServerLevel().getBlockState(placed).getBlock() == ((BlockItem) ShinobiLife.item("tatami")).getBlock()),
                    "the furnishing is placed: " + journal(w));
            c.takeScreenshot("session-furnished");

            // Sleep needs full dark; give the sky a few ticks to follow the clock.
            w.getServer().runCommand("time set 18000");
            c.waitTicks(5);
            long before = w.getServer().computeOnServer(s -> w.getConnection().getServerLevel().getOverworldClockTime());
            w.getServer().runOnServer(s -> {
                var p = w.getConnection().getServerPlayer();
                p.teleportTo(room.getX() + 1.5, room.getY() + 1, room.getZ() + 1.5);
                p.gameMode.useItemOn(p, p.level(), ItemStack.EMPTY, InteractionHand.MAIN_HAND, new BlockHitResult(Vec3.atCenterOf(room), Direction.UP, room, false));
            });
            for (int i = 0; i < 10 && !journal(w).done().contains(TRAINING); i++) c.waitTicks(10);
            check(journal(w).done().contains(TRAINING), "the player sleeps in the flat's bed at night, which ends the quest: " + journal(w));
            c.takeScreenshot("session-asleep");
            for (int i = 0; i < 30 && w.getServer().computeOnServer(s -> w.getConnection().getServerPlayer().isSleeping()); i++) c.waitTicks(10);
            long after = w.getServer().computeOnServer(s -> w.getConnection().getServerLevel().getOverworldClockTime());
            check(after / 24000 > before / 24000, "the night passes: " + before + " to " + after);
            for (int i = 0; i < 10 && ryo(w) != 160; i++) c.waitTicks(10);
            check(ryo(w) == 160 && w.getServer().computeOnServer(s -> Daily.day(s.overworld()) == 2 && "Fireday".equals(Daily.weekday(s.overworld()))),
                    "day 2, a Fireday, pays the 30 ryo stipend: " + ryo(w));
            save = w.getWorldSave();
        }
        try (var w = save.open()) {
            w.getConnection().waitForChunksRender();
            c.waitTicks(40);
            check(look.equals(w.getServer().computeOnServer(s -> w.getConnection().getServerPlayer().getAttached(PlayerLooks.LOOK)))
                    && journal(w).done().contains(TRAINING) && !journal(w).active().containsKey(TRAINING) && ryo(w) == 160
                    && w.getServer().computeOnServer(s -> w.getConnection().getServerLevel().getBlockState(placed).getBlock() == ((BlockItem) ShinobiLife.item("tatami")).getBlock())
                    && c.computeOnClient(mc -> mc.gui.screen() == null), "reopening keeps the look, the quest, the wallet and the tatami: " + journal(w) + ", " + ryo(w));
            c.takeScreenshot("session-reopened");

            // The rest of the ordinary day: up at 01:00 the player is tired; the flat's bed clears it, and day 3 pays again.
            w.getServer().runCommand("time add 19000");
            for (int i = 0; i < 10 && !tired(w); i++) c.waitTicks(10);
            check(tired(w) && slow(w) == -.1 && regen(w) == .75, "a night awake makes the player tired: " + slow(w) + ", " + regen(w));
            BlockPos room = anchors(w).get(TestStreet.PLAYER_FLAT);
            // Lying down and getting straight up is no night's sleep: the player stays tired.
            check(w.getServer().computeOnServer(s -> {
                var p = w.getConnection().getServerPlayer();
                p.teleportTo(room.getX() + 1.5, room.getY() + 1, room.getZ() + 1.5);
                p.gameMode.useItemOn(p, p.level(), ItemStack.EMPTY, InteractionHand.MAIN_HAND, new BlockHitResult(Vec3.atCenterOf(room), Direction.UP, room, false));
                boolean lay = p.isSleeping();
                p.stopSleepInBed(true, true);
                return lay;
            }), "the player lies down in the flat's bed");
            c.waitTicks(30);
            check(tired(w), "a lie-down and up again leaves the player tired");
            w.getServer().runOnServer(s -> {
                var p = w.getConnection().getServerPlayer();
                p.gameMode.useItemOn(p, p.level(), ItemStack.EMPTY, InteractionHand.MAIN_HAND, new BlockHitResult(Vec3.atCenterOf(room), Direction.UP, room, false));
            });
            for (int i = 0; i < 40 && (tired(w) || ryo(w) != 190); i++) c.waitTicks(10);
            check(!tired(w) && ryo(w) == 190 && slow(w) == 0 && w.getServer().computeOnServer(s -> Daily.day(s.overworld()) == 3),
                    "sleeping clears the fatigue and day 3 pays the stipend: " + ryo(w));

            // The flat's chest and crafting table open, even with a block in hand.
            for (var spot : List.of(TestStreet.FLAT_CHEST, TestStreet.FLAT_TABLE)) {
                BlockPos at = room.offset(spot);
                w.getServer().runOnServer(s -> {
                    var p = w.getConnection().getServerPlayer();
                    p.teleportTo(at.getX() + .5, room.getY() + 1, at.getZ() + 2.5);
                    p.setItemInHand(InteractionHand.MAIN_HAND, new ItemStack(Items.DIRT));
                });
                c.waitTicks(10);
                c.runOnClient(mc -> mc.gameMode.useItemOn(mc.player, InteractionHand.MAIN_HAND, new BlockHitResult(Vec3.atCenterOf(at), Direction.SOUTH, at, false)));
                c.waitFor(mc -> spot == TestStreet.FLAT_CHEST ? mc.gui.screen() instanceof ContainerScreen : mc.gui.screen() instanceof CraftingScreen);
                if (spot == TestStreet.FLAT_CHEST) c.takeScreenshot("session-chest");
                c.runOnClient(mc -> mc.player.closeContainer());
            }

            // A defeat at 01:30, tired: the player wakes in the flat, fatigue cleared for the night, and loses the thrown
            // tools carried, nothing else (no bill).
            w.getServer().runCommand("time set 67500");
            for (int i = 0; i < 10 && !tired(w); i++) c.waitTicks(10);
            check(tired(w), "awake at 01:30 on day 3, the player is tired");
            var kunai = BuiltInRegistries.ITEM.getValue(Identifier.fromNamespaceAndPath("shinobi_combat", "practice_kunai"));
            w.getServer().runOnServer(s -> {
                var p = w.getConnection().getServerPlayer();
                p.getInventory().add(new ItemStack(kunai, 4));
                p.teleportTo(TestStreet.SPAWN.getX() + .5, TestStreet.SPAWN.getY(), TestStreet.SPAWN.getZ() + .5);
            });
            w.getServer().runCommand("gamerule immediate_respawn true");
            w.getServer().runCommand("kill @p");
            for (int i = 0; i < 20 && !w.getServer().computeOnServer(s -> TestStreet.inPlayerRoom(s.overworld(), w.getConnection().getServerPlayer().blockPosition())); i++) c.waitTicks(10);
            c.waitTicks(40);
            check(w.getServer().computeOnServer(s -> {
                var p = w.getConnection().getServerPlayer();
                return p.isAlive() && TestStreet.inPlayerRoom(s.overworld(), p.blockPosition()) && p.getInventory().countItem(kunai) == 0 && p.getInventory().countItem(Items.DIRT) == 1;
            }) && ryo(w) == 190 && !tired(w), "a defeated player wakes in the flat, fatigue cleared, with the pack but no kunai: " + ryo(w));
            c.takeScreenshot("session-woke");

            // Adoption: at 13:00, with the shelter open (9 to 17), the keeper's shelter line hands over a kitten, tamed by the player, for 40 ryo.
            w.getServer().runCommand("time set 55000");
            UUID keeper = w.getServer().computeOnServer(s -> s.overworld().getAttachedOrElse(ShinobiVillage.ROLES, Map.<String, UUID>of()).get("job:tea_house"));
            check(w.getServer().computeOnServer(s -> {
                var p = w.getConnection().getServerPlayer();
                var v = s.overworld().getEntity(keeper);
                p.teleportTo(v.getX() + 1, v.getY(), v.getZ());
                return ShinobiProgression.buy(p, "cat_shelter", "service.adoption.cat");
            }) && ryo(w) == 150, "the kitten costs 40 ryo: " + ryo(w));
            check(w.getServer().computeOnServer(s -> {
                var p = w.getConnection().getServerPlayer();
                return p.level().getEntitiesOfClass(Cat.class, new AABB(p.blockPosition()).inflate(4), cat -> cat.isTame() && cat.isOwnedBy(p) && cat.isBaby()).size() == 1;
            }), "a tamed kitten owned by the player stands beside them");
            c.waitTicks(20);
            c.takeScreenshot("session-kitten");

            // Rest stages: lain down in the flat's bed at 20:00 on day 3, the player wakes on day 4 Well Rested (regen +10%).
            w.getServer().runCommand("time set 62000");
            c.waitTicks(5);
            w.getServer().runOnServer(s -> {
                var p = w.getConnection().getServerPlayer();
                p.teleportTo(room.getX() + 1.5, room.getY() + 1, room.getZ() + 1.5);
                p.gameMode.useItemOn(p, p.level(), ItemStack.EMPTY, InteractionHand.MAIN_HAND, new BlockHitResult(Vec3.atCenterOf(room), Direction.UP, room, false));
            });
            for (int i = 0; i < 40 && !w.getServer().computeOnServer(s -> Daily.wellRested(w.getConnection().getServerPlayer())); i++) c.waitTicks(10);
            for (int i = 0; i < 10 && ryo(w) != 180; i++) c.waitTicks(10);
            check(w.getServer().computeOnServer(s -> Daily.wellRested(w.getConnection().getServerPlayer()) && Daily.day(s.overworld()) == 4
                    && Daily.rest(w.getConnection().getServerPlayer()).rested() == 72000 + 7000)
                    && Math.abs(regen(w) - 1.1) < 1e-9 && ryo(w) == 180, "a whole night in the Cosy flat's bed leaves the player Well Rested until 13:00: " + regen(w) + ", " + ryo(w));

            // A dish: at 09:30, the tea house open, a matcha bought from the keeper and drunk (the use key held) adds its +10% chakra regen.
            w.getServer().runCommand("time set 75500");
            var matcha = ShinobiLife.item("matcha");
            int price = ShinobiLife.price("tea_house", "matcha");
            check(price > 0 && w.getServer().computeOnServer(s -> {
                var p = w.getConnection().getServerPlayer();
                var v = s.overworld().getEntity(keeper);
                p.teleportTo(v.getX() + 1, v.getY(), v.getZ());
                if (!ShinobiProgression.buy(p, "tea_house", "matcha")) return false;
                var inv = p.getInventory();
                int slot = inv.findSlotMatchingItem(new ItemStack(matcha));
                var cup = inv.getItem(slot).copy();
                inv.setItem(slot, ItemStack.EMPTY);
                p.setItemInHand(InteractionHand.MAIN_HAND, cup);
                return true;
            }) && ryo(w) == 180 - price, "the keeper sells a matcha at its catalogue price: " + price + ", " + ryo(w));
            w.getServer().runCommand("tp @p ~ ~ ~ 0 -90");
            c.waitTicks(10);
            c.getInput().holdKeyFor(o -> o.keyUse, 50);
            for (int i = 0; i < 20 && regen(w) < 1.15; i++) c.waitTicks(10);
            check(Math.abs(regen(w) - 1.2) < 1e-9 && w.getServer().computeOnServer(s -> w.getConnection().getServerPlayer().getInventory().countItem(matcha) == 0),
                    "drinking the matcha adds its regen to Well Rested's: " + regen(w));

            // Fatigue by the clock on day 4's night: the matcha is a tea, so 01:00 comes at 02:00.
            w.getServer().runCommand("time set 91500");
            c.waitTicks(40);
            check(!tired(w), "the morning's tea keeps the player fresh at 01:30");
            w.getServer().runCommand("time set 92000");
            for (int i = 0; i < 10 && !tired(w); i++) c.waitTicks(10);
            check(tired(w) && slow(w) == -.1, "tired at 02:00, an hour late for the tea: " + slow(w));
            // A bento halves the slowdown; a dango's +20% does not replace the stronger platter's +25%.
            w.getServer().runOnServer(s -> {
                var p = w.getConnection().getServerPlayer();
                for (String dish : List.of("bento", "dango_platter", "dango")) new ItemStack(ShinobiLife.item(dish)).finishUsingItem(p.level(), p);
            });
            c.waitTicks(30);
            check(slow(w) == -.05 && Math.abs(regen(w) - .75 * 1.25) < 1e-9, "a meal halves the slowdown and the strongest dish's regen stays: " + slow(w) + ", " + regen(w));
            w.getServer().runCommand("time set 93000");
            for (int i = 0; i < 10 && !exhausted(w); i++) c.waitTicks(10);
            check(exhausted(w) && slow(w) == -.1 && weak(w) == -.2 && Math.abs(regen(w) - .5 * 1.25) < 1e-9,
                    "03:00 exhausts the player (movement -20%, halved by the meal; damage -20%; regen halved): " + slow(w) + ", " + weak(w) + ", " + regen(w));
            w.getServer().runOnServer(s -> w.getConnection().getServerPlayer().teleportTo(TestStreet.SPAWN.getX() + .5, TestStreet.SPAWN.getY(), TestStreet.SPAWN.getZ() + .5));
            c.waitTicks(10);
            w.getServer().runCommand("time set 96000");
            for (int i = 0; i < 10 && tired(w); i++) c.waitTicks(10);
            check(!tired(w) && slow(w) == 0 && weak(w) == 0 && w.getServer().computeOnServer(s -> {
                var p = w.getConnection().getServerPlayer();
                return p.isAlive() && TestStreet.inPlayerRoom(s.overworld(), p.blockPosition()) && s.overworld().getOverworldClockTime() / 1000 == 102;
            }), "06:00 still awake collapses the player, who wakes in the flat at noon");
            c.waitTicks(20);
            c.takeScreenshot("session-collapsed");

            // A clock jumped two days pays both mornings; moved back, it pays nothing.
            int purse = ryo(w);
            w.getServer().runCommand("time add 48000");
            for (int i = 0; i < 10 && ryo(w) != purse + 60; i++) c.waitTicks(10);
            w.getServer().runCommand("time set 3000");
            c.waitTicks(40);
            check(ryo(w) == purse + 60, "a two-day jump pays two stipends, and moving the clock back none: " + ryo(w));
        }
    }

    static String step(TestSingleplayerContext w) { return journal(w).active().get(TRAINING); }

    static boolean tired(TestSingleplayerContext w) { return w.getServer().computeOnServer(s -> Daily.tired(w.getConnection().getServerPlayer())); }

    static boolean exhausted(TestSingleplayerContext w) { return w.getServer().computeOnServer(s -> Daily.exhausted(w.getConnection().getServerPlayer())); }

    /** Fatigue's damage modifier on the player (-0.2 for -20%), 0 without one. */
    static double weak(TestSingleplayerContext w) {
        return w.getServer().computeOnServer(s -> {
            var m = w.getConnection().getServerPlayer().getAttribute(Attributes.ATTACK_DAMAGE).getModifier(Daily.FATIGUE);
            return m == null ? 0 : m.amount();
        });
    }

    static double regen(TestSingleplayerContext w) { return w.getServer().computeOnServer(s -> ShinobiCombat.regen.applyAsDouble(w.getConnection().getServerPlayer())); }

    /** Fatigue's movement modifier on the player (-0.1 for -10%), 0 without one. */
    static double slow(TestSingleplayerContext w) {
        return w.getServer().computeOnServer(s -> {
            var m = w.getConnection().getServerPlayer().getAttribute(Attributes.MOVEMENT_SPEED).getModifier(Daily.FATIGUE);
            return m == null ? 0 : m.amount();
        });
    }

    static Map<String, BlockPos> anchors(TestSingleplayerContext w) {
        return w.getServer().computeOnServer(s -> w.getConnection().getServerLevel().getAttachedOrElse(ShinobiVillage.ANCHORS, Map.of()));
    }

    static UUID partner(TestSingleplayerContext w) {
        return w.getServer().computeOnServer(s -> {
            var p = w.getConnection().getServerPlayer();
            return p.level().getEntitiesOfClass(Villager.class, new AABB(p.blockPosition()).inflate(16), v -> v.entityTags().contains(Spar.PARTNER))
                    .stream().findFirst().map(Villager::getUUID).orElse(null);
        });
    }
}
