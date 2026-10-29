package dev.shinobi.life.roster;

/**
 * Power tiers, apart from rank (docs/RANKS.md, "Rank and power"). Rank is the village's word for what you are
 * trusted with; the tier is how strong you are, read from your level on the player's own curve. A genin prodigy can
 * fight at C, a special jonin at B in one field and C in the rest, a retired jonin at B for years.
 *
 * <pre>E Academy 1-4 | D genin 5-14 | C chunin 15-29 | B jonin 30-41 | A elite 42-49 | S kage-level 50+</pre>
 */
public enum Tier {
    E("academy", 1), D("genin", 5), C("chunin", 15), B("jonin", 30), A("elite", 42), S("kage", 50);

    public final String word; public final int floor;
    Tier(String word, int floor) { this.word = word; this.floor = floor; }

    public static Tier of(double level) {
        Tier t = E;
        for (Tier x : values()) if (level >= x.floor) t = x;
        return t;
    }
    public String id() { return name(); }
}
