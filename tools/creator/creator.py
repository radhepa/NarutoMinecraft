#!/usr/bin/env python3
"""The character creator's data (CHARACTER_CREATION.md): resolves tools/creator/creator.json against the wardrobe
into one allowed list per origin (clanless or one of the 25 clans) and age stage, checks it, and writes the compiled
file the creator screen and the server's validation read:
src/main/resources/data/narutominecraft/creator/creator.json.

    python3 tools/creator/creator.py              # compile
    python3 tools/creator/creator.py --check      # validate and confirm the compiled file is current
    python3 tools/creator/creator.py --samples    # sample created characters in docs/renders/creator/
    python3 tools/creator/creator.py --mockups    # the creator's screens, mocked up around real renders
    python3 tools/creator/creator.py --roll 42    # print the Varied "Roll a life" suggestion for save seed 42

The player's look is built from the same wardrobe pieces as the residents, so this tool reuses wardrobe.py's
loaders and its compatibility rules rather than keeping lists of its own.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from collections import Counter
from pathlib import Path

TOOL = Path(__file__).resolve().parent
sys.path.insert(0, str(TOOL.parent / "wardrobe"))
import wardrobe as W  # noqa: E402

ROOT = W.ROOT
RULES = TOOL / "creator.json"
OUT = ROOT / "src/main/resources/data/narutominecraft/creator/creator.json"
STAGES = ("child", "teen", "adult")
BODIES = ("male", "female")
CHANGE_PLACES = ("locked", "barber", "home", "settings")
PARITY_SEEDS = (1, 7, 42, 2026, 20261029, -5)


def load_rules() -> dict:
    return json.loads(RULES.read_text(encoding="utf-8"))


# -- seeded rolls, the same numbers as Shinobi Core's SaveSeed (and life/bonds Seeds.java) -----------------------
M64 = (1 << 64) - 1


def _signed(x: int) -> int:
    x &= M64
    return x - (1 << 64) if x >> 63 else x


def _mix(z: int) -> int:
    z &= M64
    z = ((z ^ (z >> 30)) * 0xbf58476d1ce4e5b9) & M64
    z = ((z ^ (z >> 27)) * 0x94d049bb133111eb) & M64
    return z ^ (z >> 31)


def _hash(s: str) -> int:
    h = 0xcbf29ce484222325
    data = s.encode("utf-16-be")
    for i in range(0, len(data), 2):   # Java hashes UTF-16 code units
        h ^= int.from_bytes(data[i:i + 2], "big")
        h = (h * 0x100000001b3) & M64
    return _mix(h)


def _rotl(x: int, n: int) -> int:
    return ((x << n) | (x >> (64 - n))) & M64


def hash64(seed: int, domain: str, key: str) -> int:
    return _mix((seed & M64) ^ ((_hash(domain) * 0x9E3779B97F4A7C15) & M64) ^ _rotl(_hash(key), 21))


class Rng:
    """SplitMix64, as Seeds.Rng: below(n) is Math.floorMod(next(), n) on the signed long."""

    def __init__(self, state: int):
        self.state = state & M64

    def next(self) -> int:
        self.state = (self.state + 0x9E3779B97F4A7C15) & M64
        return _mix(self.state)

    def unit(self) -> float:
        return (self.next() >> 11) * 2.0 ** -53

    def below(self, bound: int) -> int:
        return _signed(self.next()) % bound

    def pick(self, items: list):
        return items[self.below(len(items))]


def stream(seed: int, domain: str, key: str) -> Rng:
    return Rng(hash64(seed, domain, key))


# -- resolving the rules against the wardrobe -----------------------------------------------------------------------
class World:
    """The wardrobe as the creator sees it: pieces, tables, clans and collections, loaded once."""

    def __init__(self, garments: dict | None = None):
        self.garments = garments if garments is not None else W.build_all()
        self.clans = W.load_clans()
        self.collections = W.load_collections()
        self.palettes = W.load_palettes()
        self.hair_colors = W.load_hair_colors()
        self.eye_colors = W.load_eye_colors()
        self.marks = W.load_marks()
        self.population = W.load_population()
        self.rules = load_rules()

    def fits(self, gid: str, body: str) -> bool:
        return self.garments[gid].fits(body)

    # Every collection's hairstyles (shinobi and civilian), in collection order.
    def open_hair(self) -> list[str]:
        out = []
        for c in self.collections.values():
            out += [h for h in c["pool"]["hair"] if h not in out]
        return out

    def reserved_to(self, field: str, value: str) -> str | None:
        """The clan whose file defines this color or mark, if any."""
        for cid, c in self.clans.items():
            if value in c.get(field, {}):
                return cid
        return self.rules.get("reserved", {}).get(field, {}).get(value)

    def outfits(self, origin: str, stage: str) -> list[dict]:
        """The outfits an origin may wear at a stage: the open (collection) ones, then the clan's own, each with its own
        palettes and the bodies it fits. A clan-born player may also wear any of them in the clan's palettes."""
        rules = self.rules
        ranks = set(rules["stages"][stage]["outfit_ranks"])
        clan = self.clans.get(origin)
        if stage == "child":
            ranks = set(rules["open"]["outfits"]["ranks"])
            sources = [("collection", self.collections[rules["open"]["outfits"]["collection"]])]
        else:
            sources = [("collection", c) for c in self.collections.values() if c.get("role", "shinobi") == "shinobi"]
        if clan:
            sources.append(("clan", clan))
        out, seen = [], set()
        for what, src in sources:
            for o in src["outfits"]:
                if o.get("rank", "genin") not in ranks:
                    continue
                oid = f"{src['id']}.{o['id']}"
                if oid in seen:
                    continue
                seen.add(oid)
                out.append({"id": oid, "top": o["top"], "bottom": o["bottom"], "rank": o.get("rank", "genin"),
                            "palettes": list(o.get("palettes", src["pool"]["palettes"])),
                            "bodies": [b for b in BODIES if self.fits(o["top"], b) and self.fits(o["bottom"], b)], "from": what})
        return out

    def headwear(self, origin: str, stage: str) -> list:
        rules, clan = self.rules, self.clans.get(origin)
        if stage == "child":
            return list(rules["open"]["headwear"]) + list(rules["clans"][origin]["start_headwear"] if clan else [])
        out = [None]
        pools = [c for c in self.collections.values() if c.get("role", "shinobi") == "shinobi"] + ([clan] if clan else [])
        for src in pools:
            for h in src["pool"].get("headwear", []):
                if h is not None and h not in out and not self.garments[h].meta.get("covers_face"):
                    out.append(h)
        return out

    def allowed(self, origin: str, stage: str) -> dict:
        rules, clan = self.rules, self.clans.get(origin)
        never = rules["never_at_creation"]
        crules = rules["clans"].get(origin, {})
        lock = crules.get("lock", {})

        def colors(field: str, open_ids: list[str]) -> list[str]:
            first = []
            if clan:
                for v in clan["pool"][field]:
                    if v not in first and v not in never[field] and self.reserved_to(field, v) in (None, origin):
                        first.append(v)
            rest = [v for v in open_ids if v not in first]
            return first + rest

        hair = (list(clan["pool"]["hair"]) if clan else []) + [h for h in self.open_hair() if not clan or h not in clan["pool"]["hair"]]
        hair_colors = colors("hair_colors", rules["open"]["hair_colors"])
        eye_colors = [lock["eye_color"]] if "eye_color" in lock else colors("eye_colors", rules["open"]["eye_colors"])
        marks = [m["id"] for m in clan["pool"].get("marks", [])] if clan else []
        marks += [m for m in rules["open"]["marks"] if m not in marks]
        order, stage_marks = STAGES.index(stage), rules["stage_marks"]
        marks = [m for m in marks if (STAGES.index(stage_marks[m]) <= order if m in stage_marks else m not in never["marks"])]
        return {
            "hair": hair,
            "hair_colors": hair_colors,
            "eye_colors": eye_colors,
            "marks": marks,
            "headwear": self.headwear(origin, stage),
            "outfits": self.outfits(origin, stage),
        }

    def defaults(self, origin: str, view: dict, body: str) -> dict:
        """The look the creator opens on for an origin: the clan's most common draws, else the first of each list."""
        clan = self.clans.get(origin)
        pool = clan["pool"] if clan else {}

        def common(values: list, allowed_ids: list):
            ranked = [v for v, _ in Counter(v for v in values if v in allowed_ids).most_common()]
            return ranked[0] if ranked else allowed_ids[0]

        mine = [h for h in view["hair"] if self.garments[h].gender == body] + [h for h in view["hair"] if self.fits(h, body)]
        hair = mine[0] if mine else view["hair"][0]
        outfits = view["outfits"][body]
        outfit = next((o for o in outfits if o["from"] == "clan"), outfits[0])
        palette = clan["pool"]["palettes"][0] if clan and outfit["from"] == "collection" else outfit["palettes"][0]
        return {
            "body": body,
            "complexion": common(pool.get("complexions", []), [0, 1, 2, 3, 4, 5]) if clan else 1,
            "eye_style": "starlit",
            "brows": "fine",
            "hair": hair,
            "hair_color": common(pool.get("hair_colors", []), view["hair_colors"]),
            "eye_color": common(pool.get("eye_colors", []), view["eye_colors"]),
            "marks": [m["id"] for m in pool.get("marks", []) if m["chance"] >= 0.5 and m["id"] in view["marks"]][: self.rules["max_marks"]],
            "outfit": outfit["id"],
            "palette": palette,
            "headwear": None,
        }

    def roll_weights(self, origin: str, a: dict) -> dict:
        """Roll a life's weighted draws, the residents' own: the clan pool (repeats weight an entry), or for the
        clanless the Academy collection's pool, kept to what the creator allows."""
        r = self.rules
        pool = (self.clans[origin] if origin in self.clans else self.collections[r["open"]["outfits"]["collection"]])["pool"]
        marks = [m for m in pool.get("marks", []) if m["id"] in a["marks"]]
        if origin not in self.clans:
            marks = [{"id": m, "chance": r["roll_open_mark_chance"]} for m in r["open"]["marks"]]
        return {"hair_colors": [v for v in pool["hair_colors"] if v in a["hair_colors"]],
                "eye_colors": [v for v in pool["eye_colors"] if v in a["eye_colors"]],
                "complexions": list(pool.get("complexions", [0, 1, 2])),
                "marks": [{"id": m["id"], "chance": m["chance"]} for m in marks]}

    def origins(self) -> list[str]:
        return ["clanless"] + list(self.rules["clans"])

    def compile(self) -> dict:
        """The compiled file: one table of every outfit any origin may wear, and per origin its lists. Hair and colors
        are the same at every stage; marks, headwear and outfits are per stage."""
        r = self.rules
        origins, outfits = {}, {}
        for origin in self.origins():
            clan = self.clans.get(origin)
            stages = {}
            for stage in STAGES:
                a = self.allowed(origin, stage)
                for o in a["outfits"]:
                    outfits[o["id"]] = {k: o[k] for k in ("top", "bottom", "rank", "palettes", "bodies")}
                stages[stage] = {"marks": a["marks"], "headwear": a["headwear"], "outfits": [o["id"] for o in a["outfits"]]}
            entry = {
                "clan": origin if clan else None,
                "name": clan["name"] if clan else None,
                "standing": clan.get("standing", "noble") if clan else None,
                "blurb": (r["clans"][origin] if clan else r["clanless"])["blurb"],
                "family_names": [clan["name"]] if clan else list(self.population["family_names"]),
                "hair": a["hair"],
                "hair_colors": a["hair_colors"],
                "eye_colors": a["eye_colors"],
                "clan_palettes": list(dict.fromkeys(clan["pool"]["palettes"])) if clan else [],
                "stages": stages,
                "roll": self.roll_weights(origin, a),
            }
            if clan:
                for k in ("technique", "kekkei_genkai", "quarter"):
                    entry[k] = r["clans"][origin][k]
                entry["lock"] = r["clans"][origin].get("lock", {})
            else:
                entry["means"] = r["clanless"]["means"]
            origins[origin] = entry
        creatable = r["creatable"]["origins"]
        shinobi = {"clanless": self.population["clanless"]}
        shinobi.update({c: w for c, w in self.population["clans"].items() if c in self.clans})
        shinobi = {g: w for g, w in shinobi.items() if g in creatable}
        data = {
            "format": r["format"],
            "stages": r["stages"],
            "name": {k: r["name"][k] for k in ("min", "max")},
            "bodies": list(BODIES),
            "complexions": [c["id"] for c in r["complexions"]],
            "eye_styles": r["eye_styles"],
            "brows": r["brows"],
            "max_marks": r["max_marks"],
            "changes": {k: v for k, v in r["changes"].items() if not k.startswith("_")},
            "time_skip_restyle": r["time_skip_restyle"]["fields"],
            "grows_into": {k: v for k, v in r["grows_into"].items() if not k.startswith("_")},
            "stage_hair": {k: v for k, v in r["stage_hair"].items() if not k.startswith("_")},
            "prologue_look": {k: v for k, v in r["prologue_look"].items() if not k.startswith("_")},
            "starting_key_item": {k: v for k, v in r["starting_key_item"].items() if not k.startswith("_")},
            "creatable": creatable,
            "pronouns": {k: v for k, v in r["pronouns"].items() if not k.startswith("_")},
            "roots": {k: v for k, v in r["roots"].items() if not k.startswith("_")},
            "population": shinobi,
            "outfits": dict(sorted(outfits.items())),
            "origins": origins,
        }
        for origin, entry in origins.items():
            child = view(data, origin, "child")
            entry["defaults"] = {b: dict(self.defaults(origin, child, b), **r["default_overrides"].get(origin, {}).get(b, {}))
                                 for b in BODIES}
        data["parity"] = [{"seed": s, "origin": roll_origin(data, s), "look": roll_look(data, s, roll_origin(data, s)),
                           "roots": roll_roots(data, s)} for s in PARITY_SEEDS]
        return data


def view(data: dict, origin: str, stage: str) -> dict:
    """One origin's choices at one stage, expanded: outfits by body, each with every palette it may be shown in (its
    own, then the clan's). The Java side (CreatorRules) reads the compiled file the same way."""
    o = data["origins"][origin]
    st = o["stages"][stage]
    outfits = {b: [] for b in data["bodies"]}
    for oid in st["outfits"]:
        e = data["outfits"][oid]
        full = dict(e, id=oid, palettes=e["palettes"] + [p for p in o["clan_palettes"] if p not in e["palettes"]],
                    **{"from": "clan" if o["clan"] and oid.startswith(o["clan"] + ".") else "collection"})
        for b in e["bodies"]:
            outfits[b].append(full)
    order = STAGES.index(stage)
    hair = [h for h in o["hair"] if STAGES.index(data["stage_hair"].get(h, "child")) <= order]
    return {"hair": hair, "hair_colors": o["hair_colors"], "eye_colors": o["eye_colors"], "marks": st["marks"],
            "headwear": st["headwear"], "outfits": outfits}


# -- Varied's "Roll a life": the same seed always suggests the same character ------------------------------------
def roll_origin(data: dict, seed: int) -> str:
    """Clanless or a clan, by the population weights of the shinobi groups (as the rolled cast is drawn)."""
    groups = list(data["population"].items())
    total = sum(w for _, w in groups)
    n = stream(seed, "creator", "origin").below(total)
    for g, w in groups:
        if n < w:
            return g
        n -= w
    return groups[-1][0]


def roll_look(data: dict, seed: int, origin: str) -> dict:
    """A whole look for an origin at the child stage, field by field from one stream, in a fixed order."""
    o = data["origins"][origin]
    a = view(data, origin, "child")
    rng = stream(seed, "creator", "look:" + origin)
    w = o["roll"]
    body = rng.pick(data["bodies"])
    outfit = rng.pick(a["outfits"][body])
    marks = [m["id"] for m in w["marks"] if rng.unit() < m["chance"]][: data["max_marks"]]
    return {
        "body": body,
        "complexion": rng.pick(w["complexions"]),
        "eye_style": rng.pick(data["eye_styles"]),
        "brows": rng.pick(data["brows"]),
        "hair": rng.pick(a["hair"]),
        "hair_color": rng.pick(w["hair_colors"]),
        "eye_color": rng.pick(w["eye_colors"]),
        "marks": marks,
        "outfit": outfit["id"],
        "palette": rng.pick(outfit["palettes"]),
        "headwear": rng.pick(a["headwear"]),
        "family": rng.pick(o["family_names"]),
    }


def roll_roots(data: dict, seed: int) -> dict:
    """Roll a life's Roots: temperament, knack and affinity, from their own stream. Pronouns are never rolled."""
    rng = stream(seed, "creator", "roots")
    return {k: rng.pick(data["roots"][k]["options"]) for k in ("temperament", "knack", "affinity")}


def validate_roots(data: dict, roots: dict) -> list[str]:
    """The server's check of the Roots step and the pronouns (CreatorRules.validateRoots)."""
    errors = [f"{k} {roots.get(k)} is not offered" for k in ("temperament", "knack", "affinity")
              if roots.get(k) not in data["roots"][k]["options"]]
    if "pronouns" in roots and roots["pronouns"] not in data["pronouns"]["options"]:
        errors.append(f"pronouns {roots['pronouns']} are not offered")
    return errors


# -- checks ------------------------------------------------------------------------------------------------------------
STORY_BIBLE = ROOT / "docs/story/STORY_BIBLE.md"


def story_reserved_family_names() -> list[str]:
    """Family names the story keeps for itself, read from the story bible's creator.reserved_family_names line so
    they are written nowhere else. The check never prints them."""
    if not STORY_BIBLE.exists():
        return []
    m = re.search(r"^- \*\*creator\.reserved_family_names\*\*: (.+)$", STORY_BIBLE.read_text(encoding="utf-8"), re.M)
    return [n.strip() for n in m.group(1).split(",")] if m else []


def check(world: World, data: dict) -> list[str]:
    errors = []
    r, g = world.rules, world.garments
    never = r["never_at_creation"]
    if set(r["clans"]) != set(world.clans):
        errors.append(f"creator.json clans must match the wardrobe's: missing {sorted(set(world.clans) - set(r['clans']))}, "
                      f"unknown {sorted(set(r['clans']) - set(world.clans))}")
    for field, table in (("hair_colors", world.hair_colors), ("eye_colors", world.eye_colors), ("marks", world.marks)):
        for v in r["open"][field]:
            if v not in table:
                errors.append(f"open {field} names unknown {v}")
            elif world.reserved_to(field, v):
                errors.append(f"open {field} {v} belongs to the {world.reserved_to(field, v)} clan")
            if v in never[field]:
                errors.append(f"open {field} {v} is also never_at_creation")
        for v in never[field]:
            if v not in table:
                errors.append(f"never_at_creation {field} names unknown {v}")
    for h, stage in r["stage_hair"].items():
        if not h.startswith("_") and (h not in g or g[h].kind != "hair" or stage not in STAGES):
            errors.append(f"stage_hair {h}: unknown hair or stage {stage}")
    for origin, bodies in r["default_overrides"].items():
        if not origin.startswith("_") and (origin not in world.origins() or set(bodies) - set(BODIES)):
            errors.append(f"default_overrides {origin}: unknown origin or body")
    for m, stage in r["stage_marks"].items():
        if m not in world.marks or stage not in STAGES:
            errors.append(f"stage_marks {m}: unknown mark or stage {stage}")
    if [c["id"] for c in r["complexions"]] != list(range(6)):
        errors.append("complexions must be 0 to 5, in order")
    if set(r["eye_styles"]) != set(W.EYE_STYLES) or set(r["brows"]) != set(W.BROWS):
        errors.append("eye_styles and brows must be the wardrobe's")
    if set(r["stages"]) != set(STAGES):
        errors.append(f"stages must be {STAGES}")
    for s, st in r["stages"].items():
        if any(k not in W.RANKS for k in st["outfit_ranks"]) or not 0.5 <= st["scale"] <= 1.0:
            errors.append(f"stage {s}: unknown rank or scale out of 0.5..1")
    for field, c in r["changes"].items():
        if not field.startswith("_") and c["where"] not in CHANGE_PLACES:
            errors.append(f"changes.{field} must be one of {CHANGE_PLACES}")
    open_hair = set(world.open_hair())
    for src, stages in r["grows_into"].items():
        if src.startswith("_"):
            continue
        for stage, dst in stages.items():
            if stage not in ("teen", "adult"):
                errors.append(f"grows_into {src}: unknown stage {stage}")
            for gid in (src, dst):
                if gid not in open_hair:
                    errors.append(f"grows_into {src}: {gid} is not open hair")
    pl = r["prologue_look"]
    if pl["top"] not in g or pl["bottom"] not in g or not W.compatible(g[pl["top"]], g[pl["bottom"]]):
        errors.append("prologue_look pairs unknown or incompatible pieces")
    elif not (g[pl["top"]].gender == g[pl["bottom"]].gender == "unisex"):
        errors.append("prologue_look must fit both bodies (unisex pieces)")
    if pl["palette"] not in world.palettes:
        errors.append("prologue_look names an unknown palette")
    for cid, c in r["clans"].items():
        for k in ("blurb", "technique", "kekkei_genkai", "quarter", "start_headwear"):
            if k not in c:
                errors.append(f"clan {cid} needs {k}")
        if len(c.get("blurb", "")) > 200:
            errors.append(f"clan {cid} blurb is longer than 200 characters")
        for h in c.get("start_headwear", []):
            if h not in g or g[h].kind != "headwear":
                errors.append(f"clan {cid} start_headwear names unknown {h}")
            elif "protector" in h or ("mask" in h and g[h].meta.get("covers_face")):
                errors.append(f"clan {cid} start_headwear {h}: no forehead protector or masks before Genin")
        for field, value in c.get("lock", {}).items():
            if field != "eye_color" or value not in world.eye_colors:
                errors.append(f"clan {cid} lock {field} {value} is unknown")
    for name in story_reserved_family_names():
        if name in world.population["family_names"] or any(c["name"] == name for c in world.clans.values()):
            errors.append("a family name the story bible reserves is offered by the creator (see its creator.reserved_family_names)")
    if len(r["clanless"]["blurb"]) > 200:
        errors.append("clanless blurb is longer than 200 characters")
    # Every origin must be able to dress either body at every stage, and its defaults must be its own.
    for origin, o in data["origins"].items():
        clan = world.clans.get(origin)
        for stage in STAGES:
            a = view(data, origin, stage)
            for b in BODIES:
                if not a["outfits"][b]:
                    errors.append(f"{origin} {stage}: no outfit fits the {b} body")
                if not any(world.fits(h, b) for h in a["hair"]):
                    errors.append(f"{origin} {stage}: no hair fits the {b} body")
            for oo in a["outfits"]["male"] + a["outfits"]["female"]:
                if not W.compatible(g[oo["top"]], g[oo["bottom"]]):
                    errors.append(f"{origin} {stage}: outfit {oo['id']} pairs incompatible pieces")
                for p in oo["palettes"]:
                    if p not in world.palettes:
                        errors.append(f"{origin} {stage}: outfit {oo['id']} names unknown palette {p}")
            for field in ("hair_colors", "eye_colors", "marks"):
                for v in a[field]:
                    owner = world.reserved_to(field, v)
                    if owner and owner != origin:
                        errors.append(f"{origin} may not pick the {owner} clan's {field} {v}")
                    if stage == "child" and v in never[field] and not (field == "eye_colors" and v in o.get("lock", {}).values()):
                        errors.append(f"{origin} child may pick never_at_creation {field} {v}")
            for field in ("hair_colors", "eye_colors"):
                if not o["roll"][field] or any(v not in a[field] for v in o["roll"][field]):
                    errors.append(f"{origin}: Roll a life's {field} must be a non-empty subset of the allowed ones")
            for h in a["hair"]:
                if g[h].kind != "hair":
                    errors.append(f"{origin}: {h} is not hair")
                elif clan is None and h not in open_hair:
                    errors.append(f"clanless may not wear clan hair {h}")
                elif clan and h not in open_hair and h not in clan["pool"]["hair"]:
                    errors.append(f"{origin} may not wear another clan's hair {h}")
            if stage == "child" and any(h is not None and "protector" in h for h in a["headwear"]):
                errors.append(f"{origin}: a forehead protector before Genin")
        for b, d in o["defaults"].items():
            errors += [f"{origin} default ({b}): {e}" for e in validate_look(data, origin, "child", d)]
    for p in data["parity"]:
        errors += [f"parity roll {p['seed']}: {e}" for e in validate_look(data, p["origin"], "child", p["look"])]
        errors += [f"parity roll {p['seed']}: {e}" for e in validate_roots(data, p["roots"])]
        if p["origin"] not in data["creatable"]:
            errors.append(f"parity roll {p['seed']}: Roll a life chose {p['origin']}, which the creator does not offer")
    if not data["creatable"] or any(o not in data["origins"] for o in data["creatable"]):
        errors.append("creatable origins must be known origins, at least one")
    for k, v in data["roots"].items():
        if v["default"] not in v["options"]:
            errors.append(f"roots {k}: the default is not an option")
    pr = data["pronouns"]
    if any(pr["default_for_body"].get(b) not in pr["options"] for b in BODIES):
        errors.append("pronouns need a default for each body among the options")
    return errors


def validate_look(data: dict, origin: str, stage: str, look: dict) -> list[str]:
    """The server's check of a creator submission (the same rules as dev.shinobi.village.look.CreatorRules)."""
    errors = []
    a = view(data, origin, stage)
    body = look.get("body")
    if body not in data["bodies"]:
        return [f"unknown body {body}"]
    if look.get("complexion") not in data["complexions"]:
        errors.append(f"complexion {look.get('complexion')} is not allowed")
    if look.get("eye_style") not in data["eye_styles"]:
        errors.append(f"eye style {look.get('eye_style')} is not allowed")
    if look.get("brows") not in data["brows"]:
        errors.append(f"brows {look.get('brows')} are not allowed")
    for field, key in (("hair", "hair"), ("hair_color", "hair_colors"), ("eye_color", "eye_colors"), ("headwear", "headwear")):
        if look.get(field) not in a[key]:
            errors.append(f"{field} {look.get(field)} is not allowed")
    marks = look.get("marks", [])
    if len(marks) > data["max_marks"] or len(set(marks)) != len(marks):
        errors.append(f"at most {data['max_marks']} different marks")
    errors += [f"mark {m} is not allowed" for m in marks if m not in a["marks"]]
    outfit = next((o for o in a["outfits"][body] if o["id"] == look.get("outfit")), None)
    if outfit is None:
        errors.append(f"outfit {look.get('outfit')} is not allowed for this body")
    elif look.get("palette") not in outfit["palettes"]:
        errors.append(f"palette {look.get('palette')} is not offered for {outfit['id']}")
    return errors


# -- turning a look into a wardrobe character spec (for render.py) --------------------------------------------------
def spec(data: dict, origin: str, look: dict, stage: str = "child", name: str = "", outfit_override: dict | None = None) -> dict:
    a = view(data, origin, stage)
    o = outfit_override or next(x for x in a["outfits"][look["body"]] if x["id"] == look["outfit"])
    return {"id": f"creator_{origin}", "name": name, "face": "f01_shinobi", "hair": look["hair"], "headwear": look["headwear"],
            "top": o["top"], "bottom": o["bottom"], "palette": look["palette"], "hair_color": look["hair_color"],
            "eye_color": look["eye_color"], "eye_style": look["eye_style"], "brows": look["brows"],
            "feminine": look["body"] == "female", "complexion": look["complexion"], "marks": list(look["marks"]),
            "rank": o.get("rank", "academy"), "scale": 14}


def outputs(data: dict) -> bytes:
    return (json.dumps(data, indent=1, ensure_ascii=False) + "\n").encode()


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--check", action="store_true", help="validate and fail if the compiled file is stale")
    ap.add_argument("--samples", action="store_true", help="render sample created characters")
    ap.add_argument("--mockups", action="store_true", help="render the creator's screen mock-ups")
    ap.add_argument("--roll", type=int, help="print the Roll a life suggestion for a save seed")
    args = ap.parse_args(argv)
    world = World()
    data = world.compile()
    errors = check(world, data)
    if errors:
        print("\n".join(errors))
        return 1
    blob = outputs(data)
    if args.roll is not None:
        origin = roll_origin(data, args.roll)
        print(origin, json.dumps(roll_look(data, args.roll, origin)), json.dumps(roll_roots(data, args.roll)))
        return 0
    if args.mockups:
        import mockups
        mockups.all_screens(world, data)
        return 0
    if args.samples:
        import preview
        preview.samples(world, data)
        preview.stages_sheet(world, data)
        return 0
    if args.check:
        if not OUT.exists() or OUT.read_bytes() != blob:
            print(f"Stale creator data: {OUT.relative_to(ROOT)} (run tools/creator/creator.py)")
            return 1
        print(f"Creator current: {len(data['origins'])} origins, {len(data['outfits'])} outfits")
        return 0
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_bytes(blob)
    print(f"Compiled {OUT.relative_to(ROOT)} ({len(blob) // 1024} KB)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
