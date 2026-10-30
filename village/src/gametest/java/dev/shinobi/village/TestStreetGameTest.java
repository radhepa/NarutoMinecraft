package dev.shinobi.village;

import dev.villagefriends.VillageFriends;
import dev.villagefriends.home.House;
import dev.villagefriends.home.Homes;
import dev.villagefriends.routine.Routine;
import net.fabricmc.fabric.api.client.gametest.v1.FabricClientGameTest;
import net.fabricmc.fabric.api.client.gametest.v1.context.ClientGameTestContext;
import net.fabricmc.fabric.api.client.gametest.v1.context.TestSingleplayerContext;
import net.fabricmc.fabric.api.client.gametest.v1.world.TestWorldSave;
import net.minecraft.client.gui.screens.worldselection.WorldCreationUiState;
import net.minecraft.core.BlockPos;
import net.minecraft.core.registries.Registries;
import net.minecraft.world.entity.npc.villager.Villager;
import net.minecraft.world.level.levelgen.presets.WorldPresets;
import net.minecraft.world.phys.Vec3;

import java.util.HashSet;
import java.util.List;
import java.util.Locale;
import java.util.function.BooleanSupplier;
import java.util.function.Supplier;

/**
 * P03-2: the test street on a flat map: ten residents each get their own flat and bed, walk by day and sleep at night.
 * P03-3: the same seed gives the same cast, and reopening the save finds the same residents in the same flats. Screenshots: test-street-*.
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
            for (String cmd : List.of("gamerule advance_time false", "gamerule advance_weather false", "gamerule spawn_mobs false",
                    "weather clear", "difficulty peaceful", "time set 3000"))
                w.getServer().runCommand(cmd);
            BlockPos player = w.getServer().computeOnServer(s -> w.getConnection().getServerPlayer().blockPosition());
            // The building's street side faces south, towards the player.
            BlockPos origin = player.below().offset(-17, 0, -22);
            var built = w.getServer().computeOnServer(s -> TestStreet.build(w.getConnection().getServerLevel(), origin));
            ShinobiVillage.LOG.info("Test street plaques: {}", built.plaques());
            check(built.residents().size() == 10, "ten resident markers: " + built.residents().size());
            check(built.plaques().size() == 11 && built.plaques().stream().allMatch(p -> p.contains("1 bed")), "eleven flats with a bed each: " + built.plaques());

            // Their markers; a resident out at its hobby has walked away from one.
            List<Vec3> spawn = w.getServer().computeOnServer(s -> built.residents().stream().map(Villager::position).toList());
            until(c, () -> w.getServer().computeOnServer(s -> {
                var houses = new HashSet<String>();
                for (var v : built.residents()) { House h = Homes.houseOf(v); if (h != null) houses.add(h.id()); }
                return houses.size() == 10;
            }), 1200, () -> "each resident has a flat of their own");
            List<String> beds = w.getServer().computeOnServer(s -> built.residents().stream().map(v -> Homes.bedOf(v).map(b -> b.head().subtract(origin).toShortString()).orElse("-")).toList());
            check(java.util.stream.IntStream.range(0, 10).allMatch(i -> Homes.bedOf(built.residents().get(i)).map(b -> b.head().distSqr(BlockPos.containing(spawn.get(i))) < 64).orElse(false)),
                    "each resident's bed is in the flat it was placed in: " + beds + " for " + spawn.stream().map(p -> BlockPos.containing(p).subtract(origin).toShortString()).toList());

            until(c, () -> walked(w, built, spawn) > 0, 2400, () -> "a resident walks by day");
            ShinobiVillage.LOG.info("Test street: {} of 10 residents left their markers", walked(w, built, spawn));
            view(c, w, player.getX() + .5, player.getY() + 3, player.getZ() + 6.5, 180, 12, "test-street-day");

            // VF's routine clock, frozen at 2 am: past every chronotype's bedtime, night owls included.
            w.getServer().runCommand("time set " + (2 * 24000 + Routine.at(2, 0)));
            until(c, () -> asleep(w, built) >= 8, 2400, () -> "residents asleep in their own beds: " + asleep(w, built) + "; doing "
                    + w.getServer().computeOnServer(s -> built.residents().stream().map(dev.villagefriends.ResidentRoutines::doing).toList()));
            ShinobiVillage.LOG.info("Test street: {} of 10 residents asleep in their own beds", asleep(w, built));

            cast = w.getServer().computeOnServer(s -> built.residents().stream().map(TestStreetGameTest::identity).toList());
            ShinobiVillage.LOG.info("Test street cast: {}", cast);
            check(built.residents().getFirst().getUUID().equals(TestStreet.resident(26, 0)), "the cast comes from the seed and the markers");
            check(cast.stream().map(id -> id.split("\\|")[1]).distinct().count() == 10, "ten different residents: " + cast);
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
