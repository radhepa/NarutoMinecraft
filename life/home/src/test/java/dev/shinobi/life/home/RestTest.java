package dev.shinobi.life.home;

import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.Test;

class RestTest {
    @Test void aBareFlatGivesTheRoadmapsWellRested() {
        var r = Rest.sleep(ComfortTest.score(new Home("player", Flat.CLASSIC)), 22, true);
        assertEquals(.10, r.regen(), 1e-9);
        assertEquals(12, r.until());
    }
    @Test void aComfierHomeRestsBetterAndTheLeafSetAddsAnHour() {
        var r = Rest.sleep(ComfortTest.score(ComfortTest.leafFlat()), 22, true);
        assertEquals(.12, r.regen(), 1e-9);
        assertEquals(14, r.until(), "comfortable until 13:00, one more for the Leaf set");
    }
    @Test void lateNightsAreForgivenOnlyByAHomelyHome() {
        assertFalse(Rest.sleep(ComfortTest.score(ComfortTest.leafFlat()), 1, true).any());
        var h = ComfortTest.leafFlat();
        for (String id : new String[]{"futon_deluxe", "kotatsu", "rug", "zabuton", "tea_table", "andon_lamp", "potted_fern", "curtains"}) h.place(id);
        h.plant.water(0);
        var s = Comfort.of(h, 0, 3, "");
        assertTrue(s.tier().compareTo(Comfort.Tier.HOMELY) >= 0, "comfort " + s.comfort());
        var late = Rest.sleep(s, 1, true);
        assertEquals(.05, late.regen(), 1e-9);
        assertFalse(Rest.sleep(s, 3, true).any());
    }
    @Test void onlyYourOwnBed() {
        assertFalse(Rest.sleep(ComfortTest.score(ComfortTest.leafFlat()), 21, false).any());
    }
}
