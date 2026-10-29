package dev.shinobi.life.bond;

import java.util.Locale;

/**
 * A falling-out with an arc. A quarrel (an act marked {@link Act#quarrel}, or any personal act that costs them
 * {@link #TRIGGER} or more at once) starts an <b>argument</b>; the next day they give you the <b>cold shoulder</b>
 * for a few days, longer for the proud and shorter for the warm; then they are ready to <b>make up</b>, and a
 * reconciliation quest ({@code bond_state: making_up}) can end it, which leaves a permanent {@link Act#RECONCILED}
 * memory: a mended bond is stronger. Left alone for {@link #DRIFT_DAYS}, a mild quarrel blows over and a bad one
 * hardens into a <b>falling-out</b>. A falling-out is permanent: the level they act on stays at {@link #FALLEN_CAP}
 * or below, Kindling Bond and romance close, and only the story can mend it ({@code mend} effect).
 *
 * <p>An apology during the argument or the cold shoulder is accepted when they trust you (40 or more) or three
 * days have passed, and halves the cold shoulder.
 */
public record Conflict(State state, long since, long until, double severity, Act cause, int strikes) {
    public enum State {
        NONE, ARGUMENT, COLD_SHOULDER, MAKING_UP, FALLING_OUT;
        public String id() { return name().toLowerCase(Locale.ROOT); }
        public static State of(String id) { return valueOf(id.toUpperCase(Locale.ROOT)); }
    }
    public static final Conflict NONE = new Conflict(State.NONE, -1, -1, 0, null, 0);
    public static final double TRIGGER = 14, HARDENS = 30, BREAKS = 60;
    public static final int DRIFT_DAYS = 28, FALLEN_CAP = 2, APOLOGY_TRUST = 40, APOLOGY_DAYS = 3;

    public Conflict { severity = Math.clamp(severity, 0, 100); strikes = Math.max(0, strikes); }

    public boolean active() { return state != State.NONE && state != State.FALLING_OUT; }
    public boolean broken() { return state == State.FALLING_OUT; }

    /** How bad a hurt is: the affection and trust it cost, more for the proud. */
    public static double severity(Meters delta, Personality p) {
        return -(Math.min(0, delta.affection()) + Math.min(0, delta.trust())) * (1 + .3 * Math.max(0, p.pride()));
    }
    /** Whether this hurt starts (or deepens) a quarrel. */
    public static boolean triggers(Act act, Meters delta, Personality p) { return act.quarrel || !act.professional && severity(delta, p) >= TRIGGER; }

    /** Days of cold shoulder after an argument of this severity. */
    public static int coldDays(double severity, Personality p) {
        return (int) Math.clamp(Math.round((2 + severity / 8) * (1 + .5 * p.pride()) * (1 - .3 * p.warmth())), 1, 14);
    }

    /**
     * A new hurt. A first one starts an argument; one during a quarrel deepens it, and a third strike, or a hurt of
     * {@link #BREAKS} severity, ends in a falling-out.
     */
    public Conflict hurt(Act act, double sev, Personality p, long day) {
        if (broken()) return this;
        int nextStrikes = active() ? strikes + 1 : 1;
        double total = active() ? Math.min(100, severity + sev) : sev;
        if (sev >= BREAKS || nextStrikes >= 3 || active() && total >= BREAKS) return new Conflict(State.FALLING_OUT, day, -1, total, act, nextStrikes);
        return new Conflict(State.ARGUMENT, day, day + 1 + coldDays(total, p), total, act, nextStrikes);
    }
    /** End of a day. */
    public Conflict tick(long day) {
        return switch (state) {
            case ARGUMENT -> new Conflict(State.COLD_SHOULDER, since, until, severity, cause, strikes);
            case COLD_SHOULDER -> day >= until ? new Conflict(State.MAKING_UP, since, day, severity, cause, strikes) : this;
            case MAKING_UP -> day - until >= DRIFT_DAYS ? (severity >= HARDENS ? new Conflict(State.FALLING_OUT, day, -1, severity, cause, strikes) : NONE) : this;
            default -> this;
        };
    }
    public boolean apologyAccepted(double trust, long day) {
        return (state == State.ARGUMENT || state == State.COLD_SHOULDER) && (trust >= APOLOGY_TRUST || day - since >= APOLOGY_DAYS);
    }
    public Conflict apologized(long day) {
        if (state != State.ARGUMENT && state != State.COLD_SHOULDER) return this;
        long shorter = Math.max(day + 1, since + (until - since) / 2);
        return new Conflict(State.COLD_SHOULDER, since, Math.min(until, shorter), severity * .75, cause, strikes);
    }
    /** Whether a reconciliation can happen now: they are ready to make up. */
    public boolean canReconcile() { return state == State.MAKING_UP; }

    /** The level they act on while this lasts. */
    public int cap(int level) {
        return switch (state) {
            case ARGUMENT -> Math.max(0, level - 1);
            case COLD_SHOULDER -> Math.max(0, level - 2);
            case MAKING_UP -> Math.max(0, level - 1);
            case FALLING_OUT -> Math.min(level, FALLEN_CAP);
            case NONE -> level;
        };
    }
    /** What the quarrel costs on top of the memories: a sore spot that eases as it heals; a scar if it never did. */
    public Meters weight() {
        return switch (state) {
            case ARGUMENT, COLD_SHOULDER -> Meters.of(-severity * .5, -severity * .2, 0, 0);
            case MAKING_UP -> Meters.of(-severity * .25, -severity * .1, 0, 0);
            case FALLING_OUT -> Meters.of(-30, -30, 0, 0);
            case NONE -> Meters.ZERO;
        };
    }
    /** How much of a talk or a gift gets through: nothing during the cold shoulder. */
    public double warmthLet() {
        return switch (state) { case ARGUMENT, MAKING_UP -> .5; case COLD_SHOULDER, FALLING_OUT -> 0; case NONE -> 1; };
    }
}
