package dev.shinobi.life.home;

import dev.shinobi.life.bond.Act;
import java.util.List;
import java.util.Set;

/**
 * The home hangouts (LIFE_TOGETHER.md section 3): what friends do at your place. They are proposed to the bond engine
 * as activities with place {@code home} (hosted by the player), so it can ask, roll tastes, pick highlights and form
 * rituals as it does for Ichiraku. Until its catalog carries them, {@link BondFriends#host} counts them as a plain
 * shared experience of their act. {@code home_dinner} is already in the engine.
 */
public record HomeHangout(String id, int from, int to, int minLevel, int maxGroup, Act act, Set<String> lovedBy, String slice) {

    public static final List<HomeHangout> ALL = List.of(
            new HomeHangout("study_night", 18, 23, 2, 4, Act.STUDIED_TOGETHER, Set.of("thoughtful", "meticulous", "curious", "shy"), "b1"),
            new HomeHangout("cook_together", 17, 22, 3, 4, Act.MEAL_TOGETHER, Set.of("warmhearted", "playful", "gentle"), "b1"),
            new HomeHangout("home_dinner", 18, 21, 5, 6, Act.MEAL_TOGETHER, Set.of("warmhearted", "protective", "steadfast"), "b1"),
            new HomeHangout("squad_crash", 18, 23, 3, 3, Act.HUNG_OUT, Set.of("fiery", "adventurous", "playful"), "b2"),
            new HomeHangout("tea_at_home", 13, 20, 4, 3, Act.HUNG_OUT, Set.of("thoughtful", "stern", "gentle", "pragmatic"), "b2"),
            new HomeHangout("balcony_stargazing", 20, 24, 4, 3, Act.HUNG_OUT, Set.of("curious", "imaginative", "shy", "thoughtful"), "b1"));

    public static HomeHangout of(String id) {
        for (var h : ALL) if (h.id.equals(id)) return h;
        throw new IllegalArgumentException("unknown home hangout " + id);
    }
}
