package dev.shinobi.progression.mission;

import java.util.ArrayList;
import java.util.HashSet;
import java.util.LinkedHashMap;
import java.util.List;
import java.util.Map;
import java.util.Set;

import static dev.shinobi.progression.mission.Json.*;

/**
 * One board-mission template as compiled by {@code tools/missions/missions.py}: the quest format of ROADMAP.md
 * section 5 with {@code kind: mission}, plus the board's fields (rank, category, slots, twists, outcomes, bonuses,
 * places). The generator reads what it needs to roll and pace offers; the quest engine (Phase 0) runs the steps.
 */
public record Template(
        String id, Rank rank, String category, boolean later, int minutes, int days, String party,
        Map<String, Object> unlock, List<String> seasons, Map<String, Object> event,
        Map<String, Map<String, Object>> slots, String start, Map<String, Step> steps, List<Twist> twists,
        Map<String, Map<String, Object>> outcomes, List<String> bonuses, double fastHours, List<String> enemies,
        List<String> anchors, List<String> regions, double payWeight, List<String> tags, boolean contested,
        String chain, boolean classic) {

    public record Twist(String id, double weight, boolean harder, boolean modifier) {}
    public record Branch(Map<String, Object> condition, String next) {}
    public record Step(String name, String type, Map<String, Object> objective, String next, List<Branch> branches,
                       List<String> bonuses, List<Map<String, Object>> actions) {}

    @SuppressWarnings("unchecked")
    public static Template of(Map<String, Object> j) {
        var steps = new LinkedHashMap<String, Step>();
        map(j.get("steps")).forEach((name, raw) -> {
            var s = map(raw);
            var branches = list(s.get("branch")).stream()
                    .map(b -> new Branch(map(map(b).get("if")), str(map(b).get("next"), null))).toList();
            var actions = new ArrayList<Map<String, Object>>();
            for (Object a : list(s.get("on_enter"))) actions.add(map(a));
            for (Object a : list(s.get("on_done"))) actions.add(map(a));
            var objective = map(s.get("objective"));
            steps.put(name, new Step(name, str(objective.get("type"), "?"), objective, str(s.get("next"), null),
                    branches, strings(s.get("bonus")), actions));
        });
        var twists = list(j.get("twists")).stream().map(Json::map)
                .map(t -> new Twist(str(t.get("id"), "?"), num(t.get("weight"), 1), bool(t.get("harder")), bool(t.get("modifier"))))
                .toList();
        var slots = new LinkedHashMap<String, Map<String, Object>>();
        map(j.get("slots")).forEach((k, v) -> slots.put(k, map(v)));
        var outcomes = new LinkedHashMap<String, Map<String, Object>>();
        map(j.get("outcomes")).forEach((k, v) -> outcomes.put(k, map(v)));
        var places = map(j.get("places"));
        var pay = map(j.get("pay"));
        return new Template(
                str(j.get("id"), "?"), Rank.of(str(j.get("rank"), "d")), str(j.get("category"), "?"),
                "later".equals(j.get("status")), (int) num(j.get("minutes"), 10), (int) num(j.get("days"), 0),
                str(j.get("party"), "squad"), j.get("unlock") == null ? null : map(j.get("unlock")),
                strings(j.get("season")), j.get("event") == null ? null : map(j.get("event")),
                slots, str(j.get("start"), null), steps, twists, outcomes, strings(j.get("bonus")),
                num(j.get("fast_hours"), 0), strings(j.get("enemies")), strings(places.get("anchors")),
                strings(places.get("regions")), num(pay.get("weight"), 0.5), strings(j.get("tags")),
                bool(j.get("contested")), str(j.get("chain"), null), !Boolean.FALSE.equals(j.get("classic")));
    }

    public boolean soloAllowed() { return party.equals("solo") || party.equals("squad_or_solo"); }
    public boolean squadAllowed() { return !party.equals("solo"); }
    public boolean outsideVillage() { return !regions.isEmpty() || tags.contains("outside") || tags.contains("outdoors") || tags.contains("road"); }
    /** Minutes of play, counting a camp night's travel for multi-day missions. */
    public int playMinutes() { return minutes; }

    /**
     * The steps a run walks with this twist and these choices (step id to option): the generator's view of the graph,
     * used to check every twist has a path and to estimate length. Branches are tried in order, as the engine does;
     * a branch on an unknown condition is not taken.
     */
    public List<String> path(String twist, Map<String, String> choices) {
        var walked = new ArrayList<String>();
        var seen = new HashSet<String>();
        String at = start;
        while (at != null && seen.add(at)) {
            walked.add(at);
            Step s = steps.get(at);
            String next = s.next();
            for (Branch b : s.branches()) {
                if (passes(b.condition(), twist, choices)) { next = b.next(); break; }
            }
            if (s.type().equals("choose") && choices.containsKey(at)) {
                Object out = map(s.objective().get("options")).get(choices.get(at));
                boolean branched = s.branches().stream().anyMatch(b -> passes(b.condition(), twist, choices));
                if (out instanceof String && !branched) return walked;
            }
            if (s.actions().stream().anyMatch(a -> a.containsKey("mission_outcome"))) return walked;
            at = next;
        }
        return walked;
    }

    @SuppressWarnings("unchecked")
    private static boolean passes(Map<String, Object> c, String twist, Map<String, String> choices) {
        if (c.containsKey("twist")) return c.get("twist").equals(twist);
        if (c.containsKey("chose")) {
            var arg = (List<Object>) c.get("chose");
            return arg.get(1).equals(choices.get((String) arg.get(0)));
        }
        if (c.containsKey("all")) return list(c.get("all")).stream().allMatch(x -> passes(map(x), twist, choices));
        if (c.containsKey("any")) return list(c.get("any")).stream().anyMatch(x -> passes(map(x), twist, choices));
        if (c.containsKey("not")) return !passes(map(c.get("not")), twist, choices);
        return false;
    }

    /** Problems with the graph and references: the generator refuses a catalogue that has any. */
    public List<String> problems() {
        var p = new ArrayList<String>();
        if (start == null || !steps.containsKey(start)) p.add(id + ": no start step");
        Set<String> reach = new HashSet<>();
        var todo = new ArrayList<String>();
        if (start != null) todo.add(start);
        while (!todo.isEmpty()) {
            String n = todo.removeLast();
            if (n == null || !steps.containsKey(n) || !reach.add(n)) continue;
            Step s = steps.get(n);
            todo.add(s.next());
            s.branches().forEach(b -> todo.add(b.next()));
        }
        for (Step s : steps.values()) {
            if (!reach.contains(s.name())) p.add(id + ": step " + s.name() + " unreachable");
            if (s.next() != null && !steps.containsKey(s.next())) p.add(id + ": step " + s.name() + " -> missing " + s.next());
            for (Branch b : s.branches())
                if (!steps.containsKey(b.next())) p.add(id + ": branch of " + s.name() + " -> missing " + b.next());
        }
        for (Twist t : twists) {
            if (t.modifier()) continue;
            boolean branched = steps.values().stream().flatMap(s -> s.branches().stream())
                    .anyMatch(b -> t.id().equals(b.condition().get("twist")));
            if (!branched) p.add(id + ": twist " + t.id() + " has no branch");
            var plain = path(null, Map.of());
            var twisted = path(t.id(), Map.of());
            if (plain.equals(twisted)) p.add(id + ": twist " + t.id() + " does not change the path");
        }
        if (!outcomes.containsKey("done")) p.add(id + ": no 'done' outcome");
        if (twists.size() < 2) p.add(id + ": fewer than two twists");
        for (var e : slots.entrySet()) {
            if (e.getValue().get("pick") == null) p.add(id + ": slot " + e.getKey() + " has no pick");
        }
        return p;
    }
}
