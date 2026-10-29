package dev.shinobi.life.roster;

import static org.junit.jupiter.api.Assertions.*;

import java.util.List;
import java.util.Map;
import org.junit.jupiter.api.Test;

class TechniqueTest {
    static Roster at(double level) {
        var p = Peer.teammate("role:a", Niche.GENJUTSU, "kurama", 0, 1);
        var r = new Roster(3).player(Curve.xpAt(level)).add(p, Technique.kit(p.niche(), p.clan()), level);
        r.group(List.of("role:a"));
        return r;
    }
    @Test void techniquesWaitForABeatThePlayerSees() {
        var r = at(12);
        r.day(Day.apart(Curve.xpAt(12.0)));
        assertTrue(r.techniques("role:a").isEmpty(), "a day apart: nothing learned out of sight");
        r.day(new Day(Curve.xpAt(12.0), 10, true, Map.of()));
        assertTrue(r.techniques("role:a").contains("niche.genjutsu.1"), "training together: the niche technique shows");
        assertFalse(r.techniques("role:a").contains("nature.first"), "a beat's technique waits for its beat");
        r.beat("ch12.natures", List.of("role:a"));
        assertTrue(r.techniques("role:a").containsAll(List.of("nature.first", "clan.kurama.1")));
        assertTrue(r.drainEvents().stream().filter(e -> e.kind().equals("technique")).count() >= 3);
    }
    @Test void aBeatTheyWereNotReadyForShowsAtTheNextTraining() {
        var r = at(8);
        r.beat("ch12.natures", List.of("role:a"));
        assertFalse(r.techniques("role:a").contains("nature.first"), "level 8: not ready");
        r.promote("role:a", 11);
        r.day(new Day(Curve.xpAt(11.0), 10, true, Map.of()));
        assertTrue(r.techniques("role:a").contains("nature.first"), "learned at the next training you share");
    }
    @Test void someoneOnAnotherSquadShowsWhatTheyLearnedWhenYouMeetAgain() {
        var r = at(12);
        r.group(List.of());
        r.beat("ch12.natures", List.of());                       // their own ceremony, out of sight
        r.day(Day.apart(Curve.xpAt(12.0)));
        assertFalse(r.techniques("role:a").contains("nature.first"));
        r.beat("ch15.written_test", List.of("role:a"));            // the exams bring the class back together
        assertTrue(r.techniques("role:a").contains("nature.first"));
    }
    @Test void everyKitStartsWithTheAcademyThreeAndHasTheNiche() {
        for (var n : Niche.values()) {
            var k = Technique.kit(n, "");
            assertEquals("academy.clone", k.getFirst().id());
            assertTrue(k.stream().anyMatch(t -> t.id().equals("niche." + n.id() + ".1")));
            assertTrue(k.stream().noneMatch(t -> t.id().startsWith("clan.")), "clanless: no clan technique");
            for (int i = 1; i < k.size(); i++) assertTrue(k.get(i).minLevel() >= k.get(i - 1).minLevel(), "in level order");
        }
        assertTrue(Technique.kit(Niche.TOOLS, "nara").stream().anyMatch(t -> t.id().equals("clan.nara.1")));
    }
}
