package dev.shinobi.life.home;

import static org.junit.jupiter.api.Assertions.*;

import dev.shinobi.life.home.Piece.Source;
import java.util.List;
import java.util.Set;
import org.junit.jupiter.api.Test;

class CatalogTest {
    static final Set<String> SLICES = Set.of("b1", "b2", "b2.5", "b3", "later");

    @Test void everyPieceIsWellFormed() {
        for (var p : Catalog.PIECES.values()) {
            assertTrue(p.id().matches("[a-z_]+(\\.[a-z_]+)?"), p.id());
            assertTrue(SLICES.contains(p.slice()), p.id());
            if (p.inSet()) assertNotNull(Catalog.set(p.set()), p.id() + " names a missing set");
            if (p.source() == Source.QUEST) assertTrue(p.tags().stream().anyMatch(t -> t.startsWith("from:")), p.id() + " names no quest");
            if (p.source() == Source.SHOP) assertTrue(p.price() > 0, p.id() + " is free in the shop");
            if (p.source() == Source.SHOP) assertTrue(p.price() >= 10 && p.price() <= 1200, p.id());
        }
    }
    @Test void setsHoldTogether() {
        for (var s : Catalog.SETS.values()) {
            assertTrue(s.pieces().size() >= 3, s.id());
            for (String id : s.pieces()) assertEquals(s.id(), Catalog.piece(id).set());
        }
        assertEquals(6 + 25, Catalog.SETS.size(), "six themed sets and one per clan");
    }
    @Test void theFirstProperSetIsAboutAWeekOfSavings() {
        int cost = Catalog.set("leaf").pieces().stream().mapToInt(id -> Catalog.piece(id).price()).sum();
        // A week in the Academy saves about 45 ryo a day (ROADMAP.md, "Ryo"): the Leaf set should be roughly that.
        assertTrue(cost >= 250 && cost <= 350, "leaf set costs " + cost);
        for (String id : Catalog.STARTER) assertEquals(Source.STARTER, Catalog.piece(id).source());
    }
    @Test void everyClanHasItsPiecesAndKeepsake() {
        var clans = new java.util.ArrayList<>(Catalog.CLANS_WAVE_1); clans.addAll(Catalog.CLANS_WAVE_2);
        assertEquals(25, clans.size());
        for (String c : clans) {
            assertEquals(3, Catalog.set("clan." + c).pieces().size(), c);
            assertNotNull(Catalog.KEEPSAKES.get("clan_keepsake." + c), c);
            assertEquals("clan." + c + ".1", Catalog.KEEPSAKES.get("clan_keepsake." + c).from());
        }
    }
    @Test void counts() {
        long beta = Catalog.PIECES.values().stream().filter(p -> !p.slice().equals("later")).count();
        long clan = Catalog.PIECES.values().stream().filter(p -> p.source() == Source.CLAN).count();
        assertEquals(75, clan);
        assertEquals(156, Catalog.PIECES.size());
        assertEquals(Catalog.PIECES.size(), beta + Catalog.PIECES.values().stream().filter(p -> p.slice().equals("later")).count());
        assertEquals(39, Catalog.KEEPSAKES.size());
        assertEquals(12, Photo.MILESTONES.size());
        assertEquals(List.of("futon", "low_table", "cupboard", "storage_chest", "wardrobe_cabinet", "cooking_pot"), Catalog.STARTER);
    }
    @Test void flatsAreRolledFromTheSeedInVariedAndFixedInClassic() {
        assertSame(Flat.CLASSIC, Flat.starting(1, true));
        assertSame(Flat.CLASSIC, Flat.starting(99, true));
        var seen = new java.util.HashSet<String>();
        for (long s = 0; s < 64; s++) { seen.add(Flat.starting(s, false).id()); assertEquals(Flat.starting(s, false), Flat.starting(s, false)); }
        assertEquals(Flat.ACADEMY.size(), seen.size(), "every candidate comes up");
        for (var f : Flat.ACADEMY) assertTrue(f.cells() <= f.floor(), f.id());
    }
}
