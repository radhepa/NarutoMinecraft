package dev.shinobi.progression.mission;

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

/** Every template's slots can be cast in a real-sized village (MISSIONS.md section 4). */
class SlotFillerTest {
    static final Catalogue CAT = CatalogueTest.CAT;

    @Test void everyTemplateFillsInTheSampleVillage() {
        for (long seed = 1; seed <= 10; seed++) {
            var village = new SampleVillage(seed, CAT);
            var filler = new SlotFiller(village);
            var guard = new VarietyGuard(Json.map(CAT.desk.get("variety")));
            for (Template t : CAT.all()) {
                var slots = filler.fill(t, Seeds.stream(seed, "missions", t.id()), guard, 0, null);
                assertNotNull(slots, t.id() + " could not be cast");
                for (var e : t.slots().entrySet()) {
                    String v = slots.get(e.getKey());
                    assertNotNull(v, t.id() + " slot " + e.getKey());
                    if ("suspect".equals(e.getValue().get("pick")))
                        assertTrue(Json.strings(e.getValue().get("from")).stream().anyMatch(s -> v.equals(slots.get(s))), t.id());
                }
            }
        }
    }

    @Test void queriesMatchTheProfile() {
        var village = new SampleVillage(3, CAT);
        var filler = new SlotFiller(village);
        var guard = new VarietyGuard(Json.map(CAT.desk.get("variety")));
        Template pets = CAT.get("mission.d.lost_pet"), tutoring = CAT.get("mission.d.tutoring"), fence = CAT.get("mission.d.fence_mending");
        for (int k = 0; k < 20; k++) {
            var a = filler.fill(pets, Seeds.stream(3, "t", "a" + k), guard, 0, null);
            assertTrue(filler.resident(a.get("client")).hasPet());
            var b = filler.fill(tutoring, Seeds.stream(3, "t", "b" + k), guard, 0, null);
            assertEquals(b.get("client"), filler.resident(b.get("parent")).parentOf(), "the parent is the pupil's");
            var c = filler.fill(fence, Seeds.stream(3, "t", "c" + k), guard, 0, null);
            assertEquals(filler.resident(c.get("client")).district(), filler.resident(c.get("neighbour")).district());
            assertNotEquals(c.get("client"), c.get("neighbour"));
        }
    }

    @Test void travellersOnlyWhereTheSlotAllowsThem() {
        var village = new SampleVillage(5, CAT);
        var filler = new SlotFiller(village);
        var guard = new VarietyGuard(Json.map(CAT.desk.get("variety")));
        for (Template t : CAT.all()) {
            var slots = filler.fill(t, Seeds.stream(5, "t", t.id()), guard, 0, null);
            for (var e : t.slots().entrySet()) {
                if (!"resident".equals(e.getValue().get("pick"))) continue;
                Resident r = filler.resident(slots.get(e.getKey()));
                if (r.traveller()) assertEquals("any", Json.map(e.getValue().get("where")).get("resident_of"), t.id() + " " + e.getKey());
            }
        }
    }

    @Test void freshClientsArePreferred() {
        var village = new SampleVillage(7, CAT);
        var filler = new SlotFiller(village);
        var guard = new VarietyGuard(Json.map(CAT.desk.get("variety")));
        Template t = CAT.get("mission.d.elder_errands");
        var first = filler.fill(t, Seeds.stream(7, "t", "1"), guard, 10, null);
        guard.taken(new Offer("o", t.id(), Rank.D, first, null, false, 80, 80, 10, 12, null, null, false), t, 10);
        for (int k = 0; k < 30; k++)
            assertNotEquals(first.get("client"), filler.fill(t, Seeds.stream(7, "t", "x" + k), guard, 11, null).get("client"));
        assertTrue(guard.clientFresh(first.get("client"), 14));
        assertFalse(guard.clientFresh(first.get("client"), 13));
    }
}
