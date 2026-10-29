package dev.shinobi.village.look;

import static org.junit.jupiter.api.Assertions.*;

import java.util.List;
import org.junit.jupiter.api.Test;

class LifeRollTest {
    final CreatorRules r = Data.RULES;

    @Test
    @SuppressWarnings("unchecked")
    void javaRollsTheSameAsThePythonTool() {
        var parity = (List<Object>) r.data.get("parity");
        assertFalse(parity.isEmpty());
        for (Object p : parity) {
            var e = CreatorRules.map(p);
            long seed = ((Number) e.get("seed")).longValue();
            assertEquals(e.get("origin"), LifeRoll.origin(r, seed), "seed " + seed);
            var rolled = LifeRoll.look(r, seed, (String) e.get("origin"));
            assertEquals(e.get("look"), LifeRoll.toMap(rolled), "seed " + seed);
            var roots = LifeRoll.roots(r, seed, rolled.look().body());
            var want = CreatorRules.map(e.get("roots"));
            assertEquals(want.get("temperament"), roots.temperament(), "seed " + seed);
            assertEquals(want.get("knack"), roots.knack(), "seed " + seed);
            assertEquals(want.get("affinity"), roots.affinity(), "seed " + seed);
        }
    }

    @Test
    void everyRollIsAllowedAndStable() {
        for (long seed = 0; seed < 400; seed++) {
            var a = LifeRoll.roll(r, seed);
            assertEquals(List.of(), r.validate(a.origin(), AgeStage.CHILD, a.look()), "seed " + seed);
            assertEquals(a, LifeRoll.roll(r, seed));
        }
    }

    @Test
    void rollsOnlyOfferWhatTheCreatorOffers() {
        for (long seed = 0; seed < 400; seed++) {
            var a = LifeRoll.roll(r, seed);
            assertTrue(r.creatable().contains(a.origin()), "seed " + seed);
            var roots = LifeRoll.roots(r, seed, a.look().body());
            assertEquals(List.of(), r.validateCreation(a.origin(), a.look(), roots), "seed " + seed);
        }
    }
}
