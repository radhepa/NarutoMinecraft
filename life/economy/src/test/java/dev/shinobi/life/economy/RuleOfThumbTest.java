package dev.shinobi.life.economy;

import dev.shinobi.life.economy.sim.EconomySim;
import org.junit.jupiter.api.Test;

import java.util.ArrayList;
import java.util.List;
import java.util.function.ToIntFunction;

import static dev.shinobi.life.economy.Json.num;
import static dev.shinobi.life.economy.Json.obj;
import static org.junit.jupiter.api.Assertions.*;

/** ROADMAP §7 Ryo's rules of thumb, and the inflation guards, over nine seeds of the beta (EconomySim). */
class RuleOfThumbTest {
    static final List<String> PROFILES = List.of("frugal", "typical", "spender");
    final Catalogue c = Data.catalogue();
    final EconomySim sim = new EconomySim(c, Data.DIR);
    final List<EconomySim.Result> runs = new ArrayList<>();

    RuleOfThumbTest() {
        for (long seed = 1; seed <= 9; seed++) for (String p : PROFILES) runs.add(sim.run(p, seed));
    }
    int median(String profile, ToIntFunction<EconomySim.Result> f) {
        var v = runs.stream().filter(r -> r.profile().equals(profile)).mapToInt(f).sorted().toArray();
        return v[v.length / 2];
    }
    Object rule(String name, String key) { return obj(obj(c.economy.get("rule_of_thumb")).get(name)).get(key); }

    @Test void aDayOfDRanksCoversFoodAndLeavesAboutHalf() {
        double left = sim.dRankDayLeft("typical", 20);
        assertTrue(left >= num(rule("d_rank_day", "left_min"), .4) && left <= num(rule("d_rank_day", "left_max"), .6),
                "a typical day of D-ranks leaves " + left);
        assertTrue(sim.dRankDayLeft("spender", 20) > 0, "even a spender's day of D-ranks pays for itself");
    }

    @Test void theStipendNeverReplacesMissions() {
        int stipend = Json.integer(obj(c.economy.get("stipend")).get("amount"), 0);
        assertTrue(stipend < sim.dailyFood("typical", "beta2", 20), "the stipend alone does not feed a typical Genin");
        double dDay = 2 * num(obj(obj(c.economy.get("missions")).get("d")).get("beta2_mean"), 85);
        assertTrue(dDay >= 5 * stipend, "a day of D-ranks pays at least five days of stipend");
        for (var r : runs) if (r.profile().equals("typical"))
            assertTrue(r.earnedBy().get("stipend") * 2.5 < r.earnedBy().get("D-ranks") + r.earnedBy().get("C-ranks") + r.earnedBy().get("chapters"),
                    "missions earn far more than the stipend over the beta, Academy days included");
    }

    @Test void theFirstFurnitureSetTakesAboutAWeek() {
        int typical = median("typical", EconomySim.Result::starterSetDay);
        assertTrue(typical >= num(rule("starter_set_day", "min"), 6) && typical <= num(rule("starter_set_day", "max"), 9),
                "typical median day " + typical);
        assertTrue(median("frugal", EconomySim.Result::starterSetDay) <= typical);
        for (var r : runs) if (!r.profile().equals("spender")) assertTrue(r.starterSetDay() > 0 && r.starterSetDay() <= 11, r.profile() + " " + r.starterSetDay());
    }

    @Test void nobodyStarvesOrGoesIntoDebt() {
        for (var r : runs) {
            assertEquals(0, r.hungryDays(), r.profile());
            assertTrue(r.minBalance() >= 0, r.profile());
            assertEquals(r.earned() - r.spent(), r.finalBalance(), r.profile() + ": every ryo is accounted for");
        }
    }

    @Test void sinksKeepRyoFromPilingUp() {
        int typical = median("typical", EconomySim.Result::finalBalance);
        assertTrue(typical >= 300 && typical <= 2500, "typical ends the beta with " + typical);
        for (var r : runs) if (r.profile().equals("typical")) assertTrue(r.spent() >= 0.7 * r.earned(), "typical spends most of what it earns");
        assertTrue(median("frugal", EconomySim.Result::finalBalance) > typical);
        assertTrue(typical > median("spender", EconomySim.Result::finalBalance));
    }

    @Test void theSameSeedPlaysTheSameBeta() {
        assertEquals(sim.run("typical", 5).days(), sim.run("typical", 5).days());
        assertNotEquals(sim.run("typical", 5).days(), sim.run("typical", 6).days());
    }
}
