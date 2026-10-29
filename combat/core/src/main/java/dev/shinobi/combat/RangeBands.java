package dev.shinobi.combat;

import java.util.Locale;

/**
 * The enemy brain's range bands (ROADMAP Enemies and sparring): close for taijutsu, mid for throws and quick
 * jutsu, far for big jutsu, bows, traps and sensing.
 */
public final class RangeBands {
    public enum Band {
        CLOSE(0, 3), MID(3, 10), FAR(10, 24);

        public final double min, max;
        Band(double min, double max) { this.min = min; this.max = max; }
        public String id() { return name().toLowerCase(Locale.ROOT); }
        public static Band of(String id) { return valueOf(id.toUpperCase(Locale.ROOT)); }
        public double middle() { return this == CLOSE ? 1.8 : (min + max) / 2; }
        public boolean contains(double d) { return d >= min && d < max || this == FAR && d >= max; }
    }

    public static Band of(double distance) {
        if (distance < Band.CLOSE.max) return Band.CLOSE;
        if (distance < Band.MID.max) return Band.MID;
        return Band.FAR;
    }
    /** Which way a fighter that prefers {@code want} steps at this distance: -1 in, +1 out, 0 hold. */
    public static int step(Band want, double distance) {
        if (distance > want.max) return -1;
        if (distance < want.min) return 1;
        return 0;
    }

    private RangeBands() {}
}
