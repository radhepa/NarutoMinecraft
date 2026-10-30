package dev.shinobi.progression;

import dev.shinobi.progression.mission.Json;
import dev.shinobi.progression.mission.Template;

import java.util.Map;

/** Checking a quest file, apart from the mod's entrypoint so it runs without a game. */
final class Quests {
    private Quests() {}

    /**
     * The quest in {@code raw}, or why it is broken: a string id, a start step, each step's {@code next} null or a step,
     * and a place for every {@code go}. Template reads a wrong-typed field as its default, so the raw fields are checked.
     */
    static Template check(Map<String, Object> raw) {
        if (!(raw.get("id") instanceof String)) throw new IllegalArgumentException("no string id");
        var t = Template.of(raw);
        if (!t.steps().containsKey(t.start())) throw new IllegalArgumentException(t.id() + ": no start step " + raw.get("start"));
        Json.map(raw.get("steps")).forEach((name, s) -> {
            Object next = Json.map(s).get("next");
            if (next != null && !(next instanceof String n && t.steps().containsKey(n))) throw new IllegalArgumentException(t.id() + ": step " + name + " -> missing " + next);
            var o = t.steps().get(name).objective();
            if ("go".equals(o.get("type")) && !(o.get("place") instanceof String p && !p.isEmpty())) throw new IllegalArgumentException(t.id() + ": step " + name + " goes nowhere");
        });
        return t;
    }
}
