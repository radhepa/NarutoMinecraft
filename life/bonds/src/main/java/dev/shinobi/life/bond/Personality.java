package dev.shinobi.life.bond;

import java.util.EnumSet;
import java.util.List;
import java.util.Locale;
import java.util.Map;
import java.util.Set;

/**
 * Who someone is, deeper than Village Friends' twelve personalities: five trait axes from -1 to 1, the values they
 * live by, the things that get under their skin and the dream they are working toward. The same act lands
 * differently on different people ({@link Reaction}). {@code archetype} is the VF personality id (dialogue pools
 * and gift tastes follow it); {@code loves}, {@code likes} and {@code dislikes} are gift ids or item tags.
 */
public record Personality(String archetype, double warmth, double boldness, double pride, double discipline, double openness,
        Set<Value> values, Set<Peeve> peeves, String dream, List<String> loves, List<String> likes, List<String> dislikes) {

    /** Trait axes. Positive ends: warm, bold, proud, disciplined, open; negative ends: cool, cautious, humble, free-spirited, private. */
    public enum Trait { WARMTH, BOLDNESS, PRIDE, DISCIPLINE, OPENNESS }
    /** What a person lives by. An act that honors one of their values lands harder; one that violates it, much harder. */
    public enum Value { LOYALTY, COURAGE, KINDNESS, HONESTY, DUTY, FREEDOM, STRENGTH, KNOWLEDGE, FAMILY, CREATIVITY }
    /** Pet peeves: small things that sting more than they should. */
    public enum Peeve { LATENESS, BRAGGING, COWARDICE, RECKLESSNESS, DISHONESTY, RUDENESS, LAZINESS, CRUELTY, NOSINESS, NEGLECT }
    /** Dreams in the catalog; quests and dialogue name them by id ({@code bond.dream.<id>}). */
    public static final List<String> DREAMS = List.of("master_their_art", "protect_the_village", "become_hokage", "surpass_a_rival",
            "build_something_lasting", "see_the_world", "heal_people", "be_a_great_teacher", "raise_a_family", "honor_their_clan",
            "open_a_shop", "find_where_they_belong");

    public Personality {
        warmth = axis(warmth); boldness = axis(boldness); pride = axis(pride); discipline = axis(discipline); openness = axis(openness);
        values = values.isEmpty() ? Set.of() : Set.copyOf(EnumSet.copyOf(values));
        peeves = peeves.isEmpty() ? Set.of() : Set.copyOf(EnumSet.copyOf(peeves));
        dream = dream == null ? "" : dream;
        loves = List.copyOf(loves); likes = List.copyOf(likes); dislikes = List.copyOf(dislikes);
    }
    private static double axis(double v) { return Math.clamp(v, -1, 1); }

    public double trait(Trait t) {
        return switch (t) { case WARMTH -> warmth; case BOLDNESS -> boldness; case PRIDE -> pride; case DISCIPLINE -> discipline; case OPENNESS -> openness; };
    }
    public boolean holds(Value v) { return values.contains(v); }
    public boolean minds(Peeve p) { return peeves.contains(p); }

    /** How a gift lands: "loved", "liked", "plain", "disliked" or "hated" (a disliked gift to someone it insults). */
    public String taste(String item) {
        if (loves.contains(item)) return "loved";
        if (likes.contains(item)) return "liked";
        if (dislikes.contains(item)) return pride > .4 || minds(Peeve.RUDENESS) ? "hated" : "disliked";
        return "plain";
    }

    // -- archetypes --------------------------------------------------------------------------------

    private record Base(double warmth, double boldness, double pride, double discipline, double openness, Set<Value> values,
            Set<Peeve> peeves, List<String> loves, List<String> dislikes) {}
    private static Base base(double w, double b, double p, double d, double o, Set<Value> v, Set<Peeve> pv, List<String> loves, List<String> dislikes) {
        return new Base(w, b, p, d, o, v, pv, loves, dislikes);
    }
    /**
     * VF's twelve personalities (content.json: hobby, value, loves, dislikes) placed on the trait axes, plus four for
     * the Leaf's shinobi. Gift ids are Shinobi Life's items where they exist; VF's own still work through the tag.
     */
    private static final Map<String, Base> ARCHETYPES = Map.ofEntries(
            Map.entry("warmhearted", base(.8, 0, -.2, .1, .5, Set.of(Value.KINDNESS, Value.FAMILY), Set.of(Peeve.CRUELTY, Peeve.NEGLECT), List.of("food:dango", "food:honey"), List.of("item:spider_eye"))),
            Map.entry("thoughtful", base(.2, -.2, 0, .4, -.2, Set.of(Value.KNOWLEDGE, Value.HONESTY), Set.of(Peeve.RUDENESS, Peeve.BRAGGING), List.of("item:book", "item:scroll"), List.of("item:firework"))),
            Map.entry("playful", base(.5, .3, 0, -.6, .6, Set.of(Value.FREEDOM, Value.KINDNESS), Set.of(Peeve.NEGLECT, Peeve.LAZINESS), List.of("food:dango", "item:note_block"), List.of("item:rotten_flesh"))),
            Map.entry("adventurous", base(.3, .8, .2, -.3, .4, Set.of(Value.COURAGE, Value.FREEDOM), Set.of(Peeve.COWARDICE, Peeve.LAZINESS), List.of("item:compass", "item:sandals"), List.of("item:dead_bush"))),
            Map.entry("meticulous", base(0, -.3, .3, .8, -.2, Set.of(Value.DUTY, Value.KNOWLEDGE), Set.of(Peeve.LATENESS, Peeve.RECKLESSNESS), List.of("item:amethyst_shard", "item:glass"), List.of("item:dirt"))),
            Map.entry("steadfast", base(.3, .2, 0, .5, 0, Set.of(Value.DUTY, Value.LOYALTY), Set.of(Peeve.LATENESS, Peeve.DISHONESTY), List.of("item:seeds", "item:bone_meal"), List.of("item:poisonous_potato"))),
            Map.entry("reserved", base(-.2, -.3, .1, .3, -.8, Set.of(Value.FREEDOM, Value.HONESTY), Set.of(Peeve.NOSINESS, Peeve.RUDENESS), List.of("food:grilled_fish", "item:fishing_rod"), List.of("item:bell"))),
            Map.entry("imaginative", base(.3, 0, 0, -.4, .4, Set.of(Value.CREATIVITY, Value.FREEDOM), Set.of(Peeve.RUDENESS, Peeve.NEGLECT), List.of("item:ink", "item:brush"), List.of("item:gravel"))),
            Map.entry("pragmatic", base(-.3, .1, .2, .4, 0, Set.of(Value.HONESTY, Value.DUTY), Set.of(Peeve.LAZINESS, Peeve.BRAGGING), List.of("item:iron_ingot", "item:whetstone"), List.of("item:gold_nugget"))),
            Map.entry("curious", base(.2, .4, 0, -.1, .6, Set.of(Value.KNOWLEDGE, Value.FREEDOM), Set.of(Peeve.NEGLECT, Peeve.RUDENESS), List.of("item:spyglass", "item:scroll"), List.of("item:rotten_flesh"))),
            Map.entry("protective", base(.4, .4, .2, .3, .1, Set.of(Value.LOYALTY, Value.FAMILY), Set.of(Peeve.RECKLESSNESS, Peeve.CRUELTY), List.of("item:shield", "item:planks"), List.of("item:tnt"))),
            Map.entry("gentle", base(.7, -.4, -.5, .1, .3, Set.of(Value.KINDNESS, Value.FAMILY), Set.of(Peeve.CRUELTY, Peeve.RUDENESS), List.of("item:poppy", "item:dandelion"), List.of("item:spider_eye"))),
            // The Leaf's own.
            Map.entry("proud", base(-.4, .5, .9, .6, -.6, Set.of(Value.STRENGTH, Value.FAMILY), Set.of(Peeve.BRAGGING, Peeve.NOSINESS), List.of("food:onigiri_okaka", "item:whetstone"), List.of("food:dango"))),
            Map.entry("fiery", base(.6, .9, .4, -.5, .8, Set.of(Value.COURAGE, Value.LOYALTY), Set.of(Peeve.COWARDICE, Peeve.NEGLECT), List.of("food:ramen", "item:pet_treat"), List.of("item:book"))),
            Map.entry("shy", base(.5, -.7, -.4, .2, -.6, Set.of(Value.CREATIVITY, Value.KINDNESS), Set.of(Peeve.RUDENESS, Peeve.NOSINESS), List.of("item:brush", "item:ink"), List.of("item:firework"))),
            Map.entry("stern", base(-.1, .3, .4, .9, -.5, Set.of(Value.DUTY, Value.LOYALTY), Set.of(Peeve.RECKLESSNESS, Peeve.LATENESS), List.of("food:green_tea", "item:scroll"), List.of("food:candy"))));
    public static Set<String> archetypes() { return ARCHETYPES.keySet(); }

    /** The archetype as designed (Classic cast and tests). */
    public static Personality of(String archetype, String dream) {
        var b = ARCHETYPES.get(archetype.toLowerCase(Locale.ROOT));
        if (b == null) throw new IllegalArgumentException("unknown personality " + archetype);
        return new Personality(archetype, b.warmth, b.boldness, b.pride, b.discipline, b.openness, b.values, b.peeves, dream,
                b.loves, List.of("food:ramen", "food:onigiri"), b.dislikes);
    }
    /** A rolled resident: the archetype's axes moved by up to {@code spread}, and a dream from the catalog. */
    public static Personality rolled(String archetype, Seeds.Rng rng, double spread) {
        var p = of(archetype, DREAMS.get(rng.below(DREAMS.size())));
        return new Personality(archetype, p.warmth + rng.range(-spread, spread), p.boldness + rng.range(-spread, spread),
                p.pride + rng.range(-spread, spread), p.discipline + rng.range(-spread, spread), p.openness + rng.range(-spread, spread),
                p.values, p.peeves, p.dream, p.loves, p.likes, p.dislikes);
    }
    public Personality withDream(String next) {
        return new Personality(archetype, warmth, boldness, pride, discipline, openness, values, peeves, next, loves, likes, dislikes);
    }
    public Personality withTraits(double w, double b, double p, double d, double o) {
        return new Personality(archetype, w, b, p, d, o, values, peeves, dream, loves, likes, dislikes);
    }
    public Personality withValues(Set<Value> next) {
        return new Personality(archetype, warmth, boldness, pride, discipline, openness, next, peeves, dream, loves, likes, dislikes);
    }
    public Personality withPeeves(Set<Peeve> next) {
        return new Personality(archetype, warmth, boldness, pride, discipline, openness, values, next, dream, loves, likes, dislikes);
    }

    /**
     * How naturally two people click, from -1 to 1, after VF's {@code Chemistry.chemistry}: a stable spark for the pair
     * plus shared values and nearby temperaments, and a little for the warm. The player has no personality, so for
     * the player pass {@code null} and only the resident's warmth and openness add to the spark.
     */
    public static double chemistry(double spark, Personality x, Personality y) {
        if (x == null || y == null) {
            var p = x == null ? y : x;
            return Math.clamp(spark * .6 + p.warmth * .2 + p.openness * .1, -1, 1);
        }
        double shared = 0;
        for (Value v : x.values) if (y.values.contains(v)) shared += .15;
        double distance = 0;
        for (Trait t : Trait.values()) distance += Math.abs(x.trait(t) - y.trait(t));
        double temper = .2 - distance / 10 * .4;
        double warm = (x.warmth + y.warmth) * .05;
        return Math.clamp(spark * .6 + shared + temper + warm, -1, 1);
    }
}
