"""Compile the combat data (tools/combat/*.py) to data/combat/ and check it.

    python3 tools/combat/build.py           # write every file
    python3 tools/combat/build.py --check   # write, then validate ids, references, signs and spoilers
"""

import glob
import hashlib
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(__file__))

import animations  # noqa: E402
import barks  # noqa: E402
import clans  # noqa: E402
import core  # noqa: E402
import docs  # noqa: E402
import enemies  # noqa: E402
import progression  # noqa: E402
import squad  # noqa: E402
import taijutsu  # noqa: E402
import techniques  # noqa: E402
import weapons  # noqa: E402
from common import OUT, RANK_LEVEL, RANKS, ROOT, SIGNS, SLICES, write  # noqa: E402

FAMILIES = {
    "neutral": techniques.NEUTRAL, "fire": techniques.FIRE, "wind": techniques.WIND, "lightning": techniques.LIGHTNING,
    "earth": techniques.EARTH, "water": techniques.WATER, "genjutsu": techniques.GENJUTSU, "medical": techniques.MEDICAL,
    "sensing": techniques.SENSING, "fuinjutsu": techniques.FUINJUTSU, "weapon": techniques.WEAPON_JUTSU,
}


def short(eid):
    return eid.split(":", 1)[1]


def build():
    for old in glob.glob(os.path.join(OUT, "**", "*.json"), recursive=True):
        os.remove(old)
    write("core/resources.json", {"resources": core.RESOURCES})
    write("core/scaling.json", core.SCALING)
    write("core/natures.json", core.NATURE_RULES)
    write("core/damage_types.json", {"types": core.DAMAGE_TYPES})
    write("core/status_effects.json", {"statuses": core.STATUS_EFFECTS, "diminishing_returns": core.DIMINISHING_RETURNS})
    write("core/armour.json", core.ARMOUR)
    write("core/signs.json", core.SIGN_INPUT)
    write("core/difficulty.json", core.DIFFICULTY)
    write("core/feel.json", core.FEEL)
    write("core/kindle.json", core.KINDLE)
    write("core/knacks.json", core.KNACKS)

    write("styles/taijutsu.json", {"tiers": taijutsu.TIERS, "styles": taijutsu.STYLES, "guard": taijutsu.GUARD,
                                   "competitive": taijutsu.COMPETITIVE})
    write("styles/gates.json", taijutsu.GATES)
    write("styles/weapons.json", {"tiers": taijutsu.TIERS, "styles": weapons.WEAPON_STYLES})

    write("weapons/weapons.json", {"grades": weapons.GRADES, "weapons": weapons.WEAPONS})
    write("weapons/tools.json", {"tools": weapons.TOOLS})
    write("weapons/coatings.json", weapons.COATINGS)
    write("weapons/throwing.json", weapons.THROWING)

    for fam, lst in FAMILIES.items():
        write("techniques/%s.json" % fam, {"techniques": lst})
    write("techniques/movement.json", {"rules": techniques.CHAKRA_MOVEMENT_RULES, "movement": techniques.MOVEMENT})
    write("techniques/rules.json", {"genjutsu": techniques.GENJUTSU_RULES, "medical": techniques.MEDICAL_RULES,
                                    "sensing": techniques.SENSING_RULES, "fuinjutsu": techniques.FUINJUTSU_RULES})

    for c in clans.CLANS:
        write("clans/%s.json" % c["id"], c)
    write("clans/_clanless.json", {"clanless": clans.CLANLESS, "player_clan_arts": clans.PLAYER_CLAN_ARTS,
                                   "tiers": {"rank": clans.TIER_RANK, "level": clans.TIER_LEVEL, "slice": clans.TIER_SLICE}})

    write("combos/nature.json", {"combos": squad.NATURE_COMBOS})
    write("combos/squad.json", {"combos": squad.SQUAD_COMBOS})
    write("combos/tactics.json", {"commands": squad.COMMANDS, "formations": squad.FORMATIONS, "cohesion": squad.COHESION,
                                  "teammates": squad.TEAMMATE_AI})

    write("enemies/_ai.json", {"tiers": enemies.TIERS, "ai": enemies.AI})
    for e in enemies.HUMANS + enemies.ANIMALS:
        write("enemies/%s.json" % short(e["id"])[len("enemy."):], e)
    write("enemies/_groups.json", {"groups": enemies.GROUPS, "mission_bands": enemies.MISSION_BANDS})
    for b in enemies.BOSSES:
        write("bosses/%s.json" % short(b["id"])[len("boss."):], b)

    write("rules/sparring.json", enemies.SPARRING)
    write("rules/judging.json", enemies.JUDGING)
    write("rules/pvp.json", squad.PVP)

    write("progression/timeline.json", {"timeline": progression.TIMELINE, "exam_reward": progression.EXAM_REWARD})
    write("progression/beta_loadout.json", progression.beta_loadout())
    write("sim/builds.json", {"builds": progression.sim_builds()})

    write("animations.json", {"clips": animations.CLIPS, "counts": animations.summary()})
    write("barks.json", barks.BARKS)

    every = all_techniques()
    write("index.json", {
        "counts": {
            "techniques": len(every),
            "techniques_by_rank": {r: sum(1 for t in every if t["rank"] == r) for r in RANKS},
            "catalogue": len(techniques.CATALOGUE), "clan_techniques": sum(len(c["techniques"]) for c in clans.CLANS),
            "lesser": sum(1 for c in clans.CLANS if c.get("lesser")), "clans": len(clans.CLANS),
            "taijutsu_styles": len(taijutsu.STYLES), "weapon_styles": len(weapons.WEAPON_STYLES),
            "moves": sum(len(s["moves"]) for s in taijutsu.STYLES + weapons.WEAPON_STYLES),
            "weapons": len(weapons.WEAPONS), "tools": len(weapons.TOOLS), "enemies": len(enemies.HUMANS) + len(enemies.ANIMALS),
            "human_enemies": len(enemies.HUMANS), "animal_enemies": len(enemies.ANIMALS), "bosses": len(enemies.BOSSES),
            "beta_bosses": sum(1 for b in enemies.BOSSES if b["slice"] in progression.BETA_SLICES),
            "groups": len(enemies.GROUPS), "nature_combos": len(squad.NATURE_COMBOS), "squad_combos": len(squad.SQUAD_COMBOS),
            "movement": len(techniques.MOVEMENT), "clips": len(animations.CLIPS),
            "beta_techniques": sum(1 for t in every if t.get("beta")),
        }})
    return every


def all_techniques():
    out = list(techniques.CATALOGUE)
    for c in clans.CLANS:
        out += c["techniques"]
        if c.get("lesser"):
            out.append(c["lesser"])
    return out


# Spoiler guard: the story bible's distinctive terms are read and hashed at check time, so this
# file names none of them.
def fold(text):
    return text.replace("ū", "u").replace("ō", "o")


def spoiler_terms_from_bible():
    """The bible's distinctive terms: bold names, proper-noun pairs, macron words and story ids.
    A term that also appears in a public document (the roadmap, the README, BONDS, SIDE_QUESTS,
    CLANS) is not a secret and is dropped."""
    path = os.path.join(ROOT, "docs", "story", "STORY_BIBLE.md")
    if not os.path.exists(path):
        return set()
    text = open(path, encoding="utf-8").read()
    terms = set()
    for m in re.finditer(r"\*\*([^*]{3,60})\*\*", text):
        for part in re.split(r"[:(.]", m.group(1)):
            part = re.sub(r"^(the|a|an)\s+", "", part.strip().lower())
            if part and len(part.split()) <= 3:
                terms.add(part)
    for m in re.finditer(r"[a-z,] ([A-Z][a-zūō]+ [A-Z][a-zūō]+)", text):
        terms.add(m.group(1).lower())
    for m in re.finditer(r"\b\w*[ūō]\w*\b", text):
        terms.add(m.group(0).lower())
    for m in re.finditer(r"`((?:role|twist|story\.seed)[:.][a-z_]+)`", text):
        terms.add(m.group(1).lower())
    terms = {fold(t) for t in terms} | terms
    public = ""
    for doc in ("ROADMAP.md", "README.md", "BONDS.md", "SIDE_QUESTS.md", "CLANS.md"):
        if os.path.exists(os.path.join(ROOT, doc)):
            public += fold(open(os.path.join(ROOT, doc), encoding="utf-8").read().lower())
    return {t for t in terms if len(t) > 3 and fold(t) not in public}


def public_text_hashes():
    """Every word and two-word phrase of every public text combat writes, hashed."""
    files = glob.glob(os.path.join(OUT, "**", "*.json"), recursive=True)
    files += glob.glob(os.path.join(ROOT, "docs", "combat", "*.md"))
    if os.path.exists(os.path.join(ROOT, "docs", "COMBAT.md")):
        files.append(os.path.join(ROOT, "docs", "COMBAT.md"))
    files += glob.glob(os.path.join(ROOT, "tools", "combat", "*.py"))
    files += glob.glob(os.path.join(ROOT, "combat", "**", "*.java"), recursive=True)
    seen = {}
    for f in files:
        words = re.findall(r"[a-zūō_.:'-]+", fold(open(f, encoding="utf-8").read().lower()))
        for i, w in enumerate(words):
            for phrase in (w, " ".join(words[i:i + 2])):
                seen.setdefault(phrase, f)
    return seen


def check(every):
    errors = []
    ids = {}
    for t in every:
        if t["id"] in ids:
            errors.append("duplicate technique id " + t["id"])
        ids[t["id"]] = t
        if t["rank"] not in RANKS:
            errors.append("%s: bad rank" % t["id"])
        if t["slice"] not in SLICES + ["never"]:
            errors.append("%s: bad slice %s" % (t["id"], t["slice"]))
        if t["level"] < RANK_LEVEL[t["rank"]] and not t.get("clan"):
            errors.append("%s: level %d under its rank's %d" % (t["id"], t["level"], RANK_LEVEL[t["rank"]]))
        for s in t["signs"]:
            if s not in SIGNS:
                errors.append("%s: unknown sign %s" % (t["id"], s))
        if len(t["signs"]) > 8:
            errors.append("%s: more than 8 signs" % t["id"])
        if not t["teach"]:
            errors.append("%s: nobody teaches it" % t["id"])
        if t.get("beta") and t["slice"] not in progression.BETA_SLICES:
            errors.append("%s: marked beta but slice %s" % (t["id"], t["slice"]))
    # Sign sequences must be unique among what one player can know: the catalogue, every lesser
    # technique, and one clan's own techniques. Two clans may share a sequence.
    # Sign sequences must be unique among what one player can know: the catalogue, other clans'
    # lesser techniques, and one clan's own techniques (a clan-born player never learns their own
    # clan's lesser technique). A technique that `replaces` another shares its signs on purpose.
    catalogue = [t for t in every if not t.get("clan")]
    for c in clans.CLANS:
        seqs = {}
        scope = catalogue + [o["lesser"] for o in clans.CLANS if o.get("lesser") and o is not c] + c["techniques"]
        for t in scope:
            if t["signs"]:
                key = " ".join(t["signs"])
                if key in seqs and seqs[key] != t["id"] and t.get("replaces") != seqs[key]:
                    errors.append("sign sequence '%s' shared by %s and %s" % (key, seqs[key], t["id"]))
                seqs[key] = t["id"]
        for t in c["techniques"]:
            if t.get("replaces") and t["replaces"] not in ids:
                errors.append("%s replaces unknown %s" % (t["id"], t["replaces"]))
    def statuses_in(x, out):
        if isinstance(x, dict):
            if isinstance(x.get("status"), str):
                out.add(x["status"])
            for v in x.values():
                statuses_in(v, out)
        elif isinstance(x, list):
            for v in x:
                statuses_in(v, out)
        return out
    for t in every:
        for s in statuses_in(t["effects"], set()):
            if s not in core.STATUS_EFFECTS:
                errors.append("%s applies unknown status %s" % (t["id"], s))
    for s in core.STATUS_EFFECTS.values():
        for x in [s.get("at_max"), s.get("then")] + s.get("cleanses", []) + s.get("cleansed_by", []):
            if x and x not in core.STATUS_EFFECTS and x != "water":
                errors.append("status refers to unknown %s" % x)
    styles = {s["id"] for s in taijutsu.STYLES + weapons.WEAPON_STYLES}
    enemy_ids = {e["id"] for e in enemies.HUMANS + enemies.ANIMALS}
    group_ids = {g["id"] for g in enemies.GROUPS}
    item_ids = {w["item"] for w in weapons.WEAPONS} | {t["item"] for t in weapons.TOOLS} | {c["item"] for c in weapons.COATINGS["list"]} \
        | set(core.ARMOUR["gear"]) | {"item:tool_pouch_large", "vanilla:bow"}
    for s in taijutsu.STYLES + weapons.WEAPON_STYLES:
        seen = set()
        for m in s["moves"]:
            key = (m["state"], " ".join(m["input"]), m["tier"])
            if key in seen:
                errors.append("%s: two moves on %s" % (s["id"], key))
            seen.add(key)
        for w in s.get("weapons", []):
            if w not in item_ids:
                errors.append("%s: unknown item %s" % (s["id"], w))
    for w in weapons.WEAPONS:
        if w.get("style") and w["style"] not in styles:
            errors.append("%s: unknown style %s" % (w["item"], w["style"]))
    for t in every:
        for r in t.get("requires", []):
            base = r.split(":mastered")[0]
            if base.startswith("combat:") and base not in ids:
                errors.append("%s requires unknown %s" % (t["id"], base))
            if base.startswith("item:") and base.split(":")[0] + ":" + base.split(":")[1] not in item_ids:
                errors.append("%s requires unknown item %s" % (t["id"], base))
        for e in t["effects"]:
            if isinstance(e, dict) and "style" in e and e["style"] not in styles:
                errors.append("%s: unknown style %s" % (t["id"], e["style"]))
    for e in enemies.HUMANS + enemies.ANIMALS:
        for t in e["techniques"]:
            if t not in ids:
                errors.append("%s: unknown technique %s" % (e["id"], t))
        if e.get("style") and e["style"] not in styles:
            errors.append("%s: unknown style %s" % (e["id"], e["style"]))
        for w in e["weapons"] + list(e["tools"]):
            if w not in item_ids:
                errors.append("%s: unknown item %s" % (e["id"], w))
    for g in enemies.GROUPS:
        for m in g["members"]:
            for x in ([m["enemy"]] if "enemy" in m else m.get("pick", [])):
                if x not in enemy_ids:
                    errors.append("%s: unknown enemy %s" % (g["id"], x))
    for b in enemies.BOSSES:
        if b["base"] not in enemy_ids | group_ids:
            errors.append("%s: unknown base %s" % (b["id"], b["base"]))
        for t in b.get("techniques", []):
            if t not in ids:
                errors.append("%s: unknown technique %s" % (b["id"], t))
        for p in b["phases"]:
            for a in p.get("adds", []):
                if a not in enemy_ids | group_ids:
                    errors.append("%s: unknown add %s" % (b["id"], a))
    for band in enemies.MISSION_BANDS.values():
        if isinstance(band, dict):
            for x in band["enemies"]:
                if x not in enemy_ids | group_ids:
                    errors.append("mission band: unknown %s" % x)
    for pool in progression.EXAM_REWARD["pool"].values():
        for x in pool:
            if x.count(":") == 1 and x not in ids:
                errors.append("exam reward: unknown %s" % x)
    for b in progression.sim_builds():
        for t in b["techniques"]:
            if t not in ids:
                errors.append("%s: unknown technique %s" % (b["id"], t))
    if len(clans.CLANS) != 25:
        errors.append("expected 25 clans, have %d" % len(clans.CLANS))
    for c in clans.CLANS:
        tiers = sorted(t["tier"] for t in c["techniques"])
        if tiers != [1, 2, 3, 4]:
            errors.append("%s: tiers %s" % (c["id"], tiers))
    wardrobe = {os.path.basename(p)[:-5] for p in glob.glob(os.path.join(ROOT, "tools", "wardrobe", "clans", "*.json"))}
    if wardrobe and wardrobe != {c["id"] for c in clans.CLANS}:
        errors.append("clan ids differ from tools/wardrobe/clans: %s" % sorted(wardrobe ^ {c["id"] for c in clans.CLANS}))

    # Spoilers: no story-bible term may appear in combat's public files.
    terms = spoiler_terms_from_bible()
    hashes = {hashlib.sha256(t.encode()).hexdigest(): t for t in terms}
    for phrase, f in public_text_hashes().items():
        h = hashlib.sha256(phrase.encode()).hexdigest()
        if h in hashes:
            shown = hashes[h] if "--reveal" in sys.argv else "sha256 " + h[:12] + "..."
            errors.append("possible story-bible term in %s (%s)" % (os.path.relpath(f, ROOT), shown))
    return errors


def main():
    every = build()
    pages = docs.write_all()
    n = len(glob.glob(os.path.join(OUT, "**", "*.json"), recursive=True))
    print("wrote %d files to %s (%d techniques) and %d pages to docs/combat/" % (n, os.path.relpath(OUT, ROOT), len(every), len(pages)))
    if "--check" in sys.argv:
        errs = check(every)
        for e in errs:
            print("ERROR", e)
        if errs:
            sys.exit(1)
        print("check: ok")


if __name__ == "__main__":
    main()
