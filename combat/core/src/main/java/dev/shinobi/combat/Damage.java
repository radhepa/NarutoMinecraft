package dev.shinobi.combat;

/**
 * Damage and resistance math (COMBAT.md, "Damage"). One hit is: base x level power x pillar rank x the attacker's
 * multipliers (style tier, counters, gates, clan), then armour of the matching class, the nature triangle against
 * the defender's affinity, the defender's guard, its status multipliers (soaked, hardened) and, for the player,
 * toughness. Enemies scale by their level and the difficulty instead of a pillar.
 */
public final class Damage {
    /** How a hit arrives: guards stop melee best, thrown tools well, jutsu poorly. */
    public enum Delivery { MELEE, THROWN, JUTSU, AREA }
    public enum Guard { NONE, BLOCK, PARRY, DODGE }

    public static final double ARMOUR_K = 20, ARMOUR_CAP = 0.6;
    public static final double BLOCK_MELEE = 0.6, BLOCK_THROWN = 0.8, BLOCK_JUTSU = 0.3;
    public static final double GUARD_STAMINA_PER_DAMAGE = 4;
    public static final double CHAKRA_HP_SHARE = 0.5;
    public static final double WILL_K = 40;

    /** Who strikes: a player (pillar and rank) or an enemy (its level and the difficulty's damage). */
    public record Attack(double base, DamageType type, Delivery delivery, int level, Scaling.Pillar pillar, int pillarRank,
                         double mult, boolean enemy, double difficulty) {
        public static Attack player(double base, String type, Delivery d, int level, Scaling.Pillar pillar, int rank, double mult) {
            return new Attack(base, DamageType.of(type), d, level, pillar, rank, mult, false, 1);
        }
        public static Attack enemy(double base, String type, Delivery d, int level, double mult, double difficulty) {
            return new Attack(base, DamageType.of(type), d, level, null, 1, mult, true, difficulty);
        }
        public double raw() {
            double scale = enemy ? Scaling.enemyDamage(level) * difficulty : Scaling.power(level, pillar) * Scaling.pillar(pillarRank);
            return base * scale * mult;
        }
    }
    /** Who is struck: armour by class, will, affinity, guard and the status multipliers on what it takes. */
    public record Defence(boolean player, int level, double physical, double chakra, double will, Nature affinity, Guard guard,
                          double blockReduction, double takenMult) {
        public static Defence of(boolean player, int level, double physical, double chakra, Nature affinity) {
            return new Defence(player, level, physical, chakra, 10, affinity, Guard.NONE, BLOCK_MELEE, 1);
        }
        public Defence guarding(Guard g) { return new Defence(player, level, physical, chakra, will, affinity, g, blockReduction, takenMult); }
        public Defence taking(double m) { return new Defence(player, level, physical, chakra, will, affinity, guard, blockReduction, m); }
    }
    public record Result(double hp, double chakraDrain, double staminaCost, boolean blocked, boolean avoided) {}

    public static double armourReduction(double armour, double pierce) {
        double a = Math.max(0, armour * (1 - pierce));
        return Math.min(ARMOUR_CAP, a / (a + ARMOUR_K));
    }
    /** Genjutsu and sealing: their strength (a duration) shrinks with the target's will. */
    public static double willScale(double will) { return 1 - will / (will + WILL_K); }

    public static Result hit(Attack a, Defence d) {
        if (d.guard() == Guard.DODGE) return new Result(0, 0, 0, false, true);
        if (d.guard() == Guard.PARRY && (a.delivery() == Delivery.MELEE || a.delivery() == Delivery.THROWN))
            return new Result(0, 0, 0, false, true);
        var t = a.type();
        double dmg = a.raw();
        dmg *= switch (t.armour()) {
            case PHYSICAL -> 1 - armourReduction(d.physical(), t.armourPierce());
            case CHAKRA -> 1 - armourReduction(d.chakra(), 0);
            case WILL, NONE -> 1;
        };
        dmg *= t.nature().against(d.affinity());
        boolean blocked = d.guard() == Guard.BLOCK || d.guard() == Guard.PARRY;
        double stamina = 0;
        if (blocked) {
            double r = switch (a.delivery()) {
                case MELEE -> d.blockReduction();
                case THROWN -> BLOCK_THROWN;
                case JUTSU, AREA -> BLOCK_JUTSU;
            } * (1 - t.guardPierce());
            stamina = dmg * r * GUARD_STAMINA_PER_DAMAGE;
            dmg *= 1 - r;
        }
        dmg *= d.takenMult();
        if (d.player()) dmg /= Scaling.toughness(d.level());
        if (t.noHp()) return new Result(0, 0, stamina, blocked, false);
        if (t.drainsChakra()) return new Result(dmg * CHAKRA_HP_SHARE, dmg, stamina, blocked, false);
        return new Result(dmg, 0, stamina, blocked, false);
    }

    /** Poise damage of a hit: the move's poise times the type's poise multiplier, halved through a guard. */
    public static double poise(double movePoise, DamageType type, boolean blocked) { return movePoise * type.poiseMult() * (blocked ? 0.5 : 1); }

    private Damage() {}
}
