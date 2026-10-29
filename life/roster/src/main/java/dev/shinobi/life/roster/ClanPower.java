package dev.shinobi.life.roster;

import java.util.Set;

/**
 * Clan power, for NPCs (docs/RANKS.md, "Clan power"): people of powerful clans are stronger on average, never by rule.
 * Each tier shifts where its members' levels fall within their rank ({@code shift}, in standard deviations of that
 * rank's spread), where a rolled classmate belongs against the player ({@code classShift}, in levels) and how hard
 * they train ({@code drive}). The spreads overlap: a clanless prodigy can beat a great-clan heir. The player starts
 * clanless and is outside this table; their balance is character creation's.
 */
public enum ClanPower {
    GREAT(.6, .8, 1.06), STRONG(.3, .3, 1.03), MINOR(0, -.1, 1), CLANLESS(-.2, -.3, 1);

    public final double shift, classShift, drive;
    ClanPower(double shift, double classShift, double drive) { this.shift = shift; this.classShift = classShift; this.drive = drive; }

    /** The four great clans; the other eleven noble clans are strong; the ten minor clans are minor (CLANS.md). */
    public static final Set<String> GREAT_CLANS = Set.of("uchiha", "hyuga", "senju", "uzumaki");
    public static final Set<String> MINOR_CLANS = Set.of("shiranui", "morino", "umino", "haruno", "namiashi", "hagane", "kinoshita",
            "tsuchigumo", "suzuran", "tobari");

    public static ClanPower of(String clan) {
        if (clan == null || clan.isEmpty() || clan.equals("none")) return CLANLESS;
        if (GREAT_CLANS.contains(clan)) return GREAT;
        return MINOR_CLANS.contains(clan) ? MINOR : STRONG;
    }

    /** A resident's level within a rank's spread ({@code mean}, {@code sd}, clamped to {@code min..max}), shifted by clan power. */
    public double roll(double mean, double sd, double min, double max, Seeds.Rng rng) {
        double u = Math.max(1e-12, rng.unit()), v = rng.unit();
        double normal = Math.sqrt(-2 * Math.log(u)) * Math.cos(2 * Math.PI * v);
        return Math.clamp(mean + (shift + normal) * sd, min, max);
    }
    public String id() { return name().toLowerCase(java.util.Locale.ROOT); }
}
