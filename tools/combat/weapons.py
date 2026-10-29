"""Weapons as a full pillar: stats keyed by item id (the items session owns the registry, prices,
crafting and grades), throw and retrieval rules, coatings, tools, and the weapon and kenjutsu styles."""

from taijutsu import mv


def weapon(item, name, cls, slice_, *, melee=None, throw=None, style=None, notes=None, **extra):
    w = {"item": item, "name": name, "class": cls, "slice": slice_}
    if melee:
        w["melee"] = melee
    if throw:
        w["throw"] = throw
    if style:
        w["style"] = style
    if notes:
        w["notes"] = notes
    w.update(extra)
    return w


def melee(dmg, kind, reach, interval, poise, **kw):
    d = {"damage": dmg, "type": kind, "reach": reach, "chain_interval_ticks": interval, "poise": poise}
    d.update(kw)
    return d


def thrown(dmg, kind, speed, rng, *, spread=1.0, retrieve=True, stack=1, poise=1, recovery=8, **kw):
    d = {"damage": dmg, "type": kind, "speed": speed, "range": rng, "spread_degrees": spread,
         "retrievable": retrieve, "per_throw": stack, "poise": poise, "recovery_ticks": recovery}
    d.update(kw)
    return d


# Melee weapon damage multiplies the style moves marked weapon_mult, so it sits near a fist's 2.0: a blade's
# edge is reach, slashing, parry frames and its techniques, never twice a punch (COMBAT.md, "Weapons").
GRADES = {"source": "the items session's crafted grades", "default_mult": {"common": 1.0, "fine": 1.1, "master": 1.2},
          "applies_to": ["damage", "durability"], "note": "Combat reads the grade from the item stack; the multipliers are the items session's to tune"}

WEAPONS = [
    weapon("item:kunai_practice", "Practice kunai", "both", "beta1",
           melee=melee(1.4, "physical.blunt", 2.6, 6, 2), throw=thrown(1.0, "physical.blunt", 1.6, 16, spread=2.0),
           style="combat:style.academy_blade", notes="Blunt Academy tool: no bleeding, no loss on death"),
    weapon("item:shuriken_practice", "Practice shuriken", "thrown", "beta1",
           throw=thrown(0.8, "physical.blunt", 2.0, 18, spread=2.5, stack=1, recovery=10), style="combat:style.throwing_arts"),
    weapon("item:kunai", "Kunai", "both", "beta2",
           melee=melee(2.0, "physical.pierce", 2.6, 6, 3, parry_bonus_ticks=1),
           throw=thrown(3.0, "physical.pierce", 1.8, 24, spread=1.0, poise=4, recovery=12, embeds=True, taggable=True, wireable=True),
           style="combat:style.academy_blade",
           notes="The all-round tool: a combo weapon in hand (the taijutsu chain with slashes), thrown like a trident, retrievable, carries a paper bomb or wire"),
    weapon("item:shuriken", "Shuriken", "thrown", "beta2",
           throw=thrown(2.2, "physical.pierce", 2.4, 22, spread=1.5, stack=1, recovery=10,
                        fan_of_three={"rank": 2, "mult": 1.3, "dodge_mult": 0.7, "recovery_ticks": 4}),
           style="combat:style.throwing_arts", notes="Fast and stackable; three at once from Genin"),
    weapon("item:shuriken_manji", "Manji shuriken", "thrown", "beta3",
           throw=thrown(3.2, "physical.slash", 2.2, 22, spread=1.2, recovery=12, bleed_chance=0.2,
                        fan_of_three={"rank": 2, "mult": 1.3, "dodge_mult": 0.7, "recovery_ticks": 4}), style="combat:style.throwing_arts"),
    weapon("item:shuriken_fuma", "Windmill shuriken", "thrown", "chunin",
           melee=melee(2.2, "physical.slash", 2.8, 10, 6),
           throw=thrown(9.0, "physical.slash", 1.4, 28, spread=0.5, recovery=16, returns=True, pierce_targets=3),
           style="combat:style.throwing_arts", notes="Folds in hand; thrown, it curves back to you (catch it for a free re-throw)"),
    weapon("item:senbon", "Senbon", "thrown", "beta2",
           throw=thrown(1.5, "physical.pierce", 2.8, 20, spread=0.8, stack=1, recovery=8, armour_pierce=0.8, silent=True,
                        pressure_points="weapons rank 4: a headshot applies numbed; three stacks paralyse (Shiranui from rank 2)"),
           style="combat:style.needle_arts", notes="Needles: tiny damage, silent, ignore most armour, carry coatings best (x2 coating stacks)"),
    weapon("item:tanto", "Tanto", "melee", "beta2",
           melee=melee(2.3, "physical.slash", 2.8, 5, 4, parry_bonus_ticks=1), style="combat:style.academy_blade"),
    weapon("item:ninjato", "Ninjato", "melee", "beta3",
           melee=melee(2.5, "physical.slash", 3.2, 6, 6), style="combat:style.crescent_moon",
           notes="Straight short sword; works with every kenjutsu style"),
    weapon("item:katana", "Katana", "melee", "beta3",
           melee=melee(2.7, "physical.slash", 3.5, 7, 7), style="combat:style.crescent_moon"),
    weapon("item:kokuto", "Black blade (kokuto)", "melee", "beta2",
           melee=melee(2.5, "physical.slash", 3.2, 6, 6, silent=True), style="combat:style.wave_foot", clan="namiashi",
           notes="The Namiashi's black sword: drinks light (no glint telegraph on your heavies)"),
    weapon("item:white_sabre", "White chakra sabre", "melee", "jonin",
           melee=melee(3.1, "physical.slash", 3.0, 5, 6, chakra_flow="lightning"), style="combat:style.white_fang", clan="hatake",
           notes="A tanto that glows with chakra; its finisher is a lightning dash"),
    weapon("item:clan_staff", "Clan staff", "melee", "beta2",
           melee=melee(2.2, "physical.blunt", 4.5, 7, 9, sweep=True), style="combat:style.monkey_staff", clan="sarutobi",
           notes="The Sarutobi's long staff (an item, not a summon): 4.5 blocks of reach, uses the combo system"),
    weapon("item:bo_staff", "Bo staff", "melee", "beta2",
           melee=melee(1.9, "physical.blunt", 4.0, 7, 8, sweep=True), style="combat:style.monkey_staff"),
    weapon("item:kusarigama", "Kusarigama", "both", "beta3",
           melee=melee(2.0, "physical.slash", 6.0, 8, 5, pull=True, wraps=True),
           throw=thrown(3.0, "physical.slash", 1.6, 10, retrieve=False, recovery=10, tethered=True, pulls=True),
           style="combat:style.chain_arts", notes="Sickle on a chain: hook at six blocks and pull the target in, or wrap a weapon arm (disarms for 40 ticks)"),
    weapon("item:chain_weight", "Weighted chain", "melee", "beta3",
           melee=melee(1.8, "physical.blunt", 5.0, 7, 8, binds=True), style="combat:style.chain_arts"),
    weapon("item:tessen", "Iron war fan", "melee", "beta3",
           melee=melee(2.0, "physical.blunt", 2.8, 6, 6, guard_reduction=0.7),
           style="combat:style.fan_arts", notes="Guard as a fan, strike with its edge; a wind user's gusts from it cost 20% less"),
    weapon("item:great_fan", "Great fan", "melee", "chunin",
           melee=melee(2.2, "physical.blunt", 3.4, 9, 10, guard_reduction=0.75, wind_amplify=1.3),
           style="combat:style.fan_arts", notes="Wind jutsu cast through it gain 30% power and width"),
    weapon("item:mace", "Mace", "melee", "beta2",
           melee=melee(2.6, "physical.blunt", 3.0, 9, 14, guard_damage_mult=2.0), style="combat:style.mace_arts", clan="hagane"),
    weapon("item:trench_knives", "Chakra trench knives", "melee", "jonin",
           melee=melee(2.6, "physical.slash", 2.8, 5, 5, chakra_flow="any"), style="combat:style.academy_blade",
           notes="Knuckle blades that conduct chakra: chakra flow costs half"),
    weapon("item:knuckle_wraps", "Fist wraps", "gear", "beta1", notes="Taijutsu gear: +0.5 light damage, no weapon in hand"),
]

TOOLS = [
    {"item": "item:paper_bomb", "name": "Paper bomb", "slice": "beta2", "use": "throw (sticks to surfaces and entities) or tag a kunai",
     "fuse_ticks": 30, "damage": 6.0, "type": "physical.blunt", "radius": 3.0, "poise": 30, "blocks": "never breaks blocks",
     "cooldown_ticks": 60, "avoid": "a lit tag is seen: anyone not stunned walks out of it about half the time, more with a dodge",
     "remote": "Weave Ram detonates every bomb you placed (weapons rank 3)", "trap": "placed on the ground it is a mine for 60 s"},
    {"item": "item:smoke_bomb", "name": "Smoke bomb", "slice": "beta1", "radius": 4.0, "ticks": 120,
     "effect": "smoked: enemies inside lose their target unless sensing; you leave their tracking", "escape": "dropping one at your feet breaks lock-on"},
    {"item": "item:flash_bomb", "name": "Flash bomb", "slice": "beta2", "radius": 6.0, "effect": "blinded 40 ticks for anyone facing it (yourself too)",
     "counters": "genjutsu: a flash breaks genjutsu on allies"},
    {"item": "item:wire_spool", "name": "Ninja wire", "slice": "beta1", "uses": 8,
     "modes": {"tripwire": "between two points (a trap that trips, knocks down and triggers tagged bombs)",
               "tether": "on a thrown kunai: yank it back with the throw key (and the target, if light)",
               "binding": "throw two kunai past a target and pull: bound for 40 ticks (weapons rank 4)",
               "fire_line": "a fire user can run a flame down a wire (Dragon Flame)"}},
    {"item": "item:caltrops", "name": "Caltrops", "slice": "beta2", "radius": 2.0, "ticks": 400, "effect": "slow 0.4 and 1.0 damage a second to anyone walking (not running on chakra)"},
    {"item": "item:sealing_tag", "name": "Sealing tag", "slice": "beta2",
     "effect": "stick on a downed or stunned enemy: captured (a quest objective; bosses resist); or on a technique scroll: stores one cast",
     "fuinjutsu": "the base of the sealing techniques (four tags make a barrier)"},
    {"item": "item:tool_pouch", "name": "Tool pouch", "slice": "beta2", "quick_slots": 4,
     "use": "quick-throw key (G) throws the selected pouch slot without changing the hotbar; scroll with G held",
     "upgrades": {"item:tool_pouch_large": 6, "weapons_rank_4": 1, "weapons_rank_8": 1, "item:flak_vest": 2}},
    {"item": "item:soldier_pill", "name": "Soldier pill", "slice": "beta2", "restores": {"chakra_fraction": 0.4, "stamina": 100},
     "cooldown_ticks": 1200, "side_effect": "hunger -3"},
    {"item": "item:blood_pill", "name": "Blood pill", "slice": "beta3", "restores": {"hp_per_second": 0.5, "ticks": 200}, "cooldown_ticks": 1200},
    {"item": "item:poultice", "name": "Herbal poultice", "slice": "beta2", "restores": {"hp": 6}, "cleanses": ["poisoned", "bleeding"],
     "use_ticks": 30, "clan_craft": "suzuran"},
    {"item": "item:antidote", "name": "Antidote", "slice": "beta2", "cleanses": ["poisoned", "numbed", "drowsy"], "immunity_ticks": 200},
]

COATINGS = {
    "how": "Right click a coating with a blade, kunai, shuriken or senbon in the off hand: the next N hits carry it. Suzuran craft them at the workbench (clan technique tier 1); others buy them",
    "list": [
        {"item": "item:coating_numbing", "status": "numbed", "hits": 6, "slice": "beta2"},
        {"item": "item:coating_sleep", "status": "drowsy", "hits": 4, "slice": "beta3", "bosses": "drowsy only, never asleep"},
        {"item": "item:coating_venom", "status": "poisoned", "hits": 6, "slice": "beta2"},
    ],
    "senbon_mult": 2, "resisted_by": {"clan:suzuran": "immune", "clan:aburame": "poison half", "enemy.trait:poison_immune": "immune"},
}

THROWING = {
    "aim": "hold use to aim (a thin arc preview on Story), release to throw; tap to throw at once at the crosshair",
    "accuracy": "spread in degrees x (1 + 0.5 moving) x (1 - 0.05 weapons rank); Story aim assist bends 5 degrees toward a lock-on target",
    "retrieval": "thrown kunai, shuriken and senbon embed as entities for 60 s; walk over them to pick them up; a wired kunai comes back on the throw key; the windmill returns by itself",
    "death": "the thrown tools you carry are lost on death (ROADMAP Death); practice tools are never lost",
    "deflect": "a thrown tool can be knocked down by a parry, a kunai swing timed on it, a wind gust or an earth wall",
    "multi": "three shuriken at once from weapons rank 2 (x1.3 damage, 30% harder to dodge, 4 more ticks of recovery); five from rank 6 (Manipulated Shuriken bends them)",
    "pouch": "tool pouch quick-throw (G) reaches the pouch's slots",
    "budget": "a throw costs 2 stamina and its recovery ticks; ryo is the real limit: a kunai costs about 10 ryo, a paper bomb 40",
}


def wstyle(sid, name, weapons, who, mentor, slice_, feel, moves, **kw):
    s = {"id": sid, "name": name, "pillar": "weapons", "weapons": weapons, "who": who, "mentor": mentor, "slice": slice_,
         "feel": feel, "moves": moves}
    s.update(kw)
    return s


SL = "physical.slash"
BL = "physical.blunt"
PI = "physical.pierce"

WEAPON_STYLES = [
    wstyle("combat:style.academy_blade", "Academy blade", ["item:kunai_practice", "item:kunai", "item:tanto", "item:trench_knives"],
           "everyone", "role:instructor", "beta1", "The taijutsu chain with a blade in hand: slashes, a reverse-grip parry and a throw-out finisher.",
           [mv("slash_1", "L", 1.0, 3, (2, 2, 5), kind=SL, slice_="beta1", weapon_mult=True),
            mv("slash_2", "L L", 1.0, 3, (2, 2, 5), kind=SL, slice_="beta1", weapon_mult=True),
            mv("slash_3", "L L L", 1.3, 6, (3, 2, 10), kind=SL, window=(0, 0), slice_="beta1", weapon_mult=True, knockback=1.0),
            mv("stab", "H", 2.4, 10, (8, 3, 10), stamina=12, kind=PI, window=(0, 0), slice_="beta1", weapon_mult=True),
            mv("reverse_parry", "P L", 1.6, 8, (1, 2, 6), kind=SL, slice_="beta2", weapon_mult=True, counter=True),
            mv("throw_out", "L L H", 2.0, 8, (4, 2, 8), stamina=8, kind=PI, window=(0, 0), slice_="beta2", weapon_mult=True,
               throws_held=True, note="Ends the chain by throwing the kunai into the target")],
           note="Weapon moves with weapon_mult multiply the held weapon's melee damage"),
    wstyle("combat:style.throwing_arts", "Throwing arts", ["item:shuriken_practice", "item:shuriken", "item:shuriken_manji", "item:kunai", "item:shuriken_fuma"],
           "everyone", "role:instructor", "beta1", "Accurate, fast and tricky throws: fans, curves and hidden second stars.",
           [mv("quick_throw", "T", 1.0, 1, (2, 1, 5), kind=PI, slice_="beta1", weapon_mult=True, thrown=True),
            mv("fan_of_three", "T T", 1.0, 1, (3, 1, 8), kind=PI, slice_="beta2", weapon_mult=True, thrown=True, projectiles=3),
            mv("rising_throw", "J T", 1.2, 2, (2, 1, 6), state="air", kind=PI, slice_="beta2", weapon_mult=True, thrown=True, projectiles=3,
               note="Thrown from the air, downward"),
            mv("rain", "J T T", 1.0, 1, (4, 6, 10), state="air", kind=PI, slice_="chunin", weapon_mult=True, thrown=True, projectiles=8,
               momentum=50, finisher=True)],
           input_note="T is the throw key (use while aiming, or G for the pouch)"),
    wstyle("combat:style.needle_arts", "Needle arts", ["item:senbon"], "anyone; the Shiranui teach it (clan friendship 5)", "role:clan_elder.shiranui",
           "beta2", "Silent senbon at pressure points: numb, slow and paralyse rather than kill.",
           [mv("needle_flick", "T", 1.0, 0, (1, 1, 3), kind=PI, slice_="beta2", weapon_mult=True, thrown=True),
            mv("needle_fan", "T T", 1.0, 0, (2, 1, 6), kind=PI, slice_="beta2", weapon_mult=True, thrown=True, projectiles=5),
            mv("pressure_point", "H T", 2.0, 0, (6, 1, 8), kind=PI, slice_="chunin", weapon_mult=True, thrown=True, applies="numbed", stacks=2)],
           clan_lesser="shiranui"),
    wstyle("combat:style.crescent_moon", "Crescent Moon kenjutsu", ["item:ninjato", "item:katana", "item:tanto"],
           "anyone at weapons rank 4; the Gekko (clan-born) from Genin", "role:clan_elder.gekko", "beta3",
           "The Gekko's kenjutsu: wide arcs, a draw-cut counter and the Dance of the Crescent Moon.",
           [mv("arc_1", "L", 1.0, 4, (3, 2, 5), kind=SL, slice_="beta3", weapon_mult=True),
            mv("arc_2", "L L", 1.0, 4, (3, 2, 5), kind=SL, slice_="beta3", weapon_mult=True),
            mv("arc_3", "L L L", 1.4, 10, (4, 3, 10), kind=SL, window=(0, 0), slice_="beta3", weapon_mult=True, area_blocks=2.5),
            mv("draw_cut", "P L", 2.0, 12, (1, 2, 6), kind=SL, slice_="beta3", weapon_mult=True, counter=True),
            mv("moon_rising", "L L H", 1.6, 14, (5, 3, 8), stamina=15, kind=SL, window=(0, 10), slice_="beta3", weapon_mult=True, launches=True),
            mv("crescent_finish", "L L L H", 3.5, 40, (6, 6, 14), stamina=10, momentum=70, kind=SL, window=(0, 0), slice_="chunin",
               weapon_mult=True, finisher=True, cinematic=True)],
           clan="gekko"),
    wstyle("combat:style.wave_foot", "Wave-foot kenjutsu", ["item:kokuto", "item:tanto", "item:ninjato"],
           "Namiashi from Genin; others at weapons rank 5 with clan friendship 7", "role:clan_elder.namiashi", "beta2",
           "The bodyguard's sword: short, silent strokes, a guard that steps aside and returns the blow.",
           [mv("ripple_1", "L", 0.9, 3, (2, 2, 4), kind=SL, slice_="beta2", weapon_mult=True),
            mv("ripple_2", "L L", 0.9, 3, (2, 2, 4), kind=SL, slice_="beta2", weapon_mult=True),
            mv("ripple_3", "L L L", 0.9, 3, (2, 2, 4), kind=SL, slice_="beta2", weapon_mult=True),
            mv("undertow", "L L L L", 1.5, 10, (3, 2, 10), kind=SL, window=(0, 0), slice_="beta2", weapon_mult=True, knocks_down=True),
            mv("side_step_cut", "D L", 1.6, 6, (2, 2, 6), kind=SL, slice_="beta2", weapon_mult=True, counter=True),
            mv("guard_of_waves", "G L", 1.8, 10, (2, 2, 6), kind=SL, slice_="chunin", weapon_mult=True, counter=True,
               note="A block that deflects the blow to the side and cuts back")],
           clan="namiashi"),
    wstyle("combat:style.white_fang", "White Fang", ["item:white_sabre", "item:tanto"], "Hatake; others at weapons rank 8", "role:clan_elder.hatake",
           "jonin", "Blinding tanto speed and a lightning dash finisher.",
           [mv("fang_1", "L", 1.0, 3, (1, 2, 4), kind=SL, slice_="jonin", weapon_mult=True),
            mv("fang_2", "L L", 1.0, 3, (1, 2, 4), kind=SL, slice_="jonin", weapon_mult=True),
            mv("fang_3", "L L L", 1.4, 8, (2, 2, 8), kind=SL, window=(0, 0), slice_="jonin", weapon_mult=True),
            mv("white_light_dash", "L L L H", 4.0, 50, (4, 6, 14), stamina=10, momentum=70, kind="ninjutsu.lightning", window=(0, 0),
               slice_="jonin", weapon_mult=True, finisher=True, dash_blocks=10, chakra=10, cinematic=True)],
           clan="hatake"),
    wstyle("combat:style.monkey_staff", "Monkey King staff", ["item:clan_staff", "item:bo_staff"], "Sarutobi with the clan staff; anyone with a bo staff (tiers 1 and 2)",
           "role:clan_elder.sarutobi", "beta2", "Long sweeping arcs that keep a crowd at bay, pole vaults and a spinning finisher.",
           [mv("sweep_1", "L", 1.0, 5, (3, 2, 6), kind=BL, slice_="beta2", weapon_mult=True, area_blocks=1.5),
            mv("sweep_2", "L L", 1.0, 5, (3, 2, 6), kind=BL, slice_="beta2", weapon_mult=True, area_blocks=1.5),
            mv("thrust", "L L L", 1.4, 12, (4, 2, 10), kind=BL, window=(0, 0), slice_="beta2", weapon_mult=True, knockback=2.5),
            mv("pole_vault", "X H", 1.6, 12, (6, 3, 10), stamina=12, kind=BL, window=(0, 0), slice_="beta2", weapon_mult=True, dash_blocks=6, launches=True),
            mv("whirling_staff", "L L L H", 3.6, 40, (5, 14, 14), stamina=10, momentum=60, kind=BL, window=(0, 0), slice_="chunin",
               weapon_mult=True, finisher=True, area_blocks=4.5, deflects_projectiles=True)],
           clan="sarutobi"),
    wstyle("combat:style.chain_arts", "Chain arts", ["item:kusarigama", "item:chain_weight"], "anyone at weapons rank 3", "role:weapon_master",
           "beta3", "Reach and control: hook, pull, wrap and bind.",
           [mv("chain_lash", "L", 1.0, 3, (3, 2, 6), kind=SL, slice_="beta3", weapon_mult=True),
            mv("chain_lash_2", "L L", 1.0, 3, (3, 2, 6), kind=SL, slice_="beta3", weapon_mult=True),
            mv("hook_pull", "H", 1.2, 6, (8, 2, 10), stamina=12, kind=SL, window=(0, 0), slice_="beta3", weapon_mult=True, pulls_blocks=5),
            mv("wrap_bind", "L L H", 0.8, 10, (6, 2, 10), stamina=15, kind=BL, window=(0, 0), slice_="chunin", weapon_mult=True, applies="bound", ticks=40)]),
    wstyle("combat:style.fan_arts", "Fan arts", ["item:tessen", "item:great_fan"], "anyone at weapons rank 3 (wind users gain most)", "role:nature_master.wind",
           "beta3", "Guard behind steel, slice with the edge, and push gusts through the fan.",
           [mv("fan_cut", "L", 1.0, 4, (2, 2, 5), kind=SL, slice_="beta3", weapon_mult=True),
            mv("fan_cut_2", "L L", 1.0, 4, (2, 2, 5), kind=SL, slice_="beta3", weapon_mult=True),
            mv("fan_snap", "L L L", 1.3, 10, (3, 2, 10), kind=BL, window=(0, 0), slice_="beta3", weapon_mult=True, knockback=2.0),
            mv("gust_parry", "P H", 1.0, 12, (2, 3, 8), kind="ninjutsu.wind", slice_="beta3", weapon_mult=True, counter=True, chakra=4,
               deflects_projectiles=True)]),
    wstyle("combat:style.mace_arts", "Mace arts", ["item:mace", "item:bo_staff"], "Hagane; others at clan friendship 5", "role:clan_elder.hagane", "beta2",
           "Slow, crushing swings that break guards and poise.",
           [mv("mace_1", "L", 1.0, 6, (4, 2, 8), kind=BL, slice_="beta2", weapon_mult=True),
            mv("mace_2", "L L", 1.1, 8, (4, 2, 8), kind=BL, slice_="beta2", weapon_mult=True),
            mv("mace_overhead", "H", 1.8, 24, (10, 3, 14), stamina=14, kind=BL, window=(0, 0), slice_="beta2", weapon_mult=True, guard_break=True)],
           clan_lesser="hagane"),
    wstyle("combat:style.wire_arts", "Wire arts", ["item:wire_spool", "item:kunai"], "anyone; the Kinoshita teach traps (clan friendship 5)",
           "role:clan_elder.kinoshita", "beta2", "Traps, tethers and binds: fight on ground you prepared.",
           [mv("tether_yank", "T H", 1.0, 6, (2, 2, 6), kind=PI, slice_="beta2", weapon_mult=True, pulls_blocks=3),
            mv("trip_line", "G T", 0.0, 20, (6, 2, 6), slice_="beta2", trap=True, knocks_down=True),
            mv("binding_cross", "T T H", 0.5, 10, (4, 2, 10), kind=PI, slice_="chunin", weapon_mult=True, applies="bound", ticks=40)],
           clan_lesser="kinoshita"),
    wstyle("combat:style.iaido", "Iaido", ["item:katana"], "post-game, from a samurai master", "role:samurai_master", "post",
           "Sheathe, wait, and cut once.",
           [mv("quick_draw", "H", 4.0, 30, (12, 2, 16), stamina=15, kind=SL, window=(0, 0), slice_="post", weapon_mult=True, counter=True,
               note="A held stance: any melee attack inside 3 blocks is answered by the draw")]),
]
