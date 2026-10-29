"""Taijutsu styles: combo trees, guard and counters, finishers, the inner gates.

A move is reached by an input path from the style's root. Inputs: L (light, a tap), H (heavy, a hold
of 8 ticks), D (dodge), P (a parry that landed), J (jump or airborne), X (dash: D then attack).
`frames` is [startup, active, recovery] in ticks; `window` is when the next input may be pressed,
counted from the end of `active` (inputs pressed earlier are buffered for 2 ticks). Damage is base
damage before level, pillar, style and gear scaling. `tier` is the style tier that opens the move.
"""


def mv(mid, inp, dmg, poise, frames, window=(0, 8), stamina=3, state="ground", tier=1, kind="physical.blunt",
       momentum=0, slice_=None, **fx):
    m = {"id": mid, "input": inp.split(), "state": state, "damage": dmg, "poise": poise,
         "frames": list(frames), "window": list(window), "stamina": stamina, "type": kind, "tier": tier}
    if momentum:
        m["momentum_cost"] = momentum
    if slice_:
        m["slice"] = slice_
    if fx:
        m["effects"] = fx
    return m


TIERS = {
    "names": ["initiate", "adept", "expert", "master", "grandmaster"],
    "style_mult": [1.0, 1.05, 1.1, 1.15, 1.2],
    "how": "A style's tier rises with uses of its moves in real fights and a mentor's trial at tiers 2 to 5; tiers need taijutsu (or weapons) rank 1, 3, 5, 7 and 9",
}

ACADEMY = [
    mv("jab", "L", 2.0, 3, (2, 2, 5), slice_="beta1"),
    mv("cross", "L L", 2.0, 3, (2, 2, 5), slice_="beta1"),
    mv("roundhouse", "L L L", 2.6, 8, (3, 2, 10), window=(0, 0), slice_="beta1", knockback=1.5),
    mv("heavy", "H", 5.0, 14, (8, 3, 10), stamina=12, window=(0, 0), slice_="beta1", guard_damage_mult=2.0),
    mv("flying_kick", "X H", 4.0, 12, (4, 3, 12), stamina=12, window=(0, 0), slice_="beta1", dash_blocks=4, knockback=2.0),
    mv("lunge", "X L", 2.4, 4, (3, 2, 6), stamina=5, slice_="beta1", dash_blocks=4),
    mv("counter", "P L", 3.0, 10, (1, 2, 6), slice_="beta2", counter=True),
    mv("sweep", "L H", 3.0, 10, (5, 3, 10), stamina=12, window=(0, 4), slice_="beta2", knocks_down=True),
    mv("launcher", "L L H", 3.0, 12, (5, 3, 6), stamina=15, window=(0, 10), slice_="beta2", launches=True),
    mv("air_1", "J L", 1.6, 3, (2, 2, 4), state="air", stamina=4, slice_="beta2"),
    mv("air_2", "J L L", 1.6, 3, (2, 2, 4), state="air", stamina=4, slice_="beta2"),
    mv("air_3", "J L L L", 2.0, 4, (2, 2, 6), state="air", stamina=4, slice_="beta2"),
    mv("air_spike", "J L L H", 3.5, 14, (4, 3, 10), state="air", stamina=10, window=(0, 0), slice_="beta2", knocks_down=True),
    mv("palm_rush", "L L L H", 8.0, 30, (6, 12, 12), stamina=10, momentum=60, tier=2, window=(0, 0), slice_="beta2",
       finisher=True, hits=5, cinematic=False),
]

STYLES = [
    {
        "id": "combat:style.academy_basics", "name": "Academy taijutsu", "pillar": "taijutsu",
        "who": "everyone", "mentor": "role:instructor", "slice": "beta1",
        "feel": "Clean, balanced forms: the three-hit chain, a heavy, dodge and block. The base every style builds on.",
        "passives": {}, "moves": ACADEMY,
    },
    {
        "id": "combat:style.strong_fist", "name": "Strong Fist", "pillar": "taijutsu",
        "who": "anyone; the master's trial asks for taijutsu rank 3 and a week of weighted training",
        "mentor": "role:strong_fist_master", "slice": "beta2",
        "feel": "Hard, fast, relentless. Heavies keep poise while winding up, kicks dominate, and the gates open its last forms.",
        "passives": {"heavy_hyper_armour": True, "poise_damage_mult": 1.3, "training_weights": "weights raise taijutsu XP x1.5; releasing them gives +30% speed for 10 s"},
        "moves": [
            mv("leaf_hurricane", "L L L", 3.4, 12, (3, 4, 10), window=(0, 0), tier=1, slice_="beta2", area_blocks=2.5, knockback=2.0),
            mv("leaf_rising_wind", "L L H", 3.6, 16, (4, 3, 6), stamina=15, window=(0, 12), tier=1, slice_="beta2", launches=True),
            mv("leaf_whirlwind", "X H", 5.0, 16, (4, 4, 10), stamina=12, window=(0, 0), tier=2, slice_="beta2", knockback=2.5),
            mv("leaf_great_whirlwind", "L L L H", 10.0, 40, (5, 10, 14), stamina=10, momentum=60, tier=2, window=(0, 0),
               slice_="beta3", finisher=True, area_blocks=3.0),
            mv("primary_lotus", "J L L H", 14.0, 60, (6, 14, 20), state="air", stamina=20, momentum=100, tier=3,
               window=(0, 0), slice_="chunin", finisher=True, requires_gate=1, cinematic=True, knocks_down=True),
            mv("reverse_lotus", "J L L L H", 22.0, 80, (6, 20, 24), state="air", stamina=25, momentum=100, tier=4,
               window=(0, 0), slice_="jonin", finisher=True, requires_gate=3, cinematic=True),
            mv("morning_peacock", "L L L H", 34.0, 100, (8, 24, 30), stamina=30, momentum=100, tier=5, window=(0, 0),
               slice_="road", finisher=True, requires_gate=6, cinematic=True, kind="ninjutsu.fire", note="Punches so fast the air ignites"),
        ],
    },
    {
        "id": "combat:style.gentle_fist", "name": "Gentle Fist", "pillar": "taijutsu",
        "who": "Hyuga only (needs the Byakugan)", "clan": "hyuga", "mentor": "role:clan_elder.hyuga", "slice": "beta2",
        "feel": "Palms that ignore armour and close chakra points. Weaker on health, deadly to casters; the Rotation is the best defence in the game.",
        "passives": {"palm_type": "chakra", "palm_hp_share": 0.5, "closes_points_per_hit": 1, "ignores_physical_armour": True,
                     "byakugan_crit": "with Byakugan stage 2, palms crit (x1.5) a target's back"},
        "moves": [
            mv("palm_1", "L", 1.6, 3, (2, 2, 4), kind="chakra", tier=1, slice_="beta2"),
            mv("palm_2", "L L", 1.6, 3, (2, 2, 4), kind="chakra", tier=1, slice_="beta2"),
            mv("palm_3", "L L L", 1.6, 3, (2, 2, 4), kind="chakra", tier=1, slice_="beta2"),
            mv("palm_4", "L L L L", 2.4, 8, (3, 2, 10), kind="chakra", window=(0, 0), tier=1, slice_="beta2", knockback=1.5, closes_points=3),
            mv("palm_thrust", "H", 4.0, 10, (8, 3, 10), stamina=12, kind="chakra", window=(0, 0), tier=1, slice_="beta2", closes_points=4),
            mv("vacuum_palm", "X H", 4.5, 14, (6, 3, 12), stamina=12, kind="ninjutsu.none", window=(0, 0), tier=2, slice_="chunin",
               range_blocks=6, chakra=6),
            mv("palm_rotation", "G H", 4.0, 20, (2, 12, 10), stamina=0, kind="chakra", window=(0, 0), tier=2, slice_="chunin",
               chakra=15, iframes=10, deflects_projectiles=True, area_blocks=3.0, knockback=3.0, cooldown=120),
            mv("sixty_four_palms", "L L L H", 12.0, 50, (6, 30, 16), stamina=10, momentum=100, kind="chakra", tier=3, window=(0, 0),
               slice_="chunin", finisher=True, closes_points=64, cinematic=True),
            mv("hundred_twenty_eight_palms", "L L L L H", 20.0, 80, (6, 40, 20), stamina=10, momentum=100, kind="chakra", tier=4,
               window=(0, 0), slice_="jonin", finisher=True, closes_points=128, cinematic=True),
            mv("twin_lion_fists", "G L L H", 30.0, 100, (10, 20, 24), stamina=20, momentum=100, kind="chakra", tier=5, window=(0, 0),
               slice_="road", finisher=True, chakra=40, drains_chakra=40, cinematic=True),
        ],
    },
    {
        "id": "combat:style.swaying_willow", "name": "Swaying Willow", "pillar": "taijutsu",
        "who": "anyone; a wandering master's side line (Chunin)", "mentor": "role:willow_master", "slice": "chunin",
        "feel": "The flowing, drunken-looking style: every dodge is an attack, every miss a lean, and nobody can read the rhythm.",
        "passives": {"dodge_iframes_bonus": 3, "dodge_cost_mult": 0.7, "perfect_dodge_counters": True, "telegraph_mult_against_you": 0.8,
                     "random_extra_hit_chance": 0.15},
        "moves": [
            mv("sway_strike", "D L", 2.6, 4, (2, 2, 5), stamina=4, tier=1, slice_="chunin"),
            mv("sway_strike_2", "D L L", 2.6, 4, (2, 2, 5), stamina=4, tier=1, slice_="chunin"),
            mv("falling_willow", "D L L H", 6.0, 18, (5, 4, 10), stamina=12, window=(0, 0), tier=1, slice_="chunin", knocks_down=True),
            mv("lean_back_kick", "D H", 4.5, 12, (4, 3, 10), stamina=12, window=(0, 0), tier=2, slice_="chunin", counter=True),
            mv("willow_storm", "D L L L H", 15.0, 50, (4, 20, 14), stamina=10, momentum=80, tier=3, window=(0, 0), slice_="jonin",
               finisher=True, hits=8, cinematic=True),
        ],
    },
    {
        "id": "combat:style.iron_body", "name": "Iron Body", "pillar": "taijutsu",
        "who": "Akimichi only", "clan": "akimichi", "mentor": "role:clan_elder.akimichi", "slice": "beta2",
        "feel": "Weight as a weapon. Slow, unstoppable, huge poise damage; expansion turns every move into a landslide.",
        "passives": {"poise_bonus": 20, "knockback_resist": 0.7, "expansion_synergy": "moves gain reach x1.6 while expanded"},
        "moves": [
            mv("body_slam", "L L L", 3.6, 16, (4, 3, 12), window=(0, 0), tier=1, slice_="beta2", knockback=2.5),
            mv("crushing_palm", "H", 7.0, 24, (10, 3, 12), stamina=14, window=(0, 0), tier=1, slice_="beta2", guard_damage_mult=3.0),
            mv("human_boulder", "X H", 6.0, 30, (6, 30, 14), stamina=20, window=(0, 0), tier=1, slice_="beta2", chakra=10,
               charge_blocks=12, note="A rolling charge; needs Expansion"),
            mv("partial_expansion_slap", "L L H", 8.0, 30, (8, 4, 12), stamina=15, window=(0, 0), tier=2, slice_="chunin", chakra=10,
               area_blocks=4.0),
            mv("meat_tank", "X L L H", 18.0, 70, (6, 40, 18), stamina=20, momentum=80, tier=3, window=(0, 0), slice_="jonin",
               finisher=True, chakra=20, cinematic=True),
        ],
    },
    {
        "id": "combat:style.beast_fang", "name": "Beast Fang (Four Legs)", "pillar": "taijutsu",
        "who": "Inuzuka only", "clan": "inuzuka", "mentor": "role:clan_elder.inuzuka", "slice": "beta2",
        "feel": "On all fours with your ninken: fast claws, pounces and paired attacks.",
        "passives": {"move_speed": 0.1, "claw_type": "physical.slash", "ninken_follow_up": "every 3rd hit, your ninken bites (2.0)"},
        "moves": [
            mv("claw_1", "L", 1.8, 3, (2, 2, 4), kind="physical.slash", tier=1, slice_="beta2"),
            mv("claw_2", "L L", 1.8, 3, (2, 2, 4), kind="physical.slash", tier=1, slice_="beta2"),
            mv("claw_3", "L L L", 1.8, 3, (2, 2, 4), kind="physical.slash", tier=1, slice_="beta2"),
            mv("claw_4", "L L L L", 2.6, 8, (2, 2, 10), kind="physical.slash", window=(0, 0), tier=1, slice_="beta2"),
            mv("pounce", "X L", 3.0, 8, (3, 3, 6), stamina=6, kind="physical.slash", tier=1, slice_="beta2", dash_blocks=6, knocks_down=True),
            mv("passing_fang", "X H", 5.0, 14, (4, 6, 10), stamina=12, kind="physical.slash", window=(0, 0), tier=2, slice_="chunin",
               dash_blocks=8, chakra=6),
        ],
    },
    {
        "id": "combat:style.iron_guard", "name": "Iron Guard", "pillar": "taijutsu",
        "who": "anyone; the gate guards teach it at clan friendship 5 with the Hagane", "clan_lesser": "hagane",
        "mentor": "role:clan_elder.hagane", "slice": "beta2",
        "feel": "A defensive style: hold the line, punish every blow you block, never move back.",
        "passives": {"guard_reduction": 0.75, "guard_stamina_mult": 0.7, "block_counter": "a hit blocked while holding guard charges a counter (G L)"},
        "moves": [
            mv("guard_shove", "G L", 2.5, 14, (2, 2, 8), stamina=6, window=(0, 6), tier=1, slice_="beta2", knockback=2.0, counter=True),
            mv("guard_crush", "G L H", 5.5, 24, (6, 3, 12), stamina=12, window=(0, 0), tier=1, slice_="beta2", guard_damage_mult=2.5),
            mv("iron_wall", "G H", 0.0, 0, (2, 40, 6), stamina=0, window=(0, 0), tier=2, slice_="chunin", chakra=10,
               immovable=True, reflect_melee=0.5),
        ],
    },
    {
        "id": "combat:style.blossom_strength", "name": "Blossom Strength", "pillar": "taijutsu",
        "who": "chakra control 70: the Haruno at Chunin, anyone else at Jonin with control 80",
        "clan": "haruno", "mentor": "role:medic", "slice": "chunin",
        "feel": "Perfectly timed chakra in a fist: slow heavies that crater the ground (never the map) and break any guard.",
        "passives": {"heavy_chakra": 5, "heavy_mult": 2.5, "heavy_guard_break": True, "control_required": 70},
        "moves": [
            mv("blossom_punch", "H", 12.5, 40, (10, 3, 12), stamina=12, window=(0, 0), tier=1, slice_="chunin", chakra=5,
               area_blocks=2.0, guard_break=True),
            mv("blossom_heel", "J H", 14.0, 50, (8, 3, 16), stamina=15, state="air", window=(0, 0), tier=2, slice_="chunin",
               chakra=8, area_blocks=4.0, knocks_down=True),
            mv("cherry_blossom_impact", "L L L H", 24.0, 90, (10, 4, 20), stamina=15, momentum=80, tier=3, window=(0, 0),
               slice_="jonin", finisher=True, chakra=15, area_blocks=5.0, cinematic=True),
        ],
    },
    {
        "id": "combat:style.lightning_body", "name": "Lightning Body", "pillar": "taijutsu",
        "who": "lightning nature, taijutsu rank 7 (Jonin)", "nature": "lightning", "mentor": "role:nature_master.lightning",
        "slice": "jonin",
        "feel": "Wrap the body in lightning armour and hit like a storm. Drains chakra every second it burns.",
        "passives": {"needs_status": "shrouded", "shroud_technique": "combat:lightning.armour"},
        "moves": [
            mv("lariat", "X H", 14.0, 50, (4, 4, 12), stamina=12, kind="ninjutsu.lightning", window=(0, 0), tier=1, slice_="jonin",
               dash_blocks=10),
            mv("guillotine_drop", "J H", 16.0, 60, (6, 4, 14), stamina=15, state="air", kind="ninjutsu.lightning", window=(0, 0),
               tier=2, slice_="jonin", knocks_down=True),
            mv("liger_bomb", "J L L H", 26.0, 100, (6, 16, 20), stamina=20, momentum=100, state="air", kind="ninjutsu.lightning",
               tier=3, window=(0, 0), slice_="road", finisher=True, cinematic=True),
        ],
    },
]

# Inner gates: Strong Fist's last forms, opened from Chunin. Each gate drains health while open and
# leaves gate strain when it closes. Gate 8 is never playable.
GATES = {
    "who": "Strong Fist tier 3 and taijutsu rank 5 for the first gate; each further gate one more taijutsu rank",
    "key": "hold Style (B) and press Weave: opens the next gate you know; again closes them",
    "gates": [
        {"n": 1, "name": "Opening", "slice": "chunin", "damage": 0.2, "speed": 0.1, "hp_drain_per_second": 0.2, "max_ticks": 400, "strain_ticks": 200},
        {"n": 2, "name": "Healing", "slice": "chunin", "damage": 0.3, "speed": 0.15, "heal_on_open": 0.1, "hp_drain_per_second": 0.3, "max_ticks": 400, "strain_ticks": 240},
        {"n": 3, "name": "Life", "slice": "jonin", "damage": 0.45, "speed": 0.25, "hp_drain_per_second": 0.5, "max_ticks": 360, "strain_ticks": 300, "look": "skin flushes red"},
        {"n": 4, "name": "Pain", "slice": "jonin", "damage": 0.6, "speed": 0.3, "hp_drain_per_second": 0.7, "max_ticks": 300, "strain_ticks": 360},
        {"n": 5, "name": "Limit", "slice": "road", "damage": 0.75, "speed": 0.35, "hp_drain_per_second": 0.9, "max_ticks": 260, "strain_ticks": 420},
        {"n": 6, "name": "View", "slice": "road", "damage": 0.9, "speed": 0.4, "hp_drain_per_second": 1.2, "max_ticks": 220, "strain_ticks": 600, "look": "a blue-green aura"},
        {"n": 7, "name": "Wonder", "slice": "post", "damage": 1.1, "speed": 0.5, "hp_drain_per_second": 1.6, "max_ticks": 160, "strain_ticks": 1200, "note": "post-game only"},
        {"n": 8, "name": "Death", "slice": "never", "note": "Not playable."},
    ],
}

GUARD = {
    "block": {"input": "right click (hold) with an empty hand or a melee weapon", "melee_reduction": 0.6, "thrown_reduction": 0.8,
              "ninjutsu_reduction": 0.3, "genjutsu_reduction": 0.0, "move_speed": 0.5, "slice": "beta1",
              "breaks": "stamina at 0: staggered for 20 ticks; heavies and guard-break moves drain extra stamina"},
    "parry": {"input": "start a block inside the parry window before a melee hit lands (Story 6 ticks, Shinobi 4, Hard 3)",
              "effect": "no damage, attacker staggered 20 ticks, +25 momentum, a 12-tick counter window (x1.5)", "slice": "beta2",
              "thrown": "parrying a thrown kunai or shuriken knocks it down (weapons rank 3: catches a kunai)",
              "not_parryable": ["ninjutsu (except palm rotation and some counters)", "grabs", "unblockable red-flash moves"]},
    "dodge": {"input": "double-tap a direction or Left Alt", "blocks": 4, "iframes": 6, "cooldown_ticks": 30, "stamina": 22,
              "chakra": 0, "perfect": "dodging inside the perfect window grants focus (+25% next attack) and +15 momentum", "slice": "beta1"},
    "substitution": {"input": "dodge as a hit lands with 10 chakra", "blink_blocks": 5, "iframes": 12, "cooldown_ticks": 400,
                     "leaves": "a log entity", "slice": "beta1", "enemies": "Genin and up substitute once per fight"},
    "counters": "Counters come from parries (P L), Iron Guard's block counter, Swaying Willow's dodge strikes and counter jutsu (Palm Rotation, substitution feints)",
    "stagger_and_poise": "Every move carries poise damage; at 0 poise the target staggers (16 ticks), which interrupts casts. Bosses show a poise ring when low",
}

COMPETITIVE = [
    "Taijutsu costs stamina, which refills in about three seconds; ninjutsu costs chakra, which takes a minute to refill. Close fighters are limited by timing, casters by their bar.",
    "Taijutsu scales +4% a level (ninjutsu and weapons +3%), plus the taijutsu pillar's rank, the style's tier and the inner gates.",
    "Any hit interrupts an enemy weaving signs, and hand signs take 4 ticks each: a fighter who closes the gap shuts a caster down.",
    "Momentum finishers are the close-range answer to an S-rank jutsu: no chakra, cinematic, and they grow with each style tier.",
    "Parries, counters and poise breaks matter against every enemy; bosses have taijutsu openings (a stagger phase after each poise break).",
    "Enemies that resist ninjutsu (barrier users, armoured samurai, chakra absorbers, Gentle Fist users) appear from the Genin arc on; the duel simulator checks every build stays within 20% of the others' time-to-kill.",
    "Chakra-infused styles (Gentle Fist, Blossom Strength, Lightning Body, chakra flow) let close fighters spend chakra for bursts without giving up their pillar.",
]
