package dev.shinobi.life.home;

import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.Test;

class RentTest {
    @Test void offByDefaultTheAcademyFlatIsFree() {
        var r = new Rent(false);
        assertEquals(0, r.weekly(1, Flat.CLASSIC));
        assertEquals(0, r.weekDue(1, Flat.CLASSIC, 0, 0).asked());
        assertEquals(Rent.CHUNIN_FLAT_WEEKLY, r.weekly(2, Flat.of("flat.leaf_block.5b")), "the Chunin flat is rented either way");
    }
    @Test void whenOnTheLandladyForgivesOneLateWeekASeason() {
        var r = new Rent(true);
        assertEquals(0, r.weekly(0, Flat.CLASSIC), "the stipend covers the Academy years");
        assertEquals("home.landlady.thanks", r.weekDue(1, Flat.CLASSIC, 0, 80).note());
        var late = r.weekDue(1, Flat.CLASSIC, 0, 10);
        assertTrue(late.forgiven());
        assertEquals(0, r.owed());
        var again = r.weekDue(1, Flat.CLASSIC, 0, 10);
        assertFalse(again.forgiven());
        assertEquals(40, r.owed());
        assertEquals(90, r.weekDue(1, Flat.CLASSIC, 0, 0).owed(), "it carries over; nothing is taken");
        assertEquals(0, r.weekDue(1, Flat.CLASSIC, 0, 500).owed());
        assertTrue(r.weekDue(1, Flat.CLASSIC, 1, 0).forgiven(), "a new season, a new grace");
    }
}
