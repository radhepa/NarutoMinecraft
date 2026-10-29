package dev.shinobi.life.home;

import dev.shinobi.life.bond.Seeds;
import java.util.ArrayList;
import java.util.List;
import java.util.Set;

/**
 * Who comes to your door, decided once a day from the save seed (stream {@code home_visit}) and the bond engine.
 *
 * <ul>
 * <li><b>Drop-ins.</b> Friends at level 3 or more, at most one a day, each no more than once in five days: about
 *     {@code 1.5% + 1% per level above 3}, more for warm and open people and for key holders, in a free evening hour.
 * <li><b>Crashing after a mission.</b> The day the squad comes back from a mission, a teammate at level 3 or more
 *     comes over with a 20% chance each (together if both), at most every four days.
 * <li><b>The sensei checks on you</b> from Genin, at level 2 or more, every week or so (35% a day once a week has
 *     passed); in the Academy years the instructor does, every ten days or so.
 * <li><b>Neighbours knock</b> about once in ten days (a cup of sugar, a parcel taken in, the noise upstairs).
 * <li><b>Key holders</b> who come by while you are out wait inside if you are back within two hours, and when you
 *     have been away all day the warm-hearted ones may leave food in the cupboard (and the tidy ones tidy up).
 * </ul>
 *
 * A visit while you are out becomes a note in the mailbox. A visit while you are home plays out: the visitor reacts to
 * the home (the comfort, the decor, the mess, a gift you kept, a photo they are in) and the bond engine hears how it
 * went through {@link Friends#visited}. Mess draws a comment, never a loss.
 */
public final class Visits {
    public static final int DROP_IN_GAP = 5, CRASH_GAP = 4, SENSEI_GAP = 7, INSTRUCTOR_GAP = 10, WAIT_HOURS = 2, MAX_REACTIONS = 3;
    public static final Set<String> FUSSY = Set.of("meticulous", "stern", "reserved", "proud"),
            EASYGOING = Set.of("playful", "adventurous", "fiery"), FEEDERS = Set.of("warmhearted", "protective", "gentle", "steadfast");

    /** The player's day as the visit scheduler sees it. {@code atHome[h]}: home during hour h. */
    public record Day(long day, int season, int rank, String clan, boolean[] atHome, boolean missionReturn,
            List<String> squad, String sensei, String instructor, List<String> neighbours) {
        public boolean home(int hour) { return hour >= 0 && hour < 24 && atHome[hour]; }
        public boolean awayAllDay() { for (int h = 6; h < 24; h++) if (atHome[h]) return false; return true; }
    }
    /** A knock at the door: who, why, when, whether you were in, and what they said about the place. */
    public record Visit(List<String> who, String kind, long day, int hour, boolean met, List<String> reactions, double quality) {}

    public static List<Visit> daily(long seed, Home home, Friends f, Day d) {
        var out = new ArrayList<Visit>();
        String dayKey = Long.toString(d.day());
        // The squad, back from a mission.
        if (d.missionReturn() && since(home, "crash", d.day()) >= CRASH_GAP) {
            var crew = new ArrayList<String>();
            for (String who : d.squad())
                if (f.level(who) >= 3 && !f.cold(who) && Seeds.roll(seed, "home_visit", "crash", who, dayKey) < .2) crew.add(who);
            if (!crew.isEmpty() && d.home(20)) { out.add(meet(home, f, d, crew, "squad_crash", 20)); home.lastVisit.put("crash", d.day()); }
        }
        // The sensei (from Genin) or the instructor (Academy years) looks in.
        String mentor = d.rank() >= 1 ? d.sensei() : d.instructor();
        int gap = d.rank() >= 1 ? SENSEI_GAP : INSTRUCTOR_GAP;
        if (mentor != null && !mentor.isEmpty() && f.level(mentor) >= 2 && since(home, mentor, d.day()) >= gap
                && Seeds.roll(seed, "home_visit", "mentor", mentor, dayKey) < (d.rank() >= 1 ? .35 : .3)) {
            out.add(knock(home, f, d, List.of(mentor), d.rank() >= 1 ? "sensei_check" : "instructor_check", 18));
        }
        // A friend drops by.
        var taken = new java.util.HashSet<String>();
        for (var v : out) taken.addAll(v.who());
        for (String who : f.known()) {
            if (taken.contains(who) || f.cold(who) || f.level(who) < 3 || since(home, who, d.day()) < DROP_IN_GAP) continue;
            double chance = .015 + .01 * (f.level(who) - 3) + .01 * Math.max(0, f.openness(who)) + .01 * Math.max(0, f.warmth(who))
                    + (home.keyHolder(who) ? .015 : 0);
            if (Seeds.roll(seed, "home_visit", "drop_in", who, dayKey) >= chance) continue;
            var hours = new ArrayList<Integer>();
            for (int h = 17; h <= 21; h++) if (f.free(who, d.day(), h)) hours.add(h);
            if (hours.isEmpty()) continue;
            int hour = hours.get((int) (Seeds.roll(seed, "home_visit", "drop_in_hour", who, dayKey) * hours.size()));
            out.add(knock(home, f, d, List.of(who), "drop_in", hour));
            break;
        }
        // Neighbours.
        if (!d.neighbours().isEmpty() && Seeds.roll(seed, "home_visit", "neighbour", dayKey) < .1) {
            var n = d.neighbours().get((int) (Seeds.roll(seed, "home_visit", "which_neighbour", dayKey) * d.neighbours().size()));
            if (since(home, n, d.day()) >= 3) {
                String[] why = {"borrow", "parcel", "noise", "thanks", "gossip"};
                String reason = why[(int) (Seeds.roll(seed, "home_visit", "neighbour_why", dayKey) * why.length)];
                out.add(knock(home, f, d, List.of(n), "neighbour." + reason, 19));
            }
        }
        // Key holders look after the place while you are away.
        if (d.awayAllDay()) for (String who : home.keys().keySet()) {
            if (f.cold(who) || since(home, "food:" + who, d.day()) < 3) continue;
            if (FEEDERS.contains(f.archetype(who)) || f.warmth(who) > .3) {
                if (Seeds.roll(seed, "home_visit", "left_food", who, dayKey) < .25) {
                    home.pantry.store("home_dish", d.day(), 2);
                    home.mailbox.post(Mailbox.Kind.NOTE, who, d.day(), "home.note.left_food", "home_dish");
                    home.lastVisit.put("food:" + who, d.day());
                    out.add(new Visit(List.of(who), "left_food", d.day(), 15, false, List.of(), 0));
                }
            }
            if (home.tidiness() == Home.Tidiness.MESSY && FUSSY.contains(f.archetype(who)) && Seeds.roll(seed, "home_visit", "tidied", who, dayKey) < .3) {
                home.clean();
                home.mailbox.post(Mailbox.Kind.NOTE, who, d.day(), "home.note.tidied", "");
                out.add(new Visit(List.of(who), "tidied", d.day(), 15, false, List.of(), 0));
            }
        }
        return out;
    }

    private static long since(Home home, String key, long day) { return day - home.lastVisit.getOrDefault(key, Long.MIN_VALUE / 2); }

    /** A single visitor at the door: in, waiting inside (a key holder, if you are back soon), or a note. */
    private static Visit knock(Home home, Friends f, Day d, List<String> who, String kind, int hour) {
        if (d.home(hour)) return meet(home, f, d, who, kind, hour);
        String one = who.getFirst();
        if (home.keyHolder(one)) for (int h = hour + 1; h <= hour + WAIT_HOURS; h++)
            if (d.home(h)) return meet(home, f, d, who, kind + ".waited_inside", h);
        for (String w : who) home.lastVisit.put(w, d.day());
        home.mailbox.post(kind.startsWith("neighbour") ? Mailbox.Kind.NEIGHBOUR : Mailbox.Kind.NOTE, one, d.day(), "home.note." + kind, "");
        return new Visit(who, kind, d.day(), hour, false, List.of(), 0);
    }

    /** The visit plays out with you home: reactions, then the bond engine hears how it went. */
    static Visit meet(Home home, Friends f, Day d, List<String> who, String kind, int hour) {
        var reactions = new ArrayList<String>();
        double total = 0;
        var score = Comfort.of(home, d.day(), d.season(), d.clan());
        for (String w : who) {
            double q = react(home, f, d, w, score, reactions);
            total += q;
            f.visited(w, kind, q);
            home.lastVisit.put(w, d.day());
        }
        home.mess(who.size(), "guests");
        return new Visit(who, kind, d.day(), hour, true, List.copyOf(reactions.subList(0, Math.min(MAX_REACTIONS, reactions.size()))), total / who.size());
    }

    /** One visitor's take on the place: dialogue keys into {@code out} and how much they enjoyed it (0 to 1). */
    static double react(Home home, Friends f, Day d, String who, Comfort.Score score, List<String> out) {
        String arch = f.archetype(who);
        double q = .5 + .04 * score.tier().ordinal();
        for (var k : home.displayed()) if (k.giver().equals(who) && !home.noticed(who, k.id())) {
            home.notice(who, k.id());
            if (f.noticed(who, k.id())) { out.add("home.visit.kept_gift"); q += .15; }
        }
        for (var p : home.wall()) if (p.people().contains(who) && !home.noticed(who, p.id() + "#" + p.version())) {
            home.notice(who, p.id() + "#" + p.version());
            f.noticed(who, p.id() + "#" + p.version());
            out.add("home.visit.photo." + p.id()); q += .1;
        }
        long curios = home.displayed().stream().filter(k -> k.kind() == Keepsake.Kind.CURIO).count();
        if (curios >= 3) out.add("home.visit.curios");
        switch (home.tidiness()) {
            case MESSY -> {
                if (EASYGOING.contains(arch)) out.add("home.visit.mess.dont_mind");
                else if (FUSSY.contains(arch)) { out.add("home.visit.mess.fussy"); q -= .15; }
                else { out.add("home.visit.mess"); q -= .05; }
            }
            case LIVED_IN -> { if (home.ramenCups() >= 3) out.add("home.visit.ramen_cups"); }
            case TIDY -> { if (FUSSY.contains(arch)) { out.add("home.visit.tidy"); q += .05; } }
        }
        String best = null;
        for (var e : score.setPieces().entrySet()) {
            var set = Catalog.set(e.getKey());
            if (e.getValue() < 2) continue;
            if (set.clanSet() ? set.clan().equals(f.clan(who)) : set.lovedBy().contains(arch)) { best = e.getKey(); break; }
        }
        if (best != null) { out.add("home.visit.decor." + (best.startsWith("clan.") ? "clan" : best)); q += .1; }
        if (score.perk(FurnitureSet.FESTIVE)) q += .05;
        if (score.perk(FurnitureSet.MORNING_AIR) && home.flat().balcony()) q += .05;
        if (home.plant.flowering(d.day(), d.season())) out.add("home.visit.plant.flowering");
        if (home.petAtHome()) out.add("home.visit.pet");
        out.add("home.visit.comfort." + score.tier().id());
        return Math.clamp(q, 0, 1);
    }

    /**
     * The player invites friends over for a home hangout ({@link HomeHangout}). The bond engine runs the hangout; the
     * home adds the visitors' reactions to the place, and a little mess.
     */
    public static Visit host(Home home, Friends f, Day d, List<String> who, String activity, int hour) {
        String band = f.host(who, activity, d.day(), hour);
        boolean held = Set.of("great", "good", "fine", "rough").contains(band);
        if (!held) return new Visit(who, "hosted." + activity + "." + band, d.day(), hour, false, List.of(), 0);
        var reactions = new ArrayList<String>();
        var score = Comfort.of(home, d.day(), d.season(), d.clan());
        double total = 0;
        for (String w : who) { total += react(home, f, d, w, score, reactions); home.lastVisit.put(w, d.day()); }
        home.mess(Math.min(3, who.size()) + (activity.equals("cook_together") || activity.equals("home_dinner") ? 1 : 0), "guests");
        return new Visit(who, "hosted." + activity, d.day(), hour, true, List.copyOf(reactions.subList(0, Math.min(MAX_REACTIONS, reactions.size()))), total / who.size());
    }

    /** Gives a spare key (bond level 6): the bond engine records it as the flag {@code home.key}. */
    public static String giveKey(Home home, Friends f, String who, long day) {
        String r = home.giveKey(who, f.level(who), day);
        if (r.equals("ok")) f.keyGiven(who);
        return r;
    }

    private Visits() {}
}
