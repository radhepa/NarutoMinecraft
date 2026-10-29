package dev.shinobi.life.home;

import dev.shinobi.life.home.Piece.Category;
import java.util.ArrayList;
import java.util.Comparator;
import java.util.List;
import java.util.Map;
import java.util.TreeMap;

/**
 * How comfortable and how stylish a home is. Comfort is what rest reads; style is what visitors notice.
 *
 * <pre>
 * comfort = pieces (diminishing within a category: 1, 0.5, 0.25...) + set bonuses + plant + pet + own clan's set
 *           (a kotatsu counts double in winter), at most the home's cap, less 10% (at most 5) when messy
 * style   = each different piece's style once + 1 per keepsake and photo on show + half the set bonuses
 * </pre>
 *
 * Tiers: Bare (under 10), Cosy (10), Comfortable (20), Homely (38), Beloved (55). The Academy flat holds 60, so
 * Beloved is the very top of a small flat; bigger homes hold more.
 */
public final class Comfort {
    public enum Tier {
        BARE(0), COSY(10), COMFORTABLE(20), HOMELY(38), BELOVED(55);
        public final int from;
        Tier(int from) { this.from = from; }
        public static Tier of(double comfort) {
            Tier t = BARE;
            for (var x : values()) if (comfort >= x.from) t = x;
            return t;
        }
        public String id() { return name().toLowerCase(java.util.Locale.ROOT); }
    }
    public static final double DIMINISH = .5, MESSY_SHARE = .1, MESSY_MAX = 5;

    /** The breakdown, so the furnish screen can show where comfort comes from. */
    public record Score(double comfort, double style, Tier tier, double pieces, int sets, int extras, double messPenalty,
            Map<String, Integer> setPieces, List<String> perks) {
        public boolean perk(String id) { return perks.contains(id); }
    }

    /** {@code season} is VF's (0 spring to 3 winter); {@code clan} the player's clan, or empty. */
    public static Score of(Home home, long day, int season, String clan) {
        var byCategory = new TreeMap<Category, List<Integer>>();
        var setPieces = new TreeMap<String, Integer>();
        var distinct = new java.util.TreeSet<String>();
        double style = 0;
        for (String id : home.placed()) {
            var p = Catalog.piece(id);
            int c = p.comfort() * (p.tags().contains("winter") && season == 3 ? 2 : 1);
            byCategory.computeIfAbsent(p.category(), k -> new ArrayList<>()).add(c);
            if (distinct.add(id)) {
                style += p.style();
                if (p.inSet()) setPieces.merge(p.set(), 1, Integer::sum);
            }
        }
        for (String fixture : List.of("window", "bathtub")) style += Catalog.piece(fixture).style();
        double pieces = 0;
        for (var list : byCategory.values()) {
            list.sort(Comparator.reverseOrder());
            double w = 1;
            for (int c : list) { pieces += c * w; w *= DIMINISH; }
        }
        pieces += Catalog.piece("bathtub").comfort();
        int sets = 0;
        var perks = new ArrayList<String>();
        for (var e : setPieces.entrySet()) {
            var set = Catalog.set(e.getKey());
            int bonus = set.bonus(e.getValue());
            if (set.clanSet() && !set.clan().equals(clan)) bonus = 0;
            sets += bonus;
            if (set.complete(e.getValue()) && !perks.contains(set.perk())) perks.add(set.perk());
        }
        int extras = home.plant.comfort(day) * (home.hasTag("plant") ? 1 : 0) + (home.petAtHome() ? 2 : 0);
        double raw = Math.min(home.flat().tier().cap, pieces + sets + extras);
        double penalty = home.tidiness() == Home.Tidiness.MESSY ? Math.min(MESSY_MAX, raw * MESSY_SHARE) : 0;
        double comfort = raw - penalty;
        style += home.displayed().size() + home.wall().size() + sets / 2.0;
        return new Score(comfort, style, Tier.of(comfort), pieces, sets, extras, penalty, setPieces, List.copyOf(perks));
    }

    private Comfort() {}
}
