package dev.shinobi.life.bond;

import java.util.ArrayList;
import java.util.List;
import java.util.Map;
import java.util.TreeMap;

/**
 * The player's squad: teammates and a sensei, and what lives between them.
 *
 * <ul>
 * <li><b>Cohesion</b> (0 to 100), its own number: <pre>0.35 avg trust + 0.35 (avg affection + 100) / 2
 *     + 0.2 min(100, 5 x missions) + 0.1 (100 - avg jealousy) - 12 x quarrels inside the squad</pre> over every
 *     squadmate's feeling toward the player and toward each other.</li>
 * <li><b>Favoritism and jealousy:</b> talks, gifts, meals and being picked as partner are attention, which fades by
 *     half in a week. A teammate who gets clearly less than their share ({@link #FAIR_SLACK}) grows jealous, faster
 *     if proud; at {@link #JEALOUS} they feel overlooked (by you, and toward whoever you favor), and at
 *     {@link #BOILS} it boils over into a quarrel (not again while that quarrel lasts).</li>
 * <li><b>Sensei trust</b> is the sensei's trust meter: orders followed or disobeyed, missions won or failed.</li>
 * <li><b>Leaving and coming back:</b> a teammate whose bond stays low (the level they act on at 1 or less, trust
 *     under 10, or a falling-out) for {@link #LOW_DAYS} days leaves and stays in the village, if a classmate on the bench can take
 *     their place (otherwise they stay on, strained), and at most one leaves every {@link #LOW_DAYS} days. The story can also remove someone. Once their bond is back at level 4 with no quarrel, they
 *     can come back ({@code squad_can_return}, then {@code return_to_squad}).</li>
 * </ul>
 */
public final class Squad {
    public static final double FAIR_SLACK = .15, JEALOUS = 40, BOILS = 70, ATTENTION_HALF_LIFE = 7, MIN_ATTENTION = 4;
    public static final int LOW_DAYS = 14, GRACE_DAYS = 7, RETURN_LEVEL = 4, LOW_LEVEL = 1;
    public static final double LOW_TRUST = 10;

    public record Departure(String reason, long day, String replacedBy) {}

    final String id;
    String sensei;
    final List<String> teammates = new ArrayList<>(), bench = new ArrayList<>();
    final long formed;
    int missions;
    final Map<String, Double> attention = new TreeMap<>(), jealousy = new TreeMap<>();
    final Map<String, Integer> lowDays = new TreeMap<>();
    final Map<String, Departure> departed = new TreeMap<>();
    final Map<String, Boolean> overlooked = new TreeMap<>();

    Squad(String id, String sensei, List<String> teammates, List<String> bench, long formed) {
        this.id = id; this.sensei = sensei; this.formed = formed;
        this.teammates.addAll(teammates); this.bench.addAll(bench);
    }
    public String id() { return id; }
    public String sensei() { return sensei; }
    public List<String> teammates() { return List.copyOf(teammates); }
    public List<String> bench() { return List.copyOf(bench); }
    public List<String> members() { var all = new ArrayList<>(teammates); if (sensei != null) all.add(sensei); return all; }
    public int missions() { return missions; }
    public long formed() { return formed; }
    public double jealousy(String who) { return jealousy.getOrDefault(who, 0.0); }
    public double attention(String who) { return attention.getOrDefault(who, 0.0); }
    public Map<String, Departure> departed() { return Map.copyOf(departed); }
    public boolean has(String who) { return teammates.contains(who) || who.equals(sensei); }

    void favor(String who, double amount) { if (teammates.contains(who)) attention.merge(who, amount, Double::sum); }

    /** The teammate who gets the most attention, or "" when nobody stands out. */
    public String favorite() {
        String best = ""; double most = 0, total = 0;
        for (String t : teammates) { double a = attention(t); total += a; if (a > most) { most = a; best = t; } }
        return total >= MIN_ATTENTION && teammates.size() > 1 && most / total > 1.0 / teammates.size() + FAIR_SLACK ? best : "";
    }

    public static double cohesion(double avgTrust, double avgAffection, int missions, double avgJealousy, int quarrels) {
        return Math.clamp(.35 * avgTrust + .35 * (avgAffection + 100) / 2 + .2 * Math.min(100, 5 * missions) + .1 * (100 - avgJealousy) - 12 * quarrels, 0, 100);
    }
    /** Today's jealousy for one teammate, from their share of the attention. */
    static double jealousy(double current, double share, int teammates, double pride) {
        double gap = 1.0 / teammates - share;
        return gap > FAIR_SLACK ? Math.min(100, current + 25 * gap * (1 + .5 * pride)) : current * .85;
    }
    static double fadeAttention(double a) { return a * Math.pow(.5, 1 / ATTENTION_HALF_LIFE); }

    /** Leaves the squad; the first bench classmate takes the place. Returns the replacement or "". */
    String leave(String who, String reason, long day) {
        if (!teammates.remove(who)) return "";
        String replacement = bench.isEmpty() ? "" : bench.removeFirst();
        if (!replacement.isEmpty()) teammates.add(replacement);
        departed.put(who, new Departure(reason, day, replacement));
        attention.remove(who); jealousy.remove(who); lowDays.remove(who); overlooked.remove(who);
        return replacement;
    }
    /** Comes back; whoever replaced them steps back to the bench. */
    boolean rejoin(String who) {
        var d = departed.remove(who); if (d == null) return false;
        if (!d.replacedBy().isEmpty() && teammates.remove(d.replacedBy())) bench.addFirst(d.replacedBy());
        teammates.add(who);
        return true;
    }
}
