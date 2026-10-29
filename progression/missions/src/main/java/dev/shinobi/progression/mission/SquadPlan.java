package dev.shinobi.progression.mission;

import java.util.ArrayList;
import java.util.LinkedHashMap;
import java.util.List;
import java.util.Map;

import static dev.shinobi.progression.mission.Json.*;

/**
 * Teammates' roles on a mission (MISSIONS.md section 6), from {@code squad.json}. At the briefing the player gives each
 * teammate a role: point, guard, tracker or support. Each mission category wants two roles; a teammate whose
 * aptitude matches the role they were given, in a role the mission wants, is a <b>good call</b> and lifts the grade.
 * Every assignment is attention for the bond engine's jealousy rules. The squad's cohesion
 * (BONDS.md section 7) picks a band: in step and steady squads assist each other; ragged and split squads do not,
 * and a split squad's teammates sometimes ignore an order.
 */
public final class SquadPlan {
    /** A teammate as the planner sees them: clan, strongest personality traits, and whether they have a ninken. */
    public record Mate(String id, String clan, List<String> traits, boolean ninken) {}
    public record Band(String name, int score, boolean assists, double disobey) {}

    final Map<String, Object> squad;

    public SquadPlan(Map<String, Object> squadJson) { this.squad = squadJson; }

    public List<String> wanted(String category) {
        var wanted = map(squad.get("wanted"));
        return strings(wanted.containsKey(category) ? wanted.get(category) : wanted.get("*"));
    }

    /** The roles a teammate is good at, best first. */
    public List<String> aptitude(Mate m) {
        var out = new ArrayList<String>();
        for (Object o : list(map(squad.get("aptitude")).get("rules"))) {
            var rule = map(o);
            var cond = map(rule.get("if"));
            boolean ok = true;
            if (cond.containsKey("has_ninken")) ok &= m.ninken() == bool(cond.get("has_ninken"));
            if (cond.containsKey("clan")) ok &= strings(cond.get("clan")).contains(m.clan());
            if (cond.containsKey("trait")) ok &= m.traits().contains((String) cond.get("trait"));
            if (ok) for (String r : strings(rule.get("roles"))) if (!out.contains(r)) out.add(r);
        }
        return out;
    }

    /** The best assignment for a category: each wanted role to the teammate most suited, everyone else to support. */
    public Map<String, String> suggest(String category, List<Mate> mates) {
        var plan = new LinkedHashMap<String, String>();
        var free = new ArrayList<>(mates);
        for (String role : wanted(category)) {
            Mate best = null;
            int bestRank = Integer.MAX_VALUE;
            for (Mate m : free) {
                int k = aptitude(m).indexOf(role);
                if (k >= 0 && k < bestRank) { best = m; bestRank = k; }
            }
            if (best != null) { plan.put(best.id(), role); free.remove(best); }
        }
        for (Mate m : free) plan.put(m.id(), "support");
        return plan;
    }

    /** A good call: at least one teammate holds a wanted role they are suited to, and nobody holds one they are not. */
    public boolean goodCall(String category, Map<String, String> plan, List<Mate> mates) {
        var wanted = wanted(category);
        boolean any = false;
        for (Mate m : mates) {
            String role = plan.get(m.id());
            if (role == null) continue;
            boolean suited = aptitude(m).contains(role);
            if (wanted.contains(role) && suited) any = true;
            if (wanted.contains(role) && !suited) return false;
        }
        return any;
    }

    public Band band(double cohesion) {
        for (Object o : list(squad.get("cohesion"))) {
            var b = map(o);
            if (cohesion >= num(b.get("min"), 0))
                return new Band(str(b.get("name"), "?"), (int) num(b.get("score"), 0), bool(b.get("assists")), num(b.get("disobey"), 0));
        }
        return new Band("split", -10, false, 0.15);
    }

    /** The dialogue key a teammate speaks from at a phase of a mission (the dialogue session writes the lines). */
    public static String banter(String category, String phase, String band) {
        return "mission.banter." + category + "." + phase + (band == null ? "" : "." + band);
    }
}
