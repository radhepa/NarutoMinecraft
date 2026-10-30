package dev.shinobi.village;

import dev.villagefriends.home.House;
import dev.villagefriends.home.HousingIndex;
import dev.villagefriends.social.Townsfolk;
import net.minecraft.core.BlockPos;
import net.minecraft.core.Direction;
import net.minecraft.world.level.levelgen.structure.BoundingBox;
import org.junit.jupiter.api.AfterEach;
import org.junit.jupiter.api.Test;

import java.util.List;
import java.util.Map;
import java.util.Optional;

import static org.junit.jupiter.api.Assertions.assertEquals;

class LeafFlatsTest {
    @AfterEach
    void clearClaims() { LeafFlats.CLAIMS.clear(); }

    static House flat(String id, int x, String name, boolean closed) {
        var foot = new BlockPos(x, 64, 0);
        var bed = new House.Bed(foot.relative(Direction.NORTH), foot, Direction.NORTH, 0, true);
        return new House(id, House.Kind.PLAYER, "", House.Use.HOME, new BoundingBox(x, 60, -2, x + 3, 70, 2), List.of(new House.Room("room0", new BoundingBox(x, 64, -1, x + 1, 65, 1))),
                List.of(bed), List.of(), List.of(), Optional.of(new BlockPos(x, 65, 1)), name, closed, true, 1);
    }

    static BlockPos head(House h) { return h.beds().getFirst().head(); }

    static Townsfolk folk(String id, String status) {
        return new Townsfolk(id, id, "FEMALE", "none", "warmhearted", true, 0, 0, status, "", -1, false, Map.of(), "", -1);
    }

    @Test
    void residentsKeepFreeLeafFlatBedsTheySleepIn() {
        var a = flat("a", 0, "Flat 1a", false); var b = flat("b", 10, "Flat 1b", false); var shut = flat("c", 20, "Flat 1c", true);
        var own = flat("d", 30, "My house", false); var held = flat("e", 40, "Flat 2a", false);
        var shop = flat("f", 50, LeafFlats.TEA_HOUSE, false);
        var previous = new HousingIndex("v", List.of(a, b, shut, own, held, shop), Map.of("holder", new HousingIndex.BedKey("e", head(held))),
                List.of(), Map.of(), List.of(), Map.of(), Map.of(), 0, true);
        var folk = List.of(folk("ann", Townsfolk.HOME), folk("bo", Townsfolk.HOME), folk("cy", Townsfolk.HOME), folk("di", Townsfolk.HOME),
                folk("ed", Townsfolk.HOME), folk("gone", Townsfolk.PASSED), folk("holder", Townsfolk.HOME), folk("fay", Townsfolk.HOME));
        var anchors = Map.of("ann", head(a), "bo", head(a), "cy", head(shut), "di", head(own), "ed", head(held), "gone", head(b), "fay", head(shop));
        var beds = LeafFlats.seed(previous, folk, anchors).beds();
        // ann keeps flat a and fay the tea house (bo shares the anchor and gets nothing); a private flat, a player's own house, a held bed and the dead are skipped.
        assertEquals(Map.of("holder", new HousingIndex.BedKey("e", head(held)), "ann", new HousingIndex.BedKey("a", head(a)),
                "fay", new HousingIndex.BedKey("f", head(shop))), beds);
    }

    @Test
    void placedResidentsTakeTheirBedBackOnce() {
        var sakura = flat("s", 0, "Flat 1a", false); var spare = flat("t", 10, "Flat 2c", false);
        // VF handed out beds before it noted where cy sleeps: cy got the spare flat and bo the bed cy claims.
        var previous = new HousingIndex("v", List.of(sakura, spare), Map.of("cy", new HousingIndex.BedKey("t", head(spare)), "bo", new HousingIndex.BedKey("s", head(sakura))),
                List.of(), Map.of(), List.of(), Map.of(), Map.of(), 0, true);
        LeafFlats.CLAIMS.put("cy", head(sakura));
        var beds = LeafFlats.seed(previous, List.of(folk("cy", Townsfolk.HOME), folk("bo", Townsfolk.HOME)), Map.of()).beds();
        assertEquals(Map.of("cy", new HousingIndex.BedKey("s", head(sakura))), beds);
        // Granted once, the claim is spent: after VF moves cy to the spare flat, a later seed leaves cy there.
        assertEquals(null, LeafFlats.CLAIMS.get("cy"));
        var moved = Map.of("cy", new HousingIndex.BedKey("t", head(spare)));
        var next = new HousingIndex("v", List.of(sakura, spare), moved, List.of(), Map.of(), List.of(), Map.of(), Map.of(), 0, true);
        assertEquals(moved, LeafFlats.seed(next, List.of(folk("cy", Townsfolk.HOME)), Map.of()).beds());
    }
}
