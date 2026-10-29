#!/usr/bin/env python3
"""The Leaf's named shinobi and how many of each rank live in the village (docs/RANKS.md).

roster.json lists every named shinobi of the beta by role: public rank, power tier, importance, clan and clan
power, specialty, first appearance and level by story stretch. rank_distribution.json is how the population
sampler gives every other resident a rank and a level. This tool checks both against each other, the level
curve, the wardrobe's clans, looks and family names, and population.json, and prints the tables RANKS.md quotes.

    python tools/roster/roster.py --check     # validate (CI)
    python tools/roster/roster.py --table     # the roster as a Markdown table
    python tools/roster/roster.py --counts    # head counts: on the map, met per slice, lore
    python tools/roster/roster.py --power     # average level by rank and clan power
"""
from __future__ import annotations

import argparse
import json
import random
import re
import sys
from collections import Counter
from pathlib import Path

TOOL = Path(__file__).resolve().parent
ROOT = TOOL.parent.parent
WARDROBE = ROOT / "tools" / "wardrobe"

STRETCHES = ("academy", "genin", "exams", "chunin", "jonin", "road")
TIERS = (("S", 50), ("A", 42), ("B", 30), ("C", 15), ("D", 5), ("E", 1))
# The four great clans and the ten minor clans (CLANS.md); the other eleven noble clans are strong.
GREAT = {"uchiha", "hyuga", "senju", "uzumaki"}
MINOR = {"shiranui", "morino", "umino", "haruno", "namiashi", "hagane", "kinoshita", "tsuchigumo", "suzuran", "tobari"}
CLAN_POWER = ("great", "strong", "minor", "clanless")
# Words that would hint at a story secret; this file is read by people who play the game.
SPOILER_WORDS = re.compile(r"\b(traitor|betray\w*|suspicious|suspect\w*|spy|mole|twist|fate|dies|death|killed|secret\w*|kagari|y[uū]gure|"
                           r"hokage_[5-8]|fifth|sixth|seventh|eighth|future hokage|lineage)\b", re.I)


def tier(level: int) -> str:
    return next(t for t, floor in TIERS if level >= floor)


def power_of(clan: str) -> str:
    return "unknown" if clan == "unknown" else "clanless" if clan == "none" else "great" if clan in GREAT else "minor" if clan in MINOR else "strong"


def group_of(clan: str) -> str:
    return "clanless" if clan == "none" else "minor" if clan in MINOR else "noble"


def load(name: str) -> dict:
    return json.loads((TOOL / name).read_text(encoding="utf-8"))


def first_level(p: dict) -> int:
    """The level at which the player first sees them: the class on day one at 1, the squad a year ahead at 10, everyone else at their slice."""
    if p.get("grows"):
        return 1 if p.get("group") == "class" else 10
    lv = p["levels"]
    return lv["exams"] if p["first"] == "beta3" else lv["genin"] if p["first"] in ("beta2", "beta2.5") else lv["academy"]


def bucket(p: dict) -> str:
    """The rank_distribution category a named person fills."""
    return "elite_jonin" if p["rank"] == "jonin" and p.get("tier") == "A" else p["rank"]


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


def check_name(p: dict, clans: dict, pool: set) -> list[str]:
    """Given name first, family last; clan members carry the clan's name, everyone else an ordinary one that says so."""
    role, clan, given, family = p["role"], p.get("clan"), p.get("given"), p.get("family")
    if p.get("name") != "{name:%s}" % role:
        return [f"{role}: name must be the token {{name:{role}}}"]
    if p.get("masked"):
        return [] if given is None and family is None and clan == "unknown" else [f"{role}: a masked ANBU has no name or clan in the beta"]
    if p.get("rank") == "kage":
        return [] if family is None and p.get("placeholder") == given else [f"{role}: a Hokage goes by given name only"]
    errors = []
    if not given or not family:
        return [f"{role}: needs a given and a family name"]
    if clan == "none":
        if family not in pool:
            errors.append(f"{role}: a clanless family name comes from population.json's family_names ({family})")
        if family.lower() in clans or family in clans.values():
            errors.append(f"{role}: {family} is a clan's name")
        want = f"{given} {family} (no clan)"
    else:
        if clans.get(clan) != family:
            errors.append(f"{role}: a {clan} carries the clan's name ({clans.get(clan)}), not {family}")
        want = f"{given} {family}"
    if p.get("placeholder") != want:
        errors.append(f"{role}: placeholder should read '{want}'")
    return errors


def check(roster: dict, dist: dict) -> list[str]:
    errors = []
    people, civilians = roster["people"], roster.get("civilians", [])
    ranks, slices = set(roster["ranks"]), set(roster["slices"])
    clans = {p.stem: json.loads(p.read_text(encoding="utf-8"))["name"] for p in (WARDROBE / "clans").glob("*.json")}
    looks = {json.loads(p.read_text(encoding="utf-8"))["id"] for p in (WARDROBE / "characters").glob("*.json")}
    pop = json.loads((WARDROBE / "population.json").read_text(encoding="utf-8"))
    pool = set(pop["family_names"])
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
        if p.get("rank") not in ranks:
            errors.append(f"{role}: unknown rank {p.get('rank')}")
        if p.get("first") not in slices:
            errors.append(f"{role}: first must be one of {', '.join(sorted(slices))}")
        clan = p.get("clan")
        if clan not in clans and clan not in ("none", "unknown"):
            errors.append(f"{role}: clan must be a clan id, none (clanless) or unknown (masked), not {clan}")
        errors += check_name(p, clans, pool)
        for word in SPOILER_WORDS.findall(" ".join(strings(p))):
            errors.append(f"{role}: '{word}' does not belong in a spoiler-free file")
    for p in people:
        role = p["role"]
        if p.get("importance") not in roster["importance"]:
            errors.append(f"{role}: importance is one of {', '.join(roster['importance'])}")
        if p.get("spotlight") not in roster["spotlight"]:
            errors.append(f"{role}: spotlight is one of {', '.join(roster['spotlight'])}")
        if p.get("clan_power") != power_of(p["clan"]):
            errors.append(f"{role}: clan_power should be {power_of(p['clan'])}")
        if p.get("look") and p["look"] not in looks:
            errors.append(f"{role}: unknown look {p['look']} (tools/wardrobe/characters)")
        if p.get("job") and p["job"] not in dist["jobs"]:
            errors.append(f"{role}: unknown job {p['job']} (rank_distribution.json jobs)")
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
            if any(lv[a] > lv[b] for a, b in zip(STRETCHES, STRETCHES[1:])):
                errors.append(f"{role}: levels never go down")
            for s in STRETCHES:
                if p.get("group") == "class" and not player[s] - 3 <= lv[s] <= player[s] + 3:
                    errors.append(f"{role}: {s} level {lv[s]} is more than 3 from the player's {player[s]}")
                if p.get("group") == "seniors" and lv[s] < player[s] - 1:
                    errors.append(f"{role}: the squad a year ahead stays ahead ({s} {lv[s]} against {player[s]})")
    # Squads: the year makes four squads of three with the player; the squad a year ahead is the fifth.
    squads = roster["squads"]
    year = [m for sid, s in squads.items() if sid != "squad_5" for m in s["members"]]
    klass = [p["role"] for p in people if p.get("group") == "class"]
    if sorted(m for m in year if m != "player") != sorted(klass) or len(year) != 12:
        errors.append("squads: your year is four squads of three, and every classmate is on exactly one")
    if any(len(s["members"]) != 3 for s in squads.values()):
        errors.append("squads: three to a squad")
    for sid, s in squads.items():
        for m in s["members"] + [s["sensei"]] + s.get("bench", []):
            if m != "player" and m not in seen:
                errors.append(f"{sid}: unknown member {m}")
        leader = next((p for p in people if p["role"] == s["sensei"]), None)
        if leader is None or leader.get("leads") != sid:
            errors.append(f"{sid}: its sensei must say leads: {sid}")
    for word in SPOILER_WORDS.findall(" ".join(strings(squads))):
        errors.append(f"squads: '{word}' does not belong in a spoiler-free file")
    # The year leans toward the noble clans, by the weights Varied saves roll with.
    w = {k: v for k, v in roster["class_clan_weights"].items() if k != "_doc"}
    if abs(sum(w.values()) - 1) > 1e-9:
        errors.append("class_clan_weights: the weights sum to 1")
    mix = Counter(group_of(p["clan"]) for p in people if p.get("group") == "class")
    for g, share in w.items():
        if abs(mix[g] - share * len(klass)) > 1.5:
            errors.append(f"class_clan_weights: the Classic class has {mix[g]} {g}, the weights give {share * len(klass):.1f}")
    # The rank distribution: it adds up, matches the population's shares, and has room for the named roster.
    total = Counter()
    for weights in dist["by_group"].values():
        total.update(weights)
    total.update(dist["fixed"])
    if dict(total) != dist["targets"]:
        errors.append(f"rank_distribution: by_group + fixed {dict(total)} != targets {dist['targets']}")
    if sum(dist["targets"].values()) != dist["residents"]:
        errors.append(f"rank_distribution: targets sum to {sum(dist['targets'].values())}, not {dist['residents']}")
    for r, groups in dist["fixed_groups"].items():
        if sum(groups.values()) != dist["fixed"].get(r):
            errors.append(f"rank_distribution: fixed_groups for {r} must add up to fixed")
    clan_w = pop["clans"]
    weight = {"civilian": pop["civilian"], "clanless": pop["clanless"],
              "minor": sum(v for c, v in clan_w.items() if c in MINOR), "noble": sum(v for c, v in clan_w.items() if c not in MINOR)}
    whole = sum(weight.values())
    for group, wt in weight.items():
        have = sum(dist["by_group"][group].values()) + sum(g.get(group, 0) for g in dist["fixed_groups"].values())
        want = dist["residents"] * wt / whole
        if abs(have - want) > 2:
            errors.append(f"rank_distribution: {group} has {have} residents, population.json gives {want:.1f}")
    named = Counter(bucket(p) for p in people if p.get("on_map", True))
    for r, n in named.items():
        if n > dist["targets"].get(r, 0):
            errors.append(f"rank_distribution: {n} named {r} on the map, but only {dist['targets'].get(r, 0)} in the village")
    if set(dist["outfit_rank"].values()) - {"academy", "genin", "chunin", "jonin", "anbu", "kage", "civilian"}:
        errors.append("rank_distribution: outfit_rank must use the wardrobe's ranks")
    if set(dist["rank_levels"]) - {"_doc"} != set(dist["targets"]) - {"kage", "elder", "jonin_commander", "anbu"}:
        errors.append("rank_distribution: rank_levels covers every drawn rank")
    if [k for k in dist["clan_power"] if k != "_doc"] != list(CLAN_POWER):
        errors.append(f"rank_distribution: clan_power tiers are {', '.join(CLAN_POWER)}")
    if dist["clan_power"]["great"]["clans"] != sorted(GREAT, key=["uchiha", "hyuga", "senju", "uzumaki"].index):
        errors.append("rank_distribution: the great clans are the Uchiha, Hyuga, Senju and Uzumaki")
    return errors


def table(roster: dict) -> str:
    rows = ["| Role | Placeholder name | Rank | Tier | Importance | Spotlight | Clan (power) | Specialty | First | Levels (Academy / Genin / Exams) |",
            "|---|---|---|---|---|---|---|---|---|---|"]
    for p in roster["people"]:
        lv = p["levels"]
        clan = "masked" if p.get("masked") else "none (clanless)" if p["clan"] == "none" else f"{p['clan']} ({p['clan_power']})"
        name = p["placeholder"] + (" *" if p.get("provisional") else "")
        rows.append(f"| `{p['role']}` | {name} | {p['rank'].replace('_', ' ')} | {p['tier']} | {p['importance']} | {p['spotlight']} | {clan} | "
                    f"{p['specialty']} | {p['first']} | {lv['academy']} / {lv['genin']} / {lv['exams']} |")
    return "\n".join(rows)


def counts(roster: dict, dist: dict) -> str:
    met = {s: Counter() for s in roster["slices"]}
    for p in roster["people"]:
        met[p["first"]][bucket(p)] += 1
    out = ["| Rank | On the map | Named, first met in Beta 1 / 2 / 2.5 / 3 | Lore (the whole village) |", "|---|---|---|---|"]
    for r in dist["targets"]:
        if r == "civilian":
            continue
        m = " / ".join(str(met[s][r]) for s in ("beta1", "beta2", "beta2.5", "beta3"))
        out.append(f"| {r.replace('_', ' ')} | {dist['targets'][r]} | {m} | {dist['lore'].get(r, '—')} |")
    return "\n".join(out)


def power(dist: dict) -> str:
    """Average level of drawn residents by rank and clan power (the same draw as life:roster's ClanPower.roll)."""
    rng = random.Random(20261029)
    out = ["| Rank | Spread | " + " | ".join(CLAN_POWER) + " | Clanless above the great clans' median |", "|---|---|" + "---|" * (len(CLAN_POWER) + 1)]
    for r, (mean, sd, lo, hi) in ((k, v) for k, v in dist["rank_levels"].items() if k not in ("_doc", "civilian")):
        cells, draws = [], {}
        for tier_id in CLAN_POWER:
            shift = dist["clan_power"][tier_id]["shift"]
            draws[tier_id] = sorted(min(hi, max(lo, mean + (shift + rng.gauss(0, 1)) * sd)) for _ in range(20000))
            cells.append(f"{sum(draws[tier_id]) / len(draws[tier_id]):.1f}")
        median = draws["great"][len(draws["great"]) // 2]
        above = sum(1 for x in draws["clanless"] if x > median) / len(draws["clanless"])
        out.append(f"| {r.replace('_', ' ')} | {lo}–{hi} | " + " | ".join(cells) + f" | {100 * above:.0f}% |")
    return "\n".join(out)


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--check", action="store_true")
    ap.add_argument("--table", action="store_true")
    ap.add_argument("--counts", action="store_true")
    ap.add_argument("--power", action="store_true")
    args = ap.parse_args(argv)
    roster, dist = load("roster.json"), load("rank_distribution.json")
    for flag, fn in ((args.table, lambda: table(roster)), (args.counts, lambda: counts(roster, dist)), (args.power, lambda: power(dist))):
        if flag:
            print(fn())
    errors = check(roster, dist)
    if errors:
        print("\n".join(errors))
        return 1
    if args.check or not (args.table or args.counts or args.power):
        print(f"Roster current: {len(roster['people'])} named shinobi, {len(roster.get('civilians', []))} civilians, "
              f"{dist['residents']} residents by rank")
    return 0


if __name__ == "__main__":
    sys.exit(main())
