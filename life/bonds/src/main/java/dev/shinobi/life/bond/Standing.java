package dev.shinobi.life.bond;

import java.util.Locale;

/**
 * The player's standing with one community: a clan ({@code clan:nara}), the clanless shinobi
 * ({@code group:clanless}) or civilians ({@code group:civilian}), a district ({@code district:market}), a rank
 * ({@code rank:chunin}, {@code rank:civilian}) or the whole {@code village}. It is what its members think of you,
 * averaged:
 *
 * <pre>deeds    = sum over the deeds they know of: worth x how they know it x fading
 * opinion  = 40 (1 - e^(-deeds / 40)) for good news (bad news counts in full)  +  2 x their bond level with you
 * standing = mean opinion over the community's members</pre>
 *
 * Titles keep VF's names: Unwelcome, Newcomer, Helping Hand, Good Neighbor, Pillar of the Community, Hero.
 */
public final class Standing {
    public enum Title {
        UNWELCOME(Double.NEGATIVE_INFINITY), NEWCOMER(-8), HELPING_HAND(4), GOOD_NEIGHBOR(10), PILLAR(20), HERO(35);
        public final double from;
        Title(double from) { this.from = from; }
        public String id() { return name().toLowerCase(Locale.ROOT); }
        public static Title of(String id) { return valueOf(id.toUpperCase(Locale.ROOT)); }
        public static Title of(double score) {
            Title t = UNWELCOME;
            for (Title x : values()) if (score >= x.from) t = x;
            return t;
        }
    }
    public static final double LEVEL_WEIGHT = 2, SATURATION = 40;

    static double opinion(BondWorld w, String member) {
        double sum = 0;
        for (var d : w.deeds) {
            var k = d.know(member);
            if (k != null && d.act.worth != 0) sum += d.act.worth * k.how().weight * d.fade(w.day);
        }
        if (sum > 0) sum = SATURATION * (1 - Math.exp(-sum / SATURATION));
        var b = w.bonds.get(BondWorld.key(member, BondWorld.PLAYER));
        if (b != null && b.met()) sum += LEVEL_WEIGHT * w.effectiveLevel(member);
        return sum;
    }
    /** The mean opinion of a community's members, or 0 for a community nobody belongs to. */
    public static double score(BondWorld w, String community) {
        double sum = 0; int n = 0;
        for (var p : w.people.values()) if (p.communities().contains(community)) { sum += opinion(w, p.id()); n++; }
        return n == 0 ? 0 : sum / n;
    }
    public static Title title(BondWorld w, String community) { return Title.of(score(w, community)); }

    private Standing() {}
}
