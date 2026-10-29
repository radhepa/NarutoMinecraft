package dev.shinobi.village.look;

import static org.junit.jupiter.api.Assertions.*;

import java.util.List;
import org.junit.jupiter.api.Test;

class CreatorRulesTest {
    final CreatorRules r = Data.RULES;

    @Test
    void everyClanAndTheClanlessArePickable() {
        assertEquals(26, r.origins().size());
        assertEquals(CreatorRules.CLANLESS, r.origins().get(0));
        assertFalse(r.isClan(CreatorRules.CLANLESS));
        assertTrue(r.isClan("hyuga"));
        assertEquals("Hyuga", r.clanName("hyuga"));
        assertNull(r.clanName(CreatorRules.CLANLESS));
    }

    @Test
    void everyOpeningLookIsAllowedForBothBodies() {
        for (String o : r.origins())
            for (String b : r.bodies)
                assertEquals(List.of(), r.validate(o, AgeStage.CHILD, r.defaults(o, b)), o + " " + b);
    }

    @Test
    void everyOriginCanDressEitherBodyAtEveryStage() {
        for (String o : r.origins())
            for (var s : AgeStage.values())
                for (String b : r.bodies)
                    assertFalse(r.choices(o, s).outfits().get(b).isEmpty(), o + " " + s + " " + b);
    }

    @Test
    void clanHairAndColorsStayWithTheClan() {
        var clanless = r.choices(CreatorRules.CLANLESS, AgeStage.CHILD);
        var hyuga = r.choices("hyuga", AgeStage.CHILD);
        assertTrue(hyuga.hair().containsAll(clanless.hair().stream().filter(h -> !h.startsWith("hc002") && !h.startsWith("hc006")).toList()));
        assertTrue(hyuga.hair().stream().anyMatch(h -> h.startsWith("h4")), "Hyuga hair is offered to the Hyuga-born");
        assertTrue(clanless.hair().stream().noneMatch(h -> h.startsWith("h4")), "and to no one else");
        assertFalse(clanless.hairColors().contains("UCHIHA_BLACK"));
        assertTrue(r.choices("uchiha", AgeStage.CHILD).hairColors().contains("UCHIHA_BLACK"));
    }

    @Test
    void theHyugaEyesAreLockedAndTheSharinganIsNeverChosen() {
        assertEquals(List.of("BYAKUGAN"), r.choices("hyuga", AgeStage.CHILD).eyeColors());
        for (String o : r.origins()) {
            var eyes = r.choices(o, AgeStage.CHILD).eyeColors();
            assertFalse(eyes.contains("SHARINGAN"), o);
            if (!o.equals("hyuga")) assertFalse(eyes.contains("BYAKUGAN"), o);
        }
    }

    @Test
    void conferredMarksAreNeverChosenAndAgeLinesWaitForAdulthood() {
        assertFalse(r.choices("hyuga", AgeStage.ADULT).marks().contains("hyuga_caged_bird"));
        assertFalse(r.choices("senju", AgeStage.CHILD).marks().contains("senju_strength_seal"));
        assertFalse(r.choices("sarutobi", AgeStage.CHILD).marks().contains("sarutobi_age_lines"));
        assertTrue(r.choices("sarutobi", AgeStage.ADULT).marks().contains("sarutobi_age_lines"));
        assertTrue(r.choices("inuzuka", AgeStage.CHILD).marks().contains("inuzuka_fangs"));
    }

    @Test
    void beardsAndEldersStylesWaitForAdulthood() {
        assertFalse(r.choices("sarutobi", AgeStage.CHILD).hair().contains("h902_guardian_beard"));
        assertFalse(r.choices("sarutobi", AgeStage.TEEN).hair().contains("h902_guardian_beard"));
        assertTrue(r.choices("sarutobi", AgeStage.ADULT).hair().contains("h902_guardian_beard"));
        assertFalse(r.choices(CreatorRules.CLANLESS, AgeStage.CHILD).hair().contains("hc002_balding_crown"));
    }

    @Test
    void noForeheadProtectorBeforeGenin() {
        for (String o : r.origins())
            for (String h : r.choices(o, AgeStage.CHILD).headwear())
                assertTrue(h == null || !h.contains("protector"), o + " " + h);
        assertTrue(r.choices(CreatorRules.CLANLESS, AgeStage.TEEN).headwear().contains("w02_forehead_protector"));
    }

    @Test
    void theChildStageWearsAcademyOutfitsOnly() {
        for (String o : r.origins())
            for (var outfit : r.choices(o, AgeStage.CHILD).outfits().get("male"))
                assertEquals("academy", outfit.rank(), o + " " + outfit.id());
    }

    @Test
    void clanBornMayWearAnyOutfitInTheClanColors() {
        var nara = r.choices("nara", AgeStage.CHILD).outfit("male", "academy_genin.first_day");
        assertNotNull(nara);
        var clanless = r.choices(CreatorRules.CLANLESS, AgeStage.CHILD).outfit("male", "academy_genin.first_day");
        assertTrue(nara.palettes().containsAll(clanless.palettes()));
        assertTrue(nara.palettes().size() > clanless.palettes().size());
        var look = r.defaults("nara", "male").withOutfit("academy_genin.first_day", nara.palettes().get(nara.palettes().size() - 1));
        assertEquals(List.of(), r.validate("nara", AgeStage.CHILD, look));
        assertFalse(r.validate(CreatorRules.CLANLESS, AgeStage.CHILD, look.withHair("hg001_messy_mop")).isEmpty());
    }

    @Test
    void theServerRefusesWhatTheScreenWouldNotOffer() {
        var base = r.defaults(CreatorRules.CLANLESS, "female");
        assertTrue(r.validate(CreatorRules.CLANLESS, AgeStage.CHILD, base.withHair("h401_byakugan_heir")).stream().anyMatch(e -> e.startsWith("hair")));
        assertTrue(r.validate(CreatorRules.CLANLESS, AgeStage.CHILD, base.withEyeColor("SHARINGAN")).stream().anyMatch(e -> e.startsWith("eye_color")));
        assertTrue(r.validate(CreatorRules.CLANLESS, AgeStage.CHILD, base.withHeadwear("w02_forehead_protector")).stream().anyMatch(e -> e.startsWith("headwear")));
        assertTrue(r.validate(CreatorRules.CLANLESS, AgeStage.CHILD, base.withMarks(List.of("whiskers", "whiskers"))).stream().anyMatch(e -> e.startsWith("at most")));
        assertTrue(r.validate(CreatorRules.CLANLESS, AgeStage.CHILD, base.withOutfit("academy_genin.first_day", "UCHIHA_NIGHT")).stream().anyMatch(e -> e.startsWith("palette")));
        assertEquals(List.of("unknown origin kagura"), r.validate("kagura", AgeStage.CHILD, base));
    }

    @Test
    void aLookSurvivesTheSaveRoundTrip() {
        var look = r.defaults("inuzuka", "female");
        assertEquals(look, Look.fromMap(look.toMap()));
    }
}
