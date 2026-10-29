package dev.shinobi.village.dialogue;

import java.util.List;
import java.util.Set;

/**
 * Answers a line's {@code when}: a condition in Core's condition and action language (ROADMAP.md, "Conditions and
 * actions"). In the game the glue hands it to Core's registry, where every mod registers what it can answer (bond
 * conditions from Shinobi Life, flags and ranks from Core). {@link #basic} answers the common ones from the context
 * and a set of flags, for tests and the simulation. Unknown conditions are false: a line that cannot be checked is
 * not said.
 */
@FunctionalInterface
public interface Conditions {
    boolean test(Object condition, Context c);

    /** Only lines with no condition pass. */
    Conditions NONE = (cond, c) -> cond == null;

    List<String> LADDER = List.of("academy", "genin", "chunin", "jonin", "anbu", "hokage");

    /**
     * all, any, not; flag (in {@code flags}); rank_at_least / rank_at_most (the context's {@code player_rank});
     * friendship [who, n] (the speaker's {@code level}); event_active, village_mood, age_stage, clan, clanless,
     * calendar {season}; answered [who, question, answer?] (the ledger).
     */
    static Conditions basic(Heard heard, Set<String> flags) {
        return new Conditions() {
            @Override public boolean test(Object cond, Context c) {
                if (cond == null) return true;
                if (cond instanceof List<?> all) {
                    for (var x : all) if (!test(x, c)) return false;
                    return true;
                }
                var m = Json.map(cond);
                if (m.size() != 1) return false;
                var e = m.entrySet().iterator().next();
                Object v = e.getValue();
                return switch (e.getKey()) {
                    case "all" -> { for (var x : Json.list(v)) if (!test(x, c)) yield false; yield true; }
                    case "any" -> { for (var x : Json.list(v)) if (test(x, c)) yield true; yield false; }
                    case "not" -> !test(v, c);
                    case "flag" -> flags.contains(v instanceof List<?> l ? l.getFirst().toString() : v.toString());
                    case "rank_at_least" -> LADDER.indexOf(c.get("player_rank")) >= LADDER.indexOf(v.toString());
                    case "rank_at_most" -> LADDER.indexOf(c.get("player_rank")) <= LADDER.indexOf(v.toString());
                    case "friendship" -> c.level() >= Json.integer(Json.list(v).get(1), 0);
                    case "event_active" -> v.toString().equals(c.get("event"));
                    case "village_mood" -> Json.list(v).size() > 1 && Json.list(v).get(1).toString().equals(c.get("mood"));
                    case "age_stage" -> v.toString().equals(c.get("player_stage"));
                    case "clan" -> v.toString().equals(c.get("player_clan"));
                    case "clanless" -> "clanless".equals(c.get("clan_status"));
                    case "calendar" -> {
                        Object season = Json.map(v).get("season");
                        yield season == null || Json.list(season instanceof List<?> ? season : List.of(season)).contains(c.get("season"));
                    }
                    case "answered" -> {
                        var a = Json.list(v);
                        String given = heard.answer(a.get(1).toString());
                        yield given != null && (a.size() < 3 || a.get(2).toString().equals(given));
                    }
                    default -> false;
                };
            }
        };
    }
}
