package dev.shinobi.life.bond;

import java.util.Locale;

/**
 * Romance between the player and a resident: a foundation only, nothing of it plays in the beta. Never with or
 * between children: the romance meter and every stage stay at zero until both are teens, and only within the same
 * age stage (teen with teen, adult with adult). The resident must be romantic, drawn to the player's gender, not
 * family, and not fallen out with you.
 *
 * <pre>romance = spark x (1 - e^(-days since both were teens / 30)) + romantic memories + 0.4 max(0, affection - 40)</pre>
 *
 * {@code spark} (0 to 30) is the pair's own, from the save seed and their chemistry. Stages: interest (romance 15,
 * hidden), a crush (romance 30 and level 6, hidden until level 8 or they confess), then the player's moves: asking
 * them out at level 7 and romance 35 (dating), confessing at level 8 and romance 50 (sweethearts, village news), proposing at level 10
 * and romance 65 between adults after 14 days as sweethearts (engaged), the wedding (married). Then children, in the post-game
 * ({@link Household}).
 */
public final class Courtship {
    public enum Stage {
        NONE, INTEREST, CRUSH, DATING, SWEETHEARTS, ENGAGED, MARRIED;
        public String id() { return name().toLowerCase(Locale.ROOT); }
        public static Stage of(String id) { return valueOf(id.toUpperCase(Locale.ROOT)); }
        public boolean committed() { return compareTo(DATING) >= 0; }
    }
    public static final double INTEREST_AT = 15, CRUSH_AT = 30, DATE_AT = 35, CONFESS_AT = 50, PROPOSE_AT = 65;
    public static final int SWEETHEART_DAYS = 14;

    /** Whether romance is possible at all between the player and this person, today. */
    public static boolean eligible(Person who, Person.Stage playerStage, String playerGender, boolean family, Conflict conflict) {
        return playerStage != Person.Stage.CHILD && who.stage() == playerStage && who.romantic() && who.attractedTo(playerGender)
                && !family && !conflict.broken();
    }
    /** The pair's spark: 0 to 30, steady for the save. */
    public static double spark(long seed, String id, double chemistry) {
        return 30 * Seeds.roll(seed, "romance", id) * (.5 + .5 * Math.clamp(chemistry, -1, 1));
    }
    public static double meter(double spark, long teenDays, double romanticMemories, double affection) {
        return Math.clamp(spark * (1 - Math.exp(-Math.max(0, teenDays) / 30.0)) + romanticMemories + .4 * Math.max(0, affection - 40), 0, 100);
    }
    /** Where an untended stage drifts by itself (the resident's side: interest and a crush). */
    public static Stage drift(Stage stage, double romance, int level) {
        if (stage.committed()) return stage;
        if (romance >= CRUSH_AT && level >= Levels.KINDLE_NATURE) return Stage.CRUSH;
        if (romance >= INTEREST_AT) return Stage.INTEREST;
        return Stage.NONE;
    }

    /** The player's move: {@code ask_out}, {@code confess}, {@code propose} or {@code wed}. Returns "" when it works, else why not. */
    public static String refuse(String move, Stage stage, double romance, int level, Person.Stage playerStage, long sweetheartDays, boolean elsewhere) {
        return switch (move) {
            case "ask_out" -> elsewhere ? "committed_elsewhere" : stage.committed() ? "already" : stage == Stage.NONE ? "no_interest"
                    : level < Levels.DATING ? "level" : romance < DATE_AT ? "not_yet" : "";
            case "confess" -> stage != Stage.DATING ? "not_dating" : level < Levels.CONFESS ? "level" : romance < CONFESS_AT ? "not_yet" : "";
            case "propose" -> stage != Stage.SWEETHEARTS ? "not_sweethearts" : playerStage != Person.Stage.ADULT ? "too_young"
                    : level < Levels.MARRY ? "level" : romance < PROPOSE_AT ? "not_yet" : sweetheartDays < SWEETHEART_DAYS ? "too_soon" : "";
            case "wed" -> stage != Stage.ENGAGED ? "not_engaged" : "";
            default -> "unknown_move";
        };
    }
    public static Stage after(String move) {
        return switch (move) { case "ask_out" -> Stage.DATING; case "confess" -> Stage.SWEETHEARTS; case "propose" -> Stage.ENGAGED; case "wed" -> Stage.MARRIED; default -> Stage.NONE; };
    }

    private Courtship() {}
}
