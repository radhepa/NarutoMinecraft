package dev.shinobi.life.bond;

import java.util.ArrayList;
import java.util.List;
import java.util.Optional;

/**
 * Which dialogue pools a resident speaks from, given the bond: keys into VF's dialogue bank, most specific first,
 * so a line written for a proud rival's cold shoulder wins over the general cold shoulder, which wins over the
 * level's greeting. Each key comes in two forms: {@code <key>.<archetype>} (their VF personality) and {@code <key>}.
 */
public final class BondDialogue {
    /** Days a missed birthday or a fresh piece of news is still brought up. */
    public static final int FRESH_DAYS = 7;

    /** Pools for their greeting: a quarrel, then a missed birthday, jealousy, courtship, then the level. */
    public static List<String> greeting(BondWorld w, String who) {
        var b = w.bond(who); var keys = new ArrayList<String>();
        String archetype = w.person(who).personality().archetype();
        var state = b.conflict().state();
        if (state != Conflict.State.NONE) both(keys, "bond.greet." + state.id(), archetype);
        if (b.memories().stream().anyMatch(m -> m.act() == Act.MISSED_BIRTHDAY && w.day() - m.day() <= FRESH_DAYS)) both(keys, "bond.birthday.missed", archetype);
        if (w.squad() != null && w.squad().jealousy(who) >= Squad.JEALOUS) both(keys, "bond.jealous", archetype);
        if (b.romance().committed()) both(keys, "bond.romance." + b.romance().id(), archetype);
        both(keys, "bond.greet.level." + w.effectiveLevel(who), archetype);
        return keys;
    }
    /**
     * What they say when a {@code level_up} event reaches a new level with the player ({@code bond.levelup.<n>}, apart
     * from the level's name in the book, {@code bond.level.<n>}); empty for other events and for ties between residents.
     */
    public static List<String> levelUp(BondWorld w, BondEvent e) {
        if (!e.kind().equals("level_up") || e.who().contains(">")) return List.of();
        var keys = new ArrayList<String>();
        both(keys, "bond.levelup." + e.detail(), w.person(e.who()).personality().archetype());
        return keys;
    }
    /**
     * Something they heard or saw about you and haven't brought up yet: the newest fresh secondhand memory, as
     * {@code bond.heard.<act>} (or {@code bond.seen.<act>}). Brought up once; the bond remembers it was said.
     */
    public static Optional<String> news(BondWorld w, String who) {
        var b = w.bond(who);
        for (var m : b.memories().reversed()) {
            if (m.source() == Reaction.Source.SELF || m.source() == Reaction.Source.TOLD || w.day() - m.day() > FRESH_DAYS) continue;
            String said = "said:" + m.act().id() + "@" + m.day();
            if (b.has(said)) continue;
            b.flags.add(said);
            return Optional.of("bond." + (m.source() == Reaction.Source.SEEN ? "seen." : "heard.") + m.act().id());
        }
        return Optional.empty();
    }
    /**
     * A highlight from a hangout at least a week ago, brought up now and then ({@code callback.hangout.<activity>.highlight.<n>}):
     * at most once every two weeks per person, the newest first.
     */
    public static Optional<String> callback(BondWorld w, String who) {
        var b = w.bond(who);
        if (b.flags.stream().anyMatch(f -> f.startsWith("callback:") && w.day() - Long.parseLong(f.substring(9)) < 14)) return Optional.empty();
        var h = b.highlights().reversed().stream().filter(x -> w.day() - x.day() >= 7).findFirst();
        if (h.isEmpty()) return Optional.empty();
        b.flags.removeIf(f -> f.startsWith("callback:"));
        b.flags.add("callback:" + w.day());
        return Optional.of("callback." + h.get().key());
    }
    /**
     * Something they meant to ask the player, now due ({@code followup.<topic>}: how the exam went, the ritual they
     * miss); asking shows they care, so it warms the bond a little. Once each.
     */
    public static Optional<String> followUp(BondWorld w, String who) {
        var b = w.bond(who);
        var f = b.followUps.stream().filter(x -> x.theyAsk() && x.due() <= w.day()).findFirst();
        if (f.isEmpty()) return Optional.empty();
        b.followUps.remove(f.get());
        w.addFriendship(who, .5);
        return Optional.of("followup." + f.get().topic());
    }
    /** Their news, when they would tell it: see {@link LifeEvents#tell}. */
    public static Optional<String> lifeNews(BondWorld w, String who) { return LifeEvents.tell(w, who); }

    private static void both(List<String> keys, String key, String archetype) { keys.add(key + "." + archetype); keys.add(key); }

    private BondDialogue() {}
}
