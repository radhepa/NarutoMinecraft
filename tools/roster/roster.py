#!/usr/bin/env python3
"""The Leaf's named shinobi and how many of each rank live in the village (docs/RANKS.md).

roster.json lists every named shinobi of the beta by role: public rank, power tier, importance, clan,
specialty, first appearance and level by story stretch. rank_distribution.json is how the population
sampler gives every other resident a rank. This tool checks both against each other, the level curve,
the wardrobe's clans and looks, and population.json, and prints the tables RANKS.md quotes.

    python tools/roster/roster.py --check     # validate (CI)
    python tools/roster/roster.py --table     # the roster as a Markdown table
    python tools/roster/roster.py --counts    # head counts: on the map, met per slice, lore
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from collections import Counter
from pathlib import Path

TOOL = Path(__file__).resolve().parent
ROOT = TOOL.parent.parent
WARDROBE = ROOT / "tools" / "wardrobe"

STRETCHES = ("academy", "genin", "exams", "chunin", "jonin", "road")
TIERS = (("S", 50), ("A", 42), ("B", 30), ("C", 15), ("D", 5), ("E", 1))
# Peer bands around the player, as life:roster's Peer factories set them (below, above).
BANDS = {"role:rival": (1, 3), "role:teammate_a": (2, 2), "role:teammate_b": (2, 2)}
CLASS_BAND = (3, 3)
# The ten minor clans (CLANS.md); the other fifteen are noble.
MINOR = {"shiranui", "morino", "umino", "haruno", "namiashi", "hagane", "kinoshita", "tsuchigumo", "suzuran", "tobari"}
# Words that would hint at a story secret; this file is read by people who play the game.
SPOILER_WORDS = re.compile(r"\b(traitor|betray\w*|suspicious|suspect\w*|spy|mole|twist|fate|dies|death|killed|secret\w*|kagari|y[uū]gure|hokage_[5-8]|future hokage|lineage)\b", re.I)


def tier(level: int) -> str:
    return next(t for t, floor in TIERS if level >= floor)


def load(name: str) -> dict:
    return json.loads((TOOL / name).read_text(encoding="utf-8"))


def first_level(p: dict) -> int:
    """The level at which the player first sees them: the class on day one, everyone else at their slice."""
    if p.get("grows"):
        return 1
    lv = p["levels"]
    return lv["exams"] if p["first"] == "beta3" else lv["genin"] if p["first"] in ("beta2", "beta2.5") else lv["academy"]


def bucket(p: dict) -> str:
    """The rank_distribution category a named person fills."""
    if p["rank"] == "jonin" and p.get("tier") == "A":
        return "elite_jonin"
    return p["rank"]


def strings(x):
    if isinstance(x, str):
        yield x
    elif isinstance(x, dict):
        for k, v in x.items():
            if k != "_doc":
                yield from strings(v)
    elif isinstance(x, list):
        for v in x:
            yield from strings(v)


def check(roster: dict, dist: dict) -> list[str]:
    errors = []
    people, civilians = roster["people"], roster.get("civilians", [])
    ranks, slices, importance = set(roster["ranks"]), set(roster["slices"]), set(roster["importance"])
    clans = {p.stem for p in (WARDROBE / "clans").glob("*.json")}
    looks = {json.loads(p.read_text(encoding="utf-8"))["id"] for p in (WARDROBE / "characters").glob("*.json")}
    pop = json.loads((WARDROBE / "population.json").read_text(encoding="utf-8"))
    pool = set(pop["family_names"])
    given = ROOT / "src" / "main" / "resources" / "data" / "narutominecraft" / "names" / "given.json"
    if given.exists():
        g = json.loads(given.read_text(encoding="utf-8"))
        for names in (g.values() if isinstance(g, dict) else [g]):
            if isinstance(names, list):
                pool |= set(names)
    seen = set()
    player = roster["player"]["levels"]
    for p in people + civilians:
        role = p.get("role", "?")
        for r in [role] + p.get("also", []):
            if r in seen:
                errors.append(f"{r}: listed twice")
            seen.add(r)
        if not role.startswith("role:"):
            errors.append(f"{role}: roles start with role:")
        if p.get("name") != "{name:%s}" % role:
            errors.append(f"{role}: name must be the token {{name:{role}}}")
        if p.get("rank") not in ranks:
            errors.append(f"{role}: unknown rank {p.get('rank')}")
        if p.get("first") not in slices:
            errors.append(f"{role}: first must be one of {', '.join(sorted(slices))}")
        for word in re.findall(r"[A-Z][a-z]+", p.get("placeholder", "")):
            if word in pool:
                errors.append(f"{role}: the placeholder uses a pool name ({word}); names are rolled per save")
    for p in people:
        role = p["role"]
        if p.get("importance") not in importance:
            errors.append(f"{role}: unknown importance {p.get('importance')}")
        clan = p.get("clan")
        if clan not in (None, "") and clan not in clans:
            errors.append(f"{role}: unknown clan {clan}")
        if p.get("masked") and clan is not None:
            errors.append(f"{role}: a masked ANBU's clan stays unknown (null)")
        if p.get("look") and p["look"] not in looks:
            errors.append(f"{role}: unknown look {p['look']} (tools/wardrobe/characters)")
        lv = p.get("levels", {})
        need = STRETCHES if p.get("grows") else STRETCHES[:3]
        if any(not isinstance(lv.get(s), int) or not 1 <= lv[s] <= 60 for s in need):
            errors.append(f"{role}: levels needs whole levels 1..60 for {', '.join(need)}")
            continue
        if not p.get("grows") and set(lv) - set(STRETCHES[:3]):
            errors.append(f"{role}: adults hold their level through the beta; later stretches belong to the later arcs")
        if p.get("tier") != tier(first_level(p)):
            errors.append(f"{role}: tier {p.get('tier')} but level {first_level(p)} at first sight is {tier(first_level(p))}")
        if p.get("grows"):
            below, above = BANDS.get(role, CLASS_BAND)
            for s in STRETCHES:
                if not player[s] - below - 1 <= lv[s] <= player[s] + above:
                    errors.append(f"{role}: {s} level {lv[s]} is outside the band around the player's {player[s]}")
        for word in SPOILER_WORDS.findall(" ".join(strings(p))):
            errors.append(f"{role}: '{word}' does not belong in a spoiler-free file")
    # Squads: the class makes four squads of three with the player.
    squads = roster["squads"]
    members = [m for s in squads.values() if s is not squads.get("squad_senior") for m in s["members"]]
    klass = [p["role"] for p in people if p.get("group") == "class"]
    if sorted(m for m in members if m != "player") != sorted(klass):
        errors.append("squads: every classmate is on exactly one squad of the year")
    if len(members) != 12 or any(len(s["members"]) != 3 for s in squads.values()):
        errors.append("squads: four squads of three in your year, plus the senior squad")
    for sid, s in squads.items():
        for m in s["members"] + [s["sensei"]] + s.get("bench", []):
            if m != "player" and m not in seen:
                errors.append(f"{sid}: unknown member {m}")
        leader = next((p for p in people if p["role"] == s["sensei"]), None)
        if leader is None or leader.get("leads") != sid:
            errors.append(f"{sid}: its sensei must say leads: {sid}")
    for word in SPOILER_WORDS.findall(" ".join(strings(roster.get("squads", {})))):
        errors.append(f"squads: '{word}' does not belong in a spoiler-free file")
    # The rank distribution: it adds up, matches the population's shares, and has room for the named roster.
    total = Counter()
    for weights in dist["by_group"].values():
        total.update(weights)
    total.update(dist["fixed"])
    if dict(total) != dist["targets"]:
        errors.append(f"rank_distribution: by_group + fixed {dict(total)} != targets {dist['targets']}")
    if sum(dist["targets"].values()) != dist["residents"]:
        errors.append(f"rank_distribution: targets sum to {sum(dist['targets'].values())}, not {dist['residents']}")
    clan_w = pop["clans"]
    weight = {"civilian": pop["civilian"], "clanless": pop["clanless"],
              "minor": sum(w for c, w in clan_w.items() if c in MINOR), "noble": sum(w for c, w in clan_w.items() if c not in MINOR)}
    whole = sum(weight.values())
    for group, w in weight.items():
        have = sum(dist["by_group"][group].values()) + sum(n for r, n in dist["fixed"].items() if dist["fixed_groups"].get(r) == group)
        want = dist["residents"] * w / whole
        if abs(have - want) > 2:
            errors.append(f"rank_distribution: {group} has {have} residents, population.json gives {want:.1f}")
    named = Counter(bucket(p) for p in people if p.get("on_map", True))
    for r, n in named.items():
        if n > dist["targets"].get(r, 0):
            errors.append(f"rank_distribution: {n} named {r} on the map, but only {dist['targets'].get(r, 0)} in the village")
    if set(dist["outfit_rank"].values()) - {"academy", "genin", "chunin", "jonin", "anbu", "kage", "civilian"}:
        errors.append("rank_distribution: outfit_rank must use the wardrobe's ranks")
    return errors


def table(roster: dict) -> str:
    rows = ["| Role | Placeholder | Rank | Tier | Importance | Clan | Specialty | First | Levels (Academy / Genin / Exams) |",
            "|---|---|---|---|---|---|---|---|---|"]
    for p in roster["people"]:
        lv = p["levels"]
        clan = "masked" if p.get("masked") else (p["clan"] or "clanless") if p["clan"] is not None else "—"
        rank = p["rank"].replace("_", " ")
        rows.append(f"| `{p['role']}` | {p['placeholder']} | {rank} | {p['tier']} | {p['importance']} | {clan} | {p['specialty']} | {p['first']} | "
                    f"{lv['academy']} / {lv['genin']} / {lv['exams']} |")
    return "\n".join(rows)


def counts(roster: dict, dist: dict) -> str:
    met = {s: Counter() for s in roster["slices"]}
    for p in roster["people"]:
        met[p["first"]][bucket(p)] += 1
    order = list(dist["targets"])
    out = ["| Rank | On the map | Named, first met in Beta 1 / 2 / 2.5 / 3 | Lore (the whole village) |", "|---|---|---|---|"]
    for r in order:
        if r == "civilian":
            continue
        m = " / ".join(str(met[s][r]) for s in ("beta1", "beta2", "beta2.5", "beta3"))
        out.append(f"| {r.replace('_', ' ')} | {dist['targets'][r]} | {m} | {dist['lore'].get(r, '—')} |")
    return "\n".join(out)


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--check", action="store_true")
    ap.add_argument("--table", action="store_true")
    ap.add_argument("--counts", action="store_true")
    args = ap.parse_args(argv)
    roster, dist = load("roster.json"), load("rank_distribution.json")
    if args.table:
        print(table(roster))
    if args.counts:
        print(counts(roster, dist))
    errors = check(roster, dist)
    if errors:
        print("\n".join(errors))
        return 1
    if args.check or not (args.table or args.counts):
        print(f"Roster current: {len(roster['people'])} named shinobi, {len(roster.get('civilians', []))} civilians, "
              f"{dist['residents']} residents by rank")
    return 0


if __name__ == "__main__":
    sys.exit(main())
