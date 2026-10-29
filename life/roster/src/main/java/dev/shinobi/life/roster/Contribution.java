package dev.shinobi.life.roster;

/**
 * A first estimate of how much a teammate does in a fight, against the player (docs/RANKS.md, "Pulling their
 * weight"): {@code power = level x (1 + 0.04 techniques)}, and in {@link #NICHE_SHARE} of fights the fight plays to
 * their niche and they act at their niche level. The target is 0.7 to 1.1 of the player's share. Shinobi Combat's
 * duel simulator gives the real numbers (damage and utility); this is the roster's own check that growth keeps them
 * in range.
 */
public final class Contribution {
    public static final double NICHE_SHARE = .35, PER_TECHNIQUE = .04, LOW = .7, HIGH = 1.1;

    public static double power(double level, int techniques) { return level * (1 + PER_TECHNIQUE * techniques); }

    /** A teammate's expected contribution over the player's. */
    public static double share(double level, double nicheLevel, int techniques, double playerLevel, int playerTechniques) {
        double them = NICHE_SHARE * power(nicheLevel, techniques) + (1 - NICHE_SHARE) * power(level, techniques);
        return them / power(playerLevel, playerTechniques);
    }
    public static double share(Roster r, String who, int playerTechniques) {
        return share(r.level(who), r.nicheLevel(who), r.techniques(who).size(), r.playerLevel(), playerTechniques);
    }

    private Contribution() {}
}
