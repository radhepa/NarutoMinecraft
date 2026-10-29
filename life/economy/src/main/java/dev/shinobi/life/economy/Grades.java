package dev.shinobi.life.economy;

import java.util.List;

import static dev.shinobi.life.economy.Json.integer;
import static dev.shinobi.life.economy.Json.list;
import static dev.shinobi.life.economy.Json.num;
import static dev.shinobi.life.economy.Json.obj;

/**
 * Quality grades of crafted things (ITEMS.md, Crafting): standard (all shop stock), fine and masterwork. A craft
 * rolls its grade from the crafter's mastery at that station family (crafts done there), the recipe's difficulty,
 * whether refined materials went in, and the station's cap (the small forge at home stops at fine). Difficulty 0
 * recipes (furniture, plain dishes) always come out standard. Durability and price follow the grade; damage is
 * the combat session's (it reads the grade).
 */
public final class Grades {
    public static final List<String> LEVELS = List.of("standard", "fine", "masterwork");
    private final Catalogue catalogue;

    public Grades(Catalogue catalogue) { this.catalogue = catalogue; }

    /** Mastery level 0 to 5 from crafts done at a station family. */
    public int mastery(int crafts) {
        var steps = list(catalogue.tuning("grades").get("mastery_crafts"));
        int level = 0;
        for (int i = 0; i < steps.size(); i++) if (crafts >= integer(steps.get(i), 0)) level = i;
        return level;
    }

    public double fineChance(int crafts, int difficulty, boolean refined) {
        if (difficulty <= 0) return 0;
        var f = obj(catalogue.tuning("grades").get("fine_chance"));
        return Math.clamp(num(f.get("base"), 0) + num(f.get("per_mastery"), 0) * mastery(crafts)
                - num(f.get("difficulty_penalty"), 0) * difficulty + (refined ? num(f.get("refined_bonus"), 0) : 0), 0, 0.9);
    }
    public double masterworkChance(int crafts, int difficulty, boolean refined) {
        var m = obj(catalogue.tuning("grades").get("masterwork_chance"));
        int over = mastery(crafts) - (int) num(m.get("min_mastery"), 3);
        if (difficulty <= 0 || over < 0) return 0;
        return Math.min(num(m.get("max"), .25), num(m.get("base"), 0) + num(m.get("per_mastery_over"), 0) * (over + 1)
                + (refined ? num(m.get("refined_bonus"), 0) : 0));
    }

    /**
     * The grade of one craft, rolled from the {@code crafts} stream keyed by player, station and craft count, so a
     * reload never rerolls it. {@code stationMax} is the station's max_grade.
     */
    public String roll(long seed, String player, String station, int crafts, int difficulty, boolean refined, String stationMax) {
        double r = Streams.roll(seed, "crafts", player, station, Integer.toString(crafts));
        String grade = "standard";
        double mw = masterworkChance(crafts, difficulty, refined), fine = fineChance(crafts, difficulty, refined);
        if (r < mw) grade = "masterwork";
        else if (r < mw + fine) grade = "fine";
        return cap(grade, stationMax);
    }
    public static String cap(String grade, String max) {
        return LEVELS.indexOf(grade) > LEVELS.indexOf(max) ? max : grade;
    }
    public double durability(String grade) { return num(obj(catalogue.tuning("grades").get("durability")).get(grade), 1); }

    /** What the weapon shop charges to repair: base x missing share x factor, rounded up (masterwork costs more). */
    public int repairCost(String item, String grade, double missing) {
        var r = catalogue.tuning("repair");
        double cost = catalogue.item(item).price() * Math.clamp(missing, 0, 1) * num(r.get("factor"), .3);
        if (grade.equals("masterwork")) cost *= num(r.get("masterwork_factor"), 1.5);
        return (int) Math.ceil(cost);
    }
}
