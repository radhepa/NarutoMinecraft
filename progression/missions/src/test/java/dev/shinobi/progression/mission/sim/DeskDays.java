package dev.shinobi.progression.mission.sim;

import dev.shinobi.progression.mission.Catalogue;
import dev.shinobi.progression.mission.Desk;
import dev.shinobi.progression.mission.Economy;
import dev.shinobi.progression.mission.Grade;
import dev.shinobi.progression.mission.Offer;
import dev.shinobi.progression.mission.Player;
import dev.shinobi.progression.mission.Rank;
import dev.shinobi.progression.mission.SampleVillage;
import dev.shinobi.progression.mission.Seeds;
import dev.shinobi.progression.mission.SquadPlan;
import dev.shinobi.progression.mission.Template;
import dev.shinobi.progression.mission.Unlocks;

import java.util.ArrayList;
import java.util.EnumMap;
import java.util.HashMap;
import java.util.HashSet;
import java.util.List;
import java.util.Locale;
import java.util.Map;
import java.util.Set;
import java.util.TreeMap;

/**
 * Plays the Mission Desk day by day for three kinds of player, in Classic and Varied saves, over many seeds, and
 * prints what a player would feel: how many missions, how varied, what they pay against the cost of living, how
 * much XP they give, and how the grades, requests by name, chains and contests turn up.
 *
 * <ul>
 * <li><b>Beta 2</b> (Genin life, 24 in-game days): the board opens with Ch 9, C-ranks after Ch 11, far regions after
 *     Ch 13; chapter days leave no time for the board.</li>
 * <li><b>The long run</b> (Genin and then Chunin, 200 days, later templates allowed from Chunin): does the board
 *     stay fresh when the player keeps coming back?</li>
 * </ul>
 * Run with {@code ./gradlew :progression:missions:simulate} ({@code -Pseed=N}).
 */
public final class DeskDays {
    /** A kind of player: how often they visit the desk, how much they take, and how well they do. */
    public record Profile(String name, double visit, boolean takeMax, double skill, boolean prefersHigher) {}

    public static final List<Profile> PROFILES = List.of(
            new Profile("casual", 0.45, false, 0.45, false),
            new Profile("steady", 0.75, false, 0.65, true),
            new Profile("keen", 0.95, true, 0.85, true));

    /** Beta 2's story, as the day each chapter is played (relative to the start of Genin life). */
    public static final Map<Integer, String> BETA2 = new TreeMap<>(Map.of(
            0, "story.ch8", 1, "main.ch9.small_jobs", 3, "story.ch10", 6, "main.ch11.paper_trail",
            9, "story.ch12", 12, "main.ch13.far_village", 18, "main.ch14.second_escort"));
    public static final int BETA2_DAYS = 24, START = 20;

    public static final class Run {
        public final Map<Rank, Integer> taken = new EnumMap<>(Rank.class);
        public final Map<String, Integer> perTemplate = new HashMap<>();
        public final Map<String, Integer> lastDay = new HashMap<>();
        public int minRepeatGap = Integer.MAX_VALUE, repeats, twists, requests, chainOffers, contests, contestsWon;
        public final Set<String> clients = new HashSet<>(), categories = new HashSet<>();
        public final Map<String, Integer> grades = new TreeMap<>();
        public double ryo, living, xp, minutes;
        public final Map<Rank, Double> ryoByRank = new EnumMap<>(Rank.class);
        public int otherSquads, boardDays;
        public final Set<String> boardTemplates = new HashSet<>();
    }

    public static Run play(Catalogue cat, long seed, Desk.Mode mode, Profile prof, int days, boolean longRun) {
        var village = new SampleVillage(seed, cat);
        var desk = new Desk(cat, seed, mode, village, longRun);
        var plan = new SquadPlan(cat.squad);
        var mates = List.of(new SquadPlan.Mate("resident:0", "kurama", List.of("openness", "warmth"), false),
                new SquadPlan.Mate("resident:1", "", List.of("boldness"), true));
        var p = new Player();
        p.rank = "genin";
        p.level = 5;
        p.cohesion = 45;
        var run = new Run();
        var rng = Seeds.stream(seed, "sim", prof.name() + "|" + mode + "|" + longRun);
        for (int d = 0; d < days; d++) {
            int day = START + d;
            String chapter = BETA2.get(d);
            if (chapter != null) {
                p.done.add(chapter);
                p.flags.add(chapter.startsWith("story.") ? chapter + ".done" : chapter);
                if (chapter.startsWith("story.ch10")) p.flags.add("story.ch10.done");
            }
            if (longRun && d == 60) { p.rank = "chunin"; p.level = Math.max(p.level, 18); }
            if (longRun && d == 140) { p.rank = "jonin"; p.level = Math.max(p.level, 30); }
            // The Leaf Festival is Summer 14; its setup missions go up in the three days before it.
            int festival = 28 + 13;
            p.events.clear();
            p.eventIn.clear();
            int inYear = Math.floorMod(day, 112);
            if (inYear == festival) p.events.add("event.leaf_festival");
            if (inYear < festival) p.eventIn.put("event.leaf_festival", festival - inYear);
            run.living += cat.economy.livingPerDay(rng.unit());
            var board = desk.open(day, p);
            if (!board.isEmpty()) run.boardDays++;
            board.forEach(o -> run.boardTemplates.add(o.template()));
            if (chapter != null && d > 1) continue;
            if (!rng.chance(prof.visit())) continue;
            int wanted = prof.takeMax() ? 2 : 1;
            for (int k = 0; k < wanted; k++) {
                var choices = new ArrayList<>(desk.offers());
                if (choices.isEmpty()) break;
                choices.sort((a, b) -> {
                    int byReq = Boolean.compare(b.requested(), a.requested());
                    if (byReq != 0) return byReq;
                    int byRank = prof.prefersHigher() ? b.rank().compareTo(a.rank()) : a.rank().compareTo(b.rank());
                    return byRank != 0 ? byRank : Integer.compare(b.pay(), a.pay());
                });
                Offer pick = null;
                for (Offer o : choices) if (desk.refusal(o, p, day) == null) { pick = o; break; }
                if (pick == null) break;
                desk.take(pick, day);
                Template t = cat.get(pick.template());
                record(run, pick, t, day, desk);
                var perf = perform(t, pick, prof, rng);
                boolean squadRun = t.squadAllowed() && !(t.soloAllowed() && rng.chance(0.3));
                var assign = plan.suggest(t.category(), mates);
                boolean good = squadRun && rng.chance(prof.skill()) && plan.goodCall(t.category(), assign, mates);
                Economy.Result r = desk.turnIn(pick, perf, squadRun ? p.cohesion : -1, good, day);
                if (pick.contest()) {
                    run.contests++;
                    if (r.success() && rng.chance(prof.skill())) run.contestsWon++;
                }
                run.ryo += r.ryo();
                run.ryoByRank.merge(t.rank(), (double) r.ryo(), Double::sum);
                p.gainXp(r.xp(), cat.economy);
                run.xp += r.xp();
                run.minutes += t.minutes();
                run.grades.merge(r.grade() == null ? r.end().name().toLowerCase(Locale.ROOT) : r.end() == Economy.Result.End.PARTIAL ? "partial" : r.grade().name(), 1, Integer::sum);
                if (squadRun) p.cohesion = Math.max(0, Math.min(100, p.cohesion + (r.success() ? 1.5 : -3)));
                if (t.rank() != Rank.D) break;
            }
        }
        run.otherSquads = desk.takenByOthers().size();
        return run;
    }

    static void record(Run run, Offer o, Template t, int day, Desk desk) {
        run.taken.merge(o.rank(), 1, Integer::sum);
        int n = run.perTemplate.merge(o.template(), 1, Integer::sum);
        Integer last = run.lastDay.put(o.template(), day);
        if (n > 1) { run.repeats++; run.minRepeatGap = Math.min(run.minRepeatGap, day - last); }
        if (o.twist() != null) run.twists++;
        if (o.requested()) run.requests++;
        if (o.chain() != null) run.chainOffers++;
        if (o.client() != null) run.clients.add(o.client());
        run.categories.add(t.category());
    }

    /** How a mission goes for a player of this skill: bonuses met, knockouts, the odd failure or partial job. */
    static Economy.Performance perform(Template t, Offer o, Profile prof, Seeds.Rng rng) {
        double s = prof.skill() - (o.harder() ? 0.1 : 0);
        double failP = switch (t.rank()) { case D -> 0.02; case C -> 0.07; default -> 0.1; } * (1.6 - s);
        if (rng.chance(failP)) return Economy.Performance.failure();
        boolean partial = rng.chance(0.06 * (1.2 - s));
        int met = 0;
        for (int k = 0; k < t.bonuses().size(); k++) if (rng.chance(s)) met++;
        int ko = t.rank() == Rank.D ? 0 : rng.chance(0.3 * (1 - s)) ? 1 : 0;
        boolean hurt = rng.chance(0.08 * (1 - s));
        boolean late = rng.chance(0.1 * (1 - s));
        return new Economy.Performance(false, false, partial, met, ko, hurt, false, late);
    }

    public static void main(String[] args) {
        long seed = args.length > 0 ? Long.parseLong(args[0]) : 20261029L;
        var cat = Catalogue.load();
        int seeds = 24;
        System.out.printf("Mission Desk simulation, base seed %d, %d seeds per row%n", seed, seeds);
        System.out.printf("Catalogue: %d templates (%s)%n", cat.all().size(), counts(cat));
        System.out.println();
        System.out.println("Beta 2: Genin life, " + BETA2_DAYS + " in-game days (board from Ch 9, C-ranks from Ch 11)");
        table(cat, seed, seeds, BETA2_DAYS, false);
        System.out.println();
        System.out.println("The long run: 200 days (Chunin from day 60, Jonin from day 140, later templates allowed)");
        table(cat, seed, seeds, 200, true);
        System.out.println();
        boardsDiffer(cat, seed);
    }

    static String counts(Catalogue cat) {
        var sb = new StringBuilder();
        for (Rank r : Rank.values()) {
            long beta = cat.of(r).stream().filter(t -> !t.later()).count();
            sb.append(r).append(' ').append(cat.of(r).size()).append(beta > 0 ? " (" + beta + " beta)" : "").append(", ");
        }
        return sb.substring(0, sb.length() - 2);
    }

    static void table(Catalogue cat, long seed, int seeds, int days, boolean longRun) {
        System.out.println("| Mode | Player | D | C | B+ | Distinct | Repeats | Min gap | Twists | Clients | Grades S/A/B/C/part/fail | Req | Chain | Contest won | Ryo/day | Living/day | Saved | Ryo/D | Ryo/C | Board XP | Min/mission | Others took |");
        System.out.println("|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|");
        for (Desk.Mode mode : Desk.Mode.values()) {
            for (Profile prof : PROFILES) {
                double d = 0, c = 0, b = 0, distinct = 0, repeats = 0, twists = 0, clients = 0, req = 0, chain = 0, cont = 0, won = 0;
                double ryo = 0, living = 0, levels = 0, minutes = 0, missions = 0, others = 0, ryoD = 0, ryoC = 0;
                int minGap = Integer.MAX_VALUE;
                var grades = new TreeMap<String, Integer>();
                for (int k = 0; k < seeds; k++) {
                    Run r = play(cat, seed + k * 7919L, mode, prof, days, longRun);
                    int dn = r.taken.getOrDefault(Rank.D, 0), cn = r.taken.getOrDefault(Rank.C, 0);
                    int bn = r.taken.values().stream().mapToInt(Integer::intValue).sum() - dn - cn;
                    d += dn; c += cn; b += bn;
                    distinct += r.perTemplate.size(); repeats += r.repeats; twists += r.twists; clients += r.clients.size();
                    req += r.requests; chain += r.chainOffers; cont += r.contests; won += r.contestsWon;
                    ryo += r.ryo; living += r.living; levels += r.xp; minutes += r.minutes; missions += dn + cn + bn;
                    others += r.otherSquads;
                    ryoD += r.ryoByRank.getOrDefault(Rank.D, 0.0); ryoC += r.ryoByRank.getOrDefault(Rank.C, 0.0);
                    minGap = Math.min(minGap, r.minRepeatGap);
                    r.grades.forEach((g, n) -> grades.merge(g, n, Integer::sum));
                }
                double n = seeds;
                String gr = String.format(Locale.ROOT, "%d/%d/%d/%d/%d/%d", pct(grades, "S"), pct(grades, "A"), pct(grades, "B"),
                        pct(grades, "C"), pct(grades, "partial"), pct(grades, "failed"));
                System.out.printf(Locale.ROOT, "| %s | %s | %.1f | %.1f | %.1f | %.1f | %.1f | %s | %.0f%% | %.1f | %s%% | %.1f | %.1f | %.1f/%.1f | %.0f | %.0f | %.0f | %.0f | %.0f | %s | %.1f | %.1f |%n",
                        mode.name().toLowerCase(Locale.ROOT), prof.name(), d / n, c / n, b / n, distinct / n, repeats / n,
                        minGap == Integer.MAX_VALUE ? "—" : minGap + " d", 100 * twists / Math.max(1, missions), clients / n, gr,
                        req / n, chain / n, won / n, cont / n, ryo / n / days, living / n / days, (ryo - living) / n,
                        d == 0 ? 0 : ryoD / d, c == 0 ? 0 : ryoC / c, xpCell(cat, levels / n, longRun), minutes / Math.max(1, missions), others / n);
            }
        }
    }

    /** Board XP: in Beta 2 as a share of the XP from level 5 to 15 (Genin's span); in the long run in thousands. */
    static String xpCell(Catalogue cat, double xp, boolean longRun) {
        if (longRun) return String.format(Locale.ROOT, "%.0fk", xp / 1000);
        double span = 0;
        for (int l = 5; l < 15; l++) span += cat.economy.xpToNext(l);
        return String.format(Locale.ROOT, "%.0f (%.0f%%)", xp, 100 * xp / span);
    }

    static int pct(Map<String, Integer> grades, String g) {
        int total = grades.values().stream().mapToInt(Integer::intValue).sum();
        return total == 0 ? 0 : (int) Math.round(100.0 * grades.getOrDefault(g, 0) / total);
    }

    /** The same seed in Classic and Varied gives different boards; the same seed and mode the same board. */
    static void boardsDiffer(Catalogue cat, long seed) {
        var p = new Player();
        p.done.add("main.ch9.small_jobs");
        String classic = board(cat, seed, Desk.Mode.CLASSIC, p), varied = board(cat, seed, Desk.Mode.VARIED, p);
        System.out.println("First Genin board, Classic: " + classic);
        System.out.println("First Genin board, Varied:  " + varied);
        System.out.println("Same seed, same board twice: " + classic.equals(board(cat, seed, Desk.Mode.CLASSIC, p)));
    }

    static String board(Catalogue cat, long seed, Desk.Mode mode, Player p) {
        var desk = new Desk(cat, seed, mode, new SampleVillage(seed, cat), false);
        var sb = new StringBuilder();
        for (Offer o : desk.open(START + 1, p))
            sb.append(o.template().replace("mission.", "")).append(o.twist() == null ? "" : "+" + o.twist()).append(' ').append(o.pay()).append("r; ");
        return sb.toString();
    }

    private DeskDays() {}
}
