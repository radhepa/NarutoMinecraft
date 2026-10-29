package dev.shinobi.combat.sim;

import dev.shinobi.combat.Chakra;
import dev.shinobi.combat.CombatData;
import dev.shinobi.combat.Cooldowns;
import dev.shinobi.combat.Difficulty;
import dev.shinobi.combat.Json;
import dev.shinobi.combat.Nature;
import dev.shinobi.combat.Pool;
import dev.shinobi.combat.RangeBands;
import dev.shinobi.combat.Scaling;
import dev.shinobi.combat.Scaling.Pillar;
import dev.shinobi.combat.StatusEffects;
import dev.shinobi.combat.Style;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * One fighter in a simulated battle: a player build or an enemy loadout, its bars, statuses, cooldowns and how
 * well it reacts. The brain lives in {@link Battle}.
 */
final class Fighter {
    /** How well a fighter reads telegraphs: chances to dodge, parry and block a readable attack. */
    record Skill(double dodge, double parry, double block) {
        static final Skill NOVICE = new Skill(0.2, 0.05, 0.25), AVERAGE = new Skill(0.35, 0.15, 0.3), SKILLED = new Skill(0.55, 0.3, 0.3);
    }

    final String name;
    final int side;
    final boolean player, boss;
    final int level;
    final Nature affinity;
    final double maxHp;
    final Chakra chakra;
    final Pool stamina, poise;
    final StatusEffects status;
    final Cooldowns cd = new Cooldowns();
    final Style moves;
    final int tier, gatesKnown, control;
    final Map<Pillar, Integer> ranks;
    final CombatData.Weapon melee, thrown;
    final List<CombatData.Technique> techniques;
    final double physical, chakraArmour, will;
    final Skill skill;
    final RangeBands.Band band;
    final boolean animal, substitutes, nonlethal;
    final String rank;
    final Map<String, Integer> repeats = new HashMap<>();
    double damageMult = 1;
    int think;

    double hp, x, momentum;
    int ammo, bombs;
    long busyUntil, castUntil, counterUntil, focusUntil, gateUntil, buffUntil, fooledUntil;
    int gateOpen;
    double buffDamage = 1, buffTaken = 1;
    boolean casting, interrupted, subUsed, airborneTarget;
    Fighter target;
    Battle.Chain chain;

    private Fighter(String name, int side, boolean player, boolean boss, int level, Nature affinity, double maxHp, double maxChakra,
                    double maxStamina, double maxPoise, Map<String, StatusEffects.Def> defs, Style moves, int tier, int gates, int control,
                    Map<Pillar, Integer> ranks, CombatData.Weapon melee, CombatData.Weapon thrown, List<CombatData.Technique> techniques,
                    double physical, double chakraArmour, double will, Skill skill, RangeBands.Band band, boolean animal, boolean substitutes,
                    boolean nonlethal, String rank, int ammo, int bombs) {
        this.name = name; this.side = side; this.player = player; this.boss = boss; this.level = level; this.affinity = affinity;
        this.maxHp = maxHp; this.hp = maxHp; this.chakra = new Chakra(maxChakra); this.stamina = Pool.stamina(maxStamina);
        this.poise = Pool.poise(maxPoise); this.status = new StatusEffects(defs, boss); this.moves = moves; this.tier = tier;
        this.gatesKnown = gates; this.control = control; this.ranks = ranks; this.melee = melee; this.thrown = thrown;
        this.techniques = techniques; this.physical = physical; this.chakraArmour = chakraArmour; this.will = will; this.skill = skill;
        this.band = band; this.animal = animal; this.substitutes = substitutes; this.nonlethal = nonlethal; this.rank = rank;
        this.ammo = ammo; this.bombs = bombs;
    }

    /** A player build from data/combat/sim/builds.json. */
    static Fighter player(CombatData data, CombatData.Build b, Skill skill, int side) {
        var techs = new ArrayList<CombatData.Technique>();
        for (String t : b.techniques()) techs.add(data.technique(t));
        var melee = b.melee() == null ? null : data.weapons.get(b.melee());
        var thrown = b.thrown() == null ? null : data.weapons.get(b.thrown());
        int ammo = 0;
        for (var e : b.tools().entrySet()) if (e.getKey().contains("kunai") || e.getKey().contains("shuriken")) ammo += ((Number) e.getValue()).intValue();
        if (thrown != null && thrown.item().endsWith("_practice")) ammo = 999;
        int bombs = ((Number) b.tools().getOrDefault("item:paper_bomb", 0.0)).intValue();
        double stamina = 100 + 5 * (b.rank(Pillar.TAIJUTSU) - 1);
        double poise = 20 + 2 * (b.rank(Pillar.TAIJUTSU) - 1) + (b.style().contains("strong_fist") ? 8 : 0);
        String styleId = b.style();
        if (melee != null && melee.style() != null && b.focus().equals("weapons") && Json.num(melee.melee(), "damage", 0) >= 2) styleId = melee.style();
        var band = switch (b.focus()) {
            case "ninjutsu" -> RangeBands.Band.MID;
            case "weapons" -> b.level() >= 15 || b.level() < 5 ? RangeBands.Band.CLOSE : RangeBands.Band.MID;
            default -> RangeBands.Band.CLOSE;
        };
        return new Fighter(b.id(), side, true, false, b.level(), b.nature(), Scaling.playerHp(b.level(), 0),
                Scaling.maxChakra(b.level(), 1), stamina, poise, data.statuses, data.moveset(styleId), b.styleTier(), b.gates(), b.control(),
                b.ranks(), melee, thrown, techs, b.physical(), b.chakraArmour(), 10 + 0.5 * b.level(), skill, band, false, true, false, "player",
                ammo, bombs);
    }

    /** An enemy (or an ally built from an enemy loadout) at a level, with a boss's overrides when given. */
    static Fighter enemy(CombatData data, CombatData.Enemy e, int level, Difficulty diff, int side, CombatData.Boss boss, boolean ally) {
        var techs = new ArrayList<CombatData.Technique>();
        List<String> tids = boss != null && !boss.techniques().isEmpty() ? boss.techniques() : e.techniques();
        for (String t : tids) techs.add(data.technique(t));
        List<String> weapons = boss != null && !boss.weapons().isEmpty() ? boss.weapons() : e.weapons();
        CombatData.Weapon melee = null, thrown = null;
        for (String w : weapons) {
            var wd = data.weapons.get(w);
            if (w.equals("vanilla:bow")) { thrown = bow(); continue; }
            if (wd == null) continue;
            if (melee == null && wd.canMelee() && !"thrown".equals(wd.cls())) melee = wd;
            if (thrown == null && wd.canThrow()) thrown = wd;
        }
        String style = boss != null && boss.style() != null ? boss.style() : e.style();
        if (style == null && melee != null && melee.style() != null) style = melee.style();
        var react = Json.obj(data.ai, "reactions");
        String rank = e.animal() ? "genin" : e.rank().equals("beast") ? "genin" : e.rank();
        double dodge = Json.num(Json.obj(react, "dodge_by_rank"), rank, 0.2) * diff.enemyDodgeMult();
        double parry = Json.num(Json.obj(react, "parry_by_rank"), rank, 0.1) * diff.enemyDodgeMult();
        if (e.ai().get("dodge") instanceof Number n) dodge = n.doubleValue();
        if (e.ai().get("parry") instanceof Number n) parry = n.doubleValue();
        double hpMult = boss != null ? boss.hpMult() : e.hpMult();
        double hp = Scaling.enemyHp(level, hpMult) * (ally ? 1 : diff.enemyHp());
        var armour = boss != null && !boss.armour().isEmpty() ? boss.armour() : e.armour();
        int tier = Math.min(5, 1 + switch (e.rank()) { case "chunin" -> 1; case "jonin" -> 2; case "kage" -> 3; default -> 0; } + level / 20);
        boolean subs = !e.animal() && !"civilian".equals(e.rank()) && !"academy".equals(e.rank());
        int ammo = 0;
        for (var t : e.tools().entrySet()) if (t.getKey().contains("kunai") || t.getKey().contains("shuriken")) ammo += ((Number) t.getValue()).intValue();
        if (thrown != null) ammo = Math.max(ammo, 12);
        int bombs = ((Number) e.tools().getOrDefault("item:paper_bomb", 0.0)).intValue();
        var ranks = Map.of(Pillar.TAIJUTSU, 1, Pillar.WEAPONS, 1, Pillar.NINJUTSU, 1);
        double poise = boss != null ? boss.poise() : e.poise();
        boolean nonlethal = e.traits().contains("nonlethal") || boss != null && boss.nonlethal();
        var f = new Fighter(boss != null ? boss.id() : e.id(), side, false, boss != null, level, e.nature(), hp, Scaling.maxChakra(level, 1),
                100, poise, data.statuses, data.moveset(style), tier, 0, 30 + level, ranks, melee, thrown, techs,
                Json.num(armour, "physical", 0), Json.num(armour, "chakra", 0), Json.num(armour, "will", 10),
                new Skill(dodge, parry, ally ? 0.3 : 0.2), RangeBands.Band.of(e.band()), e.animal(), subs, nonlethal, e.rank(), ammo, bombs);
        var tierData = Json.obj(data.tiers, boss != null && data.enemies.containsKey(boss.base()) ? "boss" : e.tier());
        f.damageMult = boss != null ? boss.damageMult() * (data.enemies.containsKey(boss.base()) ? 1 : e.damageMult()) : Json.num(tierData, "damage", e.damageMult());
        f.think = Json.integer(tierData, "think_ticks", e.thinkTicks());
        return f;
    }

    static CombatData.Weapon bow() {
        return new CombatData.Weapon("vanilla:bow", "thrown", Map.of(),
                Map.of("damage", 3.0, "type", "physical.pierce", "speed", 3.0, "range", 24.0, "recovery_ticks", 20.0, "poise", 2.0), null);
    }

    boolean alive() { return hp > (nonlethal ? 0.3 * maxHp : 0); }
    boolean down() { return !alive(); }
    double hpFraction() { return hp / maxHp; }
    double distance(Fighter o) { return Math.abs(x - o.x); }
    boolean incapacitated() {
        return status.stunned() || status.has("fear") || status.has("confused") || status.has("possessed") || status.has("asleep");
    }
    int rankOf(Pillar p) { return ranks.get(p); }
    double reach() {
        double r = melee != null ? Json.num(melee.melee(), "reach", 2.6) : 2.6;
        if (status.has("expanded")) r *= 1.6;
        return r;
    }
    double speed() {
        double s = animal ? 0.3 : 0.28;
        s *= 1 - status.slow();
        if (gateOpen > 0) s *= 1 + 0.05 * gateOpen;
        if (status.has("shrouded")) s *= 1.3;
        return s;
    }
}
