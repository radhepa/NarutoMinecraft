package dev.shinobi.life.bond;

import java.util.LinkedHashMap;
import java.util.List;
import java.util.Map;

/**
 * A tension, need or opportunity the village simulation raises, for the quest engine's side-quest generators to bind
 * to: what kind it is, who is involved (by the roles a quest template fills its slots from), where, when it was
 * raised and when it lapses, how pressing it is, what a quest must check before offering it, and what is at stake.
 * Quests resolve a hook with {@code resolve_hook} and one of the type's outcomes; an unresolved hook simply lapses.
 * See BONDS.md, "Society hooks", for the schema the quest engine reads ({@link #toMap}).
 */
public record SocietyHook(String id, String type, Map<String, String> roles, String place, long raised, long expires, double urgency,
        List<Map<String, Object>> requires, Map<String, Object> stakes) {
    public static final int FORMAT = 1;
    /** The hook types and the outcomes a quest can resolve each with. */
    public static final Map<String, List<String>> OUTCOMES = Map.ofEntries(
            Map.entry("clan_feud", List.of("mediated", "sided_a", "sided_b")),
            Map.entry("favor_needed", List.of("done", "refused")),
            Map.entry("quarrel_to_mediate", List.of("mediated", "failed")),
            Map.entry("secret_crush", List.of("helped", "kept_quiet", "told")),
            Map.entry("lost_item", List.of("returned", "kept")),
            Map.entry("newcomer", List.of("befriended", "ignored")),
            Map.entry("elder_request", List.of("done", "refused")),
            Map.entry("rivalry_heating", List.of("cooled", "fanned")),
            Map.entry("forbidden_match", List.of("supported", "discouraged")),
            Map.entry("estrangement", List.of("reconciled", "failed")));
    /** The kinds of favor a {@code favor_needed} hook can ask for ({@code stakes.variant}), picked from the client's life. */
    public static final List<String> FAVOR_VARIANTS = List.of("neighbor", "elder_errand", "lost_pet", "escort", "sick_relative", "shop_trouble",
            "apprentice", "festival_help");

    public SocietyHook {
        roles = Map.copyOf(roles); requires = List.copyOf(requires); stakes = Map.copyOf(stakes);
        if (!OUTCOMES.containsKey(type)) throw new IllegalArgumentException("unknown hook type " + type);
    }
    public boolean open(long day) { return day <= expires; }

    /** The hook as the quest engine reads it (JSON-shaped). */
    public Map<String, Object> toMap() {
        var m = new LinkedHashMap<String, Object>();
        m.put("format", FORMAT); m.put("id", id); m.put("type", type); m.put("roles", new java.util.TreeMap<>(roles)); m.put("place", place);
        m.put("raised", raised); m.put("expires", expires); m.put("urgency", Math.round(urgency * 100) / 100.0);
        m.put("requires", requires.isEmpty() ? Map.of() : Map.of("all", requires)); m.put("stakes", new java.util.TreeMap<>(stakes));
        m.put("outcomes", OUTCOMES.get(type));
        return m;
    }
}
