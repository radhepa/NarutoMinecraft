package dev.shinobi.life.economy;

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

class PricesTest {
    final Catalogue c = Data.catalogue();
    final Prices prices = new Prices(c);

    @Test void standingAndFriendshipLowerPricesUpToTheCap() {
        assertEquals(0, prices.discount("newcomer", 0), 1e-9);
        assertEquals(0.05, prices.discount("good_neighbor", 0), 1e-9);
        assertEquals(0.07, prices.discount("good_neighbor", 5), 1e-9);
        assertEquals(0.15, prices.discount("hero", 10), 1e-9);        // 12% + 3%, at the cap
        assertEquals(-0.2, prices.discount("unwelcome", 10), 1e-9);   // friendship does not soften Unwelcome
        assertEquals("pillar", Prices.better("pillar", "helping_hand"));
    }

    @Test void priceFollowsTheShopTheGradeAndTheCustomer() {
        var ichiraku = c.shops.get("ichiraku");
        assertEquals(12, prices.buy("miso_ramen", ichiraku, "standard", "newcomer", 0));
        assertEquals(11, prices.buy("miso_ramen", ichiraku, "standard", "hero", 0));
        assertEquals(14, prices.buy("miso_ramen", ichiraku, "standard", "unwelcome", 0));
        var festival = c.shops.get("festival_stalls");
        assertEquals(Math.round(c.item("yakitori").price() * festival.markup()), prices.buy("yakitori", festival, "standard", "newcomer", 0));
        assertEquals(Math.round(220 * 1.6), prices.buy("tanto", c.shops.get("weapon_shop"), "fine", "newcomer", 0));
        assertEquals(300, prices.buy("technique_scroll@fire.phoenix_flower", c.shops.get("scroll_shop"), "standard", "newcomer", 0));
        assertEquals(3, prices.buy("refreshing_towel", c.shops.get("bath_house"), "standard", "newcomer", 0));
    }

    @Test void clanShopsRefuseTheUnwelcome() {
        assertFalse(prices.serves(c.shops.get("barbecue_house"), "unwelcome"));
        assertTrue(prices.serves(c.shops.get("ichiraku"), "unwelcome"));
    }

    @Test void onlyFurnitureAndLootSellBack() {
        assertEquals(30, prices.sellBack("low_table", "standard"));
        assertEquals(0, prices.sellBack("kunai", "standard"));
        assertEquals(0, prices.sellBack("miso_ramen", "standard"));
        assertEquals(12, prices.sellBack("bandit_trinket", "standard"));
        assertEquals(0, prices.sellBack("keepsake_framed_ladle", "standard"));
    }

    @Test void thePawnShopPaysLessForRepeatsAndRunsOutOfRyo() {
        var pawn = prices.pawn();
        int first = pawn.sell(5, "bandit_trinket", "standard");
        int second = pawn.sell(5, "bandit_trinket", "standard");
        assertEquals(12, first);
        assertTrue(second < first);
        int total = first + second;
        for (int i = 0; i < 100; i++) total += pawn.sell(5, "tansu_chest", "standard");
        assertEquals(400, total);                                   // the day's purse
        assertEquals(0, pawn.sell(5, "low_table", "standard"));
        assertEquals(30, pawn.sell(6, "low_table", "standard"));    // a new day, a full till
        assertEquals(0, pawn.sell(6, "kunai", "standard"));         // tools are not pawnable
    }

    @Test void hagglingOnlyWhereShopsHaggleAndAlwaysTheSameForTheSameDay() {
        assertEquals(500, prices.haggle(500, 0.2, "hero", 1, -1, 99, "furniture_shop", 3, "kotatsu"));
        int a = prices.haggle(500, 0.1, "good_neighbor", 0.5, 0, 99, "market_day_stalls", 6, "silk");
        assertEquals(a, prices.haggle(500, 0.1, "good_neighbor", 0.5, 0, 99, "market_day_stalls", 6, "silk"));
        assertTrue(a == 500 || a == 450);
        assertTrue(prices.haggleChance(0.1, "hero", 1, 0) > prices.haggleChance(0.1, "newcomer", 0, 1));
        assertTrue(prices.haggleChance(0.2, "newcomer", 0, 0) < prices.haggleChance(0.1, "newcomer", 0, 0));
        int won = 0;
        for (int day = 0; day < 1000; day++) if (prices.haggle(100, 0.1, "newcomer", 0, 0, 1, "pawn_shop", day, "silk") < 100) won++;
        assertEquals(550, won, 60);                                 // about the 55% the ask gives
    }
}
