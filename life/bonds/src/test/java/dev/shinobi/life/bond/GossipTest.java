package dev.shinobi.life.bond;

import static dev.shinobi.life.bond.Leaf.*;
import static org.junit.jupiter.api.Assertions.*;

import java.util.ArrayList;
import java.util.List;
import org.junit.jupiter.api.Test;

class GossipTest {
    /** A district of residents who all share a street, plus a squad. */
    static BondWorld street(long seed, int n) {
        var w = Leaf.classic(seed, 0);
        for (int i = 0; i < n; i++) w.add(Leaf.person("r" + i, "", "riverside", Person.CIVILIAN, Person.Stage.ADULT, Personality.of("curious", "see_the_world"),
                "FEMALE", "MALE", 0, List.of()));
        return w;
    }
    static long knowing(Deed d, String prefix) { return d.knowers().keySet().stream().filter(k -> k.startsWith(prefix)).count(); }

    @Test void aboutHalfADistrictHearsANotableDeedInThreeDaysAndMostInSix() {
        double half = 0, most = 0; int runs = 12;
        for (int seed = 0; seed < runs; seed++) {
            var w = street(seed, 30);
            var d = w.deed(Act.PROTECTED_THEM, "r0", List.of("r1"));
            w.advance(4);
            half += knowing(d, "r") / 30.0;
            w.advance(3);
            most += knowing(d, "r") / 30.0;
        }
        half /= runs; most /= runs;
        assertTrue(half > .3 && half < .8, "after three days " + half);
        assertTrue(most > .75, "after six days " + most);
    }
    @Test void smallDeedsStayInCloseCirclesAndBigOnesAreNews() {
        var w = street(3, 20);
        var small = w.deed(Act.HELPED_RESIDENT, "r0", List.of("r1"));
        var big = w.deed(Act.SAVED_LIFE, "r2", List.of());
        w.advance(10);
        assertEquals(2, knowing(small, "r"), "a street is not close enough for small news");
        assertEquals(w.people().size(), big.knowers().size(), "everyone heard the big news the next day");
    }
    @Test void wordReachesTeammatesThroughTheSquadBeforeYouTellThem() {
        var w = Leaf.classic(9, 0);
        w.formSquad("squad:7", SENSEI, TEAMMATES, List.of());
        w.quarrel(TEAMMATE_A, Act.QUARREL);
        var d = w.deeds().getLast();
        for (int day = 0; day < 10 && !d.knows(TEAMMATE_B); day++) w.endDay();
        assertTrue(d.knows(TEAMMATE_B), "squadmates talk");
        assertFalse(w.tell(TEAMMATE_B, d.serial()), "too late: they heard it first");
        assertTrue(w.bond(TEAMMATE_B).remembers(Act.QUARREL));
        assertEquals(Reaction.Source.HEARD, w.bond(TEAMMATE_B).memories().stream().filter(m -> m.act() == Act.QUARREL).findFirst().orElseThrow().source());
    }
    @Test void tellingSomeoneYourselfLandsBetterThanGossip() {
        var told = Leaf.classic(4, 0); var heard = Leaf.classic(4, 0);
        for (var w : List.of(told, heard)) w.act(RIVAL, Act.QUARREL);
        assertTrue(told.tell(TEAMMATE_A, told.deeds().getLast().serial()));
        var rumor = heard.deeds().getLast();
        for (int day = 0; day < 30 && !rumor.knows(TEAMMATE_A); day++) { heard.endDay(); told.endDay(); }
        assertEquals(Reaction.Source.HEARD, rumor.know(TEAMMATE_A).how());
        assertTrue(told.meters(TEAMMATE_A).trust() > heard.meters(TEAMMATE_A).trust(), "honesty earns trust");
        assertTrue(told.meters(TEAMMATE_A).affection() >= heard.meters(TEAMMATE_A).affection());
        assertTrue(told.bond(TEAMMATE_A).memories().stream().anyMatch(m -> m.source() == Reaction.Source.TOLD && m.delta().trust() > 0));
    }
    @Test void gossipIsDeterministic() {
        var runs = new ArrayList<List<String>>();
        for (int i = 0; i < 2; i++) {
            var w = street(42, 25);
            var d = w.deed(Act.DEFENDED_VILLAGE, "", List.of("r3"));
            w.advance(5);
            runs.add(List.copyOf(d.knowers().keySet()));
        }
        assertEquals(runs.get(0), runs.get(1));
    }
    @Test void hearingYouHelpedSomeoneTheyLoveCountsMore() {
        var w = Leaf.classic(2, 0);
        w.add(new Person("kid", "", "residential", Person.CIVILIAN, Person.Stage.CHILD, Personality.of("playful", "see_the_world"), "MALE", "NONE", 3,
                java.util.Map.of(COOK, "parent"), List.of()));
        w.add(new Person(COOK, "", "market", Person.CIVILIAN, Person.Stage.ADULT, Personality.of("warmhearted", "open_a_shop"), "MALE", "FEMALE", 56,
                java.util.Map.of("kid", "child"), List.of("work:ichiraku")));
        w.add(Leaf.resident("stranger", "warmhearted"));
        w.deed(Act.PROTECTED_THEM, "kid", List.of(COOK, "stranger"));
        assertTrue(w.meters(COOK).trust() > w.meters("stranger").trust(), "a parent hears it differently");
    }
}
