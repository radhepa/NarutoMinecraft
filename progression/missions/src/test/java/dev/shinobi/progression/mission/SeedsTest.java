package dev.shinobi.progression.mission;

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertEquals;

/** The desk's seed streams are Core's and the bond engine's, bit for bit (ROADMAP.md, "One seed, many streams"). */
class SeedsTest {
    @Test void sameStreamsAsTheBondEngine() {
        for (long seed : new long[]{0, 1, 20261029L, -7L, Long.MAX_VALUE}) {
            for (String key : new String[]{"desk|21|d", "request|40", "", "chain|chain.kiln|33"}) {
                assertEquals(dev.shinobi.life.bond.Seeds.hash64(seed, "missions", key), Seeds.hash64(seed, "missions", key));
                var a = dev.shinobi.life.bond.Seeds.stream(seed, "missions", key);
                var b = Seeds.stream(seed, "missions", key);
                for (int k = 0; k < 8; k++) assertEquals(a.next(), b.next());
                assertEquals(dev.shinobi.life.bond.Seeds.roll(seed, "missions", "weight", key), Seeds.roll(seed, "missions", "weight", key));
            }
        }
    }
}
