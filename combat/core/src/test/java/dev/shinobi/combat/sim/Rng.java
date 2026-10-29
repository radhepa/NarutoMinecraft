package dev.shinobi.combat.sim;

/** A SplitMix64 stream (the save seed's stream generator, ROADMAP "One seed, many streams"). */
final class Rng {
    private long state;

    Rng(long seed) { this.state = seed; }

    long next() {
        long z = (state += 0x9E3779B97F4A7C15L);
        z = (z ^ (z >>> 30)) * 0xbf58476d1ce4e5b9L;
        z = (z ^ (z >>> 27)) * 0x94d049bb133111ebL;
        return z ^ (z >>> 31);
    }
    double unit() { return (next() >>> 11) * 0x1.0p-53; }
    boolean chance(double p) { return unit() < p; }
    double range(double lo, double hi) { return lo + (hi - lo) * unit(); }
}
