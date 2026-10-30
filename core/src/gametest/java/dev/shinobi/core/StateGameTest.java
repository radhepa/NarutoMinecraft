package dev.shinobi.core;

import net.fabricmc.fabric.api.client.gametest.v1.FabricClientGameTest;
import net.fabricmc.fabric.api.client.gametest.v1.context.ClientGameTestContext;
import net.fabricmc.fabric.api.client.gametest.v1.world.TestWorldSave;
import net.minecraft.server.MinecraftServer;
import net.minecraft.server.level.ServerPlayer;

/** P02-1: the player record and the save seed survive quitting to the title screen and reopening the world; P02-4: the record reaches its owner's client. */
@SuppressWarnings("UnstableApiUsage")
public final class StateGameTest implements FabricClientGameTest {
    static final PlayerRecord CHANGED = new PlayerRecord(PlayerRecord.VERSION, "genin", 7, "teen", "nara", "hard");
    static final SaveSeed TYPED = new SaveSeed(-42L, "varied");

    @Override
    public void runTest(ClientGameTestContext c) {
        TestWorldSave save;
        try (var w = c.worldBuilder().create()) {
            save = w.getWorldSave();
            w.getServer().runOnServer(s -> {
                SaveSeed seed = s.overworld().getAttached(ShinobiCore.SEED);
                check(seed != null && seed.seed() == s.overworld().getSeed() && seed.mode().equals("classic"), "new save seed " + seed);
                check(player(s).getAttachedOrCreate(ShinobiCore.PLAYER).equals(PlayerRecord.NEW), "new player record");
                // A typed seed differs from the world seed, so a reload that recomputed it would fail below.
                s.overworld().setAttached(ShinobiCore.SEED, TYPED);
                player(s).setAttached(ShinobiCore.PLAYER, CHANGED);
            });
            // P02-4: the owner's client receives the change.
            c.waitFor(mc -> mc.player != null && CHANGED.equals(mc.player.getAttached(ShinobiCore.PLAYER)), 100);
        }
        try (var w = save.open()) {
            w.getServer().runOnServer(s -> {
                check(TYPED.equals(s.overworld().getAttached(ShinobiCore.SEED)), "reloaded seed " + s.overworld().getAttached(ShinobiCore.SEED));
                check(CHANGED.equals(player(s).getAttached(ShinobiCore.PLAYER)), "reloaded record " + player(s).getAttached(ShinobiCore.PLAYER));
            });
        }
        ShinobiCore.LOG.info("Player record synced to its owner; record and save seed survived a reload");
    }

    static ServerPlayer player(MinecraftServer s) {
        return s.getPlayerList().getPlayers().getFirst();
    }

    static void check(boolean ok, String what) {
        if (!ok) throw new AssertionError("Failed: " + what);
    }
}
