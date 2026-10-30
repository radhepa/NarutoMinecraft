#!/usr/bin/env python3
"""The Hidden Leaf's map layout (layout.json): districts, streets and plots.

  python tools/konoha/layout.py --check   every plot fits the border and has its corners in its district, no plot overlaps
                                          another or a street, every design exists, homes have a plaque
                                          and a bed, bed markers sit on bed heads, doors open onto a
                                          street, each anchor is placed once
  python tools/konoha/layout.py --plan    a top-down PNG of the village, docs/renders/konoha/layout_plan.png

A plot's `at` is the north-west corner of its footprint after `rot` (clockwise quarter turns, in
degrees) and `mirror` (east-west, before the turn); a planned plot gives its footprint as `size`
and has no design yet. The game pastes the same transform (village/.../Blueprint.java).
"""
import argparse
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
LAYOUT = HERE / "layout.json"
BLUEPRINTS = HERE / "blueprints"
PLAN = ROOT / "docs" / "renders" / "konoha" / "layout_plan.png"
# the quest places the map saves (TestStreet.PLACES, missions.py STREET_ANCHORS), each placed once
ANCHORS = ("notice_board", "anchor:training", "anchor:hokage_office", "anchor:academy.grounds", "anchor:academy.yard", "anchor:academy.library")
HOMES = ("home", "apartment")
DOOR_REACH = 3   # how far a door anchor may sit from its street


def load():
    return json.loads(LAYOUT.read_text(encoding="utf-8"))


def blueprint(design):
    return json.loads((BLUEPRINTS / f"{design}.json").read_text(encoding="utf-8"))


def street_rect(s):
    """(x0, z0, x1, z1), inclusive, of a street's run."""
    (ax, az), (bx, bz), h = s["from"], s["to"], s["width"] // 2
    if az == bz:
        return min(ax, bx), az - h, max(ax, bx), az + h
    return ax - h, min(az, bz), ax + h, max(az, bz)


def touches(rect, x, z):
    """Whether block x, z is in the rect or next to it (sides or corners)."""
    x0, z0, x1, z1 = rect
    return x0 - 1 <= x <= x1 + 1 and z0 - 1 <= z <= z1 + 1


def turned(plot, w, d):
    return (d, w) if plot.get("rot", 0) in (90, 270) else (w, d)


def local(plot, w, d, x, z):
    """Where a blueprint's block x, z lands from the plot's corner (mirror first, then the turn)."""
    if plot.get("mirror"):
        x = w - 1 - x
    r = plot.get("rot", 0)
    return {0: (x, z), 90: (d - 1 - z, x), 180: (w - 1 - x, d - 1 - z), 270: (z, w - 1 - x)}[r]


def footprint(plot):
    """(x0, z0, x1, z1), inclusive, of a plot."""
    if plot.get("planned"):
        w, d = plot["size"]
    else:
        bw, _, bd = blueprint(plot["design"])["size"]
        w, d = turned(plot, bw, bd)
    x, _, z = plot["at"]
    return x, z, x + w - 1, z + d - 1


def overlap(a, b):
    return a[0] <= b[2] and b[0] <= a[2] and a[1] <= b[3] and b[1] <= a[3]


def inside(poly, x, z):
    """Point in polygon (even-odd), counting the polygon's edges as inside."""
    hit = False
    for (ax, az), (bx, bz) in zip(poly, poly[1:] + poly[:1]):
        if min(ax, bx) <= x <= max(ax, bx) and min(az, bz) <= z <= max(az, bz) and (bx - ax) * (z - az) == (bz - az) * (x - ax):
            return True
        if (az > z) != (bz > z) and x < ax + (z - az) * (bx - ax) / (bz - az):
            hit = not hit
    return hit


def check(lay):
    errors = []
    err = errors.append
    if lay.get("format") != "konoha-layout/1":
        err("layout: format must be konoha-layout/1")
    b = lay["border"]
    half = b["size"] / 2
    edge = (b["x"] - half, b["z"] - half, b["x"] + half - 1, b["z"] + half - 1)
    districts = {d["id"]: d["polygon"] for d in lay["districts"]}
    streets = {}
    for s in lay["streets"]:
        (ax, az), (bx, bz) = s["from"], s["to"]
        if s["width"] % 2 == 0 or (ax != bx) == (az != bz):
            err(f"street {s['id']}: needs an odd width and one axis")
            continue
        if s["id"] in streets:
            err(f"street {s['id']}: id used twice")
        streets[s["id"]] = street_rect(s)
        sp = BLUEPRINTS / f"street.{s['id']}.json"
        r = streets[s["id"]]
        if not sp.exists():
            err(f"street {s['id']}: no blueprint; run roads.py")
        elif blueprint("street." + s["id"])["size"][::2] != [r[2] - r[0] + 1, r[3] - r[1] + 1]:
            err(f"street {s['id']}: its blueprint is stale; run roads.py")
    seen, rects, anchors = set(), {}, {}
    for p in lay["plots"]:
        pid = p["id"]
        if pid in seen:
            err(f"plot {pid}: id used twice")
        seen.add(pid)
        if p.get("rot", 0) not in (0, 90, 180, 270):
            err(f"plot {pid}: rot must be 0, 90, 180 or 270")
            continue
        if not p.get("planned") and not (BLUEPRINTS / f"{p.get('design')}.json").exists():
            err(f"plot {pid}: no blueprint {p.get('design')!r}")
            continue
        if p["at"][1] != 0:
            err(f"plot {pid}: at's y must be 0, the map's ground")
        r = rects[pid] = footprint(p)
        if not (edge[0] <= r[0] and r[2] <= edge[2] and edge[1] <= r[1] and r[3] <= edge[3]):
            err(f"plot {pid}: {r} is outside the border")
        if p["district"] not in districts:
            err(f"plot {pid}: no district {p['district']!r}")
        elif not all(inside(districts[p["district"]], x, z) for x in (r[0], r[2]) for z in (r[1], r[3])):
            err(f"plot {pid}: a corner is outside district {p['district']}")
        for sid, sr in streets.items():
            if overlap(r, sr):
                err(f"plot {pid}: overlaps street {sid}")
        if p.get("planned"):
            continue
        bp = blueprint(p["design"])
        w, _, d = bp["size"]
        types = [m["type"] for m in bp["markers"]]
        if bp["kind"] in HOMES and not ("house_plaque" in types and "bed" in types):
            err(f"plot {pid}: a {bp['kind']} needs a house_plaque and a bed marker")
        for m in bp["markers"]:
            if m["type"] == "bed":
                x, y, z = m["pos"]
                ch = bp["layers"][y][z][x]
                if ch == "." or not ("_bed[" in bp["palette"][ch] and "part=head" in bp["palette"][ch]):
                    err(f"plot {pid}: bed marker {m['pos']} of {p['design']} is not on a bed head")
            if m["type"] in ANCHORS:
                anchors[m["type"]] = anchors.get(m["type"], 0) + 1
            if m["type"] == "door_anchor":
                lx, lz = local(p, w, d, m["pos"][0], m["pos"][2])
                x, z = r[0] + lx, r[1] + lz
                if not any(abs(x - min(max(x, sr[0]), sr[2])) + abs(z - min(max(z, sr[1]), sr[3])) <= DOOR_REACH for sr in streets.values()):
                    err(f"plot {pid}: its door at {x}, {z} is more than {DOOR_REACH} blocks from a street")
    ids = list(rects)
    for i, a in enumerate(ids):
        for c in ids[i + 1:]:
            if overlap(rects[a], rects[c]):
                err(f"plot {a}: overlaps plot {c}")
    for a in ANCHORS:
        if anchors.get(a) != 1:
            err(f"layout: anchor {a} placed {anchors.get(a, 0)} times, not once")
    return errors


# -- the plan view --------------------------------------------------------------------------------
COLOURS = [("grass", (96, 150, 60)), ("dirt_path", (170, 140, 90)), ("cobblestone", (120, 120, 120)),
           ("gravel", (135, 130, 125)), ("oxidized", (76, 150, 128)), ("green_kawara", (76, 150, 128)),
           ("cut_copper", (192, 110, 72)), ("orange_kawara", (192, 110, 72)), ("deepslate", (72, 72, 78)),
           ("grey_kawara", (72, 72, 78)), ("red_sandstone", (190, 100, 50)), ("sandstone", (222, 210, 160)),
           ("quartz", (236, 233, 226)), ("calcite", (230, 230, 225)), ("red_terracotta", (150, 64, 50)),
           ("brown_terracotta", (110, 70, 50)), ("terracotta", (160, 95, 70)), ("cherry", (236, 172, 200)),
           ("leaves", (70, 130, 55)), ("water", (60, 100, 200)), ("tatami", (190, 180, 110)), ("spruce", (115, 85, 52)),
           ("oak", (165, 132, 84)), ("stone_bricks", (128, 128, 128)), ("andesite", (136, 136, 136)),
           ("stone", (140, 140, 140)), ("glass", (205, 220, 230)), ("lantern", (210, 200, 150)), ("pole", (90, 70, 50)),
           ("wire", (40, 40, 40)), ("sand", (215, 200, 150))]
DISTRICT_TINTS = [(229, 115, 115), (240, 170, 90), (230, 210, 100), (150, 200, 110), (100, 190, 170), (110, 160, 220),
                  (150, 130, 210), (210, 130, 190), (180, 150, 120), (140, 140, 140)]
SCALE = 2


def colour(state):
    name = state.split("[")[0]
    return next((c for k, c in COLOURS if k in name), (150, 150, 150))


def plan(lay, out=PLAN):
    from PIL import Image, ImageDraw, ImageFont
    b = lay["border"]
    half = b["size"] / 2
    ox, oz = int(b["x"] - half), int(b["z"] - half)
    n = int(b["size"])
    img = Image.new("RGB", (n * SCALE, n * SCALE), (96, 150, 60))
    draw = ImageDraw.Draw(img, "RGBA")
    font = ImageFont.load_default(size=11)

    def box(r, fill, outline=None):
        draw.rectangle([(r[0] - ox) * SCALE, (r[1] - oz) * SCALE, (r[2] - ox + 1) * SCALE - 1, (r[3] - oz + 1) * SCALE - 1], fill=fill, outline=outline)

    tint = {d["id"]: DISTRICT_TINTS[i % len(DISTRICT_TINTS)] for i, d in enumerate(lay["districts"])}
    for d in lay["districts"]:
        pts = [((x - ox) * SCALE, (z - oz) * SCALE) for x, z in d["polygon"]]
        draw.polygon(pts, fill=tint[d["id"]] + (40,), outline=tint[d["id"]] + (200,))
        draw.text((pts[0][0] + 4, pts[0][1] + 3), d["name"], fill=(30, 30, 30), font=font)

    def top(design, corner, plot):
        bp = blueprint(design)
        w, h, d = bp["size"]
        for z in range(d):
            for x in range(w):
                for y in range(h - 1, -1, -1):
                    ch = bp["layers"][y][z][x]
                    if ch != ".":
                        lx, lz = local(plot, w, d, x, z)
                        box((corner[0] + lx, corner[1] + lz, corner[0] + lx, corner[1] + lz), colour(bp["palette"][ch]))
                        break

    for s in lay["streets"]:
        r = street_rect(s)
        top("street." + s["id"], r, {}) if (BLUEPRINTS / f"street.{s['id']}.json").exists() else box(r, (170, 140, 90))
    for p in lay["plots"]:
        r = footprint(p)
        if p.get("planned"):
            box(r, tint[p["district"]] + (150,), (40, 40, 40, 220))
            draw.text(((r[0] - ox) * SCALE + 3, (r[1] - oz) * SCALE + 2), p["name"], fill=(20, 20, 20), font=font)
        else:
            top(p["design"], r, p)
    out.parent.mkdir(parents=True, exist_ok=True)
    img.save(out)
    return out


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--check", action="store_true")
    ap.add_argument("--plan", action="store_true")
    a = ap.parse_args()
    lay = load()
    if a.plan:
        print(f"plan: {plan(lay).relative_to(ROOT)}")
    if a.check or not a.plan:
        errors = check(lay)
        for e in errors:
            print(e)
        built = [p for p in lay["plots"] if not p.get("planned")]
        print(f"{'FAILED' if errors else 'ok'}: {len(lay['districts'])} districts, {len(lay['streets'])} streets, "
              f"{len(built)} plots built, {len(lay['plots']) - len(built)} planned")
        sys.exit(1 if errors else 0)


if __name__ == "__main__":
    main()
