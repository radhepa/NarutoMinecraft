package dev.shinobi.life.bond;

import static dev.shinobi.life.bond.Leaf.*;
import static org.junit.jupiter.api.Assertions.*;

import java.util.List;
import org.junit.jupiter.api.Test;

class BondDialogueTest {
    @Test void greetingsGoFromTheMostSpecificPoolToTheLevel() {
        var w = Leaf.classic(4, 0);
        w.talk(RIVAL);
        int level = w.effectiveLevel(RIVAL);
        assertEquals(List.of("bond.greet.level." + level + ".proud", "bond.greet.level." + level), BondDialogue.greeting(w, RIVAL));
        w.quarrel(RIVAL, Act.QUARREL);
        w.endDay();
        var keys = BondDialogue.greeting(w, RIVAL);
        assertEquals("bond.greet.cold_shoulder.proud", keys.getFirst());
        assertEquals("bond.greet.level." + w.effectiveLevel(RIVAL), keys.getLast());
    }
    @Test void theyBringUpWhatTheyHeardOnce() {
        var w = Leaf.classic(4, 0);
        w.act(TEAMMATE_B, Act.SAVED_LIFE, List.of(TEAMMATE_A));
        assertEquals("bond.seen.saved_life", BondDialogue.news(w, TEAMMATE_A).orElseThrow());
        assertTrue(BondDialogue.news(w, TEAMMATE_A).isEmpty(), "said once");
        w.endDay(); w.endDay();
        assertEquals("bond.heard.saved_life", BondDialogue.news(w, CLASSMATE_C).orElseThrow(), "the village heard the next day");
        assertTrue(BondDialogue.news(w, TEAMMATE_B).isEmpty(), "they lived it; nothing to report");
    }
}
