"""Core resources, scaling, natures, damage types, status effects, armour, difficulty and feel."""

from common import NATURES, SIGNS, TICKS_PER_SIGN

# --- Resources -------------------------------------------------------------------------------

RESOURCES = {
    "health": {
        "base_hp": 20, "hearts_every_levels": 6, "hp_per_heart": 2,
        "regen_per_second_out_of_combat": 0.25, "regen_delay_ticks": 100,
        "note": "Vanilla health: 10 hearts at level 1, +1 heart every 6 levels (level 60: 19 hearts). Clan and gear hearts stack on top."
    },
    "toughness": {
        "per_level": 0.025,
        "note": "Incoming damage to the player is divided by 1 + 0.025 x (level - 1): a level-50 body takes 45% of what a level-1 body takes from the same blow, so hearts stay readable while enemies scale."
    },
    "chakra": {
        "base": 50, "per_level": 3,
        "regen_flat_per_second": 0.6, "regen_fraction_per_second": 0.01,
        "combat_regen_mult": 0.75, "combat_window_ticks": 80,
        "meditate_mult": 4.0, "meditate_still_ticks": 20,
        "overdraw_limit": 0.25, "overdraw_hp_per_chakra": 0.5,
        "note": "A bar beside hunger. Regenerates slowly, faster meditating (sneak and stand still), from soldier pills and some food. Casting short of chakra (by at most 25% of the cost) is a desperate cast: the shortfall is paid in health at 0.5 HP per point and leaves you exhausted."
    },
    "control": {
        "base": 30, "max": 100,
        "cost_mult_at_0": 1.15, "cost_mult_at_100": 0.85,
        "sign_ticks_at_0": 4, "sign_ticks_at_80": 3,
        "movement_bonus_at_100": 0.25,
        "gains": {"leaf_concentration": 5, "tree_walking": 10, "water_walking": 10, "chakra_meditation_week": 2, "medical_training": 10},
        "note": "Chakra control, 0 to 100. Lowers chakra cost (x1.15 at 0, x0.85 at 100), speeds hand signs (4 ticks a sign, 3 from 80), stretches chakra movement and gates medical and precision techniques. Grows through training, not levels."
    },
    "stamina": {
        "base": 100, "regen_per_second": 30, "regen_delay_ticks": 15, "guarding_regen_mult": 0.3,
        "costs": {"light": 3, "heavy": 12, "launcher": 15, "air_hit": 4, "finisher": 10, "dodge": 22,
                  "dash": 10, "throw": 2, "sprint_per_second": 0, "guard_per_damage": 4, "parry": 0},
        "empty_effect": "winded",
        "note": "Taijutsu and weapons run on stamina, ninjutsu on chakra. Stamina refills in about three seconds, so a close-range fighter is limited by footwork and timing, never by a slow bar. A guard that runs out of stamina breaks (staggered for 20 ticks)."
    },
    "poise": {
        "player_base": 20, "regen_fraction_per_second": 0.15, "regen_delay_ticks": 40,
        "stagger_ticks": 16, "reset_to_full": True,
        "note": "Hidden toughness bar on every fighter. Every hit carries poise damage; at 0 the target staggers (16 ticks, interrupts any cast) and poise refills. Heavies, launchers, blunt weapons and earth hit poise hard; Strong Fist and Akimichi build it up."
    },
    "momentum": {
        "max": 100, "per_hit": 6, "per_parry": 25, "per_perfect_dodge": 15,
        "lost_when_hit": 30, "decay_per_second_after_ticks": [5, 40],
        "note": "Builds as you land hits and parries without being hit; taijutsu and weapon finishers spend it. Momentum is the close-range pillar's answer to a full chakra bar: big finishers that cost no chakra."
    },
    "exhaustion": {
        "chakra_exhaustion": {"trigger": "chakra reaches 0 or a desperate cast", "status": "chakra_exhausted",
                              "until_fraction": 0.2},
        "gate_exhaustion": {"trigger": "an inner gate closes", "status": "gate_strain"},
        "fatigue_link": "Shinobi Life's fatigue writes stat modifiers (movement, damage, chakra regen); Combat reads chakra regen and the movement and damage attributes."
    },
}

# --- Level and pillar scaling ----------------------------------------------------------------

SCALING = {
    "power_per_level": 0.03,
    "taijutsu_extra_per_level": 0.01,
    "enemy_hp_per_level": 0.055,
    "enemy_damage_per_level": 0.03,
    "pillars": {
        "taijutsu": {"rank_mult_per_rank": 0.07, "perk": "+5 stamina and +2 poise a rank; finishers at ranks 3, 6 and 9"},
        "weapons": {"rank_mult_per_rank": 0.07, "perk": "+1 tool pouch slot at ranks 4 and 8; throw recovery -0.5 ticks a rank"},
        "ninjutsu": {"rank_mult_per_rank": 0.07, "perk": "-2% chakra cost a rank; sign time -1 tick at ranks 5 and 10 (never below 2)"},
    },
    "pillar_ranks": {"min": 1, "max": 10, "cap_formula": "3 + floor(level / 2), at most 30",
                     "trials_at": [3, 6, 9],
                     "note": "Each pillar has a rank from 1 to 10, raised by use in real fights, drills at the training grounds and a mentor's trial at ranks 3, 6 and 9. The three ranks together cannot pass 3 + level/2, so mid-game you specialise and late-game you round out."},
    "fight_xp_falloff": "Repeated kills of the same enemy kind give less pillar XP, like level XP (ROADMAP Levels).",
    "note": "power(level) = 1 + 0.03 (level - 1), plus 0.01 (level - 1) more for taijutsu (ROADMAP Levels: +1% taijutsu a level). pillar(rank) = 1 + 0.07 (rank - 1)."
}

# --- Natures ---------------------------------------------------------------------------------

BEATS = {"fire": "wind", "wind": "lightning", "lightning": "earth", "earth": "water", "water": "fire"}
NATURE_RULES = {
    "beats": BEATS,
    "affinity_vs_weak": 1.25,
    "affinity_vs_strong": 0.8,
    "clash": {"stronger_passes_at": 0.5, "same_nature": "higher remaining power wins, at the difference",
              "neutral": "both dissipate; the larger keeps the difference"},
    "own_nature_cost_mult": 0.75,
    "clan_nature_power_bonus": 0.10,
    "colours": {"fire": "#ff7a2a", "wind": "#bfe9d6", "lightning": "#9fd8ff", "earth": "#a8814f", "water": "#4b9be0"},
    "note": "Fire beats wind, wind beats lightning, lightning beats earth, earth beats water, water beats fire. A defender with an affinity takes x1.25 from the nature that beats theirs and x0.8 from the nature theirs beats. When two jutsu collide, the stronger nature passes through at half power; equal natures compare power."
}

DAMAGE_TYPES = {
    "physical.blunt": {"armour": "physical", "poise_mult": 1.5, "note": "Fists, staffs, maces, boulders"},
    "physical.slash": {"armour": "physical", "poise_mult": 1.0, "bleed_chance": 0.1, "note": "Blades, wind blades count as wind"},
    "physical.pierce": {"armour": "physical", "armour_pierce": 0.3, "poise_mult": 0.6, "note": "Kunai, shuriken, senbon"},
    "ninjutsu.fire": {"armour": "chakra", "nature": "fire", "poise_mult": 0.8, "status": "burning"},
    "ninjutsu.wind": {"armour": "chakra", "nature": "wind", "poise_mult": 1.0, "guard_pierce": 0.3},
    "ninjutsu.lightning": {"armour": "chakra", "nature": "lightning", "poise_mult": 0.9, "status": "shocked"},
    "ninjutsu.earth": {"armour": "chakra", "nature": "earth", "poise_mult": 1.6},
    "ninjutsu.water": {"armour": "chakra", "nature": "water", "poise_mult": 1.2, "status": "soaked"},
    "ninjutsu.none": {"armour": "chakra", "poise_mult": 1.2, "note": "Pure chakra (spiralling spheres, chakra fists)"},
    "chakra": {"armour": "none", "drains": "chakra", "note": "Gentle Fist and insect drain: lowers the target's chakra and closes chakra points"},
    "genjutsu": {"armour": "will", "no_hp": True, "poise_mult": 0, "note": "Illusions: no health damage of their own; strength against the target's will"},
    "poison": {"armour": "none", "dot": True, "poise_mult": 0, "note": "Ticks over time; Suzuran are immune, Aburame resist"},
    "sealing": {"armour": "will", "no_hp": True, "poise_mult": 0, "note": "Seals chakra, techniques or movement; strength against will"},
    "true": {"armour": "none", "poise_mult": 0, "note": "Gate strain and desperate casts: never reduced"},
}

STATUS_EFFECTS = {
    "burning": {"dot": 0.5, "ticks": 60, "stacks": 1, "cleansed_by": ["soaked", "water"], "vanilla": "on fire (no block fire)"},
    "shocked": {"stun_ticks": 6, "then_slow": 0.2, "ticks": 30, "dr_group": "stun"},
    "soaked": {"ticks": 100, "lightning_taken_mult": 1.3, "fire_taken_mult": 0.7, "cleanses": ["burning"]},
    "chilled": {"slow": 0.25, "ticks": 60},
    "bleeding": {"dot": 0.3, "ticks": 80, "stacks": 3},
    "poisoned": {"dot": 0.4, "ticks": 120, "stacks": 5, "resisted_by": ["clan:suzuran", "clan:aburame"]},
    "numbed": {"slow": 0.15, "attack_speed": -0.15, "ticks": 100, "stacks": 3, "at_max": "paralysed"},
    "paralysed": {"stun_ticks": 40, "dr_group": "stun"},
    "drowsy": {"slow": 0.2, "ticks": 120, "stacks": 3, "at_max": "asleep"},
    "asleep": {"stun_ticks": 100, "breaks_on_damage": True, "dr_group": "stun"},
    "stunned": {"stun_ticks": 20, "dr_group": "stun"},
    "staggered": {"stun_ticks": 16, "interrupts": True},
    "knocked_down": {"stun_ticks": 24, "interrupts": True, "ground_hits_only": True},
    "airborne": {"ticks": 20, "juggle_gravity": 0.5},
    "bound": {"root": True, "no_cast": False, "dr_group": "bind", "note": "Roots, chains, webs, water prison: cannot move; can still weave unless the binding says otherwise"},
    "possessed": {"copies_caster": True, "stun_ticks": 100, "dr_group": "bind", "note": "Shadow Possession: copies the caster's movement"},
    "blinded": {"ticks": 60, "vision": "darkness effect", "ai": "loses target, swings at noise"},
    "smoked": {"ticks": 80, "ai": "loses target unless sensing", "player": "fog"},
    "silenced": {"no_signs": True, "ticks": 60, "dr_group": "seal"},
    "chakra_sealed": {"no_cast": True, "ticks": 80, "dr_group": "seal"},
    "points_closed": {"stacks": 64, "per_stack": {"chakra_regen": -0.015, "ninjutsu_power": -0.01}, "decay_ticks": 200,
                       "note": "Gentle Fist closes chakra points: each stack lowers chakra regen and ninjutsu power; 64 stacks seal chakra for 6 s"},
    "marked": {"ticks": 200, "visible_through_walls": True, "note": "Insects, ninken scent, sensing"},
    "genjutsu": {"slow": 0.4, "fake_entities": True, "breaks": ["release_sign", "damage_over_10_percent", "ally_touch"],
                 "note": "The shared genjutsu effect (see COMBAT.md)"},
    "fear": {"ai": "flees or hesitates", "ticks": 40, "dr_group": "mind"},
    "confused": {"ai": "attacks nearest", "ticks": 60, "dr_group": "mind"},
    "focus": {"next_attack_mult": 1.25, "ticks": 40, "note": "After a perfect dodge"},
    "counter_window": {"ticks": 12, "next_attack_mult": 1.5, "note": "After a parry"},
    "winded": {"ticks": 30, "no_dodge": True, "note": "Stamina emptied"},
    "chakra_exhausted": {"slow": 0.3, "stamina_regen_mult": 0.5, "no_cast_until_fraction": 0.2},
    "gate_strain": {"slow": 0.4, "damage_dealt_mult": 0.6, "ticks": 600},
    "hardened": {"physical_taken_mult": 0.5, "slow": 0.2, "note": "Earth armour"},
    "shrouded": {"lightning_armour": True, "move": 0.3, "attack_speed": 0.3, "chakra_per_second": 3},
    "expanded": {"scale": 2.0, "reach_mult": 1.6, "knockback_mult": 2.0, "poise_mult": 2.0, "slow": 0.1},
    "hidden": {"ai": "cannot see unless sensing or within 3 blocks", "breaks_on_attack": True},
    "silent_steps": {"noise_mult": 0.0},
    "well_fed": {"note": "Shinobi Life food buffs feed combat stats (ramen: chakra; barbecue: taijutsu +5%)"},
    "decoy": {"ticks": 100, "note": "Clone Technique: mobs may switch to an illusory copy"},
    "disguised": {"ticks": 1200, "breaks_on_damage": True, "ai": "mobs lose their target; residents do not recognize you"},
    "iframes": {"ticks": 6, "invulnerable": True},
    "sensing": {"ticks": 200, "note": "living things within the radius glow through walls; reveals hidden and disguised"},
    "unsensed": {"ticks": 300, "note": "sensing and Byakugan stage 1 cannot find you"},
    "read": {"ticks": 200, "note": "the target's chakra and next technique's nature shown"},
    "genjutsu_reflect": {"ticks": 40, "note": "the next genjutsu cast on you turns back on its caster"},
    "mind_immune": {"ticks": 300, "immune": ["genjutsu", "fear", "confused"]},
    "mind_link": {"ticks": 600, "note": "squad shares sensing; commands instant; cohesion counts 10 higher"},
    "mind_transferred": {"ticks": 160, "stun_ticks": 160, "note": "the caster's body slumps; damage to it ends the jutsu"},
    "nature_sealed": {"ticks": 400, "dr_group": "seal", "note": "nature jutsu sealed; taijutsu and genjutsu still work"},
    "broken_guard": {"ticks": 100, "no_guard": True},
    "guarding_ally": {"ticks": 300, "redirect": 0.5},
    "immovable": {"ticks": 200, "knockback_resist": 1.0, "stagger_immune": True},
    "light": {"ticks": 200, "move": 0.3, "double_jump": True},
    "heavy": {"ticks": 200, "slow": 0.5, "no_jump": True},
    "vitality_seal": {"ticks": 6000, "survive_lethal": True},
    "hundred_seal": {"ticks": 400, "heal_per_second": 2, "free_chakra": True},
    "scalpel_hands": {"ticks": 200, "on_hit": "numbed", "ignores_armour": True},
    "new_moon": {"ticks": 100, "next_hit": "no telegraph, S-rank damage"},
    "no_telegraph": {"ticks": 200, "note": "your blade attacks give no telegraph"},
    "poison_immune": {"ticks": 400, "immune": ["poisoned"]},
    "butterfly": {"ticks": 300, "damage_dealt_mult": 2.0, "move": 0.4, "then": "gate_strain"},
    "blade_flow.fire": {"ticks": 200, "on_hit": "burning"},
    "blade_flow.wind": {"ticks": 200, "reach": 1.5, "armour_pierce": 0.5},
    "blade_flow.lightning": {"ticks": 200, "on_hit": "shocked", "reach": 0.5},
    "blade_flow.earth": {"ticks": 200, "poise_mult": 2.0},
    "blade_flow.water": {"ticks": 200, "on_hit": "soaked", "knockback": 1},
    "kindled": {"note": "Pluggable kindle effect (see kindle.json); its powers are not designed yet"},
}

DIMINISHING_RETURNS = {
    "groups": ["stun", "bind", "seal", "mind"],
    "window_ticks": 300,
    "durations": [1.0, 0.5, 0.25, 0.0],
    "bosses": "bosses take 50% duration from the first and are immune after the second in a group, for 15 s",
    "note": "A second stun within 15 s lasts half as long, the third a quarter, the fourth not at all. The same rule runs for binds, seals and mind effects."
}

# --- Armour and resistances -------------------------------------------------------------------

ARMOUR = {
    "formula": "reduction = armour / (armour + 20), at most 0.6; pierce removes a share of armour first",
    "classes": {
        "physical": "Blades, fists, thrown tools",
        "chakra": "Ninjutsu of every nature; nature resistances stack on top",
        "will": "Genjutsu and sealing: strength x (1 - will / (will + 40))",
    },
    "gear": {
        "item:forehead_protector": {"physical": 1, "slot": "head"},
        "item:mesh_shirt": {"physical": 3, "slot": "chest", "slice": "beta2"},
        "item:arm_guards": {"physical": 2, "parry_window_ticks": 1, "slot": "arms", "slice": "beta2"},
        "item:shin_guards": {"physical": 2, "kick_poise": 2, "slot": "legs", "slice": "beta2"},
        "item:flak_vest": {"physical": 6, "chakra": 3, "pouch_slots": 2, "slot": "chest", "slice": "chunin"},
        "item:anbu_armor": {"physical": 8, "chakra": 4, "noise_mult": 0.8, "slot": "chest", "slice": "anbu"},
        "item:training_weights": {"speed_mult": 0.85, "taijutsu_xp_mult": 1.5, "release_burst": {"speed": 0.3, "ticks": 200}, "slot": "legs", "slice": "beta2"},
        "item:knuckle_wraps": {"light_damage": 0.5, "slot": "hands", "slice": "beta1"},
    },
    "will": {"base": 10, "per_level": 0.5, "clans": {"morino": 10, "yuhi": 8, "kurama": 8, "uchiha": 5, "yamanaka": 5}},
    "note": "Three armour classes. Gear gives physical armour; chakra armour comes from vests, earth armour and some clans; will (genjutsu and sealing) grows with level and clan."
}

# --- Hand signs ------------------------------------------------------------------------------

SIGN_INPUT = {
    "signs": SIGNS,
    "ticks_per_sign": TICKS_PER_SIGN,
    "weave_key": "key.shinobi.weave (R)",
    "modes": {
        "typed": {"keys": ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "-", "="]},
        "radial": {"slices": 12, "deadzone": 0.25, "controller": "right stick, flick to a sign, triggers confirm"},
    },
    "hold_or_toggle": "hold (default) or toggle: press Weave once to start, again to cast",
    "assist": {
        "prefix_hint": "While weaving, the HUD lists the techniques you know that start with the signs so far (ghost signs show the rest)",
        "auto_sign": "Accessibility: pick a known technique from the quick wheel and the signs play themselves at 6 ticks a sign. No fizzles, no mastery shortening",
        "sign_buffer": "Inputs up to 2 ticks early are buffered, so fast typists never drop a sign",
    },
    "fizzle": {"wrong_sequence_cost_fraction": 0.25, "interrupted_cost_fraction": 0.5},
    "interrupt": "A melee hit, a stagger or a knockdown interrupts weaving; a thrown or jutsu hit only if it deals 15% of max health or more. Story difficulty: only staggers, knockdowns and hits over 10% of max health interrupt the player",
    "quick_slots": {"keys": ["Z", "X", "C", "V"], "requires_mastery": "mastered"},
    "mastery": {
        "tiers": ["novice", "practiced", "mastered", "perfected"],
        "uses_by_rank": {"e": [10, 30, 80], "d": [12, 40, 100], "c": [15, 50, 130], "b": [20, 60, 160], "a": [25, 75, 200], "s": [30, 90, 240]},
        "combat_use_counts": 2,
        "home_drill": "one hand-sign drill a day at home (Shinobi Life) counts one training use for each of up to 3 techniques drilled; real fights count 2",
        "effects": {
            "practiced": {"cost_mult": 0.95, "power_mult": 1.03},
            "mastered": {"cost_mult": 0.9, "power_mult": 1.06, "signs": "half (rounded up)", "quick_slot": True},
            "perfected": {"cost_mult": 0.8, "power_mult": 1.1, "signs": "one sign (E to C: no signs)", "quick_slot": True},
        },
    },
}

# --- Difficulty ------------------------------------------------------------------------------

DIFFICULTY = {
    "modes": {
        "story": {"parry_window": 6, "perfect_dodge_window": 8, "telegraph_mult": 1.5, "telegraph_flash": True,
                  "enemy_damage": 0.6, "enemy_hp": 0.9, "enemy_dodge_mult": 0.7, "aim_assist_degrees": 5,
                  "death_levels": 1, "fatigue_start": "01:00", "cinematic": True, "habit_adaptation": 0.5,
                  "light_hits_interrupt_player": False, "boss_enrage": False, "attack_tokens": 1},
        "shinobi": {"parry_window": 4, "perfect_dodge_window": 6, "telegraph_mult": 1.0, "telegraph_flash": False,
                    "enemy_damage": 1.0, "enemy_hp": 1.0, "enemy_dodge_mult": 1.0, "aim_assist_degrees": 2,
                    "death_levels": 1, "fatigue_start": "00:00", "cinematic": True, "habit_adaptation": 1.0,
                    "light_hits_interrupt_player": True, "boss_enrage": True, "attack_tokens": 2},
        "hard": {"parry_window": 3, "perfect_dodge_window": 5, "telegraph_mult": 0.75, "telegraph_flash": False,
                 "enemy_damage": 1.3, "enemy_hp": 1.15, "enemy_dodge_mult": 1.25, "aim_assist_degrees": 0,
                 "death_levels": 2, "fatigue_start": "23:00", "cinematic": False, "habit_adaptation": 1.5,
                 "light_hits_interrupt_player": True, "boss_enrage": True, "attack_tokens": 3},
    },
    "default": "story",
    "changeable": "at any time, per world (difficulty.json overridable per world)",
    "toggles": {"auto_sign": False, "hold_guard": True, "hold_weave": True, "camera_shake": 1.0, "hit_stop": True,
                "flash_effects": True, "subtitle_tells": False, "auto_lock_on": False, "slow_combat": 1.0},
    "note": "Story is forgiving and cinematic (ROADMAP Decisions), Shinobi is the intended challenge, Hard is for players who parry everything. Every number is data."
}

FEEL = {
    "hit_stop_ticks": {"light": 1, "heavy": 3, "launcher": 3, "finisher": 5, "parry": 4, "counter": 4, "guard_break": 4, "jutsu_hit": 2, "boss_phase": 8},
    "hit_stop_note": "The client pauses both fighters' animation; the server freezes only the target's AI for those ticks, so it is safe on an integrated server and over a network",
    "camera_shake": {"light": 0.0, "heavy": 0.15, "finisher": 0.3, "earth_jutsu": 0.4, "explosion": 0.5, "boss_slam": 0.6, "max": 0.8, "falloff_blocks": 16},
    "telegraphs": {
        "wind_up_ticks": {"light": 4, "heavy": 10, "grab": 12, "jutsu_signs": "the signs themselves", "boss_signature": 20},
        "cues": ["wind-up pose", "a glint on blades (heavy)", "a red flash on unblockables (Story and Shinobi)", "a sound sting per telegraph class", "ground decals for area jutsu"],
        "unblockable_colour": "#ff3b30", "parryable_colour": "#ffd60a"
    },
    "iframes": {"dodge": 6, "perfect_dodge_bonus": 4, "substitution": 12, "finisher_cinematic": "whole cinematic", "get_up": 10, "story_bonus": 2},
    "targets": {
        "input_latency": "the first frame of a strike plays on the client the tick the key is pressed (client-predicted), the server confirms",
        "combo_window_ticks": [4, 10],
        "dodge_cooldown_ticks": 30,
        "ttk_mook_seconds": [4, 8], "ttk_elite_seconds": [10, 20], "ttk_boss_seconds": [60, 150],
        "player_survives_mook_hits": [6, 10],
        "fps": "60 fps with 12 fighters and 20 projectiles on a mid-range PC",
        "network": "playable at 100 ms ping: server-side sweeps with 2 ticks of lag compensation"
    },
    "cinematic_camera": {"on": ["finishers", "S and A rank jutsu", "boss phase changes", "squad combos"], "length_ticks": [20, 50],
                         "skippable": True, "difficulty_hard": "off"},
    "lock_on": {"key": "middle mouse", "range": 24, "soft_lock": "attacks curve 15 degrees toward the target in front"},
}

KINDLE = {
    "effect_type": "kindle",
    "status": "designed (the owner approved the redesign); unlock timing is the story's, bond tiers are the bond engine's",
    "concept": "Power flows outward, through people: it grows with how many people you have truly bonded with and how deep those bonds go",
    "contract": {
        "reads": "dev.shinobi.combat.Kindle.Bonds, adapted by Shinobi Life's glue: tier(who) = Kindling.combatTier(w, who); web() = Kindling.bonfire(w).strength(); bonfireOpen() = Kindling.bonfire(w).lit()",
        "tiers": {"spark": "friendship 6", "flame": "friendship 8", "blaze": "friendship 10 or a spouse", "bonfire": "a large bond web (the bond engine's gate)"},
        "quarrels": "an active quarrel drops exactly one tier (a Spark goes out); a falling-out puts it out; nothing before the story's awakening (the bond engine decides; combat reads the tier)",
    },
    "thread_sight": {
        "tier": "spark", "always_on": True,
        "combat": "bonded allies' health, chakra and cooldowns show along their threads; a telegraphed attack on a bonded ally flares on its thread 4 ticks earlier (6 at Flame, 8 at Blaze) so you can Cover or parry for them; any bonded ally is a beacon anywhere on the map",
        "blind_spot": "strangers and enemies have no thread to you: no reads on them",
        "outside_combat": "the bond engine's (who is tied to whom, fraying and one-sided ties, lies as a flicker)",
    },
    "kindle": {
        "tier": "spark", "key": "Kindle (K) while a bonded ally weaves: your chakra goes into their technique",
        "boost": {"spark": {"power": 1.4, "area": 1.2, "range": 1.5, "heal": 1.5, "revives": False},
                  "flame": {"power": 1.9, "area": 1.4, "range": 2.5, "heal": 2.0, "revives": True},
                  "blaze": {"power": 2.4, "area": 1.6, "range": 4.0, "heal": 2.5, "revives": True}},
        "cost": "your chakra: 0.6 / 0.8 / 1.0 of the ally's technique cost (Spark / Flame / Blaze)",
        "cooldown_ticks": {"spark": 400, "flame": 300, "blaze": 200},
        "examples": "a fireball becomes a firestorm, a heal becomes a revival, a sensor's range covers the village",
        "rule": "you never learn the technique: they do it, bigger",
    },
    "ember_link": {
        "tier": "flame", "members": "you and up to 3 bonded allies within 24 blocks", "ticks": 600, "cooldown_ticks": 2400,
        "shared_pool": "one chakra pool: a caster pays from their own share first, then evenly from the others",
        "damage": "a hit on a linked member: the one struck keeps half, the rest is split across the others (you feel your allies' pain)",
        "sight": "look through a linked ally's eyes (hold the Link key)",
    },
    "unison": {
        "tier": "blaze", "rule": "a combination unique to each pairing that neither can do alone: your nature crossed with the ally's niche (and their nature)",
        "cost": "25 chakra each, once per fight per pairing", "power": "two A-rank casts in one blow (42 base), 4-block burst",
        "by_niche": {
            "genjutsu": "Painted <your nature>: enemies caught in the ally's illusion take your nature's damage every second and cannot release it while it burns",
            "taijutsu": "Twin Comet: both dash through the target; your nature coats the strike (with a ninken: three fangs)",
            "ninjutsu": "a nature unison: the two natures' combo (combos/nature.json) at twice the power and range, or a pure-chakra lance when the natures match",
            "medical": "Hearth: the squad heals as one and a downed member rises",
            "sensing": "Beacon Sight: every enemy within 48 blocks marked, hidden ones revealed, for 30 s",
            "weapons": "Ember Rain: the ally's weapon storm carries your nature",
            "sealing": "Burning Seal: a barrier that burns what it holds",
        },
    },
    "ember_mark": {
        "tier": "blaze", "what": "leave an ember in a deeply bonded ally: travel to their side, or summon them to yours, across any distance",
        "combat": "once per fight: swap places with a marked ally (an escape or a rescue); outside a fight, travel to them (5-minute cooldown)",
    },
    "bonfire": {
        "tier": "bonfire", "ticks": 400, "burnout_ticks": 1200,
        "strength": "the bond engine's Bonfire strength (Kindling.bonfire(w).strength(): each flame by tier 1/2/4 times its strength, dimmed by quarrels, plus 0.5 per community reached)",
        "formula": "m = 1 + 1.5 x (1 - e^(-strength / 35)): your damage x m, damage taken x 1/sqrt(m), chakra regen x (1 + strength / 25), allies' power x (1 + (m - 1) / 2)",
        "scale": {"a loner (2 to 4)": "x1.1, a candle", "12": "x1.44, a campfire", "typical at 60 h (19)": "x1.63, a bonfire", "devoted (22)": "x1.70, an inferno"},
        "forms": "candle under 5, campfire under 12, bonfire under 21, inferno above (the bond engine's names; the visuals match)",
        "burnout": "afterwards no kindling of any kind for 60 s, and the chakra bar empties",
    },
    "costs": ["while linked you feel your allies' pain (the damage split)", "past three kindles in a minute each burns 10% of your chakra bar and 30 stamina",
              "a quarrel dims that person's flame, a falling-out snuffs it", "useless with strangers until you bond with them"],
    "natures": "you still gain natures through bonds by resonance: fight beside someone often enough and their trial can teach you their nature (the bond engine counts, a nature master's trial teaches); you never copy it",
    "look": "an ember mark on the palm or chest (never an eye), threads of light, ember-gold chakra",
    "beta": "none of it ships in the beta; the story decides when Spark opens",
}

KNACKS = {
    "owner": "the character creator picks one (Roots step); combat owns the effects",
    "list": [
        {"id": "combat:knack.balanced", "effect": {"taijutsu": 0.02, "weapons": 0.02, "ninjutsu": 0.02}, "starter": None, "default": True},
        {"id": "combat:knack.taijutsu", "effect": {"taijutsu": 0.05}, "starter": "item:knuckle_wraps"},
        {"id": "combat:knack.weapons", "effect": {"weapons": 0.05}, "starter": "item:practice_kunai x5 (fine)"},
        {"id": "combat:knack.ninjutsu", "effect": {"ninjutsu": 0.05}, "starter": "item:hand_sign_primer"},
    ],
    "affinity": "the creator's affinity (or undecided) is shown at the Genin ceremony as your leaning; choosing it there gives +10% power with that nature",
    "clanless_start": {"hearts": 10, "chakra": 53, "control": 35, "stamina": 110, "poise": 20},
}
