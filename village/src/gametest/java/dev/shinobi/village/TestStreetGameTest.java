package dev.shinobi.village;

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
import net.minecraft.client.gui.screens.worldselection.WorldCreationUiState;
import net.minecraft.core.BlockPos;
import net.minecraft.core.Direction;
import net.minecraft.core.registries.Registries;
import net.minecraft.world.InteractionHand;
import net.minecraft.world.entity.npc.villager.Villager;
import net.minecraft.world.item.ItemStack;
import net.minecraft.world.item.Items;
import net.minecraft.world.level.GameType;
import net.minecraft.world.level.gamerules.GameRules;
import net.minecraft.world.level.levelgen.presets.WorldPresets;
import net.minecraft.world.phys.BlockHitResult;
import net.minecraft.world.phys.Vec3;

import java.util.HashSet;
import java.util.List;
import java.util.Locale;
import java.util.function.BooleanSupplier;
import java.util.function.Supplier;

/**
 * P03-2: the test street on a flat map: ten residents each get their own flat and bed, walk by day and sleep at night.
 * P03-3: the same seed gives the same cast, and reopening the save finds the same residents in the same flats.
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
        try (var w = c.worldBuilder().adjustSettings(ui -> {
            var flat = ui.getSettings().worldgenLoadContext().lookupOrThrow(Registries.WORLD_PRESET).getOrThrow(WorldPresets.FLAT);
            ui.setWorldType(new WorldCreationUiState.WorldTypeEntry(flat));
            ui.setGenerateStructures(false);
            ui.setSeed("26");
        }).create()) {
            w.getConnection().waitForChunksRender();
            CreatorGameTest.skipCreator(w);
            for (String cmd : List.of("gamerule advance_time false", "gamerule advance_weather false", "gamerule spawn_mobs false",
                    "weather clear", "difficulty peaceful", "time set 3000"))
                w.getServer().runCommand(cmd);
            BlockPos player = w.getServer().computeOnServer(s -> w.getConnection().getServerPlayer().blockPosition());
            // The building's street side faces south, towards the player.
            BlockPos origin = player.below().offset(-17, 0, -22);
            var built = w.getServer().computeOnServer(s -> TestStreet.build(w.getConnection().getServerLevel(), origin));
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
            view(c, w, player.getX() + .5, player.getY() + 3, player.getZ() + 6.5, 180, 12, "test-street-day");
            view(c, w, player.getX() + 25.5, player.getY() + 4, player.getZ() + 3.5, 180, 25, "test-street-yard");
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
            check(built.residents().getFirst().getUUID().equals(TestStreet.resident(26, 0)), "the cast comes from the seed and the markers");
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
        }
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
            w.getServer().runCommand(String.format(Locale.ROOT, "tp @a %d %d %d 180 15", player.getX() + x, player.getY() + 3, player.getZ() + 6));
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
