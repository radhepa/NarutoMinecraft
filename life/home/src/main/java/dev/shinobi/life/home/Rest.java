package dev.shinobi.life.home;

/**
 * Sleep at home. Your own bed always clears fatigue (ROADMAP.md, "The daily cycle"); going to bed before midnight
 * gives Well Rested, and a comfier home makes it a little better and a little longer:
 *
 * <pre>
 * tier          chakra regen   until
 * Bare          +10%           12:00   (the roadmap's Well Rested)
 * Cosy          +10%           13:00
 * Comfortable   +12%           13:00
 * Homely        +15%           14:00
 * Beloved       +15%           15:00, and fatigue starts an hour later that night
 * </pre>
 *
 * The complete Leaf set adds an hour. A late night (to bed between midnight and 2:00) still gives a short, light Well
 * Rested in a Homely or Beloved home (+5% until 11:00). Nothing here is ever a penalty: a bare flat is the roadmap's
 * rule, unchanged.
 */
public final class Rest {
    /** What the night gave: chakra regen bonus (0.10 for +10%), the hour it lasts until, and hours of fatigue delay. */
    public record Rested(double regen, int until, int fatigueDelay, String tier) {
        public static final Rested NONE = new Rested(0, 0, 0, "");
        public boolean any() { return regen > 0; }
    }

    /** {@code bedHour} is the hour you lay down (18 to 23, or 0 to 5 after midnight). */
    public static Rested sleep(Comfort.Score score, int bedHour, boolean ownBed) {
        if (!ownBed) return Rested.NONE;
        var t = score.tier();
        int leaf = score.perk(FurnitureSet.HOME_SWEET_HOME) ? 1 : 0;
        boolean late = bedHour >= 0 && bedHour < 6;
        if (late) {
            if (bedHour >= 2 || t.compareTo(Comfort.Tier.HOMELY) < 0) return Rested.NONE;
            return new Rested(.05, 11, 0, "late." + t.id());
        }
        return switch (t) {
            case BARE -> new Rested(.10, 12 + leaf, 0, t.id());
            case COSY -> new Rested(.10, 13 + leaf, 0, t.id());
            case COMFORTABLE -> new Rested(.12, 13 + leaf, 0, t.id());
            case HOMELY -> new Rested(.15, 14 + leaf, 0, t.id());
            case BELOVED -> new Rested(.15, 15 + leaf, 1, t.id());
        };
    }

    private Rest() {}
}
