package dev.shinobi.village.dialogue;

import java.util.ArrayList;
import java.util.List;

/**
 * One compiled line (or one overheard exchange, which has {@code turns} instead of {@code text}). {@code id} is
 * stable and dense, kept by {@code tools/dialogue/ids.lock}: the heard ledger is a bit per id. {@code spec} is how
 * specific its tags are (DIALOGUE.md, "Selection"); {@code group} joins the voices of one piece of content.
 */
public record Line(int id, String pool, Tags tags, Object when, List<String> functions, Kind kind, int spec, int group,
                   String mood, String text, List<Turn> turns, String lead) {

    /** How a line may come back: never ({@code LINE}), freely ({@code REPEAT}), or after the whole pool ({@code CYCLE}). */
    public enum Kind { LINE, REPEAT, CYCLE }

    /** One turn of an overheard exchange: speaker {@code a} or {@code b}. */
    public record Turn(String who, String text, String mood) {}

    public boolean filler() { return !functions.isEmpty() && functions.getFirst().equals("filler"); }
    public boolean exchange() { return turns != null; }

    static Line read(Object compiled) {
        var m = Json.map(compiled);
        var fn = new ArrayList<String>();
        for (var f : Json.list(m.get("fn"))) fn.add(f.toString());
        List<Turn> turns = null;
        if (m.containsKey("turns")) {
            turns = new ArrayList<>();
            for (var t : Json.list(m.get("turns"))) {
                var tm = Json.map(t);
                turns.add(new Turn(Json.str(tm.get("who")), Json.str(tm.get("text")), Json.str(tm.get("mood"))));
            }
            turns = List.copyOf(turns);
        }
        Kind kind = switch (String.valueOf(m.getOrDefault("kind", "line"))) {
            case "repeat" -> Kind.REPEAT;
            case "cycle" -> Kind.CYCLE;
            default -> Kind.LINE;
        };
        return new Line(Json.integer(m.get("id"), 0), Json.str(m.get("pool")), Tags.read(m.get("tags")), m.get("when"),
                List.copyOf(fn), kind, Json.integer(m.get("spec"), 0), Json.integer(m.get("group"), 0), Json.str(m.get("mood")),
                Json.str(m.get("text")), turns, Json.str(m.get("lead")));
    }
}
