package dev.shinobi.combat;

import java.util.Map;

/**
 * Mastery of one technique (ROADMAP Hand signs; data/combat/core/signs.json): uses raise it from novice through
 * practiced and mastered to perfected. A use in a real fight counts twice. Mastered techniques bind to a quick
 * slot and cast with half their signs; perfected ones with one sign, or none for E to C rank.
 */
public final class Mastery {
    public enum Tier { NOVICE, PRACTICED, MASTERED, PERFECTED }

    public static final int COMBAT_USE = 2, TRAINING_USE = 1;

    /** Uses needed for practiced, mastered and perfected, by rank. */
    static final Map<String, int[]> USES = Map.of(
            "e", new int[]{10, 30, 80}, "d", new int[]{12, 40, 100}, "c", new int[]{15, 50, 130},
            "b", new int[]{20, 60, 160}, "a", new int[]{25, 75, 200}, "s", new int[]{30, 90, 240});

    public static Tier tier(String rank, int uses) {
        int[] t = USES.get(rank);
        if (uses >= t[2]) return Tier.PERFECTED;
        if (uses >= t[1]) return Tier.MASTERED;
        if (uses >= t[0]) return Tier.PRACTICED;
        return Tier.NOVICE;
    }
    public static double costMult(Tier t) {
        return switch (t) { case NOVICE -> 1; case PRACTICED -> 0.95; case MASTERED -> 0.9; case PERFECTED -> 0.8; };
    }
    public static double powerMult(Tier t) {
        return switch (t) { case NOVICE -> 1; case PRACTICED -> 1.03; case MASTERED -> 1.06; case PERFECTED -> 1.1; };
    }
    public static boolean quickSlot(Tier t) { return t.ordinal() >= Tier.MASTERED.ordinal(); }

    /** How many of a technique's signs a caster at this tier must weave (before the sign book makes it unique). */
    public static int signsNeeded(Tier t, String rank, int fullLength) {
        if (fullLength == 0) return 0;
        return switch (t) {
            case NOVICE, PRACTICED -> fullLength;
            case MASTERED -> (fullLength + 1) / 2;
            case PERFECTED -> "edc".contains(rank) ? 0 : 1;
        };
    }

    private Mastery() {}
}
