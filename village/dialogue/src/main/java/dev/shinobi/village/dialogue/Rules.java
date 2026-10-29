package dev.shinobi.village.dialogue;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * The engine's tuning, from the compiled {@code rules.json} (source: {@code tools/dialogue/rules.json}): the talk
 * budget per speaker tier, the pools exempt from it, the filler cap, how many lines a speaker remembers saying, and
 * each topic's facets. Every number is data, so a balance pass is a datapack update.
 */
public record Rules(Map<String, Tier> tiers, List<String> exempt, double fillerCap, int recall,
                    Map<String, List<Facet>> facets, Map<String, String> topicAlias, Pacing pacing) {

    /** Questions: from which bond level, how many a day across everyone, and the days between one speaker's questions by level. */
    public record Pacing(int minLevel, int perDay, int[][] gapDays) {
        public int gap(int level) {
            int days = 0;
            for (int[] g : gapDays) if (level >= g[0]) days = g[1];
            return days;
        }
    }

    /**
     * Fresh exchanges a speaker of a tier gives the player: {@code daily} per in-game day, banked on days without
     * talk up to {@code bankDays} days' worth, and over a lifetime {@code base + perLevel x level + perSlice x slices}
     * ({@code base} null: no lifetime cap).
     */
    public record Tier(int daily, Integer base, int perLevel, int perSlice, int bankDays) {
        /** The most fresh exchanges a speaker can hold: today's and those banked on days without talk. */
        public int bankCap() { return daily * Math.max(1, bankDays); }
        public Integer lifetime(int level, int slices) { return base == null ? null : base + perLevel * level + perSlice * slices; }
    }
    /** A pool a topic draws from, with its weight and the tag it needs ("event", "weather:!clear", "stage:child", "!"). */
    public record Facet(String pool, int weight, String needs) {
        public boolean applies(Context c) {
            if (needs == null || needs.equals("!")) return true;
            int colon = needs.indexOf(':');
            if (colon < 0) return c.has(needs);
            String key = needs.substring(0, colon), value = needs.substring(colon + 1);
            String have = c.get(key);
            return value.startsWith("!") ? have != null && !have.equals(value.substring(1)) : value.equals(have);
        }
    }

    public Tier tier(String name) {
        var t = tiers.get(name == null ? "resident" : name);
        return t != null ? t : tiers.get("resident");
    }
    public boolean exempt(String pool) {
        for (String e : exempt) if (pool.equals(e) || pool.startsWith(e + ".")) return true;
        return false;
    }

    static Rules read(Object compiled) {
        var m = Json.map(compiled);
        var budget = Json.map(m.get("budget"));
        var tiers = new HashMap<String, Tier>();
        for (var e : Json.map(budget.get("tiers")).entrySet()) {
            var t = Json.map(e.getValue());
            Object base = t.get("base");
            tiers.put(e.getKey(), new Tier(Json.integer(t.get("daily"), 3), base == null ? null : Json.integer(base, 0),
                    Json.integer(t.get("per_level"), 0), Json.integer(t.get("per_slice"), 0), Json.integer(t.get("bank_days"), 1)));
        }
        var exempt = new ArrayList<String>();
        for (var x : Json.list(budget.get("exempt"))) exempt.add(x.toString());
        var facets = new HashMap<String, List<Facet>>();
        for (var e : Json.map(m.get("facets")).entrySet()) {
            if (e.getKey().startsWith("_")) continue;
            var list = new ArrayList<Facet>();
            for (var f : Json.list(e.getValue())) {
                var fm = Json.map(f);
                list.add(new Facet(Json.str(fm.get("pool")), Json.integer(fm.get("weight"), 1), Json.str(fm.get("needs"))));
            }
            facets.put(e.getKey(), List.copyOf(list));
        }
        var alias = new HashMap<String, String>();
        for (var e : Json.map(m.get("topic_alias")).entrySet()) alias.put(e.getKey(), e.getValue().toString());
        Object cap = m.get("filler_cap");
        var q = Json.map(m.get("questions"));
        var gaps = new ArrayList<int[]>();
        for (var g : Json.list(q.get("gap_days"))) gaps.add(new int[] {Json.integer(Json.map(g).get("level"), 0), Json.integer(Json.map(g).get("days"), 0)});
        var pacing = new Pacing(Json.integer(q.get("min_level"), 0), Json.integer(q.get("per_day"), 99), gaps.toArray(new int[0][]));
        return new Rules(Map.copyOf(tiers), List.copyOf(exempt), cap == null ? 0.2 : ((Number) cap).doubleValue(),
                Json.integer(m.get("recall"), 6), Map.copyOf(facets), Map.copyOf(alias), pacing);
    }
}
