package dev.shinobi.combat;

import java.util.ArrayList;
import java.util.LinkedHashMap;
import java.util.List;
import java.util.Map;
import java.util.Optional;

/**
 * The techniques one caster knows and the signs each takes for them now. Mastery shortens a sequence to a prefix,
 * but a prefix is only used when no other known technique could be meant by it: the book lengthens it sign by sign
 * until it is unique, so a mastered Great Fireball never fires when you meant a technique that starts the same way.
 */
public final class SignBook {
    public record Entry(String id, String rank, List<HandSign> full, Mastery.Tier tier) {}

    private final Map<String, Entry> entries = new LinkedHashMap<>();

    public void learn(String id, String rank, List<HandSign> signs) { entries.put(id, new Entry(id, rank, List.copyOf(signs), Mastery.Tier.NOVICE)); }
    public void setTier(String id, Mastery.Tier t) { var e = entries.get(id); entries.put(id, new Entry(id, e.rank(), e.full(), t)); }
    public boolean knows(String id) { return entries.containsKey(id); }

    /** The signs this caster weaves for a technique at its current mastery (empty: quick-slot or signless). */
    public List<HandSign> sequence(String id) {
        var e = entries.get(id);
        if (e.full().isEmpty()) return List.of();
        int n = Mastery.signsNeeded(e.tier(), e.rank(), e.full().size());
        if (n == 0) return List.of();
        for (; n < e.full().size(); n++) {
            var prefix = e.full().subList(0, n);
            if (unique(id, prefix)) return List.copyOf(prefix);
        }
        return e.full();
    }
    private boolean unique(String id, List<HandSign> prefix) {
        for (var o : entries.values()) {
            if (o.id().equals(id)) continue;
            if (o.full().equals(prefix)) return false;
            if (!o.full().isEmpty() && o.tier().ordinal() >= Mastery.Tier.MASTERED.ordinal() && sequenceNoRecurse(o).equals(prefix)) return false;
        }
        return true;
    }
    private List<HandSign> sequenceNoRecurse(Entry e) {
        int n = Mastery.signsNeeded(e.tier(), e.rank(), e.full().size());
        return n == 0 ? List.of() : e.full().subList(0, n);
    }

    /** The technique a finished weave casts, if any: an exact full sequence first, then a mastered short form. */
    public Optional<String> match(List<HandSign> woven) {
        if (woven.isEmpty()) return Optional.empty();
        for (var e : entries.values()) if (e.full().equals(woven)) return Optional.of(e.id());
        for (var e : entries.values()) if (sequence(e.id()).equals(woven)) return Optional.of(e.id());
        return Optional.empty();
    }
    /** The HUD's prefix hint: every known technique whose sequence starts with what has been woven so far. */
    public List<String> candidates(List<HandSign> prefix) {
        var out = new ArrayList<String>();
        for (var e : entries.values()) {
            var seq = sequence(e.id());
            var full = e.full();
            if (startsWith(seq, prefix) || startsWith(full, prefix)) out.add(e.id());
        }
        return out;
    }
    private static boolean startsWith(List<HandSign> seq, List<HandSign> prefix) {
        return !prefix.isEmpty() && seq.size() >= prefix.size() && seq.subList(0, prefix.size()).equals(prefix);
    }
}
