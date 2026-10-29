package dev.shinobi.life.bond;

import static dev.shinobi.life.bond.BondConditions.at;
import static dev.shinobi.life.bond.BondConditions.num;
import static dev.shinobi.life.bond.BondConditions.str;

import java.util.ArrayList;
import java.util.List;
import java.util.Map;

/**
 * The bond actions of Core's action language, read from parsed JSON. Shinobi Life registers each as
 * {@code life:<name>}; {@code remove_from_squad} and {@code marry} are the reserved names ROADMAP.md already lists.
 * A role group applies to every member. Returns "" on success, otherwise why it did nothing (quest logs show it).
 *
 * <pre>
 * {"add_friendship":    ["role:teammate_a", 3]}             warmth, as a quest reward ({"role:squad": 3} in "rewards")
 * {"bond_event":        ["role:squad", "camp_night"]}       an act; with witnesses:
 * {"bond_event":        {"who": "role:teammate_b", "act": "saved_life", "witnesses": ["role:teammate_a"]}}
 * {"shared_moment":     ["role:teammate_a", "bond.teammate_a.1"]}
 * {"start_conflict":    ["role:rival", "quarrel"]}
 * {"apologize": "role:x"}  {"reconcile": "role:x"}  {"mend": "role:x"}
 * {"reveal_fact":       ["role:rival", "dream"]}
 * {"romance":           ["role:x", "ask_out"]}             ask_out, confess, propose, wed ({"marry": "role:x"} = wed)
 * {"remove_from_squad": ["role:teammate_b", "story"]}       story, exam, low_bond
 * {"return_to_squad":   "role:teammate_b"}
 * {"favor":             ["role:teammate_a", 3]}
 * {"deed":              {"act": "defended_village", "about": "", "witnesses": ["role:squad"]}}
 * {"celebrate_birthday": "role:x"}
 * {"bond_flag":         ["role:x", "met_family"]}
 * {"set_flag":          ["story.kindling.awakened", true]} the flags the bond engine reads (Core keeps the rest)
 * {"kindle":            "role:teammate_a"}                 a use of Kindling Bond, counted
 * {"resolve_hook":      ["hook.clan_feud.12", "mediated"]} a side quest settles a society hook
 * {"clan_event":        ["inuzuka", "aburame", 10, "festival"]}
 * {"clan_deed":         {"clan": "hyuga", "act": "honored_custom"}}  witnessed by the clan's members
 * {"mood_event":        ["village", 0.4, 0]}               cheer and tension (a festival, an attack)
 * {"ask_question":      ["role:teammate_b", "q.advice.first_mission"]}  a scene asks it now, outside the budget
 * </pre>
 */
public final class BondEffects {
    @SuppressWarnings("unchecked")
    public static String apply(BondWorld w, Map<String, Object> action) {
        if (action.size() != 1) throw new IllegalArgumentException("an action has one key: " + action);
        var e = action.entrySet().iterator().next();
        Object arg = e.getValue();
        return switch (e.getKey()) {
            case "add_friendship" -> arg instanceof Map<?, ?> rewards
                    ? join(((Map<String, Object>) rewards).entrySet().stream().map(r -> each(w, r.getKey(), who -> { w.addFriendship(who, num(r.getValue())); return ""; })).toList())
                    : each(w, at(arg, 0), who -> { w.addFriendship(who, num(at(arg, 1))); return ""; });
            case "bond_event" -> {
                if (arg instanceof Map<?, ?> m) {
                    var spec = (Map<String, Object>) m;
                    var witnesses = new ArrayList<String>();
                    for (Object o : (List<Object>) spec.getOrDefault("witnesses", List.of())) witnesses.addAll(w.resolve(str(o)));
                    Act act = Act.of(str(spec.get("act")));
                    yield each(w, spec.get("who"), who -> { w.act(who, act, witnesses.stream().filter(x -> !x.equals(who)).toList()); return ""; });
                }
                Act act = Act.of(str(at(arg, 1)));
                var group = w.resolve(str(at(arg, 0)));
                if (group.isEmpty()) yield "nobody";
                if (act.experience != null && group.size() > 1) { w.experience(act, group); yield ""; }
                yield each(w, at(arg, 0), who -> { w.act(who, act); return ""; });
            }
            case "shared_moment" -> each(w, at(arg, 0), who -> { w.moment(who, str(at(arg, 1))); return ""; });
            case "start_conflict" -> each(w, at(arg, 0), who -> { w.quarrel(who, Act.of(str(at(arg, 1)))); return ""; });
            case "apologize" -> each(w, arg, who -> w.apologize(who) ? "" : "not_accepted");
            case "reconcile" -> each(w, arg, who -> w.reconcile(who) ? "" : "not_ready");
            case "mend" -> each(w, arg, who -> { w.mend(who); return ""; });
            case "reveal_fact" -> each(w, at(arg, 0), who -> { w.reveal(who, str(at(arg, 1))); return ""; });
            case "romance" -> each(w, at(arg, 0), who -> w.court(who, str(at(arg, 1))));
            case "marry" -> each(w, arg, who -> w.court(who, "wed"));
            case "remove_from_squad" -> each(w, at(arg, 0), who -> { w.leaveSquad(who, str(at(arg, 1))); return ""; });
            case "return_to_squad" -> each(w, arg, who -> w.returnToSquad(who) ? "" : "not_departed");
            case "favor" -> each(w, at(arg, 0), who -> { w.favor(who, num(at(arg, 1))); return ""; });
            case "deed" -> {
                var spec = (Map<String, Object>) arg;
                var witnesses = new ArrayList<String>();
                for (Object o : (List<Object>) spec.getOrDefault("witnesses", List.of())) witnesses.addAll(w.resolve(str(o)));
                String about = str(spec.getOrDefault("about", ""));
                w.deed(Act.of(str(spec.get("act"))), about.isEmpty() ? "" : w.resolve(about).stream().findFirst().orElse(""), witnesses);
                yield "";
            }
            case "celebrate_birthday" -> each(w, arg, who -> w.celebrate(who) ? "" : "not_today");
            case "bond_flag" -> each(w, at(arg, 0), who -> { w.setBondFlag(who, str(at(arg, 1))); return ""; });
            case "set_flag" -> { w.setFlag(str(at(arg, 0)), !(at(arg, 1) instanceof Boolean b) || b); yield ""; }
            case "ask_question" -> each(w, at(arg, 0), who -> { Questions.ask(w, who, str(at(arg, 1))); return ""; });
            case "kindle" -> each(w, arg, who -> w.kindle(who).natureCasts() > 0 ? "" : "no_bond");
            case "resolve_hook" -> w.village() == null ? "no_village" : w.village().resolve(str(at(arg, 0)), str(at(arg, 1)));
            case "clan_event" -> {
                if (w.village() == null) yield "no_village";
                w.village().relations().event(str(at(arg, 0)), str(at(arg, 1)), num(at(arg, 2)), str(at(arg, 3)), w.day());
                yield "";
            }
            case "clan_deed" -> {
                var spec = (Map<String, Object>) arg;
                String clan = str(spec.get("clan"));
                var members = w.people().stream().filter(p -> p.clan().equals(clan)).map(Person::id).toList();
                if (members.isEmpty()) yield "nobody";
                var house = w.village() == null ? null : w.village().house(clan);
                w.deed(Act.of(str(spec.get("act"))), house != null ? house.head() : members.getFirst(), members);
                yield "";
            }
            case "mood_event" -> {
                if (w.village() == null) yield "no_village";
                w.village().push(str(at(arg, 0)), num(at(arg, 1)), num(at(arg, 2)));
                yield "";
            }
            default -> throw new IllegalArgumentException("not a bond action: " + e.getKey());
        };
    }
    public static boolean known(String name) {
        return List.of("add_friendship", "bond_event", "shared_moment", "start_conflict", "apologize", "reconcile", "mend", "reveal_fact",
                "romance", "marry", "remove_from_squad", "return_to_squad", "favor", "deed", "celebrate_birthday", "bond_flag", "set_flag",
                "kindle", "resolve_hook", "clan_event", "clan_deed", "mood_event", "ask_question").contains(name);
    }

    private static String each(BondWorld w, Object ref, java.util.function.Function<String, String> f) {
        var who = w.resolve(str(ref));
        if (who.isEmpty()) return "nobody";
        return join(who.stream().map(f).toList());
    }
    private static String join(List<String> results) {
        return String.join(",", results.stream().filter(s -> !s.isEmpty()).distinct().toList());
    }

    private BondEffects() {}
}
