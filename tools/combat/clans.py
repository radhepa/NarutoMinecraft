"""Clan techniques and kekkei genkai for all 25 clans, in four tiers by rank, plus each clan's
passives, its suggested nature and the lesser technique a clanless friend can learn.

Tier 1 at Genin (Beta 2, level 10 to 12: clan-born players from the clan elder in Ch 12),
tier 2 at Chunin (level 20), tier 3 at Jonin (level 32), tier 4 on the road to Hokage (level 44).
Kekkei genkai come only through clan membership. Lesser techniques: clanless players (and members
of other clans) learn one per friendly clan at clan friendship 7 (BONDS.md clan_friendship).
"""

from techniques import T, area, cone, line, proj, st, summon_entity, touch

TIER_RANK = {1: "c", 2: "b", 3: "a", 4: "s"}
TIER_LEVEL = {1: 10, 2: 20, 3: 32, 4: 44}
TIER_SLICE = {1: "beta2", 2: "chunin", 3: "jonin", 4: "road"}


def ct(clan, tier, key, name, signs, mc, *, kind="clan", nature="none", kg=False, **kw):
    kw.setdefault("level", TIER_LEVEL[tier])
    kw.setdefault("slice_", TIER_SLICE[tier])
    kw.setdefault("teach", ["mentor:role:clan_elder." + clan])
    t = T(clan + "." + key, name, "kekkei_genkai" if kg else kind, nature, TIER_RANK[tier], signs, mc, **kw)
    t["clan"] = clan
    t["tier"] = tier
    return t


def lesser(clan, key, name, signs, mc, **kw):
    kw.setdefault("level", 12)
    kw.setdefault("slice_", "beta2" if clan in WAVE1 else "beta2_5")
    kw.setdefault("teach", ["clan_friendship:" + clan + ":7"])
    t = T(clan + "." + key, name, "clan_lesser", kw.pop("nature", "none"), "c", signs, mc, **kw)
    t["clan"] = clan
    t["lesser"] = True
    return t


# The eight great clans' welcome quests land in Beta 2 (wave 1); the rest in Beta 2.5 (SIDE_QUESTS.md).
WAVE1 = ["senju", "uzumaki", "uchiha", "hyuga", "nara", "akimichi", "yamanaka", "inuzuka"]

CLANS = []


def clan(cid, name, standing, nature, passives, techniques, lesser_tech=None, kekkei=None, style=None, notes=None):
    c = {"id": cid, "clan": "clan:" + cid, "name": name, "standing": standing, "suggested_nature": nature,
         "passives": passives, "techniques": techniques}
    if lesser_tech:
        c["lesser"] = lesser_tech
    if kekkei:
        c["kekkei_genkai"] = kekkei
    if style:
        c["style"] = style
    if notes:
        c["notes"] = notes
    CLANS.append(c)


clan("senju", "Senju", "noble", ["earth", "water"],
     {"health_regen_mult": 1.2, "chakra_mult": 1.1},
     [ct("senju", 1, "binding_roots", "Wood: Binding Roots", "snake ram boar", kg=True, nature="earth",
         mc="Roots burst from the ground under a target within 14 blocks (entities, gone after 80 ticks): bound 60 ticks",
         shape={"type": "target", "range": 14, "radius": 1.5}, effects=[st("bound", 60)], power_mult=0.5, beta=True),
      ct("senju", 2, "wooden_barrier", "Wood: Wooden Barrier", "snake ram tiger dog", kg=True, nature="earth",
         mc="A dome of interlocking timber around you and allies within 3 blocks for 160 ticks (hp 120)", power=0,
         shape=summon_entity("wood_dome", 160, radius=3, hp=120)),
      ct("senju", 3, "wood_clone", "Wood: Wood Clone", "snake ram tiger ram", kg=True, nature="earth",
         mc="A clone of wood that keeps fighting until destroyed (50% of your health) and can bind on death", power=0,
         shape=summon_entity("wood_clone", 1200, count=1)),
      ct("senju", 4, "deep_forest_bloom", "Wood: Deep Forest Bloom", "snake ram tiger dog boar horse", kg=True, nature="earth",
         mc="A forest rises in a 14-block circle for 300 ticks (entities): every enemy inside is bound for 60 ticks and drained of 1 chakra a second",
         shape=area(14), effects=[st("bound", 60), {"drain_chakra_per_second": 1}])],
     lesser_tech=lesser("senju", "vitality_breath", "Senju Vitality Breathing", "ram rat hare",
                        "A breathing form: regenerate 0.5 HP a second for 200 ticks while not attacking", power=0, effects=[{"heal_per_second": 0.5, "ticks": 200}]),
     kekkei={"name": "Wood Release", "stages": [
         {"stage": 1, "slice": "beta2", "gives": "combat:senju.binding_roots"},
         {"stage": 2, "slice": "chunin", "gives": "combat:senju.wooden_barrier"},
         {"stage": 3, "slice": "jonin", "gives": "combat:senju.wood_clone"},
         {"stage": 4, "slice": "road", "gives": "combat:senju.deep_forest_bloom"}]})

clan("uzumaki", "Uzumaki", "noble", ["wind", "water"],
     {"chakra_mult": 1.3, "extra_hearts": 1, "fuinjutsu_cost_mult": 0.8},
     [ct("uzumaki", 1, "sealing_chains", "Sealing Chains", "ram rat horse",
         mc="Chains of chakra burst from your back and hold one target within 10 blocks for 80 ticks; it cannot weave", power_mult=0.3,
         shape=line(10, 0.5), effects=[st("bound", 80, no_signs=True)], beta=True),
      ct("uzumaki", 2, "chain_fence", "Chain Fence", "ram tiger dog ox",
         mc="A fence of chains (radius 6) for 200 ticks: nobody crosses; you can reach through it", power=0,
         shape=summon_entity("chain_fence", 200, radius=6)),
      ct("uzumaki", 3, "vitality_seal", "Vitality Seal", "ram rat ram",
         mc="A seal on your chest for the fight: the first lethal blow leaves you at 1 HP and heals 30% over 5 s", power=0,
         effects=[st("vitality_seal", 6000)]),
      ct("uzumaki", 4, "chain_cage", "Adamantine Chain Cage", "ram tiger dog ox boar",
         mc="Chains from every direction: up to six targets in 14 blocks bound for 100 ticks and their chakra sealed", power_mult=0.4,
         shape=area(14, max_targets=6), effects=[st("bound", 100), st("chakra_sealed", 100)])],
     lesser_tech=lesser("uzumaki", "seal_basics", "Uzumaki Seal Basics", "ram rat dragon",
                        "Your sealing tags and fuinjutsu cost 20% less and binding tags hold bosses 20 ticks longer", power=0, cast=0))

clan("uchiha", "Uchiha", "noble", ["fire"],
     {"control_bonus": 5, "fire_power": 0.05},
     [ct("uchiha", 1, "phoenix_shuriken", "Fire: Phoenix Flower with hidden shuriken", "rat tiger dog ox hare tiger", nature="fire", replaces="combat:fire.phoenix_flower",
         mc="Phoenix Sage Fire with a shuriken hidden in each flame: blocking the fire still lets the steel through", power=14,
         shape=proj(18, 1.4, 0.4, count=5, homing=0.15), effects=[{"damage": "ninjutsu.fire"}, {"damage": "physical.pierce", "per": 1.5}], beta=True),
      ct("uchiha", 2, "dragon_flame_triple", "Dragon Flame Triple", "snake dragon hare tiger", nature="fire", replaces="combat:fire.dragon_flame",
         mc="Windmill Triple's wires, then Dragon Flame down all three", requires=["combat:weapon.windmill_triple"],
         shape=line(16, 1.0, needs="wire"), effects=[{"damage": "ninjutsu.fire"}, st("burning", 120)]),
      ct("uchiha", 3, "eye_genjutsu", "Sharingan Genjutsu", "", kg=True,
         mc="Meet a target's eyes within 8 blocks: genjutsu (binding) for 80 ticks; needs Sharingan stage 3", power=0, cast=4,
         shape={"type": "target", "range": 8, "needs_eye_contact": True}, effects=[st("genjutsu", 80, variant="eyes"), st("bound", 80)],
         tags=["no_signs"]),
      ct("uchiha", 4, "flame_storm", "Fire: Flame Storm", "snake ram monkey boar horse tiger dragon", nature="fire",
         mc="A spinning column of fire around you (radius 8) for 60 ticks that drags enemies in", shape=area(8),
         effects=[{"damage": "ninjutsu.fire"}, st("burning", 160), {"pull": 2}])],
     lesser_tech=lesser("uchiha", "fire_breath", "Uchiha Fire Breath", "snake tiger",
                        "Your fire jutsu cost 10% less and Great Fireball bursts 0.5 blocks wider (needs fire nature)", power=0, cast=0, nature="fire"),
     kekkei={"name": "Sharingan", "awakening": "Beta 3, Ch 16 for a clan-born player (a story moment); stages by rank",
             "stages": [
                 {"stage": 1, "slice": "beta3", "tomoe": 1, "gives": "enemy telegraphs flash 6 ticks earlier; chakra 1 a second while active"},
                 {"stage": 2, "slice": "chunin", "tomoe": 2, "gives": "parry window doubled; genjutsu it sees cast is broken at once"},
                 {"stage": 3, "slice": "jonin", "tomoe": 3, "gives": "copy: a jutsu you watch an enemy cast (and survive) is learnable; Sharingan Genjutsu"},
                 {"stage": 4, "slice": "never", "note": "No further stages in the game unless the story bible adds one"}],
             "key": "toggle with the Eye key (B), 1 chakra a second"})

clan("hyuga", "Hyuga", "noble", [],
     {"control_bonus": 15},
     [ct("hyuga", 1, "gentle_fist", "Gentle Fist", "", mc="Opens the Gentle Fist style (palms drain chakra and close points; see styles)",
         cast=0, cost=0, power=0, effects=[{"style": "combat:style.gentle_fist"}], tags=["no_signs"], beta=True),
      ct("hyuga", 2, "palm_rotation", "Eight Trigrams Palm Rotation", "", kg=True,
         mc="A spinning dome of chakra (radius 3): deflects every projectile and jutsu that is not S-rank, knocks back, 10 i-frames",
         cast=2, cooldown=120, cost=15, power_mult=0.3, shape=area(3), effects=[{"deflects": "all"}, {"knockback": 3}], tags=["no_signs"]),
      ct("hyuga", 3, "vacuum_palm_barrage", "Eight Trigrams Vacuum Palm Barrage", "", kg=True,
         mc="Rapid air palms at range (8 blocks): six pressure hits that close chakra points", cast=4, power_mult=0.9,
         shape=proj(8, 3.0, 0.8, count=6, interval=2), effects=[{"damage": "chakra"}, {"closes_points": 12}], tags=["no_signs"]),
      ct("hyuga", 4, "protection_64", "Eight Trigrams Sixty-Four Palms Protection", "", kg=True,
         mc="A wall of palms around you for 60 ticks: every attack entering 3 blocks is struck down and its attacker hit", cast=4,
         shape=area(3), effects=[{"deflects": "all"}, {"damage": "chakra"}], tags=["no_signs"])],
     lesser_tech=lesser("hyuga", "trigram_stance", "Eight Trigrams Stance", "",
                        "A defensive stance: guard reduction +10% and parry window +1 tick while you hold still", power=0, cast=0, tags=["no_signs"]),
     kekkei={"name": "Byakugan", "stages": [
         {"stage": 1, "slice": "beta2", "gives": "sight through walls within 16 blocks (living things glow); 1 chakra a second"},
         {"stage": 2, "slice": "chunin", "gives": "32 blocks; see chakra points: Gentle Fist palms crit to the back"},
         {"stage": 3, "slice": "jonin", "gives": "50 blocks and near-360 sight: no back-attack bonus against you"},
         {"stage": 4, "slice": "road", "gives": "see an enemy's chakra flow: its next technique's nature and target shown"}],
         "key": "toggle with the Eye key (B)"},
     style="combat:style.gentle_fist")

clan("nara", "Nara", "noble", [],
     {"control_bonus": 10, "strategist": "enemy cooldowns are shown above their heads"},
     [ct("nara", 1, "shadow_possession", "Shadow Possession", "rat",
         mc="A shadow line crawls along the ground (0.6 a tick) to a target within 12 blocks; if it reaches, the target copies your movement for 100 ticks. Needs light: half range at night and indoors",
         power=0, cast=8, shape=line(12, 0.5, ground=True, speed=0.6, needs_light=True), effects=[st("possessed", 100)],
         counters="jump over the line, stay out of light, break line of sight", beta=True),
      ct("nara", 2, "shadow_neck_bind", "Shadow Neck Bind", "rat ox",
         mc="While possessing: a shadow hand climbs to the throat, 1.5 power a second", requires=["combat:nara.shadow_possession"],
         power_mult=0.6, effects=[{"damage": "physical.blunt", "per_second": True}]),
      ct("nara", 3, "shadow_sewing", "Shadow Sewing", "rat ox dog",
         mc="Shadow needles pierce up to four targets within 12 blocks and pin them (bound 60 ticks)", shape=area(12, max_targets=4),
         effects=[{"damage": "physical.pierce"}, st("bound", 60)]),
      ct("nara", 4, "shadow_gathering", "Shadow Gathering", "rat ox dog snake",
         mc="Possess every enemy within 16 blocks for 120 ticks", shape=area(16), effects=[st("possessed", 120)], power=0)],
     lesser_tech=lesser("nara", "shadow_stitch", "Shadow Stitch", "rat",
                        "A short shadow (6 blocks) that pins one target's feet for 30 ticks", power=0, cast=8,
                        shape=line(6, 0.5, ground=True), effects=[st("bound", 30)]))

clan("akimichi", "Akimichi", "noble", [],
     {"extra_hearts": 2, "poise_bonus": 15, "stamina_bonus": 20, "food_buffs_mult": 1.5},
     [ct("akimichi", 1, "expansion", "Expansion", "ram rat monkey",
         mc="Vanilla's scale attribute: grow to 2x for 200 ticks: reach x1.6, knockback x2, poise x2 (expanded); opens Human Boulder", power=0,
         effects=[st("expanded", 200)], beta=True),
      ct("akimichi", 2, "partial_expansion", "Partial Expansion", "ram rat bird",
         mc="One arm grows: a slap that covers 4 blocks and a grab that holds a target 40 ticks", power_mult=1.0, cast=8, shape=touch(5.0, area=4),
         effects=[{"damage": "physical.blunt"}, st("bound", 40)]),
      ct("akimichi", 3, "super_expansion", "Super Expansion", "ram boar ox",
         mc="Grow to 3x (the cap; the map never breaks) for 160 ticks; body slams knock everything in 5 blocks down", power=0,
         effects=[st("expanded", 160, scale=3.0)]),
      ct("akimichi", 4, "calorie_wings", "Calorie Control: Butterfly", "ram boar ox dog",
         mc="Burn the body's stores: butterfly wings of chakra for 300 ticks, all damage x2 and speed +40%; afterwards gate strain",
         power=0, effects=[st("butterfly", 300)])],
     lesser_tech=lesser("akimichi", "hearty_meal", "Akimichi Hearty Meal", "",
                        "Leaf dishes give you the Akimichi's 1.5x food buffs", power=0, cast=0, tags=["no_signs"]),
     style="combat:style.iron_body",
     notes="The three coloured pills (spinach, curry, chili) are tier 3 and 4 consumables: items session ids item:akimichi_pill_green/yellow/red")

clan("yamanaka", "Yamanaka", "noble", [],
     {"control_bonus": 10, "sensing_radius_bonus": 4},
     [ct("yamanaka", 1, "mind_disturbance", "Mind Body Disturbance", "ram rat dog",
         mc="A pulse into one target within 10 blocks: for 60 ticks it attacks its own allies (confused)", power=0,
         shape={"type": "target", "range": 10}, effects=[st("confused", 60)], beta=True),
      ct("yamanaka", 2, "mind_transfer", "Mind Transfer", "ram rat boar",
         mc="Your camera moves into a mob or resident for 160 ticks and you steer it; your body slumps and can be hit (damage to it ends the jutsu)",
         power=0, cast=20, shape={"type": "target", "range": 12, "projectile_speed": 0.6}, effects=[st("mind_transferred", 160)],
         counters="sidestep the slow mind projectile; hit the slumped body", note="The hardest technique to build (ROADMAP)"),
      ct("yamanaka", 3, "mind_link", "Mind Link", "ram snake dog",
         mc="Links your squad's minds for 600 ticks: sensing is shared, commands are instant, cohesion counts 10 higher", power=0,
         effects=[st("mind_link", 600)]),
      ct("yamanaka", 4, "mind_destruction", "Mind Destruction", "ram snake tiger dog",
         mc="Up to four targets in 12 blocks: confused for 120 ticks and their next technique fizzles", shape=area(12, max_targets=4),
         power=0, effects=[st("confused", 120), {"fizzle_next": True}])],
     lesser_tech=lesser("yamanaka", "flower_sense", "Flower Sense", "ram rat snake",
                        "Sensing within 10 blocks for 100 ticks (a lesser Chakra Sensing)", cost=6, power=0, effects=[st("sensing", 100, radius=10)]))

clan("inuzuka", "Inuzuka", "noble", [],
     {"move_speed": 0.05, "stamina_bonus": 10, "smell": "track a marked or hidden target within 24 blocks", "ninken": "a ninken partner from the clinic (VF pet code)"},
     [ct("inuzuka", 1, "fang_over_fang", "Fang over Fang", "",
         mc="You and your ninken become spinning drills (a 10-block dash attack each, side by side)", cast=6, power_mult=1.1,
         shape=line(10, 1.5, dash=True), effects=[{"damage": "physical.slash"}, st("knocked_down", 20)], tags=["no_signs"], beta=True),
      ct("inuzuka", 2, "dynamic_marking", "Dynamic Marking", "",
         mc="Your ninken marks a target: marked for 600 ticks (visible through walls) and Fang over Fang homes on it", cast=4, power=0,
         effects=[st("marked", 600)], tags=["no_signs"]),
      ct("inuzuka", 3, "tunnelling_fang", "Tunnelling Fang", "",
         mc="A single drill so fast it bores through guards and barriers", cast=8, shape=line(14, 1.5, dash=True, breaks_guard=True),
         effects=[{"damage": "physical.slash"}], tags=["no_signs"]),
      ct("inuzuka", 4, "twin_wolf", "Twin-Headed Wolf", "ram ox rat",
         mc="You and your ninken become a giant two-headed wolf for 300 ticks (expanded 2.5x, claws only)", power=0,
         effects=[st("expanded", 300, scale=2.5), {"style": "combat:style.beast_fang"}])],
     lesser_tech=lesser("inuzuka", "keen_nose", "Keen Nose", "",
                        "Your pet ninken (if you have one) can track hidden enemies within 16 blocks in a fight", power=0, cast=0, tags=["no_signs"]),
     style="combat:style.beast_fang")

clan("sarutobi", "Sarutobi", "noble", ["fire"],
     {"fire_cost_mult": 0.8},
     [ct("sarutobi", 1, "clan_staff", "Monkey King Staff Forms", "",
         mc="Opens the clan staff (item:sarutobi_staff, 4.5 reach) with the Monkey King staff style", cost=0, cast=0, power=0,
         effects=[{"style": "combat:style.monkey_staff"}], tags=["no_signs"], beta=True),
      ct("sarutobi", 2, "fire_staff", "Fire Flow Staff", "tiger ox", nature="fire",
         mc="Fire runs along the staff for 300 ticks: every sweep sets alight and its reach grows 1 block", power=0,
         effects=[st("blade_flow.fire", 300)]),
      ct("sarutobi", 3, "ash_cloud", "Clan Ash Pile Burning", "ram rat monkey boar horse tiger", nature="fire", replaces="combat:fire.ash_pile_burning",
         mc="The clan's own Ash Pile Burning: 10-block cone, blinds longer (80 ticks)", shape=cone(10, 70),
         effects=[st("blinded", 80), {"damage": "ninjutsu.fire", "delay": 20}]),
      ct("sarutobi", 4, "extending_staff", "Staff of a Thousand Lengths", "ram ox hare",
         mc="The staff stretches to 20 blocks for one sweep and comes back: hits everything in a line", cast=6,
         shape=line(20, 1.5), effects=[{"damage": "physical.blunt"}, {"knockback": 4}])],
     lesser_tech=lesser("sarutobi", "will_of_fire", "Will of Fire", "",
                        "When a squadmate falls, you gain +15% damage for 200 ticks", power=0, cast=0, tags=["no_signs"]),
     style="combat:style.monkey_staff")

clan("aburame", "Aburame", "noble", [],
     {"poison_resist": 0.5, "insects": "a hive in the body: insect techniques cost chakra from the swarm (half cost)"},
     [ct("aburame", 1, "insect_swarm", "Insect Swarm", "ram ox dragon",
         mc="A swarm entity follows a target for 200 ticks: drains 1 chakra a second (you gain it) and marks it (it glows for you)", power=0,
         shape={"type": "entity", "entity": "insect_swarm", "ticks": 200, "range": 16}, effects=[{"drain_chakra_per_second": 1}, st("marked", 200)],
         beta=True, counters="fire jutsu burn the swarm; smoke; running on water"),
      ct("aburame", 2, "insect_clone", "Insect Clone", "ram ox snake",
         mc="A clone of insects that bursts into a swarm when struck", power=0, shape=summon_entity("insect_clone", 600)),
      ct("aburame", 3, "insect_sphere", "Insect Sphere", "ram ox horse",
         mc="A dome of insects (radius 6) for 200 ticks: anyone inside loses 2 chakra a second and is slowed", shape=area(6),
         power=0, effects=[{"drain_chakra_per_second": 2}, st("chilled", 200)]),
      ct("aburame", 4, "hive_storm", "Hive Storm", "ram snake tiger dog",
         mc="Every insect at once: a storm 16 blocks across that strips chakra from all enemies and feeds your squad", shape=area(16),
         power_mult=0.5, effects=[{"drain_chakra_per_second": 3, "shared_with_squad": True}])],
     lesser_tech=lesser("aburame", "bug_sense", "Bug Sense", "",
                        "A beetle rides on you: a hidden enemy within 8 blocks makes it buzz", power=0, cast=0, tags=["no_signs"]))

clan("hatake", "Hatake", "noble", ["lightning"],
     {"control_bonus": 5, "ninken": "a tracking ninken companion (VF pet code, not a summon)"},
     [ct("hatake", 1, "ninken_tracker", "Ninken Tracker", "",
         mc="Your ninken tracks a mission target or hidden enemy and leads you there; in a fight it pins a target 20 ticks every 15 s",
         cast=0, cost=4, power=0, effects=[st("marked", 400), st("bound", 20)], tags=["no_signs"], beta=True),
      ct("hatake", 2, "white_fang_arts", "White Fang Arts", "",
         mc="Opens the White Fang style with a tanto (the white sabre at Jonin)", cost=0, cast=0, power=0, effects=[{"style": "combat:style.white_fang"}],
         tags=["no_signs"]),
      ct("hatake", 3, "earth_hounds", "Earth: Tracking Fang", "boar rat ox", nature="earth",
         mc="Ninken burst from the ground under the target and hold it (bound 80 ticks)", shape={"type": "target", "range": 16},
         effects=[st("bound", 80), {"damage": "physical.slash"}]),
      ct("hatake", 4, "lightning_cutter", "Lightning Cutter", "ox hare monkey", nature="lightning", replaces="combat:lightning.lightning_blade",
         mc="The clan's perfected Lightning Blade: 16-block dash, half the charge, chains to a second target", cast=24, power_mult=1.0,
         shape=line(16, 1.0, dash=True, breaks_guard=True, chain=1), effects=[{"damage": "ninjutsu.lightning"}, st("shocked", 14)])],
     lesser_tech=lesser("hatake", "silent_tracking", "Silent Tracking", "",
                        "Footprints of enemies who passed in the last minute glow for you", power=0, cast=0, tags=["no_signs"]))

clan("kurama", "Kurama", "noble", [],
     {"genjutsu_power": 0.1, "will_bonus": 8},
     [ct("kurama", 1, "painted_illusion", "Painted Illusion", "ram ox ram", kind="clan",
         mc="Brush strokes in the air: a painted world closes over one target within 12 blocks for 120 ticks (genjutsu, painted)",
         power=0, shape={"type": "target", "range": 12, "needs_sight": True}, effects=[st("genjutsu", 120, variant="painted")], beta=True),
      ct("kurama", 2, "painted_beasts", "Painted Beasts", "ram ox bird", level=15, slice_="beta3",
         mc="Inside the illusion, painted beasts maul the target: genjutsu damage 1 power a second (stops if it breaks free)", power_mult=0.6,
         effects=[st("genjutsu", 160, variant="painted"), {"damage": "genjutsu", "per_second": True, "hp": True}]),
      ct("kurama", 3, "living_canvas", "Living Canvas", "ram snake boar dog",
         mc="A painted world over every enemy within 10 blocks for 120 ticks", shape=area(10), power=0,
         effects=[st("genjutsu", 120, variant="painted")]),
      ct("kurama", 4, "final_brushstroke", "Final Brushstroke", "ram snake boar dog bird",
         mc="The painting becomes real for one stroke: a target caught in your genjutsu takes S-rank damage and the illusion ends", power_mult=1.0,
         requires=["status:target_in_genjutsu"], effects=[{"damage": "ninjutsu.none"}])],
     lesser_tech=lesser("kurama", "ink_mind", "Ink Mind", "",
                        "Genjutsu on you lasts 30% shorter", power=0, cast=0, tags=["no_signs"]))

clan("shimura", "Shimura", "noble", ["wind"],
     {"wind_power": 0.05},
     [ct("shimura", 1, "vacuum_blades", "Wind: Vacuum Blades", "tiger rat ox", nature="wind",
         mc="Breath blades in a 30-degree fan (10 blocks) that break through a guard", shape=cone(10, 30, guard_pierce=1.0),
         effects=[{"damage": "ninjutsu.wind"}, st("bleeding", 60)], beta=True),
      ct("shimura", 2, "vacuum_volley", "Wind: Vacuum Volley", "tiger rat ox rat", nature="wind",
         mc="Five vacuum bullets from a single breath", shape=proj(24, 2.2, 0.5, count=5, interval=3), effects=[{"damage": "ninjutsu.wind"}]),
      ct("shimura", 3, "sealing_curse", "Sealing Curse", "ram ox tiger dog",
         mc="A curse seal: the target cannot speak of what it saw (a quest tool on ANBU-branch missions) and cannot weave for 120 ticks",
         slice_="anbu", power=0, shape=touch(2.5), effects=[st("silenced", 120)]),
      ct("shimura", 4, "great_vacuum", "Wind: Great Vacuum", "tiger rat ox rat ox", nature="wind",
         mc="A pull of air that drags every enemy in 12 blocks into a 2-block point, then a slicing burst", shape=area(12),
         effects=[{"pull": 8}, {"damage": "ninjutsu.wind"}])],
     lesser_tech=lesser("shimura", "cold_discipline", "Cold Discipline", "",
                        "Fear and confusion on you last half as long", power=0, cast=0, tags=["no_signs"]))

clan("yuhi", "Yuhi", "noble", [],
     {"genjutsu_power": 0.1, "will_bonus": 8},
     [ct("yuhi", 1, "tree_binding", "Genjutsu: Tree Binding", "ram ox dog",
         mc="The target sees itself bound by a tree and cannot move for 80 ticks; you appear behind it (a free back attack)", power=0,
         shape={"type": "target", "range": 12, "needs_sight": True}, effects=[st("genjutsu", 80, variant="binding"), st("bound", 80), {"blink_behind": True}],
         beta=True),
      ct("yuhi", 2, "thorn_illusion", "Genjutsu: Thorn Garden", "ram ox boar",
         mc="A garden of thorns in a 6-block circle (genjutsu): anyone inside believes it is cut with every step (slow 0.5, cannot sprint)",
         shape=area(6), power=0, effects=[st("genjutsu", 160, variant="binding"), st("chilled", 160, slow=0.5)]),
      ct("yuhi", 3, "rose_reversal", "Genjutsu: Rose Reversal", "ram tiger rat",
         mc="Reflects genjutsu, and the reflected illusion lasts twice as long", power=0, effects=[st("genjutsu_reflect", 80, mult=2.0)]),
      ct("yuhi", 4, "tree_binding_death", "Genjutsu: Tree Binding Death", "ram snake tiger dog",
         mc="Tree Binding on up to three targets, and your back attack on each is a guaranteed crit", shape=area(12, max_targets=3), power_mult=0.6,
         effects=[st("bound", 100), {"damage": "physical.slash", "crit": True}])],
     lesser_tech=lesser("yuhi", "crimson_eye", "Crimson Eye", "",
                        "Genjutsu cast by enemies within your sight are marked with a red ring before they land", power=0, cast=0, tags=["no_signs"]))

clan("gekko", "Gekko", "noble", [],
     {"kenjutsu_power": 0.1},
     [ct("gekko", 1, "crescent_moon_dance", "Dance of the Crescent Moon", "",
         mc="Two short-lived clones appear and all three strike a target at once from three sides (needs a blade)", cast=6, power_mult=1.1,
         shape=touch(4.0), effects=[{"damage": "physical.slash", "hits": 3}], tags=["no_signs"], requires=["weapon:blade"], beta=True),
      ct("gekko", 2, "moon_shadow_step", "Moon Shadow Step", "",
         mc="Vanish into a blade's gleam and reappear behind a target within 10 blocks (counts as a dodge with 8 i-frames)", cast=2, power=0,
         cooldown=120, effects=[{"blink_behind": True}, st("iframes", 8)], tags=["no_signs"]),
      ct("gekko", 3, "full_moon_slash", "Full Moon Slash", "",
         mc="A 360-degree draw-cut (radius 4) at the end of a parry", cast=4, shape=area(4), effects=[{"damage": "physical.slash"}], tags=["no_signs"],
         requires=["status:counter_window"]),
      ct("gekko", 4, "new_moon_blade", "New Moon Blade", "",
         mc="An invisible strike: the next sword hit within 100 ticks gives no telegraph and deals S-rank damage", cast=2,
         effects=[st("new_moon", 100)], tags=["no_signs"])],
     lesser_tech=lesser("gekko", "moon_breathing", "Moonlit Breathing", "",
                        "At night your kenjutsu stamina costs 30% less", power=0, cast=0, tags=["no_signs"]),
     style="combat:style.crescent_moon")

# Minor clans. Seven are ordinary families without a bloodline: their 'techniques' are family arts,
# open to clan-born players and taught (the lesser ones) to friends. Three have abilities.
clan("shiranui", "Shiranui", "minor", [],
     {"thrown_accuracy": 0.1, "senbon_damage": 0.15},
     [ct("shiranui", 1, "needle_spit", "Needle Spit", "", kind="family_art",
         mc="Flick a senbon from the mouth with no throw animation (no telegraph)", cast=0, cost=0, power=3, cooldown=40,
         shape=proj(16, 3.0, 0.2), effects=[{"damage": "physical.pierce"}], tags=["no_signs"]),
      ct("shiranui", 2, "pressure_needles", "Pressure Needles", "", kind="family_art",
         mc="Senbon headshots paralyse at two numbed stacks instead of three", cost=0, cast=0, power=0, tags=["no_signs"]),
      ct("shiranui", 3, "thousand_needles", "Thousand Needles", "ram tiger ox", kind="family_art",
         mc="A storm of senbon from all sides of one target (radius 2)", shape={"type": "target", "range": 16, "radius": 2},
         effects=[{"damage": "physical.pierce"}, st("numbed", 100, stacks=2)]),
      ct("shiranui", 4, "guard_formation", "Hokage Guard Formation", "ram tiger hare", kind="family_art",
         mc="For 300 ticks, half the damage an ally within 6 blocks takes is redirected to you", power=0, effects=[st("guarding_ally", 300)])],
     lesser_tech=lesser("shiranui", "needle_style", "Needle arts", "",
                        "Opens the needle arts style", power=0, cast=0, effects=[{"style": "combat:style.needle_arts"}], tags=["no_signs"]))

clan("morino", "Morino", "minor", [],
     {"will_bonus": 10, "genjutsu_resist": 0.2},
     [ct("morino", 1, "stern_presence", "Stern Presence", "", kind="family_art",
         mc="A glare: enemies under rank chunin within 8 blocks hesitate (feared 30 ticks)", cast=4, power=0, shape=area(8),
         effects=[st("fear", 30)], tags=["no_signs"]),
      ct("morino", 2, "interrogation_hold", "Interrogation Hold", "", kind="family_art",
         mc="A grab on a downed enemy: it surrenders and answers (a quest hook: combat:surrendered)", cast=20, power=0, shape=touch(2.0),
         effects=[{"surrender": True}], tags=["no_signs"]),
      ct("morino", 3, "iron_will", "Iron Will", "ram tiger dragon", kind="family_art",
         mc="Immune to genjutsu, fear and confusion for 300 ticks", power=0, effects=[st("mind_immune", 300)]),
      ct("morino", 4, "breaking_point", "Breaking Point", "ram tiger horse", kind="family_art",
         mc="A target that fails its will check (strength vs will) drops its guard and its next technique for 100 ticks", power=0,
         shape={"type": "target", "range": 8}, effects=[st("broken_guard", 100), {"fizzle_next": True}])],
     lesser_tech=lesser("morino", "unshaken", "Unshaken", "",
                        "+8 will", power=0, cast=0, tags=["no_signs"]))

clan("umino", "Umino", "minor", ["water"],
     {"stamina_bonus": 10, "teacher": "teammates you command get +5% damage"},
     [ct("umino", 1, "cover", "Cover", "", kind="family_art",
         mc="Dash up to 6 blocks to an ally and take the next hit meant for them (guarding)", cast=0, cost=6, power=0, cooldown=200,
         effects=[{"intercept": True}], tags=["no_signs"]),
      ct("umino", 2, "rally", "Rally", "", kind="family_art",
         mc="A shout: allies within 12 blocks regain 30 stamina and break fear", cast=4, power=0, shape=area(12),
         effects=[{"stamina": 30}, {"cleanse": ["fear"]}], tags=["no_signs"]),
      ct("umino", 3, "tidewall", "Water: Tidewall", "tiger snake rat ox", kind="family_art", nature="water",
         mc="A Water Wall that also shelters allies within 5 blocks", power=0, shape=summon_entity("water_wall", 100, radius=5)),
      ct("umino", 4, "teachers_resolve", "A Teacher's Resolve", "ram tiger ram", kind="family_art",
         mc="Once per fight: every downed ally within 12 blocks stands up with 30% health", power=0, shape=area(12), effects=[{"revive": 0.3}])],
     lesser_tech=lesser("umino", "steady_voice", "Steady Voice", "",
                        "Your squad commands are obeyed even at low cohesion", power=0, cast=0, tags=["no_signs"]))

clan("haruno", "Haruno", "minor", [],
     {"control_bonus": 15, "medical_aptitude": "medical techniques need 10 less control"},
     [ct("haruno", 1, "chakra_precision", "Chakra Precision", "", kind="family_art",
         mc="Every technique costs 5% less and fizzles refund half", cast=0, cost=0, power=0, tags=["no_signs"]),
      ct("haruno", 2, "blossom_strength", "Blossom Strength", "", kind="family_art",
         mc="Opens Blossom Strength at Chunin (others need Jonin and control 80)", cast=0, cost=0, power=0,
         effects=[{"style": "combat:style.blossom_strength"}], tags=["no_signs"]),
      ct("haruno", 3, "petal_shield", "Petal Shield", "ram tiger monkey", kind="family_art",
         mc="Heal yourself 20% over 60 ticks while guarding", power=0, effects=[{"heal_fraction": 0.2, "ticks": 60, "while": "guarding"}]),
      ct("haruno", 4, "hundred_strength", "Seal of a Hundred Blossoms", "", kind="family_art",
         mc="Strength of a Hundred at control 80 instead of 90, and it stores twice as fast", cast=0, cost=0, power=0, tags=["no_signs"])],
     lesser_tech=lesser("haruno", "focused_mind", "Focused Mind", "",
                        "+5 chakra control", power=0, cast=0, tags=["no_signs"]))

clan("namiashi", "Namiashi", "minor", [],
     {"kenjutsu_power": 0.05, "stamina_bonus": 10},
     [ct("namiashi", 1, "wave_step", "Wave Step", "", kind="family_art",
         mc="Footwork that leaves no sound and no ripple: silent steps and water-walking cost nothing", cast=0, cost=0, power=0, tags=["no_signs"]),
      ct("namiashi", 2, "wave_foot_arts", "Wave-foot Arts", "", kind="family_art",
         mc="Wave-foot kenjutsu tier 3 moves (the guard of waves)", cast=0, cost=0, power=0, effects=[{"style": "combat:style.wave_foot"}],
         tags=["no_signs"]),
      ct("namiashi", 3, "black_tide", "Black Tide", "", kind="family_art",
         mc="The kokuto drinks light for 200 ticks: your blade attacks give no telegraph", cast=4, power=0, effects=[st("no_telegraph", 200)],
         tags=["no_signs"]),
      ct("namiashi", 4, "hokage_guard", "Hokage's Blade", "", kind="family_art",
         mc="Counter any melee attack aimed at an ally within 4 blocks with a guaranteed draw-cut (once per 10 s)", cast=0, power_mult=0.8,
         effects=[{"intercept": True, "counter": True}], tags=["no_signs"])],
     lesser_tech=lesser("namiashi", "wave_foot", "Wave-foot basics", "",
                        "Opens wave-foot kenjutsu tiers 1 and 2", power=0, cast=0, effects=[{"style": "combat:style.wave_foot"}], tags=["no_signs"]),
     style="combat:style.wave_foot")

clan("hagane", "Hagane", "minor", [],
     {"poise_bonus": 10, "blunt_power": 0.1},
     [ct("hagane", 1, "mace_arts", "Mace Arts", "", kind="family_art", mc="Opens mace arts with the clan mace", cost=0, cast=0, power=0,
         effects=[{"style": "combat:style.mace_arts"}], tags=["no_signs"]),
      ct("hagane", 2, "iron_guard_master", "Iron Guard Mastery", "", kind="family_art",
         mc="Iron Guard tier 2 (the iron wall) and blocks never break while you stand still", cost=0, cast=0, power=0, tags=["no_signs"]),
      ct("hagane", 3, "steel_bracer", "Steel Bracer Counter", "", kind="family_art",
         mc="A parry with bracers reflects 50% of the blow", cast=0, power=0, tags=["no_signs"]),
      ct("hagane", 4, "gate_wall", "Gate Wall", "ram tiger bird", kind="family_art",
         mc="For 200 ticks you cannot be moved, staggered or knocked down; enemies who strike you are knocked back", power=0,
         effects=[st("immovable", 200)])],
     lesser_tech=lesser("hagane", "iron_guard", "Iron Guard", "",
                        "Opens Iron Guard (the gate guards' style)", power=0, cast=0, effects=[{"style": "combat:style.iron_guard"}], tags=["no_signs"]))

clan("kinoshita", "Kinoshita", "minor", ["earth"],
     {"trap_power": 0.15, "wire_uses": 4},
     [ct("kinoshita", 1, "trap_craft", "Trap Craft", "", kind="family_art",
         mc="Tripwires and caltrops are invisible to enemies below jonin; set a trap in half the time", cost=0, cast=0, power=0, tags=["no_signs"]),
      ct("kinoshita", 2, "timber_barricade", "Timber Barricade", "boar tiger", kind="family_art",
         mc="A barricade entity of planks (5 wide, hp 60) for 300 ticks: cover for throwers", power=0,
         shape=summon_entity("barricade", 300, width=5, hp=60)),
      ct("kinoshita", 3, "wire_web", "Wire Web", "", kind="family_art",
         mc="Throw a web of wire across a 6-block gap: anyone touching it is bound 40 ticks and tagged bombs on it go off", cast=10,
         power=0, shape=summon_entity("wire_web", 400, width=6), effects=[st("bound", 40)], tags=["no_signs"]),
      ct("kinoshita", 4, "carpenters_fortress", "Carpenter's Fortress", "boar ram ox", kind="family_art",
         mc="A walled square of timber (8 x 8, hp 300) with firing slits for 600 ticks: a defence objective's best friend", power=0,
         shape=summon_entity("fortress", 600, width=8, hp=300))],
     lesser_tech=lesser("kinoshita", "wire_traps", "Wire arts", "",
                        "Opens wire arts", power=0, cast=0, effects=[{"style": "combat:style.wire_arts"}], tags=["no_signs"]))

clan("tsuchigumo", "Tsuchigumo", "minor", ["earth"],
     {"earth_power": 0.05},
     [ct("tsuchigumo", 1, "earth_binding", "Earth Binding Web", "boar rat tiger", nature="earth",
         mc="A web-like binding trap (entity) on the ground for 400 ticks: the first enemy across is bound 80 ticks", power=0,
         shape=summon_entity("web_trap", 400, radius=2), effects=[st("bound", 80)], beta=True),
      ct("tsuchigumo", 2, "web_wall", "Spider Web Wall", "boar dog ram tiger", nature="earth",
         mc="A web wall 6 wide for 200 ticks: catches thrown weapons and binds anyone who walks into it", power=0,
         shape=summon_entity("web_wall", 200, width=6), effects=[st("bound", 40)]),
      ct("tsuchigumo", 3, "spider_armour", "Earth Spider Armour", "boar hare", nature="earth",
         mc="Rock Skin that also binds whoever strikes you in melee (20 ticks)", power=0, effects=[st("hardened", 200), {"on_struck": st("bound", 20)}]),
      ct("tsuchigumo", 4, "heaven_earth_seal", "Creation of Heaven and Earth (sealed)", "", nature="earth",
         mc="The clan's forbidden art. It cannot be used: the seal is the clan's to keep. Listed so data and story can refer to it", cost=0, cast=0,
         power=0, slice_="never", tags=["forbidden", "no_signs"])],
     lesser_tech=lesser("tsuchigumo", "web_snare", "Web Snare", "boar rat",
                        "A small web trap (bound 30 ticks)", power=0, shape=summon_entity("web_trap", 300, radius=1.5), effects=[st("bound", 30)]))

clan("suzuran", "Suzuran", "minor", [],
     {"poison_immune": True, "coating_hits_mult": 1.5},
     [ct("suzuran", 1, "coating_craft", "Lily Blood: Coatings", "", kind="clan",
         mc="Craft poison coatings, antidotes and poultices at the workbench; your coatings last 50% longer", cost=0, cast=0, power=0, tags=["no_signs"],
         beta=True),
      ct("suzuran", 2, "lily_poultice", "Lily Poultice", "ram tiger boar",
         mc="Heal an ally 30% over 100 ticks and cleanse every poison", power=0, shape=touch(2.0),
         effects=[{"heal_fraction": 0.3, "ticks": 100}, {"cleanse": ["poisoned", "numbed", "drowsy"]}]),
      ct("suzuran", 3, "poison_mist", "Poison Mist", "ram hare rat",
         mc="A violet mist (radius 6) for 200 ticks: poisoned, 2 stacks a second; you and your squad are immune if you share antidotes", shape=area(6),
         power=0, effects=[st("poisoned", 200, stacks=2)]),
      ct("suzuran", 4, "bloom_of_bells", "Bloom of Bells", "ram snake tiger dog",
         mc="White bells ring around you for 400 ticks: allies within 10 blocks are immune to poison and regenerate 0.5 HP a second", shape=area(10),
         power=0, effects=[st("poison_immune", 400), {"heal_per_second": 0.5}])],
     lesser_tech=lesser("suzuran", "herb_lore", "Herb Lore", "",
                        "You can craft poultices and antidotes at the workbench", power=0, cast=0, tags=["no_signs"]))

clan("tobari", "Tobari", "minor", [],
     {"noise_mult": 0.7, "night_vision": True},
     [ct("tobari", 1, "night_curtain", "Night Curtain", "snake rat",
         mc="At night, a curtain (radius 5) for 400 ticks smothers your footsteps and techniques: enemies do not hear you or your jutsu", power=0,
         effects=[st("silent_steps", 400), {"area_silence": 5}], beta=True, requires=["time:night"]),
      ct("tobari", 2, "lantern_dim", "Lantern Dim", "snake ram dog",
         mc="Dim your chakra: enemy sensing (and Byakugan stage 1) cannot find you for 300 ticks", power=0, effects=[st("unsensed", 300)]),
      ct("tobari", 3, "curtain_veil", "Curtain Veil", "snake ram dog boar",
         mc="Hidden while you move at a walk, day or night, for 300 ticks", power=0, effects=[st("hidden", 300, walking=True)]),
      ct("tobari", 4, "great_curtain", "Great Curtain", "snake ram dog boar ox",
         mc="The whole squad within 10 blocks is silent and unsensed for 600 ticks", power=0, shape=area(10),
         effects=[st("silent_steps", 600), st("unsensed", 600)])],
     lesser_tech=lesser("tobari", "soft_steps", "Soft Steps", "",
                        "Silent step costs no chakra at night", power=0, cast=0, tags=["no_signs"]))

CLANLESS = {
    "passives": {"stamina_bonus": 10, "control_bonus": 5},
    "note": "Self-made: clanless players start with +10 stamina and +5 control, learn one lesser technique per friendly clan (clan friendship 7) and every open style, so clanless is never the weaker pick.",
}

PLAYER_CLAN_ARTS = {
    "how": "A player clan's clan art is a technique its founder has mastered (ROADMAP Player clans); members learn it from the founder",
    "allowed": "any technique of rank C to A the founder has at mastered or better, not a kekkei genkai and not a clan's tier technique",
    "bonus": "the clan art costs its members 15% less",
}
