package dev.shinobi.progression;

import dev.shinobi.progression.mission.Json;
import dev.shinobi.progression.mission.Template;
import org.junit.jupiter.api.Test;

import java.util.List;
import java.util.Map;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertSame;
import static org.junit.jupiter.api.Assertions.assertThrows;

class JournalTest {
    static final Template TWO = Template.of(Json.object("""
            {"id": "q", "start": "a", "steps": {"a": {"objective": {"type": "go"}, "next": "b"},
                                                 "b": {"objective": {"type": "go"}, "next": null}}}"""));

    @Test
    void walksTheStepsThenIsDoneAndCannotBeTakenAgain() {
        var j = Journal.EMPTY.accept(TWO);
        assertEquals(Map.of("q", "a"), j.active());
        j = j.advance(TWO);
        assertEquals(Map.of("q", "b"), j.active());
        j = j.advance(TWO);
        assertEquals(new Journal(Map.of(), List.of("q")), j);
        assertSame(j, j.accept(TWO));
        assertSame(j, j.advance(TWO));
    }

    @Test
    void brokenQuestsAreRefused() {
        assertEquals("q", Quests.check(Json.object("{\"id\": \"q\", \"start\": \"a\", \"steps\": {\"a\": {\"objective\": {\"type\": \"go\", \"place\": \"anchor:x\"}}}}")).id());
        for (String bad : List.of(
                "{\"id\": 5, \"start\": \"a\", \"steps\": {\"a\": {}}}",
                "{\"id\": \"q\", \"start\": \"b\", \"steps\": {\"a\": {}}}",
                "{\"id\": \"q\", \"start\": \"a\", \"steps\": {\"a\": {\"next\": 5}}}",
                "{\"id\": \"q\", \"start\": \"a\", \"steps\": {\"a\": {\"next\": \"c\"}}}",
                "{\"id\": \"q\", \"start\": \"a\", \"steps\": {\"a\": {\"objective\": {\"type\": \"go\"}}}}"))
            assertThrows(IllegalArgumentException.class, () -> Quests.check(Json.object(bad)), bad);
    }
}
