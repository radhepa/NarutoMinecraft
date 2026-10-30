package dev.shinobi.combat;

import static org.junit.jupiter.api.Assertions.*;

import dev.shinobi.combat.Kindle.Tier;
import java.util.LinkedHashMap;
import java.util.Map;
import org.junit.jupiter.api.Test;

class KindleTest {
    @Test void deeperBondsKindleBiggerAndCostMore() {
        double last = 1;
        for (var t : new Tier[]{Tier.SPARK, Tier.FLAME, Tier.BLAZE}) {
            var b = Kindle.boost(t);
            assertTrue(b.power() > last, t + " grows the technique more");
            last = b.power();
        }
        assertFalse(Kindle.boost(Tier.SPARK).revives(), "a spark heals more, a flame revives");
        assertTrue(Kindle.boost(Tier.FLAME).revives());
        assertEquals(0, Kindle.cost(30, Tier.NONE));
        assertTrue(Kindle.cost(30, Tier.BLAZE) > Kindle.cost(30, Tier.SPARK));
        assertEquals(Kindle.Boost.NONE, Kindle.boost(Tier.NONE), "useless with strangers");
    }
    @Test void overuseBurnsChakraAndStamina() {
        assertEquals(new Kindle.Burn(0, 0), Kindle.overuse(3, 200), "three a minute are free");
        var burn = Kindle.overuse(4, 200);
        assertEquals(20, burn.chakra(), 1e-9);
        assertEquals(30, burn.stamina(), 1e-9);
        assertEquals(burn, Kindle.overuse(5, 200), "each one past three burns the same");
    }
    @Test void emberLinkSharesOnePoolAndSpreadsTheBlow() {
        var chakra = new LinkedHashMap<String, Double>();
        chakra.put("player", 20.0);
        chakra.put("role:teammate_a", 60.0);
        chakra.put("role:teammate_b", 40.0);
        var link = new Kindle.EmberLink(chakra);
        assertEquals(120, link.shared(), 1e-9);
        assertTrue(link.draw("player", 50), "the player casts beyond their own bar");
        assertEquals(0, link.chakra("player"), 1e-9);
        assertEquals(70, link.chakra("role:teammate_a") + link.chakra("role:teammate_b"), 1e-9);
        assertFalse(link.draw("player", 500));
        var hit = link.spread("role:teammate_b", 12);
        assertEquals(6, hit.get("role:teammate_b"), 1e-9);
        assertEquals(3, hit.get("player"), 1e-9, "you feel your allies' pain");
        assertEquals(12, hit.values().stream().mapToDouble(Double::doubleValue).sum(), 1e-9);
        assertThrows(IllegalArgumentException.class, () -> new Kindle.EmberLink(Map.of("a", 1.0, "b", 1.0, "c", 1.0, "d", 1.0, "e", 1.0)));
    }
    @Test void bonfireScalesWithTheWholeBondWeb() {
        var candle = Kindle.bonfire(3);
        var typical = Kindle.bonfire(19);
        var devoted = Kindle.bonfire(22);
        assertEquals(1.0, Kindle.bonfire(0).damage(), 1e-9);
        assertTrue(candle.damage() < 1.15, "a loner gets a candle: " + candle.damage());
        assertEquals(1.63, typical.damage(), 0.01, "the bond engine's typical player at 60 hours");
        assertEquals(1.70, devoted.damage(), 0.01);
        assertTrue(devoted.taken() < candle.taken());
        assertTrue(Kindle.bonfire(200).damage() < 2.5 + 1e-9, "diminishing returns");
    }
    @Test void threadSightWarnsOnlyForBondedAllies() {
        assertEquals(0, Kindle.threadWarning(Tier.NONE));
        assertTrue(Kindle.threadWarning(Tier.BLAZE) > Kindle.threadWarning(Tier.SPARK));
    }
}
