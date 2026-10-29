package dev.shinobi.life.bond;

import dev.shinobi.life.bond.Personality.Value;

/**
 * How an act lands on one particular person. Starting from the act's {@link Act#base}:
 * <ol>
 * <li>each lean adds {@code amount x trait} (a bold person respects a reckless charge, a cautious one trusts you less);</li>
 * <li>honoring one of their values multiplies the gains by 1.5 and adds 0.5 affection;</li>
 * <li>violating one multiplies the losses by 1.5 and costs 1 more trust;</li>
 * <li>touching a pet peeve multiplies the losses by 1.4 and costs 2 more affection;</li>
 * <li>warm people soften the blow to affection by up to a quarter, proud people feel it more.</li>
 * </ol>
 * Secondhand news ({@link #secondhand}) lands at a fraction, depending on how they came to know it.
 */
public final class Reaction {
    public static final double HONOR = 1.5, VIOLATE = 1.5, PEEVE = 1.4;

    /** How someone knows of an act: it happened to them, they saw it, someone told them, or you told them yourself. */
    public enum Source {
        SELF(1), SEEN(.6), HEARD(.3), TOLD(.45);
        public final double weight;
        Source(double weight) { this.weight = weight; }
    }

    public static Meters react(Personality p, Act act) { return react(p, act.base, act.leans, act.honors, act.violates, act.peeve); }
    /** The same rules for anything with an effect, leans, values and a peeve (an act, an answer's tag). */
    public static Meters react(Personality p, Meters base, java.util.List<Act.Lean> leans, java.util.Set<Value> honors, java.util.Set<Value> violates,
            Personality.Peeve peeve) {
        Meters d = base;
        for (var lean : leans) d = d.plus(lean.meter(), lean.amount() * p.trait(lean.trait()));
        if (honors.stream().anyMatch(p::holds)) d = d.gains(HONOR).plus(Meter.AFFECTION, .5);
        if (violates.stream().anyMatch(p::holds)) d = d.losses(VIOLATE).plus(Meter.TRUST, -1);
        if (peeve != null && p.minds(peeve)) d = d.losses(PEEVE).plus(Meter.AFFECTION, -2);
        if (d.affection() < 0) d = d.with(Meter.AFFECTION, d.affection() * (1 - .25 * p.warmth() + .15 * Math.max(0, p.pride())));
        return d;
    }
    public static boolean honors(Personality p, Act act) { for (Value v : act.honors) if (p.holds(v)) return true; return false; }
    public static boolean violates(Personality p, Act act) { for (Value v : act.violates) if (p.holds(v)) return true; return false; }

    /**
     * What hearing of an act done to someone else does to how this person feels about you. {@code closeToThem}
     * (0 to 1) is how much they care about whoever it happened to: hearing that you saved their sister counts more
     * than hearing you saved a stranger. Romance never travels secondhand.
     */
    public static Meters secondhand(Personality p, Act act, Source how, double closeToThem) {
        return react(p, act).with(Meter.ROMANCE, 0).times(how.weight * (.6 + .8 * Math.clamp(closeToThem, 0, 1)));
    }

    private Reaction() {}
}
