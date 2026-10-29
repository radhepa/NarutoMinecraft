package dev.shinobi.combat;

import static org.junit.jupiter.api.Assertions.*;

import dev.shinobi.combat.ComboMachine.Context;
import java.util.List;
import org.junit.jupiter.api.Test;

class ComboAndStatusTest {
    static final CombatData DATA = CombatData.load();

    @Test void theAcademyChainIsThreeLightsAboutSixTicksApartThenARecovery() {
        var m = new ComboMachine(DATA.moveset("combat:style.academy_basics"));
        var ctx = Context.ground(1, 0);
        var a = m.press("L", 0, ctx);
        assertEquals("jab", a.move().id());
        var b = m.press("L", a.activeEnd(), ctx);
        assertEquals("cross", b.move().id());
        assertTrue(b.chained());
        assertEquals(4, b.start() - a.start(), "the chain lands every few ticks");
        var c = m.press("L", b.activeEnd(), ctx);
        assertEquals("roundhouse", c.move().id());
        assertTrue(c.move().ender());
        assertEquals(1.5, Json.num(c.move().effects(), "knockback", 0), "the third knocks back");
        assertNull(m.press("L", c.activeEnd() + 1, ctx), "no fourth hit; recovering");
        assertEquals("jab", m.press("L", c.end(), ctx).move().id(), "a new string after the 10-tick recovery");
    }
    @Test void earlyInputsBufferAndLateOnesDropTheChain() {
        var m = new ComboMachine(DATA.moveset("combat:style.academy_basics"));
        var ctx = Context.ground(1, 0);
        var a = m.press("L", 0, ctx);
        var b = m.press("L", a.windowOpen() - 2, ctx);
        assertNotNull(b);
        assertEquals(a.windowOpen(), b.start(), "held until the window opens");
        var m2 = new ComboMachine(DATA.moveset("combat:style.academy_basics"));
        var x = m2.press("L", 0, ctx);
        var late = m2.press("L", x.windowClose() + 1, ctx);
        assertEquals("jab", late.move().id(), "past the window: a new string");
        assertFalse(late.chained());
    }
    @Test void launchersAndFinishersAreGatedByTierAndMomentum() {
        var m = new ComboMachine(DATA.moveset("combat:style.academy_basics"));
        var a = m.press("L", 0, Context.ground(1, 0));
        var b = m.press("L", a.activeEnd(), Context.ground(1, 0));
        var c = m.press("H", b.activeEnd(), Context.ground(1, 0));
        assertEquals("launcher", c.move().id());
        assertTrue(c.move().launches());
        var style = DATA.moveset("combat:style.academy_basics");
        assertNull(style.find(List.of("L", "L", "L", "H"), 1, 100, 0), "palm rush needs tier 2");
        assertNull(style.find(List.of("L", "L", "L", "H"), 2, 59, 0), "and 60 momentum");
        assertEquals("palm_rush", style.find(List.of("L", "L", "L", "H"), 2, 60, 0).id());
    }
    @Test void stylesBuildOnAcademyTaijutsu() {
        var sf = DATA.moveset("combat:style.strong_fist");
        assertEquals("leaf_hurricane", sf.find(List.of("L", "L", "L"), 1, 0, 0).id(), "Strong Fist replaces the roundhouse");
        assertEquals("heavy", sf.find(List.of("H"), 1, 0, 0).id(), "and keeps the Academy heavy");
        assertEquals("air_spike", sf.find(List.of("J", "L", "L", "H"), 3, 100, 0).id(), "without the first gate, no Primary Lotus: the Academy air spike");
        assertEquals("primary_lotus", sf.find(List.of("J", "L", "L", "H"), 3, 100, 1).id());
        assertEquals("morning_peacock", sf.find(List.of("L", "L", "L", "H"), 5, 100, 6).id(), "the highest tier on a path wins");
        var sword = DATA.moveset("combat:style.crescent_moon");
        assertEquals("arc_1", sword.find(List.of("L"), 1, 0, 0).id());
        assertFalse(sword.strings("", 1, 0, 0).isEmpty());
    }
    @Test void everyStyleHasAPlayableTree() {
        for (var id : DATA.styles.keySet()) {
            var s = DATA.moveset(id);
            assertFalse(s.strings("", 5, 100, 6).isEmpty() && s.strings("D", 5, 100, 6).isEmpty() && s.strings("G", 5, 100, 6).isEmpty(), id);
            for (var mv : s.all()) {
                assertTrue(mv.windowClose() >= mv.windowOpen(), id + " " + mv.id());
                assertTrue(mv.length() > 0 || mv.input().contains("P"), id + " " + mv.id());
            }
        }
    }
    @Test void statusesStunStackCleanseAndDiminish() {
        var s = new StatusEffects(DATA.statuses, false);
        assertEquals(20, s.apply("stunned", 0, 0));
        assertTrue(s.stunned());
        assertFalse(s.canCast());
        assertEquals(10, s.apply("stunned", 20, 10), "the second stun in 15 s lasts half");
        assertEquals(5, s.apply("stunned", 20, 20));
        assertEquals(0, s.apply("stunned", 20, 30), "the fourth not at all");
        assertEquals(20, s.apply("stunned", 20, 400), "the window passes");
        var t = new StatusEffects(DATA.statuses, false);
        t.apply("burning", 0, 0);
        assertTrue(t.tick() > 0, "burning hurts");
        t.apply("soaked", 0, 1);
        assertFalse(t.has("burning"), "water puts it out");
        assertEquals(1.3, t.takenMult("ninjutsu.lightning"), 1e-9);
        var n = new StatusEffects(DATA.statuses, false);
        n.apply("numbed", 0, 0);
        n.apply("numbed", 0, 1);
        n.apply("numbed", 0, 2);
        assertTrue(n.has("paralysed"), "three numbing stacks paralyse");
        var boss = new StatusEffects(DATA.statuses, true);
        assertEquals(10, boss.apply("stunned", 20, 0), "bosses take half");
        assertEquals(5, boss.apply("stunned", 20, 5));
        assertEquals(0, boss.apply("stunned", 20, 6), "and are immune after the second");
        var sleep = new StatusEffects(DATA.statuses, false);
        sleep.apply("asleep", 0, 0);
        sleep.damaged();
        assertFalse(sleep.has("asleep"), "damage wakes");
    }
    @Test void rangeBandsSteerTheBrain() {
        assertEquals(RangeBands.Band.CLOSE, RangeBands.of(2));
        assertEquals(RangeBands.Band.MID, RangeBands.of(6));
        assertEquals(RangeBands.Band.FAR, RangeBands.of(30));
        assertEquals(-1, RangeBands.step(RangeBands.Band.CLOSE, 8));
        assertEquals(1, RangeBands.step(RangeBands.Band.FAR, 4));
        assertEquals(0, RangeBands.step(RangeBands.Band.MID, 5));
    }
}
