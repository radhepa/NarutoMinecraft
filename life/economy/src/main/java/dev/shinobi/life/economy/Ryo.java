package dev.shinobi.life.economy;

import java.util.Arrays;

/**
 * Ryo as notes (ROADMAP §7 Ryo): 1, 10, 100 and 1,000 ryo notes are items, so money fits in chests and vanilla
 * trading; the HUD and the shop screen show the total. A {@link Wallet} is the notes a player carries: a purchase
 * takes notes and gives change in the fewest notes, so a stack of ones is never needed.
 */
public final class Ryo {
    public static final int[] NOTES = {1000, 100, 10, 1};

    /** The fewest notes that make {@code amount}, largest first: counts of 1000, 100, 10 and 1. */
    public static int[] notes(int amount) {
        if (amount < 0) throw new IllegalArgumentException("negative ryo");
        int[] out = new int[NOTES.length];
        for (int i = 0; i < NOTES.length; i++) { out[i] = amount / NOTES[i]; amount %= NOTES[i]; }
        return out;
    }

    /** Notes in a player's inventory (or a chest). */
    public static final class Wallet {
        private final int[] counts = new int[NOTES.length];

        public static Wallet of(int amount) {
            var w = new Wallet();
            w.add(amount);
            return w;
        }
        public int total() {
            int t = 0;
            for (int i = 0; i < NOTES.length; i++) t += counts[i] * NOTES[i];
            return t;
        }
        public int count(int note) { return counts[index(note)]; }
        public int[] counts() { return counts.clone(); }
        public void add(int amount) {
            int[] n = notes(amount);
            for (int i = 0; i < n.length; i++) counts[i] += n[i];
        }
        public void addNote(int note, int count) { counts[index(note)] += count; }

        /**
         * Pays {@code price}: takes notes largest first while they fit, then breaks the smallest note left for the
         * rest and gives the change in the fewest notes. False, and nothing taken, if the wallet holds too little.
         * (Every note greedy left unused is worth more than what is still owed, so one break always settles it.)
         */
        public boolean pay(int price) {
            if (price < 0) throw new IllegalArgumentException("negative price");
            if (total() < price) return false;
            int remaining = price;
            for (int i = 0; i < NOTES.length; i++) {
                int use = Math.min(counts[i], remaining / NOTES[i]);
                counts[i] -= use;
                remaining -= use * NOTES[i];
            }
            if (remaining > 0) {
                int i = NOTES.length - 1;
                while (counts[i] == 0) i--;
                counts[i]--;
                add(NOTES[i] - remaining);
            }
            return true;
        }
        private static int index(int note) {
            for (int i = 0; i < NOTES.length; i++) if (NOTES[i] == note) return i;
            throw new IllegalArgumentException("no " + note + "-ryo note");
        }
        @Override public String toString() { return total() + " ryo " + Arrays.toString(counts); }
    }

    private Ryo() {}
}
