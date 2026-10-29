package dev.shinobi.life.bond;

import java.util.ArrayList;
import java.util.List;
import java.util.Optional;
import java.util.Set;

/**
 * Gifts the player receives: who gave what, when and why, kept for the home's collection book. Residents give for an
 * occasion the glue names ({@link #OCCASIONS}: a birthday, a festival, thanks, a souvenir from a hangout, a wedding, a
 * farewell, a quest's reward), and kindred spirits (level 9) save the player a small gift now and then on their own,
 * one of their favorite things. When a giver later sees their gift displayed in the player's home, it warms them
 * ({@link Act#SAW_GIFT_DISPLAYED}, once per gift).
 */
public final class Gifts {
    public static final Set<String> OCCASIONS = Set.of("birthday", "festival", "thanks", "souvenir", "wedding", "farewell", "quest", "kindred", "new_year");
    /** A kindred spirit's own small gift: about one in {@link #KINDRED_EVERY} days. */
    public static final int KINDRED_EVERY = 7;

    /** One gift received. {@code seen} once the giver has seen it displayed in the player's home. */
    public record Received(int id, String item, String from, long day, String occasion, boolean seen) {}

    /** A resident gives the player something. Returns the record (its id is what the home's display refers to). */
    public static Received receive(BondWorld w, String from, String item, String occasion) {
        if (!OCCASIONS.contains(occasion)) throw new IllegalArgumentException("unknown occasion " + occasion);
        w.person(from);
        var r = new Received(++w.giftSerial, item, from, w.day(), occasion, false);
        w.received.add(r);
        w.bond(from).contact(w.day());
        w.events.add(new BondEvent(w.day(), from, "gift_received", item + " (" + occasion + ")"));
        return r;
    }
    /** Every gift the player has received, oldest first. */
    public static List<Received> received(BondWorld w) { return List.copyOf(w.received); }
    public static List<Received> from(BondWorld w, String who) { return w.received.stream().filter(r -> r.from().equals(who)).toList(); }
    public static Optional<Received> gift(BondWorld w, int id) { return w.received.stream().filter(r -> r.id() == id).findFirst(); }

    /**
     * The giver visits the player's home and sees their gift on display (the home glue knows what is displayed and
     * who visits). The first time for each gift it warms them; returns whether it did.
     */
    public static boolean seenDisplayed(BondWorld w, int id) {
        var r = gift(w, id).orElse(null);
        if (r == null || r.seen()) return false;
        w.received.set(w.received.indexOf(r), new Received(r.id(), r.item(), r.from(), r.day(), r.occasion(), true));
        w.act(r.from(), Act.SAW_GIFT_DISPLAYED);
        return true;
    }

    /**
     * A visitor saw something of theirs on show at the player's home: a gift they gave (the ledger marks it seen) or a
     * photo with them. Once per keepsake, remembered as the bond flag {@code home.noticed:<keepsake>}.
     */
    public static boolean noticed(BondWorld w, String who, String keepsake, boolean photo) {
        if (!w.bond(who).flags.add("home.noticed:" + keepsake)) return false;
        var gift = photo ? null : w.received.stream().filter(r -> r.from().equals(who) && r.item().equals(keepsake) && !r.seen()).findFirst().orElse(null);
        if (gift != null) seenDisplayed(w, gift.id());
        else w.act(who, photo ? Act.SAW_PHOTO_TOGETHER : Act.SAW_GIFT_DISPLAYED);
        return true;
    }

    /** End of day: kindred spirits (level 9 and up, not quarrelling) may leave a small gift, one of their favorite things. */
    static void daily(BondWorld w) {
        for (var b : List.copyOf(w.bonds.values())) {
            if (!b.to.equals(BondWorld.PLAYER) || !b.met() || w.effectiveLevel(b.from) < Levels.DAILY_GIFT || b.conflict.active() || b.conflict.broken()) continue;
            if (Seeds.roll(w.seed, "kindred_gift", b.from, Long.toString(w.day)) * KINDRED_EVERY >= 1) continue;
            var loves = w.person(b.from).personality().loves();
            if (loves.isEmpty()) continue;
            receive(w, b.from, loves.get((int) (Seeds.roll(w.seed, "kindred_item", b.from, Long.toString(w.day)) * loves.size())), "kindred");
        }
    }

    private Gifts() {}
}
