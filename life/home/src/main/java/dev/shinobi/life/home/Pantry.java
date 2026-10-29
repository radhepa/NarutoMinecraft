package dev.shinobi.life.home;

import java.util.ArrayList;
import java.util.List;
import java.util.Map;

/**
 * The cupboard (and the icebox, once you have one). Food keeps for a while and then goes stale, like the milk at the
 * back of a twelve-year-old's cupboard. Stale food is still eaten: it only gives one Well Fed tier less and a funny
 * line ({@code home.pantry.stale.<food>}); very stale food gives no Well Fed and a funnier one. Never sickness, never
 * damage. An icebox keeps perishable food twice as long.
 */
public final class Pantry {
    /** Days each food keeps before it goes stale; foods not listed keep {@link #DEFAULT_DAYS}. */
    public static final Map<String, Integer> KEEPS = Map.ofEntries(
            Map.entry("milk", 4), Map.entry("onigiri", 2), Map.entry("dango", 2), Map.entry("bread", 5), Map.entry("fruit", 5),
            Map.entry("vegetables", 6), Map.entry("home_dish", 3), Map.entry("bento", 2), Map.entry("dried_fish", 30),
            Map.entry("rice", 60), Map.entry("instant_ramen", 120), Map.entry("green_tea", 90), Map.entry("soldier_pill", 365));
    public static final int DEFAULT_DAYS = 7, VERY_STALE = 3;

    public record Food(String id, long stored, int tier) {}
    /** What eating gave: the Well Fed tier after staleness, and the line to show (empty for none). */
    public record Meal(String food, int tier, String freshness, String line) {}

    private final List<Food> shelf = new ArrayList<>();
    private boolean icebox;

    public void icebox(boolean on) { icebox = on; }
    public void store(String food, long day, int tier) { shelf.add(new Food(food, day, tier)); }
    public List<Food> contents() { return List.copyOf(shelf); }
    public boolean empty() { return shelf.isEmpty(); }

    public int keeps(String food) {
        int d = KEEPS.getOrDefault(food, DEFAULT_DAYS);
        return icebox && d <= 7 ? d * 2 : d;
    }
    /** "fresh", "stale" or "very_stale" on that day. */
    public String freshness(Food f, long day) {
        long age = day - f.stored();
        int k = keeps(f.id());
        return age <= k ? "fresh" : age <= (long) k * VERY_STALE ? "stale" : "very_stale";
    }
    public long staleCount(long day) { return shelf.stream().filter(f -> !freshness(f, day).equals("fresh")).count(); }

    /** Eats the freshest food in the cupboard (or the freshest of the one asked for); null when there is none. */
    public Meal eat(long day, String wanted) {
        Food pick = null;
        for (var f : shelf) {
            if (wanted != null && !f.id().equals(wanted)) continue;
            if (pick == null || keepsLeft(f, day) > keepsLeft(pick, day)) pick = f;
        }
        return pick == null ? null : take(pick, day);
    }
    /** Eats the oldest food first: what a hungry kid actually does. */
    public Meal eatOldest(long day) {
        Food pick = shelf.stream().min((a, b) -> Long.compare(a.stored(), b.stored())).orElse(null);
        return pick == null ? null : take(pick, day);
    }
    private Meal take(Food f, long day) {
        shelf.remove(f);
        String fresh = freshness(f, day);
        int tier = switch (fresh) { case "fresh" -> f.tier(); case "stale" -> Math.max(0, f.tier() - 1); default -> 0; };
        return new Meal(f.id(), tier, fresh, fresh.equals("fresh") ? "" : "home.pantry." + fresh + "." + f.id());
    }
    private long keepsLeft(Food f, long day) { return f.stored() + keeps(f.id()) - day; }
}
