package dev.shinobi.combat;

import java.util.ArrayList;
import java.util.List;
import java.util.Map;

/**
 * A taijutsu or weapon style: its combo tree as moves keyed by input path. Every style builds on Academy taijutsu
 * ({@link #over}): where the style has a move the fighter qualifies for, it wins; otherwise the Academy move on that
 * path still plays, so a sword style keeps its kick and a Strong Fist student without a gate keeps the air spike.
 */
public final class Style {
    private final String id, pillar;
    private final List<Move> moves, fallback;

    public Style(String id, String pillar, List<Move> moves) { this(id, pillar, moves, List.of()); }
    private Style(String id, String pillar, List<Move> moves, List<Move> fallback) {
        this.id = id;
        this.pillar = pillar;
        this.moves = List.copyOf(moves);
        this.fallback = List.copyOf(fallback);
    }

    public static Style of(Map<String, Object> s) {
        var moves = new ArrayList<Move>();
        for (Object m : Json.list(s, "moves")) moves.add(Move.of(Json.obj(m)));
        return new Style(Json.str(s, "id", "?"), Json.str(s, "pillar", "taijutsu"), moves);
    }

    public String id() { return id; }
    public String pillar() { return pillar; }
    public List<Move> moves() { return moves; }

    /** This style laid over a base: the style's moves first, the base's behind them. */
    public Style over(Style base) {
        var under = new ArrayList<>(base.moves);
        under.addAll(base.fallback);
        return new Style(id, pillar, moves, under);
    }

    /**
     * The move an input path reaches for a fighter of this tier with this momentum and these gates open: the
     * highest-tier move on that path it qualifies for, or null.
     */
    public Move find(List<String> path, int tier, double momentum, int gates) {
        var m = best(moves, path, tier, momentum, gates);
        return m != null ? m : best(fallback, path, tier, momentum, gates);
    }
    private static Move best(List<Move> from, List<String> path, int tier, double momentum, int gates) {
        Move best = null;
        for (var m : from) {
            if (!m.input().equals(path) || m.tier() > tier || m.momentumCost() > momentum || m.requiresGate() > gates) continue;
            if (best == null || m.tier() > best.tier()) best = m;
        }
        return best;
    }
    /** Every move the style can reach, its own and the base's. */
    public List<Move> all() {
        var out = new ArrayList<>(moves);
        out.addAll(fallback);
        return out;
    }

    /**
     * Every string a fighter can do from a prefix ("" on the ground, "J" in the air, "X" off a dash...), each
     * ending wherever the fighter stops pressing: for planning (the AI and the simulator).
     */
    public List<List<Move>> strings(String prefix, int tier, double momentum, int gates) {
        var out = new ArrayList<List<Move>>();
        walk(prefix.isEmpty() ? new ArrayList<>() : new ArrayList<>(List.of(prefix)), new ArrayList<>(), tier, momentum, gates, out);
        return out;
    }
    private void walk(List<String> path, List<Move> sofar, int tier, double momentum, int gates, List<List<Move>> out) {
        for (String in : List.of("L", "H", "T")) {
            var next = new ArrayList<>(path);
            next.add(in);
            var m = find(next, tier, momentum, gates);
            if (m == null) continue;
            var chain = new ArrayList<>(sofar);
            chain.add(m);
            out.add(chain);
            if (!m.ender() && next.size() < 6) walk(next, chain, tier, momentum - m.momentumCost(), gates, out);
        }
    }
}
