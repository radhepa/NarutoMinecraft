package dev.shinobi.life.roster;

import java.util.Map;

/**
 * One in-game day as the roster sees it: the player's total XP at the end of it, the XP the player earned on
 * shared work with their group (lessons with the class, missions and training with the squad), whether the group
 * was together at all, and each person's bond input.
 */
public record Day(double playerXp, double sharedXp, boolean together, Map<String, BondInput> bonds) {
    public Day { bonds = bonds == null ? Map.of() : Map.copyOf(bonds); }
    public BondInput bond(String who) { return bonds.getOrDefault(who, BondInput.NONE); }
    /** A day apart: the player did their own things, the group trained and took missions on its own. */
    public static Day apart(double playerXp) { return new Day(playerXp, 0, false, Map.of()); }
}
