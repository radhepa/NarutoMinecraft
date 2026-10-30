package dev.shinobi.village.dialogue;

import static org.junit.jupiter.api.Assertions.*;

import java.util.Random;
import org.junit.jupiter.api.Test;

class QuestionsAndLedgerTest {
    static final Context FRIEND = Context.of("tier", "cast", "level", "5", "stage", "adult");

    @Test void aQuestionIsAskedUntilAnsweredThenNeverAgain() {
        var talk = new Fixture().question("q.food.sweet", 0, null, null, 1, "0", "0").talk();
        var r = Fixture.random();
        var q = talk.ask("x", FRIEND, 1, r);
        assertNotNull(q);
        assertNotNull(talk.ask("y", FRIEND, 1, r), "asked but unanswered: it can still come up");
        var a = talk.answer("x", q, "a2", FRIEND, 1);
        assertEquals("Reply 2", a.reply());
        assertEquals("a2", talk.heard().answer("q.food.sweet"));
        assertNull(talk.ask("z", FRIEND, 2, r), "answered once: never asked again, by anyone");
    }

    @Test void deeperQuestionsFollowTheirFirstAndComeFirst() {
        var talk = new Fixture()
                .question("q.plans.stay", 2, "stay_or_go", null, 1, "1", "-1")
                .question("q.plans.stay_deeper", 6, "stay_or_go", "q.plans.stay", 2, "1", "-1")
                .question("q.food.sweet", 0, null, null, 1, "0", "0")
                .talk();
        var r = new Random(3);
        var close = FRIEND.with("level", 7);
        assertNotEquals("q.plans.stay_deeper", talk.ask("x", close, 1, r).id(), "not before the first is answered");
        talk.answer("x", talk.question("q.plans.stay"), "a1", close, 1);
        assertEquals("q.plans.stay_deeper", talk.ask("x", close, 2, r).id(), "the follow-up comes first once open");
        var other = new Fixture()
                .question("q.plans.stay", 2, "stay_or_go", null, 1, "1", "-1")
                .question("q.plans.stay_deeper", 6, "stay_or_go", "q.plans.stay", 2, "1", "-1")
                .talk();
        other.answer("x", other.question("q.plans.stay"), "a1", close, 1);
        assertNull(other.ask("x", FRIEND.with("level", 3), 2, r), "the follow-up waits for its level");
    }

    @Test void aPerFriendQuestionIsAskedOnceByEachCloseFriend() {
        var talk = new Fixture().question(true, "q.pref.season", 2, null, null, 1, "0", "0").talk();
        var r = Fixture.random();
        var close = FRIEND.with("level", 5);
        talk.answer("x", talk.question("q.pref.season"), "a1", close, 1);
        assertFalse(talk.askable("x", talk.question("q.pref.season"), close, 2), "spent for the friend who asked it");
        assertTrue(talk.askable("y", talk.question("q.pref.season"), close, 2), "another close friend may ask it too");
        assertFalse(talk.askable("z", talk.question("q.pref.season"), FRIEND.with("level", 3), 2), "only close friends");
        var back = Heard.read(talk.heard().write(), 6);
        assertTrue(back.askedBy.contains(talk.question("q.pref.season").num() + "@x"), "kept in the save");
    }

    @Test void anAnswerOnTheOtherSideOfAnAxisIsAContradiction() {
        var talk = new Fixture()
                .question("q.plans.stay", 0, "stay_or_go", null, 1, "1", "-1")
                .question("q.plans.sea", 0, "stay_or_go", null, 1, "1", "-1")
                .talk();
        var first = talk.answer("x", talk.question("q.plans.stay"), "a1", FRIEND, 1);
        assertNull(first.contradicts());
        var second = talk.answer("y", talk.question("q.plans.sea"), "a2", FRIEND, 3);
        assertEquals("q.plans.stay", second.contradicts(), "said they'd stay, now they'd leave");
    }

    @Test void theLedgerSurvivesASaveAndStaysSmall() {
        var h = new Heard();
        var r = new Random(1);
        for (int k = 0; k < 25_000; k++) if (r.nextInt(10) < 7) h.lines.set(1 + r.nextInt(30_000));
        for (int k = 0; k < 2_000; k++) h.groups.set(1 + r.nextInt(6_000));
        for (int k = 0; k < 300; k++) {
            var s = h.speaker("resident:" + k, 6);
            s.roll(40); s.today = 2; s.lifetime = 30 + k % 50; s.fresh = 30; s.filler = 5;
            for (int n = 0; n < 6; n++) s.said(1 + r.nextInt(30_000));
        }
        for (int k = 0; k < 80; k++) h.answers.put("q.topic.question_" + k, "a" + (1 + k % 3));
        var saved = h.write();
        var back = Heard.read(saved, 6);
        assertEquals(h.lines, back.lines);
        assertEquals(h.groups, back.groups);
        assertEquals(h.answers, back.answers);
        assertEquals(h.speakers.get("resident:7").lifetime, back.speakers.get("resident:7").lifetime);
        assertArrayEquals(h.speakers.get("resident:7").recall, back.speakers.get("resident:7").recall);
        int size = h.size();
        assertTrue(size < 32_000, "a 100-hour save's ledger stays small: " + size + " bytes");
    }

    @Test void aNewerLedgerIsRefusedNotMisread() {
        var saved = new Heard().write();
        saved.put("format", Heard.FORMAT + 1);
        assertThrows(IllegalArgumentException.class, () -> Heard.read(saved, 6));
    }

    @Test void contextBandsFollowTheLevel() {
        assertEquals("stranger", Context.of("level", "0").get("band"));
        assertEquals("friend", Context.of("level", "4").get("band"));
        assertEquals("best", Context.of("level", "9").get("band"));
    }

    @Test void jsonReadsTheCompiledShapes() {
        var m = Json.map(Json.parse("{\"a\": [1, 2.5, \"x\\\"y\", true, null], \"b\": {\"c\": \"\\u00e9\"}}"));
        assertEquals(1L, Json.list(m.get("a")).get(0));
        assertEquals(2.5, Json.list(m.get("a")).get(1));
        assertEquals("x\"y", Json.list(m.get("a")).get(2));
        assertEquals("é", Json.map(m.get("b")).get("c"));
    }

    @Test void aNewLevelBringsItsOwnBand() {
        assertEquals("friend", Context.of("level", "9").with("level", 4).get("band"));
        assertEquals("best", Context.of("level", "0").with("level", "9").get("band"));
    }
}
