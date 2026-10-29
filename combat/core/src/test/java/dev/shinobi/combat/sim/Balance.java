package dev.shinobi.combat.sim;

import dev.shinobi.combat.CombatData;
import dev.shinobi.combat.Damage;
import dev.shinobi.combat.Difficulty;
import dev.shinobi.combat.Nature;
import dev.shinobi.combat.Scaling;
import dev.shinobi.combat.Scaling.Pillar;
import java.util.ArrayList;
import java.util.List;
import java.util.Locale;
import java.util.Map;

/**
 * The balance tables (docs/COMBAT.md, "Balance"): time-to-kill by level for each build against standard enemies,
 * what each technique rank deals, build against build, and the beta's boss fights. Every number comes from
 * data/combat/ played through {@link Battle}; {@code ./gradlew :combat:core:simulate -Pseed=N -Pruns=N}.
 */
public final class Balance {
    static final String[] FOCI = {"taijutsu", "weapons", "ninjutsu", "balanced"};
    static final int[] LEVELS = {5, 10, 15, 18, 25, 30, 40, 50, 60};
    static final String MOOK = "combat:enemy.rogue_genin", ELITE = "combat:enemy.rogue_chunin";

    /** Win rate, mean seconds to win, mean health left for the player side. */
    record Stats(double win, double seconds, double hpLeft, Map<Pillar, Double> share) {
        String cell() { return String.format(Locale.ROOT, "%.0f%% %.1fs", win * 100, seconds); }
    }

    final CombatData data;
    final long seed;
    final int runs;

    Balance(CombatData data, long seed, int runs) { this.data = data; this.seed = seed; this.runs = runs; }

    public static void main(String[] args) {
        long seed = args.length > 0 ? Long.parseLong(args[0]) : 20261029L;
        int runs = args.length > 1 ? Integer.parseInt(args[1]) : 200;
        var b = new Balance(CombatData.load(), seed, runs);
        System.out.println(b.report());
    }

    String report() {
        var out = new StringBuilder();
        out.append("Seed ").append(seed).append(", ").append(runs).append(" fights a cell, average player skill.\n\n");
        out.append(ttkTable(Difficulty.STORY)).append('\n').append(ttkTable(Difficulty.SHINOBI)).append('\n');
        out.append(rankTable()).append('\n').append(pillarShare()).append('\n');
        out.append(matrix(new int[]{10, 18, 30, 50})).append('\n');
        out.append(bosses(Difficulty.STORY)).append('\n').append(bosses(Difficulty.SHINOBI));
        return out.toString();
    }

    Stats duel(String buildId, String enemy, int level, Difficulty diff, Fighter.Skill skill) {
        double wins = 0, time = 0, hp = 0;
        var share = new java.util.EnumMap<Pillar, Double>(Pillar.class);
        for (int i = 0; i < runs; i++) {
            var battle = new Battle(data, diff, seed * 31 + i * 7919L + buildId.hashCode() * 13L + enemy.hashCode());
            battle.add(Fighter.player(data, data.builds.get(buildId), skill, 0), 0);
            battle.add(Fighter.enemy(data, data.enemies.get(enemy), level, diff, 1, null, false), 8);
            var r = battle.run();
            if (r.winner() == 0) { wins++; time += r.ticks() / 20.0; hp += r.playerHp(); }
            r.playerDamage().forEach((k, v) -> share.merge(k, v, Double::sum));
        }
        return new Stats(wins / runs, wins == 0 ? 0 : time / wins, wins == 0 ? 0 : hp / wins, share);
    }

    String ttkTable(Difficulty diff) {
        var t = new StringBuilder();
        t.append("Time to kill, ").append(diff.id()).append(": win rate and mean seconds against a level-matched rogue genin (mook) and rogue chunin (elite)\n\n");
        t.append("| Level |");
        for (String f : FOCI) t.append(' ').append(f).append(" mook | ").append(f).append(" elite |");
        t.append("\n|---|");
        for (String f : FOCI) t.append("---|---|");
        t.append('\n');
        for (int lv : LEVELS) {
            t.append("| ").append(lv).append(" |");
            for (String f : FOCI) {
                String id = "sim." + f + "." + lv;
                t.append(' ').append(duel(id, MOOK, lv, diff, Fighter.Skill.AVERAGE).cell()).append(" | ")
                        .append(duel(id, ELITE, lv, diff, Fighter.Skill.AVERAGE).cell()).append(" |");
            }
            t.append('\n');
        }
        return t.toString();
    }

    /** What one cast of each rank deals at the level it is learned, per cast, per chakra point and per second of cast and cooldown. */
    String rankTable() {
        var t = new StringBuilder("Technique ranks at the level they open (ninjutsu pillar at the specialist's rank, average over the catalogue's damaging techniques)\n\n");
        t.append("| Rank | Level | Techniques | Damage a cast | Chakra | Damage a chakra | Damage a second (cast + cooldown) | Casts on a full bar |\n|---|---|---|---|---|---|---|---|\n");
        for (String r : new String[]{"d", "c", "b", "a", "s"}) {
            int level = Map.of("d", 8, "c", 10, "b", 18, "a", 30, "s", 42).get(r);
            int rank = Math.min(10, Math.max(1, (int) Math.round(Scaling.pillarCap(level) * 0.55)));
            double dmg = 0, cost = 0, dps = 0;
            int n = 0;
            for (var tech : data.techniques.values()) {
                if (!tech.rank().equals(r) || tech.power() <= 0 || tech.clan() != null) continue;
                var a = Damage.Attack.player(tech.power(), tech.damageType() == null ? "ninjutsu.none" : tech.damageType(), Damage.Delivery.JUTSU, level,
                        Pillar.NINJUTSU, rank, 1);
                double d = a.raw();
                dmg += d;
                cost += tech.chakra();
                int cast = tech.signless() ? tech.castTicks() : tech.signs().size() * 4;
                dps += d / ((cast + tech.cooldownTicks()) / 20.0);
                n++;
            }
            int bar = Scaling.maxChakra(level, 1);
            t.append(String.format(Locale.ROOT, "| %s | %d | %d | %.1f | %.0f | %.2f | %.2f | %.1f |%n", r.toUpperCase(Locale.ROOT), level, n, dmg / n, cost / n,
                    dmg / cost, dps / n, bar / (cost / n)));
        }
        return t.toString();
    }

    /** Which pillar each build's damage came from, against the elite on Shinobi: builds play their pillar. */
    String pillarShare() {
        var t = new StringBuilder("Where each build's damage comes from (against the elite, Shinobi difficulty)\n\n| Level |");
        for (String f : FOCI) t.append(' ').append(f).append(" (T/W/N) |");
        t.append("\n|---|---|---|---|---|\n");
        for (int lv : new int[]{10, 18, 30, 50}) {
            t.append("| ").append(lv).append(" |");
            for (String f : FOCI) {
                var s = duel("sim." + f + "." + lv, ELITE, lv, Difficulty.SHINOBI, Fighter.Skill.AVERAGE).share();
                double sum = s.values().stream().mapToDouble(Double::doubleValue).sum();
                t.append(String.format(Locale.ROOT, " %.0f/%.0f/%.0f |", 100 * s.getOrDefault(Pillar.TAIJUTSU, 0.0) / sum,
                        100 * s.getOrDefault(Pillar.WEAPONS, 0.0) / sum, 100 * s.getOrDefault(Pillar.NINJUTSU, 0.0) / sum));
            }
            t.append('\n');
        }
        return t.toString();
    }

    double pvp(String a, String b, Difficulty diff) {
        double wins = 0;
        for (int i = 0; i < runs; i++) {
            var battle = new Battle(data, diff, seed * 17 + i * 104729L + a.hashCode() * 3L + b.hashCode());
            boolean swap = i % 2 == 1;
            battle.add(Fighter.player(data, data.builds.get(swap ? b : a), Fighter.Skill.AVERAGE, 0), 0);
            battle.add(Fighter.player(data, data.builds.get(swap ? a : b), Fighter.Skill.AVERAGE, 1), 8);
            var r = battle.run();
            boolean aWon = r.winner() == (swap ? 1 : 0) && !r.timeout();
            if (aWon) wins++;
            else if (r.timeout()) wins += 0.5;
        }
        return wins / runs;
    }

    String matrix(int[] levels) {
        var t = new StringBuilder("Build against build (row's win rate against the column, both average skill, Shinobi rules)\n\n");
        for (int lv : levels) {
            t.append("Level ").append(lv).append("\n\n| |");
            for (String f : FOCI) t.append(' ').append(f).append(" |");
            t.append("\n|---|---|---|---|---|\n");
            for (String a : FOCI) {
                t.append("| ").append(a).append(" |");
                for (String b : FOCI) {
                    if (a.equals(b)) { t.append(" — |"); continue; }
                    t.append(String.format(Locale.ROOT, " %.0f%% |", 100 * pvp("sim." + a + "." + lv, "sim." + b + "." + lv, Difficulty.SHINOBI)));
                }
                t.append('\n');
            }
            t.append('\n');
        }
        return t.toString();
    }

    /** The squad at a fight: Beta 1 fights alone; from the team assignment on, two teammates come along (except duels). */
    static int allies(CombatData.Boss b) {
        String id = b.id();
        if (id.contains("ch2.") || id.contains("ch17.") || id.contains("ch19.finals")) return 0;
        return 2;
    }
    static int buildLevel(int bossLevel) {
        int best = 3;
        for (int lv : new int[]{3, 11, 14, 16, 18}) if (Math.abs(lv - bossLevel) <= Math.abs(best - bossLevel)) best = lv;
        return best;
    }

    Stats boss(CombatData.Boss b, String focus, Difficulty diff, Fighter.Skill skill) {
        double wins = 0, time = 0, hp = 0;
        int lv = buildLevel(b.level());
        for (int i = 0; i < runs; i++) {
            var battle = new Battle(data, diff, seed * 7 + i * 7907L + b.id().hashCode() + focus.hashCode());
            battle.add(Fighter.player(data, data.builds.get("sim.beta." + focus + "." + lv), skill, 0), 0);
            for (int k = 0; k < allies(b); k++)
                battle.add(Fighter.enemy(data, data.enemies.get("combat:enemy.spar.genin"), lv, diff, 0, null, true), -1 - k);
            if (data.enemies.containsKey(b.base())) {
                var f = battle.add(Fighter.enemy(data, data.enemies.get(b.base()), b.level(), diff, 1, b, false), 9);
                battle.boss(b, f);
            } else {
                var members = data.groups.get(b.base());
                Fighter first = null;
                double x = 9;
                for (var m : members) {
                    int count = dev.shinobi.combat.Json.integer(m, "count", 1);
                    var pick = m.containsKey("pick") ? dev.shinobi.combat.Json.strings(m, "pick") : List.of(dev.shinobi.combat.Json.str(m, "enemy", "?"));
                    for (int k = 0; k < count; k++) {
                        var e = data.enemies.get(pick.get((i + k) % pick.size()));
                        var f = battle.add(Fighter.enemy(data, e, b.level(), diff, 1, b, false), x++);
                        if (first == null) first = f;
                    }
                }
                battle.boss(b, first);
            }
            var r = battle.run();
            if (r.winner() == 0) { wins++; time += r.ticks() / 20.0; hp += r.playerHp(); }
        }
        return new Stats(wins / runs, wins == 0 ? 0 : time / wins, wins == 0 ? 0 : hp / wins, Map.of());
    }

    List<CombatData.Boss> betaBosses() {
        var out = new ArrayList<CombatData.Boss>();
        for (var b : data.bosses.values())
            if (List.of("beta1", "beta2", "beta3").contains(b.slice()) && !b.id().contains("bell_test")) out.add(b);
        out.sort((x, y) -> Integer.compare(x.level(), y.level()));
        return out;
    }

    String bosses(Difficulty diff) {
        var t = new StringBuilder("The beta's bosses, ").append(diff.id()).append(" (win rate, mean seconds, player health left), the beta loadout at the fight's level, average skill");
        t.append("; novice skill in brackets\n\n| Boss | Level | Squad |");
        for (String f : FOCI) t.append(' ').append(f).append(" |");
        t.append("\n|---|---|---|---|---|---|---|\n");
        for (var b : betaBosses()) {
            t.append("| ").append(b.id().replace("combat:boss.", "")).append(" | ").append(b.level()).append(" | ").append(allies(b) > 0 ? "+2" : "alone").append(" |");
            for (String f : FOCI) {
                var s = boss(b, f, diff, Fighter.Skill.AVERAGE);
                var n = boss(b, f, diff, Fighter.Skill.NOVICE);
                t.append(String.format(Locale.ROOT, " %.0f%% %.0fs %.0f%% (%.0f%%) |", s.win() * 100, s.seconds(), s.hpLeft() * 100, n.win() * 100));
            }
            t.append('\n');
        }
        t.append("\nThe bell test (Ch 8) is a scripted objective, not a health race, so it is not simulated.\n");
        return t.toString();
    }
}
