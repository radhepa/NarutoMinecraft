"""When each technique, style and weapon unlocks across the 60-hour story, the beta loadout, and the
player builds the duel simulator plays (generated from the catalogue, so they track the data)."""

from clans import CLANS
from common import RANK_LEVEL
from techniques import CATALOGUE

TIMELINE = [
    {"stretch": "academy", "slice": "beta1", "levels": [1, 5], "hours": [0, 4], "pillar_cap": 5,
     "taijutsu": ["Academy taijutsu: jab, cross, roundhouse, heavy, flying kick, lunge (Ch 2)", "block, dodge (Ch 2)"],
     "weapons": ["practice kunai and shuriken (Ch 2)", "smoke bomb, ninja wire (workbench, Beta 1)", "throwing arts: quick throw"],
     "ninjutsu": ["chakra bar and hand signs (Ch 3)", "Clone (the instructor), Transformation, Substitution (Ch 6)", "Release, Rope Escape, Field First Aid", "roof hopping (Ch 4)"],
     "sources": ["Academy lessons", "the instructor", "the medic (first aid)"]},
    {"stretch": "genin", "slice": "beta2", "levels": [5, 15], "hours": [4, 12], "pillar_cap": 10,
     "taijutsu": ["parry, counter, squad commands (Ch 8)", "sweep, launcher, air combo and air spike (Ch 8 to 10)", "palm rush finisher (taijutsu rank 3)",
                  "styles: Strong Fist (the master's side line), Iron Guard (Hagane friendship 5), Gentle Fist (Hyuga), Iron Body (Akimichi), Beast Fang (Inuzuka)"],
     "weapons": ["kunai, shuriken, senbon, tanto (shops, Ch 9)", "paper, smoke and flash bombs, caltrops, sealing tags, tool pouch (Ch 11 to 14)", "coatings (Suzuran, or bought)",
                 "fan of three; exploding-tag kunai and Shadow Shuriken (sensei, Ch 14); clan staff (Sarutobi), kokuto (Namiashi), mace (Hagane)",
                 "styles: academy blade, throwing arts, needle arts (Shiranui friendship), wire arts (Kinoshita friendship), wave-foot (Namiashi), monkey staff, mace arts"],
     "ninjutsu": ["chakra movement: tree walking, wall-running, chakra jump, ninja run (Ch 10), water-walking (Ch 12)", "Body Flicker, Hiding in Camouflage (sensei)",
                  "the nature ceremony: your nature's C-rank signature (Ch 12)", "the scroll shop: D-rank of your nature and second C-rank options",
                  "clan technique tier 1 and kekkei genkai stage 1 (clan-born, Ch 12); a lesser clan technique (clanless, clan friendship 7)",
                  "genjutsu basics (False Surroundings, Hell Viewing) from the genjutsu master; Binding Tag"],
     "sources": ["the sensei", "clan elders", "nature masters", "the scroll shop", "board missions (D, C)", "friendly clans"]},
    {"stretch": "chunin_exams", "slice": "beta3", "levels": [15, 18], "hours": [12, 15], "pillar_cap": 12,
     "taijutsu": ["Strong Fist tier 2: Leaf Great Whirlwind", "style tier 2 finishers (taijutsu rank 3)"],
     "weapons": ["ninjato and katana, Crescent Moon kenjutsu (weapons rank 4; Gekko from Genin)", "manji shuriken, kusarigama, weighted chain, iron fan: chain and fan arts", "blood pills"],
     "ninjutsu": ["the exam reward: one C-rank chosen by your sensei after the preliminaries (Ch 18)", "Mystical Palm (the medic, control 50), Chakra Sensing (Yamanaka or the sensor master)",
                  "Four-Tag Barrier, Hiding Mist, Mist Servant", "Sharingan stage 1 (an Uchiha in the forest, Ch 16)", "nature chakra flow on blades"],
     "sources": ["the sensei (exam reward)", "the medic", "the sensor master", "the weapon master", "exam-week stalls"]},
    {"stretch": "chunin", "slice": "chunin", "levels": [18, 30], "hours": [15, 28], "pillar_cap": 18,
     "taijutsu": ["Strong Fist tier 3 (Primary Lotus) and gates 1 and 2", "Swaying Willow (a wandering master)", "Blossom Strength (Haruno)", "Gentle Fist Palm Rotation and Sixty-Four Palms"],
     "weapons": ["windmill shuriken, Windmill Triple", "storage scroll barrage, Explosive Kunai Barrage, Rising Twin Dragons", "the great fan; chakra flow on staffs"],
     "ninjutsu": ["B-rank of every nature you hold", "the second nature (a nature master's three trials)", "Shadow Clone (sensei)", "clan tier 2, kekkei genkai stage 2",
                  "medical B-rank, Wide Sensing, Chakra Suppression, Bringer of Darkness, Mirror Reversal", "air step"],
     "sources": ["B-rank missions", "nature masters", "the sensei", "clan elders", "Kindling Bond (pending design)"]},
    {"stretch": "jonin", "slice": "jonin", "levels": [30, 42], "hours": [28, 45], "pillar_cap": 24,
     "taijutsu": ["gates 3 and 4, Reverse Lotus", "Lightning Body (lightning nature)", "128 Palms", "Blossom Strength for everyone at control 80"],
     "weapons": ["White Fang (Hatake), the white sabre", "trench knives", "Shuriken Shadow Clone"],
     "ninjutsu": ["A-rank: Lightning Blade, Spiralling Sphere, Multi Shadow Clone, great dragons", "the third nature", "clan tier 3, kekkei genkai stage 3", "Resuscitation, Five Elements Seal, Temple of Nirvana, Chakra Reading", "wind glide"],
     "sources": ["A-rank missions", "clan masters", "the sensei", "nature masters"]},
    {"stretch": "anbu", "slice": "anbu", "levels": [35, 50], "hours": ["+8"], "pillar_cap": "as level",
     "taijutsu": [], "weapons": ["ANBU armour, coatings, assassin tools"], "ninjutsu": ["stealth: detection by sight and sound; Shimura sealing curse"], "sources": ["ANBU HQ"]},
    {"stretch": "road", "slice": "road", "levels": [42, 50], "hours": [45, 60], "pillar_cap": 28,
     "taijutsu": ["gates 5 and 6, Morning Peacock", "Twin Lion Fists", "Liger Bomb"],
     "weapons": ["Iaido teaser", "grandmaster kenjutsu"],
     "ninjutsu": ["S-rank: the forbidden archive's scrolls (Great Fire Annihilation, Kirin, Earth Splitting, Thousand Sharks, Sea of Ink, Marked Teleport)", "Great Spiralling Sphere, Spiralling Shuriken", "clan tier 4, kekkei genkai stage 4", "Strength of a Hundred"],
     "sources": ["the Hokage's archive", "the sensei", "clan heads"]},
    {"stretch": "post", "slice": "post", "levels": [50, 60], "hours": ["post-game"], "pillar_cap": 30,
     "taijutsu": ["gate 7"], "weapons": ["Iaido (a samurai master)"], "ninjutsu": ["every pillar to rank 10"], "sources": ["post-game masters"]},
]

EXAM_REWARD = {
    "when": "Ch 18, after the preliminaries: your sensei picks one technique from your build (the pillar you used most in the exams)",
    "pool": {
        "ninjutsu": ["combat:fire.phoenix_flower", "combat:wind.vacuum_wave", "combat:earth.mud_river", "combat:water.water_wall",
                     "combat:lightning.spark_needle", "combat:gen.sly_mind"],
        "weapons": ["combat:weapon.manipulated_shuriken", "combat:weapon.wind_shuriken", "combat:weapon.lightning_flow"],
        "taijutsu": ["combat:style.strong_fist:leaf_great_whirlwind", "combat:style.academy_basics:palm_rush"],
    },
    "rule": "your own nature's option first; the taijutsu option unlocks the finisher one tier early",
}

BETA_SLICES = ("beta1", "beta2", "beta2_5", "beta3")


def beta_loadout():
    techs = [t for t in CATALOGUE if t.get("beta")]
    clan_t1 = [t for c in CLANS for t in c["techniques"] if t.get("tier") == 1]
    lessers = [c["lesser"] for c in CLANS if c.get("lesser")]
    return {
        "summary": "What the beta ships: enough depth in all three pillars that fights feel great by the Chunin Exams",
        "taijutsu": {
            "styles": ["combat:style.academy_basics", "combat:style.strong_fist", "combat:style.iron_guard", "combat:style.gentle_fist",
                       "combat:style.iron_body", "combat:style.beast_fang"],
            "moves": "Academy taijutsu in full (14 moves: the chain, heavy, dash attacks, sweep, launcher, a 4-hit air string, counter, palm rush); Strong Fist tiers 1 and 2; Iron Guard tier 1; the clan styles' tier 1",
            "systems": ["block (Beta 1)", "parry and counter (Beta 2)", "dodge and perfect dodge", "substitution", "poise and stagger", "momentum and finishers", "launcher and air combos"],
        },
        "weapons": {
            "items": ["item:kunai_practice", "item:shuriken_practice", "item:kunai", "item:shuriken", "item:shuriken_manji", "item:senbon", "item:tanto",
                      "item:ninjato", "item:katana", "item:kokuto", "item:clan_staff", "item:bo_staff", "item:kusarigama", "item:chain_weight",
                      "item:tessen", "item:mace", "item:knuckle_wraps"],
            "tools": ["item:paper_bomb", "item:smoke_bomb", "item:flash_bomb", "item:wire_spool", "item:caltrops", "item:sealing_tag", "item:tool_pouch",
                      "item:soldier_pill", "item:blood_pill", "item:poultice", "item:antidote", "item:coating_numbing", "item:coating_sleep", "item:coating_venom"],
            "styles": ["combat:style.academy_blade", "combat:style.throwing_arts", "combat:style.needle_arts", "combat:style.wire_arts",
                       "combat:style.wave_foot", "combat:style.monkey_staff", "combat:style.mace_arts", "combat:style.crescent_moon",
                       "combat:style.chain_arts", "combat:style.fan_arts"],
            "systems": ["throw, aim, retrieval, wire tethers", "tool pouch quick-throw", "coatings", "chakra flow on blades", "paper-bomb mines and remote detonation"],
        },
        "ninjutsu": {
            "techniques": [t["id"] for t in techs],
            "count": len(techs),
            "clan_tier_1": [t["id"] for t in clan_t1],
            "lesser": [t["id"] for t in lessers],
            "kekkei_genkai": ["Byakugan stage 1 (Beta 2)", "Wood Release stage 1 (Beta 2)", "Sharingan stage 1 (Beta 3)"],
            "systems": ["typed and radial signs, prefix hints, auto-sign", "mastery to perfected", "the nature triangle and clashes", "genjutsu and Release",
                        "chakra movement", "sensing", "sealing tags", "nature combos with teammates"],
        },
        "per_player": "A single beta player ends with about 10 to 14 techniques (Academy 5, sensei 3 to 4, nature 2 to 3, clan or lesser 1 to 2, exam reward 1), "
                      "two or three styles, and five to eight weapons and tools in regular use",
        "enemies": "22 human and 11 animal enemy types reachable in the beta, 9 beta bosses",
        "not_in_beta": ["B-rank and above", "inner gates", "Shadow Clone", "second nature", "clan tiers 2 to 4", "Swaying Willow, Blossom Strength, Lightning Body, White Fang",
                        "windmill shuriken and great fan", "medical and sensing above C", "Kindling Bond"],
    }


# --- Simulator builds -----------------------------------------------------------------------

CHECKPOINTS = [5, 10, 15, 18, 25, 30, 40, 50, 60]


def pillar_cap(level):
    return min(30, 3 + level // 2)


def ranks_for(focus, level):
    cap = pillar_cap(level)
    if focus == "balanced":
        base = [cap // 3] * 3
        for i in range(cap - sum(base)):
            base[i] += 1
        r = {"taijutsu": base[0], "ninjutsu": base[1], "weapons": base[2]}
    else:
        main = min(10, max(1, round(cap * 0.55)))
        rest = cap - main
        a = min(10, max(1, (rest + 1) // 2))
        b = min(10, max(1, rest - a))
        others = [p for p in ("taijutsu", "ninjutsu", "weapons") if p != focus]
        r = {focus: main, others[0]: a, others[1]: b}
    return {k: max(1, min(10, v)) for k, v in r.items()}


def slice_open(slice_, level):
    order = {"beta1": 1, "beta2": 5, "beta2_5": 5, "beta3": 15, "chunin": 18, "jonin": 30, "anbu": 35, "road": 42, "post": 50, "never": 999}
    return order.get(slice_, 999) <= level


def techniques_for(nature, level, kinds, limit, max_rank="s"):
    pool = [t for t in CATALOGUE if t["level"] <= level and slice_open(t["slice"], level) and t["power"] > 0
            and RANK_LEVEL[t["rank"]] <= RANK_LEVEL[max_rank]
            and t["kind"] in kinds and t["nature"] in (nature, "none")
            and all(r.startswith("item:") for r in t.get("requires", []))]
    pool.sort(key=lambda t: (-RANK_LEVEL[t["rank"]], -t["power"]))
    return [t["id"] for t in pool[:limit]]


def gear_for(level):
    if level >= 30:
        return {"physical": 16, "chakra": 5}
    if level >= 18:
        return {"physical": 14, "chakra": 3}
    if level >= 10:
        return {"physical": 8, "chakra": 0}
    return {"physical": 1, "chakra": 0}


def melee_for(focus, level):
    if focus == "weapons":
        return "item:katana" if level >= 15 else ("item:tanto" if level >= 5 else "item:kunai_practice")
    return "item:kunai" if level >= 5 else "item:kunai_practice"


def build(focus, level, nature):
    ranks = ranks_for(focus, level)
    tier = lambda r: min(5, 1 + (r - 1) // 2)
    b = {"id": "sim.%s.%d" % (focus, level), "focus": focus, "level": level, "nature": nature, "ranks": ranks,
         "control": min(100, 30 + level), "armour": gear_for(level), "techniques": ["combat:nin.substitution", "combat:nin.clone"]}
    if level >= 8:
        b["techniques"].append("combat:nin.body_flicker")
    if focus == "taijutsu":
        b["style"] = "combat:style.strong_fist" if level >= 8 else "combat:style.academy_basics"
        b["style_tier"] = tier(ranks["taijutsu"])
        b["melee"] = None
        b["gates"] = max(0, min(ranks["taijutsu"] - 4, 6 if level >= 42 else 4 if level >= 30 else 2 if level >= 18 else 0))
        b["techniques"] += techniques_for(nature, level, ("ninjutsu",), 1, max_rank="c")
        if level >= 20:
            b["techniques"].append("combat:earth.hardening")
        b["thrown"] = "item:kunai" if level >= 5 else "item:kunai_practice"
        b["tools"] = {"item:kunai": 6}
    elif focus == "weapons":
        b["style"] = "combat:style.crescent_moon" if level >= 15 else "combat:style.academy_blade"
        b["style_tier"] = tier(ranks["weapons"])
        b["melee"] = melee_for(focus, level)
        b["thrown"] = "item:shuriken" if level >= 5 else "item:shuriken_practice"
        b["techniques"] += techniques_for(nature, level, ("weapon",), 3) + techniques_for(nature, level, ("ninjutsu",), 1, max_rank="c")
        b["tools"] = {"item:shuriken": 30, "item:kunai": 10, "item:paper_bomb": 4 if level >= 10 else 0}
    elif focus == "ninjutsu":
        b["style"] = "combat:style.academy_basics"
        b["style_tier"] = tier(ranks["taijutsu"])
        b["melee"] = melee_for(focus, level)
        b["thrown"] = "item:shuriken" if level >= 5 else "item:shuriken_practice"
        b["techniques"] += techniques_for(nature, level, ("ninjutsu",), 4)
        if level >= 8:
            b["techniques"].append("combat:gen.hell_viewing" if level < 20 else "combat:gen.bringer_of_darkness")
        b["tools"] = {"item:shuriken": 10}
    else:
        b["style"] = "combat:style.strong_fist" if level >= 8 else "combat:style.academy_basics"
        b["style_tier"] = tier(ranks["taijutsu"])
        b["melee"] = melee_for(focus, level)
        b["thrown"] = "item:shuriken" if level >= 5 else "item:shuriken_practice"
        b["gates"] = max(0, min(ranks["taijutsu"] - 4, 2 if level >= 18 else 0))
        b["techniques"] += techniques_for(nature, level, ("ninjutsu",), 3) + techniques_for(nature, level, ("weapon",), 1)
        b["tools"] = {"item:shuriken": 20, "item:kunai": 6, "item:paper_bomb": 2 if level >= 10 else 0}
    return b


def sim_builds():
    builds = []
    natures = {"taijutsu": "earth", "weapons": "wind", "ninjutsu": "fire", "balanced": "lightning"}
    for lv in CHECKPOINTS:
        for focus in ("taijutsu", "weapons", "ninjutsu", "balanced"):
            builds.append(build(focus, lv, natures[focus]))
    # The beta loadout at its key fights (the boss table)
    for lv in (3, 11, 14, 16, 18):
        for focus in ("taijutsu", "weapons", "ninjutsu", "balanced"):
            b = build(focus, lv, natures[focus])
            b["id"] = "sim.beta.%s.%d" % (focus, lv)
            b["techniques"] = [t for t in b["techniques"] if any(c["id"] == t and c.get("beta") for c in CATALOGUE)]
            builds.append(b)
    return builds
