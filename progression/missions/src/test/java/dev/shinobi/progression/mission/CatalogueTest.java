package dev.shinobi.progression.mission;

import org.junit.jupiter.api.Test;

import java.util.HashSet;
import java.util.Map;

import static org.junit.jupiter.api.Assertions.*;

/** The compiled catalogue loads, holds together and is as big and varied as MISSIONS.md promises. */
class CatalogueTest {
    static final Catalogue CAT = Catalogue.load();

    @Test void noProblems() {
        assertEquals(java.util.List.of(), CAT.problems());
    }

    @Test void countsPerRank() {
        long d = CAT.of(Rank.D).stream().filter(t -> !t.later()).count();
        long c = CAT.of(Rank.C).stream().filter(t -> !t.later()).count();
        assertTrue(d >= 40, "D-rank templates in the beta: " + d);
        assertTrue(c >= 24, "C-rank templates in the beta: " + c);
        assertTrue(CAT.of(Rank.B).size() >= 12);
        assertTrue(CAT.of(Rank.A).size() >= 10);
        assertTrue(CAT.of(Rank.S).size() >= 4);
        assertTrue(CAT.all().stream().filter(t -> t.category().equals("anbu")).count() >= 5);
        for (Rank r : new Rank[]{Rank.B, Rank.A, Rank.S}) assertTrue(CAT.of(r).stream().allMatch(Template::later), r + " is later content");
    }

    @Test void dRanksCoverVillageLife() {
        var cats = new HashSet<String>();
        CAT.of(Rank.D).forEach(t -> cats.add(t.category()));
        for (String c : new String[]{"farm", "shop", "delivery", "pets", "childcare", "repairs", "festival", "clearing", "river",
                "harvest", "inventory", "posters", "academy", "hospital"})
            assertTrue(cats.contains(c), "a D-rank about " + c);
        assertTrue(cats.size() >= 20, "D-rank categories: " + cats.size());
    }

    @Test void everyTwistChangesTheJob() {
        for (Template t : CAT.all()) {
            assertTrue(t.twists().size() >= 2, t.id());
            for (Template.Twist tw : t.twists()) {
                if (tw.modifier()) continue;
                assertNotEquals(t.path(null, Map.of()), t.path(tw.id(), Map.of()), t.id() + " twist " + tw.id());
            }
        }
    }

    @Test void cRanksFightAndChoose() {
        for (Template t : CAT.of(Rank.C)) {
            assertFalse(t.enemies().isEmpty(), t.id() + " has a real fight");
            assertTrue(t.steps().values().stream().anyMatch(s -> s.type().equals("defeat") || s.actions().stream().anyMatch(a -> a.containsKey("spawn_group"))), t.id());
        }
        long withChoice = CAT.of(Rank.C).stream().filter(t -> t.steps().values().stream().anyMatch(s -> s.type().equals("choose"))).count();
        assertTrue(withChoice >= 12, "C-ranks with a choice: " + withChoice);
    }

    @Test void idsAndBandsAreConsistent() {
        for (Template t : CAT.all()) {
            String[] parts = t.id().split("\\.");
            assertEquals("mission", parts[0]);
            assertTrue(parts[1].equals(t.rank().id()) || (parts[1].equals("anbu") && t.category().equals("anbu")), t.id());
            assertTrue(t.payWeight() >= 0 && t.payWeight() <= 1, t.id());
            var band = CAT.economy.band(t.rank());
            if (t.rank() == Rank.D) assertTrue(t.minutes() >= band.minLo() && t.minutes() <= band.minHi(), t.id() + " minutes " + t.minutes());
            if (t.bonuses().contains("fast")) assertTrue(t.fastHours() > 0, t.id());
        }
    }

    @Test void placesAreListed() {
        for (Template t : CAT.all())
            for (var slot : t.slots().values())
                if ("anchor".equals(slot.get("pick"))) assertTrue(t.anchors().contains((String) slot.get("tag")), t.id());
        long far = CAT.all().stream().filter(t -> !t.later() && !t.regions().isEmpty()).count();
        assertTrue(far >= 10, "beta templates on the roads and in the far region: " + far);
    }
}
