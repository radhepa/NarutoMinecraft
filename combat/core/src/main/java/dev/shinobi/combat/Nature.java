package dev.shinobi.combat;

import java.util.Locale;

/**
 * The five natures and the triangle: fire beats wind, wind beats lightning, lightning beats earth, earth beats
 * water, water beats fire (it is a cycle of five). {@link #NONE} is pure chakra and beats nothing.
 */
public enum Nature {
    FIRE, WIND, LIGHTNING, EARTH, WATER, NONE;

    /** A defender with an affinity takes this much more from the nature that beats theirs. */
    public static final double VS_WEAK = 1.25;
    /** ...and this much from the nature theirs beats. */
    public static final double VS_STRONG = 0.8;
    /** When jutsu collide, the stronger nature passes through at this share of its power. */
    public static final double CLASH_PASS = 0.5;
    /** Your own natures' jutsu cost a quarter less. */
    public static final double OWN_COST = 0.75;

    public String id() { return name().toLowerCase(Locale.ROOT); }
    public static Nature of(String id) { return id == null || id.isEmpty() ? NONE : valueOf(id.toUpperCase(Locale.ROOT)); }

    /** The nature this one beats. */
    public Nature beats() {
        return switch (this) {
            case FIRE -> WIND;
            case WIND -> LIGHTNING;
            case LIGHTNING -> EARTH;
            case EARTH -> WATER;
            case WATER -> FIRE;
            case NONE -> NONE;
        };
    }
    public boolean beats(Nature other) { return this != NONE && beats() == other; }

    /** Damage multiplier when a jutsu of this nature hits a defender whose affinity is {@code defender}. */
    public double against(Nature defender) {
        if (this == NONE || defender == NONE) return 1;
        if (beats(defender)) return VS_WEAK;
        if (defender.beats(this)) return VS_STRONG;
        return 1;
    }

    /** What is left of two colliding jutsu: the winner's nature and remaining power (0 when both dissipate). */
    public record Clash(Nature winner, double power) {
        public boolean bothGone() { return power <= 0; }
    }
    public static Clash clash(Nature a, double powerA, Nature b, double powerB) {
        if (a.beats(b)) return new Clash(a, powerA * CLASH_PASS);
        if (b.beats(a)) return new Clash(b, powerB * CLASH_PASS);
        if (powerA == powerB) return new Clash(NONE, 0);
        return powerA > powerB ? new Clash(a, powerA - powerB) : new Clash(b, powerB - powerA);
    }
}
