package dev.shinobi.combat;

import static org.junit.jupiter.api.Assertions.*;

import dev.shinobi.combat.Damage.Attack;
import dev.shinobi.combat.Damage.Defence;
import dev.shinobi.combat.Damage.Delivery;
import dev.shinobi.combat.Damage.Guard;
import dev.shinobi.combat.Scaling.Pillar;
import org.junit.jupiter.api.Test;

class NatureAndDamageTest {
    @Test void theTriangleIsACycleOfFive() {
        assertTrue(Nature.FIRE.beats(Nature.WIND));
        assertTrue(Nature.WIND.beats(Nature.LIGHTNING));
        assertTrue(Nature.LIGHTNING.beats(Nature.EARTH));
        assertTrue(Nature.EARTH.beats(Nature.WATER));
        assertTrue(Nature.WATER.beats(Nature.FIRE));
        for (var n : Nature.values()) {
            if (n == Nature.NONE) continue;
            int beaten = 0, beatenBy = 0;
            for (var o : Nature.values()) { if (n.beats(o)) beaten++; if (o.beats(n)) beatenBy++; }
            assertEquals(1, beaten, n + " beats exactly one");
            assertEquals(1, beatenBy, n + " is beaten by exactly one");
        }
        assertFalse(Nature.NONE.beats(Nature.FIRE));
    }
    @Test void affinityMakesTheWeakNatureHurtMore() {
        assertEquals(1.25, Nature.WATER.against(Nature.FIRE));
        assertEquals(0.8, Nature.FIRE.against(Nature.WATER));
        assertEquals(1.0, Nature.FIRE.against(Nature.EARTH), "unrelated natures are even");
        assertEquals(1.0, Nature.NONE.against(Nature.FIRE));
        assertEquals(1.0, Nature.FIRE.against(Nature.NONE));
    }
    @Test void clashesFavourTheStrongerNatureThenThePower() {
        var c = Nature.clash(Nature.WATER, 10, Nature.FIRE, 30);
        assertEquals(Nature.WATER, c.winner(), "water puts out a bigger fire");
        assertEquals(5, c.power(), 1e-9, "passing through at half power");
        var same = Nature.clash(Nature.FIRE, 20, Nature.FIRE, 12);
        assertEquals(Nature.FIRE, same.winner());
        assertEquals(8, same.power(), 1e-9);
        assertTrue(Nature.clash(Nature.EARTH, 9, Nature.FIRE, 9).bothGone());
    }
    @Test void levelAndPillarScaleWhatYouDeal() {
        assertEquals(1.0, Scaling.power(1, Pillar.NINJUTSU), 1e-9);
        assertEquals(1 + 0.03 * 49, Scaling.power(50, Pillar.NINJUTSU), 1e-9);
        assertEquals(1 + 0.04 * 49, Scaling.power(50, Pillar.TAIJUTSU), 1e-9, "taijutsu gets the roadmap's +1% a level on top");
        assertEquals(1.63, Scaling.pillar(10), 1e-9);
        assertEquals(1.0, Scaling.pillar(0), 1e-9, "ranks clamp to 1..10");
    }
    @Test void heartsFollowTheRoadmap() {
        assertEquals(20, Scaling.playerHp(1, 0));
        assertEquals(20, Scaling.playerHp(6, 0));
        assertEquals(22, Scaling.playerHp(7, 0));
        assertEquals(38, Scaling.playerHp(60, 0), "19 hearts at level 60");
        assertEquals(24, Scaling.playerHp(1, 2), "Akimichi's two extra hearts");
        assertEquals(5, Scaling.pillarCap(5));
        assertEquals(30, Scaling.pillarCap(60));
    }
    @Test void armourTakesAShareCappedAt60Percent() {
        assertEquals(0, Damage.armourReduction(0, 0));
        assertEquals(0.5, Damage.armourReduction(20, 0), 1e-9);
        assertEquals(0.6, Damage.armourReduction(500, 0), 1e-9);
        assertTrue(Damage.armourReduction(20, 0.3) < 0.5, "pierce removes armour first");
    }
    @Test void aBlockStopsMeleeBestThrownWellAndJutsuPoorly() {
        var d = Defence.of(false, 10, 0, 0, Nature.NONE).guarding(Guard.BLOCK);
        double melee = Damage.hit(Attack.player(10, "physical.blunt", Delivery.MELEE, 1, Pillar.TAIJUTSU, 1, 1), d).hp();
        double thrown = Damage.hit(Attack.player(10, "physical.pierce", Delivery.THROWN, 1, Pillar.WEAPONS, 1, 1), d).hp();
        double jutsu = Damage.hit(Attack.player(10, "ninjutsu.fire", Delivery.JUTSU, 1, Pillar.NINJUTSU, 1, 1), d).hp();
        assertEquals(4, melee, 1e-9);
        assertEquals(2, thrown, 1e-9);
        assertEquals(7, jutsu, 1e-9);
        var wind = Damage.hit(Attack.player(10, "ninjutsu.wind", Delivery.JUTSU, 1, Pillar.NINJUTSU, 1, 1), d);
        assertTrue(wind.hp() > jutsu, "wind pierces guards");
        assertTrue(wind.staminaCost() > 0, "blocking costs stamina");
    }
    @Test void parriesAndDodgesAvoidTheHit() {
        var a = Attack.player(10, "physical.slash", Delivery.MELEE, 5, Pillar.WEAPONS, 3, 1);
        assertTrue(Damage.hit(a, Defence.of(false, 5, 0, 0, Nature.NONE).guarding(Guard.PARRY)).avoided());
        assertTrue(Damage.hit(a, Defence.of(false, 5, 0, 0, Nature.NONE).guarding(Guard.DODGE)).avoided());
        var jutsu = Attack.player(10, "ninjutsu.fire", Delivery.JUTSU, 5, Pillar.NINJUTSU, 3, 1);
        assertFalse(Damage.hit(jutsu, Defence.of(false, 5, 0, 0, Nature.NONE).guarding(Guard.PARRY)).avoided(), "jutsu cannot be parried");
    }
    @Test void enemiesScaleByLevelAndDifficultyAndThePlayerToughens() {
        var club = Attack.enemy(3, "physical.blunt", Delivery.MELEE, 10, 1, Difficulty.STORY.enemyDamage());
        var kid = Damage.hit(club, Defence.of(true, 1, 0, 0, Nature.NONE)).hp();
        var vet = Damage.hit(club, Defence.of(true, 50, 0, 0, Nature.NONE)).hp();
        assertEquals(3 * (1 + 0.03 * 9) * 0.6, kid, 1e-9);
        assertTrue(vet < kid * 0.5, "a level-50 body takes less than half");
    }
    @Test void gentleFistDrainsChakraAndHalfTheHealth() {
        var palm = Damage.hit(Attack.player(4, "chakra", Delivery.MELEE, 1, Pillar.TAIJUTSU, 1, 1), Defence.of(false, 1, 30, 30, Nature.NONE));
        assertEquals(4, palm.chakraDrain(), 1e-9, "ignores armour");
        assertEquals(2, palm.hp(), 1e-9);
    }
    @Test void soakedTargetsTakeMoreLightning() {
        var d = Defence.of(false, 1, 0, 0, Nature.NONE);
        double dry = Damage.hit(Attack.player(10, "ninjutsu.lightning", Delivery.JUTSU, 1, Pillar.NINJUTSU, 1, 1), d).hp();
        double wet = Damage.hit(Attack.player(10, "ninjutsu.lightning", Delivery.JUTSU, 1, Pillar.NINJUTSU, 1, 1), d.taking(1.3)).hp();
        assertEquals(dry * 1.3, wet, 1e-9);
    }
}
