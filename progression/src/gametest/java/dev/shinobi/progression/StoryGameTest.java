package dev.shinobi.progression;

import dev.shinobi.combat.runtime.ShinobiCombat;
import dev.shinobi.core.SaveSeed;
import dev.shinobi.core.ShinobiCore;
import dev.shinobi.life.ShinobiLife;
import dev.shinobi.village.ShinobiVillage;
import dev.shinobi.village.TestStreet;
import net.fabricmc.fabric.api.client.gametest.v1.FabricClientGameTest;
import net.fabricmc.fabric.api.client.gametest.v1.context.ClientGameTestContext;
import net.fabricmc.fabric.api.client.gametest.v1.context.TestSingleplayerContext;
import net.fabricmc.fabric.api.client.gametest.v1.world.TestWorldSave;
import net.fabricmc.fabric.api.client.message.v1.ClientReceiveMessageEvents;
import net.minecraft.core.BlockPos;
import net.minecraft.core.Direction;
import net.minecraft.network.chat.ClickEvent;
import net.minecraft.network.chat.Component;
import net.minecraft.network.chat.contents.TranslatableContents;
import net.minecraft.world.InteractionHand;
import net.minecraft.world.item.BlockItem;
import net.minecraft.world.item.ItemStack;
import net.minecraft.world.phys.BlockHitResult;
import net.minecraft.world.phys.EntityHitResult;
import net.minecraft.world.phys.Vec3;

import java.util.List;
import java.util.Map;
import java.util.UUID;
import java.util.concurrent.CopyOnWriteArrayList;
import java.util.stream.Stream;

import static dev.shinobi.progression.ErrandGameTest.check;
import static dev.shinobi.progression.ErrandGameTest.journal;
import static dev.shinobi.progression.SessionGameTest.anchors;
import static dev.shinobi.progression.SessionGameTest.partner;

/**
 * P07, the opening (chapters 0 to 2) played with no developer commands, each choice taken by the link the client
 * receives in chat: a new player makes a character, which starts chapter 0; its scenes are said line by line and its
 * three choices set their answers and branches; chapter 1 starts itself, the player walks to flat 3a, the world is
 * closed and reopened at the porter's question (the question is shown again), places the porter's tatami, sleeps,
 * orders at the ramen stand, walks to the Academy yard and introduces themself; chapter 2 starts, the player wins the
 * spar (which teaches the six Academy techniques) and the rival's line reads the introduction. A Varied world plays
 * chapter 0 with other answers into chapter 1.
 * Screenshots: story-choice, story-ramen, story-rival.
 */
@SuppressWarnings("UnstableApiUsage")
public final class StoryGameTest implements FabricClientGameTest {
    static final List<Component> CHAT = new CopyOnWriteArrayList<>();

    @Override
    public void runTest(ClientGameTestContext c) {
        ClientReceiveMessageEvents.GAME.register((message, overlay) -> CHAT.add(message));
        TestWorldSave save;
        try (var w = c.worldBuilder().setUseConsistentSettings(false).create()) {
            begin(c, w);
            pick(c, w, "story.ch0", "cell_reply", "find");
            c.takeScreenshot("story-choice");
            pick(c, w, "story.ch0", "freed_boy", "free");
            pick(c, w, "story.ch0", "raid_reply", "point");
            for (int i = 0; i < 100 && !journal(w).done().contains("story.ch0"); i++) c.waitTicks(5);
            check(journal(w).done().contains("story.ch0") && journal(w).knows("story.ch1")
                    && journal(w).flags().containsAll(List.of("ans.lost_child.cell.find", "ans.player.ch0.freed_boy.free", "ans.sensei.ch0.point", "story.seed.watcher", "doc.ledger_sample")),
                    "chapter 0 sets its answers and seeds, then starts chapter 1: " + journal(w));
            check(said("story.ch0.boy.1") && said("story.ch0.tunnel.1") && said("story.ch0.watcher.2"), "the freed boy's and the tunnel's lines are said");

            pick(c, w, "story.ch1", "want", "hokage");
            for (int i = 0; i < 40 && !"go_flat".equals(step(w, "story.ch1")); i++) c.waitTicks(5);
            BlockPos room = anchors(w).get(TestStreet.PLAYER_FLAT);
            w.getServer().runOnServer(s -> w.getConnection().getServerPlayer().teleportTo(room.getX() + 2.5, room.getY() + 1, room.getZ() + 2.5));
            for (int i = 0; i < 60 && !"porter_reply".equals(step(w, "story.ch1")); i++) c.waitTicks(5);
            check("porter_reply".equals(step(w, "story.ch1")), "the flat reached, the porter's scene plays: " + journal(w));
            save = w.getWorldSave();
        }
        CHAT.clear();
        try (var w = save.open()) {
            w.getConnection().waitForChunksRender();
            // Reopened at a choice: the porter's question is asked again.
            pick(c, w, "story.ch1", "porter_reply", "asked");
            for (int i = 0; i < 40 && !"furnish".equals(step(w, "story.ch1")); i++) c.waitTicks(5);
            check("furnish".equals(step(w, "story.ch1")) && said("story.ch1.porter.name")
                    && w.getServer().computeOnServer(s -> w.getConnection().getServerPlayer().getInventory().countItem(ShinobiLife.item("tatami"))) == 1,
                    "asked his name, the porter hesitates and leaves a tatami: " + journal(w));

            BlockPos room = anchors(w).get(TestStreet.PLAYER_FLAT), floor = room.offset(3, 0, 3);
            check(w.getServer().computeOnServer(s -> {
                var p = w.getConnection().getServerPlayer();
                var tatami = new ItemStack(ShinobiLife.item("tatami"));
                p.getInventory().removeItem(p.getInventory().findSlotMatchingItem(tatami), 1);
                p.setItemInHand(InteractionHand.MAIN_HAND, tatami);
                return p.gameMode.useItemOn(p, p.level(), tatami, InteractionHand.MAIN_HAND, new BlockHitResult(Vec3.atCenterOf(floor).add(0, .5, 0), Direction.UP, floor, false)).consumesAction()
                        && p.level().getBlockState(floor.above()).getBlock() == ((BlockItem) ShinobiLife.item("tatami")).getBlock();
            }), "the tatami goes down in the room");
            for (int i = 0; i < 20 && !"sleep".equals(step(w, "story.ch1")); i++) c.waitTicks(5);
            w.getServer().runCommand("time set 18000");
            c.waitTicks(5);
            w.getServer().runOnServer(s -> {
                var p = w.getConnection().getServerPlayer();
                p.teleportTo(room.getX() + 1.5, room.getY() + 1, room.getZ() + 1.5);
                p.gameMode.useItemOn(p, p.level(), ItemStack.EMPTY, InteractionHand.MAIN_HAND, new BlockHitResult(Vec3.atCenterOf(room), Direction.UP, room, false));
            });
            for (int i = 0; i < 60 && !"ramen".equals(step(w, "story.ch1")); i++) c.waitTicks(5);
            check("ramen".equals(step(w, "story.ch1")), "a night in the flat's bed, then breakfast: " + journal(w));
            for (int i = 0; i < 30 && w.getServer().computeOnServer(s -> w.getConnection().getServerPlayer().isSleeping()); i++) c.waitTicks(10);

            UUID keeper = w.getServer().computeOnServer(s -> w.getConnection().getServerLevel().getAttachedOrElse(ShinobiVillage.ROLES, Map.<String, UUID>of()).get("job:tea_house"));
            for (int i = 0; i < 3 && "ramen".equals(step(w, "story.ch1")); i++) {
                int k = w.getServer().computeOnServer(s -> {
                    var v = w.getConnection().getServerLevel().getEntity(keeper);
                    w.getConnection().getServerPlayer().teleportTo(v.getX() + 1, v.getY(), v.getZ());
                    return v.getId();
                });
                c.waitTicks(20);
                c.runOnClient(mc -> mc.gameMode.interact(mc.player, mc.level.getEntity(k), new EntityHitResult(mc.level.getEntity(k)), InteractionHand.MAIN_HAND));
                c.waitTicks(10);
            }
            c.runOnClient(mc -> { if (mc.player.containerMenu != mc.player.inventoryMenu) mc.player.closeContainer(); });
            pick(c, w, "story.ch1", "order", "salt");
            c.takeScreenshot("story-ramen");

            BlockPos yard = anchors(w).get("anchor:training");
            for (int i = 0; i < 40 && !"go_academy".equals(step(w, "story.ch1")); i++) c.waitTicks(5);
            w.getServer().runOnServer(s -> w.getConnection().getServerPlayer().teleportTo(yard.getX() + .5, yard.getY(), yard.getZ() + 3.5));
            pick(c, w, "story.ch1", "intro", "nowhere");
            for (int i = 0; i < 40 && !journal(w).knows("story.ch2"); i++) c.waitTicks(5);
            check(journal(w).done().contains("story.ch1") && journal(w).flags().containsAll(List.of("ans.hokage_4.want.hokage", "ans.porter.met.asked", "ans.player.ramen.salt", "ans.player.intro.nowhere")),
                    "chapter 1 done with its answers, chapter 2 started: " + journal(w));

            // The rival's spar: real attacks through the client's game mode, as SessionGameTest wins it.
            for (int i = 0; i < 60 && (!"spar".equals(step(w, "story.ch2")) || partner(w) == null); i++) c.waitTicks(5);
            UUID rival = partner(w);
            check("spar".equals(step(w, "story.ch2")) && rival != null, "the forms said, the spar partner waits: " + journal(w));
            w.getServer().runCommand("tp @p " + (yard.getX() + .5) + " " + yard.getY() + " " + (yard.getZ() + 2.5) + " facing entity " + rival + " feet");
            c.waitTicks(20);
            int id = w.getServer().computeOnServer(s -> w.getConnection().getServerLevel().getEntity(rival).getId());
            for (int i = 0; i < 80 && "spar".equals(step(w, "story.ch2")); i++) {
                c.runOnClient(mc -> mc.gameMode.attack(mc.player, mc.level.getEntity(id)));
                c.waitTicks(12);
            }
            pick(c, w, "story.ch2", "fall", "truth");
            for (int i = 0; i < 40 && !journal(w).done().contains("story.ch2"); i++) c.waitTicks(5);
            check(journal(w).done().contains("story.ch2") && journal(w).knows("story.ch3") && said("story.ch2.pump.nowhere") && !said("story.ch2.pump.joke") && said("story.ch2.fall.truth"),
                    "the rival's line reads the introduction, chapter 2 ends and chapter 3 starts: " + journal(w));
            // shortcut: chapters 3 to 7 (the techniques, the exam, Genin) are checked by missions.py only, until their client run.
            for (int i = 0; i < 60 && !"sign".equals(step(w, "story.ch3")); i++) c.waitTicks(5);
            check(w.getServer().computeOnServer(s -> Stream.of("release", "rope_escape", "first_aid")
                    .allMatch(t -> ShinobiCombat.knows(w.getConnection().getServerPlayer(), "combat:nin." + t))), "chapter 3's leaf teaches the first three techniques: " + journal(w));
            c.takeScreenshot("story-rival");
        }

        // Varied: the same opening on a rolled cast, with the other answers.
        CHAT.clear();
        try (var w = c.worldBuilder().setUseConsistentSettings(false).adjustSettings(ui -> {
            ui.setSeed("7");
            ui.getGameRules().set(ShinobiCore.VARIED_WORLD, true, null);
        }).create()) {
            begin(c, w);
            check(w.getServer().computeOnServer(SaveSeed::of).mode().equals("varied"), "a Varied save");
            pick(c, w, "story.ch0", "cell_reply", "silent");
            pick(c, w, "story.ch0", "freed_boy", "leave");
            pick(c, w, "story.ch0", "raid_reply", "run");
            for (int i = 0; i < 100 && !journal(w).knows("story.ch1"); i++) c.waitTicks(5);
            check(journal(w).done().contains("story.ch0") && journal(w).knows("story.ch1") && !said("story.ch0.boy.1") && !said("story.ch0.tunnel.1"),
                    "Varied plays chapter 0 into chapter 1, the skipped branches unsaid: " + journal(w));
        }
        ShinobiProgression.LINE_TICKS = 60;
    }

    /** A new world: quiet weather and clock, short line pauses, and the creator's Done, which starts the story. */
    static void begin(ClientGameTestContext c, TestSingleplayerContext w) {
        w.getConnection().waitForChunksRender();
        for (String cmd : List.of("gamerule spawn_mobs false", "gamerule advance_weather false", "weather clear", "gamerule advance_time false", "time set 3000"))
            w.getServer().runCommand(cmd);
        w.getServer().runOnServer(s -> ShinobiProgression.LINE_TICKS = 10);
        // The creator lives in Shinobi Village's client classes, which this test does not compile against.
        c.waitFor(mc -> mc.gui.screen() != null && mc.gui.screen().getClass().getSimpleName().equals("CreatorScreen"));
        c.clickScreenButton("Done");
        for (int i = 0; i < 20 && !journal(w).knows(ShinobiProgression.OPENING); i++) c.waitTicks(10);
        check(journal(w).knows(ShinobiProgression.OPENING), "the creator's look starts the story: " + journal(w));
    }

    /** Waits for the quest's choice and its link in chat, then runs the link's command from the client, as a click does. */
    static void pick(ClientGameTestContext c, TestSingleplayerContext w, String quest, String at, String option) {
        String cmd = "/shinobi answer " + quest + " " + at + " " + option;
        for (int i = 0; i < 200 && !(at.equals(step(w, quest)) && CHAT.stream().anyMatch(m -> links(m, cmd))); i++) c.waitTicks(5);
        check(at.equals(step(w, quest)) && CHAT.stream().anyMatch(m -> links(m, cmd)), "the choice " + option + " is offered in chat at " + quest + " " + at + ": " + journal(w));
        c.runOnClient(mc -> mc.player.connection.sendCommand(cmd.substring(1)));
        for (int i = 0; i < 20 && at.equals(step(w, quest)); i++) c.waitTicks(5);
        check(!at.equals(step(w, quest)), "answered " + option + " at " + quest + " " + at + ": " + journal(w));
    }

    static boolean links(Component m, String cmd) {
        return m.getStyle().getClickEvent() instanceof ClickEvent.RunCommand r && r.command().equals(cmd) || m.getSiblings().stream().anyMatch(x -> links(x, cmd));
    }

    /** Whether the client has received the line with this lang key. */
    static boolean said(String key) {
        return CHAT.stream().anyMatch(m -> m.getContents() instanceof TranslatableContents t && t.getKey().equals(key));
    }

    static String step(TestSingleplayerContext w, String quest) { return journal(w).active().get(quest); }
}
