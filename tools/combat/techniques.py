"""The technique catalogue, E to S: neutral ninjutsu, the five natures, genjutsu, medical ninjutsu,
sensing, fuinjutsu, weapon techniques and chakra movement. Clan techniques and kekkei genkai are in
clans.py. Every technique: nature, rank, level, signs, chakra cost, cast time, cooldown, its
mechanic in Minecraft terms, counters, who teaches it, and the slice it arrives in.
"""

from common import RANK_COOLDOWN, RANK_COST, RANK_LEVEL, RANK_POWER, TICKS_PER_SIGN

COUNTERS_BY_NATURE = {
    "fire": "water jutsu (water beats fire), an earth or water wall, sidestep the slow projectile",
    "wind": "fire jutsu (fire beats and swallows wind), an earth wall, a heavy stance (poise)",
    "lightning": "wind jutsu (wind beats lightning), break line of sight, dodge on the charge",
    "earth": "lightning jutsu (lightning beats earth), jump the ground wave, flank the wall",
    "water": "earth jutsu (earth beats water), stay away from water (water jutsu cost more far from it)",
    "none": "dodge or interrupt the signs; walls block projectiles",
}


def T(tid, name, kind, nature, rank, signs, mc, *, level=None, cost=None, cost_mult=1.0, cast=None, cooldown=None, cd_mult=1.0,
      power=None, power_mult=1.0, shape=None, effects=None, counters=None, teach=None, slice_=None, requires=None, beta=False,
      tags=None, note=None, replaces=None):
    signs = signs.split() if isinstance(signs, str) else list(signs)
    t = {
        "id": "combat:" + tid, "name": name, "kind": kind, "nature": nature, "rank": rank,
        "level": level if level is not None else RANK_LEVEL[rank],
        "signs": signs,
        "chakra": cost if cost is not None else round(RANK_COST[rank] * cost_mult),
        "cast_ticks": cast if cast is not None else len(signs) * TICKS_PER_SIGN,
        "cooldown_ticks": cooldown if cooldown is not None else round(RANK_COOLDOWN[rank] * cd_mult),
        "power": power if power is not None else round(RANK_POWER[rank] * power_mult, 1),
        "shape": shape or {"type": "self"},
        "effects": effects or [],
        "mechanic": mc,
        "counters": counters or COUNTERS_BY_NATURE.get(nature if kind in ("ninjutsu", "weapon") else "none", COUNTERS_BY_NATURE["none"]),
        "teach": teach or [],
        "slice": slice_ or {"e": "beta1", "d": "beta2", "c": "beta2", "b": "chunin", "a": "jonin", "s": "road"}[rank],
    }
    if requires:
        t["requires"] = requires
    if beta:
        t["beta"] = True
    if tags:
        t["tags"] = tags
    if note:
        t["note"] = note
    if replaces:
        t["replaces"] = replaces
    return t


def proj(rng, speed, radius=0.5, **kw):
    s = {"type": "projectile", "range": rng, "speed": speed, "radius": radius}
    s.update(kw)
    return s


def area(radius, **kw):
    s = {"type": "area", "radius": radius}
    s.update(kw)
    return s


def cone(rng, degrees, **kw):
    s = {"type": "cone", "range": rng, "degrees": degrees}
    s.update(kw)
    return s


def line(rng, width, **kw):
    s = {"type": "line", "range": rng, "width": width}
    s.update(kw)
    return s


def touch(rng=3.0, **kw):
    s = {"type": "melee", "range": rng}
    s.update(kw)
    return s


def summon_entity(what, ticks, **kw):
    s = {"type": "entity", "entity": what, "ticks": ticks}
    s.update(kw)
    return s


def st(status, ticks=None, **kw):
    e = {"status": status}
    if ticks is not None:
        e["ticks"] = ticks
    e.update(kw)
    return e


INS = "mentor:role:instructor"
SEN = "mentor:role:sensei"
MED = "mentor:role:medic"
SCROLL = "scroll:scroll_shop"
CER = "ceremony:nature"


def nm(n):
    return "mentor:role:nature_master." + n


NEUTRAL = [
    T("nin.clone", "Clone Technique", "ninjutsu", "none", "e", "ram snake tiger",
      "Spawns 3 illusory copies of you (no hitbox) that run off in different directions for 100 ticks; each mob has a 60% chance to switch target to a copy",
      power=0, shape=summon_entity("illusory_clone", 100, count=3), effects=[st("decoy", 100, retarget_chance=0.6)],
      counters="sensing, Byakugan and Sharingan see through them; a hit pops a copy", teach=[INS], beta=True),
    T("nin.transformation", "Transformation", "ninjutsu", "none", "e", "dog boar ram",
      "Your render becomes a chosen resident's look (or an object's: a log, a crate) until you attack or take damage; mobs lose their target; residents do not recognize you",
      power=0, cooldown=100, effects=[st("disguised")], counters="sensing; a touch; dogs smell you", teach=["mentor:lessons"], beta=True),
    T("nin.substitution", "Substitution", "ninjutsu", "none", "e", "",
      "Dodge as a hit lands, with 10 chakra: blink back 5 blocks with 12 i-frames, a log entity takes the blow. Once per 20 s",
      cost=10, cast=0, cooldown=400, power=0, shape={"type": "self", "blink": 5}, effects=[st("iframes", 12)],
      counters="a second attack right after; sensing follows the blink", teach=["mentor:lessons"], beta=True,
      note="Timing-based, no signs (ROADMAP: dodge timing)"),
    T("nin.release", "Release", "genjutsu", "none", "e", "ram",
      "Breaks a genjutsu on yourself (weave Ram while caught); costs the illusion's strength in chakra",
      cost=5, power=0, cooldown=20, effects=[{"breaks": "genjutsu"}], counters="—", teach=[INS], beta=True),
    T("nin.rope_escape", "Rope Escape", "ninjutsu", "none", "e", "",
      "Passive: mashing movement escapes wire, rope and webs 40% faster", cost=0, cast=0, cooldown=0, power=0,
      counters="—", teach=[INS], slice_="beta1"),
    T("nin.first_aid", "Field First Aid", "medical", "none", "e", "",
      "Hold use on a downed or hurt ally for 60 ticks: heals 4 HP and stops bleeding (no chakra)", cost=0, cast=60, cooldown=200, power=0,
      shape=touch(2.0), effects=[{"heal": 4}, {"cleanse": ["bleeding"]}], counters="interrupted by any hit", teach=[MED], slice_="beta1", beta=True),
    T("nin.hiding_camouflage", "Hiding in Camouflage", "ninjutsu", "none", "d", "snake rat dog",
      "Standing still you take on the colour of the block behind you: hidden until you move faster than a walk or attack",
      level=6, power=0, cooldown=100, effects=[st("hidden")], counters="sensing; Byakugan; dogs; stepping within 3 blocks",
      teach=[SEN], slice_="beta2", beta=True),
    T("nin.body_flicker", "Body Flicker", "ninjutsu", "none", "d", "tiger",
      "A burst of speed: 8 blocks in 4 ticks in the facing direction, with a leaf swirl; can open a dash attack",
      level=8, cost=8, power=0, cooldown=80, shape={"type": "self", "dash": 8}, counters="area attacks where you land", teach=[SEN], beta=True),
    T("nin.shadow_clone", "Shadow Clone", "ninjutsu", "none", "b", "ram snake tiger ram",
      "Two to four real clone entities with basic combat AI and your taijutsu chain; each takes an equal share of your current chakra and pops after one hit",
      level=18, cost_mult=1.0, power=0, shape=summon_entity("shadow_clone", 600, count=2, max_count=4), counters="area attacks pop them all",
      teach=[SEN], slice_="chunin"),
    T("nin.multi_shadow_clone", "Multi Shadow Clone", "ninjutsu", "none", "a", "ram snake tiger ram tiger",
      "Up to twelve shadow clones (cap by chakra); they swarm a target or carry your signs for a squad combo",
      level=32, power=0, shape=summon_entity("shadow_clone", 600, count=8, max_count=12), counters="area jutsu", teach=[SEN], slice_="jonin"),
    T("nin.clone_explosion", "Clone Great Explosion", "ninjutsu", "none", "a", "ram snake tiger ram boar",
      "A shadow clone that explodes when it grabs or is hit: 3-block blast", level=34, power_mult=1.0,
      shape=summon_entity("shadow_clone", 400, explodes=True, radius=3), effects=[{"damage": "ninjutsu.none"}], teach=[SEN],
      requires=["combat:nin.shadow_clone"], slice_="jonin"),
    T("nin.spiral_sphere", "Spiralling Sphere", "ninjutsu", "none", "a", "",
      "No signs: hold use for 20 ticks to form a sphere of spinning chakra in your hand, then strike: a drilling hit that launches the target 10 blocks",
      level=32, cast=20, power_mult=1.1, shape=touch(3.0, charge=20), effects=[{"damage": "ninjutsu.none"}, st("knocked_down", 24, launch=10)],
      counters="it is melee: parry the arm, keep range, substitute", teach=[SEN], slice_="jonin", tags=["no_signs"]),
    T("nin.great_spiral_sphere", "Great Spiralling Sphere", "ninjutsu", "none", "s", "",
      "A sphere as big as a barrel (needs a shadow clone to help shape it, 30 ticks): 4-block blast on contact",
      level=44, cast=30, power_mult=1.0, shape=touch(3.5, charge=30, radius=4), effects=[{"damage": "ninjutsu.none"}, st("knocked_down", 30)],
      teach=[SEN], requires=["combat:nin.spiral_sphere", "combat:nin.shadow_clone"], tags=["no_signs"]),
    T("nin.chakra_threads", "Chakra Threads", "ninjutsu", "none", "b", "",
      "Invisible threads from the fingertips (12 blocks): pull a light enemy or an item, or steer a thrown weapon after release",
      level=24, cast=0, power=0, shape=line(12, 0.3), effects=[{"pull": 4}], teach=["mentor:role:weapon_master"], slice_="chunin", tags=["no_signs"]),
]

FIRE = [
    T("fire.ember_shot", "Fire: Ember Shot", "ninjutsu", "fire", "d", "tiger snake tiger",
      "A small fast fire bolt (2 blocks a tick, 20 range) that sets the target alight", level=8, shape=proj(20, 2.0),
      effects=[{"damage": "ninjutsu.fire"}, st("burning", 60)], teach=[SCROLL], slice_="beta2", beta=True),
    T("fire.great_fireball", "Fire: Great Fireball", "ninjutsu", "fire", "c", "snake ram monkey boar horse tiger",
      "A slow projectile 2 blocks wide (0.9 a tick, 20 range) that bursts in a 2.5-block radius and sets mobs alight; never sets blocks on fire",
      shape=proj(20, 0.9, 1.0, burst=2.5), effects=[{"damage": "ninjutsu.fire"}, st("burning", 80)], teach=[CER, nm("fire"), "clan:uchiha"],
      beta=True),
    T("fire.phoenix_flower", "Fire: Phoenix Sage Fire", "ninjutsu", "fire", "c", "rat tiger dog ox hare tiger",
      "Five small fireballs in a fan that curve gently toward the target (2 power each)", level=12, power=10,
      shape=proj(18, 1.4, 0.4, count=5, homing=0.15), effects=[{"damage": "ninjutsu.fire"}, st("burning", 40)], teach=[SCROLL, "exam_reward"],
      beta=True),
    T("fire.dragon_flame", "Fire: Dragon Flame", "weapon", "fire", "c", "snake dragon hare tiger",
      "Breathe fire along a wire you have strung or tethered: the flame runs the wire and engulfs a bound target", level=14, power_mult=1.2,
      shape=line(16, 0.6, needs="wire"), effects=[{"damage": "ninjutsu.fire"}, st("burning", 100)], teach=["mentor:role:weapon_master", "clan:uchiha"],
      slice_="beta3", requires=["item:wire_spool"]),
    T("fire.fire_dragon_bullet", "Fire: Fire Dragon Bullet", "ninjutsu", "fire", "b", "snake dragon rat ox horse dog tiger",
      "A dragon of flame that hunts its target (homing 0.3, 24 range)", level=20, shape=proj(24, 1.0, 0.8, homing=0.3),
      effects=[{"damage": "ninjutsu.fire"}, st("burning", 100)], teach=[nm("fire")]),
    T("fire.flame_wall", "Fire: Flame Wall", "ninjutsu", "fire", "b", "tiger ox dog rat",
      "A wall of fire 8 blocks wide for 160 ticks: blocks thrown weapons, burns anyone crossing; wind fed into it doubles its height", level=22,
      power_mult=0.6, shape=summon_entity("fire_wall", 160, width=8), effects=[{"damage": "ninjutsu.fire", "per": "crossing"}, st("burning", 80)],
      teach=[nm("fire")], counters="water jutsu put it out; go around"),
    T("fire.ash_pile_burning", "Fire: Ash Pile Burning", "ninjutsu", "fire", "b", "ram rat monkey boar horse tiger",
      "Exhale an ash cloud (6-block cone, blinded 40 ticks), then click the teeth: the ash ignites", level=24, power_mult=0.9,
      shape=cone(6, 60), effects=[st("blinded", 40), {"damage": "ninjutsu.fire", "delay": 20}], teach=[nm("fire"), "clan:sarutobi"],
      counters="wind blows the ash back; water soaks it"),
    T("fire.great_dragon_fire", "Fire: Great Dragon Fire", "ninjutsu", "fire", "a", "snake dragon rat ox horse dog tiger boar",
      "Several dragon heads of fire on one target area (radius 4)", shape=proj(26, 1.0, 1.5, burst=4), effects=[{"damage": "ninjutsu.fire"}, st("burning", 120)],
      teach=[nm("fire")]),
    T("fire.majestic_destroyer_flame", "Fire: Majestic Destroyer Flame", "ninjutsu", "fire", "a", "horse tiger snake ram monkey boar horse tiger",
      "A sweeping wall of flame in an 18-block, 70-degree cone", level=36, power_mult=1.1, shape=cone(18, 70),
      effects=[{"damage": "ninjutsu.fire"}, st("burning", 120)], teach=["mission:a"]),
    T("fire.great_fire_annihilation", "Fire: Great Fire Annihilation", "ninjutsu", "fire", "s", "snake ram monkey boar horse tiger dragon tiger",
      "A sea of fire (radius 12) and a cloud of smoke and heat overhead that lasts 400 ticks (a storm cloud for lightning users)",
      level=46, shape=area(12, centre="ahead", offset=8), effects=[{"damage": "ninjutsu.fire"}, st("burning", 160), {"leaves": "storm_cloud"}],
      teach=["scroll:forbidden_archive"]),
]

WIND = [
    T("wind.gale_palm", "Wind: Gale Palm", "ninjutsu", "wind", "d", "ram tiger",
      "Clap a blast of air: a 6-block gust that knocks back 3 and knocks thrown weapons out of the air", level=8, power_mult=0.8,
      shape=cone(6, 40), effects=[{"damage": "ninjutsu.wind"}, {"knockback": 3}, {"deflects": "projectiles"}], teach=[SCROLL], beta=True),
    T("wind.great_breakthrough", "Wind: Great Breakthrough", "ninjutsu", "wind", "c", "tiger ox dog hare snake",
      "A wind-charge gust: a 12-block, 50-degree blast that knocks back 5, deflects projectiles and blows smoke and mist away",
      power_mult=0.8, shape=cone(12, 50), effects=[{"damage": "ninjutsu.wind"}, {"knockback": 5}, {"deflects": "projectiles"}, {"clears": ["smoked", "mist"]}],
      teach=[CER, nm("wind")], beta=True),
    T("wind.vacuum_wave", "Wind: Vacuum Wave", "ninjutsu", "wind", "c", "tiger ox dog",
      "Spin and exhale: a 360-degree ring of slicing wind around you (radius 5)", level=14, shape=area(5),
      effects=[{"damage": "ninjutsu.wind"}, st("bleeding", 60)], teach=[SCROLL, "exam_reward"], beta=True),
    T("wind.blade_of_wind", "Wind: Blade of Wind", "ninjutsu", "wind", "b", "ox dog tiger ram",
      "An invisible blade along a line (12 blocks): cuts through guards (half the guard's reduction)", level=20, shape=line(12, 1.0, guard_pierce=0.5),
      effects=[{"damage": "ninjutsu.wind"}, st("bleeding", 80)], teach=[nm("wind")]),
    T("wind.vacuum_bullet", "Wind: Vacuum Bullets", "ninjutsu", "wind", "b", "dog ox hare tiger",
      "Three compressed air bullets in quick succession (fast, 24 range)", level=22, power=15, shape=proj(24, 2.2, 0.6, count=3, interval=4),
      effects=[{"damage": "ninjutsu.wind"}], teach=[nm("wind"), "clan:shimura"]),
    T("wind.pressure_damage", "Wind: Pressure Damage", "ninjutsu", "wind", "b", "tiger ox dog hare snake ram",
      "A huge compressed gust that hits like a wall: 14-block cone, knockback 8", level=26, power_mult=1.15, shape=cone(14, 60),
      effects=[{"damage": "ninjutsu.wind"}, {"knockback": 8}], teach=["mission:b"]),
    T("wind.sickle_weasel", "Wind: Sickle Weasel", "ninjutsu", "wind", "a", "",
      "Swing a great fan: a tornado of blades that walks 16 blocks forward (needs item:great_fan)", level=32, cast=10,
      shape=line(16, 3.0, travelling=True), effects=[{"damage": "ninjutsu.wind"}, st("bleeding", 100), st("airborne", 20)],
      teach=[nm("wind")], requires=["item:great_fan"], tags=["no_signs"]),
    T("wind.vacuum_great_sphere", "Wind: Vacuum Great Sphere", "ninjutsu", "wind", "a", "tiger ox dog hare snake ram horse",
      "One giant air bullet that tears through walls of earth and water", level=36, power_mult=1.15, shape=proj(28, 1.8, 1.5, pierces_barriers=True),
      effects=[{"damage": "ninjutsu.wind"}], teach=[nm("wind"), "clan:shimura"]),
    T("wind.spiral_shuriken", "Wind: Spiralling Shuriken", "ninjutsu", "wind", "s", "",
      "Add wind to the Spiralling Sphere and throw it: a shuriken of wind that bursts into a 6-block sphere of a million tiny blades",
      level=48, cast=40, power_mult=1.1, shape=proj(30, 1.2, 1.0, burst=6), effects=[{"damage": "ninjutsu.wind"}, st("bleeding", 200), {"self_damage": 0.05}],
      teach=[SEN], requires=["combat:nin.spiral_sphere:mastered"], tags=["no_signs"]),
]

LIGHTNING = [
    T("lightning.spark_needle", "Lightning: Spark Needle", "ninjutsu", "lightning", "d", "monkey dog",
      "A thin fast bolt (3 blocks a tick, 16 range): shocked 4 ticks", level=8, power_mult=0.8, shape=proj(16, 3.0, 0.3),
      effects=[{"damage": "ninjutsu.lightning"}, st("shocked", 4)], teach=[SCROLL], beta=True),
    T("lightning.stunning_palm", "Lightning: Stunning Palm", "ninjutsu", "lightning", "c", "ram ox monkey",
      "Charge a palm and strike (reach 3): shocked for 10 ticks, chains to one more enemy within 3 blocks", power_mult=0.9,
      cast=12, shape=touch(3.0, chain=1), effects=[{"damage": "ninjutsu.lightning"}, st("shocked", 10)], teach=[CER, nm("lightning")], beta=True),
    T("lightning.false_darkness", "Lightning: False Darkness", "ninjutsu", "lightning", "b", "monkey ox ram dog",
      "A spear of black lightning in a line (20 blocks) that pierces up to three targets", level=20, shape=line(20, 0.8, pierce=3),
      effects=[{"damage": "ninjutsu.lightning"}, st("shocked", 8)], teach=[nm("lightning")]),
    T("lightning.lightning_hound", "Lightning: Lightning Hound", "ninjutsu", "lightning", "b", "dog monkey dog",
      "A hound of lightning that runs the target down (homing 0.4); splits on a dodge", level=24, shape=proj(24, 1.4, 0.8, homing=0.4, splits=2),
      effects=[{"damage": "ninjutsu.lightning"}, st("shocked", 10)], teach=["mentor:role:clan_elder.hatake", nm("lightning")]),
    T("lightning.thunder_cage", "Lightning: Thunder Cage", "ninjutsu", "lightning", "b", "monkey ram dog ox",
      "A ring of crackling posts (radius 5) for 120 ticks: anyone touching its edge is shocked; you can stand inside", level=26,
      power_mult=0.5, shape=summon_entity("thunder_cage", 120, radius=5), effects=[st("shocked", 10)], teach=["mission:b"]),
    T("lightning.lightning_blade", "Lightning Blade", "ninjutsu", "lightning", "a", "ox hare monkey",
      "Charge 20 ticks (the hand crackles; you are slowed), then a straight dash of 12 blocks that breaks through a guard, a parry or a barrier",
      cast=32, power_mult=1.2, shape=line(12, 1.0, dash=True, breaks_guard=True, breaks_barriers=True),
      effects=[{"damage": "ninjutsu.lightning"}, st("shocked", 12)], teach=[SEN], counters="sidestep at the last moment; wind jutsu; a substitution"),
    T("lightning.armour", "Lightning: Armour", "ninjutsu", "lightning", "a", "monkey ox ram",
      "Shrouds the body in lightning (shrouded, 3 chakra a second): +30% speed and attack speed, physical damage taken -30%, opens Lightning Body",
      level=36, power=0, shape={"type": "self"}, effects=[st("shrouded", 400)], teach=[nm("lightning")]),
    T("lightning.kirin", "Lightning: Kirin", "ninjutsu", "lightning", "s", "monkey ox ram dog dragon",
      "Calls a bolt from a storm cloud onto the target, instantly (no projectile). Needs rain, a thunderstorm or a fire user's storm cloud",
      level=50, power_mult=1.3, shape={"type": "target", "range": 40, "instant": True}, effects=[{"damage": "ninjutsu.lightning"}, st("shocked", 20)],
      teach=["scroll:forbidden_archive"], requires=["weather:storm_cloud"], counters="be under a roof; a lightning rod (earth spire)"),
]

EARTH = [
    T("earth.headhunter", "Earth: Headhunter", "ninjutsu", "earth", "d", "boar dog",
      "Sink into the ground (hidden 40 ticks), then grab a target's ankles from below: bound 30 ticks, buried to the neck", level=8,
      shape=touch(2.0, from_below=True), effects=[{"damage": "physical.blunt"}, st("bound", 30)], teach=[SCROLL], beta=True,
      counters="jump; earth jutsu of your own; sensing shows where they are"),
    T("earth.mud_wall", "Earth: Mud Wall", "ninjutsu", "earth", "c", "tiger hare boar dog",
      "A short-lived wall entity 5 wide and 3 high for 160 ticks: blocks projectiles and jutsu that are not lightning", power=0,
      shape=summon_entity("earth_wall", 160, width=5, height=3, hp=30), effects=[{"blocks": "projectiles"}], teach=[CER, nm("earth")], beta=True,
      counters="lightning goes through; go around; Lightning Blade breaks it"),
    T("earth.mud_river", "Earth: Mud River", "ninjutsu", "earth", "c", "boar dog ram",
      "The ground turns to a sliding river of mud (10-block cone): knocked down and carried 4 blocks", level=12, power_mult=0.6,
      shape=cone(10, 45, ground=True), effects=[{"damage": "ninjutsu.earth"}, st("knocked_down", 24)], teach=[SCROLL, "exam_reward"], beta=True),
    T("earth.hardening", "Earth: Rock Skin", "ninjutsu", "earth", "b", "boar ox",
      "Harden the skin into stone for 200 ticks (hardened: physical damage taken x0.5, -20% speed); a close fighter's best friend", level=20,
      power=0, effects=[st("hardened", 200)], teach=[nm("earth")], counters="lightning; chakra damage (Gentle Fist)"),
    T("earth.stone_spears", "Earth: Stone Spears", "ninjutsu", "earth", "b", "dog rat ox",
      "Spikes of stone burst under the target (a 2-block circle, 20 range): launches", level=22, shape={"type": "target", "range": 20, "radius": 2, "telegraph_ticks": 10},
      effects=[{"damage": "ninjutsu.earth"}, st("airborne", 20)], teach=[nm("earth")]),
    T("earth.earth_dragon_bullet", "Earth: Earth Dragon Bullet", "ninjutsu", "earth", "b", "tiger ram boar horse snake",
      "A dragon of mud rises and spits mud balls (5 x 3 power); a fire ally turns them to lava bullets", level=24, power=15,
      shape=proj(22, 1.0, 0.8, count=5, interval=5), effects=[{"damage": "ninjutsu.earth"}], teach=[nm("earth")]),
    T("earth.flow_rampart", "Earth: Flowing Rampart", "ninjutsu", "earth", "a", "tiger snake dog boar ram",
      "A great wall 15 wide and 6 high for 300 ticks (hp 200): holds a gate, covers a squad", power=0,
      shape=summon_entity("earth_wall", 300, width=15, height=6, hp=200), teach=[nm("earth")]),
    T("earth.light_weight_rock", "Earth: Light-Weight Rock", "ninjutsu", "earth", "a", "boar ram",
      "Touch: make yourself light (+30% speed, double jump) or an enemy heavy (slow 0.5, cannot jump) for 200 ticks", level=36, power=0,
      shape=touch(3.0), effects=[{"either": [st("light", 200), st("heavy", 200)]}], teach=["mission:a"]),
    T("earth.earth_splitting", "Earth: Earth Splitting", "ninjutsu", "earth", "s", "boar dog ram tiger snake horse ox",
      "Slam the ground: a fissure runs 24 blocks (an entity effect; blocks never change), knocking down everything in its path", level=46,
      shape=line(24, 3.0, ground=True), effects=[{"damage": "ninjutsu.earth"}, st("knocked_down", 40)], teach=["scroll:forbidden_archive"]),
]

WATER = [
    T("water.water_bullet", "Water: Water Bullet", "ninjutsu", "water", "d", "ox ram",
      "A fast ball of water (2 blocks a tick, 18 range): soaked; puts out burning", level=8, shape=proj(18, 2.0, 0.5),
      effects=[{"damage": "ninjutsu.water"}, st("soaked", 100)], teach=[SCROLL], beta=True),
    T("water.wild_wave", "Water: Wild Water Wave", "ninjutsu", "water", "c", "tiger ox dog hare",
      "Spit a pushing wave (12-block cone): knockback 4, soaked, puts out fire", power_mult=0.8, shape=cone(12, 50),
      effects=[{"damage": "ninjutsu.water"}, {"knockback": 4}, st("soaked", 120), {"cleanses_area": "burning"}], teach=[CER, nm("water")], beta=True),
    T("water.water_wall", "Water: Water Wall", "ninjutsu", "water", "c", "tiger snake rat",
      "A spinning wall of water around you (radius 3) for 60 ticks: blocks fire and thrown weapons", level=12, power=0,
      shape=summon_entity("water_wall", 60, radius=3), effects=[{"blocks": "projectiles"}], teach=[SCROLL, "exam_reward"], beta=True,
      counters="earth breaks it; wait it out"),
    T("water.hiding_mist", "Water: Hiding Mist", "ninjutsu", "water", "c", "ram snake",
      "A thick mist (radius 12) for 400 ticks: everyone without sensing is smoked; your silent steps go unheard", level=14, power=0,
      shape=area(12), effects=[st("smoked", 400, area=True)], teach=[nm("water")], slice_="beta3",
      counters="wind blows it away; sensing; Byakugan"),
    T("water.water_prison", "Water: Water Prison", "ninjutsu", "water", "b", "snake ram ox monkey",
      "Trap a target within 3 blocks in a sphere of water: bound and cannot weave; you must keep a hand inside (you cannot move or attack)", level=20,
      power_mult=0.3, shape=touch(3.0, hold=True), effects=[st("bound", 160, no_signs=True), {"damage": "ninjutsu.water", "per_second": True}],
      teach=[nm("water")], counters="an ally hits the caster; lightning through the water hurts the prisoner"),
    T("water.water_clone", "Water: Water Clone", "ninjutsu", "water", "b", "ram snake tiger rat",
      "A clone of water with your taijutsu (30% of your health) near water; one far from water costs double", level=20, power=0,
      shape=summon_entity("water_clone", 600, count=1), teach=[nm("water")]),
    T("water.water_dragon", "Water: Water Dragon", "ninjutsu", "water", "b", "ox monkey hare rat boar bird ox horse",
      "A dragon of water crashes onto a 3-block area (homing 0.2); far from water it costs 50% more", level=24, power_mult=1.1,
      shape=proj(24, 1.1, 1.2, homing=0.2, burst=3), effects=[{"damage": "ninjutsu.water"}, st("soaked", 160)], teach=[nm("water")]),
    T("water.great_waterfall", "Water: Great Waterfall", "ninjutsu", "water", "a", "tiger ox dog hare snake ram bird",
      "A wall of water crashing outward (radius 10 around a point ahead), carrying enemies 8 blocks", shape=area(10, centre="ahead", offset=6),
      effects=[{"damage": "ninjutsu.water"}, {"knockback": 8}, st("soaked", 200)], teach=[nm("water")]),
    T("water.shark_bomb", "Water: Shark Bomb", "ninjutsu", "water", "a", "tiger ox ram bird snake",
      "A shark of water that hunts its target and grows by eating enemy chakra jutsu it meets", level=34, shape=proj(26, 1.3, 1.0, homing=0.35, eats_jutsu=True),
      effects=[{"damage": "ninjutsu.water"}, st("soaked", 160)], teach=["mission:a"]),
    T("water.thousand_sharks", "Water: Thousand Feeding Sharks", "ninjutsu", "water", "s", "tiger ox ram bird snake dragon",
      "A thousand sharks rise from a water surface (radius 14 around you; needs water within 8 blocks or a great waterfall first)",
      level=46, shape=area(14), effects=[{"damage": "ninjutsu.water"}, st("soaked", 200)], teach=["scroll:forbidden_archive"]),
]

GENJUTSU = [
    T("gen.false_surroundings", "Genjutsu: False Surroundings", "genjutsu", "none", "d", "snake ram",
      "The target sees the world shifted: its aim is off by 3 blocks for 100 ticks (a distorted screen for a player)", level=6, power=0,
      shape={"type": "target", "range": 12, "needs_sight": True}, effects=[st("genjutsu", 100, variant="shifted")], teach=["mentor:role:genjutsu_master"],
      counters="Release (Ram), a hit, an ally's touch; high will", beta=True),
    T("gen.hell_viewing", "Genjutsu: Hell Viewing", "genjutsu", "none", "d", "ram snake boar",
      "The target sees its worst fear: feared 60 ticks (flees or freezes); bosses only hesitate", level=8, power=0,
      shape={"type": "target", "range": 10, "needs_sight": True}, effects=[st("genjutsu", 60, variant="fear"), st("fear", 60)],
      teach=["mentor:role:genjutsu_master", "clan:kurama", "clan:yuhi"], counters="Release, high will", beta=True),
    T("gen.sly_mind", "Genjutsu: Sly Mind Affect", "genjutsu", "none", "c", "snake ram tiger",
      "A cone of illusion (8 blocks): those caught attack whoever is nearest for 60 ticks", level=12, power=0, shape=cone(8, 45),
      effects=[st("genjutsu", 60, variant="confusion"), st("confused", 60)], teach=["mentor:role:genjutsu_master", "exam_reward"], beta=True),
    T("gen.mist_servant", "Genjutsu: Mist Servant", "genjutsu", "none", "c", "ram monkey snake",
      "Phantom fighters rise around the target (fake entities only it sees) for 120 ticks: it swings at them and wastes its jutsu", level=14,
      power=0, shape={"type": "target", "range": 14, "needs_sight": True}, effects=[st("genjutsu", 120, variant="phantoms")],
      teach=["mentor:role:genjutsu_master"], slice_="beta3"),
    T("gen.bringer_of_darkness", "Genjutsu: Bringer of Darkness", "genjutsu", "none", "b", "ram tiger snake",
      "Total darkness in a 6-block radius for 100 ticks for everyone but you and your squad", level=20, power=0, shape=area(6),
      effects=[st("genjutsu", 100, variant="darkness"), st("blinded", 100)], teach=["mentor:role:genjutsu_master"]),
    T("gen.mirror_reversal", "Genjutsu: Mirror Reversal", "genjutsu", "none", "b", "ram monkey",
      "Held for 40 ticks: the next genjutsu cast on you turns back on its caster", level=24, power=0, cast=8,
      effects=[st("genjutsu_reflect", 40)], teach=["mentor:role:genjutsu_master", "clan:yuhi"]),
    T("gen.temple_of_nirvana", "Genjutsu: Temple of Nirvana", "genjutsu", "none", "a", "ram dog boar snake bird",
      "Feathers fall in a 10-block radius: drowsy, then asleep after 3 stacks (60 ticks each)", level=32, power=0, shape=area(10),
      effects=[st("genjutsu", 120, variant="feathers"), st("drowsy", 120, stacks=3)], teach=["mentor:role:genjutsu_master"]),
    T("gen.false_world", "Genjutsu: Sea of Ink", "genjutsu", "none", "s", "ram snake tiger ram bird dragon",
      "A whole-area illusion (radius 16, 200 ticks): enemies see the field rearranged and their own allies as you", level=46, power=0,
      shape=area(16), effects=[st("genjutsu", 200, variant="world"), st("confused", 200)], teach=["scroll:forbidden_archive"]),
]

MEDICAL = [
    T("med.mystical_palm", "Mystical Palm", "medical", "none", "c", "ram rat",
      "Hold use on an ally (or yourself at half rate): heals 1 HP a second per 10 control above 40, 2 chakra a second", level=12,
      cost=6, cast=8, cooldown=0, power=0, shape=touch(2.0, channel=True), effects=[{"heal_per_second": "control"}],
      teach=[MED], requires=["control:50"], slice_="beta3", counters="interrupted by any hit", beta=True),
    T("med.chakra_scalpel", "Chakra Scalpel", "medical", "none", "b", "",
      "Blades of chakra on the fingers (200 ticks): melee hits ignore armour and leave the target numbed (cut muscles)", level=20, cast=6,
      power=0, effects=[st("scalpel_hands", 200), {"on_hit": st("numbed", 100)}], teach=[MED], requires=["control:60"], tags=["no_signs"]),
    T("med.poison_extraction", "Poison Extraction", "medical", "none", "b", "ram ox",
      "Draws every poison out of an ally (60 ticks) and gives 400 ticks of immunity", level=22, cast=60, power=0, shape=touch(2.0),
      effects=[{"cleanse": ["poisoned", "numbed", "drowsy", "paralysed"]}], teach=[MED, "clan:suzuran"]),
    T("med.resuscitation", "Resuscitation", "medical", "none", "a", "ram snake ox",
      "Revive a downed squadmate at once with 40% health (once per fight per ally)", level=34, power=0, shape=touch(2.0),
      effects=[{"revive": 0.4}], teach=[MED]),
    T("med.hundred_healing", "Strength of a Hundred", "medical", "none", "s", "",
      "A seal stores chakra over days (1% a day, at most 100% of your max). Release it: heal 2 HP every tick-second for 20 s and no technique costs chakra",
      level=46, cast=10, power=0, effects=[st("hundred_seal", 400)], teach=[MED], requires=["control:90"], tags=["no_signs"]),
]

SENSING = [
    T("sense.chakra_sense", "Chakra Sensing", "sensing", "none", "c", "ram hare",
      "Close your eyes (still for 20 ticks): living things within 16 blocks glow through walls for 200 ticks, hidden and disguised ones too", level=12,
      cost=8, power=0, effects=[st("sensing", 200, radius=16)], teach=["mentor:role:sensor_master", "clan:yamanaka"], slice_="beta3", beta=True),
    T("sense.wide_sense", "Wide Sensing", "sensing", "none", "b", "ram dog",
      "48 blocks, and it reads each target's rank by its chakra's colour", level=24, power=0, effects=[st("sensing", 300, radius=48)],
      teach=["mentor:role:sensor_master"]),
    T("sense.chakra_reading", "Chakra Reading", "sensing", "none", "a", "ram dog snake",
      "Your target's chakra bar and the nature of its next technique show above its head for 200 ticks", level=32, power=0,
      effects=[st("read", 200)], teach=["mentor:role:sensor_master"]),
]

FUINJUTSU = [
    T("seal.binding_tag", "Sealing: Binding Tag", "fuinjutsu", "none", "d", "ram dragon",
      "Slap a sealing tag on a downed, stunned or bound enemy (needs item:sealing_tag): captured (a mission objective); bosses only bound 40 ticks",
      level=6, cost=8, power=0, shape=touch(2.0), effects=[{"capture": True}], teach=[SEN, SCROLL], requires=["item:sealing_tag"], beta=True),
    T("seal.tag_barrier", "Sealing: Four-Tag Barrier", "fuinjutsu", "none", "c", "ram snake ox dog",
      "Throw four tags around an area (radius 4): a barrier wall for 200 ticks that nobody crosses (protect or trap)", level=14, power=0,
      shape=summon_entity("barrier", 200, radius=4), teach=["mentor:role:fuinjutsu_master", "clan:uzumaki"], requires=["item:sealing_tag:4"],
      slice_="beta3", counters="Lightning Blade or a spiralling sphere breaks it; the tags can be shot down"),
    T("seal.storage_barrage", "Sealing: Storage Scroll Barrage", "weapon", "none", "b", "ram tiger dog",
      "Unroll a storage scroll: up to 20 stored weapons rain from above in a 4-block circle (uses your kunai and shuriken from it)", level=20,
      power=0, shape={"type": "target", "range": 20, "radius": 4}, effects=[{"weapon_rain": 20}], teach=["mentor:role:weapon_master"]),
    T("seal.chakra_suppression", "Sealing: Chakra Suppression", "fuinjutsu", "none", "b", "ram ox tiger",
      "A palm seal: the target cannot weave for 80 ticks (chakra sealed)", level=22, power=0, shape=touch(2.5), effects=[st("chakra_sealed", 80)],
      teach=["mentor:role:fuinjutsu_master", "clan:uzumaki"]),
    T("seal.five_elements", "Sealing: Five Elements Seal", "fuinjutsu", "none", "a", "ram tiger ox dog snake",
      "Five fingertips of fire: the target's nature jutsu are sealed for 400 ticks (taijutsu and genjutsu still work)", level=34, power=0,
      shape=touch(2.5), effects=[st("nature_sealed", 400)], teach=["mentor:role:fuinjutsu_master"]),
    T("seal.marked_teleport", "Sealing: Marked Teleport", "fuinjutsu", "none", "s", "",
      "Throw a marked kunai (up to 3 marks): press Weave to teleport to any mark in sight, instantly", level=48, cast=0, cooldown=40,
      cost=15, power=0, effects=[{"teleport_to": "mark"}], teach=["scroll:forbidden_archive"], requires=["item:kunai"], tags=["no_signs"]),
]

WEAPON_JUTSU = [
    T("weapon.tag_kunai", "Exploding-Tag Kunai", "weapon", "none", "d", "",
      "With a paper bomb in the pouch, the throw key on a kunai throws it tagged: it sticks, then bursts (radius 3, fuse 20) or on Ram", level=6,
      cost=0, cast=0, cooldown=10, power=8, shape=proj(24, 1.8, 0.3, burst=3), effects=[{"damage": "physical.blunt"}],
      teach=[SEN, "mentor:role:weapon_master"], requires=["item:kunai", "item:paper_bomb"], beta=True, tags=["no_signs"],
      counters="knock the kunai down; substitution; wind blows it off course"),
    T("weapon.shadow_shuriken", "Shadow Shuriken", "weapon", "none", "d", "",
      "Throw one shuriken with a second hidden in its shadow: a dodge of the first meets the second", level=7, cost=3, cast=0, cooldown=40,
      power=5, shape=proj(22, 2.4, 0.3, hidden_second=True), effects=[{"damage": "physical.pierce"}], teach=["mentor:role:weapon_master"],
      requires=["item:shuriken:2"], beta=True, tags=["no_signs"]),
    T("weapon.manipulated_shuriken", "Manipulated Shuriken", "weapon", "none", "c", "",
      "Shuriken on chakra threads: up to five curve to the target around cover (homing 0.4)", level=12, cost=8, cast=4, power=10,
      shape=proj(24, 2.0, 0.3, count=5, homing=0.4), effects=[{"damage": "physical.pierce"}], teach=["mentor:role:weapon_master", "exam_reward"],
      requires=["item:shuriken:5"], beta=True, tags=["no_signs"]),
    T("weapon.windmill_triple", "Windmill Triple Attack", "weapon", "none", "c", "",
      "Three windmill shuriken on wire: they wrap and bind the target (bound 60 ticks), then fire can run the wires", level=16, cost=10, cast=6,
      power=8, shape=proj(24, 1.6, 0.5, count=3), effects=[{"damage": "physical.slash"}, st("bound", 60)], teach=["mentor:role:weapon_master", "clan:uchiha"],
      requires=["item:shuriken_fuma", "item:wire_spool"], slice_="chunin", tags=["no_signs"]),
    T("weapon.wind_shuriken", "Wind-Channelled Shuriken", "weapon", "wind", "c", "ram horse",
      "Wind chakra on a thrown shuriken: double damage, pierces two targets, range 32", level=12, cost=8, power=5,
      shape=proj(32, 2.6, 0.4, pierce=2), effects=[{"damage": "ninjutsu.wind"}], teach=[nm("wind"), "exam_reward"], requires=["item:shuriken"],
      beta=True, note="Weapon-plus-jutsu combo: scales with both the weapons and ninjutsu pillars (the average)"),
    T("weapon.lightning_flow", "Lightning Flow Blade", "weapon", "lightning", "c", "monkey",
      "Lightning in the held blade for 200 ticks: every hit shocks (4 ticks) and reach +0.5", level=12, cost=10, power=0,
      effects=[st("blade_flow.lightning", 200)], teach=[nm("lightning"), "exam_reward"], beta=True),
    T("weapon.fire_flow", "Fire Flow Blade", "weapon", "fire", "c", "tiger rat",
      "Fire in the held blade for 200 ticks: every hit sets alight", level=14, cost=10, power=0, effects=[st("blade_flow.fire", 200)],
      teach=[nm("fire"), "clan:sarutobi"], slice_="beta3"),
    T("weapon.wind_flow", "Wind Flow Blade", "weapon", "wind", "c", "ram bird",
      "Wind in the held blade for 200 ticks: reach +1.5 and armour pierce 0.5", level=14, cost=10, power=0, effects=[st("blade_flow.wind", 200)],
      teach=[nm("wind")], slice_="beta3"),
    T("weapon.earth_flow", "Earth Flow Blade", "weapon", "earth", "c", "boar",
      "Earth in the held weapon for 200 ticks: poise damage x2", level=14, cost=10, power=0, effects=[st("blade_flow.earth", 200)],
      teach=[nm("earth")], slice_="beta3"),
    T("weapon.water_flow", "Water Flow Blade", "weapon", "water", "c", "ox",
      "Water on the held weapon for 200 ticks: soaked on hit and knockback +1", level=14, cost=10, power=0, effects=[st("blade_flow.water", 200)],
      teach=[nm("water")], slice_="beta3"),
    T("weapon.kunai_barrage", "Explosive Kunai Barrage", "weapon", "none", "b", "ram boar",
      "Throw six tagged kunai in a fan; they burst together on Ram", level=22, cost=10, cast=8, power=18,
      shape=proj(24, 1.8, 0.3, count=6, burst=3), effects=[{"damage": "physical.blunt"}], teach=["mentor:role:weapon_master"],
      requires=["item:kunai:6", "item:paper_bomb:6"]),
    T("weapon.rising_twin_dragons", "Rising Twin Dragons", "weapon", "none", "b", "ram rat ox",
      "Two storage scrolls spiral up around you and you rain their weapons down (30 projectiles over 40 ticks)", level=26, power_mult=1.1,
      shape={"type": "target", "range": 20, "radius": 6}, effects=[{"weapon_rain": 30}], teach=["mentor:role:weapon_master"],
      requires=["combat:seal.storage_barrage"]),
    T("weapon.shuriken_shadow_clone", "Shuriken Shadow Clone", "weapon", "none", "a", "ram rat tiger",
      "One thrown shuriken becomes a storm of up to 40 real copies", level=34, shape=proj(28, 2.4, 0.3, count=40, spread=40),
      effects=[{"damage": "physical.pierce"}], teach=[SEN], requires=["combat:nin.shadow_clone", "item:shuriken"]),
]

MOVEMENT = [
    {"id": "combat:move.ninja_run", "name": "Ninja run", "slice": "beta2", "chakra_per_second": 0, "effect": "+15% sprint speed, arms back",
     "teach": [SEN], "control": 0},
    {"id": "combat:move.roof_hop", "name": "Roof and tree hopping", "slice": "beta1", "chakra": 1,
     "effect": "a forward boost off leaves, logs and roofs (Beta 1 roof running at night, full hopping in Beta 2)", "teach": [INS]},
    {"id": "combat:move.chakra_jump", "name": "Chakra jump", "slice": "beta2", "chakra": "2 to 6 by charge",
     "effect": "hold jump to charge, up to 3x height; no fall damage while chakra lasts", "teach": [SEN]},
    {"id": "combat:move.tree_walk", "name": "Tree walking", "slice": "beta2", "chakra_per_second": 1,
     "effect": "walk up trunks and walls; control +10 on first mastery", "teach": [SEN], "trial": "Ch 10 at Training Ground 3"},
    {"id": "combat:move.wall_run", "name": "Wall-running", "slice": "beta2", "chakra_per_second": 1.5,
     "effect": "along or up a wall for up to 3 s (+1 s at control 60, +2 at 90)", "teach": [SEN]},
    {"id": "combat:move.water_walk", "name": "Water-walking", "slice": "beta2", "chakra_per_second": 0.5,
     "effect": "stand on water (a mixin on canStandOnFluid); sneak to sink; a hit that staggers you dunks you", "teach": [SEN], "trial": "Ch 12"},
    {"id": "combat:move.air_step", "name": "Air step", "slice": "chunin", "chakra": 4, "effect": "a second jump in the air", "teach": [SEN]},
    {"id": "combat:move.wind_glide", "name": "Wind glide", "slice": "jonin", "chakra_per_second": 2, "nature": "wind",
     "effect": "a slow fall with steering, like an elytra at a third of the speed", "teach": [nm("wind")]},
    {"id": "combat:move.silent_step", "name": "Silent step", "slice": "beta2", "chakra_per_second": 0.3,
     "effect": "footsteps make no noise for the AI's hearing (Tobari: free at night)", "teach": [SEN]},
]

CATALOGUE = NEUTRAL + FIRE + WIND + LIGHTNING + EARTH + WATER + GENJUTSU + MEDICAL + SENSING + FUINJUTSU + WEAPON_JUTSU

GENJUTSU_RULES = {
    "effect_type": "genjutsu",
    "how": "Genjutsu is one shared effect: a caught target sees a client-side illusion (fake entities, a distorted screen, a wrong HUD) chosen by the technique's variant, and moves at 60% speed",
    "strength": "power = caster's ninjutsu pillar x (1 + 0.1 clan bonus); duration x (1 - will / (will + 40))",
    "breaks": ["the target weaves Release (Ram): costs chakra equal to 10 + the illusion's rank cost / 2",
               "damage over 10% of max health", "a teammate's touch (interact with them)", "a flash bomb", "the Sharingan (stage 2) breaks any it sees cast"],
    "needs_sight": "most genjutsu need the target to see the caster (look away to avoid; blinded targets are immune)",
    "ai": "caught enemies attack phantoms, flee or stand; a caught boss spends its next phase transition breaking it",
    "players": "on the player, genjutsu is drawn as a screen effect and fake mobs; HUD text flickers; it never takes control of the camera for more than 2 s",
    "variants": ["shifted", "fear", "confusion", "phantoms", "darkness", "feathers", "world", "painted", "binding", "eyes"],
}

MEDICAL_RULES = {
    "who": "anyone with control 50 who trains with the medic (Beta 3); medical ninja are a role in the squad (Progression's squad roles)",
    "healing": "Mystical Palm heals by control; healing a squadmate raises their bond (a shared experience)",
    "revive": "downed squadmates (knocked out, never killed) can be revived by First Aid (slowly) or Resuscitation (at once)",
}

SENSING_RULES = {
    "what": "Sensing shows living things through walls (the glowing effect), reveals hidden and disguised ones, and counters smoke, mist and clones",
    "who": "sensors: Yamanaka (clan), anyone trained by the sensor master; Byakugan and Inuzuka smell are clan variants",
    "ai": "enemy sensors (scout_sensor) are why stealth needs Tobari, mist or distance",
}

FUINJUTSU_RULES = {
    "what": "Fuinjutsu uses sealing tags: capture, barriers, chakra seals, storage scrolls and marks",
    "who": "the fuinjutsu master and the Uzumaki (sealing costs -20% for them)",
    "never": "seals never change the map; barriers are short-lived entities",
}

CHAKRA_MOVEMENT_RULES = {
    "how": "client-side movement with the server checking and charging chakra (ROADMAP)",
    "control": "control lengthens wall-runs, lowers per-second costs (x(1.2 - control/250)) and lets you fight while water-walking",
    "combat": "staggered while tree-walking or wall-running: you fall; while water-walking: you sink for 20 ticks",
}
