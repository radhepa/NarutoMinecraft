package dev.shinobi.progression.mission;

import dev.shinobi.progression.mission.sim.DeskDays;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

/** Beta 2 through the desk, for a steady player: the roadmap's pacing and the variety MISSIONS.md promises. */
class SimulationTest {
    static final Catalogue CAT = CatalogueTest.CAT;

    @Test void geninLifeHasTheRoadmapsMissionCount() {
        double d = 0, c = 0, saved = 0, distinct = 0, taken = 0, twists = 0;
        int seeds = 12, minGap = Integer.MAX_VALUE;
        var steady = DeskDays.PROFILES.get(1);
        for (int k = 0; k < seeds; k++) {
            var r = DeskDays.play(CAT, 20261029L + 7919L * k, k % 2 == 0 ? Desk.Mode.CLASSIC : Desk.Mode.VARIED, steady, DeskDays.BETA2_DAYS, false);
            d += r.taken.getOrDefault(Rank.D, 0);
            c += r.taken.getOrDefault(Rank.C, 0);
            saved += r.ryo - r.living;
            distinct += r.perTemplate.size();
            taken += r.taken.values().stream().mapToInt(Integer::intValue).sum();
            twists += r.twists;
            minGap = Math.min(minGap, r.minRepeatGap);
        }
        d /= seeds; c /= seeds;
        assertTrue(d >= 8 && d <= 16, "about 12 board D-ranks in Genin life: " + d);
        assertTrue(c >= 2 && c <= 4.5, "about 3 board C-ranks: " + c);
        assertTrue(saved > 0, "a steady player saves money");
        assertTrue(distinct / taken >= 0.85, "few repeats in the beta: " + distinct / taken);
        assertTrue(minGap >= 8, "a template never comes back within 8 days: " + minGap);
        assertTrue(twists / taken > 0.35, "plenty of twists: " + twists / taken);
    }
}
