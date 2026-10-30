package dev.shinobi.progression;

import dev.shinobi.progression.mission.Json;
import dev.shinobi.progression.mission.Template;

import java.util.LinkedHashMap;
import java.util.List;
import java.util.Map;
import java.util.stream.Stream;

/** Checking a quest file, casting it on the map and walking its steps, apart from the mod's entrypoint so it runs without a game. */
final class Quests {
    private Quests() {}

    /** A quest's step graph, its title key, and each step's {@code on_enter} and {@code on_done} actions. */
    record Quest(Template template, String title, Map<String, List<Object>> onEnter, Map<String, List<Object>> onDone) {}

    /** The checked quest in {@code raw}, with its actions. */
    static Quest quest(Map<String, Object> raw) {
        var t = check(raw);
        var enter = new LinkedHashMap<String, List<Object>>();
        var done = new LinkedHashMap<String, List<Object>>();
        Json.map(raw.get("steps")).forEach((name, s) -> {
            enter.put(name, Json.list(Json.map(s).get("on_enter")));
            done.put(name, Json.list(Json.map(s).get("on_done")));
        });
        return new Quest(t, Json.str(raw.get("title"), "quest." + t.id() + ".title"), Map.copyOf(enter), Map.copyOf(done));
    }

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
            for (Object b : Json.list(Json.map(s).get("branch"))) {
                if (!(Json.map(b).get("next") instanceof String n && t.steps().containsKey(n))) throw new IllegalArgumentException(t.id() + ": step " + name + " branches to missing " + Json.map(b).get("next"));
                condition(t.id() + ": step " + name, Json.map(b).get("if"), t.id());
            }
            for (String when : List.of("on_enter", "on_done"))
                for (Object a : Json.list(Json.map(s).get(when))) action(t.id() + ": step " + name + " " + when, a);
            var o = t.steps().get(name).objective();
            String field;
            try { field = field(Json.str(o.get("type"), "")); }
            catch (IllegalArgumentException e) { throw new IllegalArgumentException(t.id() + ": step " + name + " has unknown type " + o.get("type")); }
            if ("choose".equals(o.get("type")) && !(o.get("flag") instanceof String f && !f.isEmpty() && o.get("options") instanceof List<?> l && !l.isEmpty()
                    && l.stream().allMatch(x -> x instanceof String opt && opt.matches("[a-z0-9_]+")) && l.stream().distinct().count() == l.size()))
                throw new IllegalArgumentException(t.id() + ": step " + name + " needs a flag and distinct lower-case options");
            if ("cast".equals(o.get("type")) && !(o.get("technique") instanceof String tech && !tech.isEmpty()))
                throw new IllegalArgumentException(t.id() + ": step " + name + " needs a technique to cast");
            if (field == null) return;
            if (!(o.get(field) instanceof String ref && !ref.isEmpty())) throw new IllegalArgumentException(t.id() + ": step " + name + " has no " + field);
            if (ref.startsWith("slot:") && !t.slots().containsKey(ref.substring(5))) throw new IllegalArgumentException(t.id() + ": step " + name + " names undeclared " + ref);
            if ("talk".equals(o.get("type")) && !(ref.startsWith("slot:") && !"anchor".equals(t.slots().get(ref.substring(5)).get("pick"))))
                throw new IllegalArgumentException(t.id() + ": step " + name + " talks to " + ref + ", not a resident slot");
        });
        return t;
    }

    /**
     * Refuses a condition the runtime cannot answer. shortcut: {@code all}, {@code any}, {@code not}, {@code flag} and
     * {@code quest_state} only, until Shinobi Core's condition registry answers the rest (ROADMAP.md, "Conditions and actions").
     * Quest ids and flag names are checked across the files by {@code tools/missions/missions.py --quests}, not here.
     */
    static void condition(String where, Object cond, String self) {
        var m = Json.map(cond);
        if (m.size() != 1) throw new IllegalArgumentException(where + ": a condition needs exactly one key: " + cond);
        var e = m.entrySet().iterator().next();
        Object v = e.getValue();
        switch (e.getKey()) {
            case "all", "any" -> { if (!(v instanceof List<?> l) || l.isEmpty()) throw new IllegalArgumentException(where + ": " + e.getKey() + " needs a list"); l.forEach(x -> condition(where, x, self)); }
            case "not" -> condition(where, v, self);
            case "flag" -> { if (!(v instanceof String)) throw new IllegalArgumentException(where + ": flag needs a name"); }
            case "quest_state" -> {
                if (!(v instanceof List<?> l && l.size() == 2 && l.get(0) instanceof String && l.get(1) instanceof String st && List.of("done", "active", "not_started").contains(st)))
                    throw new IllegalArgumentException(where + ": quest_state needs [quest, done|active|not_started]");
                // A quest is still active while its own branches are tested.
                if (self.equals(l.get(0))) throw new IllegalArgumentException(where + ": quest_state cannot name its own quest");
            }
            default -> throw new IllegalArgumentException(where + ": unknown condition " + e.getKey());
        }
    }

    /** Whether a checked condition holds for the journal. */
    static boolean test(Object cond, Journal j) {
        var e = Json.map(cond).entrySet().iterator().next();
        Object v = e.getValue();
        return switch (e.getKey()) {
            case "all" -> Json.list(v).stream().allMatch(x -> test(x, j));
            case "any" -> Json.list(v).stream().anyMatch(x -> test(x, j));
            case "not" -> !test(v, j);
            case "flag" -> j.flags().contains((String) v);
            case "quest_state" -> j.state((String) Json.list(v).get(0)).equals(Json.list(v).get(1));
            default -> false;
        };
    }

    /**
     * Refuses an action the runtime cannot run. shortcut: {@code set_flag}, {@code give_ryo}, {@code give_item} (one of
     * an item id), {@code teach_technique} (a technique id), {@code say} (a line's lang key) and {@code start_quest}
     * (a quest id) only, until Shinobi Core's action registry.
     */
    /** The ranks a set_rank may name, as the player record spells them. */
    static final List<String> RANKS = List.of("academy", "genin", "chunin", "jonin", "anbu", "hokage");

    static void action(String where, Object action) {
        var m = Json.map(action);
        boolean ok = m.size() == 1 && (m.get("set_flag") instanceof List<?> l && l.size() == 2 && l.get(0) instanceof String && l.get(1) instanceof Boolean
                || m.get("give_ryo") instanceof Number n && n.doubleValue() >= 1 && n.doubleValue() <= Integer.MAX_VALUE && n.doubleValue() == Math.rint(n.doubleValue())
                || m.get("give_item") instanceof String item && !item.isEmpty()
                || m.get("teach_technique") instanceof String technique && !technique.isEmpty()
                || m.get("say") instanceof String line && !line.isEmpty()
                || m.get("start_quest") instanceof String quest && !quest.isEmpty()
                || m.get("set_rank") instanceof String rank && RANKS.contains(rank));
        if (!ok) throw new IllegalArgumentException(where + ": unknown or malformed action " + action
                + " (set_flag [name, true|false], give_ryo <whole ryo>, give_item <item id>, teach_technique <technique id>, say <lang key>, start_quest <quest id> or set_rank <" + String.join("|", RANKS) + ">)");
    }

    /**
     * The journal after some actions, the ryo and items they give (on each pass, so a step that loops back gives again),
     * the techniques they teach, the lines they say and the quests they start.
     */
    record Outcome(Journal journal, int ryo, List<String> items, List<String> taught, List<String> said, List<String> started, String rank) {
        Outcome(Journal journal, int ryo) { this(journal, ryo, List.of(), List.of(), List.of(), List.of(), null); }
        Outcome with(Journal j) { return new Outcome(j, ryo, items, taught, said, started, rank); }
    }

    static Outcome run(List<Object> actions, Outcome o) {
        for (Object a : actions) {
            var m = Json.map(a);
            if (m.get("give_ryo") instanceof Number n) o = new Outcome(o.journal(), o.ryo() + n.intValue(), o.items(), o.taught(), o.said(), o.started(), o.rank());
            else if (m.get("give_item") instanceof String item) o = new Outcome(o.journal(), o.ryo(), plus(o.items(), item), o.taught(), o.said(), o.started(), o.rank());
            else if (m.get("teach_technique") instanceof String t) o = new Outcome(o.journal(), o.ryo(), o.items(), plus(o.taught(), t), o.said(), o.started(), o.rank());
            else if (m.get("say") instanceof String line) o = new Outcome(o.journal(), o.ryo(), o.items(), o.taught(), plus(o.said(), line), o.started(), o.rank());
            else if (m.get("start_quest") instanceof String q) o = new Outcome(o.journal(), o.ryo(), o.items(), o.taught(), o.said(), plus(o.started(), q), o.rank());
            else if (m.get("set_rank") instanceof String r) o = new Outcome(o.journal(), o.ryo(), o.items(), o.taught(), o.said(), o.started(), r);
            else {
                var flag = Json.list(m.get("set_flag"));
                o = o.with(o.journal().flag((String) flag.get(0), (Boolean) flag.get(1)));
            }
        }
        return o;
    }

    private static List<String> plus(List<String> l, String x) { return Stream.concat(l.stream(), Stream.of(x)).toList(); }

    /** The journal with the quest accepted on this cast and its first step's {@code on_enter} run. */
    static Outcome start(Journal j, Quest q, Map<String, String> cast) {
        return run(q.onEnter().get(q.template().start()), new Outcome(j.accept(q.template(), cast), 0));
    }

    /** The journal once the quest's current step is done: its {@code on_done}, the branch or next step, the new step's {@code on_enter}. */
    static Outcome complete(Journal j, Quest q) {
        String id = q.template().id(), at = j.active().get(id);
        if (at == null) return new Outcome(j, 0);
        return complete(q, run(q.onDone().get(at), new Outcome(j, 0)));
    }

    /**
     * The journal once the player picks {@code option} at the quest's current choose step: the flag {@code <flag>.<option>}
     * set, then the step done as {@link #complete}; null if the quest is not at a choose step offering it.
     */
    static Outcome answer(Journal j, Quest q, String option) {
        var step = j.active().get(q.template().id()) instanceof String at ? q.template().steps().get(at) : null;
        if (step == null || !"choose".equals(step.type()) || !Json.list(step.objective().get("options")).contains(option)) return null;
        return complete(j.flag(step.objective().get("flag") + "." + option, true), q);
    }

    private static Outcome complete(Quest q, Outcome after) {
        String id = q.template().id();
        var moved = after.with(after.journal().advance(q.template(), c -> test(c, after.journal())));
        String now = moved.journal().active().get(id);
        return now == null ? moved : run(q.onEnter().get(now), moved);
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
            if ("place".equals(field(step.type())) && !anchors.containsKey(resolve(Json.str(step.objective().get("place"), ""), cast)))
                throw new IllegalArgumentException("no " + step.objective().get("place") + " on this map for step " + step.name());
        return Map.copyOf(cast);
    }

    /**
     * The objective field naming a step's place or person: place for go and spar, who for talk, null for furnish, sleep,
     * scene (done once its lines are said), choose (done when the player picks an option) and cast (done when the player
     * casts its technique).
     */
    static String field(String type) {
        return switch (type) {
            case "go", "spar" -> "place";
            case "talk" -> "who";
            case "furnish", "sleep", "scene", "choose", "cast" -> null;
            default -> throw new IllegalArgumentException("unknown step type " + type);
        };
    }

    /** A step's place or person: a {@code slot:} reference through the cast, anything else as written. */
    static String resolve(String ref, Map<String, String> cast) {
        return ref.startsWith("slot:") ? cast.get(ref.substring(5)) : ref;
    }
}
