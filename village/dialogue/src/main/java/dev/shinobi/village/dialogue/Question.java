package dev.shinobi.village.dialogue;

import java.util.ArrayList;
import java.util.LinkedHashMap;
import java.util.List;
import java.util.Map;

/**
 * A question a resident asks the player, with 2 to 4 answers (DIALOGUE.md, "Questions and choices"). Answers carry
 * stances, not numbers: the values they honour (+1) or violate (-1), a tone, and a pole on the question's
 * {@code axis} so a later answer can contradict an earlier one. The bond engine turns stances into meter changes
 * through the asker's personality; this engine keeps which questions were answered and how. A {@code perFriend} opinion
 * question ("What do you make of the rain?") is spent per asker rather than for everyone: each close friend may ask it
 * once.
 */
public record Question(String id, int num, List<String> functions, int level, Tags tags, Object when, String axis,
                       String follows, int depth, List<String> asks, List<Answer> answers, boolean perFriend) {

    /** The bond level a per-friend question needs: a close friend's. */
    public static final int CLOSE_FRIEND = 5;

    public record Answer(String id, String label, String reply, String mood, Map<String, Integer> values, String tone,
                         int pole, List<Object> actions) {}

    public Answer answer(String answerId) {
        for (var a : answers) if (a.id().equals(answerId)) return a;
        throw new IllegalArgumentException(id + " has no answer " + answerId);
    }
    /** Where the callbacks for an answer live: {@code callback.answer.<question>.<answer>}. */
    public String callbackPool(String answerId) { return "callback.answer." + id + "." + answerId; }

    static Question read(Object compiled) {
        var m = Json.map(compiled);
        var fn = new ArrayList<String>();
        for (var f : Json.list(m.get("fn"))) fn.add(f.toString());
        var asks = new ArrayList<String>();
        for (var a : Json.list(m.get("asks"))) asks.add(a.toString());
        var answers = new ArrayList<Answer>();
        for (var o : Json.list(m.get("answers"))) {
            var a = Json.map(o);
            var values = new LinkedHashMap<String, Integer>();
            for (var e : Json.map(a.get("values")).entrySet()) values.put(e.getKey(), Json.integer(e.getValue(), 0));
            answers.add(new Answer(Json.str(a.get("id")), Json.str(a.get("label")), Json.str(a.get("reply")), Json.str(a.get("mood")),
                    Map.copyOf(values), Json.str(a.get("tone")), Json.integer(a.get("pole"), 0), List.copyOf(Json.list(a.get("actions")))));
        }
        return new Question(Json.str(m.get("id")), Json.integer(m.get("num"), 0), List.copyOf(fn), Json.integer(m.get("level"), 0),
                Tags.read(m.get("tags")), m.get("when"), Json.str(m.get("axis")), Json.str(m.get("follows")),
                Json.integer(m.get("depth"), 1), List.copyOf(asks), List.copyOf(answers), Boolean.TRUE.equals(m.get("per_friend")));
    }
}
