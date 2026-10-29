package dev.shinobi.life.economy;

import java.util.HashMap;
import java.util.List;
import java.util.Map;

import static dev.shinobi.life.economy.Json.num;
import static dev.shinobi.life.economy.Json.obj;

/**
 * What things cost (ITEMS.md, Shops): one rule for every shop, tuned in economy.json.
 *
 * <pre>
 *   price    = round(base x grade x markup x (1 - discount))
 *   discount = title discount of the better of the shop's community and the village, + the keeper's friendship step,
 *              at most the cap; Unwelcome pays 20% more, and a clan shop will not serve you at all
 *   sell     = what an item sells back for: furniture and stations at half price, loot at its pawn value, the rest never
 * </pre>
 *
 * Standing titles are the bond engine's ({@code Standing}: Unwelcome, Newcomer, Helping Hand, Good Neighbor, Pillar,
 * Hero), as ids: unwelcome, newcomer, helping_hand, good_neighbor, pillar, hero.
 */
public final class Prices {
    public static final List<String> TITLES = List.of("unwelcome", "newcomer", "helping_hand", "good_neighbor", "pillar", "hero");
    private final Catalogue catalogue;
    private final Map<String, Object> discounts, grades;

    public Prices(Catalogue catalogue) {
        this.catalogue = catalogue;
        this.discounts = catalogue.tuning("discounts");
        this.grades = catalogue.tuning("grades");
    }

    /** The discount (negative: a markup) for a standing title and the keeper's friendship level. */
    public double discount(String title, int keeperLevel) {
        double d = num(obj(discounts.get("titles")).get(title), 0);
        if (d < 0) return d;
        double step = 0;
        for (var e : obj(discounts.get("keeper_friendship")).entrySet())
            if (keeperLevel >= Integer.parseInt(e.getKey())) step = Math.max(step, num(e.getValue(), 0));
        return Math.min(num(discounts.get("cap"), 0.15), d + step);
    }
    /** The better of two titles (the shop's community and the whole village). */
    public static String better(String a, String b) { return TITLES.indexOf(a) >= TITLES.indexOf(b) ? a : b; }
    /** Whether a shop serves you: a clan's own shop refuses an Unwelcome customer. */
    public boolean serves(Catalogue.Shop shop, String title) {
        return !(title.equals("unwelcome") && shop.standing().startsWith("clan:"));
    }

    /** The price of {@code key} (an item id, or {@code item@variant}) at a shop, in a grade, for a customer. */
    public int buy(String key, Catalogue.Shop shop, String grade, String title, int keeperLevel) {
        int base = catalogue.price(key);
        var line = shop == null ? null : shop.stock().stream()
                .filter(l -> key.equals(l.variant().isEmpty() ? l.item() : l.item() + "@" + l.variant())).findFirst().orElse(null);
        if (line != null && line.price() > 0) base = line.price();
        double markup = shop == null || (line != null && line.price() > 0) ? 1 : shop.markup();
        double g = num(obj(grades.get("price")).get(grade == null ? "standard" : grade), 1);
        return (int) Math.round(base * g * markup * (1 - discount(title, keeperLevel)));
    }

    /** What an item sells back for (before the pawn shop's purse and haggling). */
    public int sellBack(String id, String grade) {
        var item = catalogue.item(id);
        double g = item.category().equals("furniture") || item.category().equals("station") ? 1
                : num(obj(grades.get("price")).get(grade == null ? "standard" : grade), 1);
        return (int) Math.floor(item.sell() * g);
    }

    /**
     * The pawn shop: it buys loot and furniture, pays less for each repeat of the same item that day (10% less a
     * time, never under a quarter), and has only so much ryo in its till each day. Resets at dawn.
     */
    public final class Pawn {
        private final Map<String, Integer> soldToday = new HashMap<>();
        private int paidToday;
        private long day = Long.MIN_VALUE;

        /** Sells one; returns the ryo paid (0 if it will not buy it or the till is empty). */
        public int sell(long today, String id, String grade) {
            if (today != day) { day = today; soldToday.clear(); paidToday = 0; }
            var pawn = catalogue.tuning("pawn");
            int value = sellBack(id, grade);
            if (value <= 0) return 0;
            int n = soldToday.getOrDefault(id, 0);
            double factor = Math.max(num(pawn.get("repeat_floor"), .25), 1 - num(pawn.get("repeat_decay"), .1) * n);
            int pay = Math.min((int) Math.floor(value * factor), (int) num(pawn.get("daily_purse"), 400) - paidToday);
            if (pay <= 0) return 0;
            soldToday.merge(id, 1, Integer::sum);
            paidToday += pay;
            return pay;
        }
        public int paidToday() { return paidToday; }
    }
    public Pawn pawn() { return new Pawn(); }

    /**
     * Haggling, only at shops that haggle (stalls, the pawn shop): one try per item per visit, asking 10% or 20% off
     * (or more for what you sell). The chance comes from economy.json: the ask, your standing, and the keeper's warmth
     * and pride (the bond engine's trait axes, -1 to 1). The roll is the {@code haggle} stream keyed by shop, day and item.
     */
    public double haggleChance(double ask, String title, double keeperWarmth, double keeperPride) {
        var h = catalogue.tuning("haggle");
        double base = num(obj(h.get("asks")).get(String.valueOf(ask)), 0);
        double standing = num(obj(h.get("standing_bonus")).get(title), 0);
        var temper = obj(h.get("temper"));
        return Math.clamp(base + standing + num(temper.get("warmth"), 0) * keeperWarmth + num(temper.get("pride"), 0) * keeperPride, 0, 0.95);
    }
    /** The price after one haggle: lower if the roll succeeds, unchanged if it fails. */
    public int haggle(int price, double ask, String title, double warmth, double pride, long seed, String shop, long day, String item) {
        if (catalogue.shops.containsKey(shop) && !catalogue.shops.get(shop).haggles()) return price;
        boolean won = Streams.roll(seed, "haggle", shop, Long.toString(day), item) < haggleChance(ask, title, warmth, pride);
        return won ? (int) Math.round(price * (1 - ask)) : price;
    }
}
