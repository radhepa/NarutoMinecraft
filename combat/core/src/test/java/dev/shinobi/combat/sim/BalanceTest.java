package dev.shinobi.combat.sim;

import static org.junit.jupiter.api.Assertions.*;

import dev.shinobi.combat.CombatData;
import dev.shinobi.combat.Difficulty;
import org.junit.jupiter.api.Test;

/**
 * Balance guards on the shipped data (COMBAT.md, "Balance"): the duel simulator must keep every build viable and
 * the beta's bosses fair. A data change that breaks one of these needs a look at the tables
 * ({@code ./gradlew :combat:core:simulate}).
 */
class BalanceTest {
    static final Balance SIM = new Balance(CombatData.load(), 20261029L, 30);

    @Test void storyIsForgivingAtEveryBetaBossForEveryBuild() {
        for (var b : SIM.betaBosses())
            for (String f : Balance.FOCI) {
                var avg = SIM.boss(b, f, Difficulty.STORY, Fighter.Skill.AVERAGE);
                var novice = SIM.boss(b, f, Difficulty.STORY, Fighter.Skill.NOVICE);
                assertTrue(avg.win() >= 0.8, b.id() + " " + f + " story average " + avg.win());
                assertTrue(novice.win() >= 0.6, b.id() + " " + f + " story novice " + novice.win());
            }
    }
    @Test void shinobiIsAChallengeNotAWall() {
        for (var b : SIM.betaBosses())
            for (String f : Balance.FOCI) {
                var s = SIM.boss(b, f, Difficulty.SHINOBI, Fighter.Skill.AVERAGE);
                assertTrue(s.win() >= 0.25, b.id() + " " + f + " shinobi " + s.win());
            }
    }
    @Test void everyBuildBeatsALevelMatchedEliteMostOfTheTimeFromGenin() {
        for (int lv : new int[]{10, 18, 30, 50})
            for (String f : Balance.FOCI) {
                var story = SIM.duel("sim." + f + "." + lv, Balance.ELITE, lv, Difficulty.STORY, Fighter.Skill.AVERAGE);
                var shinobi = SIM.duel("sim." + f + "." + lv, Balance.ELITE, lv, Difficulty.SHINOBI, Fighter.Skill.AVERAGE);
                assertTrue(story.win() >= 0.9, f + " " + lv + " story " + story.win());
                assertTrue(shinobi.win() >= 0.4, f + " " + lv + " shinobi " + shinobi.win());
                assertTrue(story.seconds() > 1 && story.seconds() < 25, f + " " + lv + " elite time " + story.seconds());
            }
    }
    @Test void noPillarIsShutOutOfPlayerVersusPlayer() {
        String[] pillars = {"taijutsu", "weapons", "ninjutsu"};
        for (int lv : new int[]{18, 30, 50})
            for (String a : pillars) {
                double sum = 0;
                for (String b : pillars) if (!a.equals(b)) sum += SIM.pvp("sim." + a + "." + lv, "sim." + b + "." + lv, Difficulty.SHINOBI);
                assertTrue(sum / 2 >= 0.2, a + " at " + lv + " wins only " + sum / 2 + " against the other pillars");
            }
    }
    @Test void theSimulatorIsDeterministic() {
        var a = SIM.duel("sim.balanced.18", Balance.ELITE, 18, Difficulty.SHINOBI, Fighter.Skill.AVERAGE);
        var b = SIM.duel("sim.balanced.18", Balance.ELITE, 18, Difficulty.SHINOBI, Fighter.Skill.AVERAGE);
        assertEquals(a, b);
    }
}
