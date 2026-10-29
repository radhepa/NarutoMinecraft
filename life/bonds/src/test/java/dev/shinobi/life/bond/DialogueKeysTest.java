package dev.shinobi.life.bond;

import static dev.shinobi.life.bond.Leaf.*;
import static org.junit.jupiter.api.Assertions.*;

import java.util.HashSet;
import java.util.List;
import org.junit.jupiter.api.Test;

class DialogueKeysTest {
    @Test void everyKeyTheEngineEmitsIsListed() {
        var keys = new HashSet<>(DialogueKeys.required());
        assertTrue(keys.size() > 900, "the social layer needs a lot of writing: " + keys.size() + " pools");
        var w = TogetherTest.friends(TEAMMATE_B, 60);
        for (String k : BondDialogue.greeting(w, TEAMMATE_B)) if (!k.endsWith(".fiery")) assertTrue(keys.contains(k), k);
        for (String t : Conversation.TOPICS.keySet()) if (!t.equals("about_someone") && !t.equals("shared_memory") && !t.equals("their_news"))
            assertTrue(keys.contains(Conversation.talk(w, TEAMMATE_B, t, null).key().replace(".fiery", "")), t);
        var page = BondBook.page(w, TEAMMATE_B);
        for (var f : page.facts()) assertTrue(keys.contains(f.key()));
        for (String v : page.feelings().values()) assertTrue(keys.contains(v), v);
        assertTrue(keys.contains(page.kindling()));
        for (var m : page.kept()) assertTrue(keys.contains(m.key()), m.key());
        for (var m : page.recent()) assertTrue(keys.contains(m.key()), m.key());
        assertTrue(keys.containsAll(List.of("life.injured.response.comfort", "hook.clan_feud.mediated", "callback.hangout.ramen.highlight.1", "village.mood.festive")));
        assertTrue(DialogueKeys.optional().contains("talk.tease.fiery"));
    }
}
