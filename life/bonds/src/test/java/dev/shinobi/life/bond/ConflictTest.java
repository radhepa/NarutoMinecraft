package dev.shinobi.life.bond;

import static org.junit.jupiter.api.Assertions.*;

import dev.shinobi.life.bond.Conflict.State;
import org.junit.jupiter.api.Test;

class ConflictTest {
    static BondWorld friends(String archetype) {
        var w = new BondWorld(11, 0);
        w.add(Leaf.classmate("x", archetype));
        for (int d = 0; d < 30; d++) { w.talk("x"); w.experience(Act.MISSION_TOGETHER, java.util.List.of("x")); w.endDay(); }
        w.moment("x", "bond.x.1");
        return w;
    }

    @Test void anArgumentThenTheColdShoulderThenMakingUp() {
        var w = friends("steadfast");
        int before = w.level("x");
        w.quarrel("x", Act.QUARREL);
        assertEquals(State.ARGUMENT, w.bond("x").conflict().state());
        assertEquals(before - 1, w.effectiveLevel("x"), "they act a level colder");
        w.endDay();
        assertEquals(State.COLD_SHOULDER, w.bond("x").conflict().state());
        assertEquals(Math.max(0, w.level("x") - 2), w.effectiveLevel("x"));
        double warmth = w.bond("x").warmth();
        w.talk("x");
        assertEquals(warmth, w.bond("x").warmth(), 1e-9, "the cold shoulder: talk gets nothing through");
        assertFalse(w.reconcile("x"), "not ready yet");
        int guard = 0;
        while (w.bond("x").conflict().state() != State.MAKING_UP && guard++ < 30) w.endDay();
        assertEquals(State.MAKING_UP, w.bond("x").conflict().state());
        assertTrue(BondConditions.test(w, java.util.Map.of("bond_state", java.util.List.of("x", "making_up"))));
        assertTrue(w.reconcile("x"));
        assertEquals(State.NONE, w.bond("x").conflict().state());
        assertTrue(w.bond("x").remembers(Act.RECONCILED), "a mended bond remembers it for good");
        assertEquals(w.level("x"), w.effectiveLevel("x"));
    }
    @Test void anApologyIsAcceptedOnTrustOrTimeAndHalvesTheColdShoulder() {
        var p = Personality.of("proud", "surpass_a_rival");
        var c = Conflict.NONE.hurt(Act.QUARREL, 30, p, 10).tick(10);
        assertEquals(State.COLD_SHOULDER, c.state());
        assertFalse(c.apologyAccepted(20, 11));
        assertTrue(c.apologyAccepted(45, 11), "they trust you");
        assertTrue(c.apologyAccepted(20, 10 + Conflict.APOLOGY_DAYS), "or enough time has passed");
        var softer = c.apologized(11);
        assertTrue(softer.until() < c.until());
        assertTrue(Conflict.coldDays(30, p) > Conflict.coldDays(30, Personality.of("gentle", "")), "the proud sulk longer");
    }
    @Test void aMildQuarrelBlowsOverAndABadOneHardens() {
        var p = Personality.of("steadfast", "");
        var mild = Conflict.NONE.hurt(Act.QUARREL, 10, p, 0);
        var bad = Conflict.NONE.hurt(Act.QUARREL, Conflict.HARDENS + 5, p, 0);
        for (long d = 0; d < 80; d++) { mild = mild.tick(d); bad = bad.tick(d); }
        assertEquals(State.NONE, mild.state());
        assertEquals(State.FALLING_OUT, bad.state());
        assertEquals(Conflict.FALLEN_CAP, bad.cap(9));
        assertEquals(0, bad.warmthLet());
    }
    @Test void aThirdStrikeOrABetrayalIsAPermanentFallingOut() {
        var p = Personality.of("steadfast", "");
        var c = Conflict.NONE.hurt(Act.QUARREL, 15, p, 0).hurt(Act.RUDE, 15, p, 1);
        assertEquals(State.ARGUMENT, c.state());
        assertEquals(State.FALLING_OUT, c.hurt(Act.RUDE, 15, p, 2).state());
        assertEquals(State.FALLING_OUT, Conflict.NONE.hurt(Act.BROKE_SECRET, Conflict.BREAKS, p, 0).state());
        var w = friends("steadfast");
        w.act("x", Act.QUARREL); w.act("x", Act.BROKE_SECRET);
        assertTrue(w.bond("x").conflict().broken());
        w.advance(200);
        assertTrue(w.bond("x").conflict().broken(), "permanent");
        assertTrue(w.effectiveLevel("x") <= Conflict.FALLEN_CAP);
        assertFalse(w.reconcile("x"));
        w.mend("x");
        assertEquals(State.NONE, w.bond("x").conflict().state(), "only the story mends it");
    }
    @Test void professionalSetbacksCostTrustButStartNoQuarrel() {
        var w = friends("stern");
        for (int i = 0; i < 3; i++) w.act("x", Act.DISOBEYED_ORDERS);
        assertEquals(State.NONE, w.bond("x").conflict().state());
        assertTrue(w.bond("x").remembers(Act.DISOBEYED_ORDERS));
    }
}
