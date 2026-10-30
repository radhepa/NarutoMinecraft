package dev.shinobi.core;

import org.junit.jupiter.api.Test;

import java.util.stream.LongStream;

import static org.junit.jupiter.api.Assertions.*;

class SeedsTest {
    static long[] draw(Seeds.Rng r) { return LongStream.generate(r::next).limit(8).toArray(); }

    @Test void theSameSeedGivesTheSameStream() {
        assertArrayEquals(draw(new SaveSeed(20261029L, "varied").stream("cast", "rival")),
                draw(new SaveSeed(20261029L, "classic").stream("cast", "rival")));
    }

    @Test void seedsDomainsAndKeysEachGiveTheirOwnStream() {
        long[] base = draw(Seeds.stream(1, "cast", "rival"));
        assertFalse(java.util.Arrays.equals(base, draw(Seeds.stream(2, "cast", "rival"))));
        assertFalse(java.util.Arrays.equals(base, draw(Seeds.stream(1, "residents", "rival"))));
        assertFalse(java.util.Arrays.equals(base, draw(Seeds.stream(1, "cast", "sensei"))));
    }

    @Test void drawingFromOneStreamLeavesAnotherUnchanged() {
        long[] alone = draw(Seeds.stream(7, "missions", "day_3"));
        Seeds.Rng other = Seeds.stream(7, "shops", "grocer");
        for (int i = 0; i < 100; i++) other.next();
        assertArrayEquals(alone, draw(Seeds.stream(7, "missions", "day_3")));
    }

    @Test void theSameNumbersAsTheEngineCopies() {
        for (long seed : new long[]{0, 1, 20261029L, -42}) {
            assertEquals(dev.shinobi.life.bond.Seeds.hash64(seed, "cast", "rival"), Seeds.hash64(seed, "cast", "rival"));
            assertEquals(dev.shinobi.life.bond.Seeds.roll(seed, "haggle", "pawn_shop", "12"), Seeds.roll(seed, "haggle", "pawn_shop", "12"));
            var a = dev.shinobi.life.bond.Seeds.stream(seed, "residents", "m1");
            var b = Seeds.stream(seed, "residents", "m1");
            for (int i = 0; i < 10; i++) assertEquals(a.next(), b.next());
        }
    }
}
