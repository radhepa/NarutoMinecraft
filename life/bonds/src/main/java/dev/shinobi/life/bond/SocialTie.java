package dev.shinobi.life.bond;

import java.util.Map;
import java.util.Set;

/**
 * A real tie between two residents in the village's sparse social graph, after VF's {@code Tie}: what kind it is,
 * since when they have known each other, the days spent side by side, their last quarrel and whether one of them
 * is quietly smitten. Everyone without a tie gets a feeling derived on demand from their clans, district and
 * chemistry ({@link Village#affinity}).
 */
public record SocialTie(String kind, long since, int together, long lastTogether, long quarrel, boolean crush) {
    public static final int MAX_TOGETHER = 40;
    /** Ties made by where people live and work; the rest (friend, neighbor, rival) are chosen and capped. */
    public static final Set<String> STRUCTURAL = Set.of("family", "household", "spouse", "sweetheart", "squad", "class", "work", "clan");
    /** Ties whose people see each other every day. */
    public static final Set<String> DAILY = Set.of("family", "household", "spouse", "sweetheart", "squad", "class", "work");
    private static final Map<String, Double> CLOSENESS = Map.ofEntries(Map.entry("family", 4.0), Map.entry("household", 4.0),
            Map.entry("spouse", 4.0), Map.entry("sweetheart", 4.0), Map.entry("squad", 3.0), Map.entry("class", 3.0), Map.entry("work", 2.5),
            Map.entry("friend", 2.5), Map.entry("clan", 2.0), Map.entry("neighbor", 1.5), Map.entry("rival", .5));

    /** Closest first: when two people are tied twice over (spouses who also share a household), the closer kind wins. */
    private static final java.util.List<String> ORDER = java.util.List.of("spouse", "sweetheart", "family", "household", "squad", "class", "work",
            "clan", "friend", "neighbor", "rival");
    public static int rank(String kind) { int i = ORDER.indexOf(kind); return i < 0 ? ORDER.size() : i; }

    public SocialTie { together = Math.clamp(together, 0, MAX_TOGETHER); }
    public static SocialTie of(String kind, long since) { return new SocialTie(kind, since, 0, -1, -1, false); }
    /** How readily news passes along this tie, as a gossip circle closeness. */
    public double closeness() { return CLOSENESS.getOrDefault(kind, 1.0); }
    public boolean chosen() { return !STRUCTURAL.contains(kind); }
    public SocialTie together(long day) { return lastTogether == day ? this : new SocialTie(kind, since, together + 1, day, quarrel, crush); }
    public SocialTie together(long day, int days) { return new SocialTie(kind, since, together + days, day, quarrel, crush); }
    public SocialTie quarrel(long day) { return new SocialTie(kind, since, together, lastTogether, day, crush); }
    public SocialTie reconciled() { return new SocialTie(kind, since, together, lastTogether, -1, crush); }
    public SocialTie kind(String next, long day) { return new SocialTie(next, next.equals(kind) ? since : Math.min(since, day), together, lastTogether, quarrel, crush && !next.equals("spouse")); }
    public SocialTie crush(boolean on) { return new SocialTie(kind, since, together, lastTogether, quarrel, on); }
}
