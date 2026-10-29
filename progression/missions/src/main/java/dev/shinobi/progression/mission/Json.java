package dev.shinobi.progression.mission;

import java.util.ArrayList;
import java.util.LinkedHashMap;
import java.util.List;
import java.util.Map;

/**
 * A small JSON reader for the datapack's mission files: objects become insertion-ordered maps, arrays lists, numbers
 * doubles. Phase 0 reads the same files through Minecraft's codecs; this keeps the generator free of dependencies.
 */
public final class Json {
    private final String s;
    private int i;

    private Json(String s) { this.s = s; }

    public static Object parse(String text) {
        var p = new Json(text);
        Object v = p.value();
        p.ws();
        if (p.i != p.s.length()) throw p.error("trailing text");
        return v;
    }

    @SuppressWarnings("unchecked")
    public static Map<String, Object> object(String text) { return (Map<String, Object>) parse(text); }

    private Object value() {
        ws();
        if (i >= s.length()) throw error("unexpected end");
        char c = s.charAt(i);
        return switch (c) {
            case '{' -> obj();
            case '[' -> arr();
            case '"' -> str();
            case 't' -> lit("true", Boolean.TRUE);
            case 'f' -> lit("false", Boolean.FALSE);
            case 'n' -> lit("null", null);
            default -> num();
        };
    }

    private Map<String, Object> obj() {
        var m = new LinkedHashMap<String, Object>();
        i++;
        ws();
        if (peek('}')) { i++; return m; }
        while (true) {
            ws();
            String k = str();
            ws();
            expect(':');
            m.put(k, value());
            ws();
            if (peek(',')) { i++; continue; }
            expect('}');
            return m;
        }
    }

    private List<Object> arr() {
        var l = new ArrayList<Object>();
        i++;
        ws();
        if (peek(']')) { i++; return l; }
        while (true) {
            l.add(value());
            ws();
            if (peek(',')) { i++; continue; }
            expect(']');
            return l;
        }
    }

    private String str() {
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

    private Double num() {
        int start = i;
        while (i < s.length() && "+-0123456789.eE".indexOf(s.charAt(i)) >= 0) i++;
        if (start == i) throw error("unexpected character");
        return Double.parseDouble(s.substring(start, i));
    }

    private Object lit(String word, Object v) {
        if (!s.startsWith(word, i)) throw error("expected " + word);
        i += word.length();
        return v;
    }

    private void ws() { while (i < s.length() && Character.isWhitespace(s.charAt(i))) i++; }
    private boolean peek(char c) { return i < s.length() && s.charAt(i) == c; }
    private void expect(char c) { if (!peek(c)) throw error("expected '" + c + "'"); i++; }
    private IllegalArgumentException error(String why) { return new IllegalArgumentException(why + " at " + i); }

    // --- typed access to parsed values ---------------------------------------------------------------------

    @SuppressWarnings("unchecked")
    public static Map<String, Object> map(Object o) { return o == null ? Map.of() : (Map<String, Object>) o; }
    @SuppressWarnings("unchecked")
    public static List<Object> list(Object o) { return o == null ? List.of() : (List<Object>) o; }
    public static List<String> strings(Object o) { return list(o).stream().map(String::valueOf).toList(); }
    public static double num(Object o, double fallback) { return o instanceof Number n ? n.doubleValue() : fallback; }
    public static String str(Object o, String fallback) { return o instanceof String x ? x : fallback; }
    public static boolean bool(Object o) { return o instanceof Boolean b && b; }
}
