package dev.shinobi.village.dialogue;

import static org.junit.jupiter.api.Assertions.*;

import java.util.HashSet;
import java.util.List;
import org.junit.jupiter.api.Test;

class TalkTest {
    static final Context FIERY = Context.of("personality", "fiery", "time", "evening", "tier", "resident", "level", "2", "stage", "adult");

    @Test void theMostSpecificFreshLineWins() {
        var talk = new Fixture()
                .line("greet.time", "Anyone could say this.")
                .line("greet.time", "A fiery line.", "personality=fiery")
                .line("greet.time", "A fiery evening line.", "personality=fiery", "time=evening")
                .line("greet.time", "A stern line.", "personality=stern")
                .talk();
        var r = Fixture.random();
        assertEquals("A fiery evening line.", talk.greet("a", FIERY, 1, r).text());
        assertEquals("A fiery line.", talk.greet("b", FIERY, 1, r).text());
        assertEquals("Anyone could say this.", talk.greet("c", FIERY, 1, r).text());
        assertFalse(talk.greet("d", FIERY, 1, r).fresh(), "the stern line never fits a fiery speaker");
    }

    @Test void aHeardLineIsNeverChosenAgainWhileFreshOnesFit() {
        var f = new Fixture();
        for (int k = 0; k < 30; k++) f.line("chat.personal", "Line number " + k + ".");
        var talk = f.talk();
        var r = Fixture.random();
        var said = new HashSet<String>();
        // Thirty speakers, one fresh line each: every line once, none twice, across different people.
        for (int k = 0; k < 30; k++) {
            var s = talk.chat("resident:" + k, FIERY, 1, r);
            assertTrue(s.fresh());
            assertTrue(said.add(s.text()), "repeated " + s.text());
        }
        var after = talk.chat("resident:99", FIERY, 1, r);
        assertEquals(Talk.Why.EXHAUSTED, after.why());
        assertFalse(after.fresh());
    }

    @Test void oneVoiceOfAPieceOfContentSpendsTheOthers() {
        var talk = new Fixture()
                .grouped("chat.personal", "The gutters are singing. I put a pot out.", "personality=warmhearted")
                .grouped("chat.personal", "Listen to those gutters! Training weather!", "personality=fiery")
                .nextGroup()
                .line("chat.personal", "Something else entirely.")
                .talk();
        var r = Fixture.random();
        var warm = Context.of("personality", "warmhearted", "tier", "resident", "stage", "adult");
        assertTrue(talk.chat("warm", warm, 1, r).text().contains("pot"));
        assertEquals("Something else entirely.", talk.chat("fiery", FIERY, 1, r).text(), "the fiery voice of the gutters is spent");
    }

    @Test void childrenSpeakOnlyFromChildrensLines() {
        var talk = new Fixture()
                .line("chat.personal", "My wife says the roof leaks.")
                .line("chat.personal", "I lost my tooth at recess!", "stage=child")
                .talk();
        var kid = Context.of("stage", "child", "tier", "resident");
        var r = Fixture.random();
        assertEquals("I lost my tooth at recess!", talk.chat("kid", kid, 1, r).text());
        assertFalse(talk.chat("kid2", kid, 1, r).fresh());
    }

    @Test void theDailyBudgetThenAgainRepeatAndAPoliteClose() {
        var f = new Fixture();
        for (int k = 0; k < 20; k++) f.line("greet.time", "Hello number " + k + ".").line("chat.personal", "Chat number " + k + ".");
        f.repeat("again", "We already talked today.").repeat("close", "I'd better get back to it.");
        var talk = f.talk();
        var r = Fixture.random();
        var c = FIERY;
        assertTrue(talk.greet("x", c, 1, r).fresh(), "the first greeting of the day is free");
        for (int k = 0; k < 3; k++) assertTrue(talk.chat("x", c, 1, r).fresh(), "three fresh exchanges a day for a resident");
        var a = talk.chat("x", c, 1, r);
        assertEquals(Talk.Outcome.AGAIN, a.outcome());
        assertEquals(Talk.Why.BUDGET, a.why());
        var b = talk.chat("x", c, 1, r);
        assertEquals(Talk.Outcome.REPEAT, b.outcome());
        assertTrue(b.text().startsWith("Chat number") || b.text().startsWith("Hello number"), "a repeat is something they said before");
        var close = talk.chat("x", c, 1, r);
        assertEquals(Talk.Outcome.CLOSE, close.outcome());
        assertTrue(close.ended());
        assertTrue(talk.greet("x", c, 2, r).fresh(), "a new day, a new allowance");
        assertTrue(talk.chat("x", c, 2, r).fresh());
    }

    @Test void theLifetimeAllowanceGrowsWithTheBond() {
        var f = new Fixture();
        for (int k = 0; k < 60; k++) f.line("chat.personal", "Chat number " + k + ".");
        f.repeat("again", "Again?");
        var talk = f.talk();
        var r = Fixture.random();
        // Resident: 6 + 2 per level. At level 0 the seventh fresh exchange is refused, over several days.
        var stranger = Context.of("tier", "resident", "level", "0", "stage", "adult");
        int fresh = 0;
        for (int day = 1; day <= 5; day++) for (int k = 0; k < 3; k++) if (talk.chat("s", stranger, day, r).fresh()) fresh++;
        assertEquals(6, fresh);
        assertTrue(talk.chat("s", stranger.with("level", 2), 6, r).fresh(), "a closer bond: more to say");
        var cast = Context.of("tier", "cast", "level", "0", "stage", "adult");
        int castFresh = 0;
        for (int day = 1; day <= 8; day++) for (int k = 0; k < 6; k++) if (talk.chat("role:x", cast, day, r).fresh()) castFresh++;
        assertEquals(48, castFresh, "the cast has no lifetime cap: six a day, every day");
    }

    @Test void newsAndBondMomentsAreExemptFromTheBudget() {
        var talk = new Fixture()
                .line("chat.personal", "One.").line("chat.personal", "Two.").line("chat.personal", "Three.")
                .line("bond.heard.saved_life", "I heard what you did at the river.")
                .repeat("again", "Again?")
                .talk();
        var r = Fixture.random();
        for (int k = 0; k < 3; k++) talk.chat("x", FIERY, 1, r);
        assertFalse(talk.chat("x", FIERY, 1, r).fresh());
        var news = talk.say("x", List.of("bond.heard.saved_life"), FIERY, 1, r);
        assertTrue(news.fresh());
        assertEquals("I heard what you did at the river.", news.text());
    }

    @Test void fillerStaysUnderAFifthWhileOtherLinesFit() {
        var f = new Fixture();
        for (int k = 0; k < 20; k++) f.filler("chat.personal", "Nice weather number " + k + ".", "personality=fiery");
        for (int k = 0; k < 20; k++) f.line("chat.personal", "Story number " + k + ".");
        var talk = f.talk();
        var r = Fixture.random();
        int filler = 0;
        var cast = FIERY.with("tier", "cast");
        for (int day = 1; day <= 5; day++) for (int k = 0; k < 5; k++) if (talk.chat("role:x", cast, day, r).text().startsWith("Nice")) filler++;
        assertTrue(filler <= 5, "filler " + filler + " of 25, though the filler lines are the more specific ones");
        assertTrue(filler >= 3, "filler is capped, not banned: " + filler);
    }

    @Test void tokensAreFilledAndLinesThatCannotBeAreSkipped() {
        var talk = new Fixture()
                .line("chat.personal", "Have you seen {item}? Give it to {name:role:rival}.", "personality=fiery")
                .line("chat.personal", "Good to see you, {player}. {given:role:sensei} was asking after you.")
                .talk();
        var said = talk.chat("x", FIERY, 1, Fixture.random());
        assertEquals("Good to see you, Player. Sensei was asking after you.", said.text());
        assertEquals(Talk.Why.EXHAUSTED, talk.chat("y", FIERY, 1, Fixture.random()).why(), "no item and no rival here");
    }

    @Test void barksDealEveryLineOnceBeforeAnyComesBack() {
        var talk = new Fixture()
                .cycle("combat.fight_start.bandit", "Hand over the ryo!")
                .cycle("combat.fight_start.bandit", "Wrong road, kid.")
                .cycle("combat.fight_start.bandit", "Get them!")
                .talk();
        var r = Fixture.random();
        var c = Context.of("stage", "adult");
        var first = new HashSet<String>();
        for (int k = 0; k < 3; k++) first.add(talk.bark("combat.fight_start.bandit", c, r));
        assertEquals(3, first.size());
        var second = new HashSet<String>();
        for (int k = 0; k < 3; k++) second.add(talk.bark("combat.fight_start.bandit", c, r));
        assertEquals(first, second, "the second round deals the same three again");
        assertNull(talk.bark("combat.fight_start.rogue", c, r), "no pool: silence");
    }

    @Test void bondKeysWithAPersonalityPickThatVoiceFirst() {
        var talk = new Fixture()
                .line("talk.food", "Food, in general.")
                .line("talk.food", "FOOD! Ramen! Now!", "personality=fiery")
                .talk();
        var said = talk.say("x", List.of("talk.food.fiery", "talk.food"), FIERY, 1, Fixture.random());
        assertEquals("FOOD! Ramen! Now!", said.text());
        assertEquals("talk.food", Talk.normalize("talk.food.fiery"));
        assertEquals("bond.greet.level.3", Talk.normalize("bond.greet.level.3"));
        assertEquals("village.mood.proud", Talk.normalize("village.mood.proud"), "a mood, not a personality");
    }
}
