package dev.shinobi.combat;

/**
 * Levels and pillars (data/combat/core/scaling.json and resources.json). Levels are power, ranks are story
 * (ROADMAP Levels): every level adds 3% to everything you deal and 1% more to taijutsu; each pillar rank adds 7%
 * to its pillar. Hearts grow slowly (one every 6 levels), so the player's body also hardens with level
 * (toughness) while enemies' health grows with theirs.
 */
public final class Scaling {
    public enum Pillar { TAIJUTSU, WEAPONS, NINJUTSU }

    public static final double POWER_PER_LEVEL = 0.03;
    public static final double TAIJUTSU_EXTRA_PER_LEVEL = 0.01;
    public static final double PILLAR_PER_RANK = 0.07;
    public static final double TOUGHNESS_PER_LEVEL = 0.025;
    public static final double ENEMY_HP_PER_LEVEL = 0.055;
    public static final double ENEMY_DAMAGE_PER_LEVEL = 0.03;
    public static final int BASE_HP = 20, HEARTS_EVERY = 6;
    public static final int CHAKRA_BASE = 50, CHAKRA_PER_LEVEL = 3;
    public static final int MAX_LEVEL = 60, MAX_PILLAR_RANK = 10;

    public static double power(int level, Pillar pillar) {
        double p = 1 + POWER_PER_LEVEL * (level - 1);
        if (pillar == Pillar.TAIJUTSU) p += TAIJUTSU_EXTRA_PER_LEVEL * (level - 1);
        return p;
    }
    public static double pillar(int rank) { return 1 + PILLAR_PER_RANK * (Math.clamp(rank, 1, MAX_PILLAR_RANK) - 1); }

    /** The player's maximum health: 10 hearts at level 1 and one more every 6 levels, plus clan and gear hearts. */
    public static int playerHp(int level, int extraHearts) { return BASE_HP + 2 * ((level - 1) / HEARTS_EVERY) + 2 * extraHearts; }
    /** Incoming damage to the player is divided by this. */
    public static double toughness(int level) { return 1 + TOUGHNESS_PER_LEVEL * (level - 1); }
    public static double enemyHp(int level, double tierMult) { return BASE_HP * tierMult * (1 + ENEMY_HP_PER_LEVEL * (level - 1)); }
    public static double enemyDamage(int level) { return 1 + ENEMY_DAMAGE_PER_LEVEL * (level - 1); }

    public static int maxChakra(int level, double clanMult) { return (int) Math.round((CHAKRA_BASE + CHAKRA_PER_LEVEL * level) * clanMult); }

    /** The three pillar ranks together cannot pass this: specialise mid-game, round out late. */
    public static int pillarCap(int level) { return Math.min(3 * MAX_PILLAR_RANK, 3 + level / 2); }
    /** A style's tier from its pillar's rank: tiers open at ranks 1, 3, 5, 7 and 9. */
    public static int styleTier(int pillarRank) { return Math.min(5, 1 + (pillarRank - 1) / 2); }
    public static double styleMult(int tier) { return 1 + 0.1 * (Math.clamp(tier, 1, 5) - 1); }

    private Scaling() {}
}
