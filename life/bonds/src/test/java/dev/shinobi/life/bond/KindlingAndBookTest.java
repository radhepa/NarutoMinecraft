package dev.shinobi.life.bond;

import static dev.shinobi.life.bond.Leaf.*;
import static org.junit.jupiter.api.Assertions.*;

import dev.shinobi.life.bond.Kindling.Tier;
import java.util.List;
import org.junit.jupiter.api.Test;

class KindlingAndBookTest {
    @Test void tiersFollowTheBond() {
        assertEquals(Tier.NONE, Kindling.tier(false, 10, true, Conflict.NONE), "asleep until the story awakens it");
        assertEquals(Tier.NONE, Kindling.tier(true, 5, false, Conflict.NONE));
        assertEquals(Tier.SPARK, Kindling.tier(true, 6, false, Conflict.NONE));
        assertEquals(Tier.FLAME, Kindling.tier(true, 8, false, Conflict.NONE));
        assertEquals(Tier.BLAZE, Kindling.tier(true, 10, false, Conflict.NONE));
        assertEquals(Tier.BLAZE, Kindling.tier(true, 7, true, Conflict.NONE), "a spouse blazes");
        var broken = Conflict.NONE.hurt(Act.BROKE_SECRET, Conflict.BREAKS, Personality.of("steadfast", ""), 0);
        assertEquals(Tier.NONE, Kindling.tier(true, 10, false, broken), "a falling-out snuffs it out");
        assertTrue(Tier.SPARK.powers.contains(Kindling.Power.THREAD_SIGHT));
        assertFalse(Tier.SPARK.powers.contains(Kindling.Power.KINDLE));
        assertTrue(Tier.FLAME.powers.containsAll(java.util.Set.of(Kindling.Power.KINDLE, Kindling.Power.EMBER_LINK)));
        assertTrue(Tier.BLAZE.powers.containsAll(java.util.Set.of(Kindling.Power.EMBER_MARK, Kindling.Power.UNISON)));
    }
    @Test void aQuarrelDimsTheFlameAndFightingTogetherBrightensIt() {
        var w = TogetherTest.friends(TEAMMATE_B, 90);
        w.setFlag(Kindling.UNLOCK_FLAG, true);
        assertTrue(Kindling.tier(w, TEAMMATE_B).compareTo(Tier.SPARK) >= 0, "level " + w.effectiveLevel(TEAMMATE_B));
        double bright = Kindling.strength(w, TEAMMATE_B);
        assertTrue(bright > 0);
        w.quarrel(TEAMMATE_B, Act.QUARREL);
        assertTrue(Kindling.strength(w, TEAMMATE_B) < bright, "a quarrel dims it");
        assertTrue(Kindling.flame(w, TEAMMATE_B).dimmed());
        w.mend(TEAMMATE_B);
        w.advance(10);
        double calm = Kindling.strength(w, TEAMMATE_B);
        w.experience(Act.MISSION_TOGETHER, List.of(TEAMMATE_B));
        assertTrue(Kindling.strength(w, TEAMMATE_B) >= calm, "fighting side by side this week");
    }
    @Test void resonanceBuildsOnceADayTowardTheirNature() {
        var w = TogetherTest.friends(TEAMMATE_B, 90);
        assertEquals(0, w.bond(TEAMMATE_B).resonance(), "nothing before the gift awakens");
        w.setFlag(Kindling.UNLOCK_FLAG, true);
        for (int d = 0; d < Kindling.TRIAL_RESONANCE; d++) {
            w.experience(Act.MISSION_TOGETHER, List.of(TEAMMATE_B)); w.experience(Act.TRAINED_TOGETHER, List.of(TEAMMATE_B));
            w.endDay();
        }
        assertEquals(Kindling.TRIAL_RESONANCE, w.bond(TEAMMATE_B).resonance(), "once a day, however much they fought");
        assertTrue(Kindling.flame(w, TEAMMATE_B).natureTrialReady());
        assertTrue(BondConditions.test(w, java.util.Map.of("resonance", List.of(TEAMMATE_B, Kindling.TRIAL_RESONANCE))));
    }
    @Test void theBonfireGrowsWithTheWholeWeb() {
        var loner = Leaf.classic(1, 0); loner.setFlag(Kindling.UNLOCK_FLAG, true);
        var befriended = Leaf.classic(1, 0); befriended.setFlag(Kindling.UNLOCK_FLAG, true);
        loner.bond(TEAMMATE_A).meet(0); loner.bond(TEAMMATE_A).level = 6;
        for (String c : List.of(TEAMMATE_A, TEAMMATE_B, SENSEI, RIVAL, CLASSMATE_C, CLASSMATE_D, INSTRUCTOR, MEDIC)) {
            befriended.bond(c).meet(0); befriended.bond(c).level = 9;
            for (int i = 0; i < 40; i++) befriended.act(c, Act.BOND_MOMENT);
        }
        var small = Kindling.bonfire(loner); var big = Kindling.bonfire(befriended);
        assertEquals("candle", small.form(), "a loner gets a candle");
        assertTrue(big.strength() > small.strength() * 5);
        assertNotEquals("candle", big.form());
        assertEquals(8, big.bonds());
        assertFalse(big.lit(), "the story lights it");
        befriended.setFlag(Kindling.BONFIRE_FLAG, true);
        assertTrue(Kindling.bonfire(befriended).lit());
        assertTrue(BondConditions.test(befriended, java.util.Map.of("bonfire", "campfire")));
    }
    @Test void anEmberLinkJoinsTheSquadAtFlame() {
        var w = Leaf.classic(1, 0); w.setFlag(Kindling.UNLOCK_FLAG, true);
        w.formSquad("squad:7", SENSEI, TEAMMATES, List.of());
        w.bond(TEAMMATE_A).level = 8; w.bond(TEAMMATE_B).level = 6;
        assertEquals(List.of(TEAMMATE_A), Kindling.emberLink(w));
    }
    @Test void theBookRevealsWhatYouKnowAsTheBondDeepens() {
        var w = Leaf.classic(8, 0);
        w.talk(RIVAL);
        var page = BondBook.page(w, RIVAL);
        assertTrue(page.facts().getFirst().known(), "who they are");
        assertEquals("uchiha,academy", page.facts().getFirst().value());
        assertFalse(page.facts().stream().filter(f -> f.key().equals("bond.fact.dream")).findFirst().orElseThrow().known());
        w.reveal(RIVAL, "dream");
        var dream = BondBook.page(w, RIVAL).facts().stream().filter(f -> f.key().equals("bond.fact.dream")).findFirst().orElseThrow();
        assertTrue(dream.known());
        assertEquals("surpass_a_rival", dream.value());
        assertTrue(BondConditions.test(w, java.util.Map.of("knows_fact", List.of(RIVAL, "dream"))));
    }
    @Test void theBookShowsFeelingsMemoriesAndWhatComesNext() {
        var w = Leaf.classic(8, 0);
        w.act(RIVAL, Act.SPAR_WON); w.act(RIVAL, Act.SPAR_WON); w.act(RIVAL, Act.SAVED_LIFE);
        var page = BondBook.page(w, RIVAL);
        assertTrue(page.feelings().get("rivalry").startsWith("bond.feel.rivalry."));
        assertEquals(List.of("bond.memory.saved_life"), page.kept().stream().map(BondBook.MemoryLine::key).toList());
        assertTrue(page.recent().stream().anyMatch(l -> l.key().equals("bond.memory.spar_won")));
        assertTrue(page.goal().startsWith("bond.goal."));
        assertEquals("", page.romance(), "nothing to show");
        assertEquals("bond.kindling.none", page.kindling());
        assertEquals(2, page.experiences().get("spar"), "two spars folded into one memory, but both count as experiences");
        assertEquals(1, w.bond(RIVAL).memories().stream().filter(m -> m.act() == Act.SPAR_WON).count());
    }
    @Test void aSecretCrushStaysHiddenUntilTheyWouldTellYou() {
        var w = Leaf.classic(8, 0);
        var b = w.bond(TEAMMATE_A);
        b.romance = Courtship.Stage.CRUSH; b.level = 6;
        assertEquals("", BondBook.page(w, TEAMMATE_A).romance());
        b.level = 8;
        assertEquals("bond.romance.crush", BondBook.page(w, TEAMMATE_A).romance());
    }
    static BondWorld squadFriends(int days) {
        var w = Leaf.classic(31, 0);
        var pair = List.of(TEAMMATE_A, TEAMMATE_B);
        for (int d = 0; d < days; d++) {
            for (String t : pair) w.talk(t);
            w.experience(Act.TRAINED_TOGETHER, pair);
            if (d % 3 == 0) w.experience(Act.MISSION_TOGETHER, pair);
            if (d % 10 == 5) for (String t : pair) w.moment(t, "bond.test." + d);
            w.endDay();
        }
        w.setFlag(Kindling.UNLOCK_FLAG, true);
        return w;
    }
    @Test void threadSightReadsOnlyCloseBondsAndShowsThatSomethingIsHiddenNeverWhat() {
        var w = squadFriends(150);
        w.bond(RIVAL).meet(0);
        assertTrue(w.effectiveLevel(TEAMMATE_A) >= 6 && w.effectiveLevel(TEAMMATE_B) >= 6, w.effectiveLevel(TEAMMATE_A) + " " + w.effectiveLevel(TEAMMATE_B) + " " + w.bond(TEAMMATE_A).conflict().state());
        w.setBondFlag(TEAMMATE_B, Kindling.HIDING + "something");
        var sight = Kindling.threadSight(w);
        assertEquals(List.of(new Kindling.Read(TEAMMATE_A, false), new Kindling.Read(TEAMMATE_B, true)), sight.people(), "the rival is below 6: unreadable");
        assertEquals(1, sight.threads().size());
        var t = sight.threads().getFirst();
        assertEquals(List.of(TEAMMATE_A, TEAMMATE_B), List.of(t.a(), t.b()));
        assertTrue(t.level() > 0 && !t.strained());
        w.setFlag(Kindling.UNLOCK_FLAG, false);
        assertTrue(Kindling.threadSight(w).people().isEmpty(), "asleep until the story awakens it");
    }
    @Test void anOfferedFlameKindlesSomeoneBelowSpark() {
        var w = Leaf.classic(3, 0);
        w.setFlag(Kindling.UNLOCK_FLAG, true);
        w.bond(CLASSMATE_C).meet(0);
        assertEquals(Tier.NONE, Kindling.tier(w, CLASSMATE_C));
        assertEquals(Tier.NONE, w.kindle(CLASSMATE_C).tier());
        w.act(CLASSMATE_C, Act.OFFERED_FLAME);
        assertTrue(w.bond(CLASSMATE_C).moments().stream().anyMatch(m -> m.startsWith("offered_flame")), "a moment, kept");
        assertEquals(Tier.SPARK, Kindling.tier(w, CLASSMATE_C));
        assertTrue(Kindling.strength(w, CLASSMATE_C) > 0);
        w.act(CLASSMATE_D, Act.GAVE_FLAME);
        assertTrue(w.bond(CLASSMATE_D).remembers(Act.GAVE_FLAME));
    }
    @Test void aScriptedBeatCountsItsTargetAtAFloorTierForThatKindleOnly() {
        var w = Leaf.classic(3, 0);
        w.setFlag(Kindling.UNLOCK_FLAG, true);
        w.bond(TEAMMATE_A).meet(0);
        assertEquals("", BondEffects.apply(w, java.util.Map.of("kindle", java.util.Map.of("who", TEAMMATE_A, "floor", "flame"))));
        assertEquals(1, w.bond(TEAMMATE_A).kindled());
        assertEquals(1, w.bond(TEAMMATE_A).resonance());
        assertEquals(Tier.NONE, Kindling.tier(w, TEAMMATE_A), "the floor lasts for that scene only");
        assertEquals("no_bond", BondEffects.apply(w, java.util.Map.of("kindle", TEAMMATE_A)));
    }
    @Test void aRoleCanBeHeldAtALevelUntilAStoryFlag() {
        var w = Leaf.classic(31, 0);
        assertEquals("", BondEffects.apply(w, java.util.Map.of("level_cap", List.of(TEAMMATE_B, 4, "story.test.done"))));
        for (int d = 0; d < 90; d++) {
            w.talk(TEAMMATE_B); w.experience(Act.TRAINED_TOGETHER, List.of(TEAMMATE_B));
            if (d % 3 == 0) w.experience(Act.MISSION_TOGETHER, List.of(TEAMMATE_B));
            if (d % 10 == 5) w.moment(TEAMMATE_B, "bond.test." + d);
            w.endDay();
        }
        assertEquals(4, w.level(TEAMMATE_B));
        assertEquals("bond.goal.held", BondBook.goal(w, TEAMMATE_B));
        w.setFlag("story.test.done", true);
        w.talk(TEAMMATE_B); w.endDay();
        assertTrue(w.level(TEAMMATE_B) > 4, "free once the story moves on");
    }
    @Test void combatSeesAQuarrelAsOneTierLower() {
        var w = TogetherTest.friends(TEAMMATE_B, 150);
        w.setFlag(Kindling.UNLOCK_FLAG, true);
        var calm = Kindling.combatTier(w, TEAMMATE_B);
        assertTrue(calm.compareTo(Tier.SPARK) >= 0, "level " + w.level(TEAMMATE_B));
        w.quarrel(TEAMMATE_B, Act.QUARREL);
        assertEquals(Tier.values()[calm.ordinal() - 1], Kindling.combatTier(w, TEAMMATE_B));
    }
    @Test void aScriptedThreadShowsBelowLevelSixUntilItsFlag() {
        var w = Leaf.classic(3, 0);
        w.setFlag(Kindling.UNLOCK_FLAG, true);
        w.bond(RIVAL).meet(0);
        assertTrue(Kindling.threadSight(w).people().isEmpty());
        assertEquals("", BondEffects.apply(w, java.util.Map.of("thread", java.util.Map.of("who", RIVAL, "floor", "spark", "style", "one_sided", "until", "story.test.seen"))));
        assertEquals(List.of(new Kindling.Read(RIVAL, false, "one_sided")), Kindling.threadSight(w).people());
        w.setFlag("story.test.seen", true);
        assertTrue(Kindling.threadSight(w).people().isEmpty(), "gone once the beat has passed");
    }
}
