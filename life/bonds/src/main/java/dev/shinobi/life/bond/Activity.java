package dev.shinobi.life.bond;

import dev.shinobi.life.bond.Personality.Value;
import java.util.List;
import java.util.Map;
import java.util.Set;
import java.util.TreeMap;

/**
 * Something two or more people can do together in the Leaf: where (an anchor from districts.json, or someone's
 * home), when (hours, and a season for some), what it costs in ryo, how close you must be to suggest it, how many can
 * come, which act it is to the bond engine, and who loves it (VF personalities and values). Hangouts are data: the
 * Adventure datapack can add activities with the same fields.
 */
public record Activity(String id, String place, int from, int to, int season, int cost, int minLevel, int maxGroup, Act act,
        Set<String> lovedBy, Set<String> dislikedBy, Set<Value> values, boolean romantic, Person.Stage minStage, int highlights) {

    public static final int ANY_SEASON = -1;
    /** Seasons in VF's calendar: spring, summer, autumn, winter. */
    public static int season(long day) { return (int) Math.floorMod(day, BondWorld.YEAR) / 28; }
    public boolean open(long day, int hour) {
        boolean hours = from <= to ? hour >= from && hour < to : hour >= from || hour < to;
        return hours && (season == ANY_SEASON || season(day) == season);
    }
    /** The place, with {@code home:} resolved to the host's home. */
    public String placeFor(String host) { return place.equals("home") ? "home:" + host : place; }

    private static Activity a(String id, String place, int from, int to, int cost, int minLevel, int group, Act act, Set<String> loved,
            Set<String> disliked, Set<Value> values, int highlights) {
        return new Activity(id, place, from, to, ANY_SEASON, cost, minLevel, group, act, loved, disliked, values, false, Person.Stage.CHILD, highlights);
    }
    private Activity in(int s) { return new Activity(id, place, from, to, s, cost, minLevel, maxGroup, act, lovedBy, dislikedBy, values, romantic, minStage, highlights); }
    private Activity dating() { return new Activity(id, place, from, to, season, cost, minLevel, 2, act, lovedBy, dislikedBy, values, true, Person.Stage.TEEN, highlights); }

    /** The beta's hangouts and the later ones; {@code highlights} is how many highlight lines each has in the dialogue bank. */
    public static final Map<String, Activity> CATALOG = catalog();
    private static Map<String, Activity> catalog() {
        var all = List.of(
                a("ramen", "place:ichiraku", 11, 23, 8, 1, 4, Act.MEAL_TOGETHER, Set.of("fiery", "warmhearted", "playful", "adventurous"), Set.of(), Set.of(Value.FAMILY), 12),
                a("dango", "place:tea_house", 10, 19, 6, 1, 4, Act.MEAL_TOGETHER, Set.of("gentle", "shy", "playful", "warmhearted"), Set.of("proud"), Set.of(Value.KINDNESS), 10),
                a("barbecue", "place:barbecue_house", 17, 23, 30, 4, 6, Act.MEAL_TOGETHER, Set.of("warmhearted", "fiery", "steadfast"), Set.of(), Set.of(Value.FAMILY), 10),
                a("spar", "place:training_ground", 6, 20, 0, 2, 2, Act.TRAINED_TOGETHER, Set.of("proud", "fiery", "adventurous", "protective"), Set.of("gentle", "shy"), Set.of(Value.STRENGTH), 12),
                a("train", "place:training_ground_3", 6, 19, 0, 1, 4, Act.TRAINED_TOGETHER, Set.of("stern", "meticulous", "steadfast", "proud"), Set.of("playful"), Set.of(Value.DUTY, Value.STRENGTH), 10),
                a("fishing", "place:river", 5, 11, 0, 2, 3, Act.HUNG_OUT, Set.of("reserved", "steadfast", "pragmatic"), Set.of("fiery"), Set.of(Value.FREEDOM), 10),
                a("stargazing", "place:hokage_rock", 20, 2, 0, 4, 3, Act.HUNG_OUT, Set.of("curious", "imaginative", "shy", "thoughtful"), Set.of(), Set.of(Value.KNOWLEDGE), 10),
                a("painting", "place:overlook", 9, 18, 5, 3, 2, Act.HUNG_OUT, Set.of("imaginative", "shy", "gentle"), Set.of("pragmatic"), Set.of(Value.CREATIVITY), 8),
                a("shogi", "place:tea_house", 13, 21, 0, 2, 2, Act.HUNG_OUT, Set.of("thoughtful", "meticulous", "pragmatic", "stern"), Set.of("fiery", "playful"), Set.of(Value.KNOWLEDGE), 10),
                a("library", "place:academy_library", 9, 18, 0, 1, 4, Act.STUDIED_TOGETHER, Set.of("thoughtful", "curious", "meticulous"), Set.of("adventurous"), Set.of(Value.KNOWLEDGE), 8),
                a("market_stroll", "place:market_street", 9, 20, 10, 1, 4, Act.HUNG_OUT, Set.of("playful", "curious", "warmhearted"), Set.of("reserved"), Set.of(Value.FREEDOM), 12),
                a("roof_race", "place:rooftops", 7, 21, 0, 2, 4, Act.TRAINED_TOGETHER, Set.of("fiery", "adventurous", "playful"), Set.of("meticulous", "stern"), Set.of(Value.COURAGE), 8),
                a("bathhouse", "place:bathhouse", 16, 23, 5, 3, 6, Act.HUNG_OUT, Set.of("warmhearted", "steadfast", "playful"), Set.of("reserved", "shy"), Set.of(), 8),
                a("shrine_visit", "place:shrine", 6, 18, 0, 2, 4, Act.HUNG_OUT, Set.of("steadfast", "gentle", "stern"), Set.of(), Set.of(Value.FAMILY, Value.DUTY), 8),
                a("pet_walk", "place:river", 6, 20, 0, 1, 3, Act.HUNG_OUT, Set.of("protective", "fiery", "gentle"), Set.of(), Set.of(Value.KINDNESS), 8),
                a("home_dinner", "home", 18, 21, 0, 5, 6, Act.MEAL_TOGETHER, Set.of("warmhearted", "protective", "steadfast"), Set.of(), Set.of(Value.FAMILY), 12),
                // At the player's home (HOME.md, "Home hangouts"); the player hosts.
                a("study_night", "home", 18, 23, 0, 2, 4, Act.STUDIED_TOGETHER, Set.of("thoughtful", "meticulous", "curious", "shy"), Set.of("adventurous"), Set.of(Value.KNOWLEDGE), 8),
                a("cook_together", "home", 17, 22, 0, 3, 4, Act.MEAL_TOGETHER, Set.of("warmhearted", "playful", "gentle"), Set.of(), Set.of(Value.FAMILY), 8),
                a("balcony_stargazing", "home", 20, 24, 0, 4, 3, Act.HUNG_OUT, Set.of("curious", "imaginative", "shy", "thoughtful"), Set.of(), Set.of(Value.KNOWLEDGE), 8),
                a("squad_crash", "home", 18, 23, 0, 3, 3, Act.HUNG_OUT, Set.of("fiery", "adventurous", "playful"), Set.of("reserved"), Set.of(Value.LOYALTY), 8),
                a("tea_at_home", "home", 13, 20, 0, 4, 3, Act.HUNG_OUT, Set.of("thoughtful", "stern", "gentle", "pragmatic"), Set.of("fiery"), Set.of(), 8),
                a("flower_viewing", "place:flower_park", 9, 19, 0, 2, 6, Act.FESTIVAL_TOGETHER, Set.of("gentle", "imaginative", "warmhearted"), Set.of(), Set.of(Value.CREATIVITY), 8).in(0),
                a("lake_swim", "place:lake", 9, 18, 0, 2, 6, Act.HUNG_OUT, Set.of("adventurous", "playful", "fiery"), Set.of("reserved"), Set.of(Value.FREEDOM), 8).in(1),
                a("moon_viewing", "place:hokage_rock", 19, 24, 0, 3, 6, Act.HUNG_OUT, Set.of("thoughtful", "gentle", "stern"), Set.of(), Set.of(Value.FAMILY), 8).in(2),
                a("snowball_fight", "place:training_ground", 9, 17, 0, 1, 8, Act.HUNG_OUT, Set.of("playful", "fiery", "adventurous"), Set.of("stern"), Set.of(), 8).in(3),
                a("evening_walk", "place:river", 18, 23, 0, 7, 2, Act.DATE, Set.of("gentle", "shy", "imaginative", "warmhearted"), Set.of(), Set.of(), 12).dating(),
                a("lantern_night", "place:lake", 19, 24, 5, 7, 2, Act.DATE, Set.of("imaginative", "thoughtful", "gentle"), Set.of(), Set.of(Value.CREATIVITY), 10).dating());
        var m = new TreeMap<String, Activity>();
        for (var x : all) m.put(x.id(), x);
        return Map.copyOf(m);
    }
    public static Activity of(String id) {
        var a = CATALOG.get(id);
        if (a == null) throw new IllegalArgumentException("unknown activity " + id);
        return a;
    }

    /** Each person's own favorite and least favorite hangout, from the save seed: tastes beyond their personality. */
    public static String favorite(long seed, String who) { return pick(seed, who, "favorite_hangout"); }
    public static String leastFavorite(long seed, String who) {
        String fav = favorite(seed, who), least = pick(seed, who, "least_hangout");
        return least.equals(fav) ? pick(seed, who + "'", "least_hangout") : least;
    }
    private static String pick(long seed, String who, String what) {
        var ids = CATALOG.values().stream().filter(x -> !x.romantic()).map(Activity::id).sorted().toList();
        return ids.get((int) (Seeds.roll(seed, what, who) * ids.size()));
    }
    /** How much someone enjoys an activity, from -1 to 1: personality, values, and their own favorite and least favorite. */
    public static double taste(long seed, Person p, Activity a) {
        double t = 0;
        String arch = p.personality().archetype();
        if (a.lovedBy.contains(arch)) t += .6; else if (a.dislikedBy.contains(arch)) t -= .5;
        for (Value v : a.values) if (p.personality().holds(v)) t += .2;
        if (a.id.equals(favorite(seed, p.id()))) t += .5;
        if (a.id.equals(leastFavorite(seed, p.id()))) t -= .6;
        return Math.clamp(t, -1, 1);
    }
}
