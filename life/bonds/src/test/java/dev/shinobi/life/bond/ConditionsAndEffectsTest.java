package dev.shinobi.life.bond;

import static dev.shinobi.life.bond.Leaf.*;
import static org.junit.jupiter.api.Assertions.*;

import java.util.List;
import java.util.Map;
import org.junit.jupiter.api.Test;

/** The bond conditions and actions as quest and dialogue data write them (ROADMAP.md's formats). */
class ConditionsAndEffectsTest {
    static Map<String, Object> c(String key, Object arg) { return Map.of(key, arg); }

    @Test void theRoadmapsQuestBranchReadsTheLevelTheyActOn() {
        var w = Leaf.classic(1, 0);
        var branch = c("friendship", List.of(TEAMMATE_A, 5));
        assertFalse(BondConditions.test(w, branch));
        w.bond(TEAMMATE_A).level = 5;
        assertTrue(BondConditions.test(w, branch));
        w.quarrel(TEAMMATE_A, Act.QUARREL);
        assertFalse(BondConditions.test(w, branch), "a quarrel lowers the level they act on");
        var any = c("any", List.of(c("clan", "nara"), branch));
        assertThrows(IllegalArgumentException.class, () -> BondConditions.test(w, any), "clan is Core's, not the bond engine's");
        assertTrue(BondConditions.test(w, c("not", branch)));
    }
    @Test void roleGroupsPassOnlyWhenEveryMemberDoes() {
        var w = Leaf.classic(1, 0);
        w.formSquad("squad:7", SENSEI, TEAMMATES, List.of());
        w.bond(TEAMMATE_A).level = 6; w.bond(TEAMMATE_B).level = 6; w.bond(SENSEI).level = 3;
        assertTrue(BondConditions.test(w, c("friendship", List.of("role:teammates", 6))));
        assertFalse(BondConditions.test(w, c("friendship", List.of("role:squad", 6))));
        assertTrue(BondConditions.test(w, c("in_squad", TEAMMATE_B)));
        assertFalse(BondConditions.test(w, c("friendship", List.of("role:nobody", 0))), "an unbound role passes nothing");
    }
    @Test void everyConditionReadsItsPart() {
        var w = Leaf.classic(1, 0);
        w.formSquad("squad:7", SENSEI, TEAMMATES, List.of());
        w.act(TEAMMATE_B, Act.KEPT_SECRET);
        w.moment(TEAMMATE_A, "bond.teammate_a.1");
        assertTrue(BondConditions.test(w, c("bond_memory", List.of(TEAMMATE_B, "kept_secret"))));
        assertTrue(BondConditions.test(w, c("bond_moment", List.of(TEAMMATE_A, "bond.teammate_a.1"))));
        assertTrue(BondConditions.test(w, c("bond_meter", List.of(TEAMMATE_B, "trust", 20))));
        assertTrue(BondConditions.test(w, c("bond_state", List.of(TEAMMATE_B, "none"))));
        assertTrue(BondConditions.test(w, c("romance_stage", List.of(TEAMMATE_A, "none"))));
        assertFalse(BondConditions.test(w, c("romance_stage", List.of(TEAMMATE_A, "dating"))));
        assertTrue(BondConditions.test(w, c("kindling", List.of(TEAMMATE_A, "none"))));
        assertFalse(BondConditions.test(w, c("kindling", List.of(TEAMMATE_A, "spark"))));
        assertTrue(BondConditions.test(w, c("squad_cohesion", 0)));
        assertFalse(BondConditions.test(w, c("squad_can_return", TEAMMATE_B)));
        assertTrue(BondConditions.test(w, c("standing", List.of("village", "newcomer"))));
        assertFalse(BondConditions.test(w, c("standing", List.of("village", "hero"))));
        assertFalse(BondConditions.test(w, c("jealous", TEAMMATE_A)));
        for (String name : List.of("friendship", "bond_meter", "bond_memory", "bond_moment", "bond_state", "romance_stage", "kindling",
                "knows_fact", "squad_cohesion", "in_squad", "squad_can_return", "standing", "jealous")) assertTrue(BondConditions.known(name));
        assertThrows(IllegalArgumentException.class, () -> BondConditions.test(w, c("bond_meter", List.of(TEAMMATE_A, "trust"))));
    }
    @Test void questRewardsAndEventsApplyToTheRightPeople() {
        var w = Leaf.classic(1, 0);
        w.formSquad("squad:7", SENSEI, TEAMMATES, List.of());
        assertEquals("", BondEffects.apply(w, c("add_friendship", Map.of("role:squad", 3))), "the roadmap's reward form");
        for (String m : w.squad().members()) assertTrue(w.bond(m).warmth() > 0);
        assertEquals("", BondEffects.apply(w, c("bond_event", List.of("role:squad", "camp_night"))));
        assertTrue(w.bond(TEAMMATE_A, TEAMMATE_B).remembers(Act.CAMP_NIGHT), "a group experience reaches squadmates' bonds with each other");
        assertEquals("", BondEffects.apply(w, c("bond_event", Map.of("who", TEAMMATE_B, "act", "saved_life", "witnesses", List.of("role:squad")))));
        assertTrue(w.bond(TEAMMATE_A).memories().stream().anyMatch(m -> m.act() == Act.SAVED_LIFE && m.source() == Reaction.Source.SEEN));
        assertEquals("", BondEffects.apply(w, c("shared_moment", List.of(TEAMMATE_A, "bond.teammate_a.campfire"))));
        assertTrue(w.bond(TEAMMATE_A).moments().contains("bond.teammate_a.campfire"));
        BondEffects.apply(w, c("reveal_fact", List.of(RIVAL, "values")));
        assertTrue(w.bond(RIVAL).facts().contains("values"));
        BondEffects.apply(w, c("favor", List.of(TEAMMATE_A, 4)));
        assertEquals(4, w.squad().attention(TEAMMATE_A), 1e-9);
        assertEquals("", BondEffects.apply(w, c("deed", Map.of("act", "defended_village", "witnesses", List.of("role:squad")))));
        assertEquals(Act.DEFENDED_VILLAGE, w.deeds().getLast().act());
        assertEquals("", BondEffects.apply(w, c("set_flag", List.of(Kindling.UNLOCK_FLAG, true))));
        assertTrue(w.flag(Kindling.UNLOCK_FLAG));
        assertEquals("nobody", BondEffects.apply(w, c("apologize", "role:nobody")));
    }
    @Test void quarrelEffectsWalkTheArc() {
        var w = Leaf.classic(1, 0);
        BondEffects.apply(w, c("start_conflict", List.of(RIVAL, "quarrel")));
        assertEquals(Conflict.State.ARGUMENT, w.bond(RIVAL).conflict().state());
        assertEquals("not_ready", BondEffects.apply(w, c("reconcile", RIVAL)));
        assertEquals("", BondEffects.apply(w, c("mend", RIVAL)));
        assertEquals(Conflict.State.NONE, w.bond(RIVAL).conflict().state());
        assertEquals("not_eligible", BondEffects.apply(w, c("romance", List.of(TEAMMATE_A, "ask_out"))), "children: never");
        assertEquals("not_eligible", BondEffects.apply(w, c("marry", TEAMMATE_A)));
        w.formSquad("squad:7", SENSEI, TEAMMATES, List.of(CLASSMATE_C));
        assertEquals("", BondEffects.apply(w, c("remove_from_squad", List.of(TEAMMATE_B, "story"))));
        assertTrue(w.squad().teammates().contains(CLASSMATE_C));
        assertEquals("", BondEffects.apply(w, c("return_to_squad", TEAMMATE_B)));
        assertEquals("not_departed", BondEffects.apply(w, c("return_to_squad", TEAMMATE_B)));
        assertThrows(IllegalArgumentException.class, () -> BondEffects.apply(w, c("teleport", RIVAL)));
        assertTrue(BondEffects.known("marry") && BondEffects.known("remove_from_squad"));
    }
}
