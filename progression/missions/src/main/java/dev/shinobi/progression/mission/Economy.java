package dev.shinobi.progression.mission;

import java.util.ArrayList;
import java.util.EnumMap;
import java.util.List;
import java.util.Map;

import static dev.shinobi.progression.mission.Json.*;

/**
 * Pay, XP and grades, read from {@code economy.json} (MISSIONS.md section 3).
 *
 * <ul>
 * <li><b>Pay</b> is the player's share in ryo: a point in the rank's band set by the template's weight, jittered per
 *     offer, plus {@code twist_harder} for a harder twist and {@code requested} when a client asked for you by name;
 *     then scaled by the grade on turn-in.</li>
 * <li><b>XP</b> is a share of what one level takes at the rank's reference level ({@link #xpToNext(int)}), from the
 *     rank's band the same way: a D-rank is a fifth of a level at level 7 and less the higher the player is.</li>
 * <li><b>Grades</b> come from a score: {@code base} for finishing, up to {@code bonuses} for bonus objectives, minus
 *     knockouts, a hurt client, an alarm or lateness, plus a good role assignment and the squad's cohesion band.</li>
 * </ul>
 */
public final class Economy {
    public record Band(int ryoLo, int ryoHi, double xpLo, double xpHi, int refLevel, int minLo, int minHi) {}
    public record GradeRow(Grade grade, double min, double pay, double xp, double rapport, int standing) {}

    final Map<Rank, Band> bands = new EnumMap<>(Rank.class);
    final List<GradeRow> grades = new ArrayList<>();
    final double jitter, twistHarder, requested;
    final int roundTo;
    final Map<String, Object> score, partial, fail, abandoned, handedBack;
    final double xpBase, xpPerLevel;
    final double[] food, tools;

    public Economy(Map<String, Object> j) {
        map(j.get("ranks")).forEach((k, v) -> {
            var b = map(v);
            var ryo = list(b.get("ryo")); var xp = list(b.get("xp")); var min = list(b.get("minutes"));
            bands.put(Rank.of(k), new Band((int) num(ryo.get(0), 0), (int) num(ryo.get(1), 0), num(xp.get(0), 0),
                    num(xp.get(1), 0), (int) num(b.get("ref_level"), 5), (int) num(min.get(0), 0), (int) num(min.get(1), 0)));
        });
        for (Object o : list(j.get("grades"))) {
            var g = map(o);
            grades.add(new GradeRow(Grade.of(str(g.get("grade"), "C")), num(g.get("min"), 0), num(g.get("pay"), 1),
                    num(g.get("xp"), 1), num(g.get("rapport"), 0), (int) num(g.get("standing"), 0)));
        }
        jitter = num(j.get("jitter"), 0.1);
        twistHarder = num(j.get("twist_harder"), 0.1);
        requested = num(j.get("requested"), 1.15);
        roundTo = (int) num(j.get("round_to"), 5);
        score = map(j.get("score"));
        partial = map(j.get("partial"));
        fail = map(j.get("fail"));
        abandoned = map(j.get("abandoned"));
        handedBack = map(j.get("handed_back"));
        var curve = map(j.get("xp_curve"));
        xpBase = num(curve.get("base"), 200);
        xpPerLevel = num(curve.get("per_level"), 40);
        var living = map(j.get("living"));
        food = list(living.get("food_per_day")).stream().mapToDouble(x -> num(x, 0)).toArray();
        tools = list(living.get("tools_per_week")).stream().mapToDouble(x -> num(x, 0)).toArray();
    }

    public Band band(Rank r) { return bands.get(r); }

    /** The offer's pay before the grade: the band point at the template's weight, jittered by {@code roll} in [0, 1). */
    public int pay(Template t, double roll, boolean harder, boolean requestedByName) {
        Band b = bands.get(t.rank());
        double w = clamp(t.payWeight() + (roll * 2 - 1) * jitter, 0, 1);
        double ryo = b.ryoLo() + (b.ryoHi() - b.ryoLo()) * w;
        if (harder) ryo *= 1 + twistHarder;
        if (requestedByName) ryo *= requested;
        return (int) (Math.round(ryo / roundTo) * roundTo);
    }

    /** The offer's XP: a share of a level at the rank's reference level, the same way. */
    public int xp(Template t, double roll, boolean harder) {
        Band b = bands.get(t.rank());
        double w = clamp(t.payWeight() + (roll * 2 - 1) * jitter, 0, 1);
        double share = b.xpLo() + (b.xpHi() - b.xpLo()) * w;
        if (harder) share *= 1 + twistHarder;
        return (int) Math.round(share * xpToNext(b.refLevel()));
    }

    /** XP from one level to the next. Provisional: Progression's {@code ranks.json} owns the real curve. */
    public double xpToNext(int level) { return xpBase + xpPerLevel * level; }

    /** The grade for a score in 0..100 (and a little over). */
    public Grade grade(double score) {
        for (GradeRow g : grades) if (score >= g.min()) return g.grade();
        return Grade.C;
    }

    public GradeRow row(Grade g) { return grades.stream().filter(r -> r.grade() == g).findFirst().orElseThrow(); }

    /**
     * The score of a finished mission. {@code bonusesMet} of the template's bonuses were met; {@code cohesion} is the
     * squad's cohesion (or -1 for a solo mission, which has no cohesion term).
     */
    public double score(Template t, Performance p, double cohesion, boolean goodAssignment) {
        double base = num(score.get("base"), 60), bonusShare = num(score.get("bonuses"), 40);
        int available = Math.max(1, t.bonuses().size());
        double s = base + bonusShare * Math.min(available, p.bonusesMet()) / available;
        s += num(score.get("knockout"), -8) * p.knockouts();
        if (p.clientHurt()) s += num(score.get("client_hurt"), -15);
        if (p.alarm()) s += num(score.get("alarm"), -10);
        if (p.late()) s += num(score.get("late"), -10);
        if (goodAssignment) s += num(score.get("good_assignment"), 4);
        if (cohesion >= 0) {
            for (Object row : list(score.get("cohesion"))) {
                var r = list(row);
                if (cohesion >= num(r.get(0), 0)) { s += num(r.get(1), 0); break; }
            }
        }
        return s;
    }

    /** What a mission's end pays and costs, by how it ended. */
    public Result settle(Template t, Offer o, Performance p, double cohesion, boolean goodAssignment) {
        if (p.abandoned()) return new Result(Result.End.ABANDONED, null, 0, 0, num(abandoned.get("rapport"), -4),
                (int) num(abandoned.get("standing"), -4), 0);
        if (p.failed()) return new Result(Result.End.FAILED, null, (int) (o.pay() * num(fail.get("pay"), 0)),
                o.xp() * num(fail.get("xp"), 0.1), num(fail.get("rapport"), -2), (int) num(fail.get("standing"), -2), 0);
        double s = score(t, p, cohesion, goodAssignment);
        Grade g = grade(s);
        if (p.partial()) {
            Grade cap = Grade.of(str(partial.get("grade_cap"), "C"));
            if (g.atLeast(cap)) g = cap;
            return new Result(Result.End.PARTIAL, g, (int) Math.round(o.pay() * num(partial.get("pay"), 0.5)),
                    o.xp() * num(partial.get("xp"), 0.6), num(partial.get("rapport"), 0), 0, s);
        }
        GradeRow r = row(g);
        int pay = (int) (Math.round(o.pay() * r.pay() / roundTo) * roundTo);
        return new Result(Result.End.DONE, g, pay, o.xp() * r.xp(), r.rapport(), r.standing(), s);
    }

    /** One day's living costs in the simulation: food, and a week's tools spread over its days. */
    public double livingPerDay(double roll) {
        return food[0] + (food[1] - food[0]) * roll + (tools[0] + (tools[1] - tools[0]) * roll) / 7;
    }

    public double handedBackRapport() { return num(handedBack.get("rapport"), -0.5); }

    static double clamp(double v, double lo, double hi) { return Math.max(lo, Math.min(hi, v)); }

    /** How a mission went, as the engine measures it (MISSIONS.md section 2, "Grades"). */
    public record Performance(boolean failed, boolean abandoned, boolean partial, int bonusesMet, int knockouts,
                              boolean clientHurt, boolean alarm, boolean late) {
        public static Performance clean(int bonusesMet) { return new Performance(false, false, false, bonusesMet, 0, false, false, false); }
        public static Performance failure() { return new Performance(true, false, false, 0, 0, false, false, false); }
    }

    /** What turn-in gives: the end, the grade (none for a failure), ryo, XP, rapport and standing changes. */
    public record Result(End end, Grade grade, int ryo, double xp, double rapport, int standing, double score) {
        public enum End { DONE, PARTIAL, FAILED, ABANDONED }
        public boolean success() { return end == End.DONE || end == End.PARTIAL; }
    }
}
