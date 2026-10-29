package dev.shinobi.life.bond;

import static org.junit.jupiter.api.Assertions.*;

import java.util.List;
import org.junit.jupiter.api.Test;

class MemoryTest {
    static Memory of(Act act, long day) { return new Memory(act, day, act.base, Reaction.Source.SELF, "", 1); }

    @Test void memoriesFadeByHalfEachHalfLifeAndBigOnesStay() {
        var meal = of(Act.MEAL_TOGETHER, 0);
        assertEquals(1, meal.weight(0), 1e-9);
        assertEquals(.5, meal.weight(Act.MEAL_TOGETHER.halfLife), 1e-9);
        assertEquals(.25, meal.weight(2L * Act.MEAL_TOGETHER.halfLife), 1e-9);
        assertTrue(meal.forgotten(5L * Act.MEAL_TOGETHER.halfLife));
        var saved = of(Act.SAVED_LIFE, 0);
        assertEquals(1, saved.weight(10_000), 1e-9);
        assertFalse(saved.forgotten(10_000));
    }
    @Test void routineFoldsIntoOneMemoryThatSaturates() {
        var w = new BondWorld(1, 0);
        w.add(Leaf.classmate("x", "warmhearted"));
        for (int d = 0; d < 40; d++) { w.act("x", Act.MEAL_TOGETHER); w.endDay(); }
        var meals = w.bond("x").memories().stream().filter(m -> m.act() == Act.MEAL_TOGETHER).toList();
        assertEquals(1, meals.size(), "one living memory of shared meals");
        double one = Reaction.react(w.person("x").personality(), Act.MEAL_TOGETHER).affection();
        assertTrue(meals.getFirst().delta().affection() <= Memory.SATURATION * one + 1e-9, "never more than a few meals' worth");
        assertEquals(40, meals.getFirst().count());
    }
    @Test void secondhandNewsOfTheSameKindFoldsWhoeverItWasAbout() {
        var m = new Memory(Act.HELPED_RESIDENT, 0, Meters.of(1, 1, 0, 0), Reaction.Source.HEARD, "a", 1);
        assertTrue(m.merges(Act.HELPED_RESIDENT, Reaction.Source.HEARD, "b", 5));
        assertFalse(new Memory(Act.HELPED_RESIDENT, 0, Meters.of(1, 1, 0, 0), Reaction.Source.SELF, "a", 1).merges(Act.HELPED_RESIDENT, Reaction.Source.SELF, "b", 5));
        assertFalse(m.merges(Act.HELPED_RESIDENT, Reaction.Source.HEARD, "b", 100), "past its half-life it is a new memory");
    }
    @Test void pruningLetsFadedMemoriesGoAndKeepsBigOnes() {
        var w = new BondWorld(1, 0);
        w.add(Leaf.classmate("x", "warmhearted"));
        w.act("x", Act.SAVED_LIFE);
        var acts = List.of(Act.MEAL_TOGETHER, Act.TRAINED_TOGETHER, Act.STUDIED_TOGETHER, Act.RUDE, Act.BRAGGED);
        for (int d = 0; d < 400; d++) { w.act("x", acts.get(d % acts.size())); if (d % 3 == 0) w.act("x", Act.MISSION_TOGETHER); w.endDay(); }
        var b = w.bond("x");
        assertTrue(b.memories().size() <= Bond.MEMORY_CAP);
        assertTrue(b.remembers(Act.SAVED_LIFE));
        w.advance(400);
        assertTrue(b.memories().stream().allMatch(m -> m.permanent() || m.act() == Act.MISSED_BIRTHDAY || m.act() == Act.FELT_OVERLOOKED),
                "only the big memory outlasts a year of silence (and a friend noticed the forgotten birthday and the unanswered invitations)");
    }
}
