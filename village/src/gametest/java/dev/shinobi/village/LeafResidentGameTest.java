package dev.shinobi.village;

import com.google.gson.JsonPrimitive;
import dev.villagefriends.VillageFriends;
import dev.villagefriends.client.ResidentRenderer;
import dev.villagefriends.outfit.Gender;
import dev.villagefriends.outfit.PaletteID;
import dev.villagefriends.outfit.ResidentLook;
import dev.villagefriends.ResidentProfile;
import dev.villagefriends.outfit.Profession;
import dev.villagefriends.outfit.Wardrobe;
import net.fabricmc.fabric.api.client.gametest.v1.FabricClientGameTest;
import net.fabricmc.fabric.api.client.gametest.v1.context.ClientGameTestContext;
import net.minecraft.world.entity.EntityTypes;
import net.minecraft.world.entity.npc.villager.Villager;

import java.util.ArrayList;
import java.util.List;
import java.util.Locale;

/** P03-1: Village Friends residents wear the Leaf wardrobe in a real client. Screenshot: leaf-residents. */
@SuppressWarnings("UnstableApiUsage")
public final class LeafResidentGameTest implements FabricClientGameTest {
    static final List<ResidentLook> LOOKS = List.of(
            new ResidentLook(1, Gender.MALE, PaletteID.values()[0], 11L),
            new ResidentLook(2, Gender.FEMALE, PaletteID.values()[1], 22L),
            new ResidentLook(3, Gender.MALE, PaletteID.values()[2], 33L),
            new ResidentLook(4, Gender.FEMALE, PaletteID.values()[3], 44L));

    @Override
    public void runTest(ClientGameTestContext c) {
        var leaf = LeafWardrobe.read(LeafWardrobe.CATALOG);
        check(Wardrobe.TOPS.stream().allMatch(g -> leaf.getAsJsonArray("tops").contains(new JsonPrimitive(g.id()))), "VF loaded only Leaf tops");
        try (var w = c.worldBuilder().create()) {
            w.getConnection().waitForChunksRender();
            for (String cmd : List.of("time set noon", "weather clear", "gamerule advance_time false")) w.getServer().runCommand(cmd);
            double[] o = w.getServer().computeOnServer(s -> {
                var p = w.getConnection().getServerPlayer();
                return new double[]{Math.floor(p.getX()) + .5, Math.floor(p.getY()), Math.floor(p.getZ()) + .5};
            });
            int x = (int) Math.floor(o[0]), y = (int) o[1], z = (int) Math.floor(o[2]);
            w.getServer().runCommand(String.format(Locale.ROOT, "fill %d %d %d %d %d %d grass_block", x - 5, y - 1, z - 2, x + 5, y - 1, z + 8));
            w.getServer().runCommand(String.format(Locale.ROOT, "fill %d %d %d %d %d %d air", x - 5, y, z - 2, x + 5, y + 4, z + 8));
            List<Integer> ids = w.getServer().computeOnServer(s -> {
                var level = w.getConnection().getServerLevel();
                var list = new ArrayList<Integer>();
                for (int i = 0; i < LOOKS.size(); i++) {
                    var v = new Villager(EntityTypes.VILLAGER, level);
                    v.setNoAi(true);
                    v.setPos(o[0] + (i - 1.5) * 1.45, o[1], o[2] + 4.6);
                    v.setYRot(180);
                    v.yBodyRot = v.yHeadRot = 180;
                    var target = VillageFriends.target(v);
                    target.setAttached(VillageFriends.PROFILE, ResidentProfile.generate(v.getUUID(), LOOKS.get(i).recipe()));
                    target.setAttached(VillageFriends.LOOK, LOOKS.get(i).recipe());
                    level.addFreshEntity(v);
                    list.add(v.getId());
                }
                return list;
            });
            w.getConnection().waitForClientboundEntityUpdates(EntityTypes.VILLAGER);
            c.waitTicks(30);
            c.runOnClient(mc -> {
                for (int i = 0; i < ids.size(); i++) {
                    var v = (Villager) mc.level.getEntity(ids.get(i));
                    var state = ((ResidentRenderer) mc.getEntityRenderDispatcher().getRenderer(v)).createRenderState(v, 1);
                    var expected = LOOKS.get(i).outfit(Profession.NONE);
                    check(state.outfit != null && state.outfit.key().equals(expected.key()), "resident " + i + " wears its Leaf outfit");
                    VillageFriends.LOGGER.info("Leaf resident {}: hair {}, top {}, bottom {}", i, expected.hair().id(), expected.top().id(), expected.bottom().id());
                }
                if (!mc.gui.hud.isHidden()) mc.gui.hud.toggle();
            });
            w.getServer().runCommand("gamemode spectator @p");
            w.getServer().runCommand(String.format(Locale.ROOT, "tp @p %.2f %.2f %.2f 0 10", o[0], o[1] + 1.45, o[2] + 1.3));
            c.waitTicks(30);
            c.takeScreenshot("leaf-residents");
        }
    }

    static void check(boolean ok, String what) {
        if (!ok) throw new AssertionError("Failed: " + what);
    }
}
