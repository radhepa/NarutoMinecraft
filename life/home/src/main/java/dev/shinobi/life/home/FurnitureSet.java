package dev.shinobi.life.home;

import java.util.List;
import java.util.Set;

/**
 * Furniture that belongs together. Two of a set's pieces add a little comfort (1), four a little more (3), the whole
 * set 5, and the whole set turns on its {@code perk} (one small, home-only bonus). Visitors whose personality is in {@code lovedBy}
 * enjoy a home that shows the set. Clan sets ({@code clan.<id>}) are three pieces in a clan's colours; members of that
 * clan enjoy them, and the player's own clan's set adds comfort too.
 */
public record FurnitureSet(String id, List<String> pieces, String perk, Set<String> lovedBy, String clan) {

    public FurnitureSet {
        pieces = List.copyOf(pieces); lovedBy = Set.copyOf(lovedBy); clan = clan == null ? "" : clan;
    }
    public boolean clanSet() { return !clan.isEmpty(); }

    /** The comfort a set adds for {@code placed} of its pieces: 1 for two, 3 for four, 5 for all (2 for a clan set). */
    public int bonus(int placed) {
        if (placed >= pieces.size()) return clanSet() ? 2 : 5;
        if (placed >= 4) return 3;
        return placed >= 2 ? 1 : 0;
    }
    public boolean complete(int placed) { return placed >= pieces.size(); }

    /** The perks a complete set turns on. Each is read by one rule in the engine. */
    public static final String HOME_SWEET_HOME = "home_sweet_home", RAMEN_AT_HOME = "ramen_at_home", DOJO = "dojo",
            MORNING_AIR = "morning_air", TEA_TIME = "tea_time", FESTIVE = "festive", CLAN_COLOURS = "clan_colours";
}
