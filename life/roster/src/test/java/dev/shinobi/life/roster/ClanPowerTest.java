package dev.shinobi.life.roster;

import static org.junit.jupiter.api.Assertions.*;

import java.util.Arrays;
import org.junit.jupiter.api.Test;

class ClanPowerTest {
    @Test void clansFallIntoTheirTiers() {
        assertEquals(ClanPower.GREAT, ClanPower.of("uchiha"));
        assertEquals(ClanPower.STRONG, ClanPower.of("nara"));
        assertEquals(ClanPower.MINOR, ClanPower.of("tobari"));
        assertEquals(ClanPower.CLANLESS, ClanPower.of(""));
        assertEquals(ClanPower.CLANLESS, ClanPower.of("none"));
        assertEquals(ClanPower.CLANLESS, ClanPower.of(null));
    }
    static double[] chunin(ClanPower p) {
        var rng = Seeds.stream(1, "residents", p.id());
        double[] l = new double[4000];
        for (int i = 0; i < l.length; i++) l[i] = p.roll(21, 4, 15, 29, rng);
        Arrays.sort(l);
        return l;
    }
    @Test void powerfulClansAreStrongerOnAverageButTheSpreadsOverlap() {
        double last = 99;
        for (var p : ClanPower.values()) {
            double mean = Arrays.stream(chunin(p)).average().orElseThrow();
            assertTrue(mean < last, p + " is weaker on average than the tier above");
            last = mean;
        }
        double[] great = chunin(ClanPower.GREAT), clanless = chunin(ClanPower.CLANLESS);
        double greatMedian = great[great.length / 2];
        long above = Arrays.stream(clanless).filter(l -> l > greatMedian).count();
        assertTrue(above > clanless.length / 6, "plenty of clanless chunin beat the great clans' median: " + above);
        for (double l : great) assertTrue(l >= 15 && l <= 29, "the rank's range holds");
    }
    @Test void aRolledClassmateLeansOnClanPower() {
        double great = 0, clanless = 0;
        for (int i = 0; i < 500; i++) {
            great += Peer.rolled("x", Niche.NINJUTSU, "hyuga", Seeds.stream(i, "cast", "x")).late();
            clanless += Peer.rolled("x", Niche.NINJUTSU, "", Seeds.stream(i, "cast", "x")).late();
        }
        assertTrue(great / 500 > clanless / 500 + .8);
        var p = Peer.rolled("x", Niche.NINJUTSU, "", Seeds.stream(3, "cast", "x"));
        assertTrue(Math.abs(p.late()) <= 1.5);
    }
}
