package dev.shinobi.combat;

import static org.junit.jupiter.api.Assertions.*;

import java.util.HashSet;
import org.junit.jupiter.api.Test;

/** The compiled data loads, and the core's built-in tables agree with it. */
class DataTest {
    static final CombatData DATA = CombatData.load();

    @Test void everythingLoads() {
        assertEquals(((Number) DATA.index.get("techniques")).intValue(), DATA.techniques.size());
        assertEquals(25, DATA.clans.size());
        assertTrue(DATA.techniques.size() >= 200);
        assertTrue(DATA.enemies.size() >= 40);
        assertTrue(DATA.bosses.size() >= 9);
        assertEquals(3, DATA.difficulties.size());
        assertEquals(Difficulty.STORY, DATA.difficulties.get("story"), "the built-in Story mode matches the data");
        assertEquals(Difficulty.SHINOBI, DATA.difficulties.get("shinobi"));
        assertEquals(Difficulty.HARD, DATA.difficulties.get("hard"));
    }
    @Test void keyedClipsSampleBetweenTheirKeys() {
        for (var s : HandSign.values()) assertTrue(DATA.clips.containsKey("combat.sign." + s.id()), s.id());
        var rat = DATA.clips.get("combat.sign.rat");
        assertArrayEquals(new double[]{-63, -31.5, 0}, rat.rot("right_arm", 0), 1e-9);
        assertArrayEquals(new double[]{-62.5, -31.75, 0}, rat.rot("right_arm", 1), 1e-9, "halfway to the sign");
        assertArrayEquals(rat.rot("right_arm", 4), rat.rot("right_arm", 40), "held after the last key");
        assertNull(rat.rot("right_leg", 1), "a part the clip leaves alone");
        var block = DATA.clips.get("combat.def.block");
        assertArrayEquals(block.rot("left_arm", 3), block.rot("left_arm", 23), 1e-9, "a loop wraps");
    }
    @Test void damageTypesMatchTheData() {
        assertEquals(DamageType.BUILT_IN.keySet(), DATA.damageTypes.keySet());
        for (var e : DATA.damageTypes.entrySet()) {
            var m = Json.obj(e.getValue());
            assertEquals(Json.num(m, "poise_mult", 1), DamageType.of(e.getKey()).poiseMult(), 1e-9, e.getKey());
        }
    }
    @Test void everyRankHasTechniquesAndEveryNatureEveryRankFromC() {
        for (String r : new String[]{"e", "d", "c", "b", "a", "s"})
            assertTrue(DATA.techniques.values().stream().anyMatch(t -> t.rank().equals(r)), r);
        for (var n : Nature.values()) {
            if (n == Nature.NONE) continue;
            for (String r : new String[]{"d", "c", "b", "a", "s"})
                assertTrue(DATA.techniques.values().stream().anyMatch(t -> t.nature() == n && t.rank().equals(r) && t.clan() == null), n + " " + r);
        }
    }
    @Test void damagingTechniquesNameARealDamageType() {
        for (var t : DATA.techniques.values()) {
            var type = t.damageType();
            if (type != null) assertDoesNotThrow(() -> DamageType.of(type), t.id());
            for (var s : t.statuses()) assertTrue(DATA.statuses.containsKey(s.getKey()), t.id() + " applies unknown status " + s.getKey());
        }
    }
    @Test void everyEnemyAndBossResolves() {
        for (var e : DATA.enemies.values()) {
            for (var t : e.techniques()) assertTrue(DATA.techniques.containsKey(t), e.id() + " " + t);
            if (e.style() != null) assertTrue(DATA.styles.containsKey(e.style()), e.id());
            assertTrue(e.minLevel() <= e.maxLevel(), e.id());
        }
        for (var b : DATA.bosses.values())
            assertTrue(DATA.enemies.containsKey(b.base()) || DATA.groups.containsKey(b.base()), b.id() + " " + b.base());
    }
    @Test void betaTechniquesStayInTheBeta() {
        var beta = new HashSet<>(java.util.List.of("beta1", "beta2", "beta2_5", "beta3"));
        for (var t : DATA.techniques.values()) if (t.beta()) assertTrue(beta.contains(t.slice()), t.id());
    }
}
