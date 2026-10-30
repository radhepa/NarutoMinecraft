#!/usr/bin/env python3
"""Compile and check the Mission Desk's board-mission templates.

    python tools/missions/missions.py            # compile every template and table into the datapack
    python tools/missions/missions.py --check    # validate only; fails if the compiled JSON is stale
    python tools/missions/missions.py --doc      # also write docs/missions/CATALOGUE.md
    python tools/missions/missions.py --summary  # counts by rank, category and status

Templates live in tools/missions/catalogue/ (one module per rank group) and compile to one JSON file each
under adventure/data/shinobi_adventure/missions/templates/<rank>/, with economy.json, desk.json,
clients.json, squad.json and needs.json beside them. MISSIONS.md explains the format.
"""
import json
import os
import sys
from collections import Counter, defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(HERE, "catalogue"))

from mkit import BONUSES, RANKS  # noqa: E402
import d_rank  # noqa: E402
import c_rank  # noqa: E402
import later_ranks  # noqa: E402
import tables  # noqa: E402

ROOT = os.path.normpath(os.path.join(HERE, "..", ".."))
OUT = os.path.join(ROOT, "adventure", "data", "shinobi_adventure", "missions")
DOC = os.path.join(ROOT, "docs", "missions", "CATALOGUE.md")

OBJECTIVES = {"go", "talk", "inspect", "collect", "deliver", "craft", "buy", "defeat", "escort", "protect",
              "survive", "sneak", "perform", "wait_until", "sleep", "choose"}
CONDITIONS = {"all", "any", "not", "flag", "rank_at_least", "rank_at_most", "level_at_least", "quest_state",
              "friendship", "clan", "clanless", "time_between", "calendar", "knows_technique", "standing",
              "squad_cohesion", "twist", "chose", "event_active", "client_is"}
ACTIONS = {"spawn_group", "bond_event", "mission_outcome", "lead", "set_flag", "give_item", "deed", "clan_deed",
           "favor", "shared_moment"}
RANK_ORDER = {r: i for i, r in enumerate(RANKS)}


def templates():
    return d_rank.T + c_rank.T + later_ranks.T


def file_for(t):
    rank_dir = "anbu" if t["category"] == "anbu" else t["rank"]
    return os.path.join(OUT, "templates", rank_dir, t["id"].split(".")[-1] + ".json")


def walk_strings(x):
    if isinstance(x, str):
        yield x
    elif isinstance(x, dict):
        for v in x.values():
            yield from walk_strings(v)
    elif isinstance(x, list):
        for v in x:
            yield from walk_strings(v)


def walk_conditions(c):
    if isinstance(c, dict):
        for k, v in c.items():
            yield k, v
            if k in ("all", "any"):
                for sub in v:
                    yield from walk_conditions(sub)
            elif k == "not":
                yield from walk_conditions(v)


def derive_places(t):
    """Anchors are every anchor slot's tag plus every literal place the steps name; regions likewise."""
    anchors, regions = set(), set(t["places"]["regions"])
    for slot in t["slots"].values():
        if slot.get("pick") == "anchor":
            anchors.add(slot["tag"])
        if slot.get("pick") == "region":
            regions.update(slot["from"])
    for s in walk_strings(t["steps"]):
        if s.startswith("place:"):
            anchors.add(s[len("place:"):])
    return sorted(anchors), sorted(regions)


def spawned_groups(t):
    groups = set()
    for step in t["steps"].values():
        for action in step.get("on_enter", []) + step.get("on_done", []):
            if "spawn_group" in action:
                groups.add(action["spawn_group"][0])
        if step["objective"]["type"] == "defeat":
            groups.add(step["objective"]["group"])
    return groups


def check(t, ids):
    p = []
    tid = t["id"]
    err = lambda msg: p.append(f"{tid}: {msg}")
    parts = tid.split(".")
    if parts[0] != "mission" or (parts[1] != t["rank"] and not (parts[1] == "anbu" and t["category"] == "anbu")):
        err("id must be mission.<rank>.<name> (or mission.anbu.<name>)")
    if ids[tid] > 1:
        err("duplicate id")
    if t["rank"] in ("b", "a", "s") and t["status"] != "later":
        err("B, A and S templates are later content")
    if not 0 <= t["pay"]["weight"] <= 1:
        err("pay weight outside 0..1")
    steps = t["steps"]
    if t["start"] not in steps:
        err("start step missing")
    slots = set(t["slots"])
    twist_ids = {tw["id"] for tw in t["twists"]}
    branch_twists = set()
    choose_options = {name: set(s["objective"]["options"]) for name, s in steps.items() if s["objective"]["type"] == "choose"}
    outcomes = set(t["outcomes"])
    if "done" not in outcomes:
        err("every template needs a 'done' outcome")
    for name, s in steps.items():
        o = s["objective"]
        if o["type"] not in OBJECTIVES:
            err(f"step {name}: unknown objective {o['type']}")
        targets = [s["next"]] + [b["next"] for b in s.get("branch", [])]
        for n in targets:
            if n is not None and n not in steps:
                err(f"step {name}: next '{n}' does not exist")
        for b in s.get("branch", []):
            for k, v in walk_conditions(b["if"]):
                if k not in CONDITIONS:
                    err(f"step {name}: unknown condition {k}")
                if k == "twist":
                    branch_twists.add(v)
                    if v not in twist_ids:
                        err(f"step {name}: branch on undeclared twist {v}")
                if k == "chose":
                    if v[0] not in choose_options or v[1] not in choose_options[v[0]]:
                        err(f"step {name}: chose {v} names no option")
        if o["type"] == "choose":
            for opt, out in o["options"].items():
                if out is not None and out not in outcomes:
                    err(f"step {name}: option {opt} leads to unknown outcome {out}")
        for action in s.get("on_enter", []) + s.get("on_done", []):
            for k in action:
                if k not in ACTIONS:
                    err(f"step {name}: unknown action {k}")
            if "mission_outcome" in action and action["mission_outcome"] not in outcomes:
                err(f"step {name}: ends in unknown outcome {action['mission_outcome']}")
        for b in s.get("bonus", []):
            if b not in BONUSES:
                err(f"step {name}: unknown bonus {b}")
    # Reachability from the start, and every step reaches an end.
    seen, todo = set(), [t["start"]]
    while todo:
        n = todo.pop()
        if n in seen or n not in steps:
            continue
        seen.add(n)
        s = steps[n]
        todo += [x for x in [s["next"]] + [b["next"] for b in s.get("branch", [])] if x]
    for n in steps:
        if n not in seen:
            err(f"step {n} is unreachable")
    ends = {n for n, s in steps.items() if s["next"] is None}
    changed = True
    reaches = set(ends)
    while changed:
        changed = False
        for n, s in steps.items():
            if n not in reaches and any(x in reaches for x in [s["next"]] + [b["next"] for b in s.get("branch", [])] if x):
                reaches.add(n)
                changed = True
    for n in steps:
        if n not in reaches:
            err(f"step {n} never reaches an end")
    for tw in t["twists"]:
        if not tw.get("modifier") and tw["id"] not in branch_twists:
            err(f"twist {tw['id']} has no branch (mark it modifier if it changes rules only)")
    # Slot references.
    for s in walk_strings({"steps": steps, "outcomes": t["outcomes"]}):
        if s.startswith("slot:"):
            base = s[len("slot:"):].split(".")[0]
            if base not in slots:
                err(f"unknown slot {s}")
    for name, slot in t["slots"].items():
        if slot.get("pick") == "suspect":
            for other in slot["from"]:
                if other not in slots:
                    err(f"suspect slot {name} names unknown slot {other}")
        if slot.get("pick") == "enemy_group":
            for g in slot["from"]:
                if g not in t["enemies"]:
                    err(f"enemy group {g} in slot {name} is not listed in enemies")
    for g in spawned_groups(t):
        if not g.startswith("slot:") and g not in t["enemies"]:
            err(f"spawned group {g} is not listed in enemies")
    for b in t["bonus"]:
        if b not in BONUSES:
            err(f"unknown bonus {b}")
    if "fast" in t["bonus"] and not t.get("fast_hours"):
        err("bonus 'fast' needs fast_hours")
    if "unlock" in t:
        for k, _ in walk_conditions(t["unlock"]):
            if k not in CONDITIONS:
                err(f"unlock uses unknown condition {k}")
    if t["rank"] in ("c", "b", "a", "s") and not t["enemies"] and t["category"] not in ("mediation", "medical", "anbu", "investigation"):
        err("C rank and above should have a real fight (enemies)")
    if len(t["twists"]) < 2:
        err("every template needs at least two twists")
    return p


def item_id(name):
    if ":" in name or name in tables.CREATURES:
        return name
    return tables.REUSED_ITEMS.get(name, "item:mission_" + name)


def compiled(t):
    t = dict(t)
    for step in t["steps"].values():
        o = step["objective"]
        if o["type"] in ("collect", "deliver", "craft", "buy"):
            for k in ("item", "target"):
                if isinstance(o.get(k), str) and not o[k].startswith(("slot:", "place:", "role:")):
                    o[k] = item_id(o[k])
    anchors, regions = derive_places(t)
    t["places"] = {"anchors": anchors, "regions": regions}
    return t


def needs(ts):
    anchors, regions, groups, items, performs = defaultdict(set), defaultdict(set), defaultdict(set), defaultdict(set), defaultdict(set)
    for t in ts:
        for a in t["places"]["anchors"]:
            anchors[a].add(t["id"])
        for r in t["places"]["regions"]:
            regions[r].add(t["id"])
        for g in t["enemies"]:
            groups[g].add(t["id"])
        for step in t["steps"].values():
            o = step["objective"]
            for k in ("item", "target"):
                v = o.get(k)
                if isinstance(v, str) and not v.startswith(("slot:", "place:", "role:")) and o["type"] in ("collect", "deliver", "craft", "buy"):
                    items[v].add(t["id"])
            if o["type"] == "perform":
                performs[o["what"]].add(t["id"])
    fmt = lambda d: {k: sorted(v) for k, v in sorted(d.items())}
    beta = {t["id"] for t in ts if t["status"] == "beta"}
    in_beta = lambda d: sorted(k for k, v in d.items() if v & beta)
    return {"format": 1,
            "_doc": "What the mission templates ask of other sessions: anchors (Konoha build), regions (map), enemy groups (combat), items (items), perform ids (combat and life). Generated by tools/missions/missions.py.",
            "anchors": fmt(anchors), "regions": fmt(regions), "enemy_groups": fmt(groups),
            "items": fmt(items), "performs": fmt(performs),
            "collectibles": {k: v for k, v in tables.ECONOMY["collectibles"]["keepsakes"].items() if not k.startswith("_")},
            "beta": {"anchors": in_beta(anchors), "regions": in_beta(regions), "enemy_groups": in_beta(groups),
                     "items": in_beta(items), "performs": in_beta(performs)}}


def dump(obj):
    return json.dumps(obj, indent=1, ensure_ascii=False) + "\n"


def outputs(ts):
    out = {file_for(t): dump(t) for t in ts}
    out[os.path.join(OUT, "economy.json")] = dump(tables.ECONOMY)
    out[os.path.join(OUT, "desk.json")] = dump(tables.DESK)
    out[os.path.join(OUT, "clients.json")] = dump(tables.CLIENTS)
    out[os.path.join(OUT, "squad.json")] = dump(tables.SQUAD)
    out[os.path.join(OUT, "needs.json")] = dump(needs(ts))
    return out


def check_tables(ts):
    p = []
    ids = {t["id"] for t in ts}
    for tid in tables.DESK["classic_opening"]:
        if tid not in ids:
            p.append(f"desk.json: classic opening names unknown template {tid}")
    for chain in tables.CLIENTS["chains"]:
        for tid in chain.get("templates", []) + [s["template"] for s in chain.get("stages", [])]:
            if tid not in ids:
                p.append(f"clients.json: {chain['id']} names unknown template {tid}")
            else:
                t = next(x for x in ts if x["id"] == tid)
                if t.get("chain") != chain["id"]:
                    p.append(f"clients.json: {tid} is in {chain['id']} but its template says chain={t.get('chain')}")
    for tid in tables.ECONOMY["collectibles"]["keepsakes"]:
        if not tid.startswith("_") and tid not in ids:
            p.append(f"economy.json: keepsake for unknown template {tid}")
    for t in ts:
        if t.get("chain") and not any(c["id"] == t["chain"] for c in tables.CLIENTS["chains"]):
            p.append(f"{t['id']}: unknown chain {t['chain']}")
    return p


def catalogue_doc(ts):
    lines = ["# Mission catalogue", "",
             "Generated by `python tools/missions/missions.py --doc` from `tools/missions/catalogue/`; do not edit by hand.",
             "Spoiler-free: premises and twists as the player meets them. The design is in [MISSIONS.md](../../MISSIONS.md).", ""]
    by_rank = defaultdict(list)
    for t in ts:
        by_rank["anbu" if t["category"] == "anbu" else t["rank"]].append(t)
    names = {"d": "D rank", "c": "C rank", "b": "B rank", "a": "A rank", "s": "S rank", "anbu": "ANBU operations"}
    lines += ["| Rank | Templates | Beta | Later | Twists |", "|---|---|---|---|---|"]
    for r in ("d", "c", "b", "a", "s", "anbu"):
        rs = by_rank[r]
        lines.append(f"| {names[r]} | {len(rs)} | {sum(t['status'] == 'beta' for t in rs)} | {sum(t['status'] == 'later' for t in rs)} | {sum(len(t['twists']) for t in rs)} |")
    lines.append(f"| **All** | **{len(ts)}** | {sum(t['status'] == 'beta' for t in ts)} | {sum(t['status'] == 'later' for t in ts)} | {sum(len(t['twists']) for t in ts)} |")
    for r in ("d", "c", "b", "a", "s", "anbu"):
        lines += ["", f"## {names[r]}", "", "| Id | Category | Party | Min | Premise | Twists | Fights | Places |", "|---|---|---|---|---|---|---|---|"]
        for t in sorted(by_rank[r], key=lambda x: (x["category"], x["id"])):
            tw = "; ".join(f"*{k}*: {v}" for k, v in t.get("_twists", {}).items())
            places = ", ".join([f"`{a}`" for a in t["places"]["anchors"]] + [f"`{x}`" for x in t["places"]["regions"]])
            fights = ", ".join(f"`{g}`" for g in t["enemies"]) or "—"
            mins = f"{t['minutes']}" + (f" ({t['days']} d)" if t.get("days") else "")
            lines.append(f"| `{t['id']}` | {t['category']} | {t['party']} | {mins} | {t['_premise']} | {tw} | {fights} | {places} |")
    return "\n".join(lines) + "\n"


def main(argv):
    ts = [compiled(t) for t in templates()]
    ids = Counter(t["id"] for t in ts)
    problems = [x for t in ts for x in check(t, ids)] + check_tables(ts)
    if "--summary" in argv or not problems:
        by = Counter((t["rank"] if t["category"] != "anbu" else "anbu") for t in ts)
        cats = Counter(t["category"] for t in ts)
        print(f"{len(ts)} templates: " + ", ".join(f"{k} {v}" for k, v in sorted(by.items(), key=lambda kv: "dcbasanbu".find(kv[0]))))
        print(f"{len(cats)} categories, {sum(len(t['twists']) for t in ts)} twists, "
              f"{sum(t['status'] == 'beta' for t in ts)} beta and {sum(t['status'] == 'later' for t in ts)} later")
    if problems:
        print("\n".join(problems))
        print(f"{len(problems)} problems")
        return 1
    files = outputs(ts)
    if "--check" in argv:
        stale = [f for f, text in files.items() if not os.path.exists(f) or open(f, encoding="utf-8").read() != text]
        known = set(files)
        tdir = os.path.join(OUT, "templates")
        extra = [os.path.join(d, f) for d, _, fs in os.walk(tdir) for f in fs if os.path.join(d, f) not in known] if os.path.isdir(tdir) else []
        if stale or extra:
            print("stale compiled files (run missions.py):", *sorted(os.path.relpath(f, ROOT) for f in stale + extra), sep="\n  ")
            return 1
        print("ok")
        return 0
    tdir = os.path.join(OUT, "templates")
    if os.path.isdir(tdir):
        for d, _, fs in os.walk(tdir):
            for f in fs:
                if os.path.join(d, f) not in files:
                    os.remove(os.path.join(d, f))
    for f, text in files.items():
        os.makedirs(os.path.dirname(f), exist_ok=True)
        with open(f, "w", encoding="utf-8", newline="\n") as fh:
            fh.write(text)
    print(f"wrote {len(files)} files under {os.path.relpath(OUT, ROOT)}")
    if "--doc" in argv:
        os.makedirs(os.path.dirname(DOC), exist_ok=True)
        with open(DOC, "w", encoding="utf-8", newline="\n") as fh:
            fh.write(catalogue_doc(ts))
        print(f"wrote {os.path.relpath(DOC, ROOT)}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
