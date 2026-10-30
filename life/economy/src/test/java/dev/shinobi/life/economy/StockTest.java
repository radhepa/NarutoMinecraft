package dev.shinobi.life.economy;

import org.junit.jupiter.api.Test;

import java.util.HashSet;
import java.util.List;

import static org.junit.jupiter.api.Assertions.*;

class StockTest {
    final Catalogue c = Data.catalogue();

    static List<String> ids(List<Catalogue.Line> lines) {
        return lines.stream().map(l -> l.variant().isEmpty() ? l.item() : l.item() + "@" + l.variant()).toList();
    }

    @Test void rankAndSliceGateTheShelf() {
        var weapons = c.shops.get("weapon_shop");
        var academy = ids(Stock.shelf(weapons, 0, Stock.Mode.CLASSIC, 1, "academy", "beta1"));
        assertTrue(academy.contains("practice_kunai"));
        assertFalse(academy.contains("kunai"));
        var genin = ids(Stock.shelf(weapons, 0, Stock.Mode.CLASSIC, 1, "genin", "beta2"));
        assertTrue(genin.contains("kunai"));
        assertFalse(genin.contains("ninjato"));                     // Chunin stock, later
        assertTrue(Stock.shelf(c.shops.get("tool_shop"), 0, Stock.Mode.CLASSIC, 1, "genin", "beta1").isEmpty());
    }

    @Test void aShopsOwnRankGatesItsWholeShelf() {
        var tools = c.shops.get("tool_shop");                      // Genin and up
        assertTrue(Stock.shelf(tools, 0, Stock.Mode.CLASSIC, 1, "academy", "beta2").isEmpty());
        assertFalse(Stock.shelf(tools, 0, Stock.Mode.CLASSIC, 1, "chunin", "beta2").isEmpty());
        var supply = c.shops.get("academy_supply");                // Academy rank only
        assertFalse(Stock.shelf(supply, 0, Stock.Mode.CLASSIC, 1, "academy", "beta1").isEmpty());
        assertTrue(Stock.shelf(supply, 0, Stock.Mode.CLASSIC, 1, "genin", "beta1").isEmpty());
    }

    @Test void classicRotatesInOrderAndVariedRollsBySeed() {
        var furniture = c.shops.get("furniture_shop");
        var weeks = new HashSet<List<String>>();
        for (int week = 0; week < 6; week++) weeks.add(ids(Stock.shelf(furniture, week, Stock.Mode.CLASSIC, 1, "genin", "beta2")));
        assertTrue(weeks.size() > 1, "the rotating slots change week to week");
        assertEquals(ids(Stock.shelf(furniture, 3, Stock.Mode.CLASSIC, 1, "genin", "beta2")),
                ids(Stock.shelf(furniture, 3, Stock.Mode.CLASSIC, 999, "genin", "beta2")), "Classic ignores the seed");
        assertEquals(ids(Stock.shelf(furniture, 3, Stock.Mode.VARIED, 42, "genin", "beta2")),
                ids(Stock.shelf(furniture, 3, Stock.Mode.VARIED, 42, "genin", "beta2")), "the same seed, the same shelf");
        boolean differs = false;
        for (long seed = 1; seed < 20 && !differs; seed++)
            differs = !ids(Stock.shelf(furniture, 3, Stock.Mode.VARIED, seed, "genin", "beta2"))
                    .equals(ids(Stock.shelf(furniture, 3, Stock.Mode.VARIED, 0, "genin", "beta2")));
        assertTrue(differs, "Varied saves differ");
        int core = (int) furniture.core().stream().filter(l -> Stock.open(l, "genin", "beta2")).count();
        assertEquals(core + furniture.rotating(), Stock.shelf(furniture, 5, Stock.Mode.VARIED, 7, "genin", "beta2").size());
    }

    @Test void restockRefillsByPeriod() {
        var ikebana = c.shops.get("flower_shop").stock().stream().filter(l -> l.item().equals("ikebana")).findFirst().orElseThrow();
        assertEquals("3d", ikebana.restock());
        assertEquals(1, Stock.left(ikebana, 4, 3, 3));              // days 3 and 4 share a period
        assertEquals(ikebana.qty(), Stock.left(ikebana, 6, 4, 3));  // day 6 starts a new one
        var ramen = c.shops.get("ichiraku").stock().getFirst();
        assertEquals(Integer.MAX_VALUE, Stock.left(ramen, 1, 1, 500));
    }
}
