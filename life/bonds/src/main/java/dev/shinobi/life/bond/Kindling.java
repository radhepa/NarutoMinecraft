package dev.shinobi.life.bond;

import java.util.Locale;

/**
 * Kindling Bond, by the roadmap's thresholds: once the story unlocks it ({@link #UNLOCK_FLAG}), bond level 6 lets
 * you borrow an ally's nature, level 8 one of their techniques, level 10 both and for longer. A teammate, your
 * sensei and your spouse are the deepest bonds: for them the full tier opens at level 8. It reads the level they
 * act on, so a quarrel dims the flame and a falling-out puts it out. Shinobi Combat's {@code kindle} effect spends
 * the {@link Grant}.
 */
public final class Kindling {
    public static final String UNLOCK_FLAG = "story.kindling.awakened";

    public enum Tier {
        NONE, NATURE, TECHNIQUE, FULL;
        public String id() { return name().toLowerCase(Locale.ROOT); }
        public static Tier of(String id) { return valueOf(id.toUpperCase(Locale.ROOT)); }
    }
    /** What one kindling lends: casts of their nature's jutsu, uses of their technique, how long it burns, and the rest after. */
    public record Grant(int natureCasts, int techniqueUses, double duration, int rekindleMinutes) {}

    public static Tier tier(boolean unlocked, int effectiveLevel, boolean deepest, Conflict conflict) {
        if (!unlocked || conflict.active() || conflict.broken()) return Tier.NONE;
        if (effectiveLevel >= Levels.KINDLE_FULL || deepest && effectiveLevel >= Levels.KINDLE_TECHNIQUE) return Tier.FULL;
        if (effectiveLevel >= Levels.KINDLE_TECHNIQUE) return Tier.TECHNIQUE;
        if (effectiveLevel >= Levels.KINDLE_NATURE) return Tier.NATURE;
        return Tier.NONE;
    }
    /** The tier with one person in this world: teammates and the sensei (while in the squad) and a spouse are the deepest bonds. */
    public static Tier tier(BondWorld w, String who) {
        var squad = w.squad();
        boolean deepest = squad != null && squad.has(who) || who.equals(w.spouse());
        return tier(w.flag(UNLOCK_FLAG), w.effectiveLevel(who), deepest, w.bond(who).conflict());
    }
    /** In-game minutes; 60 is one in-game hour (50 real seconds). */
    public static Grant grant(Tier tier) {
        return switch (tier) {
            case NONE -> new Grant(0, 0, 0, 0);
            case NATURE -> new Grant(3, 0, 1, 180);
            case TECHNIQUE -> new Grant(3, 1, 1, 180);
            case FULL -> new Grant(5, 1, 1.5, 120);
        };
    }

    private Kindling() {}
}
