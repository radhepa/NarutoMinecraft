package dev.shinobi.life.bond;

import java.util.ArrayList;
import java.util.List;
import java.util.TreeSet;

/**
 * Every dialogue-bank key the bond engine can ask for, so the dialogue compiler can check the bank covers them all
 * ({@code dialogue.py --check} against this list) and writers can see what is still unwritten. Keys that take an
 * archetype ({@code .<archetype>}) are listed in both forms: the general pool is required, the archetype's own is
 * optional and wins when it exists.
 */
public final class DialogueKeys {
    /** Required pools: a line must exist for each. */
    public static List<String> required() {
        var keys = new TreeSet<String>();
        for (int level = 0; level <= Levels.MAX; level++) { keys.add("bond.greet.level." + level); keys.add("bond.level." + level); keys.add("bond.perk." + level); if (level > 0) keys.add("bond.levelup." + level); }
        for (var s : Conflict.State.values()) if (s != Conflict.State.NONE) { keys.add("bond.greet." + s.id()); keys.add("bond.conflict." + s.id()); }
        for (var s : Courtship.Stage.values()) if (s != Courtship.Stage.NONE) keys.add("bond.romance." + s.id());
        for (var t : Kindling.Tier.values()) keys.add("bond.kindling." + t.id());
        for (String f : Kindling.FORMS) keys.add("bond.bonfire." + f);
        keys.add("bond.kindling.dimmed"); keys.add("bond.kindling.nature_trial");
        keys.add("bond.jealous"); keys.add("bond.birthday.missed");
        for (var a : Act.values()) {
            if (!a.remembered()) continue;
            keys.add("bond.memory." + a.id());
            if (a.spreads) { keys.add("bond.memory." + a.id() + ".seen"); keys.add("bond.memory." + a.id() + ".heard"); keys.add("bond.seen." + a.id()); keys.add("bond.heard." + a.id()); }
        }
        for (String f : BondBook.FACTS.keySet()) keys.add("bond.fact." + f);
        for (String m : List.of("affection.dislikes", "affection.wary", "affection.neutral", "affection.fond", "affection.warm", "affection.devoted",
                "trust.distrusts", "trust.unsure", "trust.trusts", "trust.relies", "trust.with_their_life", "respect.unimpressed", "respect.notices",
                "respect.respects", "respect.admires", "respect.looks_up", "rivalry.none", "rivalry.friendly", "rivalry.rival", "rivalry.fierce")) keys.add("bond.feel." + m);
        for (String g : List.of("experience", "moment", "time", "max", "points", "held")) keys.add("bond.goal." + g);
        for (var a : Activity.CATALOG.values()) {
            for (String part : List.of("ask", "yes", "no.busy", "no.not_today", "no.not_their_thing", "no.not_close_enough", "invite", "arrive", "rough", "fine",
                    "good", "great", "stood_up", "ritual", "ritual_missed")) keys.add("hangout." + a.id() + "." + part);
            for (int n = 1; n <= a.highlights(); n++) { keys.add("hangout." + a.id() + ".highlight." + n); keys.add("callback.hangout." + a.id() + ".highlight." + n); }
            keys.add("followup.ritual_missed." + a.id());
        }
        for (var t : Conversation.TOPICS.keySet()) { keys.add("talk." + t); keys.add("talk." + t + ".again"); keys.add("talk." + t + ".too_soon"); }
        for (String o : List.of("dear", "likes", "neutral", "cool", "dislikes")) keys.add("talk.opinion." + o);
        keys.add("talk.not_yet");
        for (var k : LifeEvents.Kind.values()) {
            keys.add("life." + k.id()); keys.add("life." + k.id() + ".update");
            for (String r : List.of("congratulate", "comfort", "help", "shrug")) keys.add("life." + k.id() + ".response." + r);
        }
        for (String topic : List.of("exam", "mission", "festival", "training", "date")) keys.add("followup." + topic);
        for (var label : Mood.Label.values()) keys.add("village.mood." + label.id());
        for (String r : REACTIONS) keys.add("reaction." + r);
        keys.add("callback.contradict");
        for (var e : SocietyHook.OUTCOMES.entrySet()) {
            keys.add("hook." + e.getKey() + ".offer");
            for (String o : e.getValue()) keys.add("hook." + e.getKey() + "." + o);
        }
        return List.copyOf(keys);
    }
    /** The pools a question bank needs: the question, each answer, the reaction, the callback and the contradiction line. */
    public static List<String> forQuestions(List<Question> bank) {
        var keys = new TreeSet<String>();
        for (var q : bank) {
            keys.add("question." + q.id());
            for (var a : q.answers()) { keys.add("answer." + q.id() + "." + a.id()); keys.add("callback.answer." + q.id() + "." + a.id()); }
            if (!q.about().isEmpty()) keys.add("answer.contradiction." + q.about());
        }
        for (String r : REACTIONS) keys.add("reaction." + r);
        keys.add("callback.contradict");
        return List.copyOf(keys);
    }
    public static final List<String> REACTIONS = List.of("touched", "pleased", "amused", "impressed", "fine", "stung_but_respects", "hurt", "noticed_contradiction");

    /** Optional per-archetype variants: {@code <key>.<archetype>} for the pools a personality colors most. */
    public static List<String> optional() {
        var out = new ArrayList<String>();
        for (String key : required()) {
            if (!(key.startsWith("bond.greet.") || key.startsWith("talk.") || key.startsWith("life.") || key.startsWith("hangout.") && !key.contains(".highlight.")
                    || key.equals("bond.jealous") || key.equals("bond.birthday.missed"))) continue;
            for (String a : Personality.archetypes()) out.add(key + "." + a);
        }
        return out;
    }
    private DialogueKeys() {}
}
