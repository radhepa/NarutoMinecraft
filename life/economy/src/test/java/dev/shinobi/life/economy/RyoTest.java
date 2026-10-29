package dev.shinobi.life.economy;

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

class RyoTest {
    @Test void notesAreTheFewest() {
        assertArrayEquals(new int[]{1, 2, 3, 4}, Ryo.notes(1234));
        assertArrayEquals(new int[]{0, 0, 0, 0}, Ryo.notes(0));
        assertArrayEquals(new int[]{12, 0, 0, 9}, Ryo.notes(12009));
    }

    @Test void payingGivesChangeAndKeepsTheTotal() {
        var w = Ryo.Wallet.of(105);                 // a hundred and five ones
        assertTrue(w.pay(12));
        assertEquals(93, w.total());
        assertEquals(0, w.count(100));              // the hundred was broken for the change
        var exact = Ryo.Wallet.of(0);
        exact.addNote(10, 3);
        assertTrue(exact.pay(25));                  // two tens, then a ten broken for five back
        assertEquals(5, exact.total());
    }

    @Test void payingTooMuchTakesNothing() {
        var w = Ryo.Wallet.of(50);
        assertFalse(w.pay(51));
        assertEquals(50, w.total());
        assertThrows(IllegalArgumentException.class, () -> w.pay(-1));
    }

    @Test void everyPriceCanBePaidFromAnyWalletThatHoldsEnough() {
        var rng = Streams.stream(7, "test", "wallets");
        for (int i = 0; i < 2000; i++) {
            var w = new Ryo.Wallet();
            for (int note : Ryo.NOTES) w.addNote(note, rng.below(4));
            int total = w.total(), price = total == 0 ? 0 : rng.below(total + 1);
            assertTrue(w.pay(price), w + " paying " + price);
            assertEquals(total - price, w.total());
            for (int note : Ryo.NOTES) assertTrue(w.count(note) >= 0);
        }
    }
}
