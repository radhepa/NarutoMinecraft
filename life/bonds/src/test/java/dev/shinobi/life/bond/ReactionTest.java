package dev.shinobi.life.bond;

import static org.junit.jupiter.api.Assertions.*;

import dev.shinobi.life.bond.Personality.Peeve;
import dev.shinobi.life.bond.Personality.Value;
import java.util.Set;
import org.junit.jupiter.api.Test;

class ReactionTest {
    static final Personality BOLD = Personality.of("adventurous", "see_the_world");
    static final Personality CAREFUL = Personality.of("meticulous", "build_something_lasting");

    @Test void theSameActLandsDifferentlyOnDifferentPeople() {
        var bold = Reaction.react(BOLD, Act.RECKLESS_CHARGE);
        var careful = Reaction.react(CAREFUL, Act.RECKLESS_CHARGE);
        assertTrue(bold.respect() > careful.respect(), "the bold respect a reckless charge");
        assertTrue(bold.trust() > careful.trust(), "the careful trust you less for it");
        assertTrue(careful.trust() < 0);
    }
    @Test void valuesAmplifyAndPeevesSting() {
        var loyal = CAREFUL.withValues(Set.of(Value.LOYALTY));
        var plain = CAREFUL.withValues(Set.of());
        assertTrue(Reaction.react(loyal, Act.STOOD_BY_THEM).trust() > Reaction.react(plain, Act.STOOD_BY_THEM).trust(), "honoring a value");
        assertTrue(Reaction.react(loyal, Act.BROKE_SECRET).trust() < Reaction.react(plain, Act.BROKE_SECRET).trust(), "violating one");
        var minds = plain.withPeeves(Set.of(Peeve.BRAGGING));
        var shrugs = plain.withPeeves(Set.of());
        assertTrue(Reaction.react(minds, Act.BRAGGED).affection() < Reaction.react(shrugs, Act.BRAGGED).affection() - 1.5);
    }
    @Test void pridesTurnALostSparIntoRivalryAndWarmthSoftensBlows() {
        var proud = Personality.of("proud", "surpass_a_rival");
        var gentle = Personality.of("gentle", "heal_people");
        var warm = Personality.of("warmhearted", "raise_a_family");
        var lost = Reaction.react(proud, Act.SPAR_WON);
        assertTrue(lost.rivalry() > Reaction.react(gentle, Act.SPAR_WON).rivalry());
        assertTrue(lost.affection() < 0, "the proud don't like losing to you");
        assertTrue(lost.respect() > 0, "but they respect it");
        assertTrue(Reaction.react(warm, Act.RUDE).affection() > Reaction.react(proud, Act.RUDE).affection(), "the warm forgive more");
        assertTrue(Reaction.react(gentle, Act.RUDE).affection() < Reaction.react(warm, Act.RUDE).affection(), "unless it is their pet peeve");
    }
    @Test void secondhandNewsIsWeakerAndCountsMoreForThoseWhoCare() {
        var self = Reaction.react(BOLD, Act.SAVED_LIFE);
        var stranger = Reaction.secondhand(BOLD, Act.SAVED_LIFE, Reaction.Source.HEARD, 0);
        var sister = Reaction.secondhand(BOLD, Act.SAVED_LIFE, Reaction.Source.HEARD, 1);
        var seen = Reaction.secondhand(BOLD, Act.SAVED_LIFE, Reaction.Source.SEEN, 0);
        assertTrue(stranger.trust() < sister.trust() && sister.trust() < self.trust());
        assertTrue(seen.trust() > stranger.trust(), "seeing it beats hearing it");
        assertEquals(0, Reaction.secondhand(BOLD, Act.DATE, Reaction.Source.SEEN, 1).romance(), "romance never travels secondhand");
    }
    @Test void everyActHasAConsistentShape() {
        for (Act a : Act.values()) {
            assertEquals(a, Act.of(a.id()));
            if (a.size == Act.Size.BIG) assertTrue(a.permanent(), a + " is big, so permanent");
            else if (a.remembered()) assertTrue(a.halfLife > 0, a + " fades");
            if (a.worth != 0) assertTrue(a.spreads, a + " is a deed");
            assertFalse(a.quarrel && a.professional, a + " cannot both quarrel and be professional");
        }
        for (String id : Personality.archetypes()) assertNotNull(Personality.of(id, "see_the_world"));
        assertThrows(IllegalArgumentException.class, () -> Personality.of("grumpy", ""));
    }
    @Test void chemistryIsSymmetricForTheSparkAndWarmPeopleClickMore() {
        var w = new BondWorld(7, 0);
        w.add(Leaf.resident("a", "warmhearted")); w.add(Leaf.resident("b", "reserved")); w.add(Leaf.resident("c", "gentle"));
        assertEquals(Personality.chemistry(.3, w.person("a").personality(), w.person("c").personality()),
                Personality.chemistry(.3, w.person("c").personality(), w.person("a").personality()), 1e-9);
        assertTrue(Personality.chemistry(0, w.person("a").personality(), w.person("c").personality())
                > Personality.chemistry(0, w.person("a").personality(), w.person("b").personality()));
        double ab = w.chemistry("a", "b"), ba = w.chemistry("b", "a");
        assertTrue(Math.abs(ab - ba) < .3, "the spark is the pair's; only the personalities differ");
    }
}
