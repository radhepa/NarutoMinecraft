package dev.shinobi.progression;

import dev.shinobi.progression.mission.Json;
import dev.shinobi.progression.mission.Template;

import java.util.LinkedHashMap;
import java.util.Map;

/** Checking a quest file and casting it on the map, apart from the mod's entrypoint so it runs without a game. */
final class Quests {
    private Quests() {}

    /**
     * The quest in {@code raw}, or why it is broken: a string id, a start step, each step's {@code next} null or a step,
     * a place for every {@code go} and someone for every {@code talk}, every {@code slot:} reference declared, and
     * every slot one the runtime casts. Template reads a wrong-typed field as its default, so the raw fields are checked.
     */
    static Template check(Map<String, Object> raw) {
        if (!(raw.get("id") instanceof String)) throw new IllegalArgumentException("no string id");
        var t = Template.of(raw);
        if (!t.steps().containsKey(t.start())) throw new IllegalArgumentException(t.id() + ": no start step " + raw.get("start"));
        // shortcut: resident slots by job, bound roles and anchors only, until the mission generator's SlotFiller casts quests.
        t.slots().forEach((name, slot) -> {
            if (!(slot.get("pick") instanceof String pick && key(pick, slot) != null))
                throw new IllegalArgumentException(t.id() + ": slot " + name + " cannot be cast: " + slot);
        });
        Json.map(raw.get("steps")).forEach((name, s) -> {
            Object next = Json.map(s).get("next");
            if (next != null && !(next instanceof String n && t.steps().containsKey(n))) throw new IllegalArgumentException(t.id() + ": step " + name + " -> missing " + next);
            var o = t.steps().get(name).objective();
            String field = switch (Json.str(o.get("type"), "")) { case "go" -> "place"; case "talk" -> "who"; default -> null; };
            if (field == null) return;
            if (!(o.get(field) instanceof String ref && !ref.isEmpty())) throw new IllegalArgumentException(t.id() + ": step " + name + " has no " + field);
            if (ref.startsWith("slot:") && !t.slots().containsKey(ref.substring(5))) throw new IllegalArgumentException(t.id() + ": step " + name + " names undeclared " + ref);
            if ("talk".equals(o.get("type")) && !(ref.startsWith("slot:") && !"anchor".equals(t.slots().get(ref.substring(5)).get("pick"))))
                throw new IllegalArgumentException(t.id() + ": step " + name + " talks to " + ref + ", not a resident slot");
        });
        return t;
    }

    /** The key a slot is cast from in the map's roles ({@code job:}, {@code role:}) or anchors ({@code anchor:}); null if none. */
    static String key(String pick, Map<String, Object> slot) {
        return switch (pick) {
            case "resident" -> Json.map(slot.get("where")).get("job") instanceof String job ? "job:" + job : null;
            case "role" -> slot.get("role") instanceof String role ? "role:" + role : null;
            case "anchor" -> slot.get("tag") instanceof String tag ? "anchor:" + tag : null;
            default -> null;
        };
    }

    /**
     * Each slot's resident (its UUID) or anchor key on this map, and every place a step goes to checked there;
     * throws naming the first slot or place the map lacks, so accepting the quest can refuse it.
     */
    static Map<String, String> cast(Template t, Map<String, ?> roles, Map<String, ?> anchors) {
        var cast = new LinkedHashMap<String, String>();
        t.slots().forEach((name, slot) -> {
            String key = key(Json.str(slot.get("pick"), ""), slot);
            boolean anchor = key.startsWith("anchor:");
            Object found = anchor ? (anchors.containsKey(key) ? key : null) : roles.get(key);
            if (found == null) throw new IllegalArgumentException("no " + (anchor ? "" : "resident with ") + key + " on this map for " + name);
            cast.put(name, found.toString());
        });
        for (var step : t.steps().values())
            if ("go".equals(step.type()) && !anchors.containsKey(resolve(Json.str(step.objective().get("place"), ""), cast)))
                throw new IllegalArgumentException("no " + step.objective().get("place") + " on this map for step " + step.name());
        return Map.copyOf(cast);
    }

    /** A step's place or person: a {@code slot:} reference through the cast, anything else as written. */
    static String resolve(String ref, Map<String, String> cast) {
        return ref.startsWith("slot:") ? cast.get(ref.substring(5)) : ref;
    }
}
