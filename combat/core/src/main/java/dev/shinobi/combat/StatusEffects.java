package dev.shinobi.combat;

import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.LinkedHashMap;
import java.util.List;
import java.util.Map;

/**
 * The statuses on one fighter (data/combat/core/status_effects.json): durations, stacks, damage over time, what
 * they stop (acting, moving, weaving), what they change (speed, damage taken), what cleanses what, and
 * diminishing returns: a second stun within 15 s lasts half as long, a third a quarter, a fourth not at all; the
 * same for binds, seals and mind effects. Bosses take half from the first and are immune after the second.
 */
public final class StatusEffects {
    public static final int DR_WINDOW = 300;
    static final double[] DR = {1.0, 0.5, 0.25, 0.0};
    static final double[] DR_BOSS = {0.5, 0.25, 0.0};

    /** One status as data. */
    public record Def(String id, int ticks, int stunTicks, double dotPerSecond, double slow, int maxStacks, String drGroup,
                      boolean interrupts, boolean noCast, boolean root, Map<String, Double> takenMult, List<String> cleanses,
                      String atMax, boolean breaksOnDamage) {
        public static Def of(String id, Map<String, Object> m) {
            var taken = new HashMap<String, Double>();
            for (var e : m.entrySet())
                if (e.getKey().endsWith("_taken_mult") && e.getValue() instanceof Number n)
                    taken.put(e.getKey().substring(0, e.getKey().length() - "_taken_mult".length()), n.doubleValue());
            int stun = Json.integer(m, "stun_ticks", 0);
            return new Def(id, Json.integer(m, "ticks", stun > 0 ? stun : 60), stun, Json.num(m, "dot", 0), Json.num(m, "slow", 0),
                    Json.integer(m, "stacks", 1), Json.str(m, "dr_group", null), Json.bool(m, "interrupts") || stun > 0,
                    Json.bool(m, "no_cast") || Json.bool(m, "no_signs"), Json.bool(m, "root"), taken, Json.strings(m, "cleanses"),
                    Json.str(m, "at_max", null), Json.bool(m, "breaks_on_damage"));
        }
        public boolean stuns() { return stunTicks > 0; }
    }
    public record Active(Def def, int remaining, int stacks) {}

    private final Map<String, Def> defs;
    private final boolean boss;
    private final Map<String, Active> active = new LinkedHashMap<>();
    private final Map<String, ArrayDeque<Long>> drHistory = new HashMap<>();

    public StatusEffects(Map<String, Def> defs, boolean boss) { this.defs = defs; this.boss = boss; }

    public static Map<String, Def> defs(Map<String, Object> statuses) {
        var out = new LinkedHashMap<String, Def>();
        for (var e : statuses.entrySet()) out.put(e.getKey(), Def.of(e.getKey(), Json.obj(e.getValue())));
        return out;
    }

    /**
     * Applies a status for {@code ticks} (0: its default) at tick {@code now}; returns the ticks actually applied
     * after diminishing returns (0: immune). Stacks add up to the maximum; at the maximum some turn into another
     * status (numbed into paralysed, drowsy into asleep). Applying a status cleanses those it cleanses.
     */
    public int apply(String id, int ticks, long now) {
        var d = defs.get(id);
        if (d == null) throw new IllegalArgumentException("unknown status " + id);
        int t = ticks > 0 ? ticks : d.ticks();
        if (d.drGroup() != null) t = (int) Math.round(t * drFactor(d.drGroup(), now));
        if (t <= 0) return 0;
        for (String c : d.cleanses()) active.remove(c);
        var cur = active.get(id);
        int stacks = cur == null ? 1 : Math.min(d.maxStacks(), cur.stacks() + 1);
        active.put(id, new Active(d, Math.max(t, cur == null ? 0 : cur.remaining()), stacks));
        if (d.atMax() != null && stacks >= d.maxStacks() && d.maxStacks() > 1) {
            active.remove(id);
            return apply(d.atMax(), 0, now);
        }
        return t;
    }
    private double drFactor(String group, long now) {
        var h = drHistory.computeIfAbsent(group, k -> new ArrayDeque<>());
        while (!h.isEmpty() && now - h.peekFirst() > DR_WINDOW) h.pollFirst();
        double[] table = boss ? DR_BOSS : DR;
        double f = table[Math.min(h.size(), table.length - 1)];
        if (f > 0) h.addLast(now);
        return f;
    }

    public boolean has(String id) { return active.containsKey(id); }
    public int stacks(String id) { var a = active.get(id); return a == null ? 0 : a.stacks(); }
    public int remaining(String id) { var a = active.get(id); return a == null ? 0 : a.remaining(); }
    public void remove(String id) { active.remove(id); }
    public List<String> ids() { return new ArrayList<>(active.keySet()); }

    /** Advances one tick; returns the damage over time dealt this tick (per stack). */
    public double tick() {
        double dot = 0;
        var it = active.entrySet().iterator();
        while (it.hasNext()) {
            var e = it.next();
            var a = e.getValue();
            dot += a.def().dotPerSecond() / 20 * a.stacks();
            if (a.remaining() <= 1) it.remove();
            else e.setValue(new Active(a.def(), a.remaining() - 1, a.stacks()));
        }
        return dot;
    }
    /** Damage taken ends statuses that break on damage (sleep). */
    public void damaged() { active.values().removeIf(a -> a.def().breaksOnDamage()); }

    public boolean stunned() { for (var a : active.values()) if (a.def().stuns()) return true; return false; }
    public boolean rooted() { for (var a : active.values()) if (a.def().root() || a.def().stuns()) return true; return false; }
    public boolean canCast() { for (var a : active.values()) if (a.def().noCast() || a.def().stuns()) return false; return true; }
    /** The strongest slow (they do not stack with each other). */
    public double slow() { double s = 0; for (var a : active.values()) s = Math.max(s, a.def().slow()); return s; }
    /** How much more (or less) a damage type hurts with these statuses: soaked, hardened... by type prefix. */
    public double takenMult(String damageType) {
        double m = 1;
        for (var a : active.values())
            for (var e : a.def().takenMult().entrySet())
                if (damageType.endsWith(e.getKey()) || damageType.startsWith(e.getKey())) m *= e.getValue();
        return m;
    }
}
