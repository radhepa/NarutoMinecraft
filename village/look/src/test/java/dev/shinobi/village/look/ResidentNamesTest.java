package dev.shinobi.village.look;

import org.junit.jupiter.api.Test;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.HashSet;
import java.util.List;
import static org.junit.jupiter.api.Assertions.*;

class ResidentNamesTest {
    ResidentNames pools() throws Exception { return new ResidentNames(Files.readString(Path.of(System.getProperty("names.json")))); }
    CreatorRules rules() throws Exception { return CreatorRules.load(Path.of(System.getProperty("creator.json"))); }

    @Test void loadsLargeRomajiPoolsAndRejectsBrokenData() throws Exception {
        for (String gender : List.of("male", "female", "unisex")) {
            var names = pools().given(gender);
            assertTrue(names.size() >= 150, gender);
            assertEquals(names.size(), new HashSet<>(names).size());
            assertTrue(names.stream().allMatch(n -> n.matches("[A-Z][a-z]{0,63}")));
        }
        assertEquals(pools().given("unisex"), pools().given("nonbinary"));
        assertThrows(IllegalArgumentException.class, () -> new ResidentNames("{}"));
        assertThrows(IllegalArgumentException.class, () -> pools().given("unknown"));
        assertThrows(IllegalArgumentException.class, () -> pools().roll(42, "a", "male", "unknown", rules()));
    }

    @Test void clanResidentsUseTheClanRegistryAndCiviliansShareThePlayersPool() throws Exception {
        var rules = rules();
        for (String clan : rules.origins()) {
            var name = pools().roll(42, "resident:one", "female", clan, rules);
            if (rules.isClan(clan)) assertEquals(rules.clanName(clan), name.family());
            else assertTrue(rules.familyNames("clanless").contains(name.family()));
            assertEquals(name.given() + " " + name.family(), name.full());
        }
        var population = (java.util.Map<?, ?>) Json.parse(Files.readString(Path.of(System.getProperty("population.json"))));
        assertEquals(population.get("family_names"), rules.familyNames("clanless"));
        assertTrue(rules.familyNames("clanless").size() >= 150);
    }

    @Test void namesDependOnTheSaveEvenForTheSameClassicCastAndHaveFewDuplicates() throws Exception {
        var a = pools().roll(42, "role:sensei", "male", "nara", rules());
        assertEquals(a, pools().roll(42, "role:sensei", "male", "nara", rules()));
        assertNotEquals(a, pools().roll(2026, "role:sensei", "male", "nara", rules()));
        var seen = new HashSet<String>();
        for (int i = 0; i < 300; i++) seen.add(pools().roll(42, "resident:" + i, List.of("male", "female", "unisex").get(i % 3), null, rules()).full());
        assertTrue(seen.size() >= 295, "unique names in a 300-resident save: " + seen.size());
    }
}
