package dev.shinobi.life.roster;

import static dev.shinobi.life.roster.Roster.*;
import static org.junit.jupiter.api.Assertions.*;

import dev.shinobi.life.roster.sim.Season;
import dev.shinobi.life.roster.sim.Season.Profile;
import java.util.List;
import org.junit.jupiter.api.Test;

/** The 60-hour simulation holds the roster's promises for every kind of player, on five seeds. */
class SeasonTest {
    @Test void teammatesStayInTheBandAndPullTheirWeight() {
        for (long seed : Season.SEEDS) for (var p : Profile.values()) {
            var res = Season.play(seed, p);
            String at = p.id() + " seed " + seed;
            for (String t : List.of(TEAMMATE_A, TEAMMATE_B)) {
                var s = res.spread().get(t);
                assertTrue(s.min() >= -2 - 1e-9 && s.max() <= 2 + 1e-9, at + " " + t + " " + s);
                assertTrue(Math.abs(s.mean()) < 1, at + " " + t + " sits close to you on average: " + s.mean());
            }
            // The rubber band does the work; the band itself is a safety net that should almost never step in.
            for (var s : res.spread().values()) assertTrue(s.caughtUp() + s.plateaued() <= s.days() / 50, at + " band " + s);
            if (p != Profile.RECKLESS) {
                assertTrue(res.minShare() >= Contribution.LOW && res.maxShare() <= Contribution.HIGH + .05, at + " share " + res.minShare() + ".." + res.maxShare());
            } else assertTrue(res.minShare() >= Contribution.LOW, at + " share " + res.minShare());
        }
    }
    @Test void theRivalRunsSlightlyAhead() {
        for (long seed : Season.SEEDS) for (var p : Profile.values()) {
            var res = Season.play(seed, p);
            var s = res.spread().get(RIVAL);
            assertTrue(s.mean() > .5 && s.mean() < 2.5, p.id() + " seed " + seed + " rival mean " + s.mean());
            assertTrue(res.rivalAhead() > .7, p.id() + " seed " + seed + " ahead " + res.rivalAhead());
        }
    }
    @Test void theTypicalPlayerMeetsTheGatesOnTime() {
        var res = Season.play(Season.SEEDS[0], Profile.TYPICAL);
        var byId = new java.util.HashMap<String, Season.Row>();
        for (var row : res.rows()) byId.put(row.chapter(), row);
        assertTrue(byId.get("Ch 7").player() >= 5);
        assertTrue(byId.get("Ch 14").player() >= 14 && byId.get("Ch 14").player() < 17);
        assertTrue(byId.get("Ch 20").player() >= 17 && byId.get("Ch 20").player() < 20);
        for (String t : List.of(TEAMMATE_A, TEAMMATE_B)) assertTrue(byId.get("Ch 20").levels().get(t) >= 16, t + " ready for the exams");
    }
    @Test void everyTechniqueIsLearnedWhereThePlayerSeesIt() {
        var res = Season.play(7, Profile.TYPICAL);
        var beta = res.rows().get(20);
        for (String t : List.of(TEAMMATE_A, TEAMMATE_B, RIVAL)) assertTrue(beta.techniques().get(t) >= 7, t + " " + beta.techniques());
        assertEquals(8, beta.playerTechniques());
        assertTrue(res.events().stream().filter(e -> e.kind().equals("technique")).map(GrowthEvent::detail).anyMatch(d -> d.startsWith("niche.")));
    }
    @Test void theSimulationIsDeterministic() {
        assertEquals(Season.table(Season.play(11, Profile.DEVOTED)), Season.table(Season.play(11, Profile.DEVOTED)));
    }
}
