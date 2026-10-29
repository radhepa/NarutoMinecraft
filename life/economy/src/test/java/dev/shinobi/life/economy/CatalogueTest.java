package dev.shinobi.life.economy;

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

/** The compiled data seen from Java: what tools/items/items.py --check enforces, held again where the code reads it. */
class CatalogueTest {
    final Catalogue c = Data.catalogue();
    final Prices prices = new Prices(c);

    @Test void everythingOnAShelfIsAnItemWithAPrice() {
        assertTrue(c.items.size() > 350);
        assertTrue(c.shops.size() >= 25);
        for (var shop : c.shops.values()) {
            assertFalse(shop.interior().isEmpty(), shop.id());
            for (var line : shop.stock()) {
                String key = line.variant().isEmpty() || line.item().equals("folded_outfit") ? line.item() : line.item() + "@" + line.variant();
                assertTrue(c.items.containsKey(line.item()), shop.id() + " sells " + line.item());
                if (!line.item().equals("folded_outfit"))
                    assertTrue(prices.buy(key, shop, "standard", "newcomer", 0) > 0, shop.id() + " gives " + key + " no price");
            }
        }
    }

    @Test void recipesUseKnownThingsAndCraftingNeverPrintsRyo() {
        var sold = new java.util.HashSet<String>();
        c.shops.values().forEach(s -> s.stock().forEach(l -> sold.add(l.item())));
        for (var r : c.recipes.values()) {
            assertTrue(c.stations.containsKey(r.station()) || r.station().startsWith("cooking."), r.id());
            r.inputs().forEach(in -> assertTrue(c.items.containsKey(in.item()), r.id() + ": " + in.item()));
            var out = c.item(r.output());
            int cost = r.inputs().stream().mapToInt(in -> Math.max(c.item(in.item()).price(), c.item(in.item()).sell()) * in.count()).sum();
            assertTrue(out.sell() * r.count() < Math.max(cost, 1), r.id() + " sells back for more than it costs");
            // A vessel comes back when the dish is eaten (VF), so it is not part of what a craft costs.
            int ingredients = r.inputs().stream().mapToInt(in -> c.item(in.item()).price() * in.count()).sum();
            if (sold.contains(out.id()) && out.price() > 0 && !r.slice().equals("later"))
                assertTrue(ingredients <= out.price() * r.count(), r.id() + " costs more to craft (" + ingredients + ") than to buy");
        }
    }

    @Test void kitsAndJobsAndServicesHoldTogether() {
        c.kits.forEach((kit, parts) -> parts.forEach(p -> assertTrue(c.items.containsKey(p.item()), kit + ": " + p.item())));
        for (var job : c.jobs.values()) {
            assertTrue(c.shops.containsKey(job.shop()), job.id());
            assertTrue(job.pay() >= 40 && job.pay() <= 80, job.id() + " pays within ROADMAP's 40 to 80 a shift");
        }
        assertEquals(8, c.services.get("service.bath").price());
        assertTrue(c.items.values().stream().anyMatch(i -> i.prop("set").equals("starter")));
    }

    @Test void ryoNotesAreTheFourDenominations() {
        for (int note : Ryo.NOTES) assertEquals(note, c.item("ryo_" + note).price());
    }
}
