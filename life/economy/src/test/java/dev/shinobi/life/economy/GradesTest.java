package dev.shinobi.life.economy;

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

class GradesTest {
    final Grades grades = new Grades(Data.catalogue());

    @Test void masteryClimbsWithCrafts() {
        assertEquals(0, grades.mastery(0));
        assertEquals(1, grades.mastery(5));
        assertEquals(5, grades.mastery(500));
    }

    @Test void practiceMakesBetterBlades() {
        assertEquals(0, grades.fineChance(100, 0, true), 1e-9, "difficulty 0 is always standard");
        assertTrue(grades.fineChance(70, 2, false) > grades.fineChance(0, 2, false));
        assertTrue(grades.fineChance(15, 1, true) > grades.fineChance(15, 1, false));
        assertEquals(0, grades.masterworkChance(14, 3, true), 1e-9, "no masterwork before mastery 3");
        assertTrue(grades.masterworkChance(120, 3, true) > 0);
    }

    @Test void gradesRollFromTheStreamAndRespectTheStation() {
        assertEquals(grades.roll(5, "p", "smithy", 40, 2, true, "masterwork"), grades.roll(5, "p", "smithy", 40, 2, true, "masterwork"));
        int fineOrBetter = 0, masterwork = 0;
        for (int n = 0; n < 2000; n++) {
            String home = grades.roll(5, "p", "smithy", 120 + n, 3, true, "fine");
            assertNotEquals("masterwork", home, "the small forge stops at fine");
            String shop = grades.roll(5, "p", "smithy", 120 + n, 3, true, "masterwork");
            if (!shop.equals("standard")) fineOrBetter++;
            if (shop.equals("masterwork")) masterwork++;
        }
        assertTrue(masterwork > 0 && masterwork < fineOrBetter);
    }

    @Test void repairsCostAShareOfThePrice() {
        assertEquals(33, grades.repairCost("tanto", "standard", 0.5));
        assertEquals(50, grades.repairCost("tanto", "masterwork", 0.5));
        assertEquals(0, grades.repairCost("tanto", "standard", 0));
        assertEquals(2.0, grades.durability("masterwork"), 1e-9);
    }
}
