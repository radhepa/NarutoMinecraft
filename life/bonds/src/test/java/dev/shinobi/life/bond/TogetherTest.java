package dev.shinobi.life.bond;

import static dev.shinobi.life.bond.Leaf.*;
import static org.junit.jupiter.api.Assertions.*;

import java.util.List;
import org.junit.jupiter.api.Test;

/** Time together: schedules, tastes, invitations both ways, hangouts, rituals, highlights, life events and conversation. */
class TogetherTest {
    /** Friends with someone at a given level, the meters backing it. */
    static BondWorld friends(String who, int days) {
        var w = Leaf.classic(31, 0);
        for (int d = 0; d < days; d++) {
            w.talk(who); w.experience(Act.TRAINED_TOGETHER, List.of(who));
            if (d % 3 == 0) w.experience(Act.MISSION_TOGETHER, List.of(who));
            if (d % 10 == 5) w.moment(who, "bond.test." + d);
            w.endDay();
        }
        return w;
    }
    /** The first day from today when someone is free at an hour the activity is open. */
    static long[] slot(BondWorld w, String who, String activity) {
        return Schedule.nextFree(w.seed(), List.of(w.person(who)), Activity.of(activity), w.day(), 8, 10);
    }

    @Test void schedulesFollowTheirDays() {
        var kid = w0().person(TEAMMATE_A);
        assertEquals("lessons", Schedule.doing(1, kid, 0, 10), "Academy mornings on weekdays");
        assertEquals("free", Schedule.doing(1, kid, 5, 10), "not on the weekend");
        assertEquals("asleep", Schedule.doing(1, kid, 0, 23));
        var cook = w0().person(COOK);
        assertEquals("work", Schedule.doing(1, cook, 1, 12));
        var sensei = w0().person(SENSEI);
        long dutyDays = java.util.stream.LongStream.range(0, 200).filter(d -> Schedule.doing(1, sensei, d, 12).equals("duty")).count();
        assertTrue(dutyDays > 70 && dutyDays < 150, "a Jonin is away on duty about half the time: " + dutyDays);
    }
    static BondWorld w0() { return Leaf.classic(1, 0); }

    @Test void tastesComeFromPersonalityValuesAndTheirOwnFavorites() {
        var w = w0();
        var shy = w.person(TEAMMATE_A); var fiery = w.person(TEAMMATE_B);
        assertTrue(Activity.taste(w.seed(), shy, Activity.of("painting")) > Activity.taste(w.seed(), fiery, Activity.of("painting")));
        assertTrue(Activity.taste(w.seed(), fiery, Activity.of("roof_race")) > Activity.taste(w.seed(), shy, Activity.of("roof_race")));
        for (var p : w.people()) assertNotEquals(Activity.favorite(w.seed(), p.id()), Activity.leastFavorite(w.seed(), p.id()));
        assertFalse(Activity.of("lantern_night").open(0, 20) && Activity.of("flower_viewing").open(BondWorld.YEAR / 2, 12), "seasons and hours");
        assertTrue(Activity.of("stargazing").open(0, 22), "hours that wrap past midnight");
    }
    @Test void askingIsAnsweredForReasons() {
        var w = w0();
        var noPlan = Together.invite(w, List.of(TEAMMATE_A), "barbecue", 5, 19);
        assertEquals("not_close_enough", noPlan.answers().get(TEAMMATE_A));
        assertNull(noPlan.plan());
        assertEquals("not_like_that", Together.invite(w, List.of(TEAMMATE_A), "evening_walk", 5, 19).answers().get(TEAMMATE_A));
        assertEquals("too_many", Together.invite(w, List.of(TEAMMATE_A, TEAMMATE_B, RIVAL), "spar", 5, 10).answers().get("group"));
        var f = friends(TEAMMATE_A, 10);
        long weekday = f.day(); while (Schedule.weekend(weekday)) weekday++;
        var busy = Together.invite(f, List.of(TEAMMATE_A), "dango", weekday, 10);
        assertEquals("busy", busy.answers().get(TEAMMATE_A), "lessons");
        assertNotNull(busy.counter(), "with the next time they are free");
        w.quarrel(TEAMMATE_B, Act.QUARREL);
        assertEquals("cold", Together.invite(w, List.of(TEAMMATE_B), "ramen", 5, 13).answers().get(TEAMMATE_B));
    }
    @Test void closeFriendsSayYesToWhatTheyLoveMoreOften() {
        int yesFriend = 0, yesStranger = 0;
        for (int seed = 0; seed < 30; seed++) {
            var close = friends(TEAMMATE_B, 40);
            var stranger = Leaf.classic(31, 0);
            var s1 = slot(close, TEAMMATE_B, "ramen"); var s2 = slot(stranger, TEAMMATE_B, "ramen");
            close.advance(seed); stranger.advance(40 + seed);
            if (Together.invite(close, List.of(TEAMMATE_B), "ramen", close.day() + 1, 13).plan() != null) yesFriend++;
            if (Together.invite(stranger, List.of(TEAMMATE_B), "ramen", stranger.day() + 1, 13).plan() != null) yesStranger++;
            assertNotNull(s1); assertNotNull(s2);
        }
        assertTrue(yesFriend > yesStranger, yesFriend + " vs " + yesStranger);
    }
    @Test void aGreatHangoutLeavesAHighlightAndRepeatsBecomeARitual() {
        var w = friends(TEAMMATE_B, 40);
        String ritual = null; Together.Highlight highlight = null;
        for (int i = 0; i < 8; i++) {
            var s = slot(w, TEAMMATE_B, "ramen");
            var plan = new Together.Plan("plan.t" + i, List.of(TEAMMATE_B), "ramen", s[0], (int) s[1], BondWorld.PLAYER);
            w.plans.add(plan);
            while (w.day() < s[0]) w.endDay();
            var out = Together.go(w, plan.id(), true);
            assertNotEquals("stood_up", out.band());
            if (!out.newRituals().isEmpty()) ritual = out.newRituals().getFirst();
            if (out.highlight() != null) highlight = out.highlight();
            w.advance(3);
        }
        assertEquals(TEAMMATE_B + ":ramen", ritual, "our ramen");
        assertTrue(w.bond(TEAMMATE_B).rituals().contains("ramen"));
        assertTrue(w.bond(TEAMMATE_B).experiences(Act.Experience.MEAL) > 0);
        if (highlight != null) {
            w.advance(8);
            assertEquals("callback." + w.bond(TEAMMATE_B).highlights().getLast().key(), BondDialogue.callback(w, TEAMMATE_B).orElseThrow());
            assertTrue(BondDialogue.callback(w, TEAMMATE_B).isEmpty(), "not every day");
        }
        w.advance(Together.RITUAL_LAPSE * 2 + 1);
        assertFalse(w.bond(TEAMMATE_B).rituals().contains("ramen"), "a ritual lapses when nobody keeps it");
    }
    @Test void standingSomeoneUpHurts() {
        var w = friends(TEAMMATE_A, 30);
        double trust = w.meters(TEAMMATE_A).trust();
        w.plans.add(new Together.Plan("plan.x", List.of(TEAMMATE_A), "dango", w.day(), 15, BondWorld.PLAYER));
        w.endDay(); w.endDay();
        assertTrue(w.bond(TEAMMATE_A).remembers(Act.STOOD_UP), "a plan the player never came to");
        assertTrue(w.meters(TEAMMATE_A).trust() < trust);
    }
    @Test void hangingOutTogetherIntroducesFriends() {
        var w = friends(TEAMMATE_A, 30);
        for (int d = 0; d < 30; d++) { w.talk(CLASSMATE_D); w.experience(Act.TRAINED_TOGETHER, List.of(CLASSMATE_D)); w.endDay(); }
        var plan = new Together.Plan("plan.y", List.of(TEAMMATE_A, CLASSMATE_D), "market_stroll", w.day(), 14, BondWorld.PLAYER);
        w.plans.add(plan);
        var out = Together.go(w, plan.id(), true);
        if (!out.band().equals("rough")) assertTrue(w.bond(TEAMMATE_A, CLASSMATE_D).met(), "they got to know each other");
    }
    @Test void residentsInviteThePlayerAndStopWhenTurnedDownRepeatedly() {
        var w = friends(TEAMMATE_B, 40);
        int got = 0;
        for (int d = 0; d < 120 && got < 3; d++) {
            w.endDay();
            for (var inv : Together.invitations(w)) if (inv.from().equals(TEAMMATE_B)) { Together.answer(w, inv.id(), false); got++; }
        }
        assertEquals(3, got, "a friend at level " + w.level(TEAMMATE_B) + " asks the player out now and then");
        assertTrue(w.bond(TEAMMATE_B).remembers(Act.FELT_OVERLOOKED), "three refusals running");
        long quietFrom = w.day();
        for (int d = 0; d < Together.QUIET_DAYS - 1; d++) {
            w.endDay();
            assertTrue(Together.invitations(w).stream().noneMatch(i -> i.from().equals(TEAMMATE_B)), "they stop asking for a while (day " + (w.day() - quietFrom) + ")");
        }
    }
    @Test void acceptingAnInvitationMakesAPlanAtTheirChoice() {
        var w = friends(TEAMMATE_B, 40);
        Together.Invitation inv = null;
        for (int d = 0; d < 120 && inv == null; d++) { w.endDay(); inv = Together.invitations(w).stream().filter(i -> i.from().equals(TEAMMATE_B)).findFirst().orElse(null); }
        assertNotNull(inv);
        assertTrue(Activity.taste(w.seed(), w.person(TEAMMATE_B), Activity.of(inv.activity())) > 0, "they ask to do what they like");
        var plan = Together.answer(w, inv.id(), true);
        assertEquals(TEAMMATE_B, plan.host());
        assertTrue(Together.plans(w).contains(plan));
    }
    @Test void followUpsBringItBack() {
        var w = friends(TEAMMATE_A, 20);
        Together.share(w, TEAMMATE_A, "exam", 3);
        assertTrue(BondDialogue.followUp(w, TEAMMATE_A).isEmpty(), "not yet");
        w.advance(3);
        assertEquals("followup.exam", BondDialogue.followUp(w, TEAMMATE_A).orElseThrow());
        assertTrue(BondDialogue.followUp(w, TEAMMATE_A).isEmpty(), "once");
    }
    @Test void residentsHaveLivesAndHowYouRespondMatters() {
        var w = friends(TEAMMATE_B, 60);
        var b = w.bond(TEAMMATE_B);
        b.news.add(new LifeEvents.News(LifeEvents.Kind.INJURED, w.day(), false, -1, ""));
        assertEquals("life.injured", BondDialogue.lifeNews(w, TEAMMATE_B).orElseThrow());
        assertEquals("", LifeEvents.respond(w, TEAMMATE_B, "comfort"));
        assertTrue(b.remembers(Act.COMFORTED));
        if (w.effectiveLevel(TEAMMATE_B) >= LifeEvents.MOMENT_LEVEL) assertTrue(b.moments().stream().anyMatch(m -> m.startsWith("life.injured")), "a real moment");
        w.advance(15);
        assertTrue(Conversation.topics(w, TEAMMATE_B).contains("their_news"));
        assertEquals("life.injured.update", Conversation.talk(w, TEAMMATE_B, "their_news", null).key());
        assertTrue(b.remembers(Act.ASKED_AFTER_THEM));
        assertEquals("nothing_to_respond_to", LifeEvents.respond(w, TEAMMATE_B, "comfort"));
        b.news.add(new LifeEvents.News(LifeEvents.Kind.SICK, w.day(), false, -1, ""));
        BondDialogue.lifeNews(w, TEAMMATE_B);
        w.advance(LifeEvents.UNANSWERED_DAYS + 1);
        if (b.level() >= LifeEvents.MOMENT_LEVEL) assertTrue(b.memories().stream().anyMatch(m -> m.act() == Act.FELT_OVERLOOKED && m.day() > w.day() - 3),
                "a close friend's hard news, left unanswered");
    }
    @Test void lifeEventsHappenToTheKnownAndFitThem() {
        var w = friends(TEAMMATE_A, 10);
        w.advance(200);
        var news = w.bond(TEAMMATE_A).news();
        assertFalse(news.isEmpty(), "something happens in two hundred days");
        assertTrue(news.stream().noneMatch(n -> n.kind() == LifeEvents.Kind.HEARTBREAK), "children have no heartbreaks");
        assertTrue(w.bond(MERCHANT).news().isEmpty(), "nobody the player never met");
        assertTrue(news.stream().filter(n -> !n.shared()).allMatch(n -> true));
    }
    @Test void conversationsDeepenWithTheBond() {
        var w = Leaf.classic(31, 0);
        w.talk(RIVAL);
        assertFalse(Conversation.topics(w, RIVAL).contains("their_dream"));
        assertEquals("pried", Conversation.talk(w, RIVAL, "their_dream", null).reaction(), "too personal, too soon");
        assertTrue(w.bond(RIVAL).remembers(Act.PRIED));
        var friend = friends(TEAMMATE_B, 60);
        assertTrue(Conversation.topics(friend, TEAMMATE_B).contains("tease"));
        assertEquals("warm", Conversation.talk(friend, TEAMMATE_B, "tease", null).reaction(), "a fiery friend loves a bit of teasing");
        assertEquals("talk.tease.again", Conversation.talk(friend, TEAMMATE_B, "tease", null).key(), "once a day");
        var shy = friends(TEAMMATE_A, 60);
        if (shy.effectiveLevel(TEAMMATE_A) >= 4) assertEquals("awkward", Conversation.talk(shy, TEAMMATE_A, "tease", null).reaction(), "a shy one does not");
        if (friend.effectiveLevel(TEAMMATE_B) >= 6) {
            Conversation.talk(friend, TEAMMATE_B, "their_dream", null);
            assertTrue(friend.bond(TEAMMATE_B).facts().contains("dream"));
        }
        assertTrue(Conversation.talk(friend, TEAMMATE_B, "about_someone", TEAMMATE_A).key().startsWith("talk.opinion."));
    }
    @Test void timeTogetherSurvivesASave() {
        var w = friends(TEAMMATE_B, 40);
        var s = slot(w, TEAMMATE_B, "ramen");
        w.plans.add(new Together.Plan("plan.s", List.of(TEAMMATE_B), "ramen", s[0], (int) s[1], BondWorld.PLAYER));
        Together.share(w, TEAMMATE_B, "mission", 5);
        w.bond(TEAMMATE_B).news.add(new LifeEvents.News(LifeEvents.Kind.NEW_PET, w.day(), true, w.day(), ""));
        w.bond(TEAMMATE_B).rituals.add("ramen");
        var back = SaveFormat.read(SaveFormat.write(w), w.seed(), new java.util.ArrayList<>(w.people()));
        assertEquals(Together.plans(w), Together.plans(back));
        assertEquals(w.bond(TEAMMATE_B).followUps(), back.bond(TEAMMATE_B).followUps());
        assertEquals(w.bond(TEAMMATE_B).news(), back.bond(TEAMMATE_B).news());
        assertEquals(w.bond(TEAMMATE_B).rituals(), back.bond(TEAMMATE_B).rituals());
    }
}
