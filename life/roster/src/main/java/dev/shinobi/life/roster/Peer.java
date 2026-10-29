package dev.shinobi.life.roster;

/**
 * Someone who grows beside the player: a classmate, a teammate, the rival, or the squad a year ahead. Each one
 * belongs somewhere relative to the player: {@code early} levels from them at the start, moving to {@code late} by
 * the time the player reaches {@code settle} (a slow starter catches up; the year-ahead squad's lead shrinks).
 * The story sets these offsets for the Classic cast; a rolled cast takes them from clan power ({@link #rolled}).
 * The band keeps them within {@code band} levels of where they belong. {@code drive} is how hard they train on
 * days apart (1 is the player's own pace).
 */
public record Peer(String id, Niche niche, String clan, double early, double late, double settle, double band, double drive) {
    public Peer {
        if (band <= 0 || drive <= 0) throw new IllegalArgumentException(id + ": band and drive must be positive");
    }
    /** Where they belong, in levels from the player, at the player's level. */
    public double offset(double playerLevel) {
        if (settle <= 1 || playerLevel >= settle) return late;
        return early + (late - early) * Math.max(0, playerLevel - 1) / (settle - 1);
    }
    /** A squadmate who keeps one place: within a level and a half of it. */
    public static Peer teammate(String id, Niche niche, String clan, double offset, double drive) {
        return new Peer(id, niche, clan, offset, offset, 1, 1.5, drive);
    }
    /** A squadmate who starts behind (or ahead) and settles by the player's level {@code settle}. */
    public static Peer teammate(String id, Niche niche, String clan, double early, double late, double settle, double drive) {
        return new Peer(id, niche, clan, early, late, settle, 1.5, drive);
    }
    /** The rival: a level ahead, never more than one behind or three ahead of you. */
    public static Peer rival(String id, Niche niche, String clan) { return new Peer(id, niche, clan, 1, 1, 1, 2, 1.15); }
    /** A classmate on another squad: a looser band. */
    public static Peer classmate(String id, Niche niche, String clan, double early, double late, double settle, double drive) {
        return new Peer(id, niche, clan, early, late, settle, 2.5, drive);
    }
    /** The squad a year ahead: well ahead at the Academy, a level or two ahead once everyone is grown. */
    public static Peer senior(String id, Niche niche, String clan, double early, double late, double settle, double drive) {
        return new Peer(id, niche, clan, early, late, settle, 3, drive);
    }
    /**
     * A classmate rolled in a Varied save: clan power sets where they belong on average, the save seed the rest, so a
     * hard-working clanless kid can still outpace a great-clan heir.
     */
    public static Peer rolled(String id, Niche niche, String clan, Seeds.Rng rng) {
        var power = ClanPower.of(clan);
        double offset = Math.clamp(power.classShift + rng.range(-1, 1), -1.5, 1.5);
        return new Peer(id, niche, clan, offset, offset, 1, 2.5, power.drive * rng.range(.92, 1.08));
    }
}
