package dev.shinobi.village.look;

import static org.junit.jupiter.api.Assertions.*;

import java.util.List;
import org.junit.jupiter.api.Test;

class NamesTest {
    final CreatorRules r = Data.RULES;

    List<String> check(String n) { return Names.validateGiven(n, r.nameMin, r.nameMax); }

    @Test
    void ordinaryNamesPass() {
        for (String n : List.of("Kaede", "Ren", "Mei-Lin", "O'Hara", "Sora Ann", "Zoë", "陽翔", "Анна"))
            assertEquals(List.of(), check(n), n);
    }

    @Test
    void badNamesAreRefusedWithAReason() {
        assertEquals(List.of("name.empty"), check("  "));
        assertTrue(check("K").contains("name.too_short"));
        assertTrue(check("Abcdefghijklmnopq").contains("name.too_long"));
        assertTrue(check("-Ren").contains("name.start_with_letter"));
        assertTrue(check("{player}").contains("name.bad_character"), "token syntax can never enter a name");
        assertTrue(check("Ren7").contains("name.bad_character"));
        assertTrue(check("Ren  Ai").contains("name.double_space"));
    }

    @Test
    void theClanBornCarryTheClanNameAndTheClanlessAnOrdinaryOne() {
        assertEquals("Nara", Names.family(r, "nara", null, 1));
        assertEquals("Nara", Names.family(r, "nara", "Tanaka", 1), "a clan-born player cannot take another name");
        assertEquals("Tanaka", Names.family(r, CreatorRules.CLANLESS, "Tanaka", 1));
        assertThrows(IllegalArgumentException.class, () -> Names.family(r, CreatorRules.CLANLESS, "Uchiha", 1));
        String rolled = Names.family(r, CreatorRules.CLANLESS, null, 99);
        assertTrue(r.familyNames(CreatorRules.CLANLESS).contains(rolled));
        assertEquals(rolled, Names.family(r, CreatorRules.CLANLESS, null, 99), "the names stream is stable");
    }

    @Test
    void noClanNameIsInTheOrdinaryPool() {
        var pool = r.familyNames(CreatorRules.CLANLESS);
        for (String o : r.origins()) if (r.isClan(o)) assertFalse(pool.contains(r.clanName(o)), o);
    }

    @Test
    void tokensResolve() {
        var t = Names.tokens(new Names.PlayerName("Kaede", "Tanaka"), null);
        assertEquals("Kaede", t.get("player"));
        assertEquals("Kaede Tanaka", t.get("player_full"));
        assertEquals("", t.get("player_clan"));
        assertEquals("Hyuga", Names.tokens(new Names.PlayerName("Ren", "Hyuga"), "Hyuga").get("player_clan"));
    }
}
