package dev.shinobi.combat;

import java.util.Map;

/**
 * A difficulty mode (data/combat/core/difficulty.json): Story is forgiving and cinematic (the default), Shinobi the
 * intended challenge, Hard for players who parry everything. It can change at any time.
 */
public record Difficulty(String id, int parryWindow, int perfectDodgeWindow, double telegraphMult, double enemyDamage, double enemyHp,
                         double enemyDodgeMult, double aimAssist, int deathLevels, double habitAdaptation, boolean lightHitsInterruptPlayer,
                         int attackTokens) {
    public static Difficulty of(String id, Map<String, Object> m) {
        return new Difficulty(id, Json.integer(m, "parry_window", 4), Json.integer(m, "perfect_dodge_window", 6), Json.num(m, "telegraph_mult", 1),
                Json.num(m, "enemy_damage", 1), Json.num(m, "enemy_hp", 1), Json.num(m, "enemy_dodge_mult", 1),
                Json.num(m, "aim_assist_degrees", 0), Json.integer(m, "death_levels", 1), Json.num(m, "habit_adaptation", 1),
                Json.bool(m, "light_hits_interrupt_player"), Json.integer(m, "attack_tokens", 2));
    }
    public static final Difficulty STORY = new Difficulty("story", 6, 8, 1.5, 0.6, 0.9, 0.7, 5, 1, 0.5, false, 1);
    public static final Difficulty SHINOBI = new Difficulty("shinobi", 4, 6, 1.0, 1.0, 1.0, 1.0, 2, 1, 1.0, true, 2);
    public static final Difficulty HARD = new Difficulty("hard", 3, 5, 0.75, 1.3, 1.15, 1.25, 0, 2, 1.5, true, 3);
}
