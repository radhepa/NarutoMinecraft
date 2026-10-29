package dev.shinobi.life.roster;

/**
 * Someone who grows beside the player: a classmate, a teammate or the rival. They sit {@code offset} levels from the
 * player (the rival a level ahead, a shy teammate a little behind) and never leave the band from {@code below} under
 * the player to {@code above} over them. {@code drive} is how hard they train on days apart (1 is the player's own
 * pace).
 */
public record Peer(String id, Niche niche, String clan, double offset, double below, double above, double drive) {
    public Peer {
        if (offset < -below || offset > above) throw new IllegalArgumentException(id + ": offset outside the band");
    }
    /** A squadmate: within two levels of you either way. */
    public static Peer teammate(String id, Niche niche, String clan, double offset, double drive) {
        return new Peer(id, niche, clan, offset, 2, 2, drive);
    }
    /** The rival: a level ahead, never more than one behind or three ahead. */
    public static Peer rival(String id, Niche niche, String clan) { return new Peer(id, niche, clan, 1, 1, 3, 1.15); }
    /** A classmate on another squad: a looser band of three. */
    public static Peer classmate(String id, Niche niche, String clan, double offset, double drive) {
        return new Peer(id, niche, clan, offset, 3, 3, drive);
    }
}
