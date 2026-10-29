package dev.shinobi.life.bond;

/**
 * Something the bond engine noticed, for the glue to show (a level-up toast, a speech bubble, village news) and for
 * the play log. {@code kind}: level_up, level_down, gated, conflict, apology, reconciled, jealous, left_squad,
 * rejoined, romance, heard, birthday_missed, standing.
 */
public record BondEvent(long day, String who, String kind, String detail) {
    @Override public String toString() { return "day " + day + " " + who + " " + kind + (detail.isEmpty() ? "" : " " + detail); }
}
