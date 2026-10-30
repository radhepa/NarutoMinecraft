package dev.shinobi.life.economy;

import java.util.ArrayList;
import java.util.List;

/**
 * What is on a shop's shelf (ITEMS.md, Shops). Core lines are always there once the player's rank and the slice
 * allow them. A shop also has a few weekly rotating slots: a Classic save fills them from the rotating lines in
 * their listed order, a week at a time; a Varied save rolls them from the {@code shops} stream keyed by shop id and
 * week (ROADMAP §5 World creation), so the same seed always shows the same shelf.
 */
public final class Stock {
    public enum Mode { CLASSIC, VARIED }

    /** The lines on {@code shop}'s shelf in {@code week} (a VF week: day / 7) for a player of {@code rank}. */
    public static List<Catalogue.Line> shelf(Catalogue.Shop shop, long week, Mode mode, long seed, String rank, String slice) {
        var out = new ArrayList<Catalogue.Line>();
        if (!Ladder.sliceAllows(slice, shop.slice()) || !serves(shop, rank)) return out;
        for (var line : shop.core()) if (open(line, rank, slice)) out.add(line);
        var pool = shop.rotation().stream().filter(l -> open(l, rank, slice)).toList();
        int slots = Math.min(shop.rotating(), pool.size());
        if (slots == 0) return out;
        if (mode == Mode.CLASSIC) {
            for (int i = 0; i < slots; i++) out.add(pool.get((int) Math.floorMod(week * slots + i, (long) pool.size())));
        } else {
            var left = new ArrayList<>(pool);
            var rng = Streams.stream(seed, "shops", shop.id() + "|" + week);
            for (int i = 0; i < slots; i++) out.add(left.remove(rng.below(left.size())));
        }
        return out;
    }

    /** Whether a shop serves a player of {@code rank}: an Academy shop serves students only (ITEMS.md), the rest that rank and up. */
    public static boolean serves(Catalogue.Shop shop, String rank) {
        return shop.rank().equals("academy") ? rank.equals("academy") : Ladder.rankAllows(rank, shop.rank());
    }

    static boolean open(Catalogue.Line line, String rank, String slice) {
        return Ladder.rankAllows(rank, line.rank()) && Ladder.sliceAllows(slice, line.slice());
    }

    /** How many of a line are left: {@code qty} at each restock (0 is unlimited), less what was bought since. */
    public static int left(Catalogue.Line line, long day, long lastBuyDay, int boughtSince) {
        if (line.qty() == 0) return Integer.MAX_VALUE;
        if (line.restock().equals("once")) return Math.max(0, line.qty() - boughtSince);
        boolean restocked = restockIndex(line.restock(), day) != restockIndex(line.restock(), lastBuyDay);
        return restocked ? line.qty() : Math.max(0, line.qty() - boughtSince);
    }
    /** Which restock period a day falls in: a new period means a full shelf. */
    public static long restockIndex(String restock, long day) {
        return switch (restock) {
            case "daily" -> day;
            case "3d" -> Math.floorDiv(day, 3);
            case "weekly" -> Math.floorDiv(day, 7);
            default -> 0;
        };
    }

    private Stock() {}
}
