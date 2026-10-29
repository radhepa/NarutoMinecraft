package dev.shinobi.progression.mission;

import org.junit.jupiter.api.Test;

import java.util.List;

import static org.junit.jupiter.api.Assertions.*;

/** Client rapport, requests by name, chains, and the squad's roles and cohesion (MISSIONS.md sections 5 and 6). */
class ClientsAndSquadTest {
    static final Catalogue CAT = CatalogueTest.CAT;

    static Economy.Result graded(Grade g) {
        var row = CAT.economy.row(g);
        return new Economy.Result(Economy.Result.End.DONE, g, 100, 100, row.rapport(), row.standing(), g == Grade.S ? 100 : g == Grade.A ? 90 : 70);
    }

    @Test void rapportGrowsWithGoodWorkAndSours() {
        var c = new Clients(CAT.clients);
        assertEquals("stranger", c.tier("resident:4"));
        c.record("resident:4", graded(Grade.A), 1);
        assertEquals("known", c.tier("resident:4"));
        assertEquals(List.of("resident:4"), c.requesters(2), "a known client pleased with an A asks for you by name");
        c.record("resident:4", graded(Grade.S), 5);
        c.record("resident:4", graded(Grade.B), 9);
        assertTrue(c.atLeast("resident:4", "regular"));
        var bad = new Clients(CAT.clients);
        bad.record("resident:8", CAT.economy.settle(CAT.get("mission.d.harvest"), EconomyTest.offer(CAT.get("mission.d.harvest"), 100, 100),
                Economy.Performance.failure(), -1, false), 3);
        bad.record("resident:8", CAT.economy.settle(CAT.get("mission.d.harvest"), EconomyTest.offer(CAT.get("mission.d.harvest"), 100, 100),
                Economy.Performance.failure(), -1, false), 4);
        assertTrue(bad.soured("resident:8", 10));
        assertFalse(bad.soured("resident:8", 19));
        assertTrue(bad.requesters(10).isEmpty());
    }

    @Test void requestsByNameReachTheBoard() {
        var village = new SampleVillage(11, CAT);
        var desk = new Desk(CAT, 11, Desk.Mode.VARIED, village, false);
        var p = DeskTest.genin();
        boolean seen = false;
        for (int day = 30; day < 90 && !seen; day++) {
            for (Offer o : desk.open(day, p)) if (o.requested()) { seen = true; assertEquals(o.client(), o.requestedBy()); }
            final int today = day;
            var pick = desk.offers().stream().filter(o -> !o.requested() && o.client() != null && desk.refusal(o, p, today) == null).findFirst();
            if (pick.isEmpty()) continue;
            desk.take(pick.get(), day);
            desk.turnIn(pick.get(), Economy.Performance.clean(CAT.get(pick.get().template()).bonuses().size()), 80, true, day);
        }
        assertTrue(seen, "a pleased client asks for you by name within two months");
    }

    @Test void theKilnFamilyComesBackRankByRank() {
        var village = new SampleVillage(13, CAT);
        var desk = new Desk(CAT, 13, Desk.Mode.VARIED, village, true);
        var p = DeskTest.genin("main.ch11.paper_trail", "main.ch13.far_village");
        p.flags.add("story.ch10.done");
        var stages = new java.util.ArrayList<String>();
        for (int day = 30; day < 400 && stages.size() < 4; day++) {
            if (day == 120) { p.rank = "chunin"; p.level = 20; }
            if (day == 240) { p.rank = "jonin"; p.level = 32; }
            for (Offer o : desk.open(day, p)) {
                if (!"chain.kiln".equals(o.chain()) || desk.refusal(o, p, day) != null) continue;
                desk.take(o, day);
                desk.turnIn(o, Economy.Performance.clean(CAT.get(o.template()).bonuses().size()), 80, true, day);
                stages.add(o.template());
                break;
            }
        }
        assertEquals(List.of("mission.d.kiln_firing", "mission.c.kiln_delivery", "mission.b.kiln_glaze", "mission.a.kiln_court"), stages);
    }

    @Test void rolesAndCohesion() {
        var plan = new SquadPlan(CAT.squad);
        var painter = new SquadPlan.Mate("a", "kurama", List.of("openness"), false);
        var loud = new SquadPlan.Mate("b", "", List.of("boldness"), true);
        assertEquals("support", plan.aptitude(painter).getFirst());
        assertEquals("tracker", plan.aptitude(loud).getFirst());
        var tracking = plan.suggest("tracking", List.of(painter, loud));
        assertEquals("tracker", tracking.get("b"));
        assertTrue(plan.goodCall("tracking", tracking, List.of(painter, loud)));
        var wrong = java.util.Map.of("a", "tracker", "b", "guard");
        assertFalse(plan.goodCall("tracking", wrong, List.of(painter, loud)));
        assertEquals("in_step", plan.band(80).name());
        assertEquals("split", plan.band(10).name());
        assertTrue(plan.band(10).disobey() > 0);
        assertEquals("mission.banter.escort.camp.steady", SquadPlan.banter("escort", "camp", "steady"));
    }
}
