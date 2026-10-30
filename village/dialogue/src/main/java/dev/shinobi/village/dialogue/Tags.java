package dev.shinobi.village.dialogue;

import java.util.HashMap;
import java.util.Map;
import java.util.Set;

/**
 * What a line needs of the moment: for each tag, the values it may take ({@code any}), the values it may not
 * ({@code not}), or a numeric range ({@code level=3..10}). A tag the line does not name may be anything, with one
 * rule: a line with no {@code stage} is said by teens and adults only, so children speak only from lines written for
 * children.
 */
public final class Tags {
    public static final Tags NONE = new Tags(Map.of());
    private final Map<String, Need> needs;

    private record Need(Set<String> any, Set<String> not, int lo, int hi) {
        boolean ok(String value) {
            if (any != null) return value != null && any.contains(value);
            if (not != null) return value == null || !not.contains(value);
            if (value == null) return false;
            try { int v = Integer.parseInt(value); return v >= lo && v <= hi; } catch (NumberFormatException e) { return false; }
        }
    }

    private Tags(Map<String, Need> needs) { this.needs = needs; }

    static Tags read(Object compiled) {
        var m = Json.map(compiled);
        if (m.isEmpty()) return NONE;
        var needs = new HashMap<String, Need>();
        for (var e : m.entrySet()) {
            var t = Json.map(e.getValue());
            if (t.containsKey("range")) {
                var r = Json.list(t.get("range"));
                needs.put(e.getKey(), new Need(null, null, Json.integer(r.get(0), 0), Json.integer(r.get(1), 0)));
            } else if (t.containsKey("any")) needs.put(e.getKey(), new Need(strings(t.get("any")), null, 0, 0));
            else needs.put(e.getKey(), new Need(null, strings(t.get("not")), 0, 0));
        }
        return new Tags(Map.copyOf(needs));
    }
    private static Set<String> strings(Object o) {
        var out = new java.util.HashSet<String>();
        for (var v : Json.list(o)) out.add(v.toString());
        return Set.copyOf(out);
    }

    public boolean matches(Context c) {
        // story indexes the authoring gate; when evaluates it. A moment can have many completed story flags.
        for (var e : needs.entrySet()) if (!e.getKey().equals("story") && !e.getValue().ok(c.get(e.getKey()))) return false;
        return needs.containsKey("stage") || !"child".equals(c.get("stage"));
    }
    public boolean names(String key) { return needs.containsKey(key); }
    public int size() { return needs.size(); }
}
