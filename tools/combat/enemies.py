"""Enemies: the AI (range bands, tells, reactions to the player's habits), the bestiary of every
human and animal enemy, loadout files, spawn groups, bosses with phases, sparring and exam rules.

Story enemies are written by role and neutral ids; what a story boss is, and any secret mechanic,
lives only in the story bible, keyed by the boss id.
"""

# Enemy tiers: health and damage multipliers, poise, XP, and think_ticks: how long the brain waits between
# actions (mooks hesitate; bosses press). The player out-classes a mook one on one; groups are the danger.
TIERS = {"mook": {"hp": 1.0, "damage": 0.75, "poise": 15, "xp": 1.0, "think_ticks": 10},
         "elite": {"hp": 2.2, "damage": 1.0, "poise": 30, "xp": 2.0, "think_ticks": 6},
         "miniboss": {"hp": 3.5, "damage": 1.15, "poise": 60, "xp": 5.0, "think_ticks": 5},
         "boss": {"hp": 7.0, "damage": 1.15, "poise": 100, "xp": 12.0, "think_ticks": 4}}

AI = {
    "brain": "One shinobi entity for every human enemy, drawn with VF's resident model and our wardrobe; animals are vanilla-based entities with our brain",
    "range_bands": {"close": [0, 3], "mid": [3, 10], "far": [10, 24]},
    "band_rules": [
        "Each loadout prefers a band; the brain moves to it, strafes at 1.5 to 3 blocks a second and keeps a 30% chance to switch band every 4 s",
        "Close: taijutsu chains, grabs and guard; mid: throws, D and C jutsu, dashes in; far: jutsu, bows, traps, sensing, retreat to heal",
        "Two or more enemies coordinate bands: one presses close while the others hold mid or far (a cell is always one close, one far)",
    ],
    "reactions": {
        "dodge_by_rank": {"civilian": 0.05, "academy": 0.1, "genin": 0.2, "chunin": 0.35, "jonin": 0.5, "kage": 0.65},
        "parry_by_rank": {"civilian": 0.0, "academy": 0.05, "genin": 0.1, "chunin": 0.2, "jonin": 0.3, "kage": 0.4},
        "telegraph_factor": "dodge chance x (telegraph ticks / 10), at most 1.5x: slow, readable attacks are dodged more",
        "substitution": "Genin and up substitute once per fight when a hit would take 20% of their health",
        "kiting": "a fighter that prefers a farther band backs off at 60% of its speed, and only on half its decisions: a closer catches it",
        "retreat": "retreat to heal at 30% health if they carry pills or a medic is near; rogue ninja use smoke to break off",
        "flee": "bandits flee at 25% health (chance in the loadout); a fleeing enemy that is hit again surrenders",
        "flinch": "a landed hit makes a mook or elite flinch: its wind-up is cancelled (bosses flinch only when their poise breaks); the player flinches too, except from light hits on Story",
        "interrupt": "melee hits, staggers and knockdowns interrupt a weave; a thrown or jutsu hit interrupts only if it deals 15% of the weaver's health or more (a single shuriken does not; a tagged kunai or a big jutsu does). Enemies weave only when no one is within 3 blocks, unless they are jonin",
    },
    "tells": {
        "rule": "Every enemy attack has a wind-up pose and a sound, scaled by difficulty (telegraph_mult). Unblockables flash red (Story, Shinobi). Signs are visible as the enemy weaves",
        "classes": {"light": 4, "heavy": 10, "grab": 12, "throw": 6, "jutsu": "its signs", "signature": 20},
    },
    "habits": {
        "how": "The brain keeps a short memory of the player's habits in this fight (last 60 s) and adapts, scaled by difficulty's habit_adaptation; the sensei comments in barks",
        "rules": [
            {"habit": "spam_same_jutsu", "when": "the same technique 3 times in 30 s", "react": "+15% dodge against it for each repeat; casters raise a counter-nature wall"},
            {"habit": "never_guards", "when": "no block in 20 s while fighting", "react": "more feints and fast light chains"},
            {"habit": "always_guards", "when": "blocking more than 50% of the time", "react": "guard breaks, grabs, paper bombs, wind (guard pierce)"},
            {"habit": "dodge_same_side", "when": "4 dodges in a row the same way", "react": "attacks lead to that side"},
            {"habit": "stays_far", "when": "over 10 blocks for 15 s", "react": "body flicker in, smoke, rushers lead"},
            {"habit": "stays_close", "when": "inside 3 blocks for 15 s", "react": "substitution, knockback jutsu, shove to mid"},
            {"habit": "turtles_in_cover", "when": "behind a wall or barrier", "react": "paper bombs over it, flanking, area jutsu"},
            {"habit": "out_of_chakra", "when": "under 15% chakra", "react": "enemies press; casters stop holding back"},
            {"habit": "parries_well", "when": "3 parries in 20 s", "react": "unblockables and throws instead of melee"},
        ],
    },
    "attack_tokens": "At most N enemies may attack the player in melee or with jutsu at once (Story 1, Shinobi 2, Hard 3; difficulty attack_tokens); the rest circle, throw, reposition or fight your teammates. Bosses always hold a token",
    "squad_ai": "Enemy groups pick a leader; the leader calls a focus target (the weakest or the caster). Animals pack-hunt: they circle and bite from behind",
    "knockout": "Residents and spar partners are knocked out, never killed (VF Knockouts). Bandits and rogue ninja can be knocked out or defeated; story enemies follow their boss file",
}


def enemy(eid, name, kind, tier, rank, levels, band, *, style=None, weapons=None, techniques=None, tools=None, nature=None,
          armour=None, traits=None, ai=None, slice_="beta2", found=None, barks=None, note=None, hp=None, poise=None):
    e = {"id": "combat:enemy." + eid, "name": name, "kind": kind, "tier": tier, "rank": rank, "levels": list(levels),
         "band": band, "slice": slice_}
    if style:
        e["style"] = style
    e["weapons"] = weapons or []
    e["techniques"] = ["combat:" + t if not t.startswith("combat:") else t for t in (techniques or [])]
    e["tools"] = tools or {}
    if nature:
        e["nature"] = nature
    e["armour"] = armour or {"physical": 0, "chakra": 0, "will": 10}
    e["traits"] = traits or []
    e["ai"] = ai or {}
    if found:
        e["found"] = found
    e["barks"] = barks or ("beast_none" if kind == "animal" else "bandit")
    if note:
        e["note"] = note
    if hp:
        e["hp_mult"] = hp
    if poise:
        e["poise"] = poise
    return e


AB = "combat:style.academy_basics"
SF = "combat:style.strong_fist"

HUMANS = [
    # Sparring partners (non-lethal, VF Knockouts)
    enemy("spar.classmate", "Academy classmate", "human", "mook", "academy", (1, 6), "close", style=AB, weapons=["item:practice_kunai"],
          techniques=["nin.substitution"], ai={"yield_at": 0.3, "dodge": 0.1}, slice_="beta1", found="Academy yard, training grounds", barks="spar_partner",
          traits=["nonlethal"]),
    enemy("spar.genin", "Genin sparring partner", "human", "elite", "genin", (5, 16), "close", style=AB, weapons=["item:kunai", "item:shuriken"],
          techniques=["nin.substitution", "nin.body_flicker"], ai={"yield_at": 0.3}, slice_="beta2", found="training grounds", barks="spar_partner",
          traits=["nonlethal"]),
    enemy("spar.chunin", "Chunin sparring partner", "human", "elite", "chunin", (15, 30), "mid", style=AB, weapons=["item:kunai", "item:shuriken"],
          techniques=["nin.substitution", "nin.body_flicker", "nin.shadow_clone"], ai={"yield_at": 0.3}, slice_="beta3", barks="spar_partner",
          traits=["nonlethal", "uses_your_nature_weakness"]),
    # Bandits (Beta 2): the road and the camps
    enemy("bandit_thug", "Bandit thug", "human", "mook", "civilian", (5, 14), "close", weapons=["item:bo_staff"],
          ai={"flee_chance": 0.4, "aggression": 0.8}, found="roads, bandit camps", note="Club swings, a shove; flees at 25%"),
    enemy("bandit_knife", "Bandit knife-fighter", "human", "mook", "civilian", (5, 14), "close", weapons=["item:tanto"],
          tools={"item:smoke_bomb": 1}, ai={"flee_chance": 0.4, "aggression": 1.0}, traits=["backstabber"]),
    enemy("bandit_archer", "Bandit archer", "human", "mook", "civilian", (6, 16), "far", weapons=["vanilla:bow"],
          ai={"flee_chance": 0.5, "keeps_distance": 12}, note="A vanilla bow: arrows count as physical.pierce"),
    enemy("bandit_brute", "Bandit brute", "human", "elite", "civilian", (8, 18), "close", weapons=["item:iron_mace"], poise=45,
          armour={"physical": 4, "chakra": 0, "will": 5}, ai={"flee_chance": 0.2}, traits=["heavy_hitter", "grab"],
          note="Slow overheads (10-tick tell) and a grab; poise 45: break it for a stagger"),
    enemy("bandit_ronin", "Ronin sellsword", "human", "elite", "genin", (10, 20), "close", weapons=["item:katana"], style="combat:style.crescent_moon",
          ai={"parry": 0.2, "flee_chance": 0.1}, traits=["parries", "draw_cut"], note="Parries your lights: use heavies, throws or jutsu"),
    enemy("bandit_chief", "Bandit chief", "human", "miniboss", "genin", (10, 16), "close", weapons=["item:iron_mace", "item:kunai"],
          tools={"item:paper_bomb": 3, "item:smoke_bomb": 2}, ai={"flee_chance": 0.0, "calls_reinforcements": True},
          found="bandit camps (weekly refill)", note="Leads a camp; see boss.ch11.bandit_chief"),
    enemy("smuggler_runner", "Smuggler", "human", "mook", "civilian", (8, 16), "mid", weapons=["item:kunai"], tools={"item:smoke_bomb": 2, "item:makibishi": 1},
          ai={"flee_first": True}, traits=["runner"], note="Runs for it: catch, bind or tag them (combat:captured)"),
    # Village trouble (Beta 2): non-lethal street fights for village missions
    enemy("street_tough", "Street tough", "human", "mook", "civilian", (5, 14), "close", weapons=["item:bo_staff"],
          ai={"flee_chance": 0.6, "yield_at": 0.3}, traits=["nonlethal"], found="the market, the toll bridge, back alleys",
          note="Hired muscle: knocked out, never killed; flees at low health"),
    enemy("pickpocket", "Pickpocket", "human", "mook", "civilian", (3, 12), "mid", ai={"flee_first": True},
          traits=["nonlethal", "steals_item", "runner"], tools={"item:smoke_bomb": 1}, note="Quick and weak: catch them before they reach the crowd"),
    enemy("cat_burglar", "Cat burglar", "human", "elite", "civilian", (6, 16), "far", weapons=["item:shuriken"],
          ai={"flee_first": True}, traits=["nonlethal", "runner", "roof_runner"], tools={"item:smoke_bomb": 2, "item:makibishi": 1},
          note="Runs the rooftops faster than a genin: wire, binds and shuriken to the legs stop them; a chase objective"),
    # Rogue ninja and scouts (Beta 2 on)
    enemy("rogue_genin", "Rogue genin", "human", "mook", "genin", (8, 18), "mid", style=AB, weapons=["item:kunai", "item:shuriken"],
          techniques=["nin.substitution", "nin.body_flicker", "fire.ember_shot"], tools={"item:smoke_bomb": 1}, barks="rogue"),
    enemy("rogue_bomber", "Rogue bomber", "human", "elite", "genin", (10, 20), "far", weapons=["item:kunai"],
          techniques=["nin.substitution", "weapon.tag_kunai"], tools={"item:paper_bomb": 8}, traits=["traps"], barks="rogue",
          note="Lays paper-bomb mines and throws tagged kunai; ground decals show its mines on Story"),
    enemy("rogue_kunoichi", "Rogue illusionist", "human", "elite", "genin", (10, 20), "mid", weapons=["item:senbon"],
          techniques=["nin.substitution", "gen.false_surroundings", "gen.hell_viewing"], armour={"physical": 0, "chakra": 0, "will": 25},
          barks="rogue", note="Opens with genjutsu: weave Release (Ram) or get a teammate to touch you"),
    enemy("rogue_chunin", "Rogue chunin", "human", "elite", "chunin", (15, 28), "mid", style=AB, weapons=["item:kunai", "item:shuriken", "item:tanto"],
          techniques=["nin.substitution", "nin.body_flicker", "nin.shadow_clone", "wind.great_breakthrough", "earth.mud_wall"],
          tools={"item:paper_bomb": 2, "item:smoke_bomb": 2}, slice_="beta3", barks="rogue", ai={"retreat_at": 0.3}),
    enemy("scout_runner", "Enemy scout", "human", "mook", "genin", (8, 18), "far", weapons=["item:kunai", "item:shuriken"],
          techniques=["nin.hiding_camouflage", "nin.body_flicker"], tools={"item:smoke_bomb": 2}, barks="cell",
          ai={"flee_first": True, "reports": True}, note="If it escapes, the next fight in that mission has +1 enemy"),
    enemy("scout_sensor", "Enemy sensor", "human", "elite", "genin", (10, 20), "far", weapons=["item:senbon"],
          techniques=["sense.chakra_sense", "nin.substitution"], barks="cell", traits=["sensor"],
          note="Sees through clones, Transformation and smoke; take it out first"),
    enemy("cell_vanguard", "Cell vanguard", "human", "elite", "genin", (12, 22), "close", style=AB, weapons=["item:tanto", "item:kunai"],
          techniques=["nin.substitution", "nin.body_flicker", "lightning.stunning_palm"], tools={"item:smoke_bomb": 1, "item:paper_bomb": 2},
          barks="cell", ai={"pairs_with": "combat:enemy.cell_support"}, note="Enemy cells fight in pairs: the vanguard presses close"),
    enemy("cell_support", "Cell support", "human", "elite", "genin", (12, 22), "far", weapons=["item:shuriken", "item:ninja_wire"],
          techniques=["nin.substitution", "fire.great_fireball", "earth.mud_wall", "gen.false_surroundings"], tools={"item:paper_bomb": 3},
          barks="cell", ai={"pairs_with": "combat:enemy.cell_vanguard"}, note="The partner holds far and combines natures with the vanguard"),
    # Exam rivals (Beta 3): foreign genin
    enemy("exam_genin_wind", "Foreign genin (fan)", "human", "elite", "genin", (13, 18), "far", weapons=["item:war_fan"],
          techniques=["nin.substitution", "wind.great_breakthrough", "wind.gale_palm"], nature="wind", slice_="beta3", barks="exam_genin"),
    enemy("exam_genin_sound", "Foreign genin (sonic)", "human", "elite", "genin", (13, 18), "mid", weapons=["item:kunai"],
          techniques=["nin.substitution", "gen.sly_mind"], traits=["sonic_waves"], slice_="beta3", barks="exam_genin",
          note="Arm tubes blast sonic waves (a cone that ignores guard and makes the screen wobble); a custom loadout move"),
    enemy("exam_genin_puppet", "Foreign genin (puppeteer)", "human", "elite", "genin", (13, 18), "far", weapons=["item:kunai"],
          techniques=["nin.chakra_threads"], traits=["puppet"], slice_="beta3", barks="exam_genin",
          note="A puppet entity fights for it on chakra threads; hit the puppeteer, not the puppet"),
    enemy("exam_genin_needle", "Foreign genin (needles)", "human", "elite", "genin", (13, 18), "mid", weapons=["item:senbon"],
          techniques=["nin.substitution", "water.hiding_mist", "water.water_bullet"], nature="water", tools={"item:coating_numbing": 1},
          slice_="beta3", barks="exam_genin"),
    enemy("exam_genin_brawler", "Foreign genin (brawler)", "human", "elite", "genin", (13, 18), "close", style=SF,
          techniques=["nin.substitution", "earth.hardening"], nature="earth", slice_="beta3", barks="exam_genin", poise=40),
    # Later (foundation)
    enemy("rogue_jonin", "Rogue jonin", "human", "miniboss", "jonin", (30, 45), "mid", style=AB, weapons=["item:katana", "item:kunai"],
          techniques=["nin.substitution", "nin.shadow_clone", "lightning.false_darkness", "water.water_dragon", "water.hiding_mist"],
          tools={"item:paper_bomb": 4}, slice_="chunin", barks="rogue"),
    enemy("hunter_nin", "Hunter-nin", "human", "elite", "chunin", (20, 40), "mid", weapons=["item:senbon"],
          techniques=["nin.substitution", "nin.body_flicker", "water.hiding_mist", "sense.chakra_sense"], slice_="chunin", barks="rogue"),
    enemy("foreign_chunin", "Foreign chunin", "human", "elite", "chunin", (18, 32), "mid", style=AB, weapons=["item:kunai", "item:shuriken"],
          techniques=["nin.substitution", "nin.body_flicker", "fire.fire_dragon_bullet", "wind.blade_of_wind"], slice_="chunin", barks="cell"),
    enemy("foreign_jonin", "Foreign jonin", "human", "miniboss", "jonin", (30, 50), "mid", style=AB, weapons=["item:katana"],
          techniques=["nin.substitution", "nin.shadow_clone", "lightning.lightning_blade", "earth.flow_rampart"], slice_="jonin", barks="cell"),
    enemy("samurai", "Samurai", "human", "elite", "chunin", (25, 45), "close", weapons=["item:katana"], style="combat:style.iaido",
          armour={"physical": 8, "chakra": 10, "will": 20}, traits=["chakra_blade", "ninjutsu_resist"], slice_="jonin", barks="cell",
          note="Heavy armour that turns ninjutsu (chakra armour 10): fight it with taijutsu, poise and weapons"),
    enemy("mercenary_captain", "Mercenary captain", "human", "miniboss", "chunin", (20, 35), "close", weapons=["item:kusarigama"],
          style="combat:style.chain_arts", tools={"item:smoke_bomb": 2, "item:flash_bomb": 2}, slice_="chunin", barks="bandit"),
    enemy("puppet_master", "Puppet master", "human", "miniboss", "jonin", (30, 45), "far", techniques=["nin.chakra_threads"],
          traits=["puppet", "puppet_x3", "poison_blades"], slice_="jonin", barks="rogue"),
    enemy("sealing_adept", "Sealing adept", "human", "elite", "chunin", (25, 40), "far", tools={"item:sealing_tag": 12},
          techniques=["seal.tag_barrier", "seal.chakra_suppression", "seal.binding_tag"], traits=["ninjutsu_resist_inside_barrier"],
          slice_="chunin", barks="cell"),
    enemy("sensor_team_lead", "Sensor team leader", "human", "elite", "chunin", (25, 40), "far", techniques=["sense.wide_sense", "nin.body_flicker"],
          traits=["sensor", "calls_focus"], slice_="chunin", barks="cell"),
    enemy("assassin", "Assassin", "human", "elite", "jonin", (30, 50), "close", weapons=["item:tanto", "item:senbon"],
          techniques=["nin.hiding_camouflage", "nin.body_flicker", "gen.bringer_of_darkness"], tools={"item:coating_venom": 2},
          traits=["ambush", "backstabber"], slice_="anbu", barks="cell"),
    enemy("cell_veteran", "Cell veteran", "human", "miniboss", "jonin", (30, 50), "mid", style=AB, weapons=["item:katana", "item:kunai"],
          techniques=["nin.substitution", "nin.shadow_clone", "fire.great_dragon_fire", "earth.flow_rampart", "gen.bringer_of_darkness"],
          slice_="jonin", barks="cell"),
    enemy("warlord", "Bandit warlord", "human", "miniboss", "chunin", (20, 32), "close", weapons=["item:iron_mace", "item:kunai"],
          style="combat:style.mace_arts", techniques=["nin.substitution", "earth.hardening", "earth.mud_wall"], tools={"item:paper_bomb": 4, "item:smoke_bomb": 2},
          armour={"physical": 6, "chakra": 2, "will": 15}, slice_="chunin", barks="bandit", note="A B-rank mission target holding a fort; the target is bound as a role by the mission"),
    enemy("legend_rogue", "Legendary missing-nin", "human", "boss", "jonin", (45, 60), "mid", style=AB, weapons=["item:katana", "item:kunai"],
          techniques=["nin.substitution", "nin.multi_shadow_clone", "water.water_dragon", "water.hiding_mist", "lightning.lightning_blade", "earth.flow_rampart"],
          tools={"item:paper_bomb": 6}, armour={"physical": 8, "chakra": 8, "will": 30}, slice_="road", barks="rogue",
          note="An S-rank bounty: no story, a neutral legend of the bingo book"),
    enemy("hollow_fighter", "Flat-eyed fighter", "human", "elite", "chunin", (20, 50), "mid", style=AB, weapons=["item:kunai"],
          techniques=["fire.fire_dragon_bullet", "wind.blade_of_wind", "lightning.false_darkness"], traits=["flat_ai", "no_flinch", "no_retreat", "cycles_natures"],
          slice_="chunin", barks="beast_none", note="Flat AI: never flinches or retreats; cycles three natures"),
    enemy("chakra_absorber", "Chakra absorber", "human", "elite", "chunin", (25, 45), "close", style=AB,
          armour={"physical": 2, "chakra": 30, "will": 20}, traits=["absorbs_ninjutsu"], slice_="chunin", barks="rogue",
          note="Drinks ninjutsu that hits it (heals for half): taijutsu and weapon users' favourite target"),
]

ANIMALS = [
    enemy("wolf", "Wolf", "animal", "mook", "beast", (3, 14), "close", traits=["pack", "flanks"], slice_="beta2", found="the forests outside the walls"),
    enemy("boar", "Wild boar", "animal", "mook", "beast", (3, 12), "close", traits=["charge"], slice_="beta2",
          note="Charges in a straight line (10-tick tell): sidestep and it stuns itself on a tree"),
    enemy("bear", "Bear", "animal", "elite", "beast", (8, 20), "close", traits=["grab", "heavy_hitter"], poise=50, slice_="beta2"),
    enemy("monkey_thief", "Thieving monkey", "animal", "mook", "beast", (1, 10), "mid", traits=["steals_item", "flees"], slice_="beta2",
          note="Steals a hotbar item and runs for the trees: a chase objective"),
    enemy("hawk", "Hawk", "animal", "mook", "beast", (5, 16), "far", traits=["dive", "flying"], slice_="beta2"),
    enemy("deer", "Deer", "animal", "mook", "beast", (1, 1), "far", traits=["passive", "nara_forest"], slice_="beta2",
          note="Never hostile; hurting a Nara deer is a bad deed"),
    enemy("giant_centipede", "Giant centipede", "animal", "elite", "beast", (13, 18), "close", traits=["poison_bite", "armoured"],
          armour={"physical": 6, "chakra": 0, "will": 40}, slice_="beta3", found="Forest of Death"),
    enemy("giant_leech", "Giant leech", "animal", "mook", "beast", (13, 18), "close", traits=["drains_hp", "latches"], slice_="beta3",
          found="Forest of Death streams", note="Latches on; fire or salt (a sealing tag) pops it"),
    enemy("giant_snake", "Giant snake", "animal", "miniboss", "beast", (14, 20), "close", traits=["constrict", "swallow"], poise=80, slice_="beta3",
          found="Forest of Death", note="A wild animal, not a summon. Its swallow is escaped by damage from inside"),
    enemy("giant_tiger", "Giant tiger", "animal", "elite", "beast", (14, 20), "close", traits=["pounce", "roar_fear"], slice_="beta3", found="Forest of Death"),
    enemy("giant_spider", "Giant spider", "animal", "elite", "beast", (16, 30), "mid", traits=["webs", "poison_bite"], slice_="chunin",
          found="the mountain shrine's caves"),
]

GROUPS = [
    {"id": "combat:group.training_dummies", "members": [{"entity": "combat:dummy.training", "count": 3}], "slice": "beta1"},
    {"id": "combat:group.bandits_small", "members": [{"enemy": "combat:enemy.bandit_thug"}, {"enemy": "combat:enemy.bandit_knife"}, {"enemy": "combat:enemy.bandit_archer"}], "slice": "beta2"},
    {"id": "combat:group.road_ambush", "members": [{"enemy": "combat:enemy.bandit_thug", "count": 2}, {"enemy": "combat:enemy.bandit_archer"}, {"enemy": "combat:enemy.bandit_brute"}], "slice": "beta2"},
    {"id": "combat:group.bandits_camp", "members": [{"enemy": "combat:enemy.bandit_thug", "count": 2}, {"enemy": "combat:enemy.bandit_knife"}, {"enemy": "combat:enemy.bandit_archer"}, {"enemy": "combat:enemy.bandit_ronin"}, {"enemy": "combat:enemy.bandit_chief"}], "slice": "beta2"},
    {"id": "combat:group.smugglers", "members": [{"enemy": "combat:enemy.smuggler_runner", "count": 2}, {"enemy": "combat:enemy.rogue_genin"}], "slice": "beta2"},
    {"id": "combat:group.rogue_pair", "members": [{"enemy": "combat:enemy.rogue_genin"}, {"enemy": "combat:enemy.rogue_bomber"}], "slice": "beta2"},
    {"id": "combat:group.scout_pair", "members": [{"enemy": "combat:enemy.scout_runner"}, {"enemy": "combat:enemy.scout_sensor"}], "slice": "beta2"},
    {"id": "combat:group.cell_trio", "members": [{"enemy": "combat:enemy.cell_vanguard", "count": 2}, {"enemy": "combat:enemy.cell_support"}], "slice": "beta2"},
    {"id": "combat:group.cell_pair", "members": [{"enemy": "combat:enemy.cell_vanguard"}, {"enemy": "combat:enemy.cell_support"}], "slice": "beta2"},
    {"id": "combat:group.wolves_pack", "members": [{"enemy": "combat:enemy.wolf", "count": 3}], "slice": "beta2"},
    {"id": "combat:group.forest_beasts", "members": [{"enemy": "combat:enemy.giant_centipede"}, {"enemy": "combat:enemy.giant_leech", "count": 2}], "slice": "beta3"},
    {"id": "combat:group.exam_team", "members": [{"pick": ["combat:enemy.exam_genin_wind", "combat:enemy.exam_genin_sound", "combat:enemy.exam_genin_puppet", "combat:enemy.exam_genin_needle", "combat:enemy.exam_genin_brawler"], "count": 3, "distinct": True}], "slice": "beta3"},
    {"id": "combat:group.exam_rival", "members": [{"pick": ["combat:enemy.exam_genin_wind", "combat:enemy.exam_genin_sound", "combat:enemy.exam_genin_puppet", "combat:enemy.exam_genin_needle", "combat:enemy.exam_genin_brawler"], "count": 1}], "slice": "beta3"},
    {"id": "combat:group.hired_thugs", "members": [{"enemy": "combat:enemy.street_tough", "count": 3}], "slice": "beta2", "nonlethal": True},
    {"id": "combat:group.pickpockets", "members": [{"enemy": "combat:enemy.pickpocket", "count": 3}], "slice": "beta2", "nonlethal": True},
    {"id": "combat:group.kidnappers", "members": [{"enemy": "combat:enemy.street_tough", "count": 3}, {"enemy": "combat:enemy.rogue_genin"}], "slice": "beta2"},
    {"id": "combat:group.fort_guards", "members": [{"enemy": "combat:enemy.bandit_thug", "count": 2}, {"enemy": "combat:enemy.bandit_archer", "count": 2}, {"enemy": "combat:enemy.bandit_brute"}], "slice": "chunin"},
    {"id": "combat:group.mercenary_band", "members": [{"enemy": "combat:enemy.bandit_ronin", "count": 2}, {"enemy": "combat:enemy.bandit_brute", "count": 2}, {"enemy": "combat:enemy.bandit_archer"}, {"enemy": "combat:enemy.mercenary_captain"}], "slice": "chunin", "waves": [3, 3]},
    {"id": "combat:group.foreign_squad", "members": [{"enemy": "combat:enemy.foreign_chunin", "count": 3}], "slice": "chunin"},
    {"id": "combat:group.hunter_squad", "members": [{"enemy": "combat:enemy.hunter_nin", "count": 3}], "slice": "chunin"},
    {"id": "combat:group.foreign_platoon", "members": [{"enemy": "combat:enemy.foreign_chunin", "count": 5}, {"enemy": "combat:enemy.sensor_team_lead"}, {"enemy": "combat:enemy.foreign_jonin", "count": 2}], "slice": "jonin", "waves": [4, 4]},
    {"id": "combat:group.assassins", "members": [{"enemy": "combat:enemy.assassin", "count": 3}], "slice": "anbu"},
    {"id": "combat:group.ronin_band", "members": [{"pick": ["combat:enemy.samurai", "combat:enemy.bandit_ronin"], "count": 4}], "slice": "chunin"},
    {"id": "combat:group.rogue_cell_b", "members": [{"enemy": "combat:enemy.rogue_chunin"}, {"enemy": "combat:enemy.hunter_nin"}], "slice": "chunin"},
]

MISSION_BANDS = {
    "d": {"levels": [5, 10], "enemies": ["combat:enemy.wolf", "combat:enemy.boar", "combat:enemy.monkey_thief", "combat:enemy.bandit_thug", "combat:enemy.bandit_knife"]},
    "c": {"levels": [9, 16], "enemies": ["combat:group.bandits_small", "combat:group.road_ambush", "combat:group.bandits_camp", "combat:group.smugglers", "combat:group.rogue_pair", "combat:group.scout_pair", "combat:group.wolves_pack"]},
    "b": {"levels": [16, 30], "enemies": ["combat:group.cell_pair", "combat:group.rogue_cell_b", "combat:enemy.mercenary_captain", "combat:enemy.sealing_adept", "combat:enemy.chakra_absorber"]},
    "a": {"levels": [30, 45], "enemies": ["combat:enemy.rogue_jonin", "combat:enemy.foreign_jonin", "combat:enemy.puppet_master", "combat:enemy.cell_veteran", "combat:enemy.samurai"]},
    "s": {"levels": [42, 60], "enemies": ["combat:enemy.cell_veteran", "combat:enemy.foreign_jonin", "combat:enemy.assassin"]},
    "level_rule": "enemy level = the band's level for the mission (from the player's level, clamped to the band) + the combat stream's jitter of -1 to +1",
    "hooks": ["combat:defeated <enemy|group>", "combat:surrendered", "combat:captured", "combat:perform <technique|combo>", "combat:no_damage_taken",
              "combat:spotted <enemy|group> (an enemy first detects the player by sight, sound or sensing; `unseen` objectives fail on it)"],
    "detection": "Enemies detect by sight (a cone of 70 degrees, 24 blocks by day, 12 at night), sound (footsteps 8 blocks, sprinting 16, jutsu 24; silent step and Tobari remove it) and sensing (sensors only, through walls). Hidden and disguised players are detected only within 3 blocks or by sensing",
    "drops": "Loot drops use the enemy id: drop:<enemy id without the combat:enemy. prefix> (bandit_thug, bandit_chief, wolf, giant_snake...); the items session owns the loot tables",
}


def phase(at, name, behaviour, adds=None, opening=None, tell=None):
    p = {"at_hp": at, "name": name, "behaviour": behaviour}
    if adds:
        p["adds"] = adds
    if opening:
        p["openings"] = opening
    if tell:
        p["signature_tell"] = tell
    return p


def boss(bid, name, chapter, slice_, base, level, *, role=None, nonlethal=False, arena=None, win=None, lose=None, phases=None,
         techniques=None, weapons=None, style=None, hp=None, poise=None, armour=None, notes=None, story=False, damage=None,
         scripted=None, objectives=None, mechanics=None, npc_only=False, optional=False):
    b = {"id": "combat:boss." + bid, "name": name, "chapter": chapter, "slice": slice_, "base": base, "level": level,
         "nonlethal": nonlethal, "arena": arena, "win": win or "defeat", "lose": lose or "the player is downed",
         "phases": phases or [], "hp_mult": hp or 7.0, "poise": poise or 100,
         "damage_mult": damage if damage is not None else (1.0 if slice_ in ("beta1", "beta2", "beta3") else 1.15)}
    if role:
        b["role"] = role
    if techniques:
        b["techniques"] = ["combat:" + t for t in techniques]
    if weapons:
        b["weapons"] = weapons
    if style:
        b["style"] = style
    if armour:
        b["armour"] = armour
    if notes:
        b["notes"] = notes
    if story:
        b["story"] = "bible:" + b["id"]
    if scripted:
        b["scripted"] = scripted
    if objectives:
        b["objectives"] = objectives
    if mechanics:
        b["mechanics"] = mechanics
    if npc_only:
        b["npc_only"] = True
    if optional:
        b["optional"] = True
    b["dialogue"] = "dlg:combat.boss." + bid
    return b


BOSSES = [
    boss("ch2.rival_spar", "Spar with your rival", 2, "beta1", "combat:enemy.spar.classmate", 3, role="role:rival", nonlethal=True,
         arena="place:academy.yard", hp=1.8, poise=25, damage=0.8, style=AB, weapons=["item:practice_kunai"], techniques=["nin.substitution"],
         win="the rival drops to 30% health or yields", lose="you drop to 30%: the story continues either way (a flag)",
         phases=[phase(1.0, "Show-off", "fast three-hit chains, a dash kick; dodges 15%", opening="the chain's 10-tick recovery: punish it", tell="the dash kick's crouch (8 ticks)"),
                 phase(0.6, "Serious", "starts blocking; a heavy after every blocked chain", opening="block breaks with your own heavy"),
                 phase(0.4, "Desperate", "one substitution, then a rush", opening="the log: wait for them to land")],
         notes="Teaches combo, heavy, dodge and block; losing is allowed and remembered (bond: rivalry)"),
    boss("ch8.cord_test", "The cord test", 8, "beta2", "combat:enemy.spar.chunin", 12, role="role:sensei", nonlethal=True,
         arena="place:training_ground_3", hp=99.0, poise=200,
         win="the squad takes the three small tags on the sensei's cord together: touch the cord while the sensei is staggered, bound, possessed or in genjutsu",
         lose="the timer (until noon) runs out", style=AB, techniques=["nin.substitution", "nin.body_flicker", "nin.hiding_camouflage", "earth.headhunter"],
         phases=[phase(1.0, "Reading a book", "dodges everything 90%; counters with a light shove; ignores you if you only attack alone",
                       opening="a squad combo or a teammate's distraction makes it drop to 30% dodge for 60 ticks"),
                 phase(0.0, "Lesson", "when a tag is touched: Headhunter on the one who did not help")],
         notes="Unwinnable alone by design; teaches squad commands and parry. Health never matters (hp 99x)"),
    boss("ch11.bandit_chief", "Bandit chief", 11, "beta2", "combat:enemy.bandit_chief", 11, arena="place:road.east_camp", hp=5.0, poise=70, damage=0.8,
         weapons=["item:iron_mace", "item:kunai"],
         phases=[phase(1.0, "Bluster", "mace overheads (12-tick tell), a ground slam (radius 3); an archer on the wagon", adds=["combat:enemy.bandit_archer"],
                       opening="every overhead is parryable: a parry staggers him for 20"),
                 phase(0.6, "Dirty fighting", "throws smoke, then a paper bomb into it; calls a knife-fighter from the tents", adds=["combat:enemy.bandit_knife"],
                       opening="wind blows the smoke away; sensing sees through it"),
                 phase(0.25, "Cornered", "faster, no flee; grabs (red flash)", opening="poise 70: a heavy chain breaks it")]),
    boss("ch14.road_ambush", "Ambush on the road", 14, "beta2", "combat:group.cell_trio", 14, hp=1.1, poise=30, damage=0.8,
         arena="place:road.east_bend", win="the runner is captured (combat:captured) and the ambush driven off",
         lose="the runner escapes, the client falls, or you are downed",
         phases=[phase(1.0, "Pin down", "a three-person cell in road clothes and face scarves holds the road with smoke, makibishi and a fire-and-wind combo while a runner flees",
                       adds=["combat:enemy.smuggler_runner"], opening="bind, possess, wire or a shuriken to the legs stops the runner"),
                 phase(0.5, "Mines", "paper-bomb mines across the road and tagged kunai", opening="wind or a flash shows the mines; a sealing tag captures a downed foe")],
         scripted=[{"event": "bridge_cut", "at": "60% of the fight's time limit", "what": "an area-denial line across the pursuit path"}],
         objectives=[{"id": "capture_runner", "required": True}],
         notes="Teaches enemy cells, smoke and paper bombs, capture with a sealing tag", story=True),
    boss("ch16.forest_team", "A hunting team in the forest", 16, "beta3", "combat:group.exam_team", 16, hp=1.5, poise=35, damage=0.85,
         arena="place:forest_of_death", win="take their scroll, or drive them off (two of three downed)", lose="your scroll is taken or the squad is downed",
         phases=[phase(1.0, "Ambush", "traps and a genjutsu opener from the trees; one fighter stays hidden", opening="sensing and Byakugan find the hidden one"),
                 phase(0.5, "Hunt", "they split your squad: one each", opening="regroup command and a squad combo")],
         scripted=[{"event": "interrupt", "at": "player health 25% or less", "what": "ends the fight, no loss"}],
         notes="A hostile three-on-three", story=True),
    boss("ch16.forest_beast", "A giant of the forest", 16, "beta3", "combat:enemy.giant_snake", 16, hp=6.0, poise=90, arena="place:forest_of_death.river",
         phases=[phase(1.0, "Coils", "tail sweeps (radius 4, jump them), lunges (10-tick tell)", opening="its head after a missed lunge"),
                 phase(0.5, "Swallow", "a red-flash grab: swallowed; deal 15% of its health from inside or a teammate frees you",
                       opening="fire and lightning from inside count double")]),
    boss("ch17.prelim", "Preliminary bout", 17, "beta3", "combat:group.exam_rival", 16, nonlethal=True, arena="place:tower.arena", hp=3.0, poise=50,
         win="the opponent is knocked out or yields (or the proctor stops it at 10%)", lose="you are knocked out or yield",
         phases=[phase(1.0, "Feeling out", "the rolled exam rival's loadout; tests your guard"),
                 phase(0.5, "All in", "uses its signature (its loadout's best technique) on a 20-tick tell")],
         notes="The opponent is rolled from the combat stream among the exam rivals and your classmates' squad (role:classmate_c, role:classmate_d). Judged (see judging)"),
    boss("ch19.finals", "Finals bout", 19, "beta3", "combat:enemy.spar.chunin", 18, role="role:rival", nonlethal=True, arena="place:stadium.floor",
         hp=3.0, poise=60, damage=0.7, style=AB, techniques=["nin.substitution", "nin.body_flicker", "fire.great_fireball", "fire.phoenix_flower"],
         win="the opponent is knocked out or yields", lose="you are knocked out or yield (judging still counts how you fought)",
         phases=[phase(1.0, "Pride", "aggressive fire jutsu at mid range and a fast chain close; dodges 30%", opening="interrupt the signs: it weaves at 4 blocks"),
                 phase(0.6, "Pressure", "shuriken with fire (phoenix flowers with hidden steel) and a clone feint", opening="sensing or parry the real one"),
                 phase(0.3, "No holding back", "its signature on a 20-tick tell; if it has the Sharingan, telegraphs are shorter against it", opening="water or a wall; then a finisher")],
         npc_only=True,
         notes="For the NPC exam seasons (the calendar event); role-based: role:rival by default"),
    boss("ch19.stadium_cell", "Attackers in the stands", 19, "beta3", "combat:group.cell_trio", 18, hp=0.9, poise=30, damage=0.7, arena="place:stadium.stands",
         win="the stands are cleared and the east stair is held", lose="the evacuation on the east stair is broken, or you are downed",
         phases=[phase(1.0, "Smoke", "the attack's opening: smoke and fire in the stands; cells of three or more target civilians", opening="protect objective: Cover, walls, barriers"),
                 phase(0.5, "Second wave", "a fresh runner of the cell tries for the stair (a race, not a fight)")],
         objectives=[{"id": "east_stair", "kind": "protect", "what": "children evacuating down a stair"}],
         scripted=[{"event": "stair_strike", "what": "an NPC on the stair is hit (a cinematic cutaway, no blood)"}, {"event": "tier_collapse"}],
         notes="The defence and protect objectives of the finals' attack", story=True),
    # Later arcs: non-story bosses
    boss("chunin.missing_nin_bounty", "A missing-nin with a bounty", "chunin", "chunin", "combat:enemy.rogue_jonin", 26, hp=6.0,
         phases=[phase(1.0, "Mist", "water.hiding_mist then senbon"), phase(0.5, "Dragon", "water.water_dragon on a 20-tick tell")]),
    boss("chunin.mercenary_fort", "The mercenary fort", "chunin", "chunin", "combat:enemy.mercenary_captain", 24,
         phases=[phase(1.0, "Chains", "kusarigama pulls into a guard line"), phase(0.4, "Flash", "flash bombs and a charge")]),
    boss("jonin.samurai_captain", "Samurai captain", "jonin", "jonin", "combat:enemy.samurai", 38, hp=7.0, poise=140,
         armour={"physical": 10, "chakra": 14, "will": 30},
         phases=[phase(1.0, "Stance", "quick-draw counters anything in 3 blocks", opening="throws and feints bait the draw; its 16-tick recovery"),
                 phase(0.5, "Chakra blade", "its sword cuts through jutsu", opening="taijutsu poise breaks")]),
    boss("jonin.puppet_theatre", "The puppet master", "jonin", "jonin", "combat:enemy.puppet_master", 36,
         phases=[phase(1.0, "Three puppets", "three puppets with poison blades", opening="cut the threads (a slash between puppet and master)"),
                 phase(0.4, "Master", "the master fights", opening="close in: it is weak up close")]),
    # Later arcs: story bosses. Neutral ids; what they are lives in the story bible.
    boss("chunin.story_1", "Story boss", "chunin", "chunin", "combat:enemy.hollow_fighter", 24, story=True,
         mechanics=["never lands a killing blow on the player (floors at 1 HP)", "cycles three natures"],
         scripted=[{"event": "ally_down", "starts": "phase 2"}, {"event": "recognition", "ends": True}],
         phases=[phase(1.0, "First", "flat, relentless; cycles natures"), phase(0.0, "Second", "begins on ally_down")]),
    boss("chunin.story_2", "Story boss", "chunin", "chunin", "combat:group.cell_trio", 28, hp=2.0, story=True,
         mechanics=["smothered: no audio cues within 16 blocks"]),
    boss("jonin.story_1", "Story boss", "jonin", "jonin", "combat:enemy.cell_veteran", 34, story=True, style="combat:style.crescent_moon",
         weapons=["item:katana"], mechanics=["ink_lines: short-lived area-denial lines after each slash"],
         objectives=[{"id": "basket", "kind": "protect", "what": "a block entity"}],
         scripted=[{"event": "retreat", "at": "40% health", "ends": True}]),
    boss("jonin.story_2", "Story boss", "jonin", "jonin", "combat:enemy.cell_veteran", 36, story=True, optional=True,
         phases=[phase(1.0, "Leader and two", "a cell leader and two", adds=["combat:enemy.cell_vanguard", "combat:enemy.cell_support"])],
         objectives=[{"id": "cells", "kind": "protect", "what": "children"}], notes="A stealth path skips most of it"),
    boss("anbu.story_1", "Story boss", "anbu", "anbu", "combat:enemy.sealing_adept", 38, story=True,
         phases=[phase(1.0, "Masks", "masked sealers lay sealing traps"), phase(0.5, "Prodigy", "a kenjutsu and ninjutsu prodigy", adds=["combat:enemy.cell_veteran"])],
         scripted=[{"event": "stand_down", "what": "dialogue can end the fight mid-way"}]),
    boss("road.story_1", "Story boss", "road", "road", "combat:enemy.cell_veteran", 45, story=True, style="combat:style.crescent_moon",
         weapons=["item:katana"], mechanics=["ink_lines"], scripted=[{"event": "dialogue", "at": "25% health", "ends": True, "no_kill": True}],
         notes="The jonin.story_1 duellist's best loadout"),
    boss("road.story_2", "Story boss", "road", "road", "combat:group.cell_trio", 44, hp=2.2, story=True,
         objectives=[{"id": "basket", "kind": "protect"}, {"id": "npc", "kind": "protect"}]),
    boss("road.final", "Final boss", "road", "road", "combat:enemy.cell_veteran", 50, hp=12.0, poise=200, story=True,
         mechanics=["drain_beam: a channelled beam, broken by line of sight; drains chakra and health",
                    "adds scale with a story counter: 0 to 81 gives 0 to 6 extra combat:enemy.hollow_fighter"],
         phases=[phase(1.0, "Beam", "drain_beam and adds"), phase(0.3, "every_fire", "the player's damage and resistance scale with the story's bond-web tier: small under 20, strong from 20, the whole village from 41")],
         scripted=[{"event": "mirror_turns", "ends": True}]),
]

SPARRING = {
    "rules": "Sparring never kills: a spar ends at 30% health or a yield (hold the Yield key, Y, for 20 ticks), with no level loss (ROADMAP Death). Residents are knocked out, never killed (VF Knockouts)",
    "where": "training grounds; ranked residents spar if their friendship is 3 or more (BONDS spar_won / spar_lost)",
    "rewards": "pillar XP, a bond experience (spar), and a small ryo prize in Academy tournaments",
    "dummies": "combat:dummy.training: posts that log damage, combo length and parries; a log post (substitution practice); a target board for throws",
    "proctor": "exam bouts are stopped by the proctor at 10% health or a yield",
}

JUDGING = {
    "owner": "Progression's Judging reads these metrics; combat emits them per bout and per exam stage",
    "metrics": ["damage_dealt", "damage_taken", "time_to_win", "parries", "perfect_dodges", "distinct_techniques", "pillars_used",
                "combos_landed", "longest_combo", "interrupts", "squad_combos", "allies_protected", "civilians_protected",
                "smart_counters (nature advantage, genjutsu released fast, sensing used)", "yielded", "knocked_out"],
    "note": "Promotion is judged on how you fought (ROADMAP Ch 20): variety and protecting others count as much as winning",
}


# Ally kits: every named shinobi in the ranks session's roster has kit combat:ally.<role>. A kit is built
# from the person's level, niche, clan and nature by these rules, so 70 people need no hand-written file;
# the named kits below override the rule for the Classic squad (ROADMAP "The Classic cast").
ALLY_KITS = {
    "rule": {
        "build": "a player-like build at the person's level (the same pillar scaling as the player, Scaling.pillarCap), focused by niche",
        "niche_focus": {"genjutsu": "ninjutsu (genjutsu techniques first)", "taijutsu": "taijutsu", "ninjutsu": "ninjutsu",
                        "weapons": "weapons", "medical": "balanced, with the medical techniques", "sensing": "balanced, with the sensing techniques"},
        "niche_edge": "they fight niche_edge levels higher in their niche (the roster's value)",
        "clan": "clan members add their clan's techniques of every tier their level reaches (10, 20, 32, 44) and the kekkei genkai stage; clanless add the lesser techniques of up to two friendly clans",
        "nature": "the roster's nature, else the clan's suggested nature, else rolled from the combat stream (domain combat, key the role)",
        "style": "taijutsu niche: Strong Fist (or the clan style); weapons niche: the clan's weapon style, else Crescent Moon from level 15",
        "ai": "Fighter skill by rank: genin average, chunin and up skilled; squad role from Progression (vanguard, support, sensor, medic)",
        "never_killed": "allies are knocked out at 30% health and can be revived",
    },
    "named": {
        "combat:ally.teammate_a": {"niche": "genjutsu", "clan": "kurama", "nature": "water", "pet": None,
                                   "signature": ["combat:kurama.painted_illusion", "combat:kurama.painted_beasts", "combat:gen.hell_viewing", "combat:gen.mist_servant"]},
        "combat:ally.teammate_b": {"niche": "taijutsu", "clan": None, "nature": "earth", "pet": "ninken pup (bites every third landed hit; grows with its owner's level)",
                                   "signature": ["combat:style.strong_fist", "combat:nin.body_flicker", "combat:earth.headhunter"]},
        "combat:ally.rival": {"niche": "ninjutsu", "clan": "uchiha", "nature": "fire",
                              "signature": ["combat:fire.great_fireball", "combat:uchiha.phoenix_shuriken", "combat:fire.phoenix_flower"]},
        "combat:ally.sensei": {"niche": "ninjutsu", "clan": None, "nature": "rolled", "rank": "jonin",
                               "signature": ["combat:nin.shadow_clone", "combat:nin.body_flicker", "combat:earth.headhunter"]},
        "combat:ally.instructor": {"niche": "taijutsu", "clan": None, "nature": "rolled", "rank": "chunin", "signature": ["combat:style.iron_guard"]},
        "combat:ally.medic": {"niche": "medical", "clan": None, "nature": "rolled", "rank": "chunin", "signature": ["combat:med.mystical_palm", "combat:nin.first_aid"]},
    },
}
