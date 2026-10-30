package dev.shinobi.progression;

import com.mojang.serialization.Codec;
import com.mojang.serialization.codecs.RecordCodecBuilder;
import dev.shinobi.progression.mission.Template;

import java.util.ArrayList;
import java.util.LinkedHashMap;
import java.util.List;
import java.util.Map;

/**
 * The player's quest journal: each accepted quest's current step and its cast (slot to resident UUID or anchor),
 * and the quests done. Saved with the player.
 */
public record Journal(Map<String, String> active, Map<String, Map<String, String>> cast, List<String> done) {
    public static final Journal EMPTY = new Journal(Map.of(), Map.of(), List.of());
    public static final Codec<Journal> CODEC = RecordCodecBuilder.create(i -> i.group(
            Codec.unboundedMap(Codec.STRING, Codec.STRING).optionalFieldOf("active", Map.of()).forGetter(Journal::active),
            Codec.unboundedMap(Codec.STRING, Codec.unboundedMap(Codec.STRING, Codec.STRING)).optionalFieldOf("cast", Map.of()).forGetter(Journal::cast),
            Codec.STRING.listOf().optionalFieldOf("done", List.of()).forGetter(Journal::done)).apply(i, Journal::new));

    /** Whether the quest is under way or done: a quest is taken once. */
    public boolean knows(String quest) { return active.containsKey(quest) || done.contains(quest); }

    public Journal accept(Template quest, Map<String, String> slots) {
        if (knows(quest.id())) return this;
        var a = new LinkedHashMap<>(active);
        a.put(quest.id(), quest.start());
        var c = new LinkedHashMap<>(cast);
        c.put(quest.id(), Map.copyOf(slots));
        return new Journal(Map.copyOf(a), Map.copyOf(c), done);
    }

    /** The quest's cast, empty for a quest with no slots. */
    public Map<String, String> castOf(String quest) { return cast.getOrDefault(quest, Map.of()); }

    /**
     * The journal once the quest's current step is done: on to its next step, or the quest done.
     * shortcut: follows {@code next} only, not {@code branch}, until P04-3's conditions.
     */
    public Journal advance(Template quest) {
        String at = active.get(quest.id());
        if (at == null) return this;
        String next = quest.steps().get(at).next();
        var a = new LinkedHashMap<>(active);
        var c = new LinkedHashMap<>(cast);
        var d = new ArrayList<>(done);
        if (next == null) { a.remove(quest.id()); c.remove(quest.id()); d.add(quest.id()); }
        else a.put(quest.id(), next);
        return new Journal(Map.copyOf(a), Map.copyOf(c), List.copyOf(d));
    }
}
