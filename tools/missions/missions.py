#!/usr/bin/env python3
"""Compile and check the Mission Desk's board-mission templates.

    python tools/missions/missions.py            # compile every template and table into the datapack
    python tools/missions/missions.py --check    # validate only; fails if the compiled JSON is stale
    python tools/missions/missions.py --doc      # also write docs/missions/CATALOGUE.md
    python tools/missions/missions.py --summary  # counts by rank, category and status
    python tools/missions/missions.py --quests   # check only the quest files (also part of --check)

Templates live in tools/missions/catalogue/ (one module per rank group) and compile to one JSON file each
under adventure/data/shinobi_adventure/missions/templates/<rank>/, with economy.json, desk.json,
clients.json, squad.json and needs.json beside them. MISSIONS.md explains the format.
Quests (*/src/main/resources/data/<ns>/quests/*.json, run by Shinobi Progression) are checked against the test
street's map: its anchors and bound roles from tools/konoha/blueprints.
"""
import glob
import json
import re
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
# Technique ids a quest may teach, as the combat runtime loads them: the technique files and each clan's.
def _techniques():
    ids = set()
    for f in glob.glob(os.path.join(ROOT, "data", "combat", "techniques", "*.json")):
        with open(f, encoding="utf-8") as fh:
            ids |= {t["id"] for t in json.load(fh).get("techniques", [])}
    for f in glob.glob(os.path.join(ROOT, "data", "combat", "clans", "[!_]*.json")):
        with open(f, encoding="utf-8") as fh:
            c = json.load(fh)
        ids |= {t["id"] for t in c.get("techniques", [])} | ({c["lesser"]["id"]} if c.get("lesser") else set())
    return ids


TECHNIQUES = _techniques()
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

# The quest runtime's vocabulary (progression/.../Quests.java) and the test street it casts quests on.
# shortcut: the map's built plots and saved anchors mirror TestStreet.build and firstStart, until the map's anchors are data.
QUEST_STEPS = {"go", "spar", "talk", "furnish", "sleep", "scene", "choose", "cast"}
RANKS = {"academy", "genin", "chunin", "jonin", "anbu", "hokage"}
QUEST_CONDITIONS = {"all", "any", "not", "flag", "quest_state"}
QUEST_STATES = {"done", "active", "not_started"}
STREET_ANCHORS = {"notice_board", "anchor:training", "anchor:hokage_office", "anchor:academy.grounds", "anchor:academy.yard", "anchor:academy.library"}
PLAYER_FLAT = "flat.leaf_block.3a"
BAD_QUEST = os.path.join(HERE, "fixtures", "quest.bad.json")
MISSING_QUEST = os.path.join(ROOT, "progression", "src", "gametest", "resources", "data", "shinobi_progression_tests", "quests", "errand.test.missing.json")


def street():
    """The anchor keys and role keys (role:x, job:x) the Leaf map saves when it is pasted (tools/konoha/layout.json)."""
    anchors, roles = {PLAYER_FLAT}, set()
    with open(os.path.join(ROOT, "tools", "konoha", "layout.json"), encoding="utf-8") as fh:
        built = [p["design"] for p in json.load(fh)["plots"] if not p.get("planned")]
    for b in built:
        with open(os.path.join(ROOT, "tools", "konoha", "blueprints", b + ".json"), encoding="utf-8") as fh:
            for m in json.load(fh).get("markers", []):
                if m["type"] in STREET_ANCHORS:
                    anchors.add(m["type"])
                elif m["type"] == "resident":
                    if "role" in m:
                        roles.add("role:" + m["role"])
                    if m.get("job", "any") != "any":
                        roles.add("job:" + m["job"])
    return anchors, roles


def quest_files():
    return sorted(glob.glob(os.path.join(ROOT, "*", "src", "main", "resources", "data", "*", "quests", "*.json")))


def slot_key(slot):
    pick = slot.get("pick") if isinstance(slot, dict) else None
    if pick == "resident" and isinstance(slot.get("where"), dict) and isinstance(slot["where"].get("job"), str):
        return "job:" + slot["where"]["job"]
    if pick == "role" and isinstance(slot.get("role"), str):
        return "role:" + slot["role"]
    if pick == "anchor" and isinstance(slot.get("tag"), str):
        return "anchor:" + slot["tag"]
    return None


def lang_keys(quest_file):
    """The lang keys of the module that holds the quest file (its assets/*/lang/en_us.json)."""
    module = quest_file.replace(os.sep, "/").split("/src/main/resources/")[0]
    keys = set()
    for f in glob.glob(os.path.join(module, "src", "main", "resources", "assets", "*", "lang", "en_us.json")):
        with open(f, encoding="utf-8") as fh:
            keys |= set(json.load(fh))
    return keys


def check_quests(files, map_data=None):
    """
    Every problem in the quest files, as `file: quest/step: problem`; quest ids and flags are checked across all files,
    and each line said, choice and step name against its module's lang file.
    """
    anchors, roles = map_data or street()
    quests, problems = {}, []
    for f in files:
        rel = os.path.relpath(f, ROOT).replace(os.sep, "/")
        try:
            with open(f, encoding="utf-8") as fh:
                q = json.load(fh)
        except (OSError, ValueError) as e:
            problems.append(f"{rel}: cannot read: {e}")
            continue
        qid = q.get("id") if isinstance(q, dict) else None
        if not isinstance(qid, str):
            problems.append(f"{rel}: no string id")
            continue
        if qid in quests:
            problems.append(f"{rel}: {qid}: duplicate id (also {quests[qid][0]})")
        quests[qid] = (rel, q)
    all_steps = [s for _, q in quests.values() for s in (q["steps"] if isinstance(q.get("steps"), dict) else {}).values() if isinstance(s, dict)]
    set_flags = {a["set_flag"][0] for s in all_steps
                 for when in ("on_enter", "on_done") for a in s.get(when) or [] if isinstance(a, dict) and isinstance(a.get("set_flag"), list) and a["set_flag"]}
    # A choose step sets <flag>.<option> for the option picked.
    set_flags |= {f"{o['flag']}.{opt}" for s in all_steps for o in [s.get("objective")] if isinstance(o, dict) and o.get("type") == "choose"
                  and isinstance(o.get("flag"), str) and isinstance(o.get("options"), list) for opt in o["options"] if isinstance(opt, str)}
    for qid, (rel, q) in quests.items():
        keys = lang_keys(os.path.join(ROOT, rel))
        def err(where, msg):
            problems.append(f"{rel}: {qid}{'/' + where if where else ''}: {msg}")
        steps = q.get("steps")
        if not isinstance(steps, dict) or not steps:
            err("", "no steps")
            continue
        slots = q.get("slots") or {}
        if not isinstance(slots, dict):
            err("", "slots must be an object")
            slots = {}
        start = q.get("start") if isinstance(q.get("start"), str) else None
        for name, slot in slots.items():
            key = slot_key(slot)
            if key is None:
                err("", f"slot {name} cannot be cast (resident with where.job, role with role, or anchor with tag): {slot}")
            elif key.startswith("anchor:") and key not in anchors:
                err("", f"slot {name}: no {key} on the map (anchors: {', '.join(sorted(anchors))})")
            elif not key.startswith("anchor:") and key not in roles:
                err("", f"slot {name}: no resident with {key} on the map (roles: {', '.join(sorted(roles))})")
        if start not in steps:
            err("", f"no start step {q.get('start')!r}")

        def condition(where, c):
            if not isinstance(c, dict) or len(c) != 1:
                return err(where, f"a condition needs exactly one key: {c}")
            (k, v), = c.items()
            if k not in QUEST_CONDITIONS:
                err(where, f"unknown condition {k} (known: {', '.join(sorted(QUEST_CONDITIONS))})")
            elif k in ("all", "any"):
                if not isinstance(v, list) or not v:
                    return err(where, f"{k} needs a list")
                for x in v:
                    condition(where, x)
            elif k == "not":
                condition(where, v)
            elif k == "flag":
                if not isinstance(v, str):
                    err(where, "flag needs a name")
                elif v not in set_flags:
                    err(where, f"flag {v} is never set by any quest's set_flag")
            elif not (isinstance(v, list) and len(v) == 2 and isinstance(v[0], str) and isinstance(v[1], str) and v[1] in QUEST_STATES):
                err(where, "quest_state needs [quest, done|active|not_started]")
            elif v[0] == qid:
                err(where, "quest_state cannot name its own quest")
            elif v[0] not in quests:
                err(where, f"quest_state names unknown quest {v[0]}")

        for name, s in steps.items():
            if not isinstance(s, dict):
                err(name, "a step must be an object")
                continue
            nxt = s.get("next")
            if nxt is not None and not (isinstance(nxt, str) and nxt in steps):
                err(name, f"next names missing step {nxt!r}")
            for b in s.get("branch") or []:
                if not (isinstance(b, dict) and isinstance(b.get("next"), str) and b["next"] in steps):
                    err(name, f"branch to missing step {b.get('next') if isinstance(b, dict) else b!r}")
                condition(name, b.get("if") if isinstance(b, dict) else None)
            for when in ("on_enter", "on_done"):
                for a in s.get(when) or []:
                    ok = isinstance(a, dict) and len(a) == 1 and (
                        isinstance(a.get("set_flag"), list) and len(a["set_flag"]) == 2 and isinstance(a["set_flag"][0], str) and isinstance(a["set_flag"][1], bool)
                        or type(a.get("give_ryo")) in (int, float) and 1 <= a["give_ryo"] <= 2**31 - 1 and a["give_ryo"] == int(a["give_ryo"])
                        or isinstance(a.get("give_item"), str) and a["give_item"] != ""
                        or isinstance(a.get("teach_technique"), str) and a["teach_technique"] in TECHNIQUES
                        or isinstance(a.get("say"), str) and a["say"] != ""
                        or isinstance(a.get("start_quest"), str) and a["start_quest"] != ""
                        or a.get("set_rank") in RANKS)
                    if not ok:
                        err(name, f"{when}: unknown or malformed action {a} (set_flag [name, true|false], give_ryo <whole ryo, 1 to 2147483647>, give_item <item id>, teach_technique <technique id>, say <lang key>, start_quest <quest id> or set_rank <{'|'.join(sorted(RANKS))}>)")
                    elif "say" in a and a["say"] not in keys:
                        err(name, f"{when}: says {a['say']}, which the lang file lacks")
                    elif "start_quest" in a and a["start_quest"] not in quests:
                        err(name, f"{when}: starts unknown quest {a['start_quest']}")
            o = s.get("objective") or {}
            if not isinstance(o, dict):
                err(name, "objective must be an object")
                continue
            kind = o.get("type", "")
            if not isinstance(kind, str) or kind not in QUEST_STEPS:
                err(name, f"unknown step type {kind!r} (known: {', '.join(sorted(QUEST_STEPS))})")
                continue
            # A scene tells itself; every other step is named (a choice's name is its question).
            if kind != "scene" and f"quest.{qid}.step.{name}" not in keys:
                err(name, f"the lang file lacks quest.{qid}.step.{name}")
            if kind == "choose":
                opts = o.get("options")
                if not (isinstance(o.get("flag"), str) and o["flag"] and isinstance(opts, list) and opts
                        and all(isinstance(x, str) and re.fullmatch(r"[a-z0-9_]+", x) for x in opts) and len(set(opts)) == len(opts)):
                    err(name, "choose step needs a flag and distinct lower-case options")
                else:
                    for x in opts:
                        if f"{o['flag']}.{x}" not in keys:
                            err(name, f"the lang file lacks option {o['flag']}.{x}")
            if kind == "cast" and o.get("technique") not in TECHNIQUES:
                err(name, f"cast step names unknown technique {o.get('technique')!r}")
            field = {"go": "place", "spar": "place", "talk": "who"}.get(kind)
            if field is None:
                continue
            ref = o.get(field)
            if not isinstance(ref, str) or not ref:
                err(name, f"{kind} step has no {field}")
            elif ref.startswith("slot:"):
                slot = slots.get(ref[5:])
                if slot is None:
                    err(name, f"names undeclared {ref}")
                elif isinstance(slot, dict) and (kind == "talk") == (slot.get("pick") == "anchor"):
                    err(name, f"{kind} step needs {'a resident or role' if kind == 'talk' else 'an anchor'} slot, not {ref}")
            elif kind == "talk":
                err(name, f"talks to {ref}, not a resident slot")
            elif ref not in anchors:
                err(name, f"no anchor {ref} on the map (anchors: {', '.join(sorted(anchors))})")
        reached, todo = set(), [start]
        while todo:
            n = todo.pop()
            if not isinstance(n, str) or n in reached or n not in steps or not isinstance(steps[n], dict):
                continue
            reached.add(n)
            todo += [steps[n].get("next")] + [b.get("next") for b in steps[n].get("branch") or [] if isinstance(b, dict)]
        for name in steps:
            if name not in reached and start in steps:
                err(name, "unreachable from the start step")
    return problems


def quest_mode():
    """Checks the repo's quests, and that the bad fixtures still fail (the checker's self-test)."""
    files = quest_files()
    problems = check_quests(files)
    bad = check_quests([BAD_QUEST]) + check_quests([MISSING_QUEST])
    want = ["objective must be an object", "unknown step type", "unknown step type ''", "unknown condition", "malformed action", "missing step", "unreachable", "never set",
            "unknown quest", "no anchor", "no resident", "no anchor:nowhere", "'teach_technique': 'combat:nin.none'"]
    missed = [w for w in want if not any(w in p for p in bad)]
    if missed:
        problems.append("self-test: the bad quest fixtures no longer report: " + ", ".join(missed))
    if problems:
        print("\n".join(problems))
        print(f"{len(problems)} quest problems")
        return 1
    print(f"{len(files)} quests ok")
    return 0


def main(argv):
    if "--quests" in argv:
        return quest_mode()
    bad_quests = "--check" in argv and quest_mode()
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
        if bad_quests:
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
