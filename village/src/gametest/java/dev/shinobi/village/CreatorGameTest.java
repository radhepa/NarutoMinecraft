package dev.shinobi.village;

import dev.shinobi.village.client.CreatorScreen;
import net.fabricmc.fabric.api.client.gametest.v1.FabricClientGameTest;
import net.fabricmc.fabric.api.client.gametest.v1.context.ClientGameTestContext;
import net.fabricmc.fabric.api.client.gametest.v1.context.TestSingleplayerContext;
import net.fabricmc.fabric.api.client.gametest.v1.world.TestWorldSave;
import net.minecraft.client.CameraType;
import net.minecraft.client.gui.components.Button;
import net.minecraft.core.ClientAsset;
import net.minecraft.network.chat.contents.TranslatableContents;

import java.util.stream.Stream;

/**
 * P05-1: a new player meets the creator, steps the body, hair and outfit, and Done keeps the look on the server, which
 * refuses a second pick and looks the rules do not allow; the player wears the look, and reopening keeps it without
 * the creator. Screenshots: creator-open, creator-picked, creator-look, creator-reopened.
 */
@SuppressWarnings("UnstableApiUsage")
public final class CreatorGameTest implements FabricClientGameTest {
    @Override
    public void runTest(ClientGameTestContext c) {
        TestWorldSave save;
        String chosen;
        try (var w = c.worldBuilder().create()) {
            w.getConnection().waitForChunksRender();
            w.getServer().runCommand("time set noon");
            c.waitForScreen(CreatorScreen.class);
            c.takeScreenshot("creator-open");
            for (String step : new String[]{"body", "hair", "outfit", "palette"}) press(c, step);
            c.waitTicks(5);
            c.takeScreenshot("creator-picked");
            String bad = PlayerLooks.defaultLook().replace("\"marks\":[]", "\"marks\":[1]");
            check(!bad.equals(PlayerLooks.defaultLook()), "the bad look differs: " + bad);
            for (String json : new String[]{"[]", "x", bad})
                check(!w.getServer().computeOnServer(s -> PlayerLooks.choose(w.getConnection().getServerPlayer(), json)), "a broken look is refused: " + json);
            press(c, "done");
            c.waitTicks(10);
            chosen = w.getServer().computeOnServer(s -> w.getConnection().getServerPlayer().getAttached(PlayerLooks.LOOK));
            check(chosen != null && PlayerLooks.parse(chosen).body().equals("female"), "the server keeps the picked look: " + chosen);
            check(c.computeOnClient(mc -> mc.gui.screen() == null), "Done closes the creator");
            check(!w.getServer().computeOnServer(s -> PlayerLooks.choose(w.getConnection().getServerPlayer(), PlayerLooks.defaultLook())), "a second pick is refused");
            var look = PlayerLooks.parse(chosen);
            check(!PlayerLooks.allowed(look.withHairColor("SUN_BLOND")) && !PlayerLooks.allowed(look.withOutfit("aburame.elder_mantle", "ABURAME_DUST"))
                    && !PlayerLooks.allowed(look.withComplexion(9)), "looks outside the rules or the wardrobe are refused");

            c.runOnClient(mc -> mc.options.setCameraType(CameraType.THIRD_PERSON_FRONT));
            c.waitTicks(20);
            check(worn(c), "the player wears the look");
            c.takeScreenshot("creator-look");
            save = w.getWorldSave();
        }
        try (var w = save.open()) {
            w.getConnection().waitForChunksRender();
            c.waitTicks(60);
            check(chosen.equals(w.getServer().computeOnServer(s -> w.getConnection().getServerPlayer().getAttached(PlayerLooks.LOOK))), "the look survives reopening");
            check(c.computeOnClient(mc -> mc.gui.screen() == null) && worn(c), "no creator after reopening, and the look is still worn");
            c.takeScreenshot("creator-reopened");
            c.runOnClient(mc -> mc.options.setCameraType(CameraType.FIRST_PERSON));
        }
    }

    /** Clicks the creator button for {@code key}; the gametest matches buttons by their shown text. */
    static void press(ClientGameTestContext c, String key) {
        c.clickScreenButton(c.computeOnClient(mc -> mc.gui.screen().children().stream()
                .flatMap(e -> e instanceof Button b && b.getMessage().getContents() instanceof TranslatableContents t
                        && t.getKey().equals("narutominecraft.creator." + key) ? Stream.of(b.getMessage().getString()) : Stream.empty())
                .findFirst().orElseThrow()));
    }

    static boolean worn(ClientGameTestContext c) {
        return c.computeOnClient(mc -> mc.player.getSkin().body() instanceof ClientAsset.ResourceTexture t && t.id().getNamespace().equals("narutominecraft"));
    }

    /** Skips the creator in the other tests: the player takes the opening look. */
    static void skipCreator(TestSingleplayerContext w) {
        check(w.getServer().computeOnServer(s -> PlayerLooks.choose(w.getConnection().getServerPlayer(), PlayerLooks.defaultLook())), "the opening look is allowed");
    }

    static void check(boolean ok, String what) {
        if (!ok) throw new AssertionError("Failed: " + what);
    }
}
