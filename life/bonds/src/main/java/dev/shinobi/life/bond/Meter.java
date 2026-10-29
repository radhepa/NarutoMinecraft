package dev.shinobi.life.bond;

/**
 * The five things a person feels about you. Affection runs from -100 (loathing) to 100; the others from 0 to 100.
 * Rivalry is not dislike: a rival can respect you, and even like you. Romance stays at 0 until the teen stage.
 */
public enum Meter {
    AFFECTION(-100), TRUST(0), RESPECT(0), RIVALRY(0), ROMANCE(0);

    public final int min;
    Meter(int min) { this.min = min; }
    public static final int MAX = 100;
    public String id() { return name().toLowerCase(java.util.Locale.ROOT); }
    public static Meter of(String id) { return valueOf(id.toUpperCase(java.util.Locale.ROOT)); }
}
