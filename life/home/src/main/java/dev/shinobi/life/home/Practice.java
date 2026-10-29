package dev.shinobi.life.home;

/**
 * Short practice at home: the dummy, hand-sign drills, chakra-control meditation and study at the scroll shelf. It
 * counts at 40% of a training ground's rate, and at most one in-game hour a day counts (an hour and a half with the
 * whole training set), so it fills a quiet evening and never replaces the training grounds. A hand-sign drill counts
 * once a day toward mastering a jutsu. The glue pays credited hours as player XP at Progression's training-ground rate
 * ({@code ranks.json}); it is solo, so it is never shared with the squad.
 */
public final class Practice {
    public static final double RATE = .4, CAP_HOURS = 1, DOJO_CAP_HOURS = 1.5;

    /** What a session gave: training-ground-equivalent hours credited, hours over the day's cap, and a drill. */
    public record Session(double credited, double wasted, boolean drill) {}

    private long day = Long.MIN_VALUE;
    private double usedToday;
    private boolean drilledToday;
    private double total;

    /** {@code kind}: "dummy", "signs", "meditate" or "study"; each needs its piece (a dummy, a mat, a scroll shelf). */
    public Session session(Home home, Comfort.Score score, long today, String kind, double hours) {
        if (today != day) { day = today; usedToday = 0; drilledToday = false; }
        boolean can = switch (kind) {
            case "dummy" -> home.has("training_dummy");
            case "signs" -> true;
            case "meditate" -> home.has("meditation_mat");
            case "study" -> home.has("scroll_shelf") || home.has("low_desk");
            default -> false;
        };
        if (!can || hours <= 0) return new Session(0, hours, false);
        double cap = score.perk(FurnitureSet.DOJO) ? DOJO_CAP_HOURS : CAP_HOURS;
        double counted = Math.min(hours, Math.max(0, cap - usedToday));
        usedToday += counted;
        boolean drill = kind.equals("signs") && !drilledToday;
        if (drill) drilledToday = true;
        total += counted * RATE;
        return new Session(counted * RATE, hours - counted, drill);
    }
    public double total() { return total; }
}
