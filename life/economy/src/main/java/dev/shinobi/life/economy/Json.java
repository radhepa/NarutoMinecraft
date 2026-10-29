package dev.shinobi.life.economy;

import java.util.ArrayList;
import java.util.LinkedHashMap;
import java.util.List;
import java.util.Map;

/**
 * A small JSON reader for the item data, so the module needs no library: objects become {@code Map<String, Object>}
 * (in file order), arrays {@code List<Object>}, numbers {@code Double} or {@code Long}, and the rest strings,
 * booleans and null. Phase 0 reads the same files through Minecraft's codecs instead.
 */
public final class Json {
    private final String s;
    private int i;

    private Json(String s) { this.s = s; }

    public static Object parse(String text) {
        var json = new Json(text);
        Object value = json.value();
        json.space();
        if (json.i != json.s.length()) throw json.fail("trailing text");
        return value;
    }

    @SuppressWarnings("unchecked")
    public static Map<String, Object> obj(Object o) { return (Map<String, Object>) o; }
    @SuppressWarnings("unchecked")
    public static List<Object> list(Object o) { return o == null ? List.of() : (List<Object>) o; }
    public static double num(Object o, double fallback) { return o instanceof Number n ? n.doubleValue() : fallback; }
    public static int integer(Object o, int fallback) { return o instanceof Number n ? n.intValue() : fallback; }
    public static String str(Object o, String fallback) { return o instanceof String t ? t : fallback; }

    private Object value() {
        space();
        if (i >= s.length()) throw fail("unexpected end");
        char c = s.charAt(i);
        return switch (c) {
            case '{' -> object();
            case '[' -> array();
            case '"' -> string();
            case 't' -> word("true", Boolean.TRUE);
            case 'f' -> word("false", Boolean.FALSE);
            case 'n' -> word("null", null);
            default -> number();
        };
    }

    private Map<String, Object> object() {
        var map = new LinkedHashMap<String, Object>();
        i++;
        space();
        if (peek('}')) { i++; return map; }
        while (true) {
            space();
            String key = string();
            space();
            expect(':');
            map.put(key, value());
            space();
            if (peek(',')) { i++; continue; }
            expect('}');
            return map;
        }
    }

    private List<Object> array() {
        var list = new ArrayList<Object>();
        i++;
        space();
        if (peek(']')) { i++; return list; }
        while (true) {
            list.add(value());
            space();
            if (peek(',')) { i++; continue; }
            expect(']');
            return list;
        }
    }

    private String string() {
        expect('"');
        var out = new StringBuilder();
        while (true) {
            if (i >= s.length()) throw fail("unterminated string");
            char c = s.charAt(i++);
            if (c == '"') return out.toString();
            if (c != '\\') { out.append(c); continue; }
            char e = s.charAt(i++);
            switch (e) {
                case 'n' -> out.append('\n');
                case 't' -> out.append('\t');
                case 'r' -> out.append('\r');
                case 'b' -> out.append('\b');
                case 'f' -> out.append('\f');
                case 'u' -> { out.append((char) Integer.parseInt(s.substring(i, i + 4), 16)); i += 4; }
                default -> out.append(e);
            }
        }
    }

    private Object number() {
        int start = i;
        while (i < s.length() && "+-0123456789.eE".indexOf(s.charAt(i)) >= 0) i++;
        String t = s.substring(start, i);
        if (t.isEmpty()) throw fail("unexpected character");
        return t.contains(".") || t.contains("e") || t.contains("E") ? (Object) Double.parseDouble(t) : (Object) Long.parseLong(t);
    }

    private Object word(String w, Object value) {
        if (!s.startsWith(w, i)) throw fail("expected " + w);
        i += w.length();
        return value;
    }

    private void space() { while (i < s.length() && Character.isWhitespace(s.charAt(i))) i++; }
    private boolean peek(char c) { return i < s.length() && s.charAt(i) == c; }
    private void expect(char c) {
        if (!peek(c)) throw fail("expected '" + c + "'");
        i++;
    }
    private IllegalArgumentException fail(String why) { return new IllegalArgumentException("JSON at " + i + ": " + why); }
}
