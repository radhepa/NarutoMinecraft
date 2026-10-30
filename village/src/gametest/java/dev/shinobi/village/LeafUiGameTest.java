package dev.shinobi.village;

import dev.villagefriends.VillageFriends;
import dev.villagefriends.VillageLedger;
import dev.villagefriends.VillageSettlements;
import dev.villagefriends.ResidentProfile;
import dev.villagefriends.client.FriendshipScreen;
import dev.villagefriends.client.LedgerScreen;
import net.fabricmc.fabric.api.client.gametest.v1.FabricClientGameTest;
import net.fabricmc.fabric.api.client.gametest.v1.context.ClientGameTestContext;
import net.minecraft.client.CameraType;
import net.minecraft.client.gui.ActiveTextCollector;
import net.minecraft.client.gui.components.ChatComponent;
import net.minecraft.client.gui.screens.ChatScreen;
import net.minecraft.network.chat.ClickEvent;
import net.minecraft.network.chat.Component;
import net.minecraft.world.entity.EntityTypes;
import net.minecraft.world.entity.npc.villager.Villager;

import java.util.Locale;

import static dev.shinobi.village.LeafResidentGameTest.check;

/**
 * The player's face beside a resident's (VF's eye planes on both), and the Hidden Leaf screens in a real client: a resident's conversation window and the village ledger in the Leaf colours
 * with scroll rods and the crest, and the chat as the Leaf message scroll (a narrated line, a speaker's line with its
 * name plate, an answer card), shut and open; a click on the answer card still finds its command.
 * Screenshots: leaf-eyes, leaf-talk, leaf-ledger, leaf-chat, leaf-chat-open.
 */
@SuppressWarnings("UnstableApiUsage")
public final class LeafUiGameTest implements FabricClientGameTest {
    @Override
    public void runTest(ClientGameTestContext c) {
        try (var w = c.worldBuilder().create()) {
            w.getConnection().waitForChunksRender();
            CreatorGameTest.skipCreator(w);
            for (String cmd : new String[]{"time set noon", "weather clear", "gamerule advance_time false"}) w.getServer().runCommand(cmd);
            double[] o = w.getServer().computeOnServer(s -> {
                var p = w.getConnection().getServerPlayer();
                return new double[]{Math.floor(p.getX()) + .5, Math.floor(p.getY()), Math.floor(p.getZ()) + .5};
            });
            int x = (int) Math.floor(o[0]), y = (int) o[1], z = (int) Math.floor(o[2]);
            w.getServer().runCommand(String.format(Locale.ROOT, "fill %d %d %d %d %d %d grass_block", x - 4, y - 1, z - 2, x + 4, y - 1, z + 6));
            w.getServer().runCommand(String.format(Locale.ROOT, "fill %d %d %d %d %d %d air", x - 4, y, z - 2, x + 4, y + 4, z + 6));
            w.getServer().runCommand(String.format(Locale.ROOT, "tp @p %.2f %.2f %.2f 0 10", o[0], o[1], o[2]));
            int id = w.getServer().computeOnServer(s -> {
                var level = w.getConnection().getServerLevel();
                var v = new Villager(EntityTypes.VILLAGER, level);
                v.setNoAi(true);
                v.setPos(o[0] + 1.1, o[1], o[2]);   // beside the player, facing the same way, to compare faces
                v.setYRot(0);
                v.yBodyRot = v.yHeadRot = 0;
                var look = LeafResidentGameTest.LOOKS.get(1);
                VillageFriends.target(v).setAttached(VillageFriends.PROFILE, ResidentProfile.generate(v.getUUID(), look.recipe()));
                VillageFriends.target(v).setAttached(VillageFriends.LOOK, look.recipe());
                level.addFreshEntity(v);
                return v.getId();
            });
            w.getConnection().waitForClientboundEntityUpdates(EntityTypes.VILLAGER);
            c.runOnClient(mc -> mc.options.setCameraType(CameraType.THIRD_PERSON_FRONT));
            c.waitTicks(30);
            c.takeScreenshot("leaf-eyes");
            c.runOnClient(mc -> mc.options.setCameraType(CameraType.FIRST_PERSON));

            w.getServer().runOnServer(s -> VillageFriends.show(w.getConnection().getServerPlayer(), (Villager) w.getConnection().getServerLevel().getEntity(id),
                    "talk", "Fine weather for training today.", "", true));
            c.waitForScreen(FriendshipScreen.class);
            c.waitTicks(10);
            c.takeScreenshot("leaf-talk");
            c.setScreen(() -> null);

            w.getServer().runOnServer(s -> {   // the ledger reads the village around the player, so mark one here
                var p = w.getConnection().getServerPlayer();
                VillageSettlements.mark(w.getConnection().getServerLevel(), p.blockPosition(), "Leaf Yard");
                VillageLedger.openHere(p);
            });
            c.waitForScreen(LedgerScreen.class);
            c.waitTicks(10);
            c.takeScreenshot("leaf-ledger");
            c.setScreen(() -> null);

            w.getServer().runOnServer(s -> {
                var p = w.getConnection().getServerPlayer();
                p.sendSystemMessage(Component.literal("§7§oA warm wind moves through the leaves of the yard."));
                p.sendSystemMessage(Component.literal("Instructor: \"Line up, everyone. Today we practise the basic stances, then you spar.\""));
                p.sendSystemMessage(Component.literal("Are you ready?").withStyle(net.minecraft.ChatFormatting.YELLOW));
                p.sendSystemMessage(Component.literal(" [Ready]").withStyle(st -> st.withColor(net.minecraft.ChatFormatting.GREEN).withClickEvent(new ClickEvent.RunCommand("/say ready"))));
            });
            c.runOnClient(mc -> { if (mc.gui.hud.isHidden()) mc.gui.hud.toggle(); });   // the test's settings hide the HUD, and the shut chat with it
            c.waitTicks(60);
            c.takeScreenshot("leaf-chat");

            c.setScreen(() -> new ChatScreen("Hello, Instructor", false));
            c.waitTicks(10);
            c.takeScreenshot("leaf-chat-open");
            String found = c.computeOnClient(mc -> {
                var chat = mc.gui.hud.getChat();
                int h = mc.getWindow().getGuiScaledHeight();
                for (int py = h - 40; py > h - 200; py--)
                    for (int px = 0; px < 120; px += 2) {
                        var finder = new ActiveTextCollector.ClickableStyleFinder(mc.font, px, py);
                        chat.captureClickableText(finder, h, mc.gui.hud.getGuiTicks(), ChatComponent.DisplayMode.FOREGROUND);
                        if (finder.result() != null && finder.result().getClickEvent() instanceof ClickEvent.RunCommand run) return run.command();
                    }
                return null;
            });
            check("/say ready".equals(found), "a click on the answer card finds its command: " + found);
            c.setScreen(() -> null);
        }
    }
}
