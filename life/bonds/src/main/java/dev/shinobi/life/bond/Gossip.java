package dev.shinobi.life.bond;

import java.util.ArrayList;
import java.util.List;

/**
 * How word of a deed gets around the Leaf, after VF's {@code deed/Rumors}. Pure and deterministic: every roll is
 * seeded by the save, the deed, the two people and the day, so a village tells the same story on every replay.
 *
 * <p>Once a day, everyone who knows a fresh deed may tell each person they share a circle with (in a circle of more
 * than {@link #BIG_CIRCLE}, a seeded sample of about {@link #TIES} of them, as VF's ties). The chance is
 * {@link #BASE}, times how close the circle is ({@link #closeness}: household 4, squad or class 3, workplace 2.5,
 * clan 2, district 1.5) and times the deed's size (small 0.5, notable 1), at most 0.9. Small deeds travel only
 * through close circles ({@link #SMALL_REACH}: households, squads, classes, workplaces). Big deeds are village news:
 * the next day everyone has heard. So news reaches a teammate through the squad, a clan through its members and a
 * district through its streets, and someone may hear of your quarrel before you tell them. In a settled
 * {@link Village}, news travels along real ties, slower between clans on bad terms; a tense or cheerful village
 * talks more; every retelling bends the story ({@link #slant}); and news nobody passes on for
 * {@link #DIES_DOWN} days has died down.
 */
public final class Gossip {
    public static final double BASE = .12, MAX = .9, SMALL_REACH = 2.5;
    /** In a circle bigger than this, each member talks with about {@link #TIES} of the others, like VF's ties. */
    public static final int BIG_CIRCLE = 12, TIES = 8, DIES_DOWN = 3;

    /** Whether two members of a circle talk: everyone in a small circle; in a big one, a steady seeded sample of pairs. */
    public static boolean talks(long seed, String circle, String a, String b, int members) {
        if (members <= BIG_CIRCLE) return true;
        String pair = a.compareTo(b) < 0 ? a + "|" + b : b + "|" + a;
        return Seeds.roll(seed, "ties", circle, pair) < (double) TIES / (members - 1);
    }

    /** How close a shared circle is, from its prefix. */
    public static double closeness(String circle) {
        int colon = circle.indexOf(':');
        return switch (colon < 0 ? circle : circle.substring(0, colon)) {
            case "household", "family" -> 4;
            case "squad", "class" -> 3;
            case "work" -> 2.5;
            case "clan" -> 2;
            case "district" -> 1.5;
            default -> 1;
        };
    }
    public static double chance(double closeness, Act.Size size) {
        double s = switch (size) { case SMALL -> .5; case NOTABLE -> 1; case BIG -> 2; };
        return Math.min(MAX, BASE * closeness * s);
    }

    /**
     * How a retelling bends the news: it keeps most of the teller's own slant, leans the way the teller feels about
     * the player (a friend tells it kindly, someone cold tells it worse), and picks up a little noise each hop.
     */
    static double slant(BondWorld w, Deed d, Deed.Know heard, String teller, String listener, long today) {
        var b = w.bonds.get(BondWorld.key(teller, BondWorld.PLAYER));
        double lean = b != null && b.met() ? (Levels.feeling(w.meters(teller)) - 20) / 200 : 0;
        double noise = (Seeds.roll(w.seed, "distort", Integer.toString(d.serial), teller, listener, Long.toString(today)) - .5) * .3;
        return Math.clamp(heard.slant() * .8 + lean + noise, -.6, .6);
    }
    /** A slanted retelling: every effect moved by its own size times the slant, for the player or against them. */
    public static Meters slanted(Meters m, double slant) {
        return new Meters(m.affection() + Math.abs(m.affection()) * slant, m.trust() + Math.abs(m.trust()) * slant,
                m.respect() + Math.abs(m.respect()) * slant, m.rivalry(), m.romance());
    }

    /** One day of talk about one deed. Returns who heard, in order. */
    static List<String> spread(BondWorld w, Deed d, long today) {
        var heard = new ArrayList<String>();
        if (!d.fresh(today) || today <= d.day || d.quiet >= DIES_DOWN) return heard;
        if (d.act.size == Act.Size.BIG) {
            for (var p : w.people.values()) if (!d.knows(p.id())) { d.knowers.put(p.id(), new Deed.Know(Reaction.Source.HEARD, today, "news")); heard.add(p.id()); }
            return heard;
        }
        for (String teller : List.copyOf(d.knowers.keySet())) {
            var known = d.knowers.get(teller);
            if (known.day() >= today || !w.people.containsKey(teller)) continue;
            for (var contact : w.contacts(teller).entrySet()) {
                String listener = contact.getKey();
                if (d.knows(listener) || d.act.size == Act.Size.SMALL && contact.getValue() < SMALL_REACH) continue;
                double p = chance(contact.getValue(), d.act.size);
                if (w.village != null) {
                    var m = w.village.mood("village");
                    p = Math.min(MAX, p * (1 + .3 * (d.good() ? Math.max(0, m.cheer()) : 0) + .3 * m.tension()));
                }
                if (Seeds.roll(w.seed, "gossip", Integer.toString(d.serial), teller, listener, Long.toString(today)) < p) {
                    d.knowers.put(listener, new Deed.Know(Reaction.Source.HEARD, today, teller, slant(w, d, known, teller, listener, today)));
                    heard.add(listener);
                }
            }
        }
        d.quiet = heard.isEmpty() ? d.quiet + 1 : 0;
        return heard;
    }

    private Gossip() {}
}
