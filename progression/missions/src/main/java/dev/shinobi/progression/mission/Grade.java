package dev.shinobi.progression.mission;

/**
 * How well a mission went, S (best) to C (done, but barely); a failed mission has no grade. Grades scale pay, XP and
 * client rapport ({@link Economy#grade(double)}); they are not mission ranks.
 */
public enum Grade {
    S, A, B, C;

    public static Grade of(String id) { return valueOf(id); }
    public boolean atLeast(Grade other) { return ordinal() <= other.ordinal(); }
}
