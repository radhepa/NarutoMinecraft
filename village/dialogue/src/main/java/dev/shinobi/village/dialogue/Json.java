package dev.shinobi.village.dialogue;

import java.util.ArrayList;
import java.util.LinkedHashMap;
import java.util.List;
import java.util.Map;

/**
 * A small JSON reader for the compiled bank, so the engine needs no library: objects become {@link LinkedHashMap},
 * arrays {@link ArrayList}, numbers {@link Long} or {@link Double}. The Minecraft glue may hand over Gson's output
 * converted to the same shapes instead.
 */
public final class Json {
    private final String s;
    private int i;

    private Json(String s) { this.s = s; }

    public static Object parse(String text) {
        var p = new Json(text);
        Object v = p.value();
        p.space();
        if (p.i != p.s.length()) throw p.error("trailing text");
        return v;
    }

    private Object value() {
        space();
        if (i >= s.length()) throw error("unexpected end");
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
        var m = new LinkedHashMap<String, Object>();
        i++; space();
        if (peek('}')) { i++; return m; }
        while (true) {
            space();
            String key = string();
            space(); expect(':');
            m.put(key, value());
            space();
            if (peek(',')) { i++; continue; }
            expect('}');
            return m;
        }
    }
    private List<Object> array() {
        var a = new ArrayList<Object>();
        i++; space();
        if (peek(']')) { i++; return a; }
        while (true) {
            a.add(value());
            space();
            if (peek(',')) { i++; continue; }
            expect(']');
            return a;
        }
    }
    private String string() {
        expect('"');
        var b = new StringBuilder();
        while (true) {
            if (i >= s.length()) throw error("unterminated string");
            char c = s.charAt(i++);
            if (c == '"') return b.toString();
            if (c != '\\') { b.append(c); continue; }
            char e = s.charAt(i++);
            switch (e) {
                case 'n' -> b.append('\n');
                case 't' -> b.append('\t');
                case 'r' -> b.append('\r');
                case 'b' -> b.append('\b');
                case 'f' -> b.append('\f');
                case 'u' -> { b.append((char) Integer.parseInt(s.substring(i, i + 4), 16)); i += 4; }
                default -> b.append(e);
            }
        }
    }
    private Object number() {
        int start = i;
        while (i < s.length() && "+-0123456789.eE".indexOf(s.charAt(i)) >= 0) i++;
        String n = s.substring(start, i);
        if (n.isEmpty()) throw error("unexpected character");
        if (n.contains(".") || n.contains("e") || n.contains("E")) return Double.parseDouble(n);
        return Long.parseLong(n);
    }
    private Object word(String w, Object v) {
        if (!s.startsWith(w, i)) throw error("expected " + w);
        i += w.length();
        return v;
    }
    private void space() { while (i < s.length() && Character.isWhitespace(s.charAt(i))) i++; }
    private boolean peek(char c) { return i < s.length() && s.charAt(i) == c; }
    private void expect(char c) {
        if (!peek(c)) throw error("expected '" + c + "'");
        i++;
    }
    private IllegalArgumentException error(String what) { return new IllegalArgumentException("JSON: " + what + " at " + i); }

    // -- reading helpers for the compiled shapes ---------------------------------------------------------------

    @SuppressWarnings("unchecked")
    static Map<String, Object> map(Object o) { return o == null ? Map.of() : (Map<String, Object>) o; }
    @SuppressWarnings("unchecked")
    static List<Object> list(Object o) { return o == null ? List.of() : (List<Object>) o; }
    static int integer(Object o, int otherwise) { return o == null ? otherwise : ((Number) o).intValue(); }
    static String str(Object o) { return o == null ? null : o.toString(); }
}
