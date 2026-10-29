package dev.shinobi.life.bond;

/**
 * Ten bond levels on VF's thresholds (5, 15, 28, 40, 58, 80, 105, 140, 170, 200), read from <em>closeness</em>, one
 * number made of the meters:
 *
 * <pre>regard    = min(100, max(respect, romance) + 0.2 min(rivalry, respect))
 * feeling   = 0.45 affection + 0.35 trust + 0.2 regard                       (-45..100)</pre>
 *
 * so a friend you like and trust, a sensei who respects you, a sweetheart, and a rival who respects you as much as
 * they want to beat you can all grow close. Levels open at feeling 5, 12, 20, 28, 36, 45, 55, 66, 80 and 95: each
 * step wider than the last, so level 10 wants every part near the top. <em>Closeness</em> is the same reading on
 * VF's 0..200 points scale (straight lines between the thresholds), so VF's ledger and goals keep working. Points alone stop at the story gates ({@link #cap}): a shared experience to pass 3,
 * a real moment (a bond quest, a life saved, a secret kept) to pass 5, and more moments and more days in each
 * other's company to pass 7, 8 and 9.
 *
 * <p>Levels rise as soon as they are earned (right after the act that earned them) and fall slowly: only when closeness drops {@link #SLACK} below the
 * level's threshold, and one level a day. A quarrel lowers the level people actually act on ({@link Conflict#cap}).
 */
public final class Levels {
    public static final int MAX = 10, SLACK = 10;
    private static final int[] THRESHOLDS = {0, 5, 15, 28, 40, 58, 80, 105, 140, 170, 200};
    /** Feeling at which each level opens. */
    private static final double[] FEELING = {0, 5, 12, 20, 28, 36, 45, 55, 66, 80, 95};
    private static final String[] NAMES = {"New Face", "Familiar Face", "Acquaintance", "Friendly", "Friend", "Good Friend",
            "Close Friend", "Trusted Friend", "Best Friend", "Kindred Spirit", "Lifelong Bond"};
    /** What each level opens; text keys {@code bond.perk.<n>} carry the words. */
    private static final String[] PERKS = {"", "They remember you between visits.", "Their favorite things; their first bond quest.",
            "Village news; they spar with you.", "A friend: they expect you on their birthday.", "Heart-to-heart talks; their values.",
            "Their dream; Kindling Bond can borrow their nature.", "They trust you with secrets; they would join your clan; dating (teen and up).",
            "Kindling Bond can borrow a technique; a confession (teen and up).", "A small gift saved for you each day.",
            "A bond for life: Kindling at full strength; marriage (adults)."};
    /** Levels at which features open (quests and dialogue use the numbers, not these names). */
    public static final int FIRST_BOND_QUEST = 2, NEWS = 3, FRIEND = 4, HEART_TO_HEART = 5, KINDLE_NATURE = 6, RECRUIT = 7, DATING = 7,
            KINDLE_TECHNIQUE = 8, CONFESS = 8, DAILY_GIFT = 9, KINDLE_FULL = 10, MARRY = 10;
    /** Gate requirements: contact days to pass levels 7, 8 and 9. */
    public static final int DAYS_PAST_7 = 15, DAYS_PAST_8 = 35, DAYS_PAST_9 = 60;

    public static double closeness(Meters m) {
        var c = m.clamped();
        double f = feeling(m);
        if (f <= 0) return 0;
        for (int i = 1; i <= MAX; i++)
            if (f < FEELING[i]) return THRESHOLDS[i - 1] + (THRESHOLDS[i] - THRESHOLDS[i - 1]) * (f - FEELING[i - 1]) / (FEELING[i] - FEELING[i - 1]);
        return 200;
    }
    public static double feelingFor(int level) { return FEELING[Math.clamp(level, 0, MAX)]; }
    /** The meters folded into one feeling, from -45 to 100. */
    public static double feeling(Meters m) {
        var c = m.clamped();
        double regard = Math.min(100, Math.max(c.respect(), c.romance()) + .2 * Math.min(c.rivalry(), c.respect()));
        return .45 * c.affection() + .35 * c.trust() + .2 * regard;
    }
    public static int byPoints(double points) {
        int level = 0;
        while (level < MAX && points >= THRESHOLDS[level + 1]) level++;
        return level;
    }
    public static int threshold(int level) { return THRESHOLDS[Math.clamp(level, 0, MAX)]; }
    public static String name(int level) { return NAMES[Math.clamp(level, 0, MAX)]; }
    public static String perk(int level) { return PERKS[Math.clamp(level, 0, MAX)]; }

    /** Which gate holds a bond back, or "" when none does. */
    public static String gate(int experiences, int moments, int contactDays, int level) {
        if (level >= MAX) return "";
        int cap = cap(experiences, moments, contactDays);
        if (level < cap) return "";
        if (experiences == 0) return "experience";
        if (moments == 0) return "moment";
        if (moments < 2 || contactDays < DAYS_PAST_7) return moments < 2 ? "moment" : "time";
        if (moments < 3 || contactDays < DAYS_PAST_8) return moments < 3 ? "moment" : "time";
        return moments < 4 ? "moment" : "time";
    }
    /** The highest level shared history allows. */
    public static int cap(int experiences, int moments, int contactDays) {
        if (experiences == 0) return 3;
        if (moments == 0) return 5;
        if (moments < 2 || contactDays < DAYS_PAST_7) return 7;
        if (moments < 3 || contactDays < DAYS_PAST_8) return 8;
        if (moments < 4 || contactDays < DAYS_PAST_9) return 9;
        return MAX;
    }
    /** Tomorrow's level from today's, with the gate and the slack for falling. */
    public static int next(int level, double closeness, int cap) {
        int target = Math.min(byPoints(closeness), cap);
        if (target > level) return target;
        if (level > cap) return level - 1;
        if (target < level && closeness < threshold(level) - SLACK) return level - 1;
        return level;
    }

    private Levels() {}
}
