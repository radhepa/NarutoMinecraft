package dev.shinobi.life.roster;

import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.Test;

class CurveAndTierTest {
    /** ROADMAP.md §7: a typical player reaches each gate at the end of its stretch's hours (XP is main-path minutes). */
    @Test void theCurveMeetsTheRoadmapsGates() {
        assertEquals(5, Curve.level(4 * 60), 1e-9);
        assertEquals(15, Curve.level(12 * 60), 1e-9);
        assertEquals(18, Curve.level(15 * 60), 1e-9);
        assertEquals(30, Curve.level(28 * 60), 1e-9);
        assertEquals(42, Curve.level(45 * 60), 1e-9);
        assertEquals(50, Curve.level(60 * 60), 1e-9);
        assertEquals(60, Curve.level(1e9));
        assertEquals(1, Curve.level(-5));
    }
    @Test void aBetaLevelTakesAboutFiftyMinutesAndLaterOnesLonger() {
        for (int l = 1; l < 18; l++) { double m = Curve.xpAt(l + 1) - Curve.xpAt(l); assertTrue(m >= 45 && m <= 60, "level " + l + ": " + m); }
        for (int l = 18; l < 50; l++) { double m = Curve.xpAt(l + 1) - Curve.xpAt(l); assertTrue(m >= 65 && m <= 113, "level " + l + ": " + m); }
    }
    @Test void fractionalLevelsRoundTrip() {
        for (double l = 1; l < 60; l += .37) assertEquals(l, Curve.level(Curve.xpAt(l)), 1e-9);
        assertEquals(Curve.xpAt(12), Curve.xpAt(12.0), 1e-9);
        assertEquals(Curve.Stretch.GENIN, Curve.Stretch.of(14.9));
        assertEquals(Curve.Stretch.EXAMS, Curve.Stretch.of(15));
    }
    @Test void tiersFollowLevelNotRank() {
        assertEquals(Tier.E, Tier.of(1)); assertEquals(Tier.E, Tier.of(4.99));
        assertEquals(Tier.D, Tier.of(5)); assertEquals(Tier.C, Tier.of(15)); assertEquals(Tier.B, Tier.of(30));
        assertEquals(Tier.A, Tier.of(42)); assertEquals(Tier.S, Tier.of(50)); assertEquals(Tier.S, Tier.of(60));
        assertEquals("elite", Tier.A.word);
    }
}
