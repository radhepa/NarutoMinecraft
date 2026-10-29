package dev.shinobi.life.home;

import static org.junit.jupiter.api.Assertions.*;

import java.util.List;
import org.junit.jupiter.api.Test;

class MoveTest {
    @Test void everyHomeKeepsABed() {
        var h = new Home("player", Flat.CLASSIC);
        assertEquals("last_bed", h.remove("futon"));
        assertEquals("ok", h.place("thick_futon").equals("too_many_beds") ? "ok" : "unexpected");
        assertEquals("fixed", h.remove("window"));
        assertEquals("fixed", h.place("mailbox"));
    }
    @Test void aLoftHasNoBalcony() {
        var loft = new Home("player", Flat.of("flat.market_loft.4"));
        assertEquals("balcony", loft.place("wind_chime"));
        assertEquals("ok", loft.place("houseplant"));
    }
    @Test void movingTakesEverythingAlong() {
        var h = ComfortTest.leafFlat();
        h.place("photo_frame"); h.place("houseplant"); h.place("pet_bed"); h.pet("ninken");
        h.keep(Catalog.KEEPSAKES.get("shogi_board")); h.display("shogi_board");
        h.photo("photo.squad", 30, List.of("role:teammate_a", "role:teammate_b", "role:sensei"), "child"); h.hang("photo.squad");
        h.giveKey("role:teammate_b", 6, 40);
        var before = h.placed();
        h.moveTo(Flat.of("flat.leaf_block.5b"));
        assertEquals(before, h.placed());
        assertTrue(h.crates().isEmpty());
        assertEquals(1, h.displayed().size()); assertEquals(1, h.wall().size());
        assertTrue(h.keyHolder("role:teammate_b")); assertTrue(h.petAtHome());
        assertTrue(Comfort.of(h, 0, 0, "").comfort() > 0);
    }
    @Test void whatDoesNotFitStaysInItsCrate() {
        var h = new Home("player", Flat.of("flat.leaf_block.5b"));
        for (int i = 0; i < 12; i++) h.place("kotatsu");
        h.moveTo(Flat.CLASSIC);
        assertFalse(h.crates().isEmpty());
        assertTrue(h.cellsUsed() <= Flat.CLASSIC.cells());
        h.remove("kotatsu");
        assertEquals("ok", h.unpack("kotatsu"));
    }
    @Test void aSpouseNeedsRoomInTheBed() {
        var h = new Home("player", Flat.of("house.residential.small"));
        assertEquals("needs_bed", h.moveIn("role:spouse"));
        h.remove("futon"); // not allowed: the last bed
        assertEquals("ok", h.place("double_futon"));
        assertEquals("ok", h.moveIn("role:spouse"));
        assertEquals(List.of("player", "role:spouse"), h.residents());
    }
    @Test void keepsakesAndPhotosNeedSomewhereToGo() {
        var h = new Home("player", Flat.CLASSIC);
        var all = Catalog.KEEPSAKES.values().stream().limit(Home.FREE_STANDING + 1).toList();
        for (var k : all) h.keep(k);
        for (int i = 0; i < Home.FREE_STANDING; i++) assertEquals("ok", h.display(all.get(i).id()), "keepsakes stand on their own");
        assertEquals("no_space", h.display(all.getLast().id()));
        assertEquals("not_owned", h.display("lake_lantern"));
        h.place("display_shelf");
        assertEquals("ok", h.display(all.getLast().id()));
        assertEquals("already", h.display(all.getLast().id()));
        assertEquals("no_photo", h.hang("photo.class"));
        h.photo("photo.squad", 30, List.of("role:teammate_a"), "child");
        assertEquals("no_frame", h.hang("photo.squad"));
        h.place("photo_frame");
        assertEquals("ok", h.hang("photo.squad"));
        h.photo("photo.squad", 200, List.of("role:teammate_a"), "teen");
        assertEquals(2, h.wall().getFirst().version(), "the retake hangs; the first goes in the album");
        assertEquals(2, h.album().get("photo.squad").size());
        h.remove("photo_frame");
        assertTrue(h.wall().isEmpty());
    }
}
