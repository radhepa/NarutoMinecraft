package dev.shinobi.life.bond;

import java.util.ArrayList;
import java.util.List;
import java.util.Map;
import java.util.Set;

/**
 * What you can talk about, and how deep it can go. Topics open with the bond: small talk at once, their hobby at 2,
 * family at 4, values at 5, their dream at 6, what worries them at 7. Asking about something personal before they
 * are ready is prying. Some people love being teased and some hate it; some light up when asked for advice. Each
 * topic counts once a day per person; the reply is a dialogue key ({@code talk.<topic>.<archetype>}, then
 * {@code talk.<topic>}).
 */
public final class Conversation {
    public record Topic(String id, int level, boolean personal, String fact, Act act, double warmth, Set<String> lovedBy, Set<String> dislikedBy) {}
    public record Reply(String key, String reaction) {}

    public static final Map<String, Topic> TOPICS = topics();
    private static Map<String, Topic> topics() {
        var list = List.of(
                new Topic("small_talk", 0, false, "", null, .5, Set.of(), Set.of()),
                new Topic("food", 1, false, "", null, .7, Set.of("fiery", "warmhearted", "playful"), Set.of()),
                new Topic("training", 1, false, "", null, .5, Set.of("proud", "stern", "fiery", "adventurous"), Set.of("gentle")),
                new Topic("compliment", 1, false, "", null, 1, Set.of("gentle", "warmhearted", "shy", "playful"), Set.of("reserved", "pragmatic")),
                new Topic("village_news", 3, false, "", null, .5, Set.of("curious", "playful"), Set.of("reserved")),
                new Topic("their_hobby", 2, true, "hobby", null, 1, Set.of(), Set.of()),
                new Topic("about_someone", 3, false, "", null, .3, Set.of("curious"), Set.of("stern")),
                new Topic("their_family", 4, true, "family", null, 1, Set.of("warmhearted", "protective"), Set.of()),
                new Topic("your_story", 4, false, "", Act.HEART_TO_HEART, .5, Set.of("warmhearted", "curious", "gentle"), Set.of("reserved")),
                new Topic("tease", 4, false, "", null, 1.5, Set.of("playful", "fiery", "adventurous"), Set.of("proud", "shy", "stern")),
                new Topic("their_values", 5, true, "values", null, 1, Set.of("thoughtful", "steadfast"), Set.of()),
                new Topic("ask_advice", 5, false, "", null, 1, Set.of("thoughtful", "stern", "proud", "protective"), Set.of()),
                new Topic("their_dream", 6, true, "dream", Act.HEART_TO_HEART, 1, Set.of(), Set.of()),
                new Topic("their_worries", 7, true, "worries", Act.HEART_TO_HEART, 1, Set.of(), Set.of()),
                new Topic("shared_memory", 3, false, "", null, 1.5, Set.of(), Set.of()),
                new Topic("their_news", 3, false, "", Act.ASKED_AFTER_THEM, .5, Set.of(), Set.of()));
        var m = new java.util.LinkedHashMap<String, Topic>();
        for (var t : list) m.put(t.id(), t);
        return java.util.Collections.unmodifiableMap(m);
    }

    /** The topics open with someone today. */
    public static List<String> topics(BondWorld w, String who) {
        var b = w.bond(who); int level = w.effectiveLevel(who);
        var out = new ArrayList<String>();
        for (var t : TOPICS.values()) {
            if (t.level() > level) continue;
            if (t.id().equals("shared_memory") && b.highlights.stream().noneMatch(h -> w.day - h.day() >= 7)) continue;
            if (t.id().equals("their_news") && b.followUps.stream().noneMatch(f -> !f.theyAsk() && f.due() <= w.day)) continue;
            out.add(t.id());
        }
        return out;
    }
    /**
     * Talks about a topic ({@code about} names the third person for {@code about_someone}). Returns the line's key and
     * the reaction: "warm" (they liked it), "fine", "awkward", or "pried" (too personal, too soon).
     */
    public static Reply talk(BondWorld w, String who, String topicId, String about) {
        var t = TOPICS.get(topicId);
        if (t == null) throw new IllegalArgumentException("unknown topic " + topicId);
        var b = w.bond(who); var p = w.person(who);
        if (b.topicsDay != w.day) { b.topicsDay = w.day; b.topicsToday.clear(); }
        String arch = p.personality().archetype();
        String key = "talk." + topicId;
        if (!b.topicsToday.add(topicId)) return new Reply(key + ".again", "fine");
        b.contact(w.day);
        int level = w.effectiveLevel(who);
        if (t.personal() && level < t.level()) { w.act(who, Act.PRIED); return new Reply(key + ".too_soon", "pried"); }
        if (level < t.level()) return new Reply("talk.not_yet", "fine");
        if (t.dislikedBy().contains(arch)) {
            if (topicId.equals("tease")) w.act(who, Act.RUDE); else w.act(who, Act.AWKWARD_HANGOUT);
            return new Reply(key + "." + arch, "awkward");
        }
        double warmth = t.warmth() * (t.lovedBy().contains(arch) ? 1.6 : 1);
        b.warm(warmth, b.conflict.warmthLet());
        if (!t.fact().isEmpty()) b.facts.add(t.fact());
        if (t.act() != null && !(t.act() == Act.HEART_TO_HEART && b.remembers(Act.HEART_TO_HEART) && w.day - lastHeart(b) < 14)) w.act(who, t.act());
        switch (topicId) {
            case "shared_memory" -> {
                var h = b.highlights.stream().filter(x -> w.day - x.day() >= 7).reduce((x, y) -> y).orElseThrow();
                key = "callback." + h.key();
            }
            case "their_news" -> {
                var f = b.followUps.stream().filter(x -> !x.theyAsk() && x.due() <= w.day).findFirst().orElseThrow();
                b.followUps.remove(f);
                key = f.topic();
            }
            case "about_someone" -> {
                if (about != null && w.people.containsKey(about)) {
                    double aff = w.village != null ? w.village.affinity(who, about) : w.bonds.containsKey(BondWorld.key(who, about)) ? w.meters(who, about).affection() : 0;
                    key = "talk.opinion." + (aff >= 50 ? "dear" : aff >= 20 ? "likes" : aff >= -10 ? "neutral" : aff >= -40 ? "cool" : "dislikes");
                }
            }
            default -> {}
        }
        if (topicId.equals("ask_advice")) w.act(who, Act.ASKED_ADVICE);
        w.favor(who, .5);
        return new Reply(key, t.lovedBy().contains(arch) ? "warm" : "fine");
    }
    private static long lastHeart(Bond b) {
        return b.memories.stream().filter(m -> m.act() == Act.HEART_TO_HEART).mapToLong(Memory::day).max().orElse(Long.MIN_VALUE / 2);
    }

    private Conversation() {}
}
