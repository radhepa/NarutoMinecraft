package dev.shinobi.combat;

import java.util.ArrayList;
import java.util.LinkedHashMap;
import java.util.List;
import java.util.Map;

/**
 * A small JSON reader for data/combat/: objects become {@code Map<String, Object>} in file order, arrays
 * {@code List<Object>}, numbers {@code Double}. Phase 0's mod reads the same files through Minecraft's resource
 * manager and Gson; the core keeps this reader so it stays dependency-free.
 */
public final class Json {
    private final String s;
    private int i;

    private Json(String s) { this.s = s; }

    public static Object parse(String text) {
        var j = new Json(text);
        j.ws();
        Object v = j.value();
        j.ws();
        if (j.i != j.s.length()) throw j.error("trailing characters");
        return v;
    }

    private Object value() {
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
        i++;
        ws();
        if (peek('}')) { i++; return m; }
        while (true) {
            ws();
            String k = string();
            ws();
            expect(':');
            ws();
            m.put(k, value());
            ws();
            if (peek(',')) { i++; continue; }
            expect('}');
            return m;
        }
    }
    private List<Object> array() {
        var l = new ArrayList<Object>();
        i++;
        ws();
        if (peek(']')) { i++; return l; }
        while (true) {
            ws();
            l.add(value());
            ws();
            if (peek(',')) { i++; continue; }
            expect(']');
            return l;
        }
    }
    private String string() {
        expect('"');
        var b = new StringBuilder();
        while (true) {
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
    private Double number() {
        int start = i;
        while (i < s.length() && "+-0123456789.eE".indexOf(s.charAt(i)) >= 0) i++;
        if (start == i) throw error("unexpected character '" + s.charAt(i) + "'");
        return Double.parseDouble(s.substring(start, i));
    }
    private Object word(String w, Object v) {
        if (!s.startsWith(w, i)) throw error("expected " + w);
        i += w.length();
        return v;
    }
    private void ws() { while (i < s.length() && Character.isWhitespace(s.charAt(i))) i++; }
    private boolean peek(char c) { return i < s.length() && s.charAt(i) == c; }
    private void expect(char c) { if (!peek(c)) throw error("expected '" + c + "'"); i++; }
    private IllegalArgumentException error(String what) { return new IllegalArgumentException("JSON at " + i + ": " + what); }

    // Typed access to parsed trees, with defaults.
    @SuppressWarnings("unchecked")
    public static Map<String, Object> obj(Object o) { return o == null ? Map.of() : (Map<String, Object>) o; }
    @SuppressWarnings("unchecked")
    public static List<Object> list(Object o) { return o == null ? List.of() : (List<Object>) o; }
    public static Map<String, Object> obj(Map<String, Object> m, String k) { return obj(m.get(k)); }
    public static List<Object> list(Map<String, Object> m, String k) { return list(m.get(k)); }
    public static double num(Map<String, Object> m, String k, double dflt) { return m.get(k) instanceof Number n ? n.doubleValue() : dflt; }
    public static int integer(Map<String, Object> m, String k, int dflt) { return m.get(k) instanceof Number n ? n.intValue() : dflt; }
    public static String str(Map<String, Object> m, String k, String dflt) { return m.get(k) instanceof String v ? v : dflt; }
    public static boolean bool(Map<String, Object> m, String k) { return Boolean.TRUE.equals(m.get(k)); }
    public static List<String> strings(Map<String, Object> m, String k) {
        var out = new ArrayList<String>();
        for (Object o : list(m, k)) if (o instanceof String v) out.add(v);
        return out;
    }
}
