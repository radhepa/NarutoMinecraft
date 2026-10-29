package dev.shinobi.combat;

import static org.junit.jupiter.api.Assertions.*;

import java.util.List;
import org.junit.jupiter.api.Test;

class SignsTest {
    static final List<HandSign> FIREBALL = HandSign.sequence("snake ram monkey boar horse tiger");
    static final List<HandSign> CLONE = HandSign.sequence("ram snake tiger");

    @Test void typedKeysAndTheRadialWheelReachEverySign() {
        assertEquals(HandSign.RAT, HandSign.byKey("1"));
        assertEquals(HandSign.BOAR, HandSign.byKey("="));
        assertNull(HandSign.byKey("q"));
        assertEquals(HandSign.RAT, HandSign.radial(0, 1), "top");
        assertEquals(HandSign.HARE, HandSign.radial(1, 0), "right, three spokes round");
        assertEquals(HandSign.HORSE, HandSign.radial(0, -1), "bottom");
        assertEquals(HandSign.BIRD, HandSign.radial(-1, 0), "left, nine spokes round");
        assertNull(HandSign.radial(0.1, 0.1), "dead zone");
        for (int i = 0; i < 12; i++) {
            double a = Math.toRadians(i * 30);
            assertEquals(HandSign.values()[i], HandSign.radial(Math.sin(a), Math.cos(a)));
        }
    }
    @Test void aWeaveCastsTheExactSequenceAndFizzlesOtherwise() {
        var book = new SignBook();
        book.learn("combat:fire.great_fireball", "c", FIREBALL);
        book.learn("combat:nin.clone", "e", CLONE);
        var w = new Weaver(book, 4);
        w.begin(0);
        long t = 0;
        for (var s : CLONE) { assertTrue(w.input(s, t)); t += 4; }
        var r = w.release(t);
        assertEquals(Weaver.Outcome.CAST, r.outcome());
        assertEquals("combat:nin.clone", r.technique().orElseThrow());
        assertEquals(12, r.ticks());

        w.begin(100);
        w.input(HandSign.RAM, 100);
        w.input(HandSign.DOG, 104);
        assertEquals(Weaver.Outcome.FIZZLE, w.release(108).outcome());

        w.begin(200);
        w.input(HandSign.RAM, 200);
        w.interrupt();
        assertEquals(Weaver.Outcome.INTERRUPTED, w.release(204).outcome());
    }
    @Test void earlyInputsAreBufferedNotDropped() {
        var book = new SignBook();
        book.learn("combat:nin.clone", "e", CLONE);
        var w = new Weaver(book, 4);
        w.begin(0);
        assertTrue(w.input(HandSign.RAM, 0));
        assertFalse(w.input(HandSign.SNAKE, 1), "far too early: dropped");
        assertTrue(w.input(HandSign.SNAKE, 2), "two ticks early: buffered");
        assertTrue(w.input(HandSign.TIGER, 8));
        assertEquals("combat:nin.clone", w.release(12).technique().orElseThrow());
    }
    @Test void thePrefixHintNarrowsAsYouWeave() {
        var book = new SignBook();
        book.learn("combat:nin.clone", "e", CLONE);
        book.learn("combat:nin.transformation", "e", HandSign.sequence("dog boar ram"));
        book.learn("combat:nin.shadow_clone", "b", HandSign.sequence("ram snake tiger ram"));
        assertEquals(List.of("combat:nin.clone", "combat:nin.shadow_clone"), book.candidates(List.of(HandSign.RAM)));
        assertEquals(List.of("combat:nin.shadow_clone"), book.candidates(HandSign.sequence("ram snake tiger ram")));
        assertTrue(book.candidates(List.of()).isEmpty());
    }
    @Test void masteryShortensSignsButNeverIntoAmbiguity() {
        var book = new SignBook();
        book.learn("combat:fire.great_fireball", "c", FIREBALL);
        book.learn("combat:nin.hiding", "d", HandSign.sequence("snake rat dog"));
        book.setTier("combat:fire.great_fireball", Mastery.Tier.MASTERED);
        assertEquals(HandSign.sequence("snake ram monkey"), book.sequence("combat:fire.great_fireball"), "half the signs");
        book.learn("combat:test.snake_ram_monkey", "c", HandSign.sequence("snake ram monkey"));
        assertEquals(HandSign.sequence("snake ram monkey boar"), book.sequence("combat:fire.great_fireball"), "lengthened until unique");
        assertEquals("combat:test.snake_ram_monkey", book.match(HandSign.sequence("snake ram monkey")).orElseThrow(), "the exact one wins");
        assertEquals("combat:fire.great_fireball", book.match(HandSign.sequence("snake ram monkey boar")).orElseThrow());
        book.setTier("combat:fire.great_fireball", Mastery.Tier.PERFECTED);
        assertEquals(List.of(), book.sequence("combat:fire.great_fireball"), "perfected C-rank: quick slot, no signs");
    }
    @Test void masteryTiersByRank() {
        assertEquals(Mastery.Tier.NOVICE, Mastery.tier("c", 14));
        assertEquals(Mastery.Tier.PRACTICED, Mastery.tier("c", 15));
        assertEquals(Mastery.Tier.MASTERED, Mastery.tier("c", 50));
        assertEquals(Mastery.Tier.PERFECTED, Mastery.tier("s", 240));
        assertEquals(Mastery.Tier.MASTERED, Mastery.tier("s", 90));
        assertTrue(Mastery.quickSlot(Mastery.Tier.MASTERED));
        assertFalse(Mastery.quickSlot(Mastery.Tier.PRACTICED));
        assertEquals(1, Mastery.signsNeeded(Mastery.Tier.PERFECTED, "s", 8), "S-rank perfected keeps one sign");
    }
    @Test void signSpeedFollowsControlAndRank() {
        assertEquals(4, Weaver.ticksPerSign(30, 1));
        assertEquals(3, Weaver.ticksPerSign(80, 1));
        assertEquals(2, Weaver.ticksPerSign(80, 5));
        assertEquals(2, Weaver.ticksPerSign(100, 10), "never below 2");
    }
}
