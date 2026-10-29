package dev.shinobi.life.bond;

import static dev.shinobi.life.bond.Leaf.*;
import static org.junit.jupiter.api.Assertions.*;

import dev.shinobi.life.bond.sim.VillageSim;
import java.util.List;
import java.util.Map;
import org.junit.jupiter.api.Test;

/** The Leaf at village scale: the sparse social graph, clans, relations, moods, tiers, hooks and the cost of it all. */
class VillageScaleTest {
    static Person member(String id, String clan, String district) {
        return Leaf.person(id, clan, district, 2, Person.Stage.ADULT, Personality.of("steadfast", "honor_their_clan"), "MALE", "FEMALE", 5, List.of());
    }

    @Test void everyoneHasABoundedSetOfRealTies() {
        var w = VillageSim.populate(1, 300);
        var v = Village.settle(w);
        for (var p : w.people()) {
            long chosen = v.tiesOf(p.id()).stream().filter(o -> v.tie(p.id(), o).chosen()).count();
            assertTrue(chosen <= Village.CHOSEN_TIES, p.id() + " has " + chosen);
            for (String kin : p.family().keySet()) assertNotNull(v.tie(p.id(), kin), "family are tied");
        }
        assertTrue(v.tieCount() < 300 * 15, "sparse: " + v.tieCount() + " ties, not 45,000 pairs");
        var spouses = w.people().stream().filter(p -> p.family().containsValue("spouse")).findFirst().orElseThrow();
        String partner = spouses.family().entrySet().stream().filter(e -> e.getValue().equals("spouse")).findFirst().orElseThrow().getKey();
        assertEquals("spouse", v.tie(spouses.id(), partner).kind(), "the closest kind of tie wins");
    }
    @Test void clansHaveAHeadEldersAnHeirAndHouseholds() {
        var w = VillageSim.populate(3, 300);
        var v = Village.settle(w);
        assertFalse(v.houses().isEmpty());
        for (var h : v.houses()) {
            assertFalse(h.head().isEmpty());
            assertEquals(h.clan(), w.person(h.head()).clan());
            assertFalse(h.elders().contains(h.head()));
            assertTrue(h.elders().size() <= ClanProfile.of(h.clan()).elders());
            assertEquals(w.people().stream().filter(p -> p.clan().equals(h.clan())).count(), h.households().values().stream().mapToLong(List::size).sum());
            if (!ClanProfile.of(h.clan()).branchHouse()) assertTrue(h.branch().isEmpty());
        }
        var shaped = ClanProfile.of("hyuga").shape(Personality.of("playful", "see_the_world"));
        assertTrue(shaped.discipline() > Personality.of("playful", "").discipline(), "a strict upbringing");
        assertTrue(shaped.holds(Personality.Value.DUTY));
    }
    @Test void strangersFeelTheirClansRelation() {
        var w = new BondWorld(5, 0);
        for (var p : List.of(member("nara1", "nara", "x"), member("akimichi1", "akimichi", "y"), member("inuzuka1", "inuzuka", "x"), member("aburame1", "aburame", "y")))
            w.add(p);
        var v = Village.settle(w);
        assertTrue(v.affinity("nara1", "akimichi1") > v.affinity("inuzuka1", "aburame1") + 10, "old allies versus an old grudge");
        assertEquals(ClanRelations.Label.ALLIES, v.relations().label("nara", "yamanaka"));
        v.link("inuzuka1", "aburame1", "neighbor"); v.link("inuzuka1", "nara1", "neighbor");
        var c = v.contacts("inuzuka1");
        assertTrue(c.get("aburame1") < c.get("nara1"), "news crosses a grudge more slowly");
    }
    @Test void relationsDriftBackButMarriagesLast() {
        var r = new ClanRelations();
        double base = r.base("uchiha", "hyuga");
        r.event("uchiha", "hyuga", -30, "incident", 0);
        assertEquals(base - 30, r.get("uchiha", "hyuga"), 1e-9);
        for (int i = 0; i < 80; i++) r.week();
        assertEquals(base, r.get("uchiha", "hyuga"), 1);
        r.married("uchiha", "hyuga", 1);
        for (int i = 0; i < 80; i++) r.week();
        assertTrue(r.get("uchiha", "hyuga") > base, "a marriage leaves the clans a little warmer for good");
        assertEquals(1, Village.marriageChance("hyuga", "hyuga"));
        assertTrue(Village.marriageChance("hyuga", "uchiha") < Village.marriageChance("haruno", "umino"), "strict clans marry in");
    }
    @Test void rumorsBendWithTheTellersFeelings() {
        var m = Meters.of(4, 4, 2, 0);
        assertTrue(Gossip.slanted(m, .5).trust() > m.trust());
        assertTrue(Gossip.slanted(Meters.of(-4, -4, 0, 0), .5).trust() > -4, "a kind telling softens bad news");
        assertTrue(Gossip.slanted(m, -.5).affection() < m.affection());
        var w = Leaf.classic(2, 0);
        w.formSquad("squad:7", SENSEI, TEAMMATES, List.of());
        for (int d = 0; d < 30; d++) { w.talk(TEAMMATE_A); w.experience(Act.MISSION_TOGETHER, List.of(TEAMMATE_A)); w.endDay(); }
        w.moment(TEAMMATE_A, "a"); w.moment(TEAMMATE_A, "b");
        var d = w.deed(Act.PROTECTED_THEM, MERCHANT, List.of(TEAMMATE_A));
        assertTrue(Gossip.slant(w, d, d.know(TEAMMATE_A), TEAMMATE_A, TEAMMATE_B, w.day()) > 0, "a friend tells it kindly");
    }
    @Test void moodsRiseWithEventsAndEase() {
        var w = Leaf.classic(2, 0);
        var v = Village.settle(w);
        v.push("village", .7, 0);
        assertEquals(Mood.Label.FESTIVE, v.mood("village").label());
        assertTrue(BondConditions.test(w, Map.of("village_mood", List.of("village", "festive"))));
        w.advance(20);
        assertEquals(Mood.Label.CALM, v.mood("village").label());
        w.deed(Act.HURT_RESIDENT, COOK, List.of());
        assertTrue(v.mood("district:market").tension() > 0, "harm makes a district uneasy");
        assertEquals(Mood.Label.TENSE, new Mood(0, .7).label());
        assertEquals(Mood.Label.GRIEVING, new Mood(-.5, .2).label());
    }
    @Test void backgroundResidentsAreUpdatedWeeklyUntilTheyAreMet() {
        var w = VillageSim.populate(4, 120);
        var v = Village.settle(w);
        assertEquals(Village.Tier.CAST, v.tier(TEAMMATE_A));
        assertEquals(Village.Tier.BACKGROUND, v.tier("resident:3"));
        v.meet("resident:3");
        assertEquals(Village.Tier.KNOWN, v.tier("resident:3"));
        String kin = w.person("resident:3").family().keySet().stream().findFirst().orElse(null);
        if (kin != null) {
            int before = v.tie("resident:3", kin).together();
            w.endDay();
            assertEquals(before + 1, v.tie("resident:3", kin).together(), "a known resident's daily ties tick every day");
        }
    }
    @Test void hooksCarryASchemaQuestsCanBindToAndResolve() {
        var w = new BondWorld(6, 0);
        for (var p : List.of(member("a", "inuzuka", "x"), member("b", "aburame", "x"))) w.add(p);
        var v = Village.settle(w);
        v.link("a", "b", "friend");
        var h = v.raise("clan_feud", Map.of("clan_a", "inuzuka", "clan_b", "aburame", "a", "a", "b", "b"), "village", 14, .5,
                List.of(Map.of("rank_at_least", "genin")), Map.of("relation", List.of("inuzuka", "aburame", 10)));
        var json = h.toMap();
        for (String key : List.of("format", "id", "type", "roles", "place", "raised", "expires", "urgency", "requires", "stakes", "outcomes")) assertTrue(json.containsKey(key), key);
        assertEquals(Map.of("all", List.of(Map.of("rank_at_least", "genin"))), json.get("requires"));
        assertTrue(BondConditions.test(w, Map.of("hook_open", h.id())));
        assertNull(v.raise("clan_feud", h.roles(), "village", 14, .5, List.of(), Map.of()), "no duplicates");
        double before = v.relations().get("inuzuka", "aburame");
        assertEquals("", BondEffects.apply(w, Map.of("resolve_hook", List.of(h.id(), "mediated"))));
        assertTrue(v.relations().get("inuzuka", "aburame") > before);
        assertTrue(w.bond("a").remembers(Act.MEDIATED));
        assertFalse(BondConditions.test(w, Map.of("hook_open", h.id())));
        assertEquals("no_hook", v.resolve(h.id(), "mediated"));
        var lapse = v.raise("lost_item", Map.of("owner", "a"), "district:x", 2, .2, List.of(), Map.of());
        w.advance(4);
        assertNull(v.hook(lapse.id()), "an unanswered hook lapses");
        assertThrows(IllegalArgumentException.class, () -> new SocietyHook("x", "dragon", Map.of(), "", 0, 1, 0, List.of(), Map.of()));
    }
    @Test void favorsSayWhatKindOfHelp() {
        var r = VillageSim.run(5, 300, 56, 2);
        var favors = r.world().village().hooks().stream().filter(h -> h.type().equals("favor_needed")).toList();
        var w = r.world();
        for (var h : favors) assertTrue(SocietyHook.FAVOR_VARIANTS.contains((String) h.stakes().get("variant")), h.stakes().toString());
        var shopkeeper = w.people().stream().filter(p -> !p.shinobi() && p.circles().stream().anyMatch(c -> c.startsWith("work:"))).findFirst().orElseThrow();
        var seen = new java.util.TreeSet<String>();
        for (long d = 0; d < 200; d++) seen.add(w.village().favorVariant(shopkeeper, d));
        assertTrue(seen.contains("shop_trouble") && !seen.contains("festival_help") || w.village().mood("village").cheer() >= .2, seen.toString());
    }
    @Test void relativesWhoStopSpeakingBecomeAnEstrangementAfterTheBeta() {
        var w = new BondWorld(9, 0);
        var mother = new Person("mother", "", "x", Person.CIVILIAN, Person.Stage.ADULT, Personality.of("proud", ""), "FEMALE", "MALE", 1, Map.of("son", "child"), List.of());
        var son = new Person("son", "", "x", Person.CIVILIAN, Person.Stage.ADULT, Personality.of("fiery", ""), "MALE", "FEMALE", 2, Map.of("mother", "parent"), List.of());
        w.add(mother); w.add(son);
        var v = Village.settle(w);
        v.meet("son");
        double close = v.affinity("mother", "son");
        String key = ClanRelations.pair("mother", "son");
        v.ties.put(key, v.tie("mother", "son").quarrel(w.day()));
        w.advance(Village.ESTRANGED_DAYS + 14);
        var sore = v.tie("mother", "son");
        double withQuarrel = v.affinity("mother", "son");
        v.ties.put(key, sore.reconciled());
        double without = v.affinity("mother", "son");
        v.ties.put(key, sore);
        assertEquals(without - Village.KIN_GRUDGE, withQuarrel, 1e-9, "a family quarrel does not just fade");
        assertTrue(close > 0);
        assertTrue(v.hooks().stream().noneMatch(h -> h.type().equals("estrangement")), "not while the player is a child");
        w.setPlayerStage(Person.Stage.TEEN);
        w.advance(Village.WEEK + 1);
        var h = v.hooks().stream().filter(x -> x.type().equals("estrangement")).findFirst().orElseThrow();
        assertEquals(Map.of("a", "mother", "b", "son"), h.roles());
        assertEquals(List.of("reconciled", "failed"), h.toMap().get("outcomes"));
        assertEquals("", v.resolve(h.id(), "reconciled"));
        assertTrue(v.tie("mother", "son").quarrel() < 0);
        assertTrue(w.bond("son").remembers(Act.MEDIATED));
    }
    @Test void secretCrushHooksWaitForThePostBetaRules() {
        var w = new BondWorld(7, 0);
        var x = Leaf.person("x", "", "x", 1, Person.Stage.ADULT, Personality.of("warmhearted", ""), "FEMALE", "ANY", 1, List.of());
        var y = Leaf.person("y", "", "x", 1, Person.Stage.ADULT, Personality.of("gentle", ""), "MALE", "ANY", 2, List.of());
        w.add(x); w.add(y);
        var v = Village.settle(w);
        v.link("x", "y", "friend"); v.meet("x");
        w.advance(Village.WEEK * 30);
        assertEquals(0, (int) v.raisedByType().getOrDefault("secret_crush", 0), "nothing romantic surfaces while the player is a child");
        assertTrue(List.of("friend", "sweetheart", "spouse").contains(v.tie("x", "y").kind()), "but adults still fall in love in the background");
    }
    @Test void theClanBornAreOneOfTheirOwnAndTheClanlessMakeFriends() {
        var born = Leaf.classic(1, 0); born.player("MALE", "uchiha");
        var clanless = Leaf.classic(1, 0);
        for (var w : List.of(born, clanless)) { w.talk(RIVAL); w.endDay(); }
        assertTrue(born.meters(RIVAL).affection() > clanless.meters(RIVAL).affection() + 5);
        assertFalse(BondConditions.test(clanless, Map.of("clan_friendship", List.of("kurama", 7))));
        clanless.bond(TEAMMATE_A).level = 7;
        assertTrue(BondConditions.test(clanless, Map.of("clan_friendship", List.of("kurama", 7))), "a friend in the clan can teach a lesser technique");
    }
    @Test void kindlingCountsUsesAndASpouseBurnsLongest() {
        var w = Leaf.classic(1, 0);
        w.setFlag(Kindling.UNLOCK_FLAG, true);
        w.bond(TEAMMATE_A).level = 8;
        w.formSquad("squad:7", SENSEI, TEAMMATES, List.of());
        assertEquals(Kindling.grant(Kindling.Tier.FULL), w.kindle(TEAMMATE_A));
        assertEquals("", BondEffects.apply(w, Map.of("kindle", TEAMMATE_A)));
        assertTrue(BondConditions.test(w, Map.of("kindling_uses", List.of(TEAMMATE_A, 2))));
        assertEquals("no_bond", BondEffects.apply(w, Map.of("kindle", RIVAL)));
        assertTrue(Kindling.grant(Kindling.Tier.FULL, true).duration() > Kindling.grant(Kindling.Tier.FULL).duration());
    }
    @Test void theBondWebCountsDepthAndReach() {
        var w = Leaf.classic(1, 0);
        assertEquals(0, BondWeb.score(w));
        for (String c : List.of(TEAMMATE_A, RIVAL)) { w.bond(c).meet(0); w.bond(c).level = 6; }
        int two = BondWeb.score(w);
        w.bond(TEAMMATE_A).level = 10;
        assertTrue(BondWeb.score(w) > two);
        assertTrue(BondConditions.test(w, Map.of("bond_web", two)));
    }
    @Test void dyingOnAMissionCostsStandingWithTheClient() {
        var w = Leaf.classic(1, 10);
        double before = w.standing("district:market");
        w.act(MERCHANT, Act.FAILED_CLIENT, List.of(COOK));
        w.advance(3);
        assertTrue(w.standing("district:market") < before);
        assertEquals(Conflict.State.NONE, w.bond(MERCHANT).conflict().state(), "a failed mission is not a quarrel");
    }
    @Test void theVillageSavesAndLoads() {
        var w = VillageSim.populate(8, 120);
        var v = Village.settle(w);
        v.relations().event("uchiha", "hyuga", -12, "incident", 0);
        v.push("village", .4, .1);
        w.advance(30);
        var back = Village.read(w, v.write());
        assertEquals(v.tieKinds(), back.tieKinds());
        assertEquals(v.relations().get("uchiha", "hyuga"), back.relations().get("uchiha", "hyuga"), 1e-9);
        assertEquals(v.mood("village"), back.mood("village"));
        assertEquals(v.hooks().stream().map(SocietyHook::toMap).toList(), back.hooks().stream().map(SocietyHook::toMap).toList());
    }
    @Test void aVillageOfThreeHundredIsCheapAndBusyEnough() {
        var r = VillageSim.run(20261029L, 300, 56, 2);
        assertTrue(r.msPerDay() < 100, "cost " + r.msPerDay() + " ms a day");
        assertTrue(r.chosenPerResident() >= 3 && r.maxChosen() <= Village.CHOSEN_TIES);
        assertTrue(r.visiblePerWeek() >= 2 && r.visiblePerWeek() <= 16, "hooks a week " + r.visiblePerWeek());
        var again = VillageSim.run(20261029L, 300, 56, 2);
        assertEquals(r.tieKinds(), again.tieKinds(), "deterministic");
        assertEquals(r.raised(), again.raised());
        assertEquals(r.drift(), again.drift());
    }
}
