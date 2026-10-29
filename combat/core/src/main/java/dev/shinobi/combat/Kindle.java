package dev.shinobi.combat;

import java.util.ArrayList;
import java.util.LinkedHashMap;
import java.util.List;
import java.util.Map;

/**
 * Kindling Bond in combat (docs/COMBAT.md, "Kindling Bond"): power flows outward, through the people you are bonded
 * with. Thread Sight reads your allies; Kindle pushes your chakra into a bonded ally so their own technique goes past
 * its limits; Ember Link binds the squad into one flame (a shared chakra pool, damage spread across it); unison
 * techniques belong to each pairing; Bonfire draws on every bond at once and scales with the whole bond web.
 * The bond engine (Shinobi Life) owns bond levels, tiers and gates; combat reads them through {@link Bonds}.
 */
public final class Kindle {
    /** A bond's tier, as Shinobi Life gates it: Spark at friendship 6, Flame at 8, Blaze at 10 or a spouse. */
    public enum Tier { NONE, SPARK, FLAME, BLAZE }

    /** What combat reads from the bond engine. The bonds session implements it; a quarrel dims a tier, a falling-out puts it out. */
    public interface Bonds {
        Tier tier(String who);
        /** The bond web's score (BondWeb), which sizes Bonfire. */
        double web();
        /** Whether the story and the bond engine have opened Bonfire. */
        boolean bonfireOpen();
    }

    /** What one kindle does to an ally's technique: power, area, range and healing multipliers, and whether a heal revives. */
    public record Boost(double power, double area, double range, double heal, boolean revives) {
        public static final Boost NONE = new Boost(1, 1, 1, 1, false);
    }

    public static Boost boost(Tier t) {
        return switch (t) {
            case NONE -> Boost.NONE;
            case SPARK -> new Boost(1.4, 1.2, 1.5, 1.5, false);
            case FLAME -> new Boost(1.9, 1.4, 2.5, 2.0, true);
            case BLAZE -> new Boost(2.4, 1.6, 4.0, 2.5, true);
        };
    }
    /** Your chakra a kindle takes, as a share of the ally's technique cost: bigger flames cost more. */
    public static double cost(double allyTechniqueCost, Tier t) {
        return allyTechniqueCost * switch (t) { case NONE -> 0; case SPARK -> 0.6; case FLAME -> 0.8; case BLAZE -> 1.0; };
    }
    /** Ticks before the same ally can be kindled again. */
    public static int cooldown(Tier t) {
        return switch (t) { case NONE -> Integer.MAX_VALUE; case SPARK -> 400; case FLAME -> 300; case BLAZE -> 200; };
    }

    /** Overuse: past three kindles in a minute, each one burns a tenth of your chakra bar and 30 stamina more. */
    public static final int FREE_PER_MINUTE = 3;
    public record Burn(double chakra, double stamina) {}
    public static Burn overuse(int kindlesInLastMinute, double maxChakra) {
        int over = Math.max(0, kindlesInLastMinute - FREE_PER_MINUTE + 1);
        return new Burn(over * 0.1 * maxChakra, over * 30);
    }

    /**
     * Ember Link (Flame): you and up to three bonded allies share one chakra pool, and a hit on any of you is spread:
     * the one struck keeps half, the rest is split across the others. While linked you feel your allies' pain.
     */
    public static final class EmberLink {
        public static final int MAX_ALLIES = 3, TICKS = 600;
        public static final double KEEP = 0.5;
        private final Map<String, Double> pool = new LinkedHashMap<>();

        public EmberLink(Map<String, Double> chakra) {
            if (chakra.size() > MAX_ALLIES + 1) throw new IllegalArgumentException("a link holds you and three allies");
            pool.putAll(chakra);
        }
        public List<String> members() { return new ArrayList<>(pool.keySet()); }
        public double shared() { return pool.values().stream().mapToDouble(Double::doubleValue).sum(); }

        /** Draws a cost from the pool, from the caster first and then evenly from the rest; false if the pool cannot pay. */
        public boolean draw(String caster, double cost) {
            if (shared() < cost) return false;
            double own = Math.min(pool.get(caster), cost);
            pool.merge(caster, -own, Double::sum);
            double rest = cost - own;
            while (rest > 1e-9) {
                var others = pool.entrySet().stream().filter(e -> e.getValue() > 1e-9).toList();
                if (others.isEmpty()) break;
                double share = rest / others.size();
                for (var e : others) { double d = Math.min(e.getValue(), share); e.setValue(e.getValue() - d); rest -= d; }
            }
            return true;
        }
        public double chakra(String who) { return pool.get(who); }

        /** How a hit of {@code damage} on {@code struck} lands across the link. */
        public Map<String, Double> spread(String struck, double damage) {
            var out = new LinkedHashMap<String, Double>();
            int others = pool.size() - 1;
            out.put(struck, others == 0 ? damage : damage * KEEP);
            for (String m : pool.keySet()) if (!m.equals(struck)) out.put(m, damage * (1 - KEEP) / others);
            return out;
        }
    }

    /**
     * Bonfire, the ultimate: a form fed by every bond. Its strength follows the bond web's score with diminishing
     * returns, so a player who befriended half the village burns like a beacon and a loner gets a candle.
     */
    public record Form(double damage, double taken, double regen, double allyPower, int ticks) {}
    public static final int BONFIRE_TICKS = 400, BONFIRE_BURNOUT = 1200;

    public static Form bonfire(double web) {
        double m = 1 + 1.5 * (1 - Math.exp(-Math.max(0, web) / 35));
        return new Form(m, 1 / Math.sqrt(m), 1 + Math.max(0, web) / 25, 1 + 0.5 * (m - 1), BONFIRE_TICKS);
    }

    /** Thread Sight in a fight: a bonded ally's danger shows on their thread this many ticks earlier, so you can cover them. Strangers show nothing. */
    public static int threadWarning(Tier t) {
        return switch (t) { case NONE -> 0; case SPARK -> 4; case FLAME -> 6; case BLAZE -> 8; };
    }

    private Kindle() {}
}
