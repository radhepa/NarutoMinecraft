package dev.shinobi.life.roster;

import static dev.shinobi.life.roster.Roster.*;
import static org.junit.jupiter.api.Assertions.*;

import java.util.List;
import java.util.Map;
import org.junit.jupiter.api.Test;

class RosterTest {
    static final Peer A = Peer.teammate("role:a", Niche.GENJUTSU, "", 0, 1);

    /** A roster of one, with the player at {@code level}. */
    static Roster one(Peer p, double level, double playerLevel) {
        var r = new Roster(1).player(Curve.xpAt(playerLevel)).add(p, Technique.kit(p.niche(), p.clan()), level);
        r.group(List.of(p.id()));
        return r;
    }
    static double perDay(double level) { return Curve.Stretch.of(level).cost() / 3; }

    @Test void someoneBehindCatchesUpAndSomeoneAheadSlowsDown() {
        var behind = one(A, 8, 10); var ahead = one(A, 11.9, 10); var even = one(A, 10, 10);
        double b0 = behind.level("role:a"), a0 = ahead.level("role:a"), e0 = even.level("role:a");
        double pxp = Curve.xpAt(10.0);
        for (int d = 0; d < 6; d++) {
            pxp += perDay(10);
            for (var r : List.of(behind, ahead, even)) r.day(new Day(pxp, perDay(10), true, Map.of()));
        }
        double moved = Curve.level(pxp) - 10;
        assertTrue(behind.level("role:a") - b0 > 1.5 * moved, "behind: catches up faster than the player moves");
        assertTrue(ahead.level("role:a") - a0 < .6 * moved, "ahead: slows down");
        assertEquals(moved, even.level("role:a") - e0, .05, "on target: keeps pace");
    }
    @Test void theBandHoldsWhenThePlayerRacesAheadOrStops() {
        var r = one(A, 10, 10);
        double pxp = Curve.xpAt(10.0);
        // The player binges side quests: six levels in a day, alone.
        r.day(Day.apart(pxp = Curve.xpAt(16.0)));
        assertTrue(r.level("role:a") >= 16 - A.band() - 1e-9, "lifted to the band");
        assertTrue(r.caughtUp("role:a") > 0);
        assertTrue(r.drainEvents().stream().anyMatch(e -> e.kind().equals("caught_up")));
        // The player stops playing missions for weeks; the teammate trains on.
        for (int d = 0; d < 60; d++) r.day(Day.apart(pxp));
        assertTrue(r.level("role:a") <= 16 + A.band() + 1e-9, "held at the top of the band");
    }
    @Test void dyingDoesNotDragTheSquadDown() {
        var r = one(A, 10, 10);
        double best = Curve.xpAt(10.0);
        r.day(Day.apart(Curve.xpAt(9.0)));       // the player died: one level lost
        assertEquals(10, r.bestPlayerLevel(), 1e-9);
        assertTrue(r.level("role:a") >= 10 - 1e-9);
        assertEquals(9, r.playerLevel(), 1e-9);
        assertTrue(best > 0);
    }
    @Test void theRivalRunsAheadAndTeammatesStayClose() {
        var r = Roster.classic(5);
        r.group(r.ids().stream().filter(id -> !SENIORS.contains(id)).toList());
        double xp = 0;
        for (int d = 0; d < 120; d++) {
            double gain = perDay(Curve.level(xp));
            xp += gain;
            r.day(new Day(xp, d % 4 == 3 ? 0 : gain * .85, d % 4 != 3, Map.of()));
            if (d == 15) r.group(List.of(TEAMMATE_A, TEAMMATE_B));
        }
        double player = r.playerLevel();
        assertTrue(r.level(RIVAL) > player && r.level(RIVAL) < player + 3, "the rival is ahead, but not out of reach");
        for (String t : List.of(TEAMMATE_A, TEAMMATE_B)) assertEquals(player, r.level(t), 2, t);
        for (String c : r.ids()) assertEquals(player + r.peer(c).offset(player), r.level(c), r.peer(c).band(), c + " sits near where they belong");
    }
    @Test void bondsMakeTrainingTogetherWorthMore() {
        assertEquals(1, trainingBonus(0, false));
        assertEquals(1.2, trainingBonus(10, false), 1e-9);
        assertEquals(1, trainingBonus(10, true), "a quarrel takes the bonus away");
        var close = one(A, 10, 10); var cold = one(A, 10, 10); var quarrel = one(A, 10, 10);
        double pxp = Curve.xpAt(10.0) + perDay(10);
        close.day(new Day(pxp, perDay(10), true, Map.of("role:a", BondInput.of(9).training(1))));
        cold.day(new Day(pxp, perDay(10), true, Map.of("role:a", BondInput.of(1).training(1))));
        quarrel.day(new Day(pxp, perDay(10), true, Map.of("role:a", BondInput.of(9).training(1).quarrelling(true))));
        assertTrue(close.level("role:a") > cold.level("role:a"));
        assertTrue(cold.level("role:a") > quarrel.level("role:a"));
    }
    @Test void teammatesAreBetterThanYouInTheirNiche() {
        var r = one(A, 10, 10);
        assertEquals(10 + nicheEdge(10), r.nicheLevel("role:a"), 1e-9);
        assertTrue(nicheEdge(17) >= 2 && nicheEdge(50) <= 4.01);
        assertTrue(Contribution.share(r, "role:a", 0) > 1, "level with you, they pull more than their weight in a fight that suits them");
    }
    @Test void kindlingMakesThemStrongerStill() {
        var r = one(A, 30, 30);
        double before = r.nicheLevel("role:a"), xp = r.level("role:a");
        r.day(new Day(Curve.xpAt(30.0), 0, false, Map.of("role:a", BondInput.of(10).kindled("blaze"))));
        double full = r.nicheLevel("role:a");
        assertTrue(full > before, "a blaze bond: a level more in their niche");
        r.kindle("role:a");
        double now = r.level("role:a");
        assertEquals(now + nicheEdge(now) + BLAZE_EDGE + KINDLE_BOOST, r.nicheLevel("role:a"), 1e-9, "while the flame burns");
        assertTrue(r.level("role:a") > xp);
        assertEquals(1, r.kindles("role:a"));
        r.day(new Day(Curve.xpAt(30.0), 0, false, Map.of("role:a", BondInput.of(10).kindled("blaze"))));
        assertEquals(r.level("role:a") + nicheEdge(r.level("role:a")) + BLAZE_EDGE, r.nicheLevel("role:a"), 1e-9, "the flame dies down");
    }
    @Test void promotionsSetFloors() {
        var r = one(A, 4, 4.5);
        r.promote("role:a", 5);
        assertEquals(5, r.level("role:a"), 1e-9);
        for (int d = 0; d < 30; d++) r.day(Day.apart(Curve.xpAt(4.5)));
        assertTrue(r.level("role:a") >= 5);
    }
    @Test void aTimeSkipEvensThingsOutHalfway() {
        var r = one(A, 8, 10);
        r.timeSkip();
        assertEquals(9, r.level("role:a"), 1e-9);
    }
    @Test void oneSeedOneSave() {
        assertEquals(run(42), run(42));
        assertNotEquals(run(42), run(43));
    }
    static String run(long seed) {
        var r = Roster.classic(seed);
        double xp = 0;
        for (int d = 0; d < 80; d++) { xp += perDay(Curve.level(xp)); r.day(Day.apart(xp)); }
        return r.save();
    }
    @Test void saveAndLoadKeepEverything() {
        var r = Roster.classic(9);
        r.group(List.of(TEAMMATE_A, TEAMMATE_B));
        double xp = 0;
        for (int d = 0; d < 40; d++) { xp += perDay(Curve.level(xp)); r.day(new Day(xp, 30, true, Map.of())); }
        r.beat("ch12.natures", List.of(TEAMMATE_A));
        var copy = Roster.classic(9);
        copy.load(r.save());
        assertEquals(r.save(), copy.save());
        assertEquals(r.techniques(TEAMMATE_A), copy.techniques(TEAMMATE_A));
        assertEquals(List.of(TEAMMATE_A, TEAMMATE_B), copy.groupMembers());
        assertThrows(IllegalArgumentException.class, () -> copy.load("bonds 1"));
    }
    @Test void aReloadedSaveGrowsLikeAnUnbrokenOne() {
        var unbroken = Roster.classic(9);
        var reloaded = Roster.classic(9);
        double xp = 0;
        for (int d = 0; d < 40; d++) {
            xp += perDay(Curve.level(xp));
            unbroken.day(Day.apart(xp)); reloaded.day(Day.apart(xp));
            if (d == 19) { var copy = Roster.classic(9); copy.load(reloaded.save()); reloaded = copy; }
        }
        assertEquals(unbroken.save(), reloaded.save());
    }
    @Test void offsetsMoveFromEarlyToLate() {
        assertThrows(IllegalArgumentException.class, () -> new Peer("x", Niche.TOOLS, "", 0, 0, 1, 0, 1));
        assertEquals(1, Peer.rival("r", Niche.NINJUTSU, "uchiha").offset(10));
        var late = Peer.teammate("t", Niche.TAIJUTSU, "", -1.2, -.1, 15, 1);
        assertEquals(-1.2, late.offset(1), 1e-9, "a slow starter");
        assertEquals(-.1, late.offset(15), 1e-9, "caught up by level 15");
        assertTrue(late.offset(8) > -1.2 && late.offset(8) < -.1);
    }
    @Test void groupLevelIsTheSquadsMean() {
        var r = one(A, 12, 10);
        assertEquals((10 + r.level("role:a")) / 2, r.groupLevel(), 1e-9);
    }
}
