package dev.shinobi.village.look;

import static org.junit.jupiter.api.Assertions.*;

import java.util.List;
import org.junit.jupiter.api.Test;

class RestyleAndGrowUpTest {
    final CreatorRules r = Data.RULES;
    final Restyle restyle = new Restyle(r);
    final GrowUp grow = new GrowUp(r);

    @Test
    void lockedFieldsNeverChangeAndEachVenueChangesItsOwn() {
        assertEquals(Restyle.Venue.LOCKED, restyle.venue("complexion"));
        assertEquals(Restyle.Venue.LOCKED, restyle.venue("clan"));
        assertEquals(Restyle.Venue.LOCKED, restyle.venue("eye_color"));
        assertTrue(restyle.canChange("hair", Restyle.Venue.BARBER));
        assertFalse(restyle.canChange("hair", Restyle.Venue.HOME));
        assertTrue(restyle.canChange("outfit", Restyle.Venue.HOME));
        assertFalse(restyle.canChange("body", Restyle.Venue.TIME_SKIP));
        assertTrue(restyle.canChange("hair", Restyle.Venue.TIME_SKIP));
        assertTrue(restyle.canChange("pronouns", Restyle.Venue.SETTINGS));
        assertEquals(Restyle.Venue.LOCKED, restyle.venue("affinity"));
    }

    @Test
    void theBarberChargesAndKeepsToTheCreatorsChoices() {
        var look = r.defaults(CreatorRules.CLANLESS, "male");
        var ok = restyle.apply(look, CreatorRules.CLANLESS, AgeStage.CHILD, "hair_color", "SNOW", Restyle.Venue.BARBER);
        assertTrue(ok.ok());
        assertEquals("SNOW", ok.look().hairColor());
        assertEquals(restyle.cost("hair_color"), ok.cost());
        var clanColor = restyle.apply(look, CreatorRules.CLANLESS, AgeStage.CHILD, "hair_color", "UZUMAKI_CRIMSON", Restyle.Venue.BARBER);
        assertFalse(clanColor.ok());
        assertEquals(look, clanColor.look());
        var wrongPlace = restyle.apply(look, CreatorRules.CLANLESS, AgeStage.CHILD, "outfit", List.of("academy_genin.layers", "ACADEMY_GENIN_SKY"), Restyle.Venue.BARBER);
        assertFalse(wrongPlace.ok());
        var atHome = restyle.apply(look, CreatorRules.CLANLESS, AgeStage.CHILD, "outfit", List.of("academy_genin.layers", "ACADEMY_GENIN_SKY"), Restyle.Venue.HOME);
        assertTrue(atHome.ok(), atHome.refused());
        assertEquals(0, atHome.cost());
    }

    @Test
    void theMirrorIsFree() {
        var child = r.defaults("sarutobi", "male");
        var look = grow.grow(grow.grow(child, "sarutobi", AgeStage.TEEN, "genin"), "sarutobi", AgeStage.ADULT, "jonin");
        var res = restyle.apply(look, "sarutobi", AgeStage.ADULT, "hair", "h902_guardian_beard", Restyle.Venue.TIME_SKIP);
        assertTrue(res.ok(), res.refused());
        assertEquals(0, res.cost());
        assertFalse(restyle.apply(child, "sarutobi", AgeStage.CHILD, "hair", "h902_guardian_beard", Restyle.Venue.BARBER).ok());
    }

    @Test
    void hairGrowsAndOutfitsFollowTheRank() {
        var child = r.defaults(CreatorRules.CLANLESS, "female").withHair("hg003_short_twin_tails");
        var teen = grow.grow(child, CreatorRules.CLANLESS, AgeStage.TEEN, "genin");
        assertEquals("hg004_low_pigtails", teen.hair());
        assertEquals("genin", r.outfit(teen.outfit()).rank(), "the Academy outfit gives way to a Genin one");
        assertEquals(List.of(), r.validate(CreatorRules.CLANLESS, AgeStage.TEEN, teen));
        var adult = grow.grow(teen, CreatorRules.CLANLESS, AgeStage.ADULT, "chunin");
        assertEquals("hg021_tied_long_straight", adult.hair());
        assertEquals(List.of(), r.validate(CreatorRules.CLANLESS, AgeStage.ADULT, adult));
        assertEquals(child.complexion(), adult.complexion());
        assertEquals(child.eyeColor(), adult.eyeColor());
    }

    @Test
    void everyOpeningLookGrowsIntoAnAllowedOne() {
        for (String o : r.origins())
            for (String b : r.bodies) {
                var teen = grow.grow(r.defaults(o, b), o, AgeStage.TEEN, "genin");
                assertEquals(List.of(), r.validate(o, AgeStage.TEEN, teen), o + " " + b);
                var adult = grow.grow(teen, o, AgeStage.ADULT, "jonin");
                assertEquals(List.of(), r.validate(o, AgeStage.ADULT, adult), o + " " + b);
            }
    }

    @Test
    void venuesReadTheSameUnderATurkishLocale() {
        var before = java.util.Locale.getDefault();
        try {
            java.util.Locale.setDefault(java.util.Locale.forLanguageTag("tr-TR"));
            var turkish = new Restyle(r);
            assertEquals(Restyle.Venue.SETTINGS, turkish.venue("pronouns"));
            var look = r.defaults(CreatorRules.CLANLESS, "male");
            var no = turkish.apply(look, CreatorRules.CLANLESS, AgeStage.ADULT, "body", "x", Restyle.Venue.TIME_SKIP);
            assertTrue(no.refused().endsWith("time_skip"), no.refused());
        } finally {
            java.util.Locale.setDefault(before);
        }
    }
}
