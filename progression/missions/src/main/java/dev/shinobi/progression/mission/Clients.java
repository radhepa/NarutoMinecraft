package dev.shinobi.progression.mission;

import java.util.ArrayList;
import java.util.List;
import java.util.Map;
import java.util.TreeMap;

import static dev.shinobi.progression.mission.Json.*;

/**
 * Client rapport (MISSIONS.md section 5): every client keeps a tally of the missions done for them. A grade adds
 * points ({@code economy.json}), a failure or abandonment takes them away. Tiers: stranger, known, regular, trusted,
 * patron. A regular or better whose missions averaged a good score may post a <b>request by name</b>: a board offer
 * for the player only, paying {@code requests.pay} more. A client whose rapport sinks below {@code soured_below}
 * stops posting to the player for two weeks. Rapport is separate from the bond engine's feelings, which the
 * turn-in moves too ({@code mission_success}, {@code failed_client}).
 */
public final class Clients {
    public static final class Rapport {
        double points;
        int jobs;
        double scoreSum;
        int scored;
        int lastDay = Integer.MIN_VALUE / 2;
        int souredUntil = Integer.MIN_VALUE / 2;
        public double points() { return points; }
        public int jobs() { return jobs; }
        public double averageScore() { return scored == 0 ? 0 : scoreSum / scored; }
    }

    final Map<String, Rapport> book = new TreeMap<>();
    final List<Object[]> tiers = new ArrayList<>();
    final double souredBelow;
    final Map<String, Object> requests;

    public Clients(Map<String, Object> clientsJson) {
        var rapport = map(clientsJson.get("rapport"));
        for (Object t : list(rapport.get("tiers"))) tiers.add(new Object[]{list(t).get(0), num(list(t).get(1), 0)});
        souredBelow = num(rapport.get("soured_below"), -2);
        requests = map(clientsJson.get("requests"));
    }

    public Rapport of(String client) { return book.computeIfAbsent(client, k -> new Rapport()); }
    public Map<String, Rapport> all() { return Map.copyOf(book); }

    public String tier(String client) {
        double pts = book.containsKey(client) ? book.get(client).points : 0;
        String tier = (String) tiers.getFirst()[0];
        for (Object[] t : tiers) if (pts >= (double) t[1]) tier = (String) t[0];
        return tier;
    }
    public int tierIndex(String tier) {
        for (int i = 0; i < tiers.size(); i++) if (tiers.get(i)[0].equals(tier)) return i;
        return 0;
    }
    public boolean atLeast(String client, String tier) { return tierIndex(tier(client)) >= tierIndex(tier); }
    public boolean soured(String client, int day) { return book.containsKey(client) && day < book.get(client).souredUntil; }

    /** Records a turn-in for the client. */
    public void record(String client, Economy.Result r, int day) {
        if (client == null) return;
        Rapport x = of(client);
        x.points += r.rapport();
        x.jobs++;
        x.lastDay = day;
        if (r.success()) { x.scoreSum += r.score(); x.scored++; }
        if (x.points < souredBelow) x.souredUntil = day + 14;
    }

    /** Clients who may ask for the player by name today, most rapport first. */
    public List<String> requesters(int day) {
        String min = str(requests.get("min_tier"), "regular");
        double minScore = num(requests.get("min_avg_score"), 70);
        return book.entrySet().stream()
                .filter(e -> atLeast(e.getKey(), min) && e.getValue().averageScore() >= minScore && !soured(e.getKey(), day))
                .sorted((a, b) -> Double.compare(b.getValue().points, a.getValue().points))
                .map(Map.Entry::getKey).toList();
    }
    public double requestChance() { return num(requests.get("chance_per_day"), 0.2); }
    public int requestLifetime() { return (int) num(requests.get("expires_days"), 4); }
    public int maxRequests() { return (int) num(requests.get("max_on_board"), 1); }
}
