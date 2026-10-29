package dev.shinobi.combat.sim;

import dev.shinobi.combat.CombatData;
import dev.shinobi.combat.Difficulty;

/** One traced fight for tuning: {@code Trace <build id> <boss id|enemy id> [level] [story|shinobi|hard] [seed]}. */
public final class Trace {
    public static void main(String[] args) {
        var data = CombatData.load();
        var diff = data.difficulties.get(args.length > 3 ? args[3] : "shinobi");
        long seed = args.length > 4 ? Long.parseLong(args[4]) : 1;
        var battle = new Battle(data, diff, seed);
        battle.trace = true;
        battle.add(Fighter.player(data, data.builds.get(args[0]), Fighter.Skill.AVERAGE, 0), 0);
        if (data.bosses.containsKey(args[1])) {
            var b = data.bosses.get(args[1]);
            for (int k = 0; k < Balance.allies(b); k++)
                battle.add(Fighter.enemy(data, data.enemies.get("combat:enemy.spar.genin"), Balance.buildLevel(b.level()), diff, 0, null, true), -1 - k);
            battle.boss(b, battle.add(Fighter.enemy(data, data.enemies.get(b.base()), b.level(), diff, 1, b, false), 9));
        } else battle.add(Fighter.enemy(data, data.enemies.get(args[1]), Integer.parseInt(args[2]), diff, 1, null, false), 8);
        var r = battle.run();
        System.out.println("winner " + r.winner() + " after " + r.ticks() / 20.0 + "s, player hp " + r.playerHp());
    }
}
