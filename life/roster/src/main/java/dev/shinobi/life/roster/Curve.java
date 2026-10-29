package dev.shinobi.life.roster;

/**
 * The player's level curve (ROADMAP.md §7, "Levels"), shared by everyone who grows beside them. XP is counted in
 * main-path minutes, so a level costs what the roadmap budgets for it: about 48 to 60 minutes in the beta, 65 to 112
 * later. Levels are fractional here ({@code 12.5} is halfway through level 12); the game shows the whole part.
 */
public final class Curve {
    /** The stretches of the main path: levels from and to, and their hours. */
    public enum Stretch {
        ACADEMY(1, 5, 4), GENIN(5, 15, 8), EXAMS(15, 18, 3), CHUNIN(18, 30, 13), JONIN(30, 42, 17), ROAD(42, 50, 15), POST(50, 60, 20);

        public final int from, to; public final double hours;
        Stretch(int from, int to, double hours) { this.from = from; this.to = to; this.hours = hours; }
        /** XP for one level of this stretch. */
        public double cost() { return hours * 60 / (to - from); }
        public String id() { return name().toLowerCase(java.util.Locale.ROOT); }
        public static Stretch of(double level) {
            for (Stretch s : values()) if (level < s.to) return s;
            return POST;
        }
    }

    public static final int MAX = 60;
    private static final double[] AT = new double[MAX + 1];
    static {
        for (int l = 2; l <= MAX; l++) AT[l] = AT[l - 1] + Stretch.of(l - 1).cost();
    }

    /** XP at which a whole level starts. */
    public static double xpAt(int level) { return AT[Math.clamp(level, 1, MAX)]; }
    /** XP at a fractional level. */
    public static double xpAt(double level) {
        if (level >= MAX) return AT[MAX];
        int l = (int) Math.max(1, Math.floor(level));
        return AT[l] + (level - l) * Stretch.of(l).cost();
    }
    /** The fractional level an amount of XP reaches. */
    public static double level(double xp) {
        if (xp <= 0) return 1;
        for (int l = 1; l < MAX; l++) if (xp < AT[l + 1]) return l + (xp - AT[l]) / (AT[l + 1] - AT[l]);
        return MAX;
    }

    private Curve() {}
}
