package dev.shinobi.life.home;

import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.Test;

/** Tidiness, the cupboard and the plant: the light, never-punishing parts of living at home. */
class LivingTest {
    @Test void messPilesUpToACapAndOneCleanClearsIt() {
        var h = new Home("player", Flat.CLASSIC);
        assertEquals(Home.Tidiness.TIDY, h.tidiness());
        for (int i = 0; i < 9; i++) h.mess(1, "ramen_cup");
        assertEquals(Home.Tidiness.MESSY, h.tidiness());
        assertEquals(6, h.ramenCups(), "the tower of cups stops at six");
        for (int i = 0; i < 50; i++) h.mess(1, "meal");
        assertEquals(Home.MAX_MESS, h.mess());
        h.clean();
        assertEquals(0, h.mess()); assertEquals(0, h.ramenCups()); assertEquals(1, h.cleanings());
    }
    @Test void milkGoesStaleAndIsStillDrunk() {
        var p = new Pantry();
        p.store("milk", 0, 1);
        var m = p.eat(6, "milk");
        assertEquals("stale", m.freshness());
        assertEquals(0, m.tier());
        assertEquals("home.pantry.stale.milk", m.line());
        p.store("milk", 0, 1);
        assertEquals("very_stale", p.eat(20, null).freshness());
        assertNull(p.eat(20, null), "an empty cupboard is just empty");
    }
    @Test void anIceboxKeepsFoodTwiceAsLong() {
        var h = new Home("player", Flat.CLASSIC);
        assertEquals("ok", h.place("icebox"));
        h.pantry.store("milk", 0, 1);
        assertEquals("fresh", h.pantry.eat(7, "milk").freshness());
        h.remove("icebox");
        assertEquals(4, h.pantry.keeps("milk"));
    }
    @Test void theHungryEatTheOldestFirst() {
        var p = new Pantry();
        p.store("bread", 0, 1); p.store("bread", 5, 1);
        assertEquals("stale", p.eatOldest(9).freshness());
        assertEquals("fresh", p.eatOldest(9).freshness());
    }
    @Test void aWateredPlantGrowsAndAForgottenOneNeverDies() {
        var plant = new Plant();
        for (int d = 0; d < 60; d++) { if (d % 3 == 0) plant.water(d); plant.endDay(d, 1, false); }
        assertEquals(Plant.Stage.GRAND, plant.stage());
        assertEquals(Plant.Look.WILTED, plant.look(80));
        var stage = plant.stage();
        plant.water(80);
        assertEquals(Plant.Look.HEALTHY, plant.look(80));
        assertEquals(stage, plant.stage(), "wilting costs nothing but its looks");
    }
    @Test void seasonsSetThePace() {
        var spring = new Plant(); var winter = new Plant();
        for (int d = 0; d < 28; d++) { spring.water(d); winter.water(d); spring.endDay(d, 0, false); winter.endDay(d, 3, false); }
        assertTrue(spring.growth() > 2.5 * winter.growth());
        assertTrue(spring.flowering(27, 0));
        assertFalse(spring.flowering(27, 2), "no flowers in autumn");
    }
    @Test void practiceAtHomeIsCapped() {
        var h = new Home("player", Flat.CLASSIC); h.place("training_dummy");
        var pr = new Practice();
        var s = ComfortTest.score(h);
        assertEquals(.4, pr.session(h, s, 1, "dummy", 3).credited(), 1e-9);
        assertEquals(0, pr.session(h, s, 1, "dummy", 1).credited(), 1e-9);
        assertTrue(pr.session(h, s, 1, "signs", 1).drill());
        assertFalse(pr.session(h, s, 1, "signs", 1).drill());
        assertEquals(0, pr.session(h, s, 2, "meditate", 1).credited(), 1e-9, "no mat, no meditation corner");
        for (String id : Catalog.set("training").pieces()) h.place(id);
        assertEquals(.6, pr.session(h, ComfortTest.score(h), 3, "dummy", 3).credited(), 1e-9, "the whole set: an hour and a half");
    }
    @Test void theStipendArrivesEveryMorning() {
        var h = new Home("player", Flat.CLASSIC);
        assertEquals(30, h.morning(0));
        assertEquals(30, h.morning(500));
        assertEquals(Mailbox.Kind.STIPEND, h.mailbox.collect().getFirst().kind());
    }
    @Test void chestsArePlainStorageAndMoreComeWithFurniture() {
        var h = new Home("player", Flat.CLASSIC);
        assertEquals(27, h.storageSlots(), "the starting chest");
        h.place("barrel"); h.place("storage_chest");
        assertEquals(81, h.storageSlots());
    }
}
