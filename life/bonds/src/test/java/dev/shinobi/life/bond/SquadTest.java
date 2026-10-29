package dev.shinobi.life.bond;

import static dev.shinobi.life.bond.Leaf.*;
import static org.junit.jupiter.api.Assertions.*;

import java.util.List;
import org.junit.jupiter.api.Test;

class SquadTest {
    /** A squad of classmates who already know each other from the Academy. */
    static BondWorld squad() {
        var w = Leaf.classic(5, 0);
        for (int d = 0; d < 12; d++) {
            for (String m : List.of(TEAMMATE_A, TEAMMATE_B, SENSEI, CLASSMATE_C)) { w.talk(m); w.experience(Act.TRAINED_TOGETHER, List.of(m)); }
            w.endDay();
        }
        for (String m : List.of(TEAMMATE_A, TEAMMATE_B, SENSEI)) w.moment(m, "bond.academy");
        w.formSquad("squad:7", SENSEI, TEAMMATES, List.of(CLASSMATE_C));
        return w;
    }

    @Test void cohesionGrowsWithMissionsAndFallsWithQuarrels() {
        assertEquals(Squad.cohesion(50, 0, 0, 0, 0) - 12, Squad.cohesion(50, 0, 0, 0, 1), 1e-9);
        var w = squad();
        double fresh = w.cohesion();
        for (int d = 0; d < 15; d++) { w.experience(Act.MISSION_TOGETHER, w.squad().members()); w.endDay(); }
        double seasoned = w.cohesion();
        assertTrue(seasoned > fresh + 10, fresh + " -> " + seasoned);
        assertEquals(15, w.squad().missions());
        w.npcAct(TEAMMATE_A, TEAMMATE_B, Act.QUARREL);
        assertTrue(w.cohesion() < seasoned, "teammates quarrelling with each other hurts the squad");
    }
    @Test void favoritismBreedsJealousyTowardYouAndTheFavorite() {
        var w = squad();
        for (int d = 0; d < 20; d++) { w.talk(TEAMMATE_A); w.gift(TEAMMATE_A, "item:brush"); w.favor(TEAMMATE_A, 3); w.endDay(); }
        assertEquals(TEAMMATE_A, w.squad().favorite());
        assertTrue(w.squad().jealousy(TEAMMATE_B) >= Squad.JEALOUS);
        assertTrue(w.bond(TEAMMATE_B).remembers(Act.FELT_OVERLOOKED), "overlooked by you");
        assertTrue(w.bond(TEAMMATE_B, TEAMMATE_A).remembers(Act.FELT_OVERLOOKED), "and resentful of the favorite");
        assertTrue(w.meters(TEAMMATE_B, TEAMMATE_A).rivalry() > w.meters(TEAMMATE_A, TEAMMATE_B).rivalry());
        assertTrue(BondConditions.test(w, java.util.Map.of("jealous", TEAMMATE_B)));
        assertTrue(w.drainEvents().stream().anyMatch(e -> e.kind().equals("conflict") && e.who().equals(TEAMMATE_B)), "left alone, it boils over");
    }
    @Test void anEvenHandBreedsNoJealousy() {
        var w = squad();
        for (int d = 0; d < 20; d++) { for (String t : TEAMMATES) { w.talk(t); w.favor(t, 3); } w.endDay(); }
        for (String t : TEAMMATES) assertTrue(w.squad().jealousy(t) < 1);
        assertEquals("", w.squad().favorite());
    }
    @Test void aTeammateWhoseBondStaysLowLeavesAndCanComeBack() {
        var w = squad();
        w.act(TEAMMATE_B, Act.BROKE_SECRET);
        for (int d = 0; d < Squad.GRACE_DAYS + Squad.LOW_DAYS + 2; d++) { w.talk(TEAMMATE_A); w.endDay(); }
        assertFalse(w.squad().teammates().contains(TEAMMATE_B), "left");
        assertTrue(w.squad().teammates().contains(CLASSMATE_C), "a classmate took the place");
        assertEquals("low_bond", w.squad().departed().get(TEAMMATE_B).reason());
        assertFalse(w.canReturn(TEAMMATE_B), "not while it is broken");
        w.mend(TEAMMATE_B);
        for (int d = 0; d < 100 && !w.canReturn(TEAMMATE_B); d++) {
            w.talk(TEAMMATE_B); w.experience(Act.MISSION_TOGETHER, List.of(TEAMMATE_B)); w.act(TEAMMATE_B, Act.STOOD_BY_THEM); w.act(TEAMMATE_B, Act.PROTECTED_THEM); w.endDay();
        }
        assertTrue(w.canReturn(TEAMMATE_B));
        assertTrue(w.returnToSquad(TEAMMATE_B));
        assertTrue(w.squad().teammates().contains(TEAMMATE_B));
        assertEquals(List.of(CLASSMATE_C), w.squad().bench(), "the stand-in steps back");
    }
    @Test void nobodyLeavesWithoutSomeoneToTakeTheirPlaceAndStoryExitsNeedTheStory() {
        var w = Leaf.classic(5, 0);
        w.formSquad("squad:7", SENSEI, TEAMMATES, List.of());
        w.act(TEAMMATE_B, Act.BROKE_SECRET);
        w.advance(40);
        assertTrue(w.squad().teammates().contains(TEAMMATE_B), "strained, but still on the squad");
        w.leaveSquad(TEAMMATE_A, "story");
        assertFalse(w.canReturn(TEAMMATE_A), "the story brings them back, not the bond");
        assertTrue(BondEffects.apply(w, java.util.Map.of("return_to_squad", TEAMMATE_A)).isEmpty());
        assertTrue(w.squad().has(TEAMMATE_A));
    }
    @Test void senseiTrustFollowsOrdersAndMissions() {
        var good = squad(); var bad = squad();
        for (int d = 0; d < 10; d++) {
            good.act(SENSEI, Act.FOLLOWED_ORDERS); good.act(SENSEI, Act.MISSION_SUCCESS);
            bad.act(SENSEI, Act.DISOBEYED_ORDERS); bad.act(SENSEI, Act.MISSION_FAILED);
            good.endDay(); bad.endDay();
        }
        assertTrue(good.meters(SENSEI).trust() > bad.meters(SENSEI).trust() + 15);
        assertTrue(BondConditions.test(good, java.util.Map.of("bond_meter", List.of("role:sensei", "trust", 20))));
    }
}
