package dev.shinobi.life.bond;

/**
 * One thing a person remembers about you: what happened, when, what it did to their meters, how they know it, and
 * who it was about ({@code about} is empty when it happened to them). Small and notable memories fade by half every
 * {@link Act#halfLife} days and are let go below 1/16; big ones are kept for good. A repeat of a fading act within its
 * half-life folds into the same memory at half weight (secondhand news of the same kind folds whoever it was about),
 * and a folded memory never grows past {@link #SATURATION} times one act: routine keeps a memory fresh rather than
 * piling up, so the hundredth shared mission matters less than the first.
 */
public record Memory(Act act, long day, Meters delta, Reaction.Source source, String about, int count) {
    public static final double SATURATION = 2;
    public static final double FORGOTTEN = 1 / 16.0;

    public Memory { about = about == null ? "" : about; count = Math.max(1, count); }

    public boolean permanent() { return act.permanent(); }
    public double weight(long today) {
        if (permanent()) return 1;
        long age = Math.max(0, today - day);
        return Math.pow(.5, (double) age / act.halfLife);
    }
    public Meters now(long today) { return delta.times(weight(today)); }
    public boolean forgotten(long today) { return !permanent() && weight(today) < FORGOTTEN; }
    /** Whether a fresh memory of the same act folds into this one. */
    public boolean merges(Act next, Reaction.Source how, String who, long today) {
        boolean sameAbout = how != Reaction.Source.SELF || about.equals(who == null ? "" : who);
        return act == next && !permanent() && source == how && sameAbout && today - day <= act.halfLife;
    }
    /** The merged memory: the newer day and half of the new change, so repeats count, but less. */
    public Memory merged(Meters more, long today) { return merged(more, today, about); }
    public Memory merged(Meters more, long today, String who) {
        var sum = delta.times(weight(today)).plus(more.times(.5));
        var capped = Meters.ZERO;
        for (Meter m : Meter.values()) {
            double limit = SATURATION * Math.abs(more.get(m)), v = sum.get(m);
            capped = capped.with(m, Math.clamp(v, -limit, limit));
        }
        return new Memory(act, today, capped, source, who == null ? about : who, count + 1);
    }
}
