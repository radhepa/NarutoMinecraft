package dev.shinobi.life.bond;

import static dev.shinobi.life.bond.Leaf.*;
import static org.junit.jupiter.api.Assertions.*;

import dev.shinobi.life.bond.sim.Playthrough;
import dev.shinobi.life.bond.sim.Playthrough.Profile;
import java.util.List;
import org.junit.jupiter.api.Test;

class TimeAndPacingTest {
    @Test void seedStreamsAreReproducibleAndIndependent() {
        var a = Seeds.stream(9, "cast", "role:rival"); var b = Seeds.stream(9, "cast", "role:rival");
        for (int i = 0; i < 5; i++) assertEquals(a.next(), b.next());
        assertNotEquals(Seeds.stream(9, "cast", "role:rival").next(), Seeds.stream(9, "names", "role:rival").next());
        assertEquals(Seeds.roll(9, "gossip", "1", "a", "b"), Seeds.roll(9, "gossip", "1", "a", "b"));
        double sum = 0; var r = Seeds.stream(1, "x", "y");
        for (int i = 0; i < 10_000; i++) sum += r.unit();
        assertEquals(.5, sum / 10_000, .02);
    }
    @Test void aTimeSkipKeepsCompanionsCloseAndLetsOthersDriftGently() {
        var w = Leaf.classic(3, 0);
        for (int d = 0; d < 40; d++) { for (String c : CLASSMATES) { w.talk(c); w.experience(Act.TRAINED_TOGETHER, List.of(c)); } w.endDay(); }
        for (String c : CLASSMATES) w.moment(c, "bond.x");
        int a = w.level(TEAMMATE_A), c = w.level(CLASSMATE_C);
        w.timeSkip(BondWorld.YEAR, List.of(TEAMMATE_A));
        assertTrue(w.level(TEAMMATE_A) >= a, "together all along");
        assertTrue(w.bond(TEAMMATE_A).remembers(Act.YEARS_TOGETHER));
        assertTrue(w.level(CLASSMATE_C) >= c - BondWorld.YEAR / 28, "at most a level for every four weeks apart");
        assertTrue(w.level(CLASSMATE_C) <= c);
        assertEquals(40 + BondWorld.YEAR, w.day());
    }
    @Test void pacingMeetsTheRoadmapsFriendshipGates() {
        for (long seed : new long[]{20261029L, 7L}) {
            var devoted = Playthrough.play(seed, Profile.DEVOTED);
            var typical = Playthrough.play(seed, Profile.TYPICAL);
            var reckless = Playthrough.play(seed, Profile.RECKLESS);
            for (var r : List.of(devoted, typical)) {
                assertTrue(r.checks().entrySet().stream().anyMatch(e -> e.getKey().startsWith("ch11 campfire") && e.getValue().equals("plays")),
                        r.profile() + " seed " + seed + ": the Ch 11 campfire wants teammate_a at level 5 " + r.checks());
                var beta = row(r, "Ch 20");
                assertTrue(beta.levels().get(TEAMMATE_A) >= 6 && beta.levels().get(TEAMMATE_B) >= 6, r.profile() + " beta end " + beta);
                var academy = row(r, "Ch 7");
                assertTrue(academy.levels().get(TEAMMATE_A) >= 2 && academy.levels().get(TEAMMATE_A) <= 5, "the Academy is early days " + academy);
            }
            assertTrue(reckless.checks().entrySet().stream().anyMatch(e -> e.getKey().startsWith("ch11 campfire") && e.getValue().equals("skipped")));
            assertTrue(Integer.parseInt(reckless.checks().get("squad departures")) >= 1, "a teammate leaves a reckless player");
            assertTrue(Integer.parseInt(reckless.checks().get("fallings-out")) >= 1);
            assertTrue(row(reckless, "Ch 20").levels().get(TEAMMATE_A) <= row(typical, "Ch 20").levels().get(TEAMMATE_A) - 3, "far behind a typical player");
            for (var r : List.of(devoted, typical, reckless)) assertEquals("none", r.checks().get("romance before the first time skip"), "nothing romantic in the beta");
            assertTrue(Integer.parseInt(devoted.checks().get("bonds at level 10")) >= 2, "a devoted player ends with lifelong bonds");
            assertTrue(Integer.parseInt(devoted.checks().get("bonds at level 10")) >= Integer.parseInt(typical.checks().get("bonds at level 10")));
            assertEquals("0", reckless.checks().get("bonds at level 10"));
            int devotedEnd = devoted.rows().getLast().levels().values().stream().mapToInt(Integer::intValue).sum();
            int recklessEnd = reckless.rows().getLast().levels().values().stream().mapToInt(Integer::intValue).sum();
            assertTrue(devotedEnd > recklessEnd * 2);
        }
    }
    @Test void theWholePlaythroughIsDeterministic() {
        assertEquals(Playthrough.table(Playthrough.play(11, Profile.TYPICAL)), Playthrough.table(Playthrough.play(11, Profile.TYPICAL)));
    }
    static Playthrough.Row row(Playthrough.Result r, String chapter) { return r.rows().stream().filter(x -> x.chapter().equals(chapter)).findFirst().orElseThrow(); }
}
