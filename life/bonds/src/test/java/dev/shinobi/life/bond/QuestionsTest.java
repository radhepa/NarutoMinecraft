package dev.shinobi.life.bond;

import static dev.shinobi.life.bond.Leaf.*;
import static org.junit.jupiter.api.Assertions.*;

import java.util.ArrayList;
import java.util.List;
import java.util.Map;
import org.junit.jupiter.api.Test;

/** Questions and choices: tags against personality, gating and pacing, the ledger, callbacks, contradictions, growth, gossip. */
class QuestionsTest {
    static BondWorld world(String who, int days) {
        var w = TogetherTest.friends(who, days);
        Questions.load(w, SampleQuestions.bank());
        return w;
    }
    static Question q(BondWorld w, String id) { return Questions.question(w, id); }

    @Test void theBankParsesAndRefusesBadQuestions() {
        var bank = SampleQuestions.bank();
        assertTrue(bank.size() >= 30);
        assertTrue(bank.stream().map(Question::kind).distinct().count() == Question.Kind.values().length, "every kind of question");
        var bad = new java.util.HashMap<>(SampleQuestions.raw().getFirst());
        bad.put("answers", List.of(Map.of("id", "only", "tags", List.of("kind"))));
        assertThrows(IllegalArgumentException.class, () -> Question.parse(bad));
        var badTag = new java.util.HashMap<>(SampleQuestions.raw().getFirst());
        badTag.put("answers", List.of(Map.of("id", "x", "tags", List.of("sarcastic")), Map.of("id", "y", "tags", List.of("kind"))));
        assertThrows(IllegalArgumentException.class, () -> Question.parse(badTag));
    }
    @Test void theSameAnswerLandsDifferentlyOnDifferentPeople() {
        var warm = Personality.of("warmhearted", ""); var stern = Personality.of("stern", ""); var proud = Personality.of("proud", "");
        var open = Personality.of("playful", ""); var shy = Personality.of("shy", "");
        var blunt = AnswerTag.BLUNT.react(warm);
        assertTrue(blunt.trust() > 0 && blunt.affection() < 0, "a blunt answer raises trust and costs warmth");
        assertTrue(AnswerTag.BLUNT.react(warm).affection() < AnswerTag.BLUNT.react(Personality.of("pragmatic", "")).affection(), "more so with the warm");
        assertTrue(AnswerTag.AMBITIOUS.react(proud).respect() > AnswerTag.AMBITIOUS.react(shy).respect(), "ambition impresses the proud");
        assertTrue(AnswerTag.PLAYFUL.react(open).affection() > AnswerTag.PLAYFUL.react(stern).affection(), "playful charms the open, grates on the disciplined");
        assertTrue(AnswerTag.DUTIFUL.react(stern).trust() > AnswerTag.DUTIFUL.react(open).trust());
        assertTrue(AnswerTag.RUDE.react(Personality.of("gentle", "")).affection() < AnswerTag.RUDE.react(Personality.of("pragmatic", "")).affection(), "a pet peeve");
    }
    @Test void questionsOpenByLevelAndAreNeverAskedTwice() {
        var w = Leaf.classic(31, 0);
        Questions.load(w, SampleQuestions.bank());
        assertTrue(Questions.next(w, TEAMMATE_B).isEmpty(), "strangers ask nothing");
        var f = world(TEAMMATE_B, 60);
        int level = f.effectiveLevel(TEAMMATE_B);
        var seen = new java.util.HashSet<String>();
        for (int d = 0; d < 300; d++) {
            var q = Questions.next(f, TEAMMATE_B);
            if (q.isPresent()) {
                assertTrue(q.get().level() <= f.effectiveLevel(TEAMMATE_B));
                assertTrue(q.get().suits(f.person(TEAMMATE_B)));
                assertTrue(seen.add(q.get().id()), "never asked twice: " + q.get().id());
                if (!q.get().followUpOf().isEmpty()) assertTrue(Questions.answered(f, TEAMMATE_B, q.get().followUpOf(), ""));
                Questions.answer(f, TEAMMATE_B, q.get().id(), q.get().answers().getFirst().id());
            }
            f.endDay();
        }
        assertFalse(seen.contains("q.role.sensei.why_shinobi"), "another character's question");
        assertFalse(seen.contains("q.pref.paint_me"), "not for a fiery teammate");
        assertTrue(seen.size() > 10, level + " " + seen);
        assertTrue(f.questionsDry() > 0, "the sample bank runs dry for a close friend: the real bank needs more");
    }
    @Test void theBudgetPacesQuestions() {
        var w = world(TEAMMATE_B, 60);
        var first = Questions.next(w, TEAMMATE_B).orElseThrow();
        assertEquals(first, Questions.next(w, TEAMMATE_B).orElseThrow(), "an unanswered question waits");
        Questions.answer(w, TEAMMATE_B, first.id(), first.answers().getFirst().id());
        assertTrue(Questions.next(w, TEAMMATE_B).isEmpty(), "one a day");
        int level = w.effectiveLevel(TEAMMATE_B);
        for (int d = 1; d < Questions.gap(level); d++) { w.endDay(); assertTrue(Questions.next(w, TEAMMATE_B).isEmpty(), "a gap of " + Questions.gap(level) + " days"); }
        w.endDay();
        assertTrue(Questions.next(w, TEAMMATE_B).isPresent());
        assertTrue(Questions.gap(8) < Questions.gap(2), "close friends ask more often");
        var many = Leaf.classic(31, 0);
        Questions.load(many, SampleQuestions.bank());
        for (String c : CLASSMATES) for (int d = 0; d < 40; d++) { many.talk(c); many.experience(Act.TRAINED_TOGETHER, List.of(c)); }
        many.endDay();
        int asked = 0;
        for (String c : CLASSMATES) if (Questions.next(many, c).isPresent()) asked++;
        assertTrue(asked <= Questions.DAILY_CAP, "at most one a day across everyone");
    }
    @Test void answersAreRememberedAndBroughtUp() {
        var w = world(TEAMMATE_B, 60);
        Questions.ask(w, TEAMMATE_B, "q.dilemma.found_wallet");
        var out = Questions.answer(w, TEAMMATE_B, "q.dilemma.found_wallet", "return_it");
        assertEquals("answer.q.dilemma.found_wallet.return_it", out.lineKey());
        assertNotEquals("", w.bond(TEAMMATE_B).mood(w.day()));
        assertTrue(w.bond(TEAMMATE_B).remembers(Act.ANSWERED));
        assertTrue(BondConditions.test(w, Map.of("answered", List.of(TEAMMATE_B, "q.dilemma.found_wallet", "return_it"))));
        assertFalse(BondConditions.test(w, Map.of("answered", List.of(TEAMMATE_B, "q.dilemma.found_wallet", "keep_it"))));
        assertTrue(Questions.callback(w, TEAMMATE_B).isEmpty(), "not yet");
        w.advance(Questions.CALLBACK_AFTER);
        assertEquals("callback.answer.q.dilemma.found_wallet.return_it", Questions.callback(w, TEAMMATE_B).orElseThrow());
        assertTrue(Questions.callback(w, TEAMMATE_B).isEmpty(), "once, and not again for two weeks");
    }
    @Test void sayingTheOppositeLaterCanBeNoticed() {
        int noticedHonest = 0, noticedPlayful = 0, contradictions = 0;
        for (int seed = 0; seed < 40; seed++) {
            for (String who : List.of(TEAMMATE_B, CLASSMATE_C)) {
                var w = Leaf.classic(seed, 0);
                Questions.load(w, SampleQuestions.bank());
                for (int d = 0; d < 50; d++) { w.talk(who); w.experience(Act.MISSION_TOGETHER, List.of(who)); if (d % 10 == 5) w.moment(who, "m" + d); w.endDay(); }
                Questions.ask(w, who, "q.dilemma.found_wallet");
                Questions.answer(w, who, "q.dilemma.found_wallet", "return_it");
                w.advance(5);
                Questions.ask(w, who, "q.dilemma.friend_cheats");
                var out = Questions.answer(w, who, "q.dilemma.friend_cheats", "let_it_go");
                assertTrue(out.contradiction(), "honest, then not");
                contradictions++;
                if (out.noticed()) { if (who.equals(CLASSMATE_C)) noticedHonest++; else noticedPlayful++; }
                if (out.noticed()) { assertEquals("noticed_contradiction", out.reaction()); assertTrue(w.bond(who).remembers(Act.CAUGHT_CONTRADICTION)); }
            }
        }
        assertTrue(noticedHonest > noticedPlayful, "someone who lives by honesty notices more: " + noticedHonest + " vs " + noticedPlayful);
        var w = world(TEAMMATE_B, 60);
        Questions.ask(w, TEAMMATE_B, "q.dilemma.found_wallet"); Questions.answer(w, TEAMMATE_B, "q.dilemma.found_wallet", "return_it");
        w.advance(Questions.CHANGED_MIND + 1);
        Questions.ask(w, TEAMMATE_B, "q.dilemma.friend_cheats");
        assertFalse(Questions.answer(w, TEAMMATE_B, "q.dilemma.friend_cheats", "let_it_go").contradiction(), "a year later, people change");
    }
    @Test void adviceCanShapeThemAndQuestsReadIt() {
        var w = world(TEAMMATE_A, 40);
        double before = w.person(TEAMMATE_A).personality().boldness();
        Questions.ask(w, TEAMMATE_A, "q.advice.first_mission");
        Questions.answer(w, TEAMMATE_A, "q.advice.first_mission", "go_for_it");
        assertEquals(before + .05, w.person(TEAMMATE_A).personality().boldness(), 1e-9, "they took it to heart");
        Questions.ask(w, TEAMMATE_A, "q.advice.quit_or_not");
        Questions.answer(w, TEAMMATE_A, "q.advice.quit_or_not", "keep_going");
        assertTrue(w.bond(TEAMMATE_A).has("growth.kept_going"), "a flag a quest variant can read");
        var base = new ArrayList<>(Leaf.classic(31, 0).people());
        var back = SaveFormat.read(SaveFormat.write(w), w.seed(), base);
        assertEquals(w.person(TEAMMATE_A).personality().boldness(), back.person(TEAMMATE_A).personality().boldness(), 1e-9, "growth survives a save");
        assertEquals(w.bond(TEAMMATE_A).answers(), back.bond(TEAMMATE_A).answers());
    }
    @Test void publicAnswersTravelAndCanBeCaughtByOthers() {
        var w = Leaf.classic(4, 0);
        var uchiha1 = Leaf.person("u1", "uchiha", "quarter:uchiha", 2, Person.Stage.ADULT, Personality.of("proud", ""), "MALE", "FEMALE", 3, List.of("household:u"));
        var uchiha2 = Leaf.person("u2", "uchiha", "quarter:uchiha", 2, Person.Stage.ADULT, Personality.of("thoughtful", ""), "FEMALE", "MALE", 4, List.of("household:u"));
        w.add(uchiha1); w.add(uchiha2);
        Village.settle(w);
        Questions.load(w, SampleQuestions.bank());
        for (int d = 0; d < 30; d++) { for (String u : List.of("u1", "u2")) { w.talk(u); w.experience(Act.TRAINED_TOGETHER, List.of(u)); } w.endDay(); }
        double standing = w.standing("clan:uchiha");
        Questions.ask(w, "u1", "q.opinion.uchiha");
        var out = Questions.answer(w, "u1", "q.opinion.uchiha", "stuck_up");
        assertTrue(out.deedSerial() > 0);
        assertEquals("clan:uchiha=dislikes", w.deedOf(out.deedSerial()).note());
        for (int d = 0; d < 10 && !w.deedOf(out.deedSerial()).knows("u2"); d++) w.endDay();
        assertTrue(w.deedOf(out.deedSerial()).knows("u2"), "word reached their household");
        assertTrue(w.standing("clan:uchiha") < standing, "the clan heard what you said about it");
        Questions.ask(w, "u2", "q.opinion.uchiha");
        assertTrue(Questions.answer(w, "u2", "q.opinion.uchiha", "respect_them").contradiction(), "telling one of them the opposite");
    }
    @Test void theDialogueBankHasAPoolForEveryQuestion() {
        var keys = DialogueKeys.forQuestions(SampleQuestions.bank());
        assertTrue(keys.contains("question.q.dilemma.found_wallet"));
        assertTrue(keys.contains("answer.q.dilemma.found_wallet.return_it"));
        assertTrue(keys.contains("callback.answer.q.dilemma.found_wallet.return_it"));
        assertTrue(keys.contains("answer.contradiction.value:honesty"));
        assertTrue(DialogueKeys.required().containsAll(DialogueKeys.REACTIONS.stream().map(r -> "reaction." + r).toList()));
    }
    @Test void nudgesPastTheEdgeOfATraitPlayTheSameAfterAReload() {
        var w = world(TEAMMATE_A, 40);
        var p = w.person(TEAMMATE_A).personality();
        w.add(w.person(TEAMMATE_A).withPersonality(p.withTraits(p.warmth(), .98, p.pride(), p.discipline(), p.openness())));
        var base = new ArrayList<>(w.people());
        Questions.answer(w, TEAMMATE_A, "q.advice.first_mission", "go_for_it");
        assertEquals(1, w.person(TEAMMATE_A).personality().boldness(), 1e-9);
        Questions.answer(w, TEAMMATE_A, "q.advice.first_mission", "be_careful");
        assertEquals(.98, w.person(TEAMMATE_A).personality().boldness(), 1e-9, "the nudges cancel out");
        var back = SaveFormat.read(SaveFormat.write(w), w.seed(), base);
        assertEquals(.98, back.person(TEAMMATE_A).personality().boldness(), 1e-9, "and a reload agrees");
    }
    @Test void questionsGoneFromTheBankAreSkippedNotThrown() {
        var w = world(TEAMMATE_B, 40);
        var b = w.bond(TEAMMATE_B);
        b.answers.add(new Questions.Answered("q.gone", "x", w.day(), "", "", false));
        b.pendingQuestion = "q.gone"; b.pendingSince = w.day();
        var next = assertDoesNotThrow(() -> Questions.next(w, TEAMMATE_B));
        assertTrue(next.isEmpty() || !next.get().id().equals("q.gone"));
    }
}
