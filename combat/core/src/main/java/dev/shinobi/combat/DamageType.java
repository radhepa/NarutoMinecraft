package dev.shinobi.combat;

import java.util.Map;

/**
 * A damage type (data/combat/core/damage_types.json): which armour class stops it, its nature, how hard it hits
 * poise, how much armour or guard it ignores, and whether it touches health at all.
 */
public record DamageType(String id, Armour armour, Nature nature, double poiseMult, double armourPierce, double guardPierce,
                         boolean noHp, boolean drainsChakra) {
    public enum Armour { PHYSICAL, CHAKRA, WILL, NONE }

    public boolean physical() { return armour == Armour.PHYSICAL; }
    public boolean ninjutsu() { return id.startsWith("ninjutsu."); }

    public static DamageType of(String id) {
        var t = BUILT_IN.get(id);
        if (t == null) throw new IllegalArgumentException("unknown damage type " + id);
        return t;
    }

    /** The shipped table; {@link CombatData} checks it matches the data file. */
    public static final Map<String, DamageType> BUILT_IN = Map.ofEntries(
            e("physical.blunt", Armour.PHYSICAL, Nature.NONE, 1.5, 0, 0),
            e("physical.slash", Armour.PHYSICAL, Nature.NONE, 1.0, 0, 0),
            e("physical.pierce", Armour.PHYSICAL, Nature.NONE, 0.6, 0.3, 0),
            e("ninjutsu.fire", Armour.CHAKRA, Nature.FIRE, 0.8, 0, 0),
            e("ninjutsu.wind", Armour.CHAKRA, Nature.WIND, 1.0, 0, 0.3),
            e("ninjutsu.lightning", Armour.CHAKRA, Nature.LIGHTNING, 0.9, 0, 0),
            e("ninjutsu.earth", Armour.CHAKRA, Nature.EARTH, 1.6, 0, 0),
            e("ninjutsu.water", Armour.CHAKRA, Nature.WATER, 1.2, 0, 0),
            e("ninjutsu.none", Armour.CHAKRA, Nature.NONE, 1.2, 0, 0),
            Map.entry("chakra", new DamageType("chakra", Armour.NONE, Nature.NONE, 1.0, 0, 0, false, true)),
            Map.entry("genjutsu", new DamageType("genjutsu", Armour.WILL, Nature.NONE, 0, 0, 1, true, false)),
            e("poison", Armour.NONE, Nature.NONE, 0, 0, 1),
            Map.entry("sealing", new DamageType("sealing", Armour.WILL, Nature.NONE, 0, 0, 1, true, false)),
            e("true", Armour.NONE, Nature.NONE, 0, 0, 1));

    private static Map.Entry<String, DamageType> e(String id, Armour a, Nature n, double poise, double pierce, double guard) {
        return Map.entry(id, new DamageType(id, a, n, poise, pierce, guard, false, false));
    }
}
