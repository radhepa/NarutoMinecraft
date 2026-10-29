package dev.shinobi.life.roster.sim;

import static dev.shinobi.life.roster.Roster.*;

import dev.shinobi.life.roster.BondInput;
import dev.shinobi.life.roster.Contribution;
import dev.shinobi.life.roster.Curve;
import dev.shinobi.life.roster.Day;
import dev.shinobi.life.roster.GrowthEvent;
import dev.shinobi.life.roster.Roster;
import dev.shinobi.life.roster.Seeds;
import java.util.ArrayList;
import java.util.LinkedHashMap;
import java.util.List;
import java.util.Locale;
import java.util.Map;

/**
 * A seeded whole save for the roster: the 60-hour main path (ROADMAP.md's chapters, scaled so each stretch has its
 * hours: Academy 4, Genin 8, Chunin Exams 3, Chunin 13, Jonin 17, the road to Hokage 15), played by three kinds of
 * player, with the Classic class of twelve. It prints the player's level and every classmate's per chapter, how
 * often the band had to step in, and each teammate's contribution share.
 *
 * <p>Bond levels are inputs here, taken from the bond engine's own simulation (BONDS.md §15): the roster does not
 * depend on life:bonds. Run with {@code ./gradlew :life:roster:simulate} ({@code -Pseed=N}, or {@code -Pseeds=a,b,c}
 * for the summary over several seeds).
 */
public final class Season {
    /** Kinds of player: extra side-quest XP, deaths a day, mission success, how often they skip a training day, kindlings a day. */
    public enum Profile {
        DEVOTED(.3, .01, .97, 0, .5), TYPICAL(.1, .02, .92, .1, .3), RECKLESS(0, .07, .7, .4, .1);

        final double side, deaths, success, skips, kindles;
        Profile(double side, double deaths, double success, double skips, double kindles) {
            this.side = side; this.deaths = deaths; this.success = success; this.skips = skips; this.kindles = kindles;
        }
        public String id() { return name().toLowerCase(Locale.ROOT); }
    }
    enum Phase { ACADEMY, GENIN, EXAMS, LATER }
    /** A chapter: hours of main path, in-game days, the beat seen at its end, and the level the player needs before it starts. */
    record Chapter(String id, String title, double hours, int days, Phase phase, String beat, int gate) {}

    static final List<Chapter> CHAPTERS = List.of(
            new Chapter("Ch 0", "Prologue", .45, 1, Phase.ACADEMY, "", 0),
            new Chapter("Ch 1", "First morning", .45, 1, Phase.ACADEMY, "", 0),
            new Chapter("Ch 2", "First lessons", .5, 2, Phase.ACADEMY, "ch2.spar", 0),
            new Chapter("Ch 3", "Chakra", .6, 2, Phase.ACADEMY, "ch3.chakra", 0),
            new Chapter("Ch 4", "Night", .55, 1, Phase.ACADEMY, "", 0),
            new Chapter("Ch 5", "Errands at the Academy", .35, 1, Phase.ACADEMY, "", 0),
            new Chapter("Ch 6", "Exam eve", .5, 2, Phase.ACADEMY, "ch6.exam_eve", 0),
            new Chapter("Ch 7", "Graduation", .6, 2, Phase.ACADEMY, "ch7.graduation", 0),
            new Chapter("Ch 8", "Team assignment", .85, 3, Phase.GENIN, "ch8.bells", 5),
            new Chapter("Ch 9", "The Mission Desk", 1.2, 4, Phase.GENIN, "", 0),
            new Chapter("Ch 10", "Tree walking", .95, 3, Phase.GENIN, "ch10.tree_walking", 0),
            new Chapter("Ch 11", "First C-rank", 1.25, 4, Phase.GENIN, "ch11.campfire", 0),
            new Chapter("Ch 12", "Water walking and natures", 1.05, 3, Phase.GENIN, "ch12.natures", 0),
            new Chapter("Ch 13", "A far village", 1.25, 3, Phase.GENIN, "", 0),
            new Chapter("Ch 14", "Second C-rank", 1.45, 4, Phase.GENIN, "ch14.recommended", 0),
            new Chapter("Ch 15", "Written test", .33, 1, Phase.EXAMS, "", 15),
            new Chapter("Ch 16", "Forest of Death", 1, 5, Phase.EXAMS, "ch16.night_watch", 0),
            new Chapter("Ch 17", "Preliminaries", .33, 1, Phase.EXAMS, "ch17.preliminaries", 0),
            new Chapter("Ch 18", "Training break", .5, 6, Phase.EXAMS, "ch18.training_break", 0),
            new Chapter("Ch 19", "Chunin Exams finals", .67, 1, Phase.EXAMS, "ch19.finals", 0),
            new Chapter("Ch 20", "Results", .17, 1, Phase.EXAMS, "", 0),
            new Chapter("Chunin 1", "A year later", 3.25, 10, Phase.LATER, "", 0),
            new Chapter("Chunin 2", "Chunin arc", 3.25, 10, Phase.LATER, "arc.chunin", 0),
            new Chapter("Chunin 3", "Chunin arc", 3.25, 10, Phase.LATER, "arc.chunin.natures", 0),
            new Chapter("Chunin 4", "Chunin arc", 3.25, 10, Phase.LATER, "", 0),
            new Chapter("Jonin 1", "Three years later", 4.25, 13, Phase.LATER, "", 30),
            new Chapter("Jonin 2", "Jonin arc", 4.25, 13, Phase.LATER, "arc.jonin", 0),
            new Chapter("Jonin 3", "Jonin arc", 4.25, 13, Phase.LATER, "arc.jonin.natures", 0),
            new Chapter("Jonin 4", "Jonin arc", 4.25, 13, Phase.LATER, "", 0),
            new Chapter("Road 1", "The road to Hokage", 5, 15, Phase.LATER, "", 42),
            new Chapter("Road 2", "The road to Hokage", 5, 15, Phase.LATER, "arc.road", 0),
            new Chapter("Road 3", "The road to Hokage", 5, 15, Phase.LATER, "", 0));

    /** The player's own techniques by beat (the Academy three, a scroll, a nature and a clan or lesser technique, the sensei's lesson, the exam reward, the later arcs). */
    static final Map<String, Integer> PLAYER_TECHNIQUES = Map.ofEntries(Map.entry("ch6.exam_eve", 2), Map.entry("ch7.graduation", 1),
            Map.entry("ch10.tree_walking", 1), Map.entry("ch12.natures", 2), Map.entry("ch14.recommended", 1), Map.entry("ch18.training_break", 1), Map.entry("arc.chunin", 1),
            Map.entry("arc.chunin.natures", 1), Map.entry("Chunin 4", 1), Map.entry("arc.jonin", 1), Map.entry("arc.jonin.natures", 1), Map.entry("arc.road", 1));

    /** The bond engine's typical player, the level each teammate acts on at the end of each beta chapter (BONDS.md §15). */
    static final int[] TYPICAL_A = {1, 1, 1, 1, 1, 1, 2, 2, 3, 4, 4, 4, 4, 4, 6, 6, 7, 7, 7, 8, 8};
    static final int[] TYPICAL_B = {1, 1, 2, 2, 2, 2, 4, 4, 6, 6, 6, 7, 5, 7, 8, 8, 9, 9, 9, 9, 9};

    static int bondLevel(Profile p, String who, int chapter) {
        boolean later = chapter >= TYPICAL_A.length;
        int typical = later ? (who.equals(TEAMMATE_A) ? 9 : 9) : (who.equals(TEAMMATE_A) ? TYPICAL_A : TYPICAL_B)[chapter];
        if (who.equals(CLASSMATE_C)) typical = later ? 6 : Math.min(3, typical);
        if (who.equals(RIVAL)) typical = later ? 6 : Math.min(2, typical);
        return switch (p) {
            case DEVOTED -> Math.min(10, typical + (later ? 1 : 1));
            case TYPICAL -> typical;
            case RECKLESS -> Math.max(1, (int) Math.round(typical * (later ? .45 : .4)));
        };
    }
    static String kindling(Profile p, boolean unlocked) {
        if (!unlocked) return "none";
        return p == Profile.RECKLESS ? "nature" : "full";
    }

    public record Row(String chapter, String title, double hours, long day, double player, Map<String, Double> levels,
                      Map<String, Double> shares, int playerTechniques, Map<String, Integer> techniques, String notes, Map<String, Double> all) {}
    /** Per person: the lowest and highest level against the player's best, the mean, and the days the band stepped in. */
    public record Spread(double min, double max, double mean, int caughtUp, int plateaued, int days) {}
    public record Result(Profile profile, long seed, List<Row> rows, Map<String, Spread> spread, double rivalAhead,
                         double minShare, double maxShare, int grindDays, int deaths, List<GrowthEvent> events, Roster roster) {}

    public static final List<String> SHOWN = List.of(TEAMMATE_A, TEAMMATE_B, CLASSMATE_C, CLASSMATE_D, RIVAL);

    /** Plays one profile through the whole path. */
    public static Result play(long seed, Profile p) {
        var r = Roster.classic(seed);
        var rng = Seeds.stream(seed, "season", p.id());
        var rows = new ArrayList<Row>();
        var events = new ArrayList<GrowthEvent>();
        var team = new ArrayList<>(List.of(TEAMMATE_A, TEAMMATE_B));
        r.group(r.ids());
        double xp = 0; int floor = 1, playerTechs = 0, grind = 0, deaths = 0;
        double minShare = 9, maxShare = 0; long rivalAhead = 0, days = 0;
        var gaps = new LinkedHashMap<String, double[]>();   // min, max, sum
        for (String id : r.ids()) gaps.put(id, new double[]{99, -99, 0});
        boolean kindlingOpen = false;
        for (int ci = 0; ci < CHAPTERS.size(); ci++) {
            var ch = CHAPTERS.get(ci);
            var notes = new ArrayList<String>();
            // A gate: the player grinds on their own until they reach it, while everyone else trains apart.
            while (ch.gate > 0 && Curve.level(xp) < ch.gate) {
                xp += Curve.Stretch.of(Curve.level(xp)).cost() / 2 * rng.range(.8, 1.2);
                r.day(Day.apart(xp)); grind++; track(r, gaps); days++;
            }
            if (ch.id.equals("Ch 8")) { r.group(team); notes.add("squads formed"); }
            if (ch.id.equals("Chunin 1") || ch.id.equals("Jonin 1")) { r.timeSkip(); notes.add("time skip"); }
            if (ch.id.equals("Chunin 2")) { kindlingOpen = true; notes.add("Kindling Bond unlocks"); }
            double perDay = ch.hours * 60 / ch.days;
            for (int d = 0; d < ch.days; d++) {
                boolean together, training, mission;
                double sharedFrac;
                switch (ch.phase) {
                    case ACADEMY -> { together = true; training = d % 2 == 0; mission = false; sharedFrac = .75; }
                    case EXAMS -> {
                        together = !ch.id.equals("Ch 18") || d == 0 || d == ch.days - 1;
                        training = !ch.id.equals("Ch 16"); mission = ch.id.equals("Ch 16"); sharedFrac = .9;
                    }
                    default -> {
                        together = d % 4 != 3 && !rng.chance(p.skips * .5);
                        mission = d % 3 != 2; training = !mission; sharedFrac = .85;
                    }
                }
                double main = perDay * rng.range(.85, 1.15);
                if (mission && !rng.chance(p.success)) { main *= .4; }
                double shared = together ? main * sharedFrac : 0;
                xp += main + main * p.side;
                if (rng.chance(p.deaths)) { xp = Math.max(Curve.xpAt(floor), Curve.xpAt(Curve.level(xp) - 1)); deaths++; }
                var bonds = new LinkedHashMap<String, BondInput>();
                for (String who : List.of(TEAMMATE_A, TEAMMATE_B, CLASSMATE_C, RIVAL)) {
                    boolean sparred = who.equals(RIVAL) ? rng.chance(.15) : training && together && r.groupMembers().contains(who);
                    boolean quarrel = who.equals(TEAMMATE_B) && (p == Profile.TYPICAL && ch.id.equals("Ch 12") || p == Profile.RECKLESS && rng.chance(.3));
                    bonds.put(who, new BondInput(bondLevel(p, who, ci), sparred ? 1 : 0, quarrel, kindling(p, kindlingOpen)));
                }
                r.day(new Day(xp, shared, together, bonds));
                if (kindlingOpen && rng.chance(p.kindles)) r.kindle(team.get(rng.below(team.size())));
                track(r, gaps); days++;
                if (r.level(RIVAL) > r.bestPlayerLevel()) rivalAhead++;
            }
            // The chapter's beat, seen by the class at the Academy and by the squad after it; the whole class sits the exams,
            // and the later arcs bring the rival and the two classmates back into the story.
            if (!ch.beat.isEmpty()) {
                var present = new ArrayList<>(ch.phase == Phase.ACADEMY || ch.phase == Phase.EXAMS ? r.ids() : r.groupMembers());
                if (ch.beat.startsWith("arc.")) present.addAll(List.of(TEAMMATE_B, RIVAL, CLASSMATE_C, CLASSMATE_D));
                r.beat(ch.beat, present);
                playerTechs += PLAYER_TECHNIQUES.getOrDefault(ch.beat, 0);
            }
            playerTechs += PLAYER_TECHNIQUES.getOrDefault(ch.id, 0);
            if (ch.id.equals("Ch 7")) { floor = 5; for (String id : r.ids()) r.promote(id, 5); }
            if (ch.id.equals("Ch 12") && p == Profile.RECKLESS) {
                team.remove(TEAMMATE_B); team.add(CLASSMATE_C); r.group(team); notes.add("teammate_b left; classmate_c steps in");
            }
            if (ch.id.equals("Ch 20") && p != Profile.RECKLESS) floor = 15;
            if (ch.id.equals("Chunin 1") && p == Profile.RECKLESS) floor = 15;
            if (ch.id.equals("Jonin 1")) floor = 30;
            if (ch.id.equals("Road 3")) floor = 50;
            xp = Math.max(xp, Curve.xpAt(floor));
            for (var e : r.drainEvents()) events.add(e);
            var levels = new LinkedHashMap<String, Double>();
            for (String who : SHOWN) levels.put(who, r.level(who));
            var shares = new LinkedHashMap<String, Double>();
            var techs = new LinkedHashMap<String, Integer>();
            for (String who : team) {
                double s = Contribution.share(r, who, playerTechs);
                shares.put(who, s);
                if (ch.phase != Phase.ACADEMY) { minShare = Math.min(minShare, s); maxShare = Math.max(maxShare, s); }
            }
            for (String who : SHOWN) techs.put(who, r.techniques(who).size());
            var all = new LinkedHashMap<String, Double>();
            for (String who : r.ids()) all.put(who, r.level(who));
            rows.add(new Row(ch.id, ch.title, hours(ci), r.today(), Curve.level(xp), levels, shares, playerTechs, techs, String.join("; ", notes), all));
        }
        var spread = new LinkedHashMap<String, Spread>();
        for (var e : gaps.entrySet()) spread.put(e.getKey(), new Spread(e.getValue()[0], e.getValue()[1], e.getValue()[2] / days,
                r.caughtUp(e.getKey()), r.plateaued(e.getKey()), (int) days));
        return new Result(p, seed, rows, spread, (double) rivalAhead / days, minShare, maxShare, grind, deaths, events, r);
    }
    static String label(String who) {
        return switch (who) { case TEAMMATE_A -> "tmA"; case TEAMMATE_B -> "tmB"; case CLASSMATE_C -> "clC"; case CLASSMATE_D -> "clD"; case RIVAL -> "riv"; default -> who.substring(5); };
    }
    static double hours(int upTo) { double h = 0; for (int i = 0; i <= upTo; i++) h += CHAPTERS.get(i).hours; return h; }
    static void track(Roster r, Map<String, double[]> gaps) {
        double player = r.bestPlayerLevel();
        for (var e : gaps.entrySet()) {
            double g = r.level(e.getKey()) - player; var v = e.getValue();
            v[0] = Math.min(v[0], g); v[1] = Math.max(v[1], g); v[2] += g;
        }
    }

    public static String table(Result res) {
        var sb = new StringBuilder();
        sb.append("\n== ").append(res.profile().id()).append(" player, seed ").append(res.seed()).append(" ==\n");
        sb.append(String.format("%-9s %-26s %5s %4s | %5s | %5s %5s %5s %5s %5s | %-17s | %s%n", "chapter", "", "hours", "day", "you",
                "tmA", "tmB", "clC", "clD", "riv", "share (squad)", "notes"));
        for (var row : res.rows()) {
            var l = row.levels();
            var shares = row.shares().entrySet().stream().map(e -> label(e.getKey()) + String.format(" %.2f", e.getValue())).toList();
            sb.append(String.format("%-9s %-26s %5.1f %4d | %5.1f | %5.1f %5.1f %5.1f %5.1f %5.1f | %-17s | %s%n", row.chapter(), row.title(), row.hours(), row.day(),
                    row.player(), l.get(TEAMMATE_A), l.get(TEAMMATE_B), l.get(CLASSMATE_C), l.get(CLASSMATE_D), l.get(RIVAL), String.join(" ", shares), row.notes()));
        }
        sb.append(String.format("deaths %d, grind days before gates %d, rival ahead of you %.0f%% of days, squad share %.2f to %.2f (Genin on)%n",
                res.deaths(), res.grindDays(), 100 * res.rivalAhead(), res.minShare(), res.maxShare()));
        sb.append("against your best level (min / mean / max), and days the band stepped in (lifted / held):\n");
        res.spread().forEach((who, s) -> sb.append(String.format("  %-18s %+5.1f %+5.1f %+5.1f   %3d / %3d of %d%n", who.substring(5), s.min(), s.mean(), s.max(),
                s.caughtUp(), s.plateaued(), s.days())));
        var beta = res.rows().get(20);
        sb.append("techniques at the beta's end: you ").append(beta.playerTechniques()).append(", ").append(beta.techniques()).append('\n');
        return sb.toString();
    }

    /** The same checks over several seeds: the widest gaps, the band's interventions and the shares. */
    public static String summary(long[] seeds) {
        var sb = new StringBuilder(String.format("%nOver %d seeds%n%-9s | %-21s | %-21s | %-15s | %-11s | %-11s | %s%n", seeds.length, "player",
                "teammates vs you", "rival vs you", "band (lift/hold)", "rival ahead", "squad share", "beta end (you / tmA / tmB / rival)"));
        for (var p : Profile.values()) {
            double tmMin = 99, tmMax = -99, rvMin = 99, rvMax = -99, ahead = 0, sMin = 9, sMax = 0; int lift = 0, hold = 0, peerDays = 0;
            var beta = new ArrayList<String>();
            for (long seed : seeds) {
                var res = play(seed, p);
                for (String t : List.of(TEAMMATE_A, TEAMMATE_B)) { var s = res.spread().get(t); tmMin = Math.min(tmMin, s.min()); tmMax = Math.max(tmMax, s.max()); }
                var rv = res.spread().get(RIVAL); rvMin = Math.min(rvMin, rv.min()); rvMax = Math.max(rvMax, rv.max());
                for (var s : res.spread().values()) { lift += s.caughtUp(); hold += s.plateaued(); peerDays += s.days(); }
                ahead += res.rivalAhead() / seeds.length; sMin = Math.min(sMin, res.minShare()); sMax = Math.max(sMax, res.maxShare());
                var b = res.rows().get(20);
                beta.add(String.format("%.0f/%.0f/%.0f/%.0f", Math.floor(b.player()), Math.floor(b.levels().get(TEAMMATE_A)), Math.floor(b.levels().get(TEAMMATE_B)), Math.floor(b.levels().get(RIVAL))));
            }
            sb.append(String.format("%-9s | %+5.1f to %+5.1f        | %+5.1f to %+5.1f        | %4.1f%% / %4.1f%%   | %5.0f%%      | %.2f to %.2f | %s%n", p.id(),
                    tmMin, tmMax, rvMin, rvMax, 100.0 * lift / peerDays, 100.0 * hold / peerDays, 100 * ahead, sMin, sMax, String.join(" ", beta)));
        }
        return sb.toString();
    }

    public static final long[] SEEDS = {20261029L, 7L, 11L, 99L, 2024L};

    /** The chapters that end each stretch of the main path, for tools/roster/roster.json's {@code levels}. */
    static final Map<String, String> STRETCH_ENDS = Map.of("academy", "Ch 7", "genin", "Ch 14", "exams", "Ch 20", "chunin", "Chunin 4", "jonin", "Jonin 4", "road", "Road 3");

    /** Each classmate's whole level at the end of each stretch, typical player, as JSON (the roster file's {@code levels}). */
    public static String stretchLevels(long seed) {
        var res = play(seed, Profile.TYPICAL);
        var sb = new StringBuilder();
        for (String who : res.roster().ids()) {
            sb.append('"').append(who).append("\": {");
            var parts = new ArrayList<String>();
            for (String st : List.of("academy", "genin", "exams", "chunin", "jonin", "road")) {
                var row = res.rows().stream().filter(x -> x.chapter().equals(STRETCH_ENDS.get(st))).findFirst().orElseThrow();
                int lvl = who.equals("player") ? (int) row.player() : (int) Math.floor(levelOf(res, row, who));
                parts.add('"' + st + "\": " + lvl);
            }
            sb.append(String.join(", ", parts)).append("}\n");
        }
        return sb.toString();
    }
    static double levelOf(Result res, Row row, String who) { return row.all().get(who); }

    public static void main(String[] args) {
        long seed = args.length > 0 ? Long.parseLong(args[0]) : 20261029L;
        if (System.getProperty("stretches") != null) { System.out.print(stretchLevels(seed)); return; }
        System.out.println("Squad growth, seed " + seed + " (levels are fractional on the player's curve; share = a teammate's contribution over yours)");
        for (var p : Profile.values()) System.out.print(table(play(seed, p)));
        String list = System.getProperty("seeds");
        long[] seeds = list == null ? SEEDS : java.util.Arrays.stream(list.split(",")).mapToLong(Long::parseLong).toArray();
        System.out.print(summary(seeds));
    }

    private Season() {}
}
