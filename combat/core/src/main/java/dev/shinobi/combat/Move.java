package dev.shinobi.combat;

import java.util.List;
import java.util.Map;

/**
 * One move of a style's combo tree (data/combat/styles/*.json), reached by an input path from the root: L light,
 * H heavy, D after a dodge, P after a parry, J in the air, X a dash, G while guarding, T a throw. Frames are ticks:
 * startup, active, recovery; the next input is taken from {@code windowOpen} to {@code windowClose} ticks after
 * the active frames end. A window of (0, 0) ends the string.
 */
public record Move(String id, List<String> input, String state, double damage, double poise, int startup, int active, int recovery,
                   int windowOpen, int windowClose, double stamina, String type, int tier, double momentumCost, Map<String, Object> effects) {

    public static Move of(Map<String, Object> m) {
        var f = Json.list(m, "frames");
        var w = Json.list(m, "window");
        return new Move(Json.str(m, "id", "?"), Json.strings(m, "input"), Json.str(m, "state", "ground"),
                Json.num(m, "damage", 0), Json.num(m, "poise", 0),
                ((Number) f.get(0)).intValue(), ((Number) f.get(1)).intValue(), ((Number) f.get(2)).intValue(),
                ((Number) w.get(0)).intValue(), ((Number) w.get(1)).intValue(),
                Json.num(m, "stamina", 3), Json.str(m, "type", "physical.blunt"), Json.integer(m, "tier", 1),
                Json.num(m, "momentum_cost", 0), Json.obj(m, "effects"));
    }

    public String path() { return String.join(" ", input); }
    public boolean ender() { return windowOpen == 0 && windowClose == 0; }
    public boolean finisher() { return Json.bool(effects, "finisher"); }
    public int length() { return startup + active + recovery; }
    public int hitTick() { return startup; }
    public int hits() { return Json.integer(effects, "hits", 1); }
    public boolean weaponMult() { return Json.bool(effects, "weapon_mult"); }
    public int requiresGate() { return Json.integer(effects, "requires_gate", 0); }
    public double chakra() { return Json.num(effects, "chakra", 0); }
    public boolean launches() { return Json.bool(effects, "launches"); }
    public boolean knocksDown() { return Json.bool(effects, "knocks_down"); }
    public boolean guardBreak() { return Json.bool(effects, "guard_break") || Json.num(effects, "guard_damage_mult", 1) >= 2; }
    public double area() { return Json.num(effects, "area_blocks", 0); }
    public double dash() { return Math.max(Json.num(effects, "dash_blocks", 0), Json.num(effects, "charge_blocks", 0)); }
    public double range() { return Json.num(effects, "range_blocks", 0); }
}
