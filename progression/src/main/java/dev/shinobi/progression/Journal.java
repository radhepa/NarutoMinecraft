package dev.shinobi.progression;

import com.mojang.serialization.Codec;
import com.mojang.serialization.codecs.RecordCodecBuilder;
import dev.shinobi.progression.mission.Template;

import java.util.ArrayList;
import java.util.LinkedHashMap;
import java.util.List;
import java.util.Map;
import java.util.function.Predicate;

/**
 * The player's quest journal: each accepted quest's current step and its cast (slot to resident UUID or anchor),
 * the quests done, and the flags quests have set. Saved with the player.
 * shortcut: flags live in the journal, until Shinobi Core keeps the save's flags for every mod's conditions.
 */
public record Journal(Map<String, String> active, Map<String, Map<String, String>> cast, List<String> done, List<String> flags) {
    public static final Journal EMPTY = new Journal(Map.of(), Map.of(), List.of(), List.of());
    public static final Codec<Journal> CODEC = RecordCodecBuilder.create(i -> i.group(
            Codec.unboundedMap(Codec.STRING, Codec.STRING).optionalFieldOf("active", Map.of()).forGetter(Journal::active),
            Codec.unboundedMap(Codec.STRING, Codec.unboundedMap(Codec.STRING, Codec.STRING)).optionalFieldOf("cast", Map.of()).forGetter(Journal::cast),
            Codec.STRING.listOf().optionalFieldOf("done", List.of()).forGetter(Journal::done),
            Codec.STRING.listOf().optionalFieldOf("flags", List.of()).forGetter(Journal::flags)).apply(i, Journal::new));

    /** Whether the quest is under way or done: a quest is taken once. */
    public boolean knows(String quest) { return active.containsKey(quest) || done.contains(quest); }

    /** {@code done}, {@code active} or {@code not_started}: the quest_state condition's values. */
    public String state(String quest) { return done.contains(quest) ? "done" : active.containsKey(quest) ? "active" : "not_started"; }

    public Journal accept(Template quest, Map<String, String> slots) {
        if (knows(quest.id())) return this;
        var a = new LinkedHashMap<>(active);
        a.put(quest.id(), quest.start());
        var c = new LinkedHashMap<>(cast);
        c.put(quest.id(), Map.copyOf(slots));
        return new Journal(Map.copyOf(a), Map.copyOf(c), done, flags);
    }

    /** The quest's cast, empty for a quest with no slots. */
    public Map<String, String> castOf(String quest) { return cast.getOrDefault(quest, Map.of()); }

    /** The journal with the flag set or cleared. */
    public Journal flag(String name, boolean on) {
        if (flags.contains(name) == on) return this;
        var f = new ArrayList<>(flags);
        if (on) f.add(name); else f.remove(name);
        return new Journal(active, cast, done, List.copyOf(f));
    }

    /**
     * The journal once the quest's current step is done: on to the first branch whose condition {@code holds}, else
     * its next step, or the quest done.
     */
    public Journal advance(Template quest, Predicate<Map<String, Object>> holds) {
        String at = active.get(quest.id());
        if (at == null) return this;
        var step = quest.steps().get(at);
        String next = step.branches().stream().filter(b -> holds.test(b.condition())).map(Template.Branch::next).findFirst().orElse(step.next());
        var a = new LinkedHashMap<>(active);
        var c = new LinkedHashMap<>(cast);
        var d = new ArrayList<>(done);
        if (next == null) { a.remove(quest.id()); c.remove(quest.id()); d.add(quest.id()); }
        else a.put(quest.id(), next);
        return new Journal(Map.copyOf(a), Map.copyOf(c), List.copyOf(d), flags);
    }
}
