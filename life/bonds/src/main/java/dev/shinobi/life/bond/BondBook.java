package dev.shinobi.life.bond;

import java.util.ArrayList;
import java.util.Comparator;
import java.util.LinkedHashMap;
import java.util.List;
import java.util.Map;

/**
 * The in-game bond book, as data: what you know about each person, how they feel, and what you have lived through
 * together. The screen (Shinobi Life's client {@code BondBookScreen}, after VF's Ledger) only draws a {@link Page};
 * every string here is a dialogue-bank key, never a name (the screen resolves {@code {name:<id>}}).
 *
 * <p>What you know grows with the bond, and quests can reveal a fact early ({@code reveal_fact}):
 * level 0 who they are (clan, rank); 2 favorite things; 3 their hobby (VF personality); 4 family and their favorite
 * way to spend time together; 5 values; 6 dream; 7 pet peeves; 8 what worries them.
 */
public final class BondBook {
    public static final Map<String, Integer> FACTS = facts();
    private static Map<String, Integer> facts() {
        var m = new LinkedHashMap<String, Integer>();
        m.put("who", 0); m.put("loves", 2); m.put("hobby", 3); m.put("favorite_hangout", 4); m.put("family", 4); m.put("values", 5); m.put("dream", 6);
        m.put("peeves", 7); m.put("worries", 8);
        return m;
    }
    public static final int RECENT = 6;

    public record Fact(String key, boolean known, String value) {}
    public record MemoryLine(String key, long day, String about, boolean kept) {}
    public record Page(String who, int level, int effectiveLevel, String levelName, String perk, String goal, List<Fact> facts,
            Map<String, String> feelings, String conflict, String romance, String kindling, List<MemoryLine> kept,
            List<MemoryLine> recent, Map<String, Integer> experiences) {}

    public static Page page(BondWorld w, String who) {
        var b = w.bond(who); var p = w.person(who); var m = w.meters(who);
        int level = b.level(), acting = w.effectiveLevel(who);
        var facts = new ArrayList<Fact>();
        for (var f : FACTS.entrySet()) {
            boolean known = acting >= f.getValue() || b.facts().contains(f.getKey());
            facts.add(new Fact("bond.fact." + f.getKey(), known, known ? value(w, p, f.getKey()) : ""));
        }
        var feelings = new LinkedHashMap<String, String>();
        feelings.put("affection", "bond.feel.affection." + band(m.affection(), new double[]{-30, 0, 15, 40, 70}, "dislikes", "wary", "neutral", "fond", "warm", "devoted"));
        feelings.put("trust", "bond.feel.trust." + band(m.trust(), new double[]{15, 35, 65, 85}, "distrusts", "unsure", "trusts", "relies", "with_their_life"));
        feelings.put("respect", "bond.feel.respect." + band(m.respect(), new double[]{15, 35, 60, 80}, "unimpressed", "notices", "respects", "admires", "looks_up"));
        feelings.put("rivalry", "bond.feel.rivalry." + band(m.rivalry(), new double[]{15, 40, 70}, "none", "friendly", "rival", "fierce"));
        // A secret crush shows only once they would tell you (level 8) or you are courting.
        var stage = b.romance();
        boolean shown = stage.committed() || stage == Courtship.Stage.CRUSH && acting >= Levels.CONFESS;
        String romance = shown ? "bond.romance." + stage.id() : "";
        String goal = goal(w, who);
        var kept = new ArrayList<MemoryLine>(); var recent = new ArrayList<MemoryLine>();
        for (var mem : b.memories()) if (mem.permanent()) kept.add(line(mem, true));
        b.memories().stream().filter(mem -> !mem.permanent())
                .sorted(Comparator.comparingDouble((Memory mem) -> -mem.weight(w.day())).thenComparing(mem -> -mem.day()))
                .limit(RECENT).forEach(mem -> recent.add(line(mem, false)));
        var exp = new LinkedHashMap<String, Integer>();
        b.experienceCounts().forEach((k, v) -> exp.put(k.name().toLowerCase(java.util.Locale.ROOT), v));
        return new Page(who, level, acting, "bond.level." + level, "bond.perk." + level, goal, facts, feelings,
                b.conflict().state() == Conflict.State.NONE ? "" : "bond.conflict." + b.conflict().state().id(), romance,
                "bond.kindling." + Kindling.tier(w, who).id(), kept, recent, exp);
    }
    /** What the next level needs: "bond.goal.points:N" (N closeness to go), or the gate ("bond.goal.moment"...), or max. */
    public static String goal(BondWorld w, String who) {
        var b = w.bond(who);
        if (b.level() >= Levels.MAX) return "bond.goal.max";
        if (b.level() >= w.levelCap(b)) return "bond.goal.held";
        String gate = w.gate(who);
        if (!gate.isEmpty()) return "bond.goal." + gate;
        int need = (int) Math.ceil(Levels.threshold(b.level() + 1) - w.closeness(who));
        return "bond.goal.points:" + Math.max(1, need);
    }
    private static MemoryLine line(Memory m, boolean kept) {
        String how = m.source() == Reaction.Source.SELF ? "" : "." + m.source().name().toLowerCase(java.util.Locale.ROOT);
        return new MemoryLine("bond.memory." + m.act().id() + how, m.day(), m.about(), kept);
    }
    private static String value(BondWorld w, Person p, String fact) {
        var pp = p.personality();
        return switch (fact) {
            case "who" -> (p.clan().isEmpty() ? "clanless" : p.clan()) + "," + (p.shinobi() ? Person.RANKS.get(p.rank()) : "civilian");
            case "loves" -> String.join(",", pp.loves());
            case "hobby" -> pp.archetype();
            case "family" -> String.join(",", p.family().keySet());
            case "values" -> String.join(",", pp.values().stream().map(v -> v.name().toLowerCase(java.util.Locale.ROOT)).sorted().toList());
            case "dream" -> pp.dream();
            case "favorite_hangout" -> Activity.favorite(w.seed(), p.id());
            case "worries" -> pp.dream().isEmpty() ? "" : "worry." + pp.dream();
            case "peeves" -> String.join(",", pp.peeves().stream().map(v -> v.name().toLowerCase(java.util.Locale.ROOT)).sorted().toList());
            default -> "";
        };
    }
    private static String band(double v, double[] cuts, String... names) {
        int i = 0;
        while (i < cuts.length && v >= cuts[i]) i++;
        return names[i];
    }

    private BondBook() {}
}
