package dev.shinobi.progression.mission;

import java.util.List;
import java.util.Map;

import static dev.shinobi.progression.mission.Json.*;

/**
 * The part of Core's condition language the desk evaluates when it builds a board (ROADMAP.md, "Conditions and
 * actions"): rank, level, quests, flags, techniques, events and the calendar. Time of day ({@code time_between}) gates
 * accepting and starting a mission, not the board, so it passes here. Anything else does not pass: the desk never
 * offers a mission it cannot reason about.
 */
public final class Unlocks {
    public static final String[] SEASONS = {"spring", "summer", "autumn", "winter"};
    public static final int SEASON_DAYS = 28, WEEK = 7;

    public static String season(int day) { return SEASONS[Math.floorMod(day / SEASON_DAYS, 4)]; }
    /** VF's calendar: a season starts on a Moonday and Market Day is the 7th, 14th, 21st and 28th. */
    public static boolean marketDay(int day) { return Math.floorMod(day, WEEK) == WEEK - 1; }
    public static int week(int day) { return Math.floorDiv(day, WEEK); }

    public static boolean test(Map<String, Object> c, Player p, int day) {
        if (c == null) return true;
        for (var e : c.entrySet()) {
            Object a = e.getValue();
            boolean ok = switch (e.getKey()) {
                case "all" -> list(a).stream().allMatch(x -> test(map(x), p, day));
                case "any" -> list(a).stream().anyMatch(x -> test(map(x), p, day));
                case "not" -> !test(map(a), p, day);
                case "rank_at_least" -> p.atLeast((String) a);
                case "rank_at_most" -> p.rankIndex() <= Player.LADDER.indexOf((String) a);
                case "level_at_least" -> p.level >= num(a, 0);
                case "quest_state" -> {
                    List<String> q = strings(a);
                    yield q.get(1).equals("done") == p.done.contains(q.get(0));
                }
                case "flag" -> p.flags.contains((String) a);
                case "knows_technique" -> p.techniques.contains((String) a);
                case "event_active" -> p.events.contains((String) a);
                case "time_between" -> true;
                case "calendar" -> calendar(map(a), day);
                default -> false;
            };
            if (!ok) return false;
        }
        return true;
    }

    static boolean calendar(Map<String, Object> c, int day) {
        if ("market_day".equals(c.get("weekday")) && !marketDay(day)) return false;
        if (c.get("season") != null && !strings(c.get("season")).contains(season(day))) return false;
        return true;
    }

    /** A template's own season and event windows. */
    public static boolean window(Template t, Player p, int day) {
        if (!t.seasons().isEmpty() && !t.seasons().contains(season(day))) return false;
        if (t.event() != null) {
            if (t.event().get("during") != null) return p.events.contains((String) t.event().get("during"));
            if (t.event().get("before") != null) {
                Integer in = p.eventIn.get((String) t.event().get("before"));
                return in != null && in > 0 && in <= num(t.event().get("days"), 3);
            }
        }
        return true;
    }

    private Unlocks() {}
}
