package dev.shinobi.life.bond;

import static org.junit.jupiter.api.Assertions.*;

import dev.shinobi.life.bond.Courtship.Stage;
import java.util.List;
import org.junit.jupiter.api.Test;

class CourtshipTest {
    static Person peer(String id, Person.Stage stage, String gender, String attraction) {
        return Leaf.person(id, "", "residential", 1, stage, Personality.of("warmhearted", "raise_a_family"), gender, attraction, 10, List.of());
    }
    /** A close friend, grown up alongside the player. */
    static BondWorld close(Person.Stage stage) {
        long seed = 1;
        while (true) {
            var probe = new BondWorld(seed, 0);
            probe.add(peer("x", Person.Stage.CHILD, "FEMALE", "MALE"));
            if (Courtship.spark(seed, "x", probe.chemistry("x", BondWorld.PLAYER)) >= 20) break; // a pair that clicks
            seed++;
        }
        var w = new BondWorld(seed, 0);
        w.player("MALE", "");
        w.add(peer("x", Person.Stage.CHILD, "FEMALE", "MALE"));
        for (int d = 0; d < 60; d++) {
            w.talk("x"); w.experience(Act.MISSION_TOGETHER, List.of("x")); w.act("x", Act.PROTECTED_THEM); w.act("x", Act.FESTIVAL_TOGETHER);
            if (d % 10 == 0) w.moment("x", "bond.x." + d);
            w.endDay();
        }
        w.setPlayerStage(stage); w.grow("x", stage);
        return w;
    }

    @Test void nothingRomanticBetweenChildren() {
        var w = close(Person.Stage.CHILD);
        assertFalse(w.romanceOpen("x"));
        assertEquals(0, w.meters("x").romance());
        assertEquals(Meters.ZERO, w.act("x", Act.DATE), "a date is refused outright");
        assertEquals("not_eligible", w.court("x", "ask_out"));
        w.advance(200);
        assertEquals(Stage.NONE, w.bond("x").romance());
        assertTrue(w.bond("x").memories().stream().allMatch(m -> m.delta().romance() == 0), "festivals leave no romance behind");
    }
    @Test void onlyWithinTheSameAgeStageAndTheRightAttraction() {
        var w = close(Person.Stage.TEEN);
        assertTrue(w.romanceOpen("x"));
        w.setPlayerStage(Person.Stage.ADULT);
        assertFalse(w.romanceOpen("x"), "an adult and a teen: never");
        var p = peer("y", Person.Stage.TEEN, "FEMALE", "FEMALE");
        assertFalse(Courtship.eligible(p, Person.Stage.TEEN, "MALE", false, Conflict.NONE));
        assertFalse(Courtship.eligible(peer("z", Person.Stage.TEEN, "FEMALE", "NONE"), Person.Stage.TEEN, "MALE", false, Conflict.NONE), "not romantic");
        assertFalse(Courtship.eligible(peer("k", Person.Stage.TEEN, "FEMALE", "ANY"), Person.Stage.TEEN, "MALE", true, Conflict.NONE), "family");
    }
    @Test void interestGrowsIntoACrushAndThePlayerMakesTheMoves() {
        var w = close(Person.Stage.TEEN);
        for (int d = 0; d < 60 && w.bond("x").romance() != Stage.CRUSH; d++) { w.experience(Act.DATE, List.of("x")); w.talk("x"); w.endDay(); }
        assertEquals(Stage.CRUSH, w.bond("x").romance());
        for (int d = 0; d < 60 && !w.court("x", "ask_out").isEmpty(); d++) { w.act("x", Act.HEART_TO_HEART); w.endDay(); }
        assertEquals(Stage.DATING, w.bond("x").romance());
        assertEquals("not_sweethearts", w.court("x", "propose"));
        for (int d = 0; d < 120 && !w.court("x", "confess").isEmpty(); d++) {
            w.experience(Act.DATE, List.of("x")); w.act("x", Act.KEPT_PROMISE); w.act("x", Act.HEART_TO_HEART);
            if (d % 15 == 0) w.moment("x", "bond.x.later." + d);
            w.endDay();
        }
        assertEquals(Stage.SWEETHEARTS, w.bond("x").romance());
        assertEquals("too_young", w.court("x", "propose"), "teens don't marry");
    }
    @Test void proposalsWantAdultsLevelTenAndTime() {
        assertEquals("too_young", Courtship.refuse("propose", Stage.SWEETHEARTS, 90, 10, Person.Stage.TEEN, 30, false));
        assertEquals("level", Courtship.refuse("propose", Stage.SWEETHEARTS, 90, 9, Person.Stage.ADULT, 30, false));
        assertEquals("too_soon", Courtship.refuse("propose", Stage.SWEETHEARTS, 90, 10, Person.Stage.ADULT, 3, false));
        assertEquals("", Courtship.refuse("propose", Stage.SWEETHEARTS, 90, 10, Person.Stage.ADULT, 30, false));
        assertEquals("committed_elsewhere", Courtship.refuse("ask_out", Stage.CRUSH, 90, 9, Person.Stage.TEEN, 0, true));
        assertEquals("not_engaged", Courtship.refuse("wed", Stage.SWEETHEARTS, 90, 10, Person.Stage.ADULT, 30, false));
        assertEquals(Stage.MARRIED, Courtship.after("wed"));
    }
    @Test void theSparkIsThePairsOwnAndSteady() {
        assertEquals(Courtship.spark(5, "x", .5), Courtship.spark(5, "x", .5));
        assertTrue(Courtship.spark(5, "x", 1) >= Courtship.spark(5, "x", -1));
        assertTrue(Courtship.meter(20, 1000, 0, 40) > Courtship.meter(20, 5, 0, 40), "it grows with time as teens");
        assertEquals(0, Courtship.meter(0, 0, 0, 40));
    }
}
