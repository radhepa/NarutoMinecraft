package dev.shinobi.life.bond;

import dev.shinobi.life.bond.Personality.Value;

/**
 * The bond side of building a clan: whether a resident would join the player's clan, and whether a clan invites a
 * clanless player in. Progression's {@code Recruiting} owns the clan file, the registry and member slots; it asks
 * here first.
 *
 * <p><b>Joining your clan</b> (ROADMAP.md, "Player clans"): clanless, at bond level 7 or more, not quarrelling, and a
 * free slot (3 at Chunin, 8 at Jonin, 20 as Hokage). Then they agree with chance
 * <pre>0.45 + 0.08 (level - 7) + 0.2 if they value loyalty + 0.1 warmth + trust / 400
 *       - 0.2 if they value family and have family here - 0.15 if they value freedom</pre>
 * rolled once a week, so asking again the same week gets the same answer.
 *
 * <p><b>A clan's invitation:</b> a clanless player, Pillar standing or better with the clan, and either two members at
 * level 8 or a clan elder (a member with the circle {@code elder:<clan>}) at level 9.
 */
public final class Recruitment {
    public static int slots(int playerRank) {
        return switch (playerRank) { case 2 -> 3; case 3, 4 -> 8; case 5 -> 20; default -> 0; };
    }
    public static double chance(Person p, int level, double trust) {
        var pp = p.personality();
        double c = .45 + .08 * (level - Levels.RECRUIT) + .1 * pp.warmth() + trust / 400;
        if (pp.holds(Value.LOYALTY)) c += .2;
        if (pp.holds(Value.FAMILY) && !p.family().isEmpty()) c -= .2;
        if (pp.holds(Value.FREEDOM)) c -= .15;
        return Math.clamp(c, .05, .95);
    }
    /** "" when they agree to join {@code clan}, else why not: has_clan, rank, full, level, quarrel, not_now. */
    public static String refuse(BondWorld w, String who, String clan, int members) {
        var p = w.person(who);
        if (!p.clanless()) return "has_clan";
        if (slots(w.playerRank()) == 0) return "rank";
        if (members >= slots(w.playerRank())) return "full";
        int level = w.effectiveLevel(who);
        if (level < Levels.RECRUIT) return "level";
        if (w.bond(who).conflict().active() || w.bond(who).conflict().broken()) return "quarrel";
        double roll = Seeds.roll(w.seed(), "recruit", who, clan, Long.toString(w.day() / 7));
        return roll < chance(p, level, w.meters(who).trust()) ? "" : "not_now";
    }
    public static boolean invited(BondWorld w, String clan) {
        if (!w.playerClan().isEmpty()) return false;
        if (Standing.title(w, "clan:" + clan).compareTo(Standing.Title.PILLAR) < 0) return false;
        int close = 0;
        for (var p : w.people()) {
            if (!p.clan().equals(clan) || !w.knows(p.id())) continue;
            int level = w.effectiveLevel(p.id());
            if (p.circles().contains("elder:" + clan) && level >= 9) return true;
            if (level >= 8) close++;
        }
        return close >= 2;
    }

    private Recruitment() {}
}
