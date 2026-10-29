package dev.shinobi.combat.sim;

import dev.shinobi.combat.CombatData;
import dev.shinobi.combat.Damage;
import dev.shinobi.combat.Damage.Delivery;
import dev.shinobi.combat.Damage.Guard;
import dev.shinobi.combat.Difficulty;
import dev.shinobi.combat.Json;
import dev.shinobi.combat.Move;
import dev.shinobi.combat.Nature;
import dev.shinobi.combat.RangeBands;
import dev.shinobi.combat.Scaling;
import dev.shinobi.combat.Scaling.Pillar;
import dev.shinobi.combat.Weaver;
import java.util.ArrayList;
import java.util.EnumMap;
import java.util.List;
import java.util.Map;
import java.util.PriorityQueue;
import java.util.Set;

/**
 * A simulated fight on a line, tick by tick, between two sides. It follows the combat rules in docs/COMBAT.md:
 * the brain keeps its range band, picks the best of its combo strings, throws and techniques by expected damage
 * over time; every attack is telegraphed and the target may dodge, parry, block or substitute; combo strings run
 * on the real {@link dev.shinobi.combat.ComboMachine} timings; weaving takes its signs' ticks and is interrupted by
 * hits; poise breaks stagger; momentum feeds finishers; gates, buffs, statuses and boss phases with adds apply.
 * It is a balance model, not the game: positions are one-dimensional and the AI is the shared simple brain.
 */
final class Battle {
    static final int MAX_TICKS = 20 * 300;
    static final double ARENA = 30;
    static final Set<String> CONTROL = Set.of("bound", "stunned", "possessed", "shocked", "knocked_down", "airborne", "fear", "confused",
            "asleep", "paralysed", "blinded", "chakra_sealed", "genjutsu", "drowsy", "numbed", "mind_transferred");
    static final Set<String> SELF_BUFFS = Set.of("hardened", "shrouded", "expanded", "blade_flow.fire", "blade_flow.wind", "blade_flow.lightning",
            "blade_flow.earth", "blade_flow.water", "butterfly");

    record Result(int winner, long ticks, double playerHp, Map<Pillar, Double> playerDamage, boolean timeout) {}

    /** One telegraphed hit on its way. Strikes of one combo string share a {@link Chain}. */
    static final class Chain { boolean broken, blocked, landed; }
    record Strike(Fighter by, Fighter to, long land, int telegraph, Delivery delivery, double base, String type, double poise, Pillar pillar,
                  int pillarRank, double mult, List<Map.Entry<String, Integer>> statuses, double area, String tech, boolean guardBreak,
                  boolean launches, boolean knocksDown, double knockback, Chain chain, int index) {}
    private record Event(long tick, long seq, Runnable run) {}

    final CombatData data;
    final Difficulty diff;
    final Rng rng;
    final List<Fighter> fighters = new ArrayList<>();
    private final PriorityQueue<Event> events = new PriorityQueue<>((a, b) -> a.tick != b.tick ? Long.compare(a.tick, b.tick) : Long.compare(a.seq, b.seq));
    private final Map<Pillar, Double> playerDamage = new EnumMap<>(Pillar.class);
    /** What each fighter did: damage dealt, ticks of control (stun, bind, fear...) applied to enemies. */
    final Map<Fighter, double[]> ledger = new java.util.HashMap<>();
    private long now, seq;
    boolean trace;
    /** Kindling Bond for this fight: the player's tier with the teammates, the bond web, and whether Bonfire is open. */
    dev.shinobi.combat.Kindle.Tier kindle = dev.shinobi.combat.Kindle.Tier.NONE;
    double web;
    boolean bonfire, unisonUsed;
    private long linkUntil;
    private CombatData.Boss boss;
    private Fighter bossFighter;
    private int phase;

    Battle(CombatData data, Difficulty diff, long seed) { this.data = data; this.diff = diff; this.rng = new Rng(seed); }

    Fighter add(Fighter f, double x) { f.x = x; fighters.add(f); return f; }
    void boss(CombatData.Boss b, Fighter f) { this.boss = b; this.bossFighter = f; this.phase = 1; }

    Result run() {
        var player = player();
        if (player != null && kindle.ordinal() >= dev.shinobi.combat.Kindle.Tier.FLAME.ordinal())
            linkUntil = dev.shinobi.combat.Kindle.EmberLink.TICKS;
        if (player != null && bonfire) {
            var form = dev.shinobi.combat.Kindle.bonfire(web);
            for (var f : fighters) if (f.side == player.side && f.pillars) {
                f.kindleDamage = f == player ? form.damage() : form.allyPower();
                f.kindleTaken = f == player ? form.taken() : 1;
            }
            at(form.ticks(), () -> { for (var f : fighters) { f.kindleDamage = 1; f.kindleTaken = 1; } });
        }
        for (; now < MAX_TICKS; now++) {
            tickFighters();
            while (!events.isEmpty() && events.peek().tick <= now) events.poll().run.run();
            phases();
            for (var f : List.copyOf(fighters)) if (f.alive() && now >= f.busyUntil && !f.incapacitated()) act(f);
            int a = aliveOn(0), b = aliveOn(1);
            if (a == 0 || b == 0) return result(a > 0 ? 0 : 1, false);
        }
        return result(1, true);
    }
    private Fighter player() { for (var f : fighters) if (f.player) return f; return null; }

    /** Kindle: when a bonded teammate casts, the player may push chakra into it (once per ally per cooldown). */
    private double kindled(Fighter caster, CombatData.Technique tech, double cost) {
        var p = player();
        if (kindle == dev.shinobi.combat.Kindle.Tier.NONE || p == null || caster == p || !caster.pillars || caster.side != p.side || !p.alive()) return 1;
        String key = "kindle:" + caster.name;
        double pay = dev.shinobi.combat.Kindle.cost(cost, kindle);
        while (!p.kindles.isEmpty() && now - p.kindles.peekFirst() > 1200) p.kindles.pollFirst();
        var burn = dev.shinobi.combat.Kindle.overuse(p.kindles.size() + 1, p.chakra.max());
        if (!p.cd.ready(key, now) || p.chakra.value() < pay + burn.chakra() + 10) return 1;
        p.chakra.drain(pay + burn.chakra());
        p.stamina.spend(burn.stamina());
        p.cd.start(key, now, dev.shinobi.combat.Kindle.cooldown(kindle));
        p.kindles.addLast(now);
        return dev.shinobi.combat.Kindle.boost(kindle).power();
    }

    private Result result(int winner, boolean timeout) {
        double hp = fighters.stream().filter(f -> f.player).mapToDouble(Fighter::hpFraction).findFirst().orElse(0);
        return new Result(winner, now, Math.max(0, hp), playerDamage, timeout);
    }
    private int aliveOn(int side) { int n = 0; for (var f : fighters) if (f.side == side && f.alive()) n++; return n; }

    private void at(long tick, Runnable r) { events.add(new Event(Math.max(tick, now), seq++, r)); }

    // --- Bars, statuses, gates -------------------------------------------------------------------

    private void tickFighters() {
        for (var f : fighters) {
            if (!f.alive()) continue;
            double dot = f.status.tick();
            if (dot > 0) f.hp -= dot * Scaling.enemyDamage(f.level);
            f.chakra.tick(Chakra_COMBAT);
            f.stamina.tick(f.status.has("winded") ? 0.5 : 1);
            f.poise.tick(1);
            if (f.gateOpen > 0) {
                var g = gate(f.gateOpen);
                f.hp -= Json.num(g, "hp_drain_per_second", 0) / 20 * f.maxHp / 20;
                if (now >= f.gateUntil) { f.status.apply("gate_strain", Json.integer(g, "strain_ticks", 200), now); f.gateOpen = 0; }
            }
            if (f.buffUntil > 0 && now >= f.buffUntil) { f.buffDamage = 1; f.buffTaken = 1; f.buffUntil = 0; }
        }
    }
    private static final double Chakra_COMBAT = dev.shinobi.combat.Chakra.COMBAT_MULT;
    private Map<String, Object> gate(int n) {
        for (Object o : Json.list(data.gates, "gates")) { var g = Json.obj(o); if (Json.integer(g, "n", 0) == n) return g; }
        return Map.of();
    }

    private void phases() {
        if (boss == null || !bossFighter.alive() || phase >= boss.phases().size()) return;
        var p = boss.phases().get(phase);
        if (bossFighter.hpFraction() > p.atHp()) return;
        phase++;
        for (String add : p.adds()) spawn(add, boss.level() - 1, bossFighter.x + 2);
    }
    void spawn(String id, int level, double x) {
        if (data.groups.containsKey(id)) {
            for (var m : data.groups.get(id)) {
                int count = Json.integer(m, "count", 1);
                List<String> pick = m.containsKey("pick") ? Json.strings(m, "pick") : List.of(Json.str(m, "enemy", "?"));
                for (int i = 0; i < count; i++) {
                    String e = pick.get((int) (rng.unit() * pick.size()));
                    add(Fighter.enemy(data, data.enemies.get(e), level, diff, 1, null, false), x + i);
                }
            }
        } else add(Fighter.enemy(data, data.enemies.get(id), level, diff, 1, null, false), x);
    }

    // --- The brain -------------------------------------------------------------------------------

    private interface Plan { double value(); void run(); }

    private void act(Fighter f) {
        if (f.target == null || !f.target.alive()) f.target = pickTarget(f);
        var t = f.target;
        if (t == null) return;
        double d = f.distance(t);

        if (f.gatesKnown > 0 && f.gateOpen == 0 && !f.status.has("gate_strain") && f.hpFraction() > 0.5 && t.hpFraction() > 0.4 && t.maxHp > f.maxHp) {
            f.gateOpen = f.gatesKnown;
            f.gateUntil = now + Json.integer(gate(f.gateOpen), "max_ticks", 300);
            f.busyUntil = now + 10;
            return;
        }
        for (var tech : f.techniques) if (selfBuff(f, tech)) return;
        if (decoy(f)) return;
        if (unison(f, t)) return;
        if (t.status.has("decoy") && !f.player && f.side != t.side && now >= f.fooledUntil && rng.chance(0.6)) {
            f.fooledUntil = now + t.status.remaining("decoy");
            f.busyUntil = now + 30;
            return;
        }

        Plan best = null;
        double bestValue = 0;
        for (var p : plans(f, t, d)) {
            double v = p.value() * (0.85 + 0.3 * rng.unit());
            if (v > bestValue) { bestValue = v; best = p; }
        }
        if (best != null) { best.run(); f.busyUntil += f.think; return; }
        if (flicker(f, t, d)) return;
        move(f, t, d);
    }

    /** A unison technique (Blaze): once a fight, the player and a teammate strike as one: two A-rank casts in one blow. */
    private boolean unison(Fighter f, Fighter t) {
        if (!f.player || kindle != dev.shinobi.combat.Kindle.Tier.BLAZE || unisonUsed || t.hpFraction() > 0.7 || f.distance(t) > 12) return false;
        Fighter mate = null;
        for (var o : fighters) if (o != f && o.side == f.side && o.pillars && o.alive() && o.chakra.value() >= 25) mate = o;
        if (mate == null || f.chakra.value() < 25) return false;
        unisonUsed = true;
        f.chakra.drain(25);
        mate.chakra.drain(25);
        mate.busyUntil = Math.max(mate.busyUntil, now + 20);
        f.busyUntil = now + 24;
        schedule(new Strike(f, t, now + 20, 20, Delivery.JUTSU, 42, "ninjutsu.none", 60, Pillar.NINJUTSU, f.rankOf(Pillar.NINJUTSU), 1, List.of(), 4,
                "combat:unison", true, false, true, 3, new Chain(), 0));
        return true;
    }

    /** The Clone Technique as a defence: when pressed close, copies run off and each enemy may chase one. */
    private boolean decoy(Fighter f) {
        if (!f.player) return false;
        CombatData.Technique clone = null;
        for (var tech : f.techniques) if (tech.id().equals("combat:nin.clone")) clone = tech;
        if (clone == null || !f.cd.ready(clone.id(), now) || !f.status.canCast() || f.status.has("decoy")) return false;
        int close = 0;
        for (var o : fighters) if (o.side != f.side && o.alive() && f.distance(o) < 3) close++;
        if (close == 0 || f.band == RangeBands.Band.CLOSE && f.hpFraction() > 0.6) return false;
        double cost = techCost(f, clone);
        if (f.chakra.value() < cost + 10) return false;
        f.chakra.spend(cost, false);
        f.cd.start(clone.id(), now, clone.cooldownTicks());
        f.status.apply("decoy", 100, now);
        f.busyUntil = now + castTicks(f, clone);
        return true;
    }

    /** Body Flicker: a closer uses it to reach a far target, a caster to break away from a close one. */
    private boolean flicker(Fighter f, Fighter t, double d) {
        CombatData.Technique bf = null;
        for (var tech : f.techniques) if (tech.id().equals("combat:nin.body_flicker")) bf = tech;
        if (bf == null || !f.cd.ready(bf.id(), now) || f.status.rooted() || !f.status.canCast()) return false;
        double cost = techCost(f, bf);
        if (f.chakra.value() < cost + 5) return false;
        boolean close = f.band == RangeBands.Band.CLOSE;
        if (close && d < f.reach() + 4) return false;
        if (!close && (d > 3 || f.hpFraction() > 0.8 && hasRangedReady(f) == false)) return false;
        f.chakra.spend(cost, false);
        f.cd.start(bf.id(), now, bf.cooldownTicks());
        double dir = Math.signum(t.x - f.x);
        if (dir == 0) dir = 1;
        f.x = close ? t.x - dir * (f.reach() - 0.4) : Math.clamp(f.x - dir * 8, -ARENA, ARENA);
        f.busyUntil = now + castTicks(f, bf) + 4;
        return true;
    }

    private Fighter pickTarget(Fighter f) {
        Fighter best = null;
        for (var o : fighters) {
            if (o.side == f.side || !o.alive()) continue;
            if (!f.player && o.player && f.side == 1 && rng.chance(0.45)) return o;
            if (best == null || f.distance(o) < f.distance(best)) best = o;
        }
        return best;
    }

    private void move(Fighter f, Fighter t, double d) {
        f.busyUntil = now + 4;
        if (f.status.rooted()) return;
        double want = f.band == RangeBands.Band.CLOSE ? f.reach() - 0.4 : f.band == RangeBands.Band.MID ? 7 : 12;
        boolean ranged = f.band != RangeBands.Band.CLOSE;
        if (ranged && !hasRangedReady(f)) want = Math.max(want, 9);
        double dir = Math.signum(t.x - f.x);
        if (dir == 0) dir = 1;
        double step = f.speed() * 4;
        if (d > want + 0.3) f.x += dir * Math.min(step, d - want);
        else if (d < want - 0.6 && (f.player || rng.chance(0.5))) f.x = Math.clamp(f.x - dir * step * 0.6, -ARENA, ARENA);
    }
    private boolean hasRangedReady(Fighter f) {
        if (f.thrown != null && f.ammo > 0) return true;
        for (var tech : f.techniques) if (tech.power() > 0 && tech.range() > 4 && f.cd.ready(tech.id(), now) && f.chakra.value() >= tech.chakra()) return true;
        return false;
    }

    /** Attack tokens: only so many enemies may press the player at once; the rest throw, circle or fight the squad. */
    private boolean hasToken(Fighter f, Fighter t) {
        if (!t.player || f.side != 1 || f.boss) return true;
        int pressing = 0;
        for (var o : fighters) if (o != f && o.side == 1 && o.alive() && o.target == t && now < o.busyUntil && !o.boss) pressing++;
        for (var o : fighters) if (o.boss && o.alive() && o.target == t) pressing++;
        return pressing < diff.attackTokens();
    }

    private List<Plan> plans(Fighter f, Fighter t, double d) {
        var out = new ArrayList<Plan>();
        if (!hasToken(f, t)) {
            if (f.thrown != null && f.ammo > 0 && d >= 2 && d <= Json.num(f.thrown.thrown(), "range", 16) && rng.chance(0.3)) out.add(throwPlan(f, t, d));
            for (var o : fighters) if (o.side != f.side && o.alive() && !o.player) { f.target = o; break; }
            return out;
        }
        double reach = f.reach();
        boolean counter = now < f.counterUntil;
        String prefix = t.status.has("airborne") && f.airborneTarget ? "J" : counter ? "P" : "";
        if (d <= reach + 0.3) {
            for (var s : f.moves.strings(prefix, f.tier, f.momentum, f.gateOpen)) addString(out, f, t, s, 0);
            if (!prefix.isEmpty()) for (var s : f.moves.strings("", f.tier, f.momentum, f.gateOpen)) addString(out, f, t, s, 0);
        } else if (d <= reach + 4.5 && !f.status.rooted()) {
            for (var s : f.moves.strings("X", f.tier, f.momentum, f.gateOpen)) addString(out, f, t, s, d - reach + 0.3);
        }
        if (f.thrown != null && f.ammo > 0 && d >= 2 && d <= Json.num(f.thrown.thrown(), "range", 16)) out.add(throwPlan(f, t, d));
        if (f.bombs > 0 && d >= 3 && d <= 14 && f.cd.ready("paper_bomb", now)) out.add(bombPlan(f, t, d));
        for (var tech : f.techniques) { var p = techPlan(f, t, d, tech); if (p != null) out.add(p); }
        return out;
    }

    // Expected damage of one hit before the target's reaction, through its armour and nature.
    private double expected(Fighter f, Fighter t, double base, String type, Delivery delivery, Pillar pillar, int rank, double mult) {
        return Damage.hit(attack(f, t, base, type, delivery, pillar, rank, mult), defence(t, Guard.NONE, type)).hp();
    }
    /** How readable an attack is: melee and throws by their wind-up, jutsu by their travel (signs say one is coming, not where). */
    private double tele(Fighter by, Fighter t, int telegraph, Delivery d) {
        double ticks = by.side == 1 && t.side == 0 ? telegraph * diff.telegraphMult() : telegraph;
        if (d == Delivery.JUTSU) return Math.clamp(0.5 + ticks / 12.0, 0.3, 1.0);
        return Math.clamp(ticks / 10.0, 0.3, 1.5);
    }
    private double avoid(Fighter by, Fighter t, int telegraph, Delivery d, double area) {
        if (t.incapacitated()) return 0;
        double tele = tele(by, t, telegraph, d);
        double p = t.skill.dodge() + (d == Delivery.MELEE || d == Delivery.THROWN ? t.skill.parry() : 0);
        if (area >= 2) p *= Math.max(0.3, 1 - area / 8);
        return Math.min(0.9, p * tele);
    }

    private void addString(List<Plan> out, Fighter f, Fighter t, List<Move> s, double dash) {
        double stamina = 0, momentum = 0, damage = 0;
        long ticks = 0, prevEnd = 0;
        for (int i = 0; i < s.size(); i++) {
            var m = s.get(i);
            long start = i == 0 ? 0 : prevEnd;
            prevEnd = start + m.startup() + m.active() + m.windowOpen();
            ticks = start + m.length();
            stamina += m.stamina();
            momentum += m.momentumCost();
            damage += expected(f, t, moveBase(f, m), moveType(f, m), Delivery.MELEE, movePillar(f, m), f.rankOf(movePillar(f, m)), meleeMult(f));
        }
        if (stamina > f.stamina.value() + 5 || momentum > f.momentum) return;
        var first = s.get(0);
        double chakra = 0;
        for (var m : s) chakra += m.chakra();
        if (chakra > f.chakra.value()) return;
        double hit = 1 - avoid(f, t, Math.max(4, first.startup()), Delivery.MELEE, first.area());
        final double v = damage * hit / Math.max(1, ticks + dash / 0.5) * (first.finisher() ? 1.1 : 1);
        final long total = ticks;
        final double cost = chakra;
        out.add(new Plan() {
            public double value() { return v; }
            public void run() { runString(f, t, s, dash, total, cost); }
        });
    }
    private double moveBase(Fighter f, Move m) {
        double base = m.damage();
        if (m.weaponMult() && f.melee != null) base *= Json.num(f.melee.melee(), "damage", 1);
        if (f.animal) base *= 0.9;
        return base;
    }
    private String moveType(Fighter f, Move m) {
        if (m.weaponMult() && f.melee != null && m.type().startsWith("physical")) return Json.str(f.melee.melee(), "type", m.type());
        return m.type();
    }
    private Pillar movePillar(Fighter f, Move m) { return m.weaponMult() ? Pillar.WEAPONS : Pillar.TAIJUTSU; }
    private double meleeMult(Fighter f) {
        double m = Scaling.styleMult(f.tier) * f.buffDamage;
        if (f.gateOpen > 0) m *= 1 + Json.num(gate(f.gateOpen), "damage", 0);
        if (f.status.has("gate_strain")) m *= 0.6;
        return m;
    }

    private void runString(Fighter f, Fighter t, List<Move> s, double dash, long total, double chakra) {
        if (dash > 0) f.x += Math.signum(t.x - f.x) * dash;
        var chain = new Chain();
        double counter = s.get(0).input().get(0).equals("P") ? 1.5 : 1;
        long start = now, prevEnd = 0;
        double stamina = 0;
        for (int i = 0; i < s.size(); i++) {
            var m = s.get(i);
            long st = i == 0 ? start : prevEnd;
            prevEnd = st + m.startup() + m.active() + m.windowOpen();
            stamina += m.stamina();
            f.momentum -= m.momentumCost();
            var statuses = new ArrayList<Map.Entry<String, Integer>>();
            boolean kb = Json.num(m.effects(), "knockback", 0) > 0;
            Pillar pillar = movePillar(f, m);
            var strike = new Strike(f, t, st + m.startup(), i == 0 ? Math.max(4, m.startup()) : 0, Delivery.MELEE, moveBase(f, m), moveType(f, m),
                    m.poise() * (f.moves.id().contains("strong_fist") ? 1.3 : 1), pillar, f.rankOf(pillar), meleeMult(f) * counter, statuses, m.area(), null,
                    m.guardBreak(), m.launches(), m.knocksDown(), kb ? Json.num(m.effects(), "knockback", 0) : 0, chain, i);
            schedule(strike);
        }
        f.chain = chain;
        f.stamina.spend(stamina);
        if (chakra > 0) f.chakra.drain(chakra);
        f.counterUntil = 0;
        f.busyUntil = now + total;
    }

    private Plan throwPlan(Fighter f, Fighter t, double d) {
        var w = f.thrown.thrown();
        double speed = Json.num(w, "speed", 2), base = Json.num(w, "damage", 2);
        var fanRule = Json.obj(w, "fan_of_three");
        boolean fan = !fanRule.isEmpty() && f.rankOf(Pillar.WEAPONS) >= Json.integer(fanRule, "rank", 2);
        double mult = fan ? Json.num(fanRule, "mult", 1) : 1;
        int recovery = (int) Json.num(w, "recovery_ticks", 8) + (fan ? Json.integer(fanRule, "recovery_ticks", 0) : 0);
        int travel = (int) Math.ceil(d / speed);
        double hit = 1 - avoid(f, t, 6 + travel, Delivery.THROWN, 0) * (fan ? Json.num(fanRule, "dodge_mult", 1) : 1);
        double v = expected(f, t, base, Json.str(w, "type", "physical.pierce"), Delivery.THROWN, Pillar.WEAPONS, f.rankOf(Pillar.WEAPONS), mult * f.buffDamage)
                * hit / (recovery + 4);
        return new Plan() {
            public double value() { return v; }
            public void run() {
                f.ammo--;
                f.stamina.spend(2);
                schedule(new Strike(f, t, now + 2 + travel, 6 + travel, Delivery.THROWN, base, Json.str(w, "type", "physical.pierce"),
                        Json.num(w, "poise", 1), Pillar.WEAPONS, f.rankOf(Pillar.WEAPONS), mult * f.buffDamage, List.of(), 0, null, false, false, false, 0,
                        new Chain(), 0));
                f.busyUntil = now + recovery + 2;
            }
        };
    }
    private Plan bombPlan(Fighter f, Fighter t, double d) {
        double v = expected(f, t, 6, "physical.blunt", Delivery.AREA, Pillar.WEAPONS, f.rankOf(Pillar.WEAPONS), 1) * (1 - bombAvoid(t)) / 14;
        return new Plan() {
            public double value() { return v; }
            public void run() {
                f.bombs--;
                f.cd.start("paper_bomb", now, 60);
                schedule(new Strike(f, t, now + 30, 30, Delivery.AREA, 6, "physical.blunt", 30, Pillar.WEAPONS, f.rankOf(Pillar.WEAPONS), 1, List.of(), 3,
                        null, false, false, true, 1.5, new Chain(), 0));
                f.busyUntil = now + 10;
            }
        };
    }

    private double techCost(Fighter f, CombatData.Technique tech) {
        double rebate = 1 - 0.02 * (f.rankOf(Pillar.NINJUTSU) - 1);
        return dev.shinobi.combat.Chakra.cost(tech.chakra(), f.control, tech.nature() != Nature.NONE && tech.nature() == f.affinity, 0.95 * rebate);
    }
    private int castTicks(Fighter f, CombatData.Technique tech) {
        if (tech.signless()) return tech.castTicks();
        int ninRank = f.player ? f.rankOf(Pillar.NINJUTSU) : switch (f.rank) { case "chunin" -> 3; case "jonin" -> 6; default -> 1; };
        return tech.signs().size() * Weaver.ticksPerSign(f.control, ninRank);
    }
    private boolean selfBuff(Fighter f, CombatData.Technique tech) {
        if (tech.power() > 0 || !tech.shapeType().equals("self")) return false;
        String buff = null;
        int ticks = 0;
        for (var s : tech.statuses()) if (SELF_BUFFS.contains(s.getKey())) { buff = s.getKey(); ticks = s.getValue(); }
        if (buff == null || f.status.has(buff) || !f.cd.ready(tech.id(), now)) return false;
        double cost = techCost(f, tech);
        if (f.chakra.value() < cost + 10 || f.target == null || f.distance(f.target) < 4) return false;
        f.chakra.spend(cost, false);
        int cast = castTicks(f, tech);
        f.status.apply(buff, ticks, now);
        f.cd.start(tech.id(), now, Math.max(tech.cooldownTicks(), ticks));
        f.buffUntil = now + ticks;
        switch (buff) {
            case "hardened" -> f.buffTaken = 0.75;
            case "shrouded" -> { f.buffDamage = 1.2; f.buffTaken = 0.7; }
            case "expanded" -> f.buffDamage = 1.25;
            case "butterfly" -> f.buffDamage = 2.0;
            default -> f.buffDamage = 1.15;
        }
        f.busyUntil = now + cast;
        return true;
    }

    private Plan techPlan(Fighter f, Fighter t, double d, CombatData.Technique tech) {
        boolean control = false;
        for (var s : tech.statuses()) if (CONTROL.contains(s.getKey())) control = true;
        if (tech.power() <= 0 && !control) return null;
        if (!f.cd.ready(tech.id(), now) || !f.status.canCast()) return null;
        for (String r : tech.requires()) {
            if (r.startsWith("item:paper_bomb") && f.bombs <= 0) return null;
            if ((r.startsWith("item:kunai") || r.startsWith("item:shuriken")) && f.ammo <= 0) return null;
        }
        double cost = techCost(f, tech);
        if (f.chakra.value() < cost || f.chakra.exhausted()) return null;
        String shape = tech.shapeType();
        double range = Math.max(tech.range(), shape.equals("melee") ? 3 : 0);
        if (d > range + 0.5) return null;
        int cast = castTicks(f, tech);
        boolean threatened = false;
        for (var o : fighters) if (o.side != f.side && o.alive() && !o.incapacitated() && f.distance(o) < 3) threatened = true;
        if (threatened && cast > 8 && !shape.equals("melee")) return null;
        double speed = tech.speed();
        int travel = shape.equals("projectile") ? (int) Math.ceil(d / speed) : 0;
        String type = tech.damageType() != null ? tech.damageType() : "ninjutsu.none";
        Pillar pillar = tech.kind().equals("weapon") ? Pillar.WEAPONS : Pillar.NINJUTSU;
        int rank = tech.kind().equals("weapon") ? (f.rankOf(Pillar.WEAPONS) + f.rankOf(Pillar.NINJUTSU)) / 2 : f.rankOf(Pillar.NINJUTSU);
        double radius = tech.radius();
        boolean meleeShape = shape.equals("melee");
        double hit = 1 - avoid(f, t, meleeShape ? cast + travel : travel, meleeShape ? Delivery.MELEE : Delivery.JUTSU, radius) * (1 - Math.min(0.6, tech.homing() * 1.5));
        if (!f.player && t.player) hit = Math.min(1, hit);
        if (f.player) hit *= 1 - Math.min(0.45, 0.15 * f.repeats.getOrDefault(tech.id(), 0) * diff.habitAdaptation());
        double dmg = tech.power() > 0 ? expected(f, t, tech.power() * 1.03, type, Delivery.JUTSU, pillar, rank, f.buffDamage) : 0;
        double ctrl = 0;
        for (var s : tech.statuses()) if (CONTROL.contains(s.getKey())) ctrl += (s.getValue() > 0 ? s.getValue() : 40) * 0.12;
        double scarcity = 1 - 0.5 * cost / Math.max(1, f.chakra.value());
        double v = (dmg + ctrl) * hit * scarcity / Math.max(8, cast + travel + 6);
        final double c = cost;
        final int fc = cast, ft = travel;
        final double fr = radius;
        return new Plan() {
            public double value() { return v; }
            public void run() { cast(f, t, tech, c, fc, ft, type, pillar, rank, fr); }
        };
    }

    private void cast(Fighter f, Fighter t, CombatData.Technique tech, double cost, int cast, int travel, String type, Pillar pillar, int rank, double radius) {
        f.chakra.spend(cost, false);
        for (String r : tech.requires()) {
            if (r.startsWith("item:paper_bomb")) f.bombs--;
            else if (r.startsWith("item:kunai") || r.startsWith("item:shuriken")) f.ammo--;
        }
        f.cd.start(tech.id(), now, tech.cooldownTicks());
        if (f.player) { f.repeats.replaceAll((k, v) -> Math.max(0, v - 1)); f.repeats.merge(tech.id(), 2, Integer::sum); }
        f.casting = cast > 0;
        f.interrupted = false;
        f.busyUntil = now + cast + 4;
        at(now + cast, () -> {
            f.casting = false;
            if (f.interrupted || !f.alive()) { f.chakra.restore(cost * (1 - Weaver.INTERRUPT_COST)); return; }
            if (!t.alive()) return;
            if (tech.dash()) f.x = t.x - Math.signum(t.x - f.x) * 1.5;
            if (tech.shapeType().equals("melee") && f.distance(t) > tech.range() + 1) return;
            var statuses = new ArrayList<Map.Entry<String, Integer>>();
            for (var s : tech.statuses()) if (!SELF_BUFFS.contains(s.getKey()) && data.statuses.containsKey(s.getKey())) statuses.add(s);
            double kb = 0;
            for (var e : tech.effects()) kb = Math.max(kb, Json.num(e, "knockback", 0));
            boolean knocks = false;
            for (var s : statuses) if (s.getKey().equals("knocked_down")) knocks = true;
            boolean melee = tech.shapeType().equals("melee");
            double k = kindled(f, tech, cost);
            schedule(new Strike(f, t, now + travel, melee ? cast + travel : travel, melee ? Delivery.MELEE : Delivery.JUTSU,
                    tech.power() * 1.03, type, tech.power() * 1.2, pillar, rank, f.buffDamage * k, statuses,
                    radius * (k > 1 ? dev.shinobi.combat.Kindle.boost(kindle).area() : 1), tech.id(), tech.breaksGuard(),
                    false, knocks, kb, new Chain(), 0));
        });
    }

    // --- Resolving hits ----------------------------------------------------------------------------

    private void schedule(Strike s) { at(s.land(), () -> resolve(s)); }

    private void resolve(Strike s) {
        var f = s.by();
        if (s.chain().broken) return;
        if (s.delivery() == Delivery.MELEE && (!f.alive() || f.incapacitated())) { s.chain().broken = true; return; }
        var victims = new ArrayList<Fighter>();
        if (s.to().alive()) victims.add(s.to());
        if (s.area() >= 2)
            for (var o : fighters) if (o != s.to() && o.side != f.side && o.alive() && Math.abs(o.x - s.to().x) <= s.area()) victims.add(o);
        for (var v : victims) hitOne(s, v);
    }

    private void hitOne(Strike s, Fighter f0) {
        var by = s.by();
        if (s.delivery() == Delivery.MELEE && by.distance(f0) > by.reach() + 0.8 + s.area() && s.tech() == null) { if (s.index() == 0) s.chain().broken = true; return; }
        Guard guard = Guard.NONE;
        boolean first = s.index() == 0;
        if (first || f0 != s.to()) guard = react(by, f0, s);
        else if (s.chain().blocked) guard = Guard.BLOCK;
        if (guard == Guard.DODGE || guard == Guard.PARRY) {
            if (f0 == s.to()) s.chain().broken = true;
            if (guard == Guard.PARRY) {
                by.status.apply("staggered", 20, now);
                by.interrupted = true;
                f0.counterUntil = now + 12;
                f0.momentum = Math.min(100, f0.momentum + 25);
            } else if (rng.chance(0.4)) { f0.focusUntil = now + 40; f0.momentum = Math.min(100, f0.momentum + 15); }
            return;
        }
        double mult = s.mult();
        if (now < by.focusUntil) { mult *= 1.25; by.focusUntil = 0; }
        var a = attack(by, f0, s.base(), s.type(), s.delivery(), s.pillar(), s.pillarRank(), mult);
        var r = Damage.hit(a, defence(f0, guard, s.type()));
        if (guard == Guard.NONE && f0.substitutes && r.hp() >= 0.15 * f0.maxHp && substitute(f0, by)) return;
        if (guard == Guard.BLOCK && f0 == s.to()) s.chain().blocked = true;
        else if (f0 == s.to()) s.chain().landed = true;
        double dealt = r.hp() * f0.kindleTaken;
        if (now < linkUntil && f0.side == 0 && f0.pillars) {
            var linked = fighters.stream().filter(o -> o.side == 0 && o.pillars && o.alive()).toList();
            if (linked.size() > 1) {
                for (var o : linked) if (o != f0) o.hp -= dealt * (1 - dev.shinobi.combat.Kindle.EmberLink.KEEP) / (linked.size() - 1);
                dealt *= dev.shinobi.combat.Kindle.EmberLink.KEEP;
            }
        }
        f0.hp -= dealt;
        ledger.computeIfAbsent(by, k -> new double[2])[0] += r.hp();
        if (trace) System.out.printf(java.util.Locale.ROOT, "%5d %-34s -> %-34s %-18s %-6s %5.1f  hp %5.1f/%5.1f%n", now, by.name, f0.name,
                s.tech() != null ? s.tech().replace("combat:", "") : s.delivery().name().toLowerCase(), guard, r.hp(), f0.hp, f0.maxHp);
        if (by.player) playerDamage.merge(s.tech() != null && s.pillar() == Pillar.NINJUTSU ? Pillar.NINJUTSU : s.pillar(), r.hp(), Double::sum);
        if (r.chakraDrain() > 0) f0.chakra.drain(r.chakraDrain());
        f0.status.damaged();
        if (by.pup && s.delivery() == Delivery.MELEE && guard == Guard.NONE && ++by.landed % 3 == 0)
            at(now + 4, () -> { if (f0.alive()) schedule(new Strike(by, f0, now, 0, Delivery.MELEE, 2.0 * (1 + Math.max(0, by.level - 18) / 40.0), "physical.slash", 3, Pillar.TAIJUTSU,
                    by.rankOf(Pillar.TAIJUTSU), 1, List.of(), 0, "pup", false, false, false, 0, new Chain(), 1)); });
        if (r.hp() > 0) {
            by.momentum = Math.min(100, by.momentum + (guard == Guard.NONE ? 6 : 2));
            f0.momentum = Math.max(0, f0.momentum - 30);
        }
        boolean flinch = !f0.player || diff.lightHitsInterruptPlayer() || r.hp() >= 0.1 * f0.maxHp;
        boolean breaksWeave = s.delivery() == Delivery.MELEE || r.hp() >= 0.15 * f0.maxHp;
        if (f0.casting && flinch && breaksWeave) f0.interrupted = true;
        if (guard == Guard.NONE && r.hp() > 0 && flinch && !f0.boss && f0.chain != null && s.delivery() != Delivery.AREA) f0.chain.broken = true;
        if (guard == Guard.BLOCK) {
            double cost = r.staminaCost() * (s.guardBreak() ? 2 : 1);
            if (!f0.stamina.spend(cost)) { f0.status.apply("staggered", 20, now); f0.interrupted = true; }
        }
        var type = dev.shinobi.combat.DamageType.of(s.type());
        if (f0.poise.breaks(Damage.poise(s.poise(), type, guard == Guard.BLOCK))) {
            f0.status.apply("staggered", 16, now);
            f0.interrupted = true;
            if (f0.chain != null) f0.chain.broken = true;
        }
        if (guard != Guard.BLOCK || s.delivery() == Delivery.JUTSU) {
            for (var st : s.statuses()) {
                int ticks = st.getValue();
                if (st.getKey().equals("genjutsu") || st.getKey().equals("fear") || st.getKey().equals("confused"))
                    ticks = (int) Math.min((ticks > 0 ? ticks : 60) * Damage.willScale(f0.will), 30);
                if (ticks >= 0) {
                    int applied = f0.status.apply(st.getKey(), ticks, now);
                    if (CONTROL.contains(st.getKey())) ledger.computeIfAbsent(by, k -> new double[2])[1] += applied;
                }
            }
            if (s.knocksDown()) ledger.computeIfAbsent(by, k -> new double[2])[1] += f0.status.apply("knocked_down", 24, now);
            if (s.launches()) { f0.status.apply("airborne", 20, now); by.airborneTarget = true; }
        }
        if (s.knockback() > 0) f0.x = Math.clamp(f0.x + Math.signum(f0.x - by.x == 0 ? 1 : f0.x - by.x) * s.knockback() * (guard == Guard.BLOCK ? 0.5 : 1), -ARENA, ARENA);
    }

    /** A lit paper bomb is seen: anyone free walks out of it about half the time, more with a good dodge. */
    private double bombAvoid(Fighter t) { return t.incapacitated() || t.status.rooted() ? 0 : Math.min(0.85, 0.45 + t.skill.dodge()); }

    private Guard react(Fighter by, Fighter t, Strike s) {
        if (t.incapacitated()) return Guard.NONE;
        if (s.delivery() == Delivery.AREA && s.telegraph() >= 20) return rng.chance(bombAvoid(t)) ? Guard.DODGE : Guard.NONE;
        double tele = tele(by, t, s.telegraph(), s.delivery());
        double committed = now < t.busyUntil - 2 ? 0.6 : 1;
        double area = s.area() >= 2 ? Math.max(0.3, 1 - s.area() / 8) : 1;
        double habit = 1;
        if (by.player && s.tech() != null) habit += Math.min(0.45, 0.15 * Math.max(0, by.repeats.getOrDefault(s.tech(), 0) - 2) * diff.habitAdaptation());
        if (t.stamina.has(22) && t.cd.ready("dodge", now) && rng.chance(t.skill.dodge() * tele * committed * area * habit)) {
            t.stamina.spend(22);
            t.cd.start("dodge", now, 30);
            return Guard.DODGE;
        }
        boolean parryable = s.delivery() == Delivery.MELEE || s.delivery() == Delivery.THROWN;
        double window = t.player ? diff.parryWindow() / 4.0 : 1;
        if (parryable && rng.chance(t.skill.parry() * tele * committed * window)) return Guard.PARRY;
        if (committed == 1 && rng.chance(t.skill.block())) return Guard.BLOCK;
        return Guard.NONE;
    }

    private boolean substitute(Fighter f, Fighter by) {
        if (f.player ? !f.cd.ready("substitution", now) : f.subUsed) return false;
        if (f.chakra.value() < 10 || f.incapacitated() || f.casting) return false;
        if (!rng.chance(f.player ? 0.7 : 0.8)) return false;
        f.chakra.drain(10);
        if (f.player) f.cd.start("substitution", now, 400); else f.subUsed = true;
        f.x = Math.clamp(f.x + Math.signum(f.x - by.x == 0 ? 1 : f.x - by.x) * 5, -ARENA, ARENA);
        return true;
    }

    private Damage.Attack attack(Fighter by, Fighter t, double base, String type, Delivery d, Pillar pillar, int rank, double mult) {
        if (by.pillars) {
            boolean niche = "taijutsu".equals(by.niche) && pillar == Pillar.TAIJUTSU
                    || "genjutsu".equals(by.niche) && (type.equals("genjutsu") || pillar == Pillar.NINJUTSU);
            int level = by.level + (niche ? (int) Math.round(by.nicheEdge) : 0);
            return Damage.Attack.player(base, type, d, level, pillar, rank, mult * by.kindleDamage);
        }
        double difficulty = by.side == 1 && t.side == 0 ? diff.enemyDamage() : 1;
        return Damage.Attack.enemy(base, type, d, by.level, mult * by.damageMult, difficulty);
    }
    private Damage.Defence defence(Fighter t, Guard g, String type) {
        double block = t.moves.id().contains("iron_guard") ? 0.75 : Damage.BLOCK_MELEE;
        double taken = t.status.takenMult(type) * (type.startsWith("physical") ? t.buffTaken : 1);
        return new Damage.Defence(t.pillars, t.level, t.physical, t.chakraArmour, t.will, t.affinity, g, block, taken);
    }
}
