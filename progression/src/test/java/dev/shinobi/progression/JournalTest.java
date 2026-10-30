package dev.shinobi.progression;

import dev.shinobi.progression.mission.Json;
import dev.shinobi.progression.mission.Template;
import com.google.gson.JsonParser;
import com.mojang.serialization.JsonOps;
import org.junit.jupiter.api.Test;

import java.util.List;
import java.util.Map;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertSame;
import static org.junit.jupiter.api.Assertions.assertThrows;
import static org.junit.jupiter.api.Assertions.assertTrue;

class JournalTest {
    static final Template TWO = Template.of(Json.object("""
            {"id": "q", "start": "a", "steps": {"a": {"objective": {"type": "go"}, "next": "b"},
                                                 "b": {"objective": {"type": "go"}, "next": null}}}"""));

    @Test
    void walksTheStepsThenIsDoneAndCannotBeTakenAgain() {
        var j = Journal.EMPTY.accept(TWO, Map.of("spot", "anchor:x"));
        assertEquals(Map.of("q", "a"), j.active());
        assertEquals(Map.of("spot", "anchor:x"), j.castOf("q"));
        j = j.advance(TWO, c -> false);
        assertEquals(Map.of("q", "b"), j.active());
        j = j.advance(TWO, c -> false);
        assertEquals(new Journal(Map.of(), Map.of(), List.of("q"), List.of()), j);
        assertSame(j, j.accept(TWO, Map.of()));
        assertSame(j, j.advance(TWO, c -> false));
    }

    @Test
    void brokenQuestsAreRefused() {
        assertEquals("q", Quests.check(Json.object("{\"id\": \"q\", \"start\": \"a\", \"steps\": {\"a\": {\"objective\": {\"type\": \"go\", \"place\": \"anchor:x\"}}}}")).id());
        for (String bad : List.of(
                "{\"id\": \"q\", \"start\": \"a\", \"steps\": {\"a\": {\"branch\": [{\"if\": {\"flag\": \"f\"}, \"next\": \"z\"}]}}}",
                "{\"id\": \"q\", \"start\": \"a\", \"steps\": {\"a\": {\"branch\": [{\"if\": {\"weather\": \"rain\"}, \"next\": \"a\"}]}}}",
                "{\"id\": \"q\", \"start\": \"a\", \"steps\": {\"a\": {\"branch\": [{\"if\": {\"quest_state\": [\"x\", \"begun\"]}, \"next\": \"a\"}]}}}",
                "{\"id\": \"q\", \"start\": \"a\", \"steps\": {\"a\": {\"branch\": [{\"if\": {\"quest_state\": [\"x\", null]}, \"next\": \"a\"}]}}}",
                "{\"id\": \"q\", \"start\": \"a\", \"steps\": {\"a\": {\"branch\": [{\"if\": {\"quest_state\": [\"q\", \"done\"]}, \"next\": \"a\"}]}}}",
                "{\"id\": \"q\", \"start\": \"a\", \"steps\": {\"a\": {\"on_done\": [{\"give_ryo\": 0}]}}}",
                "{\"id\": \"q\", \"start\": \"a\", \"steps\": {\"a\": {\"on_done\": [{\"give_ryo\": 2.5}]}}}",
                "{\"id\": \"q\", \"start\": \"a\", \"steps\": {\"a\": {\"on_done\": [{\"give_item\": \"tea\"}]}}}",
                "{\"id\": \"q\", \"start\": \"a\", \"steps\": {\"a\": {\"on_enter\": [{\"set_flag\": [\"f\", \"yes\"]}]}}}",
                "{\"id\": 5, \"start\": \"a\", \"steps\": {\"a\": {}}}",
                "{\"id\": \"q\", \"start\": \"b\", \"steps\": {\"a\": {}}}",
                "{\"id\": \"q\", \"start\": \"a\", \"steps\": {\"a\": {\"next\": 5}}}",
                "{\"id\": \"q\", \"start\": \"a\", \"steps\": {\"a\": {\"next\": \"c\"}}}",
                "{\"id\": \"q\", \"start\": \"a\", \"steps\": {\"a\": {\"objective\": {\"type\": \"go\"}}}}",
                "{\"id\": \"q\", \"start\": \"a\", \"steps\": {\"a\": {\"objective\": {\"type\": \"spar\"}}}}",
                "{\"id\": \"q\", \"start\": \"a\", \"steps\": {\"a\": {\"objective\": {\"type\": \"slep\"}}}}",
                "{\"id\": \"q\", \"start\": \"a\", \"steps\": {\"a\": {\"next\": null}}}",
                "{\"id\": \"q\", \"start\": \"a\", \"steps\": {\"a\": {\"objective\": {\"type\": \"go\", \"place\": \"slot:nobody\"}}}}",
                "{\"id\": \"q\", \"start\": \"a\", \"steps\": {\"a\": {\"objective\": {\"type\": \"talk\", \"who\": \"keeper\"}}}}",
                "{\"id\": \"q\", \"start\": \"a\", \"slots\": {\"s\": {\"pick\": \"anchor\", \"tag\": \"x\"}}, \"steps\": {\"a\": {\"objective\": {\"type\": \"talk\", \"who\": \"slot:s\"}}}}",
                "{\"id\": \"q\", \"start\": \"a\", \"slots\": {\"s\": {\"pick\": \"region\"}}, \"steps\": {\"a\": {}}}",
                "{\"id\": \"q\", \"start\": \"a\", \"slots\": {\"s\": {\"pick\": \"resident\", \"where\": {\"age\": \"old\"}}}, \"steps\": {\"a\": {}}}"))
            assertThrows(IllegalArgumentException.class, () -> Quests.check(Json.object(bad)), bad);
    }

    @Test
    void savesRoundTripAndOldSavesWithoutACastLoad() {
        var j = Journal.EMPTY.accept(TWO, Map.of("spot", "anchor:x"));
        assertEquals(j, Journal.CODEC.parse(JsonOps.INSTANCE, Journal.CODEC.encodeStart(JsonOps.INSTANCE, j).getOrThrow()).getOrThrow());
        var old = Journal.CODEC.parse(JsonOps.INSTANCE, JsonParser.parseString("{\"active\": {\"q\": \"a\"}, \"done\": []}")).getOrThrow();
        assertEquals(Map.of("q", "a"), old.active());
        assertEquals(Map.of(), old.castOf("q"));
    }

    @Test
    void stepsRunTheirActionsAndFollowTheFirstBranchThatHolds() {
        var q = Quests.quest(Json.object("""
                {"id": "b", "start": "a",
                 "steps": {"a": {"objective": {"type": "sleep"}, "on_enter": [{"set_flag": ["entered", true]}], "on_done": [{"set_flag": ["met", true]}, {"give_ryo": 5}],
                                 "branch": [{"if": {"not": {"flag": "met"}}, "next": "never"},
                                            {"if": {"all": [{"flag": "met"}, {"quest_state": ["other", "not_started"]}]}, "next": "side"}],
                                 "next": "never"},
                           "side": {"objective": {"type": "sleep"}, "on_enter": [{"set_flag": ["entered", false]}], "on_done": [{"give_ryo": 15}], "next": null},
                           "never": {"objective": {"type": "sleep"}, "next": null}}}"""));
        var o = Quests.start(Journal.EMPTY, q, Map.of());
        assertEquals(List.of("entered"), o.journal().flags());
        o = Quests.complete(o.journal(), q);
        assertEquals(Map.of("b", "side"), o.journal().active());
        assertEquals(List.of("met"), o.journal().flags());
        assertEquals(5, o.ryo());
        o = Quests.complete(o.journal(), q);
        var j = o.journal();
        assertEquals(15, o.ryo());
        assertEquals(List.of("b"), j.done());
        assertEquals("done", j.state("b"));
        assertEquals("not_started", j.state("x"));
        // A done quest pays nothing more.
        assertEquals(new Quests.Outcome(j, 0), Quests.complete(j, q));
    }

    static final Template ERRAND = Quests.check(Json.object("""
            {"id": "e", "start": "ask",
             "slots": {"keeper": {"pick": "resident", "where": {"job": "tea_house"}}, "yard": {"pick": "anchor", "tag": "training"},
                       "lady": {"pick": "role", "role": "landlady"}},
             "steps": {"ask": {"objective": {"type": "talk", "who": "slot:keeper"}, "next": "go"},
                       "go": {"objective": {"type": "go", "place": "slot:yard"}, "next": "board"},
                       "board": {"objective": {"type": "go", "place": "notice_board"}, "next": null}}}"""));

    @Test
    void castsSlotsOnTheMapOrNamesWhatIsMissing() {
        var roles = Map.of("job:tea_house", "k-uuid", "role:landlady", "l-uuid");
        var anchors = Map.of("anchor:training", 1, "notice_board", 2);
        var cast = Quests.cast(ERRAND, roles, anchors);
        assertEquals(Map.of("keeper", "k-uuid", "yard", "anchor:training", "lady", "l-uuid"), cast);
        assertEquals("k-uuid", Quests.resolve("slot:keeper", cast));
        assertEquals("notice_board", Quests.resolve("notice_board", cast));
        var noKeeper = assertThrows(IllegalArgumentException.class, () -> Quests.cast(ERRAND, Map.of("role:landlady", "l"), anchors));
        assertTrue(noKeeper.getMessage().contains("job:tea_house") && noKeeper.getMessage().contains("keeper"), noKeeper.getMessage());
        var noYard = assertThrows(IllegalArgumentException.class, () -> Quests.cast(ERRAND, roles, Map.of("notice_board", 2)));
        assertTrue(noYard.getMessage().contains("anchor:training") && noYard.getMessage().contains("yard"), noYard.getMessage());
        var noBoard = assertThrows(IllegalArgumentException.class, () -> Quests.cast(ERRAND, roles, Map.of("anchor:training", 1)));
        assertTrue(noBoard.getMessage().contains("notice_board"), noBoard.getMessage());
    }
}
