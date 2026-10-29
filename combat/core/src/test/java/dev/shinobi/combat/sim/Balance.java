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
        out.append(bosses(Difficulty.STORY)).append('\n').append(bosses(Difficulty.SHINOBI)).append('\n');
        out.append(contribution(Difficulty.SHINOBI)).append('\n').append(kindling(Difficulty.SHINOBI));
        return out.toString();
    }

    /** The squad (player and both teammates at one level) against a bounty boss, with each Kindling Bond tier. */
    Stats kindled(int level, dev.shinobi.combat.Kindle.Tier tier, double web, boolean bonfire, Difficulty diff) {
        double wins = 0, time = 0, hp = 0;
        var boss = data.bosses.get("combat:boss.chunin.missing_nin_bounty");
        for (int i = 0; i < runs; i++) {
            var battle = new Battle(data, diff, seed * 19 + i * 6007L + level);
            battle.kindle = tier;
            battle.web = web;
            battle.bonfire = bonfire;
            battle.add(Fighter.player(data, data.builds.get("sim.player." + level), Fighter.Skill.AVERAGE, 0), 0);
            battle.add(Fighter.teammate(data, data.builds.get("sim.teammate_a." + level), Fighter.Skill.AVERAGE, 0), -1);
            battle.add(Fighter.teammate(data, data.builds.get("sim.teammate_b." + level), Fighter.Skill.AVERAGE, 0), -2);
            battle.boss(boss, battle.add(Fighter.enemy(data, data.enemies.get(boss.base()), level + 2, diff, 1, boss, false), 9));
            battle.add(Fighter.enemy(data, data.enemies.get(ELITE), level, diff, 1, null, false), 10);
            var r = battle.run();
            if (r.winner() == 0) { wins++; time += r.ticks() / 20.0; hp += r.playerHp(); }
        }
        return new Stats(wins / runs, wins == 0 ? 0 : time / wins, wins == 0 ? 0 : hp / wins, Map.of());
    }

    String kindling(Difficulty diff) {
        var t = new StringBuilder("Kindling Bond: the squad against a bounty boss two levels up and an elite, ").append(diff.id())
                .append(" (win rate, mean seconds, player health left)\n\n| Kindling | Level 30 | Level 45 |\n|---|---|---|\n");
        Object[][] rows = {{"none", dev.shinobi.combat.Kindle.Tier.NONE, 0.0, false}, {"Spark (kindle)", dev.shinobi.combat.Kindle.Tier.SPARK, 0.0, false},
                {"Flame (kindle, Ember Link)", dev.shinobi.combat.Kindle.Tier.FLAME, 0.0, false}, {"Blaze (and a unison technique)", dev.shinobi.combat.Kindle.Tier.BLAZE, 0.0, false},
                {"Blaze + Bonfire, web 15", dev.shinobi.combat.Kindle.Tier.BLAZE, 15.0, true}, {"Blaze + Bonfire, web 40", dev.shinobi.combat.Kindle.Tier.BLAZE, 40.0, true},
                {"Blaze + Bonfire, web 70", dev.shinobi.combat.Kindle.Tier.BLAZE, 70.0, true}};
        for (var r : rows) {
            t.append("| ").append(r[0]).append(" |");
            for (int lv : new int[]{30, 45}) {
                var s = kindled(lv, (dev.shinobi.combat.Kindle.Tier) r[1], (double) r[2], (boolean) r[3], diff);
                t.append(String.format(Locale.ROOT, " %.0f%% %.0fs %.0f%% |", s.win() * 100, s.seconds(), s.hpLeft() * 100));
            }
            t.append('\n');
        }
        return t.toString();
    }

    /** The ranks session's typical player (seed 20261029): chapter, player level, teammate_a's, teammate_b's (docs/RANKS.md). */
    static final double[][] SQUAD_LEVELS = {{8, 5.8, 5.5, 5.6}, {11, 10.7, 10.0, 10.4}, {14, 15.2, 14.4, 14.9}, {16, 16.6, 15.9, 16.2},
            {20, 18.3, 17.9, 18.3}, {28, 29.9, 29.4, 29.8}, {45, 41.4, 41.0, 41.6}, {60, 50.0, 48.4, 48.8}};

    /** Damage and control shares of each teammate against the player's, in a squad fight against level-matched enemies. */
    record Share(double damage, double control, double combined) {}

    Share[] shares(int pl, int a, int b, Difficulty diff) {
        double[] sum = new double[6];
        for (int i = 0; i < runs; i++) {
            var battle = new Battle(data, diff, seed * 13 + i * 7919L + pl * 31L);
            var p = battle.add(Fighter.player(data, data.builds.get("sim.player." + pl), Fighter.Skill.AVERAGE, 0), 0);
            var ta = battle.add(Fighter.teammate(data, data.builds.get("sim.teammate_a." + a), Fighter.Skill.AVERAGE, 0), -1);
            var tb = battle.add(Fighter.teammate(data, data.builds.get("sim.teammate_b." + b), Fighter.Skill.AVERAGE, 0), -2);
            battle.add(Fighter.enemy(data, data.enemies.get(MOOK), pl, diff, 1, null, false), 8);
            battle.add(Fighter.enemy(data, data.enemies.get(MOOK), pl, diff, 1, null, false), 9);
            battle.add(Fighter.enemy(data, data.enemies.get(ELITE), pl, diff, 1, null, false), 10);
            battle.run();
            int k = 0;
            for (var f : new Fighter[]{p, ta, tb}) {
                var l = battle.ledger.getOrDefault(f, new double[2]);
                sum[k++] += l[0];
                sum[k++] += l[1] / 20.0;
            }
        }
        double pd = sum[0], pc = sum[1];
        // One second of an enemy held is worth what the squad would deal in half a second: the player's damage a second.
        double perControlSecond = pd / Math.max(1, runs * 20.0) * 0.5;
        var out = new Share[2];
        for (int t = 0; t < 2; t++) {
            double d = sum[2 + 2 * t], c = sum[3 + 2 * t];
            out[t] = new Share(d / pd, pc == 0 ? 0 : c / pc, (d + c * perControlSecond) / (pd + pc * perControlSecond));
        }
        return out;
    }

    String contribution(Difficulty diff) {
        var t = new StringBuilder("Teammates' share of the player's damage, control and the two combined (target 70-110%), squad of three against two rogue genin and a rogue chunin at the player's level, ")
                .append(diff.id()).append("\n\n| Chapter | Player | teammate_a (genjutsu) | damage | control | combined | teammate_b (taijutsu, pup) | damage | control | combined |\n|---|---|---|---|---|---|---|---|---|---|\n");
        for (var row : SQUAD_LEVELS) {
            int pl = (int) Math.round(row[1]), a = (int) Math.round(row[2]), b = (int) Math.round(row[3]);
            var s = shares(pl, a, b, diff);
            t.append(String.format(Locale.ROOT, "| %s | %d | %d | %.0f%% | %.0f%% | %.0f%% | %d | %.0f%% | %.0f%% | %.0f%% |%n",
                    row[0] >= 28 ? (int) row[0] + " h" : "Ch " + (int) row[0], pl, a, 100 * s[0].damage(), 100 * s[0].control(), 100 * s[0].combined(),
                    b, 100 * s[1].damage(), 100 * s[1].control(), 100 * s[1].combined()));
        }
        return t.toString();
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
