package dev.shinobi.combat;

import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.Test;

class ResourcesTest {
    @Test void chakraGrowsWithLevelAndUzumakiBlood() {
        assertEquals(53, Scaling.maxChakra(1, 1));
        assertEquals(104, Scaling.maxChakra(18, 1));
        assertEquals(200, Scaling.maxChakra(50, 1));
        assertEquals(69, Scaling.maxChakra(1, 1.3));
    }
    @Test void controlOwnNatureAndMasteryCutTheCost() {
        double raw = Chakra.cost(18, 30, false, 1);
        assertEquals(18 * 1.06, raw, 1e-9);
        assertTrue(Chakra.cost(18, 100, false, 1) < Chakra.cost(18, 0, false, 1));
        assertEquals(raw * 0.75, Chakra.cost(18, 30, true, 1), 1e-9);
        assertEquals(raw * 0.8, Chakra.cost(18, 30, false, Mastery.costMult(Mastery.Tier.PERFECTED)), 1e-9);
    }
    @Test void aDesperateCastPaysInHealthAndExhausts() {
        var c = new Chakra(100);
        assertTrue(c.spend(90, false).ok());
        assertFalse(c.spend(12, false).ok(), "short without desperation");
        var s = c.spend(12, true);
        assertTrue(s.ok());
        assertEquals(1, s.health(), 1e-9, "2 short at 0.5 HP each");
        assertTrue(c.exhausted());
        assertFalse(c.spend(1, true).ok(), "no casting while exhausted");
        for (int i = 0; i < 20 * 20 && c.exhausted(); i++) c.tick(1);
        assertFalse(c.exhausted(), "back once a fifth of the bar returns");
        assertTrue(c.fraction() >= 0.2);
        assertFalse(new Chakra(100).spend(140, true).ok(), "never more than a quarter short");
    }
    @Test void chakraRegenIsSlowAndFasterMeditating() {
        var fight = new Chakra(100);
        fight.drain(100);
        var calm = new Chakra(100);
        calm.drain(100);
        for (int i = 0; i < 200; i++) { fight.tick(Chakra.COMBAT_MULT); calm.tick(Chakra.MEDITATE_MULT); }
        assertEquals(1.6 * 10 * 0.75, fight.value(), 1e-6, "about a minute to refill in a fight");
        assertTrue(calm.value() > fight.value() * 5);
    }
    @Test void staminaRefillsInAboutThreeSecondsAfterAPause() {
        var s = Pool.stamina(100);
        assertTrue(s.spend(22));
        assertTrue(s.spend(60));
        assertFalse(s.spend(30), "only 18 left");
        assertEquals(0, s.value(), 1e-9);
        for (int i = 0; i < 14; i++) s.tick(1);
        assertEquals(0, s.value(), 1e-9, "nothing during the pause");
        for (int i = 0; i < 70; i++) s.tick(1);
        assertTrue(s.value() >= 99, "full after about 3.5 s in all");
    }
    @Test void poiseBreaksIntoAStaggerAndRefills() {
        var p = Pool.poise(20);
        assertFalse(p.breaks(12));
        assertTrue(p.breaks(12), "the second heavy staggers");
        assertEquals(20, p.value(), 1e-9);
    }
    @Test void cooldownsRunOnTheTickClock() {
        var c = new Cooldowns();
        assertTrue(c.use("dodge", 0, 30));
        assertFalse(c.use("dodge", 29, 30));
        assertEquals(1, c.remaining("dodge", 29));
        assertTrue(c.use("dodge", 30, 30));
        assertTrue(c.ready("fireball", 0), "never used is ready");
        assertEquals(0, c.remaining("fireball", 1000), "never used has no wait");
    }
}
