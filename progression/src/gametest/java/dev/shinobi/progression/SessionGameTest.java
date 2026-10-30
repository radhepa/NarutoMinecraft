package dev.shinobi.progression;

import dev.shinobi.combat.runtime.Spar;
import dev.shinobi.life.ShinobiLife;
import dev.shinobi.village.PlayerLooks;
import dev.shinobi.village.ShinobiVillage;
import dev.shinobi.village.TestStreet;
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
import net.minecraft.world.item.BlockItem;
import net.minecraft.world.item.ItemStack;
import net.minecraft.world.item.Items;
import net.minecraft.world.level.levelgen.presets.WorldPresets;
import net.minecraft.world.phys.AABB;
import net.minecraft.world.phys.BlockHitResult;
import net.minecraft.world.phys.EntityHitResult;
import net.minecraft.world.phys.Vec3;

import java.util.List;
import java.util.Map;
import java.util.UUID;

import static dev.shinobi.progression.ErrandGameTest.check;
import static dev.shinobi.progression.ErrandGameTest.journal;
import static dev.shinobi.progression.ErrandGameTest.ryo;

/**
 * M2, the ten-minute play session (ROADMAP.md 13.4): on the test street a new player makes a character in the creator,
 * the training quest starts and names each step; the player walks to the yard and wins a spar by real attacks (each
 * one taken by the server), earns 30 ryo, buys a tatami from the keeper, places it in flat 3a, sleeps in the flat's bed
 * at nightfall into the next morning, and reopening keeps the look, the finished quest, the wallet and the furnishing.
 * Screenshots: session-creator, session-spar, session-won, session-furnished, session-asleep, session-reopened.
 */
@SuppressWarnings("UnstableApiUsage")
public final class SessionGameTest implements FabricClientGameTest {
    static final String TRAINING = ShinobiProgression.TRAINING;

    @Override
    public void runTest(ClientGameTestContext c) {
        TestWorldSave save;
        BlockPos placed;
        String look;
        try (var w = c.worldBuilder().adjustSettings(ui -> {
            var flat = ui.getSettings().worldgenLoadContext().lookupOrThrow(Registries.WORLD_PRESET).getOrThrow(WorldPresets.FLAT);
            ui.setWorldType(new WorldCreationUiState.WorldTypeEntry(flat));
            ui.setGenerateStructures(false);
        }).create()) {
            w.getConnection().waitForChunksRender();
            for (String cmd : List.of("gamerule spawn_mobs false", "gamerule advance_time true", "time set 3000")) w.getServer().runCommand(cmd);
            BlockPos start = w.getServer().computeOnServer(s -> w.getConnection().getServerPlayer().blockPosition());
            w.getServer().runOnServer(s -> TestStreet.build(w.getConnection().getServerLevel(), start.below().offset(-17, 0, -22)));

            // The creator lives in Shinobi Village's client classes, which this test does not compile against.
            c.waitFor(mc -> mc.gui.screen() != null && mc.gui.screen().getClass().getSimpleName().equals("CreatorScreen"));
            c.takeScreenshot("session-creator");
            c.clickScreenButton("Done");
            for (int i = 0; i < 20 && !"go_yard".equals(step(w)); i++) c.waitTicks(10);
            check("go_yard".equals(step(w)), "the creator's look starts the training quest: " + journal(w));
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
            for (int i = 0; i < 80 && "spar".equals(step(w)); i++) {
                c.runOnClient(mc -> mc.gameMode.attack(mc.player, mc.level.getEntity(id)));
                c.waitTicks(i == 3 ? 1 : 12);
                if (i == 3) c.takeScreenshot("session-spar");
            }
            check("shop".equals(step(w)) && ryo(w) == 130, "the spar won pays 30 ryo: " + journal(w) + ", " + ryo(w));
            c.takeScreenshot("session-won");

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
            check("furnish".equals(step(w)) && w.getServer().computeOnServer(s -> ShinobiProgression.buy(w.getConnection().getServerPlayer(), "furniture_shop", "tatami"))
                    && ryo(w) == 90, "talked to the keeper and bought a tatami: " + journal(w) + ", " + ryo(w));

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
            save = w.getWorldSave();
        }
        try (var w = save.open()) {
            w.getConnection().waitForChunksRender();
            c.waitTicks(40);
            check(look.equals(w.getServer().computeOnServer(s -> w.getConnection().getServerPlayer().getAttached(PlayerLooks.LOOK)))
                    && journal(w).done().contains(TRAINING) && !journal(w).active().containsKey(TRAINING) && ryo(w) == 90
                    && w.getServer().computeOnServer(s -> w.getConnection().getServerLevel().getBlockState(placed).getBlock() == ((BlockItem) ShinobiLife.item("tatami")).getBlock())
                    && c.computeOnClient(mc -> mc.gui.screen() == null), "reopening keeps the look, the quest, the wallet and the tatami: " + journal(w) + ", " + ryo(w));
            c.takeScreenshot("session-reopened");
        }
    }

    static String step(TestSingleplayerContext w) { return journal(w).active().get(TRAINING); }

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
