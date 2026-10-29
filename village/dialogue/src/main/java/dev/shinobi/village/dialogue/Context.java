package dev.shinobi.village.dialogue;

import java.util.HashMap;
import java.util.Map;

/**
 * The moment a line is chosen for, as tags: who is speaking ({@code personality}, {@code clan}, {@code group},
 * {@code rank}, {@code job}, {@code stage}, {@code role}, {@code tier}), how they stand with the player ({@code level},
 * {@code band}, {@code quarrel}), the world ({@code time}, {@code weather}, {@code season}, {@code district},
 * {@code event}, {@code market}, {@code mood}) and the player ({@code player_rank}, {@code player_stage},
 * {@code clan_status}, {@code same_clan}, {@code slice}). {@code fill} holds token values ({@code item}, {@code place},
 * {@code friend}...). The glue builds one from the world; tests build them by hand. Immutable.
 */
public final class Context {
    private final Map<String, String> tags;
    private final Map<String, String> fill;

    private Context(Map<String, String> tags, Map<String, String> fill) { this.tags = tags; this.fill = fill; }

    public static Context of(String... keyValues) {
        var m = new HashMap<String, String>();
        for (int k = 0; k + 1 < keyValues.length; k += 2) if (keyValues[k + 1] != null) m.put(keyValues[k], keyValues[k + 1]);
        return new Context(withBand(m), Map.of());
    }
    /** A copy with one more tag (or a tag changed; null removes it). */
    public Context with(String key, String value) {
        var m = new HashMap<>(tags);
        if (value == null) m.remove(key); else m.put(key, value);
        return new Context(withBand(m), fill);
    }
    public Context with(String key, int value) { return with(key, Integer.toString(value)); }
    /** A copy with a token value ({@code {item}}, {@code {place}}...). */
    public Context fill(String token, String value) {
        var f = new HashMap<>(fill);
        f.put(token, value);
        return new Context(tags, f);
    }

    public String get(String key) { return tags.get(key); }
    public boolean has(String key) { return tags.containsKey(key); }
    public int level() { return number("level", 0); }
    public int number(String key, int otherwise) {
        String v = tags.get(key);
        if (v == null) return otherwise;
        try { return Integer.parseInt(v); } catch (NumberFormatException e) { return otherwise; }
    }
    public String filled(String token) { return fill.get(token); }
    public Map<String, String> tags() { return Map.copyOf(tags); }

    /** VF's relationship bands, from the bond level (Talk.band in Village Friends). */
    public static String band(int level) {
        return level <= 0 ? "stranger" : level <= 2 ? "acquaintance" : level <= 4 ? "friend" : level <= 7 ? "close" : "best";
    }
    private static Map<String, String> withBand(Map<String, String> m) {
        if (m.containsKey("level") && !m.containsKey("band")) {
            try { m.put("band", band(Integer.parseInt(m.get("level")))); } catch (NumberFormatException ignored) {}
        }
        return m;
    }
    @Override public String toString() { return tags.toString(); }
}
