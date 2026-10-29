package dev.shinobi.life.bond;

import static dev.shinobi.life.bond.Leaf.*;
import static org.junit.jupiter.api.Assertions.*;

import java.util.ArrayList;
import java.util.List;
import java.util.Map;
import org.junit.jupiter.api.Test;

class GiftsTest {
    @Test void giftsReceivedAreKeptWithGiverDayAndOccasion() {
        var w = Leaf.classic(3, 0);
        var g = Gifts.receive(w, TEAMMATE_B, "item:pet_treat", "thanks");
        w.endDay();
        assertEquals("", BondEffects.apply(w, Map.of("give_player", Map.of("from", TEAMMATE_A, "item", "item:brush", "occasion", "souvenir"))));
        var all = Gifts.received(w);
        assertEquals(2, all.size());
        assertEquals(new Gifts.Received(g.id(), "item:pet_treat", TEAMMATE_B, 0, "thanks", false), all.getFirst());
        assertEquals(List.of(all.get(1)), Gifts.from(w, TEAMMATE_A));
        assertTrue(BondConditions.test(w, Map.of("gifts_from", List.of(TEAMMATE_B, 1))));
        assertThrows(IllegalArgumentException.class, () -> Gifts.receive(w, TEAMMATE_B, "x", "because"));
    }
    @Test void aGiverSeeingTheirGiftDisplayedIsWarmedOnce() {
        var w = TogetherTest.friends(TEAMMATE_B, 30);
        var g = Gifts.receive(w, TEAMMATE_B, "item:pet_treat", "birthday");
        double before = w.meters(TEAMMATE_B).affection();
        assertTrue(Gifts.seenDisplayed(w, g.id()));
        assertTrue(w.meters(TEAMMATE_B).affection() > before);
        assertTrue(w.bond(TEAMMATE_B).remembers(Act.SAW_GIFT_DISPLAYED));
        assertFalse(Gifts.seenDisplayed(w, g.id()), "once per gift");
        assertTrue(Gifts.gift(w, g.id()).orElseThrow().seen());
        assertFalse(Gifts.seenDisplayed(w, 999));
    }
    @Test void kindredSpiritsLeaveSmallGiftsOfTheirFavoriteThings() {
        var w = Leaf.classic(3, 0);
        w.bond(TEAMMATE_B).meet(0); w.bond(TEAMMATE_B).floor = 9; w.bond(TEAMMATE_B).level = 9;
        w.bond(RIVAL).meet(0); w.bond(RIVAL).level = 5;
        w.advance(70);
        var fromB = Gifts.from(w, TEAMMATE_B);
        assertTrue(fromB.size() >= 4 && fromB.size() <= 18, "about one a week: " + fromB.size());
        assertTrue(fromB.stream().allMatch(r -> r.occasion().equals("kindred") && w.person(TEAMMATE_B).personality().loves().contains(r.item())));
        assertTrue(Gifts.from(w, RIVAL).isEmpty(), "only kindred spirits");
        var back = SaveFormat.read(SaveFormat.write(w), w.seed(), new ArrayList<>(w.people()));
        assertEquals(Gifts.received(w), Gifts.received(back));
    }
    @Test void aKeepsakeOrPhotoOnShowIsNoticedOnceAndLeavesAFlag() {
        var w = TogetherTest.friends(TEAMMATE_B, 30);
        var g = Gifts.receive(w, TEAMMATE_B, "item:pet_treat", "birthday");
        assertTrue(Gifts.noticed(w, TEAMMATE_B, "item:pet_treat", false));
        assertTrue(Gifts.gift(w, g.id()).orElseThrow().seen(), "a gift from the ledger is marked seen");
        assertFalse(Gifts.noticed(w, TEAMMATE_B, "item:pet_treat", false), "once per keepsake");
        assertTrue(Gifts.noticed(w, TEAMMATE_B, "photo.academy_graduation", true));
        assertTrue(w.bond(TEAMMATE_B).remembers(Act.SAW_PHOTO_TOGETHER));
        assertTrue(BondConditions.test(w, Map.of("bond_flag", List.of(TEAMMATE_B, "home.noticed:photo.academy_graduation"))));
        w.setBondFlag(TEAMMATE_B, "home.key");
        assertTrue(BondConditions.test(w, Map.of("bond_flag", List.of(TEAMMATE_B, "home.key"))));
        w.clearBondFlag(TEAMMATE_B, "home.key");
        assertFalse(BondConditions.test(w, Map.of("bond_flag", List.of(TEAMMATE_B, "home.key"))), "a key taken back quietly");
    }
    @Test void homeHangoutsAreHostedAtThePlayersHome() {
        for (String id : List.of("study_night", "cook_together", "balcony_stargazing", "squad_crash", "tea_at_home", "home_dinner"))
            assertEquals("home:player", Activity.of(id).placeFor("player"));
        assertTrue(Activity.of("balcony_stargazing").open(0, 23));
        assertFalse(Activity.of("tea_at_home").open(0, 21));
        assertTrue(Act.VISITED_HOME.experience != null, "a visit counts as time spent together");
    }
}
