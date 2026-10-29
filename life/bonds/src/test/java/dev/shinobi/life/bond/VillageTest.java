package dev.shinobi.life.bond;

import static dev.shinobi.life.bond.Leaf.*;
import static org.junit.jupiter.api.Assertions.*;

import java.util.List;
import java.util.Map;
import org.junit.jupiter.api.Test;

/** Standing with the village's communities, clan invitations, recruiting for the player's clan, and children. */
class VillageTest {
    @Test void standingFollowsDeedsByCommunityAndBadNewsFades() {
        var w = Leaf.classic(12, 40);
        assertEquals(Standing.Title.NEWCOMER, w.title("village"));
        String naraOrAny = w.people().stream().filter(p -> !p.clan().isEmpty() && p.id().startsWith("resident:")).map(Person::clan).findFirst().orElseThrow();
        var clan = w.people().stream().filter(p -> p.clan().equals(naraOrAny)).map(Person::id).toList();
        w.deed(Act.SAVED_LIFE, clan.getFirst(), List.of());
        w.advance(2);
        assertTrue(w.standing("clan:" + naraOrAny) > w.standing("group:civilian"), "the clan whose member you saved thinks most of you");
        assertTrue(w.title("village").compareTo(Standing.Title.NEWCOMER) > 0);
        var bad = Leaf.classic(12, 40);
        bad.deed(Act.HURT_RESIDENT, "resident:1", List.of("resident:2", "resident:3"));
        bad.advance(3);
        double soon = bad.standing("village");
        bad.advance(120);
        assertTrue(soon < 0 && bad.standing("village") > soon, "bad deeds fade");
        assertEquals(Standing.Title.UNWELCOME, Standing.Title.of(-20));
        assertEquals(Standing.Title.HERO, Standing.Title.of(50));
    }
    @Test void recruitingNeedsRankLevelAndAWillingHeart() {
        assertEquals(0, Recruitment.slots(1));
        assertEquals(3, Recruitment.slots(2));
        assertEquals(8, Recruitment.slots(3));
        assertEquals(20, Recruitment.slots(5));
        var w = Leaf.classic(12, 0);
        assertEquals("has_clan", Recruitment.refuse(w, TEAMMATE_A, "player_x", 0), "a Kurama keeps their clan");
        assertEquals("rank", Recruitment.refuse(w, TEAMMATE_B, "player_x", 0));
        w.promote(2, List.of());
        assertEquals("level", Recruitment.refuse(w, TEAMMATE_B, "player_x", 0));
        w.bond(TEAMMATE_B).level = 9; w.bond(TEAMMATE_B).meet(0);
        assertEquals("full", Recruitment.refuse(w, TEAMMATE_B, "player_x", 3));
        String answer = Recruitment.refuse(w, TEAMMATE_B, "player_x", 0);
        assertTrue(answer.isEmpty() || answer.equals("not_now"));
        assertEquals(answer, Recruitment.refuse(w, TEAMMATE_B, "player_x", 0), "the same answer all week");
        var loyal = Recruitment.chance(w.person(TEAMMATE_B), 9, 80);
        var free = Recruitment.chance(w.person(TEAMMATE_B).withClan("").withRank(1), 7, 10);
        assertTrue(loyal > free);
    }
    @Test void aClanInvitesAClanlessPlayerItHoldsDear() {
        var w = new BondWorld(3, 0);
        for (int i = 0; i < 6; i++) w.add(Leaf.person("nara" + i, "nara", "residential", 2, Person.Stage.ADULT, Personality.of("thoughtful", "honor_their_clan"),
                "MALE", "FEMALE", i, i == 0 ? List.of("elder:nara") : List.of()));
        assertFalse(Recruitment.invited(w, "nara"));
        for (int i = 0; i < 6; i++) w.deed(Act.SAVED_LIFE, "nara" + i, List.of());
        w.advance(2);
        assertTrue(w.title("clan:nara").compareTo(Standing.Title.PILLAR) >= 0, w.standing("clan:nara") + "");
        assertFalse(Recruitment.invited(w, "nara"), "standing alone is not enough");
        w.bond("nara0").level = 9;
        assertTrue(Recruitment.invited(w, "nara"), "the elder vouches for you");
        w.player("MALE", "uchiha");
        assertFalse(Recruitment.invited(w, "nara"), "only the clanless are invited");
    }
    @Test void childrenComeInThePostGameToMarriedAdults() {
        var w = Leaf.classic(12, 0);
        assertEquals("not_married", Household.refuse(w, -1));
        w.bond(TEAMMATE_A).romance = Courtship.Stage.MARRIED;
        assertEquals("not_postgame", Household.refuse(w, -1));
        w.setFlag(Household.POSTGAME_FLAG, true);
        assertEquals("not_adults", Household.refuse(w, -1));
        w.setPlayerStage(Person.Stage.ADULT); w.grow(TEAMMATE_A, Person.Stage.ADULT);
        assertEquals("", Household.refuse(w, -1));
        var kid = Household.born(w, "resident:kid", "FEMALE");
        assertEquals("parent", kid.family().get(BondWorld.PLAYER));
        assertEquals(Person.Stage.CHILD, kid.stage());
        assertEquals(w.person(TEAMMATE_A).personality().archetype(), kid.personality().archetype());
        assertTrue(w.meters("resident:kid").affection() >= 55, "family starts close");
        assertFalse(w.romanceOpen("resident:kid"));
        assertEquals("too_soon", Household.refuse(w, w.day()));
        assertTrue(w.bond(TEAMMATE_A).remembers(Act.CHILD_BORN));
    }
    /** Friends with teammate_b until the day of their birthday. */
    static BondWorld friendsUntilTheirBirthday() {
        var w = Leaf.classic(12, 0);
        for (int d = 0; d < w.person(TEAMMATE_B).birthday(); d++) {
            w.talk(TEAMMATE_B); w.experience(Act.TRAINED_TOGETHER, List.of(TEAMMATE_B));
            if (d % 3 == 0) { w.experience(Act.MISSION_TOGETHER, List.of(TEAMMATE_B)); w.experience(Act.MEAL_TOGETHER, List.of(TEAMMATE_B)); }
            if (d == 5) w.moment(TEAMMATE_B, "bond.b.1");
            w.endDay();
        }
        assertTrue(w.level(TEAMMATE_B) >= Levels.FRIEND, "friends by now: " + w.level(TEAMMATE_B));
        return w;
    }

    @Test void birthdaysCountForFriends() {
        var w = friendsUntilTheirBirthday();
        var b = w.bond(TEAMMATE_B);
        w.endDay();
        assertTrue(b.remembers(Act.MISSED_BIRTHDAY), "a friend's birthday forgotten");
        var w2 = friendsUntilTheirBirthday();
        var b2 = w2.bond(TEAMMATE_B);
        assertTrue(w2.celebrate(TEAMMATE_B));
        assertFalse(w2.celebrate(TEAMMATE_B), "once a year");
        w2.endDay();
        assertTrue(b2.remembers(Act.BIRTHDAY_REMEMBERED));
        assertFalse(b2.remembers(Act.MISSED_BIRTHDAY));
        assertTrue(BondEffects.apply(w2, Map.of("celebrate_birthday", TEAMMATE_B)).equals("not_today"));
    }
}
