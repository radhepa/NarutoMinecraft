package dev.shinobi.life.roster;

import java.util.ArrayList;
import java.util.Collection;
import java.util.LinkedHashMap;
import java.util.LinkedHashSet;
import java.util.List;
import java.util.Map;
import java.util.Set;

/**
 * Everyone who grows beside the player: the Academy class, then the squad and the rival (docs/RANKS.md, "Squad
 * growth"). Each person has their own XP on the player's curve and their own techniques, and tracks the player
 * inside a band:
 *
 * <ul>
 * <li><b>Shared work:</b> on a day the group is together (lessons with the class, missions and training with the
 *     squad) they earn what the player earned on it ({@link Day#sharedXp}).</li>
 * <li><b>Days apart:</b> they train and take missions on their own, at the player's recent daily pace (a moving
 *     average of the player's daily XP, {@link #PACE_MEMORY}) times their
 *     {@link Peer#drive}. After team assignment the rest of the class are on squads of their own, so every day is a
 *     day apart for them.</li>
 * <li><b>Pace:</b> the gain is scaled by how far they are from where they belong ({@code player + offset}, see {@link Peer#offset}):
 *     {@code 1 - PULL x gap}, between {@link #MIN_PACE} and {@link #MAX_PACE}. Behind, they catch up; ahead, they
 *     slow down. The band ({@link Peer#band} levels either side of where they belong) is the safety net: below it they
 *     jump back in ({@code caught_up}, "I trained the whole week"), above it they wait ({@code plateau}). The band is measured from the player's best level, so dying
 *     does not drag the squad down with you.</li>
 * <li><b>Bonds:</b> training or sparring with the player is worth {@link #BOND_TRAINING} more per bond level (the
 *     same multiplier the player gets, {@link #trainingBonus}); a quarrel takes the bonus away.</li>
 * <li><b>Their niche:</b> in their own field they fight {@link #nicheEdge} levels above their level, so a teammate a
 *     little behind you overall is still better than you at what they do.</li>
 * <li><b>Kindling</b> (after the beta): a kindled ally fights {@link #KINDLE_BOOST} levels higher in their niche
 *     while the flame burns, and each kindling leaves a little XP behind; a blaze bond adds a level to their niche
 *     for good, a flame half of one.</li>
 * <li><b>Techniques</b> come at story beats and in training the player sees ({@link Technique}).</li>
 * </ul>
 *
 * Deterministic: one seed, one save, the same growth.
 */
public final class Roster {
    public static final double PULL = .5, MIN_PACE = .2, MAX_PACE = 2.2, BOND_TRAINING = .02, PACE_MEMORY = .25, DAYS_PER_LEVEL = 3;
    /** In their niche they fight {@code 1 + 0.06 x level} levels higher: about 2 by the Chunin Exams, 4 at level 50. */
    public static final double NICHE_EDGE = 1, NICHE_EDGE_PER_LEVEL = .06, KINDLE_BOOST = 3, KINDLE_EMBER = .25, BLAZE_EDGE = 1, FLAME_EDGE = .5;

    /** One person's growth. */
    static final class Grower {
        final Peer peer; final List<Technique> kit; double xp; int floor = 1; boolean inGroup = true;
        final Set<String> learned = new LinkedHashSet<>();
        int caughtUp, plateaued, kindles; boolean burning, atTop, atBottom; String kindling = "none";
        Grower(Peer peer, List<Technique> kit, double xp) { this.peer = peer; this.kit = List.copyOf(kit); this.xp = xp; }
        double level() { return Curve.level(xp); }
    }

    final long seed;
    final Map<String, Grower> people = new LinkedHashMap<>();
    final Set<String> passed = new LinkedHashSet<>();
    double playerXp, bestXp, pace; long day;
    final List<GrowthEvent> events = new ArrayList<>();

    public Roster(long seed) { this.seed = seed; player(0); }

    /** Where the player starts (0 for a new save): their XP, and a day's pace of a level every {@link #DAYS_PER_LEVEL} days. */
    public Roster player(double xp) {
        playerXp = bestXp = xp;
        pace = Curve.Stretch.of(Curve.level(xp)).cost() / DAYS_PER_LEVEL;
        return this;
    }

    /** Adds someone at a level (1 for a new Academy student), with their kit. */
    public Roster add(Peer p, List<Technique> kit, double level) {
        people.put(p.id(), new Grower(p, kit, Curve.xpAt(level)));
        return this;
    }
    public Roster add(Peer p) { return add(p, Technique.kit(p.niche(), p.clan()), 1); }

    /** Who shares the player's work from now on (the class at the Academy, the squad from team assignment). */
    public void group(Collection<String> ids) {
        for (var g : people.values()) g.inGroup = ids.contains(g.peer.id());
    }
    public List<String> groupMembers() { return people.values().stream().filter(g -> g.inGroup).map(g -> g.peer.id()).toList(); }

    /** One in-game day. */
    public void day(Day d) {
        double gained = Math.max(0, d.playerXp() - playerXp);
        pace += PACE_MEMORY * (gained - pace);
        // The pull reads where the player stood this morning (so someone level with you keeps exactly your pace);
        // the band reads where they stand tonight.
        double morning = Curve.level(bestXp);
        playerXp = d.playerXp(); bestXp = Math.max(bestXp, playerXp);
        double player = Curve.level(bestXp);
        for (var g : people.values()) {
            var bond = d.bond(g.peer.id());
            double before = g.level(), gain;
            boolean shared = g.inGroup && d.together();
            if (shared) {
                gain = d.sharedXp();
                if (bond.trainedTogether() > 0) gain *= trainingBonus(bond.level(), bond.quarrel());
            } else {
                // Rolled from the person and the day, not a running stream, so a reloaded save grows the same.
                gain = pace * g.peer.drive() * Seeds.stream(seed, "roster", g.peer.id() + "|" + day).range(.75, 1.25);
                // Sparring with someone off your squad still counts: you both get better.
                if (bond.trainedTogether() > 0) gain *= trainingBonus(bond.level(), bond.quarrel());
            }
            g.kindling = bond.kindling();
            double gap = before - (morning + g.peer.offset(morning));
            gain *= Math.clamp(1 - PULL * gap, MIN_PACE, MAX_PACE);
            g.xp += gain;
            double target = player + g.peer.offset(player);
            double lo = Math.max(target - g.peer.band(), g.floor), hi = target + g.peer.band();
            // The band: counted every day it has to hold someone, said once when it starts.
            boolean top = g.level() > hi, bottom = !top && g.level() < lo;
            if (top) { g.xp = Math.max(Curve.xpAt(before), Curve.xpAt(hi)); g.plateaued++; if (!g.atTop) emit(g, "plateau", ""); }
            if (bottom) { g.xp = Curve.xpAt(lo); g.caughtUp++; if (!g.atBottom) emit(g, "caught_up", ""); }
            g.atTop = top; g.atBottom = bottom;
            for (int l = (int) before + 1; l <= (int) g.level(); l++) emit(g, "level", Integer.toString(l));
            if (shared || bond.trainedTogether() > 0) learn(g, Technique.TRAINING);
            g.burning = false;
        }
        day++;
    }

    /**
     * A story beat, with the people the player sees there. Whoever is ready learns the techniques tied to it, and
     * shows what else they picked up since the player last saw them at work (someone on another squad learned their
     * nature at their own ceremony; you see it at the exams).
     */
    public void beat(String id, Collection<String> present) {
        passed.add(id);
        for (String who : present) {
            var g = people.get(who);
            if (g != null) learn(g, id);
        }
    }
    /** A technique is learned where the player sees it: at its own beat, or at any later beat or training with them. */
    private void learn(Grower g, String occasion) {
        int lvl = (int) g.level();
        for (var t : g.kit) {
            if (g.learned.contains(t.id()) || t.minLevel() > lvl) continue;
            if (t.beat().equals(occasion) || t.beat().equals(Technique.TRAINING) || passed.contains(t.beat())) { g.learned.add(t.id()); emit(g, "technique", t.id()); }
        }
    }

    /** A rank's level floor (genin 5, chunin 15, jonin 30): they never fall below it, and are lifted to it. */
    public void promote(String who, int floor) {
        var g = people.get(who);
        g.floor = Math.max(g.floor, floor);
        if (g.level() < floor) g.xp = Curve.xpAt(floor);
        emit(g, "promoted", Integer.toString(floor));
    }

    /** The player kindles this ally's flame (after the beta): stronger in their niche today, and a little XP stays with them. */
    public void kindle(String who) {
        var g = people.get(who);
        g.burning = true; g.kindles++;
        double player = Curve.level(bestXp), hi = Curve.xpAt(player + g.peer.offset(player) + g.peer.band());
        g.xp = Math.max(g.xp, Math.min(hi, g.xp + KINDLE_EMBER * pace));
        emit(g, "kindled", Integer.toString(g.kindles));
    }

    /** A time skip: a year (or three) of training apart evens everyone out halfway toward where they belong. */
    public void timeSkip() {
        double player = Curve.level(bestXp);
        for (var g : people.values()) {
            double target = player + g.peer.offset(player), now = g.level();
            g.xp = Curve.xpAt(Math.max(g.floor, now + (target - now) / 2));
        }
    }

    /** The multiplier on training XP with someone at this bond level: +2% a level, none while quarrelling. */
    public static double trainingBonus(int bondLevel, boolean quarrel) {
        return quarrel ? 1 : 1 + BOND_TRAINING * Math.clamp(bondLevel, 0, 10);
    }

    public double level(String who) { return people.get(who).level(); }
    public int wholeLevel(String who) { return (int) level(who); }
    public Tier tier(String who) { return Tier.of(level(who)); }
    /** How strong they are in their niche: their level and the niche edge, more with a full bond, more while kindled. */
    public double nicheLevel(String who) {
        var g = people.get(who);
        return g.level() + nicheEdge(g.level()) + kindlingEdge(g.kindling) + (g.burning ? KINDLE_BOOST : 0);
    }
    /** A Kindling bond's lasting edge in their niche: a blaze a level, a flame half of one (the bond engine's tiers). */
    public static double kindlingEdge(String tier) { return "blaze".equals(tier) ? BLAZE_EDGE : "flame".equals(tier) ? FLAME_EDGE : 0; }
    public static double nicheEdge(double level) { return NICHE_EDGE + NICHE_EDGE_PER_LEVEL * level; }
    public Niche niche(String who) { return people.get(who).peer.niche(); }
    public List<String> techniques(String who) { return List.copyOf(people.get(who).learned); }
    /** Days the band had to lift them (they were further behind than it allows). */
    public int caughtUp(String who) { return people.get(who).caughtUp; }
    /** Days the band had to hold them back. */
    public int plateaued(String who) { return people.get(who).plateaued; }
    public int kindles(String who) { return people.get(who).kindles; }
    public double playerLevel() { return Curve.level(playerXp); }
    public double bestPlayerLevel() { return Curve.level(bestXp); }
    public long today() { return day; }
    public Peer peer(String who) { return people.get(who).peer; }
    public List<String> ids() { return List.copyOf(people.keySet()); }
    /** The squad's strength for the Mission Desk: the mean level of the player and the group. */
    public double squadPower() { return groupLevel(); }
    public double groupLevel() {
        var g = groupMembers();
        return (playerLevel() + g.stream().mapToDouble(this::level).sum()) / (1 + g.size());
    }

    public List<GrowthEvent> drainEvents() { var out = List.copyOf(events); events.clear(); return out; }
    private void emit(Grower g, String kind, String detail) { events.add(new GrowthEvent(day, g.peer.id(), kind, detail)); }

    /**
     * A header (day, the player's XP, best XP and pace, the beats passed), then one line per person: id, xp, floor, in the
     * group, kindles, techniques, and whether the band is holding them at its top and at its bottom.
     */
    public String save() {
        var sb = new StringBuilder("roster 1 ").append(day).append(' ').append(playerXp).append(' ').append(bestXp).append(' ').append(pace)
                .append(' ').append(String.join(",", passed)).append('\n');
        for (var g : people.values())
            sb.append(g.peer.id()).append(' ').append(g.xp).append(' ').append(g.floor).append(' ').append(g.inGroup).append(' ').append(g.kindles)
              .append(' ').append(String.join(",", g.learned)).append(' ').append(g.atTop).append(' ').append(g.atBottom).append('\n');
        return sb.toString();
    }
    /** Restores a {@link #save} into a roster that already has the same people added. */
    public void load(String text) {
        var lines = text.lines().filter(l -> !l.isBlank()).toArray(String[]::new);
        var head = lines[0].split(" ", -1);
        if (!head[0].equals("roster") || !head[1].equals("1")) throw new IllegalArgumentException("not a roster save");
        day = Long.parseLong(head[2]); playerXp = Double.parseDouble(head[3]); bestXp = Double.parseDouble(head[4]); pace = Double.parseDouble(head[5]);
        passed.clear();
        if (!head[6].isEmpty()) passed.addAll(List.of(head[6].split(",")));
        for (int i = 1; i < lines.length; i++) {
            var f = lines[i].split(" ", -1);
            var g = people.get(f[0]);
            if (g == null) continue;
            g.xp = Double.parseDouble(f[1]); g.floor = Integer.parseInt(f[2]); g.inGroup = Boolean.parseBoolean(f[3]); g.kindles = Integer.parseInt(f[4]);
            g.learned.clear();
            if (!f[5].isEmpty()) g.learned.addAll(List.of(f[5].split(",")));
            // Older saves end at the techniques: the band state starts clear.
            g.atTop = f.length > 7 && Boolean.parseBoolean(f[6]); g.atBottom = f.length > 7 && Boolean.parseBoolean(f[7]);
        }
    }

    /**
     * The Classic cast that grows beside the player: the eleven classmates of their year (four squads of three with
     * the player) and the squad a year ahead. Offsets are the story's: the rival, the Hyuga heir and the senior
     * squad's clanless prodigy run strongest; the loud teammate and the Inuzuka start lowest and catch up. Varied saves
     * roll the class with {@link Peer#rolled}.
     */
    public static Roster classic(long seed) {
        var r = new Roster(seed);
        for (var p : CLASS) r.add(p, Technique.kit(p.niche(), p.clan()), SENIORS.contains(p.id()) ? 10 : 1);
        return r;
    }
    public static final String TEAMMATE_A = "role:teammate_a", TEAMMATE_B = "role:teammate_b", CLASSMATE_C = "role:classmate_c",
            CLASSMATE_D = "role:classmate_d", RIVAL = "role:rival";
    public static final List<String> SENIORS = List.of("role:squad5_a", "role:squad5_b", "role:squad5_c");
    public static final List<Peer> CLASS = List.of(
            // Tuned against Combat's duel simulator (docs/COMBAT.md, "Balance"): genjutsu deals less damage than the
            // player's mix, so the painter sits a little ahead; the brawler and their pup hit hard, so they settle behind.
            Peer.teammate(TEAMMATE_A, Niche.GENJUTSU, "kurama", .4, .95),
            Peer.teammate(TEAMMATE_B, Niche.TAIJUTSU, "", -1.2, -.8, 15, 1.12),
            Peer.rival(RIVAL, Niche.NINJUTSU, "uchiha"),
            Peer.classmate(CLASSMATE_C, Niche.TOOLS, "kinoshita", -.5, -.5, 1, 1),
            Peer.classmate(CLASSMATE_D, Niche.KENJUTSU, "gekko", .3, .3, 1, 1.05),
            Peer.classmate("role:squad3_a", Niche.SUPPORT, "nara", 0, 0, 1, .95),
            Peer.classmate("role:squad3_b", Niche.TAIJUTSU, "akimichi", -.3, -.3, 1, 1),
            Peer.classmate("role:squad3_c", Niche.SENSING, "yamanaka", -.2, -.2, 1, 1),
            Peer.classmate("role:squad4_a", Niche.TAIJUTSU, "hyuga", .9, .9, 1, 1.08),
            Peer.classmate("role:squad4_b", Niche.TRACKING, "inuzuka", -1.5, -.4, 20, 1.1),
            Peer.classmate("role:squad4_c", Niche.MEDICAL, "suzuran", -.4, -.4, 1, .97),
            Peer.senior("role:squad5_a", Niche.TAIJUTSU, "sarutobi", 8, 1.2, 30, 1.03),
            Peer.senior("role:squad5_b", Niche.SENSING, "tobari", 7.5, .8, 30, 1),
            Peer.senior("role:squad5_c", Niche.TAIJUTSU, "", 9, 1.8, 30, 1.12));
}
