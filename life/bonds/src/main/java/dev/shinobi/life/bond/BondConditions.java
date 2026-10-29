package dev.shinobi.life.bond;

import java.util.List;
import java.util.Map;

/**
 * The bond conditions of Core's condition language (ROADMAP.md, "Conditions and actions"), read from parsed JSON
 * (maps, lists, strings and numbers). Shinobi Life registers each with Core as {@code life:<name>}; quest data may
 * write the bare name. A role group ({@code role:squad}, {@code role:teammates}) passes only if every member does.
 *
 * <pre>
 * {"friendship":     ["role:teammate_a", 5]}          level they act on, at least
 * {"bond_meter":     ["role:sensei", "trust", 60]}    a meter, at least
 * {"bond_memory":    ["role:teammate_b", "kept_secret"]}
 * {"bond_moment":    ["role:teammate_a", "bond.teammate_a.1"]}
 * {"bond_state":     ["role:teammate_b", "making_up"]} none, argument, cold_shoulder, making_up, falling_out
 * {"romance_stage":  ["role:x", "dating"]}            at least this stage
 * {"kindling":       ["role:teammate_a", "nature"]}   at least this tier
 * {"knows_fact":     ["role:rival", "dream"]}
 * {"squad_cohesion": 60}
 * {"in_squad":       "role:teammate_b"}
 * {"squad_can_return": "role:teammate_b"}
 * {"standing":       ["clan:nara", "good_neighbor"]}  at least this title
 * {"jealous":        "role:teammate_b"}                jealousy at 40 or more
 * </pre>
 * {@code all}, {@code any} and {@code not} are here only so the bond engine can be tested alone; Core owns them.
 */
public final class BondConditions {
    @SuppressWarnings("unchecked")
    public static boolean test(BondWorld w, Map<String, Object> condition) {
        if (condition.size() != 1) throw new IllegalArgumentException("a condition has one key: " + condition);
        var e = condition.entrySet().iterator().next();
        Object arg = e.getValue();
        return switch (e.getKey()) {
            case "all" -> ((List<Map<String, Object>>) arg).stream().allMatch(c -> test(w, c));
            case "any" -> ((List<Map<String, Object>>) arg).stream().anyMatch(c -> test(w, c));
            case "not" -> !test(w, (Map<String, Object>) arg);
            case "friendship" -> every(w, at(arg, 0), who -> w.effectiveLevel(who) >= num(at(arg, 1)));
            case "bond_meter" -> every(w, at(arg, 0), who -> w.meters(who).get(Meter.of(str(at(arg, 1)))) >= num(at(arg, 2)));
            case "bond_memory" -> every(w, at(arg, 0), who -> w.bond(who).remembers(Act.of(str(at(arg, 1)))));
            case "bond_moment" -> every(w, at(arg, 0), who -> w.bond(who).moments().contains(str(at(arg, 1))));
            case "bond_state" -> every(w, at(arg, 0), who -> w.bond(who).conflict().state() == Conflict.State.of(str(at(arg, 1))));
            case "romance_stage" -> every(w, at(arg, 0), who -> w.bond(who).romance().compareTo(Courtship.Stage.of(str(at(arg, 1)))) >= 0);
            case "kindling" -> every(w, at(arg, 0), who -> Kindling.tier(w, who).compareTo(Kindling.Tier.of(str(at(arg, 1)))) >= 0);
            case "knows_fact" -> every(w, at(arg, 0), who -> BondBook.page(w, who).facts().stream()
                    .anyMatch(f -> f.key().equals("bond.fact." + str(at(arg, 1))) && f.known()));
            case "squad_cohesion" -> w.cohesion() >= num(arg);
            case "in_squad" -> w.squad() != null && w.squad().has(str(arg));
            case "squad_can_return" -> w.canReturn(str(arg));
            case "standing" -> w.title(str(at(arg, 0))).compareTo(Standing.Title.of(str(at(arg, 1)))) >= 0;
            case "jealous" -> w.squad() != null && w.squad().jealousy(str(arg)) >= Squad.JEALOUS;
            default -> throw new IllegalArgumentException("not a bond condition: " + e.getKey());
        };
    }
    public static boolean known(String name) {
        return List.of("friendship", "bond_meter", "bond_memory", "bond_moment", "bond_state", "romance_stage", "kindling", "knows_fact",
                "squad_cohesion", "in_squad", "squad_can_return", "standing", "jealous").contains(name);
    }

    static boolean every(BondWorld w, Object ref, java.util.function.Predicate<String> test) {
        var who = w.resolve(str(ref));
        return !who.isEmpty() && who.stream().allMatch(test);
    }
    static Object at(Object list, int i) {
        if (!(list instanceof List<?> l) || l.size() <= i) throw new IllegalArgumentException("expected a list with item " + i + ": " + list);
        return l.get(i);
    }
    static String str(Object o) { if (o instanceof String s) return s; throw new IllegalArgumentException("expected a string: " + o); }
    static double num(Object o) { if (o instanceof Number n) return n.doubleValue(); throw new IllegalArgumentException("expected a number: " + o); }

    private BondConditions() {}
}
