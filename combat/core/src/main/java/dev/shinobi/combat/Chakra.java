package dev.shinobi.combat;

/**
 * The chakra bar: maximum from level and clan, slow regeneration (faster meditating, slower in a fight), costs
 * shaped by chakra control, your own nature and mastery, and the desperate cast that pays a shortfall in health
 * and leaves you exhausted until a fifth of the bar is back.
 */
public final class Chakra {
    public static final double REGEN_FLAT = 0.6, REGEN_FRACTION = 0.01;
    public static final double COMBAT_MULT = 0.75, MEDITATE_MULT = 4.0;
    public static final double OVERDRAW_LIMIT = 0.25, OVERDRAW_HP_PER_POINT = 0.5;
    public static final double EXHAUSTED_UNTIL = 0.2;

    private final double max;
    private double value;
    private boolean exhausted;

    public Chakra(double max) { this.max = max; this.value = max; }

    public double max() { return max; }
    public double value() { return value; }
    public double fraction() { return value / max; }
    public boolean exhausted() { return exhausted; }

    /** One tick of regeneration; {@code mult} carries combat, meditation, fatigue and food. */
    public void tick(double mult) {
        value = Math.min(max, value + (REGEN_FLAT + REGEN_FRACTION * max) / 20 * mult);
        if (exhausted && value >= EXHAUSTED_UNTIL * max) exhausted = false;
    }
    public void restore(double amount) { value = Math.min(max, value + amount); }
    public double drain(double amount) {
        double d = Math.min(value, amount);
        value -= d;
        if (value <= 0) exhausted = true;
        return d;
    }

    /**
     * A technique's real cost. Control runs from x1.15 at 0 to x0.85 at 100; your own nature costs x0.75 (ROADMAP
     * Elemental natures); {@code mult} carries mastery, clan and pillar rebates.
     */
    public static double cost(double base, int control, boolean ownNature, double mult) {
        double c = base * (1.15 - 0.003 * Math.clamp(control, 0, 100)) * mult;
        return ownNature ? c * Nature.OWN_COST : c;
    }

    /** What a cast cost: the chakra paid and any health the shortfall took. */
    public record Spend(boolean ok, double chakra, double health) {}

    public Spend spend(double cost, boolean desperate) {
        if (exhausted) return new Spend(false, 0, 0);
        if (value >= cost) { value -= cost; if (value <= 0) exhausted = true; return new Spend(true, cost, 0); }
        double short_ = cost - value;
        if (!desperate || short_ > OVERDRAW_LIMIT * cost) return new Spend(false, 0, 0);
        double paid = value;
        value = 0;
        exhausted = true;
        return new Spend(true, paid, short_ * OVERDRAW_HP_PER_POINT);
    }
}
