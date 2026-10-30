package dev.shinobi.village.dialogue;

import org.junit.jupiter.api.Test;
import java.nio.file.Path;
import java.util.List;
import java.util.Map;
import java.util.Random;
import java.util.Set;
import static org.junit.jupiter.api.Assertions.*;

/** Exercise the real authored bank: roles, reveal gates, answer memory and the pools the bond engine requests. */
class BetaDialogueTest {
    private Bank bank() { return Bank.load(Path.of(System.getProperty("dialogue.bank"))); }
    private final Names names = Names.of(Map.of("player.given", "Player"));
    private Context context(String role) {
        return Context.of("role", "role:" + role, "stage", List.of("teammate_a", "teammate_b", "rival", "classmate_c", "classmate_d").contains(role) ? "child" : "adult",
                "player_stage", "child", "tier", "cast", "level", "7", "personality", "fiery");
    }

    @Test void everyBetaRoleHasTenQuestionsAndAReplyForEveryRememberedAnswer() {
        var bank = bank();
        var roles = List.of("sensei", "instructor", "teammate_a", "teammate_b", "rival", "classmate_c", "classmate_d", "medic",
                "hokage_4", "elder_keeper", "librarian", "elder_councillor", "merchant", "porter", "sensei_2", "sensei_3", "sensei_4", "sensei_5", "squad3_a", "squad3_b", "squad3_c",
                "squad4_a", "squad4_b", "squad4_c", "squad5_a", "squad5_b", "squad5_c", "ramen_cook");
        for (String role : roles) {
            var questions = bank.questions().stream().filter(q -> q.id().startsWith("q.cast." + role + ".")).toList();
            assertEquals(10, questions.size(), role);
            for (var q : questions) for (var answer : q.answers()) {
                assertFalse(bank.pool(q.callbackPool(answer.id())).isEmpty(), q.id() + ": answer callback");
                assertFalse(bank.pool("talk.q." + role + "." + q.id().substring(q.id().lastIndexOf('.') + 1) + ".back").isEmpty(), q.id() + ": asks back");
            }
        }
    }

    @Test void storyMetadataDoesNotRequireOneArtificialStoryContextAndActualGatesStillHold() {
        var bank = bank();
        var heard = new Heard();
        var q = bank.question("q.cast.teammate_b.judge");
        var c = context("teammate_b");
        assertNull(c.get("story"));
        var before = new Talk(bank, heard, Conditions.basic(heard, Set.of()), names);
        assertFalse(before.askable("role:teammate_b", q, c, 1), "not before meeting the role");
        var after = new Talk(bank, heard, Conditions.basic(heard, Set.of("story.ch1.done")), names);
        assertTrue(after.askable("role:teammate_b", q, c, 1), "the real flag, not a story context tag, opens the question");
        assertFalse(after.askable("role:rival", q, context("rival"), 1), "another role cannot ask it");
        assertFalse(after.askable("role:teammate_b", q, c.with("player_stage", "adult"), 1), "beta voice stays in the beta");
    }

    @Test void answerCallbackAndAskBackSurviveSavingAndDoNotRememberAnUnchosenAnswer() {
        var bank = bank();
        var heard = new Heard();
        var c = context("teammate_b");
        var flags = Set.of("story.ch1.done");
        var talk = new Talk(bank, heard, Conditions.basic(heard, flags), names);
        var q = bank.question("q.cast.teammate_b.judge");
        String selected = q.callbackPool("a1"), other = q.callbackPool("a2");
        assertTrue(bank.pool(selected).stream().noneMatch(l -> Conditions.basic(heard, flags).test(l.when(), c)));
        talk.answer("role:teammate_b", q, "a1", c, 1);
        var restored = Heard.read(heard.write(), bank.rules().recall());
        var conditions = Conditions.basic(restored, flags);
        assertTrue(bank.pool(selected).stream().anyMatch(l -> conditions.test(l.when(), c)));
        assertTrue(bank.pool(other).stream().noneMatch(l -> conditions.test(l.when(), c)));
        assertTrue(bank.pool("talk.q.teammate_b.judge.back").stream().anyMatch(l -> conditions.test(l.when(), c)));
        assertEquals("a1", restored.answer(q.id()));
    }

    @Test void roleVoiceWinsOverPersonalityAndOldStoryStatesClose() {
        var bank = bank();
        var heard = new Heard();
        var talk = new Talk(bank, heard, Conditions.basic(heard, Set.of("story.ch0.done")), names);
        var said = talk.say("role:sensei", List.of("talk.food"), context("sensei"), 1, new Random(1));
        var chosen = bank.pool("talk.food").stream().filter(l -> l.id() == said.line().id()).findFirst().orElseThrow();
        assertTrue(chosen.tags().names("role"), "a role's food voice wins over the generic fiery voice");
        var q = bank.question("q.cast.porter.load");
        var before = new Talk(bank, new Heard(), Conditions.basic(new Heard(), Set.of("story.ch1.done")), names);
        assertTrue(before.askable("role:porter", q, context("porter"), 1));
        var after = new Talk(bank, new Heard(), Conditions.basic(new Heard(), Set.of("story.ch1.done", "story.ch28.done")), names);
        assertFalse(after.askable("role:porter", q, context("porter"), 1));
    }
}
