package dev.shinobi.progression.mission;

import org.junit.jupiter.api.Test;

import java.util.HashMap;
import java.util.List;
import java.util.Map;

import static org.junit.jupiter.api.Assertions.*;

/** The Mission Desk's board: seeded, gated by rank and story, varied, and capped (MISSIONS.md section 2). */
class DeskTest {
    static final Catalogue CAT = CatalogueTest.CAT;
    static final long SEED = 20261029L;

    static Player genin(String... done) {
        var p = new Player();
        p.rank = "genin";
        p.done.add("main.ch9.small_jobs");
        for (String q : done) p.done.add(q);
        return p;
    }

    static Desk desk(long seed, Desk.Mode mode, boolean later) {
        return new Desk(CAT, seed, mode, new SampleVillage(seed, CAT), later);
    }

    static List<String> ids(List<Offer> offers) { return offers.stream().map(o -> o.template() + o.slots() + o.twist()).toList(); }

    @Test void sameSeedSameBoardOtherSeedOrModeAnother() {
        var a = ids(desk(SEED, Desk.Mode.VARIED, false).open(30, genin()));
        assertEquals(a, ids(desk(SEED, Desk.Mode.VARIED, false).open(30, genin())));
        assertNotEquals(a, ids(desk(SEED + 1, Desk.Mode.VARIED, false).open(30, genin())));
        assertNotEquals(a, ids(desk(SEED, Desk.Mode.CLASSIC, false).open(30, genin())));
    }

    @Test void theBoardOpensWithChapterNine() {
        var p = new Player();
        p.rank = "genin";
        assertTrue(desk(SEED, Desk.Mode.VARIED, false).open(30, p).isEmpty());
        p.rank = "academy";
        p.done.add("main.ch9.small_jobs");
        assertTrue(desk(SEED, Desk.Mode.VARIED, false).open(30, p).isEmpty(), "no missions for Academy students");
    }

    @Test void ranksAreGated() {
        var before = desk(SEED, Desk.Mode.VARIED, false).open(30, genin());
        assertTrue(before.stream().allMatch(o -> o.rank() == Rank.D), "C-ranks wait for Ch 11");
        var after = desk(SEED, Desk.Mode.VARIED, false).open(30, genin("main.ch11.paper_trail"));
        assertTrue(after.stream().anyMatch(o -> o.rank() == Rank.C));
        assertTrue(after.stream().noneMatch(o -> o.rank().compareTo(Rank.C) > 0), "nothing above C for a Genin");
        for (long s = 0; s < 10; s++)
            assertTrue(desk(SEED + s, Desk.Mode.VARIED, false).open(30, genin("main.ch11.paper_trail")).stream()
                    .noneMatch(o -> CAT.get(o.template()).regions().contains("region:border_village")), "the far region waits for Ch 13");
        var chunin = genin("main.ch11.paper_trail");
        chunin.rank = "chunin";
        chunin.level = 20;
        var later = desk(SEED, Desk.Mode.VARIED, true).open(30, chunin);
        assertTrue(later.stream().anyMatch(o -> o.rank() == Rank.B));
        assertTrue(desk(SEED, Desk.Mode.VARIED, false).open(30, chunin).stream().noneMatch(o -> o.rank() == Rank.B),
                "later content stays off in the beta build");
    }

    @Test void columnsHaveTheirSizeAndMixCategories() {
        for (long s = 0; s < 20; s++) {
            var board = desk(SEED + s, Desk.Mode.VARIED, false).open(30, genin("main.ch11.paper_trail", "main.ch13.far_village"));
            var d = board.stream().filter(o -> o.rank() == Rank.D).toList();
            assertTrue(d.size() >= 5, "five D-ranks for a Genin, plus chains and requests");
            var cats = new HashMap<String, Integer>();
            board.stream().filter(o -> o.chain() == null && !o.contest()).forEach(o -> cats.merge(o.rank() + CAT.get(o.template()).category(), 1, Integer::sum));
            assertTrue(cats.values().stream().allMatch(n -> n <= 1), "one offer per category per column: " + cats);
        }
    }

    @Test void aTakenTemplateStaysAwayForItsGap() {
        var desk = desk(SEED, Desk.Mode.VARIED, false);
        var p = genin();
        var taken = new HashMap<String, Integer>();
        for (int d = 30; d < 120; d++) {
            final int day = d;
            var board = desk.open(day, p);
            for (Offer o : board) {
                Integer last = taken.get(o.template());
                if (last != null) assertTrue(day - last >= desk.guard.templateGap(o.rank()), o.template() + " back after " + (day - last));
            }
            Offer pick = board.stream().filter(o -> desk.refusal(o, p, day) == null).findFirst().orElse(null);
            if (pick == null) continue;
            desk.take(pick, day);
            taken.put(pick.template(), day);
            desk.turnIn(pick, Economy.Performance.clean(1), 50, false, day);
        }
    }

    @Test void capsPerDayAndWeek() {
        var desk = desk(SEED, Desk.Mode.VARIED, false);
        var p = genin("main.ch11.paper_trail");
        int day = 35;
        var board = desk.open(day, p);
        var ds = board.stream().filter(o -> o.rank() == Rank.D).toList();
        desk.take(ds.get(0), day);
        assertEquals("in_hand", desk.refusal(ds.get(1), p, day));
        desk.turnIn(ds.get(0), Economy.Performance.clean(1), 50, false, day);
        assertNull(desk.refusal(ds.get(1), p, day));
        Offer c = board.stream().filter(o -> o.rank() == Rank.C).findFirst().orElseThrow();
        assertEquals("day_full", desk.refusal(c, p, day), "a C-rank takes the whole day");
        desk.take(ds.get(1), day);
        desk.turnIn(ds.get(1), Economy.Performance.clean(1), 50, false, day);
        Offer third = desk.offers().stream().filter(o -> o.rank() == Rank.D).findFirst().orElseThrow();
        assertEquals("day_full", desk.refusal(third, p, day), "two D-ranks a day");
        int next = day + 1;
        var c1 = desk.open(next, p).stream().filter(o -> o.rank() == Rank.C).findFirst().orElseThrow();
        desk.take(c1, next);
        desk.turnIn(c1, Economy.Performance.clean(1), 50, false, next);
        int sameWeek = next + 1 < (Unlocks.week(next) + 1) * 7 ? next + 1 : next;
        var c2 = desk.open(sameWeek, p).stream().filter(o -> o.rank() == Rank.C).findFirst();
        if (sameWeek != next && c2.isPresent()) assertEquals("week_full", desk.refusal(c2.get(), p, sameWeek), "one board C-rank a week for a Genin");
    }

    @Test void seasonsAndEventsOpenTheirMissions() {
        var p = genin();
        for (long s = 0; s < 30; s++) {
            for (Offer o : desk(SEED + s, Desk.Mode.VARIED, false).open(10, p)) {   // day 10 is spring
                Template t = CAT.get(o.template());
                assertTrue(t.seasons().isEmpty() || t.seasons().contains("spring"), o.template());
                assertNull(t.event(), "festival missions only around the festival: " + o.template());
            }
        }
        boolean setup = false;
        p.eventIn.put("event.leaf_festival", 2);
        for (long s = 0; s < 40 && !setup; s++)
            setup = desk(SEED + s, Desk.Mode.VARIED, false).open(39, p).stream().anyMatch(o -> o.template().equals("mission.d.festival_setup"));
        assertTrue(setup, "festival setup goes up in the days before the festival");
    }

    @Test void classicOpensWithTheTeachingOrder() {
        var board = desk(SEED, Desk.Mode.CLASSIC, false).open(21, genin());
        var opening = Json.strings(CAT.desk.get("classic_opening"));
        assertEquals(opening.subList(0, 2), board.stream().filter(o -> o.rank() == Rank.D).limit(2).map(Offer::template).toList());
    }

    @Test void twistsComeOftenButNotTheSameTwiceRunning() {
        int twisted = 0, total = 0;
        for (long s = 0; s < 30; s++) {
            for (Offer o : desk(SEED + s, Desk.Mode.VARIED, false).open(30, genin())) {
                total++;
                if (o.twist() != null) twisted++;
            }
        }
        double rate = (double) twisted / total;
        assertTrue(rate > 0.4 && rate < 0.8, "twist rate " + rate);
        var desk = desk(SEED, Desk.Mode.VARIED, false);
        var guard = desk.guard;
        Template t = CAT.get("mission.d.lost_pet");
        var o = new Offer("x", t.id(), Rank.D, Map.of("client", "resident:5"), "two_pets", false, 80, 90, 30, 32, null, null, false);
        guard.taken(o, t, 30);
        assertEquals("two_pets", guard.avoidTwist(t, 35));
        assertNull(guard.avoidTwist(t, 45));
    }

    @Test void slotsAreFilledAndTheSquadIsNeverACLient() {
        for (long s = 0; s < 15; s++) {
            var village = new SampleVillage(SEED + s, CAT);
            for (Offer o : desk(SEED + s, Desk.Mode.VARIED, false).open(30, genin("main.ch11.paper_trail", "main.ch13.far_village"))) {
                Template t = CAT.get(o.template());
                assertEquals(t.slots().keySet(), o.slots().keySet(), o.template());
                assertFalse(village.squad().contains(o.client()), o.template());
                assertTrue(o.pay() > 0 && o.xp() > 0);
            }
        }
    }
}
