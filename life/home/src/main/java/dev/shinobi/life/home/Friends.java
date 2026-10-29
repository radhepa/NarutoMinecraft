package dev.shinobi.life.home;

import java.util.List;

/**
 * What the home needs from the bond engine, and what it tells it. The home never keeps its own friendship numbers:
 * who is close, who is free and what a visit did all go through here. {@link BondFriends} is the real one, over
 * {@code life/bonds}' {@code BondWorld}; tests may use it directly.
 */
public interface Friends {
    /** Everyone who knows the player, closest first. */
    List<String> known();
    int level(String who);
    /** In a quarrel or a falling-out: they do not drop by. */
    boolean cold(String who);
    boolean free(String who, long day, int hour);
    /** VF personality id ({@code warmhearted}, {@code meticulous}...). */
    String archetype(String who);
    double warmth(String who);
    double openness(String who);
    String clan(String who);

    /** A visit happened and went this well (0 to 1): a shared experience for a good one, warmth for any. Never a loss. */
    void visited(String who, String kind, double quality);
    /** They noticed something at your home that is about them: a gift you kept on show, a photo they are in. */
    void noticed(String who, String what);
    /** You gave them a spare key: a moment between you. */
    void keyGiven(String who);
    /**
     * You invite them over for a home hangout. Returns how it went ("great", "good", "fine", "rough") for those who
     * came, or the reason nobody could ("busy", "not_close_enough"...).
     */
    String host(List<String> who, String activity, long day, int hour);
}
