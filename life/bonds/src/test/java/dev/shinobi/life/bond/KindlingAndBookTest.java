package dev.shinobi.life.bond;

import static dev.shinobi.life.bond.Leaf.*;
import static org.junit.jupiter.api.Assertions.*;

import dev.shinobi.life.bond.Kindling.Tier;
import java.util.List;
import org.junit.jupiter.api.Test;

class KindlingAndBookTest {
    @Test void kindlingFollowsTheRoadmapThresholds() {
        assertEquals(Tier.NONE, Kindling.tier(false, 10, true, Conflict.NONE), "locked until the story unlocks it");
        assertEquals(Tier.NONE, Kindling.tier(true, 5, false, Conflict.NONE));
        assertEquals(Tier.NATURE, Kindling.tier(true, 6, false, Conflict.NONE));
        assertEquals(Tier.TECHNIQUE, Kindling.tier(true, 8, false, Conflict.NONE));
        assertEquals(Tier.FULL, Kindling.tier(true, 10, false, Conflict.NONE));
        assertEquals(Tier.FULL, Kindling.tier(true, 8, true, Conflict.NONE), "teammates, sensei and spouse: full from 8");
        assertEquals(Tier.NATURE, Kindling.tier(true, 7, true, Conflict.NONE));
        var quarrel = Conflict.NONE.hurt(Act.QUARREL, 20, Personality.of("steadfast", ""), 0);
        assertEquals(Tier.NONE, Kindling.tier(true, 10, true, quarrel), "a quarrel puts the flame out");
        assertTrue(Kindling.grant(Tier.FULL).duration() > Kindling.grant(Tier.NATURE).duration());
        assertEquals(0, Kindling.grant(Tier.NATURE).techniqueUses());
        assertEquals(1, Kindling.grant(Tier.TECHNIQUE).techniqueUses());
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
}
