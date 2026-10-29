package dev.shinobi.life.home.sim;

import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.Test;

/** The home's pacing over the beta holds across seeds (the numbers are in docs/HOME.md, "Pacing"). */
class FirstFifteenHoursTest {
    @Test void aTypicalPlayersHomeGrowsWithThem() {
        for (long seed = 1; seed <= 5; seed++) {
            var r = FirstFifteenHours.run(seed);
            var byDay = new java.util.TreeMap<Integer, FirstFifteenHours.Snapshot>();
            for (var s : r.comfort()) byDay.put(s.day(), s);
            assertTrue(byDay.get(0).comfort() < 20, "a bare flat on the first day, seed " + seed);
            assertTrue(byDay.get(12).comfort() >= 20, "comfortable by graduation, seed " + seed);
            assertTrue(byDay.get(45).comfort() >= 38, "homely by the results, seed " + seed);
            assertTrue(byDay.get(45).comfort() < 60, "the Academy flat's top is never reached in the beta, seed " + seed);
            assertTrue(byDay.get(12).perks().contains("home_sweet_home"), "the Leaf set within the Academy weeks, seed " + seed);
            int visits = 0, nightsHome = 0;
            for (var s : r.slices()) { visits += s.visits().values().stream().mapToInt(Integer::intValue).sum(); nightsHome += s.nightsHome(); }
            double perWeek = visits * 7.0 / FirstFifteenHours.DAYS;
            assertTrue(perWeek >= 1 && perWeek <= 4, "visits a week " + perWeek + ", seed " + seed);
            assertEquals(FirstFifteenHours.DAYS - 13, nightsHome, "home every night but the away chapters");
            assertTrue(r.staleMeals() <= 20, "stale food is a joke, not a diet: " + r.staleMeals());
        }
    }
    @Test void thereIsAlwaysRoomInTheChests() {
        var r = FirstFifteenHours.run(7);
        assertTrue(r.storageSlots() >= 54, "the starting chest and at least one more: " + r.storageSlots());
    }
}
