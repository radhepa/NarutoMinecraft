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
    private static void both(List<String> keys, String key, String archetype) { keys.add(key + "." + archetype); keys.add(key); }

    private BondDialogue() {}
}
