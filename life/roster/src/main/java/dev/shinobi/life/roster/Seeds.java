package dev.shinobi.life.roster;

/**
 * The save seed's streams, as ROADMAP.md defines them: {@code stream(domain, key) = SplitMix64(hash64(saveSeed,
 * domain, key))}. The same numbers as the bond engine's {@code Seeds} and, after Phase 0, Shinobi Core's
 * {@code SaveSeed}; this copy keeps the roster engine standalone. Every roll goes through here.
 */
public final class Seeds {
    static long mix(long z) {
        z = (z ^ (z >>> 30)) * 0xbf58476d1ce4e5b9L;
        z = (z ^ (z >>> 27)) * 0x94d049bb133111ebL;
        return z ^ (z >>> 31);
    }
    /** FNV-1a over the characters, then mixed. */
    public static long hash(String s) {
        long h = 0xcbf29ce484222325L;
        for (int i = 0; i < s.length(); i++) { h ^= s.charAt(i); h *= 0x100000001b3L; }
        return mix(h);
    }
    public static long hash64(long seed, String domain, String key) {
        return mix(seed ^ hash(domain) * 0x9E3779B97F4A7C15L ^ Long.rotateLeft(hash(key), 21));
    }
    public static Rng stream(long seed, String domain, String key) { return new Rng(hash64(seed, domain, key)); }

    /** A SplitMix64 stream. */
    public static final class Rng {
        private long state;
        public Rng(long state) { this.state = state; }
        public long next() { state += 0x9E3779B97F4A7C15L; return mix(state); }
        public double unit() { return (next() >>> 11) * 0x1.0p-53; }
        public double range(double lo, double hi) { return lo + (hi - lo) * unit(); }
        public int below(int bound) { return (int) Math.floorMod(next(), (long) bound); }
        public boolean chance(double p) { return unit() < p; }
    }

    private Seeds() {}
}
