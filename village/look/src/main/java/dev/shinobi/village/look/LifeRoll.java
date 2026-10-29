package dev.shinobi.village.look;

import java.util.ArrayList;
import java.util.List;
import java.util.Map;

/**
 * Varied's "Roll a life": an origin by the shinobi groups' population weights (as the rolled cast is drawn, so most
 * rolls are clanless), then a whole child-stage look from that origin's own weighted pools, on the save seed's
 * {@code creator} stream. The same seed always suggests the same character; tools/creator/creator.py rolls the same
 * numbers (the compiled file's {@code parity} list holds both sides to it).
 */
public final class LifeRoll {
    /** A roll: the origin, the look, and the family name (the clan's, or one from the pool). */
    public record Rolled(String origin, Look look, String family) {}

    public static String origin(CreatorRules rules, long seed) {
        var groups = rules.population();
        int total = groups.values().stream().mapToInt(Integer::intValue).sum();
        int n = Seeds.stream(seed, "creator", "origin").below(total);
        String last = null;
        for (var e : groups.entrySet()) {
            if (n < e.getValue()) return e.getKey();
            n -= e.getValue();
            last = e.getKey();
        }
        return last;
    }

    @SuppressWarnings("unchecked")
    public static Rolled look(CreatorRules rules, long seed, String origin) {
        var o = rules.origin(origin);
        var w = CreatorRules.map(o.get("roll"));
        var c = rules.choices(origin, AgeStage.CHILD);
        var rng = Seeds.stream(seed, "creator", "look:" + origin);
        String body = rng.pick(rules.bodies);
        var outfit = rng.pick(c.outfits().get(body));
        var marks = new ArrayList<String>();
        for (Object m : (List<Object>) w.get("marks")) {
            var mark = CreatorRules.map(m);
            if (rng.unit() < ((Number) mark.get("chance")).doubleValue()) marks.add((String) mark.get("id"));
        }
        var kept = marks.subList(0, Math.min(marks.size(), rules.maxMarks));
        int complexion = ((Number) rng.pick((List<Object>) w.get("complexions"))).intValue();
        String eyeStyle = rng.pick(rules.eyeStyles);
        String brows = rng.pick(rules.brows);
        String hair = rng.pick(c.hair());
        String hairColor = rng.pick(CreatorRules.strings(w.get("hair_colors")));
        String eyeColor = rng.pick(CreatorRules.strings(w.get("eye_colors")));
        String palette = rng.pick(outfit.palettes());
        String headwear = rng.pick(c.headwear());
        String family = rng.pick(rules.familyNames(origin));
        return new Rolled(origin, new Look(body, complexion, eyeStyle, brows, hair, hairColor, eyeColor, kept, outfit.id(), palette, headwear), family);
    }

    public static Rolled roll(CreatorRules rules, long seed) { return look(rules, seed, origin(rules, seed)); }

    /** The roll as the compiled file's parity entries write it. */
    public static Map<String, Object> toMap(Rolled r) {
        var m = new java.util.LinkedHashMap<>(r.look().toMap());
        m.put("family", r.family());
        return m;
    }

    private LifeRoll() {}
}
