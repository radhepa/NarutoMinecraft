package dev.shinobi.progression.mission;

import org.junit.jupiter.api.Test;

import java.util.Map;

import static org.junit.jupiter.api.Assertions.*;

/** Pay bands, XP, grades and how missions end (MISSIONS.md section 3). */
class EconomyTest {
    static final Catalogue CAT = CatalogueTest.CAT;
    static final Economy E = CAT.economy;

    static Offer offer(Template t, int pay, int xp) {
        return new Offer("o", t.id(), t.rank(), Map.of("client", "resident:9"), null, false, pay, xp, 0, 2, null, null, false);
    }

    @Test void payStaysInTheBand() {
        for (Template t : CAT.all()) {
            var b = E.band(t.rank());
            for (double roll : new double[]{0, 0.25, 0.5, 0.75, 0.999}) {
                int pay = E.pay(t, roll, false, false);
                assertTrue(pay >= b.ryoLo() && pay <= b.ryoHi(), t.id() + " pays " + pay);
                assertEquals(0, pay % 5);
            }
        }
    }

    @Test void theBetasRyoRuleOfThumb() {
        var d = E.band(Rank.D);
        var c = E.band(Rank.C);
        assertEquals(60, d.ryoLo());
        assertEquals(150, d.ryoHi());
        assertEquals(300, c.ryoLo());
        assertEquals(600, c.ryoHi());
        double day = (d.ryoLo() + d.ryoHi()) / 2.0;
        double living = E.livingPerDay(0.5);
        assertTrue(living > day * 0.3 && living < day * 0.65, "a D-rank day covers food and leaves about half: " + living + " of " + day);
    }

    @Test void harderTwistsAndRequestsPayMore() {
        Template t = CAT.get("mission.d.lost_pet");
        assertTrue(E.pay(t, 0.5, true, false) > E.pay(t, 0.5, false, false));
        assertTrue(E.pay(t, 0.5, false, true) > E.pay(t, 0.5, false, false));
    }

    @Test void xpIsAShareOfALevelAtTheRanksReferenceLevel() {
        Template d = CAT.get("mission.d.delivery_run");
        double share = E.xp(d, 0.5, false) / E.xpToNext(7);
        assertTrue(share >= 0.14 && share <= 0.26, "a D-rank is about a fifth of a level at level 7: " + share);
        assertTrue(E.xp(d, 0.5, false) / E.xpToNext(14) < share, "and less at level 14");
        assertTrue(E.xp(CAT.get("mission.c.escort_merchant"), 0.5, false) > 3 * E.xp(d, 0.5, false));
    }

    @Test void gradesNeedEveryBonusForAnS() {
        Template t = CAT.get("mission.c.bandit_clearing");
        int n = t.bonuses().size();
        assertEquals(Grade.S, E.grade(E.score(t, Economy.Performance.clean(n), -1, false)));
        assertNotEquals(Grade.S, E.grade(E.score(t, Economy.Performance.clean(n - 1), -1, false)));
        assertEquals(Grade.B, E.grade(E.score(t, Economy.Performance.clean(1), -1, false)));
        assertEquals(Grade.C, E.grade(E.score(t, new Economy.Performance(false, false, false, 0, 1, true, false, false), -1, false)));
        double split = E.score(t, Economy.Performance.clean(2), 10, false), inStep = E.score(t, Economy.Performance.clean(2), 90, true);
        assertTrue(inStep - split >= 15, "cohesion and a good call move the score");
    }

    @Test void endingsPayAndCostAsTheyShould() {
        Template t = CAT.get("mission.d.harvest");
        Offer o = offer(t, 100, 100);
        var s = E.settle(t, o, Economy.Performance.clean(t.bonuses().size()), 80, true);
        assertEquals(Grade.S, s.grade());
        assertEquals(125, s.ryo());
        var partial = E.settle(t, o, new Economy.Performance(false, false, true, t.bonuses().size(), 0, false, false, false), 80, true);
        assertEquals(Grade.C, partial.grade());
        assertEquals(50, partial.ryo());
        var fail = E.settle(t, o, Economy.Performance.failure(), 80, true);
        assertNull(fail.grade());
        assertEquals(0, fail.ryo());
        assertTrue(fail.rapport() < 0 && fail.standing() < 0);
        var gone = E.settle(t, o, new Economy.Performance(false, true, false, 0, 0, false, false, false), 80, true);
        assertTrue(gone.rapport() < fail.rapport(), "abandoning costs more than failing");
    }
}
