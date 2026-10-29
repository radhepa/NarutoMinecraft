package dev.shinobi.life.bond;

import java.util.ArrayList;
import java.util.List;
import java.util.Locale;
import java.util.Map;
import java.util.TreeMap;

/**
 * How the clans (and the clanless and civilian groups) feel about each other: a symmetric matrix from -100 (a feud)
 * to 100 (sworn allies). Each pair has a base, from old alliances, rivalries, grudges, trade ties and marriage ties,
 * and a current value that events move ({@link #event}) and that drifts back toward the base by
 * {@link #DRIFT} of the gap each week. Marriages between two clans raise their base a little for good.
 */
public final class ClanRelations {
    public static final double DRIFT = .05, MARRIAGE_BOND = 3;

    public enum Label {
        FEUD(-100), RIVALS(-40), COOL(-15), NEUTRAL(-5), FRIENDLY(15), ALLIES(45);
        public final double from;
        Label(double from) { this.from = from; }
        public String id() { return name().toLowerCase(Locale.ROOT); }
        public static Label of(double v) { Label l = FEUD; for (Label x : values()) if (v >= x.from) l = x; return l; }
    }
    /** Why two clans start where they do: old alliance, rivalry, grudge, trade or marriage ties. */
    public record Base(double value, String why) {}

    private static final Map<String, Base> BASE = new TreeMap<>();
    private static void base(String a, String b, double v, String why) { BASE.put(pair(a, b), new Base(v, why)); }
    static {
        base("nara", "akimichi", 60, "alliance"); base("nara", "yamanaka", 60, "alliance"); base("akimichi", "yamanaka", 60, "alliance");
        base("senju", "uzumaki", 55, "alliance"); base("senju", "sarutobi", 30, "alliance"); base("sarutobi", "uzumaki", 15, "marriage");
        base("senju", "uchiha", -20, "rivalry"); base("uchiha", "hyuga", -15, "rivalry"); base("hyuga", "aburame", 10, "marriage");
        base("inuzuka", "aburame", -25, "grudge"); base("inuzuka", "hatake", 20, "alliance"); base("uchiha", "morino", 20, "duty");
        base("gekko", "namiashi", 20, "trade"); base("tsuchigumo", "hagane", 15, "trade");
        base("kurama", "yuhi", 25, "alliance"); base("umino", "haruno", 15, "marriage"); base("tobari", "shiranui", 15, "duty");
        for (String trade : List.of("akimichi", "hagane", "kinoshita", "yamanaka", "suzuran")) base(trade, ClanProfile.CIVILIAN, 20, "trade");
        base("uchiha", ClanProfile.CIVILIAN, -10, "rivalry"); base("hyuga", ClanProfile.CLANLESS, -10, "rivalry");
        base(ClanProfile.CLANLESS, ClanProfile.CIVILIAN, 15, "neighbors");
    }
    static String pair(String a, String b) { return a.compareTo(b) < 0 ? a + "|" + b : b + "|" + a; }
    /** The clan or group a person counts in. */
    public static String groupOf(Person p) { return !p.clan().isEmpty() ? p.clan() : p.shinobi() ? ClanProfile.CLANLESS : ClanProfile.CIVILIAN; }

    private final Map<String, Double> current = new TreeMap<>(), bonus = new TreeMap<>();
    private final List<String> log = new ArrayList<>();

    public static Base baseOf(String a, String b) { return a.equals(b) ? new Base(60, "kin") : BASE.getOrDefault(pair(a, b), new Base(0, "")); }
    public double base(String a, String b) { return a.equals(b) ? 60 : baseOf(a, b).value() + bonus.getOrDefault(pair(a, b), 0.0); }
    public double get(String a, String b) { return a.equals(b) ? 60 : current.getOrDefault(pair(a, b), base(a, b)); }
    public Label label(String a, String b) { return Label.of(get(a, b)); }
    /** Something between two clans (an incident, a favor, the player taking a side): moves the current value. */
    public void event(String a, String b, double delta, String why, long day) {
        if (a.equals(b)) return;
        current.put(pair(a, b), Math.clamp(get(a, b) + delta, -100, 100));
        log.add(day + " " + pair(a, b) + " " + (delta >= 0 ? "+" : "") + Math.round(delta) + " " + why);
        if (log.size() > 200) log.removeFirst();
    }
    /** A marriage between two clans: a little warmer for good. */
    public void married(String a, String b, long day) {
        if (a.equals(b)) return;
        bonus.merge(pair(a, b), MARRIAGE_BOND, Double::sum);
        event(a, b, MARRIAGE_BOND * 2, "marriage", day);
    }
    /** A week passes: every moved pair drifts back toward its base. */
    public void week() {
        for (var e : List.copyOf(current.entrySet())) {
            String[] ab = e.getKey().split("\\|");
            double b = base(ab[0], ab[1]), v = e.getValue() + (base(ab[0], ab[1]) - e.getValue()) * DRIFT;
            if (Math.abs(v - b) < .5) current.remove(e.getKey()); else current.put(e.getKey(), v);
        }
    }
    public List<String> log() { return List.copyOf(log); }
    Map<String, Double> moved() { return Map.copyOf(current); }
    Map<String, Double> bonuses() { return Map.copyOf(bonus); }
    void restore(Map<String, Double> moved, Map<String, Double> bonuses) { current.putAll(moved); bonus.putAll(bonuses); }
}
