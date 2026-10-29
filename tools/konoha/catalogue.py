#!/usr/bin/env python3
"""Totals and tables for KONOHA_BUILD.md, from blocks.json and buildings.json.

    python3 tools/konoha/catalogue.py           # print the totals
    python3 tools/konoha/catalogue.py --write   # also rewrite the generated sections of KONOHA_BUILD.md
    python3 tools/konoha/catalogue.py --check   # fail if KONOHA_BUILD.md is out of date

A generated section sits between <!-- gen:NAME --> and <!-- /gen:NAME --> lines.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

HERE = Path(__file__).parent
ROOT = HERE.parents[1]
DOC = ROOT / "KONOHA_BUILD.md"
BLOCK_SLICES = ("P0", "B1", "B2", "B2.5", "B3", "later")
SLICES = ("P0", "B1", "B2", "B3", "later")
SLICE_NAME = {"P0": "Phase 0", "B1": "Beta 1", "B2": "Beta 2", "B2.5": "Beta 2.5", "B3": "Beta 3", "later": "Later"}
CATEGORY = {"roof": "Roofs", "facade": "Facades and shop fronts", "crest": "Crests and banners", "interior": "Interior fittings",
            "story": "Story pieces", "light": "Lanterns", "street": "Streets", "festival": "Festival", "shrine": "Shrine",
            "furniture": "Furniture (the Leaf set)", "keepsake": "Keepsakes", "civic": "Academy, Residence, hospital, stadium",
            "shop": "Shops and food", "training": "Training", "crafting": "Crafting stations", "garden": "Gardens",
            "clan": "Clan signatures", "display": "Displays (item-rendering)"}
GROUP = {"homes": "Homes", "apartments": "Apartment buildings", "shops": "Shops", "clans": "Clan builds",
         "landmarks": "Landmarks", "training": "Training grounds", "forest": "Forest of Death", "wall": "Wall",
         "streets": "Street pieces (bridges, trees, poles)"}


def load():
    return json.loads((HERE / "blocks.json").read_text()), json.loads((HERE / "buildings.json").read_text())


def first_slice(variants):
    return min((v["slice"] for v in variants), key=BLOCK_SLICES.index)


def block_totals(cat):
    groups = cat["custom"]
    by_slice = Counter(v["slice"] for g in groups for v in g["variants"])
    groups_by_slice = Counter(first_slice(g["variants"]) for g in groups)
    return {
        "groups": len(groups), "variants": sum(len(g["variants"]) for g in groups),
        "textures": sum(g["textures"] for g in groups),
        "functional": sum(1 for g in groups if g["functional"]),
        "complexity": Counter(g["complexity"] for g in groups),
        "complexity_variants": Counter({k: sum(len(g["variants"]) for g in groups if g["complexity"] == k) for k in ("simple", "medium", "complex")}),
        "by_slice": by_slice, "groups_by_slice": groups_by_slice,
        "vanilla": len(cat["vanilla"]), "vanilla_by_slice": Counter(v["slice"] for v in cat["vanilla"]),
        "paintings": len(cat["paintings"]), "prototype_groups": sum(1 for g in groups if g["prototype"]),
        "prototype_variants": sum(1 for g in groups if g["prototype"] for v in g["variants"] if v["slice"] == "P0"),
    }


def md_block_summary(cat):
    t = block_totals(cat)
    cats = defaultdict(list)
    for g in cat["custom"]:
        cats[g["category"]].append(g)
    out = ["| Group | Blocks | With variants | Textures | Functional |", "|---|---:|---:|---:|---:|"]
    for k, gs in cats.items():
        out.append(f"| {CATEGORY[k]} | {len(gs)} | {sum(len(g['variants']) for g in gs)} | {sum(g['textures'] for g in gs)} | "
                   f"{sum(1 for g in gs if g['functional'])} |")
    out.append(f"| **All custom blocks** | **{t['groups']}** | **{t['variants']}** | **{t['textures']}** | **{t['functional']}** |")
    out += ["", "| By slice (new that slice) | " + " | ".join(SLICE_NAME[s] for s in BLOCK_SLICES) + " | Total |",
            "|---|" + "---:|" * (len(BLOCK_SLICES) + 1),
            "| Custom blocks (first needed) | " + " | ".join(str(t["groups_by_slice"].get(s, 0)) for s in BLOCK_SLICES) + f" | {t['groups']} |",
            "| Custom block variants | " + " | ".join(str(t["by_slice"].get(s, 0)) for s in BLOCK_SLICES) + f" | {t['variants']} |",
            "| Vanilla mappings | " + " | ".join(str(t["vanilla_by_slice"].get(s, 0)) for s in BLOCK_SLICES) + f" | {t['vanilla']} |",
            "", f"Complexity: {t['complexity']['simple']} simple, {t['complexity']['medium']} medium and "
            f"{t['complexity']['complex']} complex blocks ({t['complexity_variants']['simple']}, {t['complexity_variants']['medium']} "
            f"and {t['complexity_variants']['complex']} with variants). Prototyped now: {t['prototype_groups']} blocks, "
            f"{t['prototype_variants']} with variants."]
    return "\n".join(out)


def md_block_table(cat):
    cats = defaultdict(list)
    for g in cat["custom"]:
        cats[g["category"]].append(g)
    out = []
    for k, gs in cats.items():
        out += [f"#### {CATEGORY[k]}", "", "| Block | Purpose | Variants (slice) | Function | Model | Tex | First |",
                "|---|---|---|---|---|---:|---|"]
        for g in gs:
            vs = "; ".join(f"`{v['id']}` {v['label']}" + (f" ({SLICE_NAME[v['slice']]})" if v["slice"] != first_slice(g["variants"]) else "")
                           for v in g["variants"]) if len(g["variants"]) <= 6 else (
                f"{len(g['variants'])}: " + ", ".join(v["label"] for v in g["variants"]))
            fn = g["functional"] or "decor"
            if g.get("reuse"):
                fn += f" ({g['reuse']})"
            name = f"**{g['name']}**" + (" ★" if g["prototype"] else "")
            purpose = g["purpose"] + (f". {g['notes']}" if g.get("notes") else "")
            out.append(f"| {name}<br>`{g['id']}` | {purpose} | {vs} | {fn} | {g['complexity']} | {g['textures']} | "
                       f"{SLICE_NAME[first_slice(g['variants'])]} |")
        out.append("")
    return "\n".join(out).rstrip()


def md_vanilla(cat):
    out = ["| Need | Vanilla blocks | Use | First |", "|---|---|---|---|"]
    for v in cat["vanilla"]:
        out.append(f"| {v['need']} | {v['blocks']} | {v['use']} | {SLICE_NAME[v['slice']]} |")
    if cat["paintings"]:
        out += ["", "Paintings (data-pack painting variants, no Java): " +
                "; ".join(f"`{p['id']}` {p['label']} ({SLICE_NAME[p['slice']]})" for p in cat["paintings"]) + "."]
    return "\n".join(out)


def building_totals(bld):
    tot = defaultdict(Counter)
    for b in bld["buildings"]:
        for s, n in b["counts"].items():
            tot[b["group"]][s] += n
    return tot


def md_buildings(bld):
    out = []
    groups = defaultdict(list)
    for b in bld["buildings"]:
        groups[b["group"]].append(b)
    for gk, bs in groups.items():
        out += [f"#### {GROUP[gk]}", "", "| Building | Built from | Footprint | P0 | B1 | B2 | B3 | Later | Total | Notes |",
                "|---|---|---|---:|---:|---:|---:|---:|---:|---|"]
        for b in bs:
            cnt = [b["counts"].get(s, 0) for s in SLICES]
            how = b["how"].replace("program", f"program `{b['id']}`", 1) if b["how"].startswith("program") else b["how"]
            out.append(f"| {b['name']} | {how} | {b['footprint']} | " + " | ".join(str(n) if n else "" for n in cnt) +
                       f" | {sum(cnt)} | {b['notes']} |")
        out.append("")
    return "\n".join(out).rstrip()


def md_building_totals(bld):
    tot = building_totals(bld)
    out = ["| Group | " + " | ".join(SLICE_NAME[s] for s in SLICES) + " | Total |", "|---|" + "---:|" * (len(SLICES) + 1)]
    for gk, c in tot.items():
        out.append(f"| {GROUP[gk]} | " + " | ".join(str(c.get(s, 0)) for s in SLICES) + f" | {sum(c.values())} |")
    km = bld["streets_km"]
    out.append("| Streets (km, laid by roads.py) | " + " | ".join(str(km.get(s, 0)) for s in SLICES) + f" | {round(sum(km.values()), 2)} |")
    progs = Counter(p["makes"] for p in bld["programs"])
    out += ["", f"Design programs: **{len(bld['programs'])}** (" + ", ".join(f"{n} {GROUP.get(k, k).lower()}" for k, n in progs.items()) +
            f"), {sum(1 for p in bld['programs'] if p['status'] == 'prototype')} of them prototyped."]
    return "\n".join(out)


def md_programs(bld):
    out = ["| Program | Makes | First | Status |", "|---|---|---|---|"]
    for p in bld["programs"]:
        out.append(f"| `{p['id']}` | {p['name']} | {SLICE_NAME[p['first']]} | {p['status']} |")
    return "\n".join(out)


SECTIONS = {"block-summary": md_block_summary, "block-table": md_block_table, "vanilla": md_vanilla}
BSECTIONS = {"buildings": md_buildings, "building-totals": md_building_totals, "programs": md_programs}


def render_doc(text, cat, bld):
    for name, fn in list(SECTIONS.items()) + list(BSECTIONS.items()):
        body = fn(cat if name in SECTIONS else bld)
        text = re.sub(rf"(<!-- gen:{name} -->\n).*?(<!-- /gen:{name} -->)", lambda m: m.group(1) + body + "\n" + m.group(2),
                      text, flags=re.S)
    return text


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--write", action="store_true")
    ap.add_argument("--check", action="store_true")
    a = ap.parse_args()
    cat, bld = load()
    t = block_totals(cat)
    print(f"custom blocks: {t['groups']} ({t['variants']} with variants), {t['textures']} textures, {t['functional']} functional; "
          f"vanilla mappings: {t['vanilla']}; paintings: {t['paintings']}")
    print("variants by slice:", dict(t["by_slice"]), " groups by first slice:", dict(t["groups_by_slice"]))
    print("complexity:", dict(t["complexity"]), "variants:", dict(t["complexity_variants"]))
    for g, c in building_totals(bld).items():
        print(f"{g}: {dict(c)} = {sum(c.values())}")
    print("programs:", len(bld["programs"]))
    if a.write or a.check:
        text = DOC.read_text()
        new = render_doc(text, cat, bld)
        if a.check and new != text:
            sys.exit("KONOHA_BUILD.md is out of date: run catalogue.py --write")
        if a.write:
            DOC.write_text(new)


if __name__ == "__main__":
    main()
