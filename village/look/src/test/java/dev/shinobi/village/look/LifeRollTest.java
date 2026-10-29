package dev.shinobi.village.look;

import static org.junit.jupiter.api.Assertions.*;

import java.util.HashMap;
import java.util.List;
import java.util.Map;
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
            assertEquals(e.get("look"), LifeRoll.toMap(LifeRoll.look(r, seed, (String) e.get("origin"))), "seed " + seed);
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
    void rollsFollowThePopulationSoMostAreClanless() {
        Map<String, Integer> count = new HashMap<>();
        for (long seed = 0; seed < 4000; seed++) count.merge(LifeRoll.origin(r, seed), 1, Integer::sum);
        double clanless = count.getOrDefault(CreatorRules.CLANLESS, 0) / 4000.0;
        int total = r.population().values().stream().mapToInt(Integer::intValue).sum();
        assertEquals(r.population().get(CreatorRules.CLANLESS) / (double) total, clanless, 0.03);
        assertTrue(count.getOrDefault("hatake", 0) < count.getOrDefault("uchiha", 0));
    }
}
