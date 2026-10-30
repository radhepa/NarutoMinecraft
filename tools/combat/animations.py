"""Every combat pose and clip the player and residents need, keyed the way VF keys its clips
(tools/animations/: a Python dict of clip id -> clip), with the keyframes authored into this same
table (keys() below); the player's poser reads them from animations.json, and they compile later to
assets/narutominecraft/resident_animations/*.json for residents.

Fields: ticks (length), loop, who (player, resident or both), fp (needs a first-person arm path),
priority (P0: the Phase 0 spike and Beta 1; P1: Beta 2; P2: Beta 3; P3: later), slice, and keys
(None until authored: VF's keyframe list of {tick, part, rot}; rotation only, linear, for now).
"""

P0, P1, P2, P3 = "P0", "P1", "P2", "P3"
SLICE_OF = {P0: "beta1", P1: "beta2", P2: "beta3", P3: "later"}

CLIPS = {}


def clip(cid, ticks, pr, who="both", loop=False, fp=False, note=None, slice_=None):
    c = {"ticks": ticks, "loop": loop, "who": who, "fp": fp, "priority": pr, "slice": slice_ or SLICE_OF[pr], "keys": None}
    if note:
        c["note"] = note
    CLIPS["combat." + cid] = c


def many(prefix, names, ticks, pr, **kw):
    for n in names:
        clip(prefix + n, ticks, pr, **kw)


# Stance, movement and chakra movement
clip("stance.idle", 40, P0, loop=True, note="Combat-ready idle: knees bent, kunai or fists up")
clip("stance.walk_guard", 20, P0, loop=True)
clip("move.crouch_hide", 30, P0, loop=True, who="player", note="Prologue")
clip("move.slip_out", 40, P0, who="player", note="Prologue: squeezing out of the cell")
clip("move.carried", 40, P0, loop=True, who="player", note="Prologue: carried over the ravine")
clip("move.carry", 40, P0, loop=True, who="resident", note="Prologue: the captain carries you")
clip("move.roof_hop", 10, P0)
clip("move.ninja_run", 12, P1, loop=True, note="Arms back")
clip("move.chakra_jump_charge", 20, P1, loop=True, who="player")
clip("move.chakra_jump_air", 16, P1)
clip("move.land_roll", 10, P1)
clip("move.wall_run", 12, P1, loop=True)
clip("move.tree_walk", 16, P1, loop=True, note="The model is rotated to the trunk; the clip is a careful walk")
clip("move.water_stance", 40, P1, loop=True)
clip("move.water_sink", 20, P1)
clip("move.air_step", 8, P3)
clip("move.wind_glide", 20, P3, loop=True)
clip("move.four_legs_run", 10, P1, loop=True, note="Inuzuka beast fang")
clip("move.boulder_roll", 10, P1, loop=True, note="Akimichi Human Boulder")

# Defence and reactions
many("def.dodge_", ["left", "right", "back", "forward"], 8, P0)
clip("def.perfect_dodge", 8, P1, note="Adds an afterimage particle")
clip("def.substitution_vanish", 4, P0, note="A puff; the log entity takes the hit")
clip("def.block", 20, P0, loop=True, fp=True)
clip("def.block_hit", 6, P0, fp=True)
clip("def.guard_break", 20, P0)
clip("def.parry", 6, P1, fp=True)
clip("def.parry_weapon", 6, P1, fp=True)
clip("react.hit_light_front", 6, P0)
clip("react.hit_light_back", 6, P0)
clip("react.hit_heavy", 10, P0)
clip("react.stagger", 16, P0)
clip("react.knocked_down", 24, P1)
clip("react.get_up", 10, P1)
clip("react.launched", 20, P1)
clip("react.air_juggle", 6, P1)
clip("react.knocked_out", 40, P0, note="VF Knockouts: lying down")
clip("react.yield", 20, P0, note="Hand raised, kneeling")
clip("react.surrender", 30, P1, who="resident", loop=True, note="Bandits: kneel, hands up")
clip("react.flee", 12, P1, who="resident", loop=True)
clip("react.bound_struggle", 20, P1, loop=True)
clip("react.possessed_mirror", 0, P1, note="No clip: copies the caster's pose live")
clip("react.genjutsu_dazed", 30, P1, loop=True)
clip("react.shocked_twitch", 10, P1, loop=True)
clip("react.burning_flail", 20, P1, loop=True)
clip("react.poisoned_stagger", 30, P1, loop=True)
clip("react.asleep", 40, P2, loop=True)
clip("react.feared_cower", 30, P1, loop=True)
clip("react.swallowed", 0, P2, note="No clip: hidden while swallowed")
clip("pose.victory", 30, P0)
clip("pose.taunt", 30, P1, who="resident")
clip("pose.tired_slouch", 40, P0, loop=True, who="player", note="Fatigue")
clip("pose.meditate", 40, P0, loop=True)

# Hand signs: one hold pose per sign, both hands, first person too
many("sign.", ["rat", "ox", "tiger", "hare", "dragon", "snake", "horse", "ram", "monkey", "bird", "dog", "boar"], 4, P0, fp=True)
clip("sign.transition", 2, P0, fp=True, note="Blend between any two signs")
clip("sign.fizzle", 8, P0, fp=True, note="Hands shake apart")
clip("sign.release_ram", 6, P0, fp=True, note="Genjutsu Release")

# Cast poses (shared by many techniques)
clip("cast.push_palms", 8, P0, fp=True, note="Generic forward release (Clone, Transformation poof)")
clip("cast.breath", 16, P1, fp=True, note="Hand to mouth: fire and wind breath jutsu")
clip("cast.clap_gust", 8, P1, fp=True, note="Wind: Gale Palm, Great Breakthrough")
clip("cast.ground_slam", 10, P1, fp=True, note="Earth: walls, mud river")
clip("cast.palm_strike", 8, P1, fp=True, note="Lightning: Stunning Palm")
clip("cast.spit_wave", 12, P1, fp=True, note="Water: Wild Water Wave")
clip("cast.kneel_sign_hold", 20, P1, loop=True, note="Nara Shadow Possession")
clip("cast.slump", 40, P3, loop=True, note="Yamanaka Mind Transfer body")
clip("cast.grow", 20, P1, note="Akimichi Expansion")
clip("cast.arms_open_swarm", 16, P1, note="Aburame Insect Swarm")
clip("cast.chains_back", 12, P1, note="Uzumaki Sealing Chains")
clip("cast.wood_sign", 14, P1, note="Senju Wood Release")
clip("cast.brush_strokes", 24, P1, fp=True, note="Kurama Painted Illusion")
clip("cast.step_behind", 8, P1, note="Yuhi Tree Binding")
clip("cast.three_way_slash", 20, P1, note="Gekko Dance of the Crescent Moon")
clip("cast.eye_glance", 6, P2, note="Sharingan and Byakugan toggles (the eye change is a face decal)")
clip("cast.headhunter_sink", 12, P1)
clip("cast.headhunter_grab", 10, P1)
clip("cast.web_slam", 10, P1, note="Tsuchigumo Earth Binding")
clip("cast.night_curtain", 14, P1, note="Tobari")
clip("cast.mystical_palm", 20, P2, loop=True, fp=True)
clip("cast.sensing", 20, P2, loop=True, note="Eyes closed, a sign held")
clip("cast.seal_slap", 6, P1, fp=True)
clip("cast.barrier_tags", 12, P2)
clip("cast.water_prison_hold", 20, P3, loop=True)
clip("cast.lightning_blade_charge", 20, P3, loop=True, fp=True)
clip("cast.lightning_blade_run", 12, P3, loop=True)
clip("cast.spiral_sphere_form", 20, P3, fp=True)
clip("cast.spiral_sphere_strike", 8, P3, fp=True)
clip("cast.first_aid", 30, P0, loop=True)
clip("cast.revive_kneel", 30, P2, loop=True)

# Taijutsu: Academy
for n, t in [("jab", 9), ("cross", 9), ("roundhouse", 15), ("heavy_windup", 8), ("heavy_release", 13), ("flying_kick", 19), ("lunge", 11)]:
    clip("tai.academy." + n, t, P0, fp=True)
for n, t in [("counter", 9), ("sweep", 18), ("launcher", 14), ("air_1", 8), ("air_2", 8), ("air_3", 10), ("air_spike", 17), ("palm_rush", 30)]:
    clip("tai.academy." + n, t, P1, fp=n not in ("air_spike",))
# Taijutsu: styles
for n, t, pr in [("leaf_hurricane", 17, P1), ("leaf_rising_wind", 13, P1), ("leaf_whirlwind", 18, P1), ("leaf_great_whirlwind", 29, P2),
                 ("weights_release", 20, P1), ("primary_lotus", 40, P3), ("reverse_lotus", 50, P3), ("morning_peacock", 62, P3), ("gate_open", 20, P3)]:
    clip("tai.strong_fist." + n, t, pr)
clip("tai.gentle_fist.stance", 40, P1, loop=True)
for n, t, pr in [("palm_1", 8, P1), ("palm_2", 8, P1), ("palm_3", 8, P1), ("palm_4", 15, P1), ("palm_thrust", 21, P1), ("vacuum_palm", 21, P3),
                 ("palm_rotation", 24, P3), ("sixty_four_palms", 52, P3), ("hundred_twenty_eight_palms", 66, P3), ("twin_lion_fists", 54, P3)]:
    clip("tai.gentle_fist." + n, t, pr, fp=pr == P1)
for n, t in [("body_slam", 19), ("crushing_palm", 25), ("human_boulder", 50), ("partial_expansion_slap", 24), ("meat_tank", 64)]:
    clip("tai.iron_body." + n, t, P1 if n in ("body_slam", "crushing_palm", "human_boulder") else P3)
for n, t in [("claw_1", 8), ("claw_2", 8), ("claw_3", 8), ("claw_4", 14), ("pounce", 12), ("passing_fang", 20)]:
    clip("tai.beast_fang." + n, t, P1 if n != "passing_fang" else P3)
for n, t in [("guard_shove", 12), ("guard_crush", 21), ("iron_wall", 48)]:
    clip("tai.iron_guard." + n, t, P1 if n != "iron_wall" else P3, fp=True)
clip("tai.willow.sway_idle", 40, P3, loop=True)
for n, t in [("sway_strike", 9), ("falling_willow", 19), ("lean_back_kick", 17), ("willow_storm", 38)]:
    clip("tai.willow." + n, t, P3)
for n, t in [("blossom_punch", 25), ("blossom_heel", 27), ("cherry_blossom_impact", 34)]:
    clip("tai.blossom." + n, t, P3)
for n, t in [("lariat", 20), ("guillotine_drop", 24), ("liger_bomb", 42)]:
    clip("tai.lightning_body." + n, t, P3)

# Weapons
for n, t in [("slash_1", 9), ("slash_2", 9), ("slash_3", 15), ("stab", 21)]:
    clip("wpn.blade." + n, t, P0, fp=True)
for n, t in [("reverse_parry", 9), ("throw_out", 14)]:
    clip("wpn.blade." + n, t, P1, fp=True)
clip("wpn.throw.aim_hold", 20, P0, loop=True, fp=True)
clip("wpn.throw.overhand", 8, P0, fp=True)
clip("wpn.throw.sidearm", 8, P0, fp=True)
clip("wpn.throw.fan_of_three", 12, P1, fp=True)
clip("wpn.throw.air_down", 9, P1)
clip("wpn.throw.rain", 20, P3)
clip("wpn.throw.needle_flick", 5, P1, fp=True)
clip("wpn.throw.needle_fan", 9, P1, fp=True)
clip("wpn.throw.catch", 6, P2, fp=True, note="Windmill return, kunai catch on parry")
for n, t in [("arc_1", 10), ("arc_2", 10), ("arc_3", 17), ("draw_cut", 9), ("moon_rising", 16), ("unsheathe", 8), ("sheathe", 10)]:
    clip("wpn.kenjutsu." + n, t, P2, fp=True)
clip("wpn.kenjutsu.crescent_finish", 26, P3)
for n, t in [("cut", 10), ("cut_3", 17), ("thrust", 24), ("reading_guard", 9), ("rising_cut", 16)]:
    clip("wpn.long_blade." + n, t, P2, fp=True)
clip("wpn.long_blade.single_stroke", 27, P3)
clip("wpn.kenjutsu.iaido_stance", 40, P3, loop=True)
for n, t in [("ripple", 8), ("undertow", 15), ("side_step_cut", 10), ("guard_of_waves", 10)]:
    clip("wpn.wave_foot." + n, t, P1, fp=True)
for n, t in [("idle", 40), ("sweep_1", 11), ("sweep_2", 11), ("thrust", 16), ("pole_vault", 19)]:
    clip("wpn.staff." + n, t, P1, loop=n == "idle", fp=n != "pole_vault")
clip("wpn.staff.whirling_staff", 33, P3)
for n, t in [("lash", 11), ("hook_pull", 20), ("wrap_bind", 18)]:
    clip("wpn.chain." + n, t, P2, fp=True)
for n, t in [("cut", 9), ("snap", 15), ("gust_parry", 13)]:
    clip("wpn.fan." + n, t, P2, fp=True)
for n, t in [("swing_1", 14), ("swing_2", 14), ("overhead", 27)]:
    clip("wpn.mace." + n, t, P1, fp=True)
for n, t in [("tether_yank", 10), ("set_trip_line", 14), ("binding_cross", 16)]:
    clip("wpn.wire." + n, t, P1, fp=True)
for n, t in [("place_paper_bomb", 10), ("tag_kunai", 6), ("throw_smoke", 8), ("eat_pill", 12), ("apply_coating", 16), ("pouch_draw", 4)]:
    clip("wpn.tool." + n, t, P1 if n != "throw_smoke" else P0, fp=True)

# Squad play
clip("squad.command_point", 10, P1, who="player")
clip("squad.command_wave", 10, P1, who="player")
clip("squad.acknowledge", 10, P1, who="resident")
clip("squad.high_five", 16, P1, note="After a squad combo")
clip("squad.cover_dive", 10, P2)
clip("squad.call_combo", 12, P1, who="resident")

# Residents around fights
clip("res.salute", 16, P0, who="resident")
clip("res.nod", 10, P0, who="resident")
clip("res.excited_wave", 20, P0, who="resident", note="Kids")
clip("res.spar_bow", 16, P0, who="both")
clip("res.spectator_cheer", 30, P2, who="resident", loop=True)
clip("res.spectator_gasp", 12, P2, who="resident")
clip("res.spectator_seated_clap", 20, P2, who="resident", loop=True)
clip("res.proctor_stop", 16, P2, who="resident")
clip("res.sensei_reading", 40, P1, who="resident", loop=True, note="The cord test")
clip("res.sensei_book_dodge", 8, P1, who="resident", note="The cord test: dodges without looking up")
clip("res.cower_civilian", 30, P2, who="resident", loop=True, note="The attack: civilians in the stands")

# Non-combat clips the roadmap lists with the combat clips (owned by Shinobi Life's stations)
clip("life.petting", 30, P0, who="player")
clip("life.forging", 30, P1, loop=True, who="player")
clip("life.workbench", 30, P0, loop=True, who="player")


# Keys: VF's {tick, part, rot} keyframes, rot in degrees (x pitches an arm forward when negative, y turns it
# inward, z swings it out), linear between keys, held after the last; parts head, body, right_arm, left_arm,
# right_leg, left_leg. A part a clip leaves out keeps the vanilla pose.
def keys(cid, *frames):
    """frames: (tick, {part: (x, y, z)})."""
    assert all(p in ("head", "body", "right_arm", "left_arm", "right_leg", "left_leg") for _, parts in frames for p in parts), cid
    CLIPS["combat." + cid]["keys"] = [{"tick": t, "part": p, "rot": list(r)} for t, parts in frames for p, r in parts.items()]


def arms(x, y, z=0, lx=None, ly=None, lz=None):
    """Both arms: the left mirrors the right unless its own raw (x, y, z) is given."""
    return {"right_arm": (x, -y, z), "left_arm": (x if lx is None else lx, y if ly is None else ly, -z if lz is None else lz)}


HANDS = arms(-63, 31.5)   # hands together before the chest: where every sign starts and ends
SIGN_POSES = {   # (pitch, inward turn, outward swing) for each sign; a sign that is not symmetric gives the left arm too
    "rat": arms(-62, 32), "ox": arms(-70, 35, -10, -55, 30, 5), "tiger": arms(-78, 30), "hare": arms(-50, 38, 0, -65, 25),
    "dragon": arms(-82, 28, -5), "snake": arms(-58, 30, 10), "horse": arms(-88, 25), "ram": arms(-68, 34, 0, -60, 30),
    "monkey": arms(-55, 40, -15, -70, 35), "bird": arms(-65, 36, 15), "dog": arms(-45, 30, 0, -60, 35), "boar": arms(-52, 34),
}
for name, sign in SIGN_POSES.items():
    keys("sign." + name, (0, HANDS), (2, sign), (4, sign))
keys("sign.transition", (0, HANDS), (2, HANDS))
keys("sign.fizzle", (0, HANDS), (2, arms(-60, 10, 20)), (4, arms(-50, -10, 30)), (8, arms(0, 0)))
keys("cast.push_palms", (0, arms(-60, 25)), (3, arms(-90, 10)), (6, arms(-90, 10)), (8, arms(-40, 0)))
GUARD = arms(-92, 52)
keys("def.block", (0, GUARD), (10, arms(-88, 50)), (20, GUARD))
REST = {"right_arm": (0, 0, 0), "left_arm": (0, 0, 0), "right_leg": (0, 0, 0), "left_leg": (0, 0, 0)}
for d, pose in {
    "back": {**arms(-60, 15), "right_leg": (30, 0, 0), "left_leg": (-25, 0, 0)},
    "forward": {**arms(40, 0, 10), "right_leg": (-40, 0, 0), "left_leg": (30, 0, 0)},
    "left": {**arms(-20, 0, 30, -20, 0, -55), "right_leg": (0, 0, 10), "left_leg": (0, 0, -25)},
    "right": {**arms(-20, 0, 55, -20, 0, -30), "right_leg": (0, 0, 25), "left_leg": (0, 0, -10)},
}.items():
    keys("def.dodge_" + d, (0, REST), (2, pose), (6, pose), (8, REST))
# Academy taijutsu: the three-hit combo and the heavy, from a raised guard.
FISTS = arms(-70, 25)
keys("tai.academy.jab", (0, FISTS), (3, {**FISTS, "right_arm": (-90, 0, 0)}), (5, {**FISTS, "right_arm": (-90, 0, 0)}), (9, FISTS))
keys("tai.academy.cross", (0, FISTS), (3, {**FISTS, "left_arm": (-90, 0, 0), "body": (0, -20, 0)}),
     (5, {**FISTS, "left_arm": (-90, 0, 0), "body": (0, -20, 0)}), (9, {**FISTS, "body": (0, 0, 0)}))
KICK = {**FISTS, "right_leg": (-70, 0, 60), "body": (0, 0, -15)}
keys("tai.academy.roundhouse", (0, {**FISTS, "right_leg": (0, 0, 0), "body": (0, 0, 0)}), (4, {**KICK, "right_leg": (-30, 0, 40)}),
     (7, KICK), (10, KICK), (15, {**FISTS, "right_leg": (0, 0, 0), "body": (0, 0, 0)}))
WOUND = {**FISTS, "right_arm": (40, 0, 20), "body": (0, -25, 0)}
keys("tai.academy.heavy_release", (0, WOUND), (3, {**FISTS, "right_arm": (-100, 0, 0), "body": (0, 25, 0)}),
     (8, {**FISTS, "right_arm": (-100, 0, 0), "body": (0, 25, 0)}), (13, {**FISTS, "body": (0, 0, 0)}))
# The enders reachable from a spar's light and heavy presses.
LOW = {**FISTS, "body": (25, 0, 0), "right_leg": (-20, 0, 50), "left_leg": (-30, 0, 0)}
keys("tai.academy.sweep", (0, {**FISTS, "body": (0, 0, 0), "right_leg": (0, 0, 0), "left_leg": (0, 0, 0)}), (5, LOW), (12, LOW),
     (18, {**FISTS, "body": (0, 0, 0), "right_leg": (0, 0, 0), "left_leg": (0, 0, 0)}))
UP = {"right_arm": (-170, 0, 10), "left_arm": (-60, 25, 0), "body": (-10, 0, 0)}
keys("tai.academy.launcher", (0, {**FISTS, "body": (10, 0, 0)}), (4, UP), (9, UP), (14, {**FISTS, "body": (0, 0, 0)}))
PALMS = [arms(-90, 0), arms(-90, 0, 0, -50, 25)]
keys("tai.academy.palm_rush", *[(t, PALMS[i % 2]) for i, t in enumerate(range(0, 25, 3))], (30, FISTS))


def summary():
    counts = {}
    for c in CLIPS.values():
        counts[c["priority"]] = counts.get(c["priority"], 0) + 1
    return counts
