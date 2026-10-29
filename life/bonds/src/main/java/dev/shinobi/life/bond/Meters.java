package dev.shinobi.life.bond;

/** A value (or a change) for each {@link Meter}. Unclamped: {@link #clamped()} bounds a final reading. */
public record Meters(double affection, double trust, double respect, double rivalry, double romance) {
    public static final Meters ZERO = new Meters(0, 0, 0, 0, 0);

    public static Meters of(double affection, double trust, double respect, double rivalry) {
        return new Meters(affection, trust, respect, rivalry, 0);
    }
    public double get(Meter m) {
        return switch (m) {
            case AFFECTION -> affection; case TRUST -> trust; case RESPECT -> respect; case RIVALRY -> rivalry; case ROMANCE -> romance;
        };
    }
    public Meters with(Meter m, double v) {
        return new Meters(m == Meter.AFFECTION ? v : affection, m == Meter.TRUST ? v : trust, m == Meter.RESPECT ? v : respect,
                m == Meter.RIVALRY ? v : rivalry, m == Meter.ROMANCE ? v : romance);
    }
    public Meters plus(Meter m, double v) { return with(m, get(m) + v); }
    public Meters plus(Meters o) {
        return new Meters(affection + o.affection, trust + o.trust, respect + o.respect, rivalry + o.rivalry, romance + o.romance);
    }
    public Meters times(double k) { return new Meters(affection * k, trust * k, respect * k, rivalry * k, romance * k); }
    /** Scales the gains (positive parts) by {@code k}, leaving losses alone. */
    public Meters gains(double k) { return map(v -> v > 0 ? v * k : v); }
    /** Scales the losses (negative parts) by {@code k}, leaving gains alone. */
    public Meters losses(double k) { return map(v -> v < 0 ? v * k : v); }
    public double sumOfLosses() { double s = 0; for (Meter m : Meter.values()) s += Math.min(0, get(m)); return s; }
    public double sumOfGains() { double s = 0; for (Meter m : Meter.values()) s += Math.max(0, get(m)); return s; }
    public Meters clamped() { return map2((m, v) -> Math.clamp(v, m.min, Meter.MAX)); }
    public boolean isZero() { for (Meter m : Meter.values()) if (Math.abs(get(m)) > 1e-9) return false; return true; }

    private Meters map(java.util.function.DoubleUnaryOperator f) { return map2((m, v) -> f.applyAsDouble(v)); }
    private Meters map2(java.util.function.ToDoubleBiFunction<Meter, Double> f) {
        return new Meters(f.applyAsDouble(Meter.AFFECTION, affection), f.applyAsDouble(Meter.TRUST, trust),
                f.applyAsDouble(Meter.RESPECT, respect), f.applyAsDouble(Meter.RIVALRY, rivalry), f.applyAsDouble(Meter.ROMANCE, romance));
    }
}
