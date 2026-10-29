package dev.shinobi.life.economy;

import dev.shinobi.life.bond.Seeds;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

class StreamsTest {
    @Test void theSameNumbersAsTheBondEngine() {
        for (long seed : new long[]{0, 1, 20261029L, -42}) {
            assertEquals(Seeds.hash64(seed, "shops", "grocer|3"), Streams.hash64(seed, "shops", "grocer|3"));
            assertEquals(Seeds.roll(seed, "haggle", "pawn_shop", "12", "kunai"), Streams.roll(seed, "haggle", "pawn_shop", "12", "kunai"));
            var a = Seeds.stream(seed, "crafts", "x");
            var b = Streams.stream(seed, "crafts", "x");
            for (int i = 0; i < 10; i++) assertEquals(a.next(), b.next());
        }
    }
}
