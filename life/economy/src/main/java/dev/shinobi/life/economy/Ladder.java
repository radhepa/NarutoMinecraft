package dev.shinobi.life.economy;

import java.util.List;

/** The ranks and slices that gate stock and recipes, in order (ROADMAP §5 ranks, §9 slices). */
public final class Ladder {
    public static final List<String> RANKS = List.of("any", "academy", "genin", "chunin", "jonin", "anbu", "kage");
    public static final List<String> SLICES = List.of("beta1", "beta2", "beta2_5", "beta3", "later");

    /** Whether a player of {@code rank} may buy or craft something of {@code needed}. ANBU sits beside Jonin. */
    public static boolean rankAllows(String rank, String needed) {
        if (needed == null || needed.isEmpty() || needed.equals("any")) return true;
        int have = rank(rank), need = rank(needed);
        if (needed.equals("anbu")) return rank.equals("anbu") || rank.equals("kage");
        if (rank.equals("anbu")) return need <= rank("jonin");
        return have >= need;
    }
    public static int rank(String rank) { return Math.max(0, RANKS.indexOf(rank)); }
    /** Whether content of {@code needed} has shipped by {@code slice}. */
    public static boolean sliceAllows(String slice, String needed) {
        if (needed == null || needed.isEmpty()) return true;
        return slice(needed) <= slice(slice);
    }
    public static int slice(String slice) {
        int i = SLICES.indexOf(slice);
        return i < 0 ? SLICES.size() : i;
    }

    private Ladder() {}
}
