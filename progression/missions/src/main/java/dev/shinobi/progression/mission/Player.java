package dev.shinobi.progression.mission;

import java.util.HashSet;
import java.util.Set;

/**
 * What the desk reads about the player: rank, level, the quests and flags that gate missions, and the calendar.
 * In Phase 0 this is a view over Core's player record and flags; the simulation drives it directly.
 */
public final class Player {
    /** The ladder in order; ANBU is a branch from Jonin, so it ranks above Jonin for gates. */
    public static final java.util.List<String> LADDER = java.util.List.of("academy", "genin", "chunin", "jonin", "anbu", "hokage");

    public String rank = "genin";
    public int level = 5;
    public double xp;
    public double ryo;
    public final Set<String> done = new HashSet<>();
    public final Set<String> flags = new HashSet<>();
    public final Set<String> techniques = new HashSet<>();
    public final Set<String> events = new HashSet<>();
    /** Days until each upcoming event, for templates offered before one ({@code "event": {"before": id, "days": n}}). */
    public final java.util.Map<String, Integer> eventIn = new java.util.HashMap<>();
    public double cohesion = 50;

    public int rankIndex() { return LADDER.indexOf(rank); }
    public boolean atLeast(String r) { return rankIndex() >= LADDER.indexOf(r); }

    /** Adds XP and levels up; returns levels gained. */
    public int gainXp(double amount, Economy e) {
        xp += amount;
        int gained = 0;
        while (xp >= e.xpToNext(level)) { xp -= e.xpToNext(level); level++; gained++; }
        return gained;
    }
}
