package dev.shinobi.life.home;

import dev.shinobi.life.bond.Act;
import dev.shinobi.life.bond.BondWorld;
import dev.shinobi.life.bond.Person;
import dev.shinobi.life.bond.Person.Stage;
import dev.shinobi.life.bond.Personality;
import java.util.List;
import java.util.Map;

/**
 * Test fixtures: the beta cast by role (personalities as ROADMAP.md's Classic cast designs them) and the apartment
 * block's neighbours. Genders are the fixture's own choice.
 */
public final class Cast {
    public static final String SENSEI = "role:sensei", INSTRUCTOR = "role:instructor", TEAMMATE_A = "role:teammate_a",
            TEAMMATE_B = "role:teammate_b", CLASSMATE_C = "role:classmate_c", CLASSMATE_D = "role:classmate_d", RIVAL = "role:rival",
            LANDLADY = "resident:landlady", CHILD_UPSTAIRS = "resident:child_upstairs", OLD_NEIGHBOUR = "resident:old_neighbour";
    public static final List<String> SQUAD = List.of(TEAMMATE_A, TEAMMATE_B);
    public static final List<String> CLASSMATES = List.of(TEAMMATE_A, TEAMMATE_B, CLASSMATE_C, CLASSMATE_D, RIVAL);
    public static final List<String> NEIGHBOURS = List.of(LANDLADY, CHILD_UPSTAIRS, OLD_NEIGHBOUR);

    static Person person(String id, String clan, String district, int rank, Stage stage, String archetype, String dream, String gender, int birthday, List<String> circles) {
        return new Person(id, clan, district, rank, stage, Personality.of(archetype, dream), gender, "ANY", birthday, Map.of(), circles);
    }

    public static BondWorld world(long seed) {
        var w = new BondWorld(seed, 0);
        w.player("MALE", "");
        var cls = List.of("class:academy");
        w.add(person(SENSEI, "", "residential", 3, Stage.ADULT, "stern", "be_a_great_teacher", "MALE", 77, List.of("squad:7")));
        w.add(person(INSTRUCTOR, "", "academy", 2, Stage.ADULT, "warmhearted", "be_a_great_teacher", "MALE", 12, List.of("work:academy")));
        w.add(person(TEAMMATE_A, "kurama", "residential", 0, Stage.CHILD, "shy", "master_their_art", "FEMALE", 20, List.of("class:academy", "squad:7")));
        w.add(person(TEAMMATE_B, "", "residential", 0, Stage.CHILD, "fiery", "become_hokage", "MALE", 41, List.of("class:academy", "squad:7")));
        w.add(person(CLASSMATE_C, "kinoshita", "residential", 0, Stage.CHILD, "thoughtful", "build_something_lasting", "MALE", 88, cls));
        w.add(person(CLASSMATE_D, "gekko", "residential", 0, Stage.CHILD, "protective", "protect_the_village", "FEMALE", 99, cls));
        w.add(person(RIVAL, "uchiha", "residential", 0, Stage.CHILD, "proud", "surpass_a_rival", "MALE", 105, cls));
        w.add(person(LANDLADY, "", "residential", Person.CIVILIAN, Stage.ADULT, "warmhearted", "open_a_shop", "FEMALE", 60, List.of("household:block")));
        w.add(person(CHILD_UPSTAIRS, "", "residential", 0, Stage.CHILD, "playful", "become_hokage", "MALE", 3, List.of("household:block")));
        w.add(person(OLD_NEIGHBOUR, "", "residential", Person.CIVILIAN, Stage.ADULT, "reserved", "open_a_shop", "MALE", 70, List.of("household:block")));
        return w;
    }

    /** Spends time with someone (talks, meals, a moment now and then) until their bond reaches {@code level}. */
    public static void befriend(BondWorld w, String who, int level) {
        for (int i = 0; i < 400 && w.level(who) < level; i++) {
            w.talk(who);
            w.act(who, Act.MEAL_TOGETHER);
            w.act(who, Act.TRAINED_TOGETHER);
            if (i % 5 == 0) w.moment(who, "test.moment." + i);
            w.endDay();
        }
    }

    /** A school or duty day: home from 6 to 8 and from {@code back} until bed. */
    public static Visits.Day day(long day, int rank, int back, boolean missionReturn) {
        var home = new boolean[24];
        for (int h = 0; h < 24; h++) home[h] = h < 8 || h >= back;
        return new Visits.Day(day, 0, rank, "", home, missionReturn, SQUAD, SENSEI, INSTRUCTOR, NEIGHBOURS);
    }
    /** A day away from home (a mission on the road, a night at camp). */
    public static Visits.Day away(long day, int rank) {
        return new Visits.Day(day, 0, rank, "", new boolean[24], false, SQUAD, SENSEI, INSTRUCTOR, NEIGHBOURS);
    }

    private Cast() {}
}
