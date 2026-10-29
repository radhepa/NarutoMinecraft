package dev.shinobi.life.bond;

import dev.shinobi.life.bond.Person.Stage;
import java.util.ArrayList;
import java.util.List;
import java.util.Map;

/**
 * Test fixtures: the Classic cast from ROADMAP.md ("The Classic cast"), as designed there and with a rolled
 * village around them, drawn by the population shares (about 45% civilians, 28% clanless shinobi, 15% minor
 * clans, 13% noble clans). Genders and attraction are the fixture's own choices, not the cast's.
 */
public final class Leaf {
    public static final String SENSEI = "role:sensei", INSTRUCTOR = "role:instructor", MEDIC = "role:medic",
            TEAMMATE_A = "role:teammate_a", TEAMMATE_B = "role:teammate_b", CLASSMATE_C = "role:classmate_c",
            CLASSMATE_D = "role:classmate_d", RIVAL = "role:rival", MERCHANT = "role:merchant", COOK = "resident:ichiraku_cook";
    public static final List<String> CLASSMATES = List.of(TEAMMATE_A, TEAMMATE_B, CLASSMATE_C, CLASSMATE_D, RIVAL);
    public static final List<String> TEAMMATES = List.of(TEAMMATE_A, TEAMMATE_B);
    static final List<String> NOBLE = List.of("uchiha", "hyuga", "nara", "akimichi", "yamanaka", "inuzuka", "aburame", "sarutobi");
    static final List<String> MINOR = List.of("shiranui", "morino", "umino", "haruno", "namiashi", "hagane", "kinoshita");
    static final List<String> DISTRICTS = List.of("market", "residential", "riverside");
    static final List<String> ARCHETYPES = List.of("warmhearted", "thoughtful", "playful", "adventurous", "meticulous", "steadfast",
            "reserved", "imaginative", "pragmatic", "curious", "protective", "gentle");

    public static Person person(String id, String clan, String district, int rank, Stage stage, Personality p, String gender, String attraction,
            int birthday, List<String> circles) {
        return new Person(id, clan, district, rank, stage, p, gender, attraction, birthday, Map.of(), circles);
    }
    /** A plain resident for unit tests. */
    public static Person resident(String id, String archetype) {
        return person(id, "", "market", Person.CIVILIAN, Stage.ADULT, Personality.of(archetype, "open_a_shop"), "FEMALE", "MALE", 50, List.of());
    }
    public static Person classmate(String id, String archetype) {
        return person(id, "", "residential", 0, Stage.CHILD, Personality.of(archetype, "become_hokage"), "MALE", "FEMALE", 30, List.of("class:academy"));
    }

    /** The Classic cast and {@code villagers} rolled residents; the player is a clanless child at the Academy. */
    public static BondWorld classic(long seed, int villagers) {
        var w = new BondWorld(seed, 0);
        w.player("MALE", "");
        var cls = List.of("class:academy");
        w.add(person(SENSEI, "", "residential", 3, Stage.ADULT, Personality.of("stern", "be_a_great_teacher").withTraits(.2, .3, .3, .8, -.5), "MALE", "FEMALE", 77, List.of("squad:7")));
        w.add(person(INSTRUCTOR, "", "academy", 2, Stage.ADULT, Personality.of("warmhearted", "be_a_great_teacher"), "MALE", "FEMALE", 12, List.of("work:academy")));
        w.add(person(MEDIC, "", "residential", 2, Stage.ADULT, Personality.of("gentle", "heal_people"), "FEMALE", "MALE", 64, List.of("work:hospital")));
        w.add(person(TEAMMATE_A, "kurama", "residential", 0, Stage.CHILD, Personality.of("shy", "master_their_art"), "FEMALE", "MALE", 20, List.of("class:academy", "squad:7")));
        w.add(person(TEAMMATE_B, "", "residential", 0, Stage.CHILD, Personality.of("fiery", "become_hokage"), "MALE", "FEMALE", 41, List.of("class:academy", "squad:7")));
        w.add(person(CLASSMATE_C, "kinoshita", "residential", 0, Stage.CHILD, Personality.of("thoughtful", "build_something_lasting"), "MALE", "FEMALE", 88, cls));
        w.add(person(CLASSMATE_D, "gekko", "residential", 0, Stage.CHILD, Personality.of("protective", "protect_the_village"), "FEMALE", "MALE", 99, cls));
        w.add(person(RIVAL, "uchiha", "residential", 0, Stage.CHILD, Personality.of("proud", "surpass_a_rival"), "MALE", "FEMALE", 105, cls));
        w.add(person(MERCHANT, "", "market", Person.CIVILIAN, Stage.ADULT, Personality.of("pragmatic", "open_a_shop"), "MALE", "FEMALE", 9, List.of("work:caravan")));
        w.add(person(COOK, "", "market", Person.CIVILIAN, Stage.ADULT, Personality.of("warmhearted", "open_a_shop"), "MALE", "FEMALE", 56, List.of("work:ichiraku")));
        var rng = Seeds.stream(seed, "residents", "fixture");
        for (int i = 0; i < villagers; i++) {
            double roll = rng.unit();
            String clan = roll < .73 ? "" : roll < .88 ? MINOR.get(rng.below(MINOR.size())) : NOBLE.get(rng.below(NOBLE.size()));
            boolean shinobi = roll >= .45;
            int rank = !shinobi ? Person.CIVILIAN : 1 + rng.below(3);
            String district = DISTRICTS.get(rng.below(DISTRICTS.size()));
            var circles = new ArrayList<String>();
            if (!shinobi && rng.chance(.5)) circles.add("work:" + district + "_shop_" + rng.below(4));
            String gender = rng.chance(.5) ? "FEMALE" : "MALE";
            w.add(person("resident:" + i, clan, district, rank, Stage.ADULT, Personality.rolled(ARCHETYPES.get(rng.below(ARCHETYPES.size())), rng, .2),
                    gender, gender.equals("MALE") ? "FEMALE" : "MALE", rng.below(BondWorld.YEAR), circles));
        }
        return w;
    }

    private Leaf() {}
}
