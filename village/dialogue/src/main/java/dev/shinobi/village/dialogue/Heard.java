package dev.shinobi.village.dialogue;

import java.util.ArrayList;
import java.util.Base64;
import java.util.BitSet;
import java.util.HashMap;
import java.util.LinkedHashMap;
import java.util.List;
import java.util.Map;

/**
 * The per-save heard ledger (DIALOGUE.md, "Storage"): one bit for every line and question the player has heard, one
 * for every content group spent, the answers they gave, and a small record per speaker they have talked to (today's
 * and lifetime fresh exchanges, filler share, the last few lines that speaker said, for repeating). Saved as plain
 * maps and strings, which the Village mod wraps in a Codec as a player attachment ({@code narutominecraft:heard}).
 * A worst case for 100 hours (30,000 lines, 25,000 of them heard, 300 speakers with full recall, 80 answers) is about
 * 25 KB.
 */
public final class Heard {
    public static final int FORMAT = 1;
    private static final int FIXED = 9;

    final BitSet lines = new BitSet();
    final BitSet groups = new BitSet();
    final Map<String, Speaker> speakers = new HashMap<>();
    final Map<String, String> answers = new LinkedHashMap<>();
    /** For each question axis, the pole last taken and on which question: "pole:question". */
    final Map<String, String> axes = new HashMap<>();
    /** Questions asked across everyone today. */
    int askDay = -1, asksToday;

    /** What one speaker has said to the player (saved as base-36 numbers: day, today, over, greeting day, lifetime, fresh, filler, the day of their last question, then the recall ring). */
    public static final class Speaker {
        int day = -1, today, over, greetDay = -1, askDay = -1000;
        int lifetime, fresh, filler;
        final int[] recall;
        int recallNext;

        Speaker(int size) { recall = new int[size]; }

        void roll(int now) {
            if (day != now) { day = now; today = 0; over = 0; }
        }
        void said(int id) {
            for (int r : recall) if (r == id) return;
            recall[recallNext] = id;
            recallNext = (recallNext + 1) % recall.length;
        }
        public int today() { return today; }
        public int lifetime() { return lifetime; }
        public int fresh() { return fresh; }
        public int filler() { return filler; }
    }

    public boolean heard(int id) { return lines.get(id); }
    public boolean spent(int group) { return group > 0 && groups.get(group); }
    public int heardCount() { return lines.cardinality(); }
    public String answer(String question) { return answers.get(question); }
    public Map<String, String> answers() { return Map.copyOf(answers); }

    void mark(Line l) {
        lines.set(l.id());
        if (l.group() > 0) groups.set(l.group());
    }
    void unmark(Line l) { lines.clear(l.id()); }

    public Speaker speaker(String id, int recall) { return speakers.computeIfAbsent(id, k -> new Speaker(recall)); }
    public Speaker speakerOrNull(String id) { return speakers.get(id); }

    // -- save --------------------------------------------------------------------------------------------------

    public Map<String, Object> write() {
        var out = new LinkedHashMap<String, Object>();
        out.put("format", FORMAT);
        out.put("lines", bits(lines));
        out.put("groups", bits(groups));
        var sp = new LinkedHashMap<String, Object>();
        for (var e : speakers.entrySet()) {
            var s = e.getValue();
            var b = new StringBuilder();
            for (int v : new int[] {s.day, s.today, s.over, s.greetDay, s.lifetime, s.fresh, s.filler, s.askDay, s.recallNext})
                b.append(Integer.toString(v, 36)).append(',');
            for (int r : s.recall) b.append(Integer.toString(r, 36)).append(',');
            b.setLength(b.length() - 1);
            sp.put(e.getKey(), b.toString());
        }
        out.put("speakers", sp);
        out.put("answers", new LinkedHashMap<>(answers));
        out.put("axes", new LinkedHashMap<>(axes));
        out.put("asks", askDay + "," + asksToday);
        return out;
    }
    public static Heard read(Map<String, Object> saved, int recall) {
        var h = new Heard();
        int format = Json.integer(saved.get("format"), FORMAT);
        if (format > FORMAT) throw new IllegalArgumentException("heard ledger format " + format + " is newer than this engine (" + FORMAT + ")");
        h.lines.or(unbits(Json.str(saved.get("lines"))));
        h.groups.or(unbits(Json.str(saved.get("groups"))));
        for (var e : Json.map(saved.get("speakers")).entrySet()) {
            String[] t = e.getValue().toString().split(",");
            int[] f = new int[t.length];
            for (int k = 0; k < t.length; k++) f[k] = Integer.parseInt(t[k], 36);
            var s = new Speaker(Math.max(recall, f.length - FIXED));
            s.day = f[0]; s.today = f[1]; s.over = f[2]; s.greetDay = f[3]; s.lifetime = f[4]; s.fresh = f[5]; s.filler = f[6];
            s.askDay = f[7]; s.recallNext = f[8] % s.recall.length;
            for (int k = FIXED; k < f.length && k - FIXED < s.recall.length; k++) s.recall[k - FIXED] = f[k];
            h.speakers.put(e.getKey(), s);
        }
        for (var e : Json.map(saved.get("answers")).entrySet()) h.answers.put(e.getKey(), e.getValue().toString());
        for (var e : Json.map(saved.get("axes")).entrySet()) h.axes.put(e.getKey(), e.getValue().toString());
        String asks = Json.str(saved.get("asks"));
        if (asks != null) { h.askDay = Integer.parseInt(asks.split(",")[0]); h.asksToday = Integer.parseInt(asks.split(",")[1]); }
        return h;
    }
    /** About how many bytes the saved ledger takes (the strings it writes). */
    public int size() {
        int n = 0;
        for (var v : write().values()) n += String.valueOf(v).length();
        return n;
    }

    private static String bits(BitSet b) { return Base64.getEncoder().withoutPadding().encodeToString(b.toByteArray()); }
    private static BitSet unbits(String s) { return s == null || s.isEmpty() ? new BitSet() : BitSet.valueOf(Base64.getDecoder().decode(s)); }

    /** Speakers the player has talked to, for the simulation's report. */
    public List<String> speakerIds() { return new ArrayList<>(speakers.keySet()); }
}
