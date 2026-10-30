package dev.shinobi.village;

import com.google.gson.JsonObject;
import dev.shinobi.village.look.ResidentNames;
import dev.villagefriends.ResidentProfile;
import dev.villagefriends.VillageFriends;
import dev.villagefriends.VillageSettlements;
import dev.villagefriends.VillageSocieties;
import dev.villagefriends.ResidentHome;
import dev.villagefriends.outfit.Gender;
import dev.villagefriends.outfit.PaletteID;
import dev.villagefriends.outfit.ResidentLook;
import net.fabricmc.fabric.api.client.gametest.v1.FabricClientGameTest;
import net.fabricmc.fabric.api.client.gametest.v1.context.ClientGameTestContext;
import net.fabricmc.fabric.api.client.gametest.v1.world.TestWorldSave;
import net.fabricmc.fabric.api.client.gametest.v1.screenshot.TestScreenshotOptions;
import net.minecraft.network.chat.Component;
import net.minecraft.world.entity.EntityTypes;
import net.minecraft.world.entity.npc.villager.Villager;

import java.util.LinkedHashMap;
import java.util.List;
import java.util.Map;
import java.util.UUID;

/** Japanese names in a real Leaf save, including migration, all genders, clan markers and save/reopen. */
@SuppressWarnings("UnstableApiUsage")
public final class LeafNamesGameTest implements FabricClientGameTest {
    @Override public void runTest(ClientGameTestContext c) {
        TestWorldSave save;
        Map<UUID, String> names;
        var pools = new ResidentNames(LeafWardrobe.read("/data/narutominecraft/names/given.json").toString());
        try (var w = c.worldBuilder().setUseConsistentSettings(false).create()) {
            w.getConnection().waitForChunksRender();
            CreatorGameTest.skipCreator(w);
            for (String cmd : List.of("time set noon", "weather clear", "gamerule advance_time false", "gamemode spectator @p")) w.getServer().runCommand(cmd);
            names = w.getServer().computeOnServer(s -> {
                var level = w.getConnection().getServerLevel();
                var out = new LinkedHashMap<UUID, String>();
                for (int i = 0; i < 4; i++) {
                    var v = new Villager(EntityTypes.VILLAGER, level);
                    v.setNoAi(true);
                    v.setPos(i % 2 == 0 ? 11 : 23, 65, i < 2 ? 34 : 44);
                    v.setYRot(180);
                    v.yBodyRot = v.yHeadRot = 180;
                    Gender gender = List.of(Gender.MALE, Gender.FEMALE, Gender.NON_BINARY, Gender.MALE).get(i);
                    String recipe = new ResidentLook(i + 1, gender, PaletteID.values()[i], 10L + i).recipe();
                    VillageFriends.target(v).setAttached(VillageFriends.PROFILE, ResidentProfile.generate(v.getUUID(), recipe));
                    var marker = new JsonObject();
                    if (i < 2) marker.addProperty("clan", i == 0 ? "clan:nara" : "uchiha");
                    LeafNames.marker(v, marker);
                    var village = VillageSettlements.discover(level, v.blockPosition());
                    VillageFriends.target(v).setAttached(VillageFriends.HOME, new ResidentHome(village.id(), "Old Resident"));
                    VillageFriends.target(v).setAttached(VillageFriends.HOME_LABEL, "Old Resident of " + village.name());
                    v.setCustomName(Component.literal("Old Resident of " + village.name()));
                    level.addFreshEntity(v);
                    VillageFriends.ensureIdentity(v);
                    String name = VillageFriends.target(v).getAttached(VillageFriends.HOME).baseName();
                    String[] parts = name.split(" ");
                    check(parts.length == 2 && pools.given(i == 2 ? "unisex" : i == 1 ? "female" : "male").contains(parts[0]), "a Japanese given name matching the profile");
                    check(i == 0 ? parts[1].equals("Nara") : i == 1 ? parts[1].equals("Uchiha") : PlayerLooks.rules.familyNames("clanless").contains(parts[1]), "the clan's or the shared ordinary surname");
                    VillageFriends.ensureIdentity(v);
                    check(VillageFriends.name(v).startsWith(name), "dialogue uses the saved Japanese name");
                    VillageSocieties.register(v);
                    check(name.equals(VillageSocieties.society(level, village.id()).get(VillageSocieties.id(v)).name()), "the journal and ledger use the Japanese base name");
                    out.put(v.getUUID(), name);
                }
                return out;
            });
            w.getConnection().waitForClientboundEntityUpdates(EntityTypes.VILLAGER);
            w.getServer().runCommand("tp @p 17 72 22 0 25");
            c.runOnClient(mc -> { if (mc.gui.hud.isHidden()) mc.gui.hud.toggle(); });
            c.waitTicks(220);
            c.takeScreenshot(TestScreenshotOptions.of("leaf-japanese-names").withSize(1920, 1080));
            ShinobiVillage.LOG.info("Leaf name proof: {}", names.values());
            save = w.getWorldSave();
        }
        try (var w = save.open()) {
            w.getConnection().waitForChunksRender();
            Map<UUID, String> expected = names;
            TestStreetGameTest.until(c, () -> w.getServer().computeOnServer(s -> expected.entrySet().stream().allMatch(e -> {
                var entity = w.getConnection().getServerLevel().getEntity(e.getKey());
                if (!(entity instanceof Villager v)) return false;
                VillageFriends.ensureIdentity(v);
                return e.getValue().equals(VillageFriends.target(v).getAttached(VillageFriends.HOME).baseName()) && VillageFriends.name(v).startsWith(e.getValue());
            })), 600, () -> "Japanese names and clan surnames survive reopening");
            ShinobiVillage.LOG.info("Leaf name proof: all {} names survived reopening", names.size());
        }
    }

    private static void check(boolean condition, String message) {
        if (!condition) throw new AssertionError(message);
    }
}
