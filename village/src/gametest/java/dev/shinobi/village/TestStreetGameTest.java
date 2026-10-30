package dev.shinobi.village;

import dev.shinobi.core.SaveSeed;
import dev.shinobi.core.ShinobiCore;
import dev.villagefriends.HousePlaqueBlockEntity;
import dev.villagefriends.VillageBlocks;
import dev.villagefriends.VillageFriends;
import dev.villagefriends.VillageSettlements;
import dev.villagefriends.home.House;
import dev.villagefriends.home.Homes;
import dev.villagefriends.routine.Routine;
import net.fabricmc.fabric.api.client.gametest.v1.FabricClientGameTest;
import net.fabricmc.fabric.api.client.gametest.v1.context.ClientGameTestContext;
import net.fabricmc.fabric.api.client.gametest.v1.context.TestSingleplayerContext;
import net.fabricmc.fabric.api.client.gametest.v1.world.TestWorldSave;
import net.minecraft.core.BlockPos;
import net.minecraft.client.gui.screens.worldselection.WorldCreationUiState;
import net.minecraft.core.Direction;
import net.minecraft.core.registries.Registries;
import net.minecraft.server.level.ServerLevel;
import net.minecraft.world.InteractionHand;
import net.minecraft.world.entity.npc.villager.Villager;
import net.minecraft.world.item.ItemStack;
import net.minecraft.world.item.Items;
import net.minecraft.world.level.GameType;
import net.minecraft.world.level.Level;
import net.minecraft.world.level.storage.LevelData;
import net.minecraft.world.level.gamerules.GameRules;
import net.minecraft.world.level.levelgen.presets.WorldPresets;
import net.minecraft.world.phys.BlockHitResult;
import net.minecraft.world.phys.Vec3;

import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;
import java.util.Locale;
import java.util.Map;
import java.util.function.BooleanSupplier;
import java.util.function.Supplier;

/**
 * World creation: a new world made the default way loads the Leaf map, with the player on the street inside the border
 * and nothing around but the map; reopening keeps the border and spawn, and a death respawns on the street. A
 * Superflat world gets no map. Screenshot: test-street-spawn.
 * P03-2: the test street: ten residents each get their own flat and bed, walk by day and sleep at night.
 * P03-3: Classic's cast is the same whatever the world seed, and reopening the save finds the same residents in the
 * same flats; a Varied world (its game rule on) keeps that mode in its save seed and rolls a different cast.
 * P03-4: the tea house keeper lives over the shop, the notice board and training yard stand in the village, and only
 * builder mode can change the street.
 * P03-5: building the street sets the Leaf map's rules.
 * P03-6: the performance route, by day and at night, logged as the baseline. Screenshots: test-street-*.
 */
@SuppressWarnings({"UnstableApiUsage", "unchecked"})
public final class TestStreetGameTest implements FabricClientGameTest {
    @Override
    public void runTest(ClientGameTestContext c) {
        TestWorldSave save;
        List<String> cast;
        try (var w = c.worldBuilder().setUseConsistentSettings(false).create()) {
            w.getConnection().waitForChunksRender();
            CreatorGameTest.skipCreator(w);
            for (String cmd : List.of("gamerule advance_time false", "gamerule advance_weather false", "gamerule spawn_mobs false",
                    "weather clear", "difficulty peaceful", "time set 3000"))
                w.getServer().runCommand(cmd);
            BlockPos player = w.getServer().computeOnServer(s -> stand(w.getConnection().getServerPlayer()));
            BlockPos origin = TestStreet.MAP;
            w.getServer().runOnServer(s -> {
                var level = w.getConnection().getServerLevel();
                check(player.equals(TestStreet.SPAWN) && level.getWorldBorder().isWithinBounds(player), "the player spawns on the street inside the border: " + player.toShortString());
                check(SaveSeed.of(s).equals(new SaveSeed(level.getSeed(), "classic")), "a default world is Classic: " + SaveSeed.of(s));
                // No terrain: nothing under the map's ground layer, and nothing past the border on either axis.
                int out = (int) (TestStreet.BORDER / 2) + 6;
                check(empty(level, player.getX(), player.getZ(), level.getMinY(), origin.getY() - 1)
                        && empty(level, (int) TestStreet.BORDER_X + out, player.getZ(), level.getMinY(), level.getMaxY())
                        && empty(level, player.getX(), (int) TestStreet.BORDER_Z - out, level.getMinY(), level.getMaxY()), "no terrain but the map");
            });
            c.waitTicks(20);
            c.takeScreenshot("test-street-spawn");
            var built = street(c, w);
            ShinobiVillage.LOG.info("Test street plaques: {}", built.plaques());
            int n = built.residents().size();
            check(n == 11, "ten flat residents and the tea house keeper: " + n);
            check(built.plaques().size() == 12 && built.plaques().stream().allMatch(p -> p.contains("1 bed")), "eleven flats and the tea house with a bed each: " + built.plaques());

            // Their markers; a resident out at its hobby has walked away from one.
            List<Vec3> spawn = w.getServer().computeOnServer(s -> built.residents().stream().map(Villager::position).toList());
            until(c, () -> w.getServer().computeOnServer(s -> {
                var houses = new HashSet<String>();
                for (var v : built.residents()) { House h = Homes.houseOf(v); if (h != null) houses.add(h.id()); }
                return houses.size() == n;
            }), 1200, () -> "each resident has a house of their own");
            List<String> beds = w.getServer().computeOnServer(s -> built.residents().stream().map(v -> Homes.bedOf(v).map(b -> b.head().subtract(origin).toShortString()).orElse("-")).toList());
            check(java.util.stream.IntStream.range(0, n).allMatch(i -> Homes.bedOf(built.residents().get(i)).map(b -> b.head().distSqr(BlockPos.containing(spawn.get(i))) < 64).orElse(false)),
                    "each resident's bed is in the house it was placed in: " + beds + " for " + spawn.stream().map(p -> BlockPos.containing(p).subtract(origin).toShortString()).toList());

            until(c, () -> walked(w, built, spawn) > 0, 2400, () -> "a resident walks by day");
            ShinobiVillage.LOG.info("Test street: {} of {} residents left their markers", walked(w, built, spawn), n);
            view(c, w, player.getX() + .5, player.getY() + 3, player.getZ() + 14.5, 180, 12, "test-street-day");
            view(c, w, player.getX() + 25.5, player.getY() + 4, player.getZ() + 11.5, 180, 25, "test-street-yard");
            route(c, w, player, "day");

            BlockPos board = built.anchors().get("notice_board"), yard = built.anchors().get("anchor:training");
            w.getServer().runOnServer(s -> {
                var level = w.getConnection().getServerLevel();
                var rules = level.getGameRules();
                check(TestStreet.OFF.stream().noneMatch(rules::get) && rules.get(GameRules.FIRE_SPREAD_RADIUS_AROUND_PLAYER) == 0, "the Leaf map's rules");
                check(level.getBlockState(board).is(VillageBlocks.get("notice_board")), "VF's notice board on the street front");
                for (var at : List.of(board, yard))
                    check(built.village().equals(VillageSettlements.book(level).at(at).id()), "board and yard in the street's village: " + at.toShortString());
                // Adventure protection: a survival player cannot break the street; builder mode can.
                var me = w.getConnection().getServerPlayer();
                me.setGameMode(GameType.SURVIVAL);
                var ground = board.below();
                var was = level.getBlockState(ground);
                check(!me.gameMode.destroyBlock(ground) && level.getBlockState(ground).equals(was), "a player cannot break the street");
                me.addTag(StreetGuard.BUILDER);
                check(me.gameMode.destroyBlock(ground) && level.getBlockState(ground).isAir(), "builder mode can");
                level.setBlock(ground, was, 3);
                me.removeTag(StreetGuard.BUILDER);
                me.setItemInHand(InteractionHand.MAIN_HAND, new ItemStack(Items.DIRT));
                me.gameMode.useItemOn(me, level, me.getMainHandItem(), InteractionHand.MAIN_HAND, new BlockHitResult(Vec3.atCenterOf(yard.below()), Direction.UP, yard.below(), false));
                check(level.getBlockState(yard).isAir(), "a player cannot build on the street");
                // Sneak-using a flat's plaque would make it private and turn its resident out.
                var first = built.residents().getFirst();
                BlockPos plaque = Homes.houseOf(first).plaque().orElseThrow();
                me.setItemInHand(InteractionHand.MAIN_HAND, ItemStack.EMPTY);
                me.setShiftKeyDown(true);
                me.gameMode.useItemOn(me, level, ItemStack.EMPTY, InteractionHand.MAIN_HAND, new BlockHitResult(Vec3.atCenterOf(plaque), Direction.SOUTH, plaque, false));
                me.setShiftKeyDown(false);
                check(!Homes.houseOf(first).privateHome(), "a player cannot make a resident's flat private");
                me.setGameMode(GameType.CREATIVE);
            });

            // VF's routine clock, frozen at 2 am: past every chronotype's bedtime, night owls included.
            w.getServer().runCommand("time set " + (2 * 24000 + Routine.at(2, 0)));
            until(c, () -> asleep(w, built) >= n - 2, 2400, () -> "residents asleep in their own beds: " + asleep(w, built) + "; doing "
                    + w.getServer().computeOnServer(s -> built.residents().stream().map(dev.villagefriends.ResidentRoutines::doing).toList()));
            ShinobiVillage.LOG.info("Test street: {} of {} residents asleep in their own beds", asleep(w, built), n);
            route(c, w, player, "night");

            cast = w.getServer().computeOnServer(s -> built.residents().stream().map(TestStreetGameTest::identity).toList());
            ShinobiVillage.LOG.info("Test street cast: {}", cast);
            check(built.residents().getFirst().getUUID().equals(TestStreet.resident(TestStreet.CLASSIC_CAST, 0)), "Classic's cast comes from its own seed and the markers");
            check(cast.stream().map(id -> id.split("\\|")[1]).distinct().count() == n, "different residents: " + cast);
            save = w.getWorldSave();
        }

        try (var w = save.open()) {
            w.getConnection().waitForChunksRender();
            List<String>[] found = new List[1];
            until(c, () -> {
                found[0] = w.getServer().computeOnServer(s -> {
                    var level = w.getConnection().getServerLevel();
                    var out = new java.util.ArrayList<String>();
                    for (String id : cast) {
                        var e = level.getEntity(java.util.UUID.fromString(id.split("\\|")[0]));
                        if (e instanceof Villager v && Homes.houseOf(v) != null) out.add(identity(v));
                    }
                    return out;
                });
                return found[0].equals(cast);
            }, 600, () -> "the same residents in the same flats after reopening: " + found[0]);
            w.getServer().runOnServer(s -> {
                var border = w.getConnection().getServerLevel().getWorldBorder();
                check(border.getSize() == TestStreet.BORDER && border.getCenterX() == TestStreet.BORDER_X && border.getCenterZ() == TestStreet.BORDER_Z
                        && s.getRespawnData().equals(LevelData.RespawnData.of(Level.OVERWORLD, TestStreet.SPAWN, 180, 0)), "the border and the spawn survive the reload: " + s.getRespawnData());
            });
            w.getServer().runCommand("kill @p");
            c.waitTicks(5);
            c.runOnClient(mc -> mc.player.respawn());
            c.waitTicks(10);
            BlockPos respawn = w.getServer().computeOnServer(s -> stand(s.getPlayerList().getPlayers().getFirst()));
            check(respawn.equals(TestStreet.SPAWN), "a death respawns the player on the street: " + respawn.toShortString());
        }

        // Varied, set on the Game Rules screen: fixed in the save seed, which rolls the cast.
        try (var w = c.worldBuilder().setUseConsistentSettings(false).adjustSettings(ui -> {
            ui.setSeed("7");
            ui.getGameRules().set(ShinobiCore.VARIED_WORLD, true, null);
        }).create()) {
            w.getConnection().waitForChunksRender();
            CreatorGameTest.skipCreator(w);
            SaveSeed seed = w.getServer().computeOnServer(SaveSeed::of);
            check(seed.equals(new SaveSeed(7, "varied")), "a Varied world keeps its mode: " + seed);
            var varied = street(c, w);
            check(varied.residents().getFirst().getUUID().equals(TestStreet.resident(7, 0)), "Varied's cast comes from the save seed");
            List<String> names = new ArrayList<>();
            until(c, () -> {
                names.clear();
                names.addAll(w.getServer().computeOnServer(s -> varied.residents().stream().filter(v -> v.getCustomName() != null).map(v -> v.getCustomName().getString()).toList()));
                return names.size() == varied.residents().size();
            }, 600, () -> "the Varied residents have names: " + names);
            ShinobiVillage.LOG.info("Varied cast: {}", names);
            check(!names.equals(cast.stream().map(id -> id.split("\\|")[1]).toList()), "a different cast from Classic's: " + names);
        }

        // A world on another generator (Superflat here) keeps its terrain: no map is pasted over it.
        try (var w = c.worldBuilder().setUseConsistentSettings(false).adjustSettings(ui -> ui.setWorldType(new WorldCreationUiState.WorldTypeEntry(
                ui.getSettings().worldgenLoadContext().lookupOrThrow(Registries.WORLD_PRESET).getOrThrow(WorldPresets.FLAT)))).create()) {
            w.getConnection().waitForChunksRender();
            CreatorGameTest.skipCreator(w);
            check(w.getServer().computeOnServer(s -> w.getConnection().getServerLevel().getAttached(ShinobiVillage.ANCHORS) == null), "a Superflat world gets no map");
        }
    }

    /** The block a player stands in, counting the dirt path's top (a sixteenth below the block) as the block above it. */
    static BlockPos stand(net.minecraft.world.entity.Entity e) { return BlockPos.containing(e.position().add(0, .1, 0)); }

    /** The street the new world pasted at its first start, read back from the world once its residents have loaded. */
    static TestStreet.Built street(ClientGameTestContext c, TestSingleplayerContext w) {
        TestStreet.Built[] built = new TestStreet.Built[1];
        until(c, () -> (built[0] = w.getServer().computeOnServer(s -> {
            var level = w.getConnection().getServerLevel();
            long cast = TestStreet.castSeed(level);
            var plaques = new ArrayList<String>();
            var residents = new ArrayList<Villager>();
            int marker = 0;
            for (var plot : TestStreet.PLOTS)
                for (var m : Blueprint.load(plot.getKey()).json().getAsJsonArray("markers")) {
                    var at = Blueprint.at(TestStreet.MAP.offset(plot.getValue()), m.getAsJsonObject());
                    switch (m.getAsJsonObject().get("type").getAsString()) {
                        case "house_plaque" -> { if (level.getBlockEntity(at) instanceof HousePlaqueBlockEntity plaque) plaques.add(plaque.scanForBeds()); }
                        case "resident" -> { if (level.getEntity(TestStreet.resident(cast, marker++)) instanceof Villager v) residents.add(v); }
                        default -> {}
                    }
                }
            return marker == residents.size() ? new TestStreet.Built(VillageSettlements.book(level).at(TestStreet.MAP).id(), plaques, residents,
                    level.getAttachedOrElse(ShinobiVillage.ANCHORS, Map.of())) : null;
        })) != null, 600, () -> "the map's residents load");
        return built[0];
    }

    /** Whether the column at x, z holds only air from y {@code from} to {@code to}. */
    static boolean empty(ServerLevel level, int x, int z, int from, int to) {
        for (int y = from; y <= to; y++) if (!level.getBlockState(new BlockPos(x, y, z)).isAir()) return false;
        return true;
    }

    /** A resident's UUID, name, look and flat. */
    static String identity(Villager v) {
        return v.getUUID() + "|" + v.getCustomName().getString() + "|" + v.getAttached(VillageFriends.LOOK) + "|" + Homes.houseOf(v).id();
    }

    static long walked(TestSingleplayerContext w, TestStreet.Built built, List<Vec3> spawn) {
        return w.getServer().computeOnServer(s -> {
            long n = 0;
            for (int i = 0; i < spawn.size(); i++) if (built.residents().get(i).position().distanceTo(spawn.get(i)) > 1.5) n++;
            return n;
        });
    }

    static long asleep(TestSingleplayerContext w, TestStreet.Built built) {
        return w.getServer().computeOnServer(s -> built.residents().stream()
                .filter(v -> v.isSleeping() && Homes.bedOf(v).map(b -> v.getSleepingPos().map(b.head()::equals).orElse(false)).orElse(false)).count());
    }

    /**
     * The performance route: the shop, the apartment block and the yard, five seconds at each, logging the server's average
     * ms per tick and the client's frames. A record, not a gate: one shared CI runner's noise would fail it.
     */
    static void route(ClientGameTestContext c, TestSingleplayerContext w, BlockPos player, String when) {
        for (int x : new int[]{-24, 0, 25}) {
            w.getServer().runCommand(String.format(Locale.ROOT, "tp @a %d %d %d 180 15", player.getX() + x, player.getY() + 3, player.getZ() + 14));
            c.waitTicks(100);
            double mspt = w.getServer().computeOnServer(s -> s.getAverageTickTimeNanos() / 1e6);
            int fps = c.computeOnClient(mc -> mc.getFps());
            ShinobiVillage.LOG.info("Performance route ({}) at x{}: {} ms per tick on average, {} fps", when, x, String.format(Locale.ROOT, "%.2f", mspt), fps);
        }
    }

    static void view(ClientGameTestContext c, TestSingleplayerContext w, double x, double y, double z, float yaw, float pitch, String name) {
        w.getServer().runCommand(String.format(Locale.ROOT, "tp @a %.2f %.2f %.2f %.1f %.1f", x, y, z, yaw, pitch));
        c.waitTicks(40);
        c.takeScreenshot(name);
    }

    static void until(ClientGameTestContext c, BooleanSupplier test, int ticks, Supplier<String> what) {
        for (int i = 0; i < ticks; i += 10) {
            if (test.getAsBoolean()) return;
            c.waitTicks(10);
        }
        if (!test.getAsBoolean()) throw new AssertionError("Timed out: " + what.get());
    }

    static void check(boolean ok, String what) {
        if (!ok) throw new AssertionError("Failed: " + what);
    }
}
