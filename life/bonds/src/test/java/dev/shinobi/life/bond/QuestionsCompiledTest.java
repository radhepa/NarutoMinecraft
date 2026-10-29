package dev.shinobi.life.bond;

import static dev.shinobi.life.bond.Leaf.*;
import static org.junit.jupiter.api.Assertions.*;

import java.util.List;
import java.util.Map;
import org.junit.jupiter.api.Test;

/** The dialogue data's compiled question shape: values, tone, pole, axis, follows, tags. */
class QuestionsCompiledTest {
    static Map<String, Object> honestOrKind() {
        return Map.of("id", "q.values.honest_or_kind", "num", 7, "fn", List.of("reveal_character", "deepen_bond"), "level", 3, "axis", "honesty_vs_kindness",
                "depth", 1, "tags", Map.of(), "asks", List.of("..."),
                "answers", List.of(
                        Map.of("id", "a1", "label", "Tell them, gently", "reply", "...", "values", Map.of("honesty", 1), "tone", "warm", "pole", 1),
                        Map.of("id", "a2", "label", "Say it's lovely", "reply", "...", "values", Map.of("kindness", 1, "honesty", -1), "tone", "warm", "pole", -1),
                        Map.of("id", "a3", "label", "Ask what they think", "reply", "...", "values", Map.of("knowledge", 1), "tone", "curious")));
    }
    static Map<String, Object> honestOrKindAgain() {
        return Map.of("id", "q.values.honest_or_kind_again", "num", 8, "level", 3, "axis", "honesty_vs_kindness", "depth", 2, "follows", "q.values.honest_or_kind",
                "tags", Map.of("personality", List.of("thoughtful")), "answers", List.of(
                        Map.of("id", "b1", "values", Map.of("honesty", 1), "tone", "blunt", "pole", 1),
                        Map.of("id", "b2", "values", Map.of("kindness", 1), "tone", "warm", "pole", -1)));
    }

    @Test void theCompiledShapeParses() {
        var q = Question.parse(honestOrKind());
        assertEquals(Question.Kind.DILEMMA, q.kind(), "q.values is a dilemma");
        assertEquals("honesty_vs_kindness", q.about());
        assertEquals("+", q.answer("a1").stance());
        assertEquals("", q.answer("a3").stance(), "no pole, no stance");
        assertEquals(List.of(AnswerTag.KIND), q.answer("a1").tags(), "a warm tone");
        assertEquals(-1, q.answer("a2").stands().get(Personality.Value.HONESTY));
        var again = Question.parse(honestOrKindAgain());
        assertEquals("q.values.honest_or_kind", again.followUpOf());
        assertEquals(java.util.Set.of("thoughtful"), again.archetypes());
        var withSets = new java.util.HashMap<>(honestOrKind()); withSets.put("sets", "talked_about_honesty");
        assertEquals("talked_about_honesty", Question.parse(withSets).answer("a3").sets(), "a question-level flag for every answer");
    }
    @Test void valuesAndToneLandOnTheirPersonalityAndOppositePolesContradict() {
        var w = TogetherTest.friends(CLASSMATE_C, 60); // thoughtful: values knowledge and honesty
        Questions.load(w, List.of(Question.parse(honestOrKind()), Question.parse(honestOrKindAgain())));
        var q = Questions.question(w, "q.values.honest_or_kind");
        assertTrue(Questions.preview(w, CLASSMATE_C, q, "a1").trust() > Questions.preview(w, CLASSMATE_C, q, "a2").trust(),
                "someone who lives by honesty trusts the honest answer");
        Questions.ask(w, CLASSMATE_C, q.id());
        var first = Questions.answer(w, CLASSMATE_C, q.id(), "a1");
        assertFalse(first.contradiction());
        assertTrue(w.bond(CLASSMATE_C).has("answer:q.values.honest_or_kind=a1"));
        w.advance(Questions.gap(w.effectiveLevel(CLASSMATE_C)));
        var next = Questions.next(w, CLASSMATE_C, x -> true);
        assertEquals("q.values.honest_or_kind_again", next.orElseThrow().id(), "the deeper version follows");
        var out = Questions.answer(w, CLASSMATE_C, next.get().id(), "b2");
        assertTrue(out.contradiction(), "the opposite pole on the same axis");
        if (out.noticed()) assertEquals("callback.contradict", out.say());
        assertTrue(Questions.next(w, CLASSMATE_C, x -> false).isEmpty(), "the glue's veto");
    }
}
