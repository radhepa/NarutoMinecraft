package dev.shinobi.progression.mission;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.LinkedHashMap;
import java.util.List;
import java.util.Map;

import static dev.shinobi.progression.mission.Json.*;

/**
 * Fills a template's slots from the save's {@code missions} stream (ROADMAP.md, "Board missions"): who the client is,
 * where the job happens, which enemy group, how many. Residents come from a query on their profile, anchors from a
 * tag, regions and groups from a list, roles from the save's bound cast; a {@code suspect} slot names one of the
 * other resident slots (the rolled culprit). Fresh clients and anchors are preferred ({@link VarietyGuard}); the
 * squad is never cast. Returns null when a slot cannot be filled, and the desk tries another template.
 */
public final class SlotFiller {
    final World world;
    final Map<String, Resident> byId = new HashMap<>();

    public SlotFiller(World world) {
        this.world = world;
        world.residents().forEach(r -> byId.put(r.id(), r));
    }

    public Map<String, String> fill(Template t, Seeds.Rng rng, VarietyGuard guard, int day, String forcedClient) {
        return fill(t, rng, guard, day, forcedClient, null);
    }

    /** As above; {@code returning}, when given, picks the client from the residents it accepts if any fits. */
    public Map<String, String> fill(Template t, Seeds.Rng rng, VarietyGuard guard, int day, String forcedClient,
                                    java.util.function.Predicate<String> returning) {
        for (int attempt = 0; attempt < ATTEMPTS; attempt++) {
            var slots = tryFill(t, rng, guard, day, forcedClient, attempt == 0 ? returning : null);
            if (slots != null) return slots;
        }
        return null;
    }

    /** A later slot can depend on an earlier one (a parent of the client, a neighbour in their district); a cast that
     *  leaves it empty is thrown away and tried again, a few times. */
    static final int ATTEMPTS = 6;

    Map<String, String> tryFill(Template t, Seeds.Rng rng, VarietyGuard guard, int day, String forcedClient,
                                java.util.function.Predicate<String> returning) {
        var filled = new LinkedHashMap<String, String>();
        var deferred = new ArrayList<String>();
        for (var e : t.slots().entrySet()) {
            String name = e.getKey();
            var slot = e.getValue();
            if ("suspect".equals(slot.get("pick"))) { deferred.add(name); continue; }
            String v = name.equals("client") && forcedClient != null ? forcedClient
                    : pick(slot, rng, guard, day, filled, name.equals("client") ? returning : null);
            if (v == null) return null;
            filled.put(name, v);
        }
        for (String name : deferred) {
            var from = strings(t.slots().get(name).get("from"));
            filled.put(name, filled.get(from.get(rng.below(from.size()))));
        }
        return filled;
    }

    String pick(Map<String, Object> slot, Seeds.Rng rng, VarietyGuard guard, int day, Map<String, String> filled,
                java.util.function.Predicate<String> returning) {
        return switch (str(slot.get("pick"), "")) {
            case "resident" -> resident(map(slot.get("where")), rng, guard, day, filled, returning);
            case "anchor" -> {
                List<String> all = world.anchors((String) slot.get("tag"));
                if (all.isEmpty()) yield null;
                var fresh = all.stream().filter(a -> guard.anchorFresh(a, day) && !filled.containsValue(a)).toList();
                var from = fresh.isEmpty() ? all : fresh;
                yield from.get(rng.below(from.size()));
            }
            case "region", "one_of", "enemy_group" -> {
                var from = strings(slot.get("from"));
                yield from.isEmpty() ? null : from.get(rng.below(from.size()));
            }
            case "count" -> {
                var range = list(slot.get("range"));
                int lo = (int) num(range.get(0), 1), hi = (int) num(range.get(1), lo);
                yield String.valueOf(lo + rng.below(hi - lo + 1));
            }
            case "role" -> world.role((String) slot.get("role"));
            default -> null;
        };
    }

    String resident(Map<String, Object> where, Seeds.Rng rng, VarietyGuard guard, int day, Map<String, String> filled,
                    java.util.function.Predicate<String> returning) {
        var squad = world.squad();
        var fits = world.residents().stream()
                .filter(r -> !squad.contains(r.id()) && !filled.containsValue(r.id()) && r.matches(where, filled, byId))
                .toList();
        if (fits.isEmpty()) return null;
        var fresh = fits.stream().filter(r -> guard.clientFresh(r.id(), day)).toList();
        if (returning != null) {
            var known = fresh.stream().filter(r -> returning.test(r.id())).toList();
            if (!known.isEmpty()) return known.get(rng.below(known.size())).id();
        }
        var from = fresh.isEmpty() ? fits : fresh;
        return from.get(rng.below(from.size())).id();
    }

    public Resident resident(String id) { return byId.get(id); }
}
