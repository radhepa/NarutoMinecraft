package dev.shinobi.village.dialogue;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.LinkedHashMap;
import java.util.List;
import java.util.Map;
import java.util.Random;
import java.util.Set;

/** A small bank built in code, with known rules, for the engine's tests. */
final class Fixture {
    static final String RULES = """
            {"budget": {"tiers": {"cast": {"daily": 6, "base": null},
                                  "resident": {"daily": 3, "base": 6, "per_level": 2, "per_slice": 0},
                                  "passerby": {"daily": 1, "base": 2, "per_level": 0}},
                        "exempt": ["bond.heard", "combat"]},
             "filler_cap": 0.2, "recall": 4,
             "questions": {"min_level": 0, "per_day": 99, "gap_days": []},
             "facets": {"greet": [{"pool": "greet.time", "weight": 1, "needs": "!"}],
                        "chat": [{"pool": "chat.personal", "weight": 1, "needs": "!"}]},
             "topic_alias": {"talk.small_talk": "chat"}}""";

    private final Map<String, List<Line>> pools = new LinkedHashMap<>();
    private final Map<String, Question> questions = new LinkedHashMap<>();
    private int next = 1;
    private int group = 1;

    /** Adds a line: {@code tags} as compact pairs ("personality=fiery", "level=3..10", "weather=!clear"). */
    Fixture line(String pool, String text, String... tags) { return add(pool, text, Line.Kind.LINE, "react", 0, tags); }
    Fixture filler(String pool, String text, String... tags) { return add(pool, text, Line.Kind.LINE, "filler", 0, tags); }
    Fixture repeat(String pool, String text, String... tags) { return add(pool, text, Line.Kind.REPEAT, "react", 0, tags); }
    Fixture cycle(String pool, String text, String... tags) { return add(pool, text, Line.Kind.CYCLE, "react", 0, tags); }
    /** Lines that are one piece of content in several voices. */
    Fixture grouped(String pool, String text, String... tags) { return add(pool, text, Line.Kind.LINE, "react", group, tags); }
    Fixture nextGroup() { group++; return this; }

    private Fixture add(String pool, String text, Line.Kind kind, String fn, int g, String... tags) {
        var json = new StringBuilder("{");
        int spec = 0;
        for (String t : tags) {
            String[] kv = t.split("=", 2);
            if (json.length() > 1) json.append(',');
            json.append('"').append(kv[0]).append("\":");
            String v = kv[1];
            if (v.contains("..")) {
                String[] r = v.split("\\.\\.");
                json.append("{\"range\":[").append(r[0]).append(',').append(r[1]).append("]}");
            } else if (v.startsWith("!")) json.append("{\"not\":[").append(quoted(v.substring(1))).append("]}");
            else json.append("{\"any\":[").append(quoted(v)).append("]}");
            spec += 3;
        }
        json.append('}');
        var line = new Line(next++, pool, Tags.read(Json.parse(json.toString())), null, List.of(fn), kind, spec, g, null, text, null, null);
        pools.computeIfAbsent(pool, k -> new ArrayList<>()).add(line);
        return this;
    }
    private static String quoted(String alternatives) {
        var out = new StringBuilder();
        for (String a : alternatives.split("\\|")) { if (out.length() > 0) out.append(','); out.append('"').append(a).append('"'); }
        return out.toString();
    }

    Fixture question(String id, int level, String axis, String follows, int depth, String... answersWithPoles) {
        var answers = new ArrayList<Question.Answer>();
        for (int k = 0; k < answersWithPoles.length; k++) {
            int pole = Integer.parseInt(answersWithPoles[k]);
            answers.add(new Question.Answer("a" + (k + 1), "Answer " + (k + 1), "Reply " + (k + 1), null, Map.of(), "warm", pole, List.of()));
        }
        questions.put(id, new Question(id, next++, List.of("deepen_bond"), level, Tags.NONE, null, axis, follows, depth,
                List.of("Ask " + id + "?"), List.copyOf(answers)));
        return this;
    }

    Bank bank() { return Bank.of(pools, questions, Rules.read(Json.parse(RULES)), next); }

    Talk talk() { return talk(new Heard()); }
    Talk talk(Heard heard) {
        var names = new HashMap<String, String>();
        names.put("player.given", "Player");
        names.put("role:sensei.given", "Sensei");
        return new Talk(bank(), heard, Conditions.basic(heard, Set.of()), Names.of(names));
    }
    static Random random() { return new Random(7); }
}
