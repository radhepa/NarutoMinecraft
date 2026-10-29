package dev.shinobi.combat;

/**
 * A bar that refills after a pause: stamina (taijutsu and weapons; full in about three seconds) and poise (the
 * hidden toughness bar; at 0 the fighter staggers and it refills). Ticks are Minecraft ticks, 20 a second.
 */
public final class Pool {
    private final double max, regenPerTick;
    private final int delay;
    private double value;
    private int sinceUse;

    public Pool(double max, double regenPerSecond, int delayTicks) {
        this.max = max;
        this.regenPerTick = regenPerSecond / 20;
        this.delay = delayTicks;
        this.value = max;
        this.sinceUse = delayTicks;
    }
    public static Pool stamina(double max) { return new Pool(max, 30, 15); }
    /** Poise regenerates 15% of its maximum a second, two seconds after the last hit. */
    public static Pool poise(double max) { return new Pool(max, max * 0.15, 40); }

    public double max() { return max; }
    public double value() { return value; }
    public boolean empty() { return value <= 0; }

    public void tick(double mult) {
        if (sinceUse < delay) { sinceUse++; return; }
        value = Math.min(max, value + regenPerTick * mult);
    }
    public boolean has(double amount) { return value >= amount; }
    /** Spends what it can; true when the full amount was there. */
    public boolean spend(double amount) {
        sinceUse = 0;
        boolean ok = value >= amount;
        value = Math.max(0, value - amount);
        return ok;
    }
    /** Poise damage: true when this hit broke it (a stagger); the bar then refills. */
    public boolean breaks(double amount) {
        sinceUse = 0;
        value -= amount;
        if (value > 0) return false;
        value = max;
        return true;
    }
    public void fill() { value = max; }
}
