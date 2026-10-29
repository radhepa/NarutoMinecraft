package dev.shinobi.life.home;

import static org.junit.jupiter.api.Assertions.*;

import dev.shinobi.life.home.Comfort.Tier;
import org.junit.jupiter.api.Test;

class ComfortTest {
    static Home leafFlat() {
        var h = new Home("player", Flat.CLASSIC);
        for (String id : Catalog.set("leaf").pieces()) if (!h.has(id)) assertEquals("ok", h.place(id), id);
        return h;
    }
    static Comfort.Score score(Home h) { return Comfort.of(h, 0, 0, ""); }

    @Test void theFlatStartsBareButNearlyCosy() {
        var s = score(new Home("player", Flat.CLASSIC));
        assertEquals(Tier.BARE, s.tier());
        assertTrue(s.comfort() >= 7, "a futon, a table and a cupboard: " + s.comfort());
        assertEquals(1, s.sets(), "the futon and the low table are two of the Leaf set");
    }
    @Test void theLeafSetMakesItComfortable() {
        var s = score(leafFlat());
        assertEquals(Tier.COMFORTABLE, s.tier(), "comfort " + s.comfort());
        assertTrue(s.perk(FurnitureSet.HOME_SWEET_HOME));
        assertEquals(5, s.sets());
    }
    @Test void piecesOfOneKindDiminish() {
        var one = new Home("player", Flat.CLASSIC); one.place("floor_cushion");
        var many = new Home("player", Flat.CLASSIC); for (int i = 0; i < 6; i++) many.place("floor_cushion");
        double gainOne = score(one).pieces() - score(new Home("player", Flat.CLASSIC)).pieces();
        double gainMany = score(many).pieces() - score(new Home("player", Flat.CLASSIC)).pieces();
        assertTrue(gainMany < 6 * gainOne * .6, "six cushions are not six times one: " + gainMany);
        assertEquals(score(one).style(), score(many).style(), "a copy adds no style");
    }
    @Test void theFlatHoldsSoMuchComfortAndRunsOutOfFloor() {
        var h = leafFlat();
        String last = "ok";
        for (int i = 0; i < 40 && last.equals("ok"); i++) last = h.place(i % 2 == 0 ? "kotatsu" : "zabuton_pair");
        assertEquals("no_room", last);
        assertTrue(Comfort.of(h, 0, 3, "").comfort() <= Flat.Tier.ACADEMY_FLAT.cap);
    }
    @Test void messCostsALittleAndNoMore() {
        var h = leafFlat();
        double clean = score(h).comfort();
        h.mess(99, "guests");
        var messy = score(h);
        assertEquals(Home.MAX_MESS, h.mess());
        assertTrue(messy.messPenalty() <= Comfort.MESSY_MAX && messy.messPenalty() <= clean * Comfort.MESSY_SHARE + 1e-9);
        h.clean();
        assertEquals(clean, score(h).comfort(), 1e-9);
    }
    @Test void aKotatsuIsBestInWinter() {
        var h = new Home("player", Flat.CLASSIC); h.place("kotatsu");
        assertTrue(Comfort.of(h, 0, 3, "").comfort() > Comfort.of(h, 0, 1, "").comfort());
    }
    @Test void clanPiecesComfortTheirOwnClan() {
        var h = new Home("player", Flat.CLASSIC);
        for (String id : Catalog.set("clan.nara").pieces()) h.place(id);
        assertEquals(2, Comfort.of(h, 0, 0, "nara").sets() - 1);
        assertEquals(0, Comfort.of(h, 0, 0, "").sets() - 1);
    }
    @Test void keepsakesAndPhotosAddStyle() {
        var h = new Home("player", Flat.CLASSIC);
        h.place("keepsake_shelf"); h.place("photo_frame");
        double before = score(h).style();
        h.keep(Catalog.KEEPSAKES.get("framed_ladle"));
        assertEquals("ok", h.display("framed_ladle"));
        h.photo("photo.class", 3, java.util.List.of("role:teammate_a"), "child");
        assertEquals("ok", h.hang("photo.class"));
        assertEquals(before + 2, score(h).style(), 1e-9);
    }
    @Test void aPetAndACaredForPlantAddComfort() {
        var h = new Home("player", Flat.CLASSIC);
        double base = score(h).comfort();
        h.place("houseplant"); h.place("pet_bed"); h.pet("cat"); h.plant.water(0);
        assertTrue(score(h).extras() >= 3);
        assertTrue(score(h).comfort() > base + 3);
    }
}
