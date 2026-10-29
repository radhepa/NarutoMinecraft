package dev.shinobi.life.bond;

import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.Test;

class LevelsTest {
    @Test void feelingThresholdsLineUpWithVillageFriendsPoints() {
        for (int level = 0; level <= Levels.MAX; level++) {
            double f = Levels.feelingFor(level);
            var m = Meters.of(f, f, f, 0);
            assertEquals(f, Levels.feeling(m), 1e-9);
            assertEquals(Levels.threshold(level), Levels.closeness(m), 1e-6, "level " + level);
            assertEquals(level, Levels.byPoints(Levels.closeness(m)));
        }
        double last = -1;
        for (int f = -40; f <= 100; f++) { double c = Levels.closeness(Meters.of(f, f, f, 0)); assertTrue(c >= last); last = c; }
        assertEquals(0, Levels.closeness(Meters.of(-50, 0, 0, 0)));
        assertEquals("Lifelong Bond", Levels.name(10));
    }
    @Test void aRivalWhoRespectsYouCanBeCloseWithoutLikingYou() {
        var rival = Meters.of(10, 30, 70, 60);
        var stranger = Meters.of(10, 30, 10, 0);
        assertTrue(Levels.byPoints(Levels.closeness(rival)) >= Levels.byPoints(Levels.closeness(stranger)) + 2);
        var sweetheart = new Meters(60, 60, 30, 0, 90);
        assertTrue(Levels.closeness(sweetheart) > Levels.closeness(new Meters(60, 60, 30, 0, 0)), "romance counts as regard");
    }
    @Test void storyGatesNeedRealMoments() {
        assertEquals(3, Levels.cap(0, 0, 100), "points alone stop at 3");
        assertEquals(5, Levels.cap(1, 0, 100), "a shared experience opens 4 and 5");
        assertEquals(7, Levels.cap(5, 1, 100), "a moment opens 6 and 7");
        assertEquals(7, Levels.cap(5, 3, Levels.DAYS_PAST_7 - 1), "and some time");
        assertEquals(8, Levels.cap(5, 2, 100));
        assertEquals(9, Levels.cap(5, 3, 100));
        assertEquals(10, Levels.cap(5, 4, Levels.DAYS_PAST_9));
        assertEquals("experience", Levels.gate(0, 0, 0, 3));
        assertEquals("moment", Levels.gate(1, 0, 0, 5));
        assertEquals("time", Levels.gate(1, 3, 10, 7));
        assertEquals("", Levels.gate(1, 0, 0, 2));
    }
    @Test void levelsRiseAtOnceAndFallSlowly() {
        assertEquals(6, Levels.next(2, Levels.threshold(6), 10), "rises straight to what was earned");
        assertEquals(5, Levels.next(2, Levels.threshold(6), 5), "up to the gate");
        assertEquals(6, Levels.next(6, Levels.threshold(6) - Levels.SLACK + 1, 10), "a dip within the slack keeps the level");
        assertEquals(5, Levels.next(6, Levels.threshold(6) - Levels.SLACK - 1, 10), "a real drop costs one level a day");
        assertEquals(5, Levels.next(6, 0, 10));
    }
    @Test void aBondInTheWorldStopsAtItsGateUntilAMoment() {
        var w = new BondWorld(3, 0);
        w.add(Leaf.classmate("x", "warmhearted"));
        for (int d = 0; d < 60; d++) { w.talk("x"); w.gift("x", "food:dango"); w.gift("x", "food:honey"); w.endDay(); }
        assertEquals(3, w.level("x"), "gifts and talk alone reach level 3 and stop there");
        assertEquals(3, Levels.cap(w.bond("x").experiences(), w.bond("x").moments().size(), w.bond("x").contactDays()));
        for (int d = 0; d < 20; d++) {
            w.experience(Act.MISSION_TOGETHER, java.util.List.of("x")); w.act("x", Act.CAMP_NIGHT); w.act("x", Act.STOOD_BY_THEM);
            w.act("x", Act.PROTECTED_THEM); w.act("x", Act.HEART_TO_HEART); w.act("x", Act.KEPT_PROMISE); w.endDay();
        }
        assertEquals(5, w.level("x"));
        assertEquals("moment", w.gate("x"));
        w.moment("x", "bond.x.1");
        assertTrue(w.level("x") > 5, "the moment opens the next levels at once");
        assertTrue(w.drainEvents().stream().anyMatch(e -> e.kind().equals("gated")));
    }
}
