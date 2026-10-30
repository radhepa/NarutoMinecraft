#!/usr/bin/env python3
"""The home family (docs/konoha/MASTER_PLAN.md §9, BATCHES K4): every detached home of Konoha from one generator.

home(seed, w, d) builds a home for a w x d lot, street to the south. The seed rolls the form, not only the colours:
storeys (one to three), footprint, a one-storey wing at the front or back, the roof (a gable either way, a hip, or
flat with a tank), the door's place and its porch (a canopy, a veranda, a roofed gate, or a balcony over it), the
garden's side, its fence and tree, the palette, a mirror. Faces get TECHNIQUES §2 to §5: the plaster gradient,
posts every four blocks, proud floor bands, sills and lintels, the base step, eave lips. Rooms follow §10.3, and every
build is walked (§10.2): the door reaches each bed, the stove, the stairs and the resident marker, or the piece that
blocks the way is left out. street() gives a row of lots homes whose forms never repeat within five plots.

  python tools/konoha/families/home.py            # the reference sheet: docs/renders/konoha/families/home*.png
  python tools/konoha/families/home.py --check    # every lot size, many seeds: walk lines, beds, palette, variety
  python tools/konoha/families/home.py --write    # the blueprints of the home.WxD.SEED designs layout.json uses
"""
from __future__ import annotations

import random
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))
from kit import NS, WALLS, Plan, base_name, mc  # noqa: E402

WALL_W = {"cream": 5, "white": 2, "terracotta": 2, "plaster_orange": 1}
ROOF_W = {"grey": 4, "green": 2, "orange": 2, "teal": 2}
BED_COLOURS = ("red", "blue", "green", "white", "brown")
FLOORS = (2, 6, 10)  # feet height on each storey; the floor slab is the block below
DIRS = {"north": (0, -1), "south": (0, 1), "east": (1, 0), "west": (-1, 0)}


class Unbuildable(Exception):
    pass


def pick(r, weights):
    return r.choices(list(weights), list(weights.values()))[0]


# -- the walk (TECHNIQUES §10.2) ------------------------------------------------------------------
def passable(s):
    if s is None:
        return True
    n = base_name(s)
    return n.endswith(("_carpet", "tatami", "_door", ":light")) or (
        n.endswith("_trapdoor") and "half=bottom" in s and "open=false" in s)


def stand(p, x, y, z):
    w, h, d = p.size
    if not (0 <= x < w and 1 <= y < h - 1 and 0 <= z < d):
        return False
    below = p.get(x, y - 1, z)
    return below is not None and not passable(below) and passable(p.get(x, y, z)) and passable(p.get(x, y + 1, z))


def walk(p, start):
    """Every cell a resident can stand in from `start`: level steps, a drop of one, a climb onto a stair
    in its facing, or a climb of one onto a floor level (off a stair's top)."""
    seen, todo = {start}, [start]
    while todo:
        x, y, z = todo.pop()
        for d, (dx, dz) in DIRS.items():
            for dy in (0, 1, -1):
                n = (x + dx, y + dy, z + dz)
                if n in seen or not stand(p, *n):
                    continue
                if dy == 1:
                    below = p.get(n[0], y, n[2])
                    up_stair = below and base_name(below).endswith("_stairs") and f"facing={d}" in below
                    if not (up_stair or n[1] in FLOORS) or not passable(p.get(x, y + 2, z)):
                        continue
                if dy == -1 and not passable(p.get(n[0], y + 1, n[2])):
                    continue
                seen.add(n)
                todo.append(n)
    return seen


def near(cells, reach):
    return any((x + dx, y, z + dz) in reach for x, y, z in cells for dx, dz in DIRS.values())


# -- the form ---------------------------------------------------------------------------------------
def roll(r, w, d):
    """The variant's choices, rolled in a fixed order (a seed always gives the same home)."""
    f = {"wall": pick(r, WALL_W), "roof_c": pick(r, ROOF_W)}
    n = r.choices((1, 2, 3), (2, 5, 2))[0] if d >= 10 else 1
    wing = r.choice(("front", "back")) if w >= 11 and r.random() < .5 else None
    ww = 5 if wing else 0
    room = w - 2 - (ww - 1 if wing else 0)          # the widest main box inside a one-block margin each side
    if room < (7 if n == 1 else 6):
        wing, ww, room = None, 0, w - 2
    hw = r.randint(min(room, max(6 if n > 1 else 7, room - 2)), room)
    maxd = d - 3                                     # front garden 2 at least, back margin 1
    hd = r.randint(max(7 if n > 1 else 6, maxd - 2), maxd)
    kind = r.choices(("x", "z", "hip", "flat"), (4, 3, 3, 1 if n == 1 else 3))[0]
    mins = (6 if n > 1 else 7, 7 if n > 1 else 6)

    def odd(v, lo):                                  # shrink to odd, if that stays big enough
        return v if v % 2 or v - 1 < lo else v - 1
    if kind == "x":
        hd = odd(hd, mins[1])
    elif kind == "z":
        hw = odd(hw, mins[0])
    elif kind == "hip":
        if hw >= hd:
            hd = odd(hd, mins[1])
        else:
            hw = odd(hw, mins[0])
    span = {"x": hd, "z": hw, "hip": min(hw, hd)}.get(kind, 1)
    if span % 2 == 0:
        kind = "flat"
    wd = 7 if wing and hd >= 7 and r.random() < .5 else 5
    tw = hw + (ww - 1 if wing else 0)
    gap = w - 2 - tw
    ox = 1 + r.choice((0, gap // 2, gap))            # the side garden left, both sides or right
    back = 1
    fg = min(d - hd - back, 3)                       # the door within three of the street (layout.py DOOR_REACH)
    porch = r.choice(("canopy", "veranda", "gate") if fg >= 3 else ("canopy", "veranda"))   # a gate needs a front garden
    if n >= 2 and fg >= 3 and r.random() < .45:
        porch = "balcony"
    f.update(n=n, wing=wing, ww=ww, wd=wd, hw=hw, hd=hd, kind=kind, ox=ox, fg=fg, porch=porch,
             fence=r.choice(("bamboo", "hedge", "wall", "none")), tree=r.random() < .7, mirror=r.random() < .5,
             door=r.random(), beds=r.sample(BED_COLOURS, 3), extra_bed=r.random() < .5)
    return f


def form(f):
    """What makes two homes look like the same house: palette and mirror do not count."""
    return f["n"], f["kind"], f["wing"], f["porch"]


# -- the build -----------------------------------------------------------------------------------
def home(seed, w, d):
    for attempt in range(30):
        r = random.Random(f"{seed}/{attempt}")
        f = roll(r, w, d)
        try:
            return build(r, f, seed, w, d), f
        except Unbuildable:
            continue
    raise Unbuildable(f"home {seed} on {w} x {d}: no buildable roll")


def build(r, f, seed, w, d):
    n, style, hw, hd = f["n"], f["wall"], f["hw"], f["hd"]
    W = WALLS[style]
    top = 4 * n                                       # the last wall course; eaves one above
    p = Plan(f"home.{w}x{d}.{seed}", "Home", (w, top + 8, d), "home",
             "Home family (tools/konoha/families/home.py): a House Plaque on the front wall beside the door; beds by marker")
    # the main box (walls included), the wing on its west side, the stair on the east wall
    hx0 = f["ox"] + (f["ww"] - 1 if f["wing"] else 0)
    hx1, hz0 = hx0 + hw - 1, d - f["fg"] - hd
    hz1 = hz0 + hd - 1
    ix0, ix1, iz0, iz1 = hx0 + 1, hx1 - 1, hz0 + 1, hz1 - 1
    sx = ix1
    reserved = set()

    def outside(x, y, z, state):                      # proud pieces: only inside the lot, never over a block
        if 0 <= x < w and 0 <= z < d and 0 <= y < p.size[1] and p.get(x, y, z) is None:
            p.set(x, y, z, state)

    # ground, the box, its floors
    p.fill(0, 0, 0, w - 1, 0, d - 1, "grass_block")
    boxes = [(hx0, hz0, hx1, hz1, n)]
    if f["wing"]:
        wz0 = hz0 if f["wing"] == "back" else hz1 - f["wd"] + 1
        boxes.append((hx0 - f["ww"] + 1, wz0, hx0, wz0 + f["wd"] - 1, 1))
    for x0, z0, x1, z1, k in boxes:
        p.fill(x0, 1, z0, x1, 1, z1, W["base"])
        p.fill(x0 + 1, 1, z0 + 1, x1 - 1, 1, z1 - 1, "spruce_planks")
        p.walls(x0, z0, x1, z1, 2, 4 * k, style)
        for s in range(1, k):
            p.fill(x0 + 1, 1 + 4 * s, z0 + 1, x1 - 1, 1 + 4 * s, z1 - 1, "spruce_planks")
            p.band(x0, z0, x1, z1, 1 + 4 * s, style)
        for z in (z0, z1):                            # posts every four blocks on the long faces
            for x in range(x0 + 4, x1 - 1, 4):
                p.fill(x, 2, z, x, 4 * k, z, W["post"])
    # the opening from the house into the wing (its middle row)
    if f["wing"]:
        oz = boxes[1][1] + f["wd"] // 2
        p.clear(hx0, 2, oz, hx0, 3, oz)
        reserved |= {(hx0 - 1, 2, oz), (hx0 + 1, 2, oz)}

    # the door, its landing and the stair
    lo, hi = (ix0, sx - 1) if n > 1 else (ix0, ix1)
    dx = lo + min(hi - lo, int(f["door"] * (hi - lo + 1)))
    p.door(dx, 2, hz1, "south")
    entry = (dx, 2, iz1)
    # the House Plaque hangs outside on the wall beside the door; VF floods the house from two behind it
    px = next((x for x in (dx + 1, dx - 1) if ix0 <= x <= ix1 and not (n > 1 and x == sx)
               and p.get(x, 3, hz1) == mc(W["wall"])), None)
    if px is None:
        raise Unbuildable("no wall beside the door for the plaque")
    reserved |= {entry, (px, 3, iz1)}
    p.set(dx, 1, iz1, "polished_andesite")            # the genkan
    stairs = []
    if n > 1:
        if iz1 - iz0 < 4:
            raise Unbuildable("too shallow for the stair")
        for i in range(3):                            # flight 1 climbs north up the east wall
            p.set(sx, 2 + i, iz1 - 1 - i, "spruce_stairs[facing=north,half=bottom]")
        p.clear(sx, 5, iz1 - 3, sx, 5, iz1 - 1)
        stairs += [(sx, y, z) for y in range(2, 8) for z in range(iz1 - 3, iz1 + 1)]
        stairs += [(sx, 6, iz1 - 4), (sx, 7, iz1 - 4)]
        landings = [(sx, 6, iz1 - 4)]
    if n > 2:
        if ix1 - ix0 < 3:
            raise Unbuildable("too narrow for two flights")
        for i in range(3):                            # flight 2 turns back south beside it
            p.set(sx - 1, 6 + i, iz1 - 3 + i, "spruce_stairs[facing=south,half=bottom]")
        p.clear(sx - 1, 9, iz1 - 3, sx - 1, 9, iz1 - 1)
        stairs += [(sx - 1, y, z) for y in range(6, 12) for z in range(iz1 - 4, iz1 + 1)]
        landings.append((sx - 1, 10, iz1))
    reserved |= set(stairs)

    # roof
    eave = top + 1
    if f["kind"] == "flat":
        p.flat_roof(hx0, hx1, hz0, hz1, eave, style)
        tx = hx0 + 1 + r.randint(0, 1)
        p.water_tank(tx, eave + 1, hz0 + 1, 2)
        p.set(hx1 - 1, eave + 1, hz0 + 1, "potted_azalea_bush")
    else:
        p.slab_roof(hx0, hx1, hz0, hz1, eave, f["roof_c"], f["kind"], gable_style=style)
    if f["wing"]:
        x0, z0, x1, z1, _ = boxes[1]
        p.slab_roof(x0, x1, z0, z1, 5, f["roof_c"], "hip")
    for x0, z0, x1, z1, k in boxes:                   # one roof's eave never hangs inside the other's rooms
        for x in range(x0 + 1, x1):
            for z in range(z0 + 1, z1):
                for y in range(2, 4 * k + 1):
                    s = p.get(x, y, z)
                    if s and (y - 1) % 4 and not base_name(s).endswith("spruce_stairs") and s != mc("spruce_planks"):
                        p.set(x, y, z, None)

    def inside_any(x, z):
        return any(x0 <= x <= x1 and z0 <= z <= z1 for x0, z0, x1, z1, _ in boxes)

    # windows: one high on the ground floor, two tall above; never on a post, the door or a stair
    def windows(face_cells, y, h):
        for x, z, ox_, oz_ in face_cells:
            if inside_any(x + ox_, z + oz_):
                continue
            if p.get(x, y, z) != mc(W["wall"]) or any(p.get(x, y + k, z) != mc(W["wall"]) for k in range(h)):
                continue
            if (x - ox_, y, z - oz_) in reserved or any((x - ox_, y + k, z - oz_) in reserved for k in range(-1, h + 1)):
                continue
            if p.get(x + ox_, y, z + oz_) is not None:
                continue
            if f["porch"] == "balcony" and oz_ == 1 and y == 6 and abs(x - dx) <= 2:
                continue                              # the balcony's sliding doors go there
            p.window(x, y, z, h)
            outside(x + ox_, y - 1, z + oz_, "spruce_slab[type=top]")                         # sill
            facing = {(0, 1): "north", (0, -1): "south", (1, 0): "west", (-1, 0): "east"}[(ox_, oz_)]
            outside(x + ox_, y + h, z + oz_, f"spruce_stairs[facing={facing},half=top]")       # lintel
    for x0, z0, x1, z1, k in boxes:
        faces = ([(x, z1, 0, 1) for x in range(x0 + 1, x1) if x % 2 == (x0 + 1) % 2 or x1 - x0 < 6]
                 + [(x, z0, 0, -1) for x in range(x0 + 2, x1, 3)]
                 + [(x0, z, -1, 0) for z in range(z0 + 2, z1 - 1, 3)] + [(x1, z, 1, 0) for z in range(z0 + 2, z1 - 1, 3)])
        for s in range(k):
            windows(faces, 3 + 4 * s, 1 if s == 0 else 2)

    # depth: proud floor bands, the base step
    for x0, z0, x1, z1, k in boxes:
        for s in range(1, k):
            for x in range(x0 - 1, x1 + 2):
                outside(x, 1 + 4 * s, z0 - 1, "dark_oak_slab[type=top]")
                outside(x, 1 + 4 * s, z1 + 1, "dark_oak_slab[type=top]")
            for z in range(z0, z1 + 1):
                outside(x0 - 1, 1 + 4 * s, z, "dark_oak_slab[type=top]")
                outside(x1 + 1, 1 + 4 * s, z, "dark_oak_slab[type=top]")

    # the front: path, step, porch
    p.set(dx, 1, hz1 + 1, "smooth_stone_slab[type=bottom]")
    for z in range(hz1 + 1, d):
        p.set(dx, 0, z, "dirt_path" if (z - hz1) % 2 else "smooth_stone")
    porch = f["porch"]
    if porch == "canopy":
        roof = f"{ROOFS_SLAB[f['roof_c']]}[type=top]"
        for x in (dx - 1, dx, dx + 1):
            outside(x, 4, hz1 + 1, roof)
        outside(2 * dx - px, 3, hz1 + 1, f"{NS}:white_paper_lantern")
    elif porch == "veranda":
        for x in range(hx0, hx1 + 1):
            if p.get(x, 1, hz1 + 1) is None:
                p.set(x, 1, hz1 + 1, "spruce_slab[type=top]")
            outside(x, 4, hz1 + 1, f"{ROOFS_SLAB[f['roof_c']]}[type=bottom]")
        for x in (hx0, hx1):
            for y in (2, 3):
                outside(x, y, hz1 + 1, "spruce_fence")
    elif porch == "gate" and d - 1 > hz1 + 2:
        gz = d - 1
        for x in (dx - 1, dx + 1):
            for y in (1, 2):
                p.set(x, y, gz, "dark_oak_fence")
        for x in (dx - 1, dx, dx + 1):
            p.set(x, 3, gz, f"{ROOFS_SLAB[f['roof_c']]}[type=bottom]")
    elif porch == "balcony":
        bx0, bx1 = max(hx0, dx - 2), min(hx1, dx + 2)
        for x in range(bx0, bx1 + 1):
            p.set(x, 5, hz1 + 1, "spruce_planks")
            p.set(x, 5, hz1 + 2, "spruce_slab[type=top]")
            p.set(x, 6, hz1 + 2, "spruce_fence")
        for x in (bx0, bx1):
            p.fill(x, 1, hz1 + 2, x, 4, hz1 + 2, "spruce_fence")
            p.set(x, 7, hz1 + 2, "spruce_fence")      # the laundry pole's posts
        p.set(bx0 + 1, 6, hz1 + 1, "potted_fern")
        for x in range(bx0 + 1, bx1):
            if (x, 6, iz1) not in reserved and p.get(x, 6, hz1) == mc(W["wall"]) and x != sx:
                p.window(x, 6, hz1, 2, "glass_pane")    # the sliding doors behind it
    # base step round every box (the door's step stays a step)
    for x0, z0, x1, z1, _ in boxes:
        for x in range(x0 - 1, x1 + 2):
            for z in (z0 - 1, z1 + 1):
                outside(x, 1, z, "stone_brick_slab[type=bottom]")
        for z in range(z0, z1 + 1):
            outside(x0 - 1, 1, z, "stone_brick_slab[type=bottom]")
            outside(x1 + 1, 1, z, "stone_brick_slab[type=bottom]")

    # the garden: fence, a stone lantern, a tree two clear of the walls, bushes
    fence = {"bamboo": "bamboo_fence", "hedge": "azalea_leaves", "wall": "stone_brick_wall"}.get(f["fence"])
    if fence:
        for x in range(w):
            if abs(x - dx) > 1:
                outside(x, 1, d - 1, fence)
    free = [(x, z) for x in range(w) for z in range(d)
            if p.get(x, 1, z) is None and p.get(x, 0, z) == mc("grass_block") and z < d - 1
            and not (hx0 - 2 <= x <= hx1 + 2 and hz0 - 2 <= z <= hz1 + 2)
            and not (f["wing"] and boxes[1][0] - 2 <= x <= boxes[1][2] + 2 and boxes[1][1] - 2 <= z <= boxes[1][3] + 2)]
    lantern_at = [(x, z) for x in range(w) for z in range(hz1 + 2, d - 1)
                  if abs(x - dx) >= 2 and p.get(x, 1, z) is None and p.get(x, 2, z) is None]
    if lantern_at:
        x, z = r.choice(lantern_at)
        p.set(x, 1, z, f"{NS}:mossy_stone_lantern[facing=west,half=lower]")
        p.set(x, 2, z, f"{NS}:mossy_stone_lantern[facing=west,half=upper]")
    if f["tree"] and free:
        x, z = r.choice(free)
        for y in range(1, 4):
            p.set(x, y, z, "oak_log[axis=y]")
        for lx in range(x - 2, x + 3):
            for lz in range(z - 2, z + 3):
                for y in (3, 4, 5):
                    if (lx, y, lz) == (px, 3, hz1 + 1):     # the plaque stays in sight
                        continue
                    if abs(lx - x) + abs(lz - z) + abs(y - 4) <= 3 and (lx, lz) != (x, z) or y == 5 and (lx, lz) == (x, z):
                        outside(lx, y, lz, "oak_leaves")
    for _ in range(3):
        bush = [(x, z) for x in range(w) for z in range(d - 1) if p.get(x, 1, z) is None
                and p.get(x, 0, z) == mc("grass_block") and abs(x - dx) >= 1]
        if bush:
            x, z = r.choice(bush)
            p.set(x, 1, z, r.choice(("azalea_leaves", "potted_azalea_bush", "potted_fern")))

    # -- the rooms: required pieces first, then the rest, each kept only if the walk survives it
    beds_needed = {1: [2], 2: [0, 2 + f["extra_bed"]], 3: [0, 2, 1 + f["extra_bed"]]}[n]
    wanted = [entry] + (landings if n > 1 else [])
    bed_parts = []

    def ok():
        reach = walk(p, entry)
        return all(c in reach for c in wanted) and all(near(b, reach) for b in bed_parts)

    def place(items, required=False, bed=None):
        cells = [(x, y, z) for x, y, z, _ in items]
        if any(c in reserved or p.get(*c) not in (None, mc(f"{NS}:tatami[axis=x]"), mc(f"{NS}:tatami[axis=z]"))
               for c in cells):
            return False
        old = {c: p.get(*c) for c in cells}
        for x, y, z, s in items:
            p.set(x, y, z, s)
        if bed:
            bed_parts.append(bed)
        if ok():
            return True
        for c, s in old.items():
            p.set(*c, s)
        if bed:
            bed_parts.pop()
        if required:
            raise Unbuildable(f"required piece at {cells[0]}")
        return False

    def floor_cells(y):
        return [(x, z) for x in range(ix0, ix1 + 1) for z in range(iz0, iz1 + 1) if (x, y, z) not in reserved
                and p.get(x, y, z) is None and p.get(x, y - 1, z) is not None]

    def beds(y, count, colours):
        spots = []
        for x in range(ix0, ix1 + 1):
            spots += [((x, y, iz0), (x, y, iz0 + 1), "north"), ((x, y, iz1), (x, y, iz1 - 1), "south")]
        for z in range(iz0, iz1 + 1):
            spots += [((ix0, y, z), (ix0 + 1, y, z), "west"), ((ix1, y, z), (ix1 - 1, y, z), "east")]
        r.shuffle(spots)
        placed = 0
        for head, foot, facing in spots:
            if placed == count:
                break
            c = colours[placed % len(colours)]
            if place([(*head, f"{c}_bed[facing={facing},part=head]"), (*foot, f"{c}_bed[facing={facing},part=foot]")],
                     bed=(head, foot)):
                p.marker("bed", head)
                placed += 1
        if placed < count:
            raise Unbuildable(f"{placed} of {count} beds at y {y}")

    def tatami(y):
        for x, z in floor_cells(y):
            p.set(x, y, z, f"{NS}:tatami[axis={'z' if x % 2 else 'x'}]")

    def scatter(y, pieces):
        for piece in pieces:
            spots = floor_cells(y)
            wall = [(x, z) for x, z in spots if x in (ix0, ix1) or z in (iz0, iz1)]
            r.shuffle(wall)
            for x, z in wall[:12]:
                if place(piece(x, y, z)):
                    break

    # ground floor: the kitchen run (east wall in a one-storey house, else the back wall), dining, the toilet
    run = ([(x, iz0, "south") for x in range(ix1, ix0 - 1, -1)] if n > 1
           else [(ix1, z, "west") for z in range(iz0, iz1)])
    kit_pieces = ["stove", "sink", "counter", "fridge", "counter"]
    stove_done = False
    for (x, z, fc), piece in zip(run, kit_pieces):
        items = {"stove": [(x, 2, z, f"smoker[facing={fc}]"), (x, 4, z, f"iron_trapdoor[facing={fc},half=top,open=false]")],
                 "sink": [(x, 2, z, "water_cauldron[level=3]")],
                 "counter": [(x, 2, z, f"barrel[facing={fc}]"), (x, 4, z, f"spruce_trapdoor[facing={fc},half=top,open=true]")],
                 "fridge": [(x, 2, z, "white_concrete"), (x, 3, z, "white_concrete")]}[piece]
        if place(items):
            if piece == "stove":
                stove_done = True
                bed_parts.append(((x, 2, z),))   # the stove stays reachable, like a bed
    if not stove_done:
        raise Unbuildable("no stove")
    cells = floor_cells(2)
    cx = sum(x for x, _ in cells) / len(cells)
    cz = sum(z for _, z in cells) / len(cells)
    for x, z in sorted(cells, key=lambda c: abs(c[0] - cx) + abs(c[1] - cz))[:6]:
        if place([(x, 2, z, "spruce_slab[type=bottom]")]):
            for nx in (x - 1, x + 1):
                place([(nx, 2, z, "red_carpet")])
            break
    if n == 1:
        beds(2, 2, f["beds"])
    reach = walk(p, entry)
    resident = next(((x, 2, z) for x, z in sorted(floor_cells(2), key=lambda c: abs(c[0] - cx) + abs(c[1] - cz))
                     if (x, 2, z) in reach), None)
    if resident is None:
        raise Unbuildable("no resident spot")
    wanted.append(resident)
    reserved.add(resident)
    scatter(2, [lambda x, y, z: [(x, y, z, "hopper[facing=down]"), (x, y + 1, z, "birch_trapdoor[facing=north,half=bottom,open=false]")],
                lambda x, y, z: [(x, y, z, "cauldron")],
                lambda x, y, z: [(x, y, z, f"barrel[facing={r.choice(list(DIRS))}]"), (x, y + 1, z, "potted_azalea_bush")],
                lambda x, y, z: [(x, y, z, "spruce_slab[type=top]"), (x, y + 1, z, "black_concrete")],
                lambda x, y, z: [(x, y, z, "potted_fern")]])
    # upper floors: tatami, beds, then a tansu, the altar, a desk and its books, a lantern
    for s in range(1, n):
        y = FLOORS[s]
        tatami(y)
        beds(y, beds_needed[s], f["beds"][s - 1:] + f["beds"][:s - 1])
        scatter(y, [lambda x, y, z: [(x, y, z, "barrel[facing=up]"), (x, y + 1, z, "potted_spruce_sapling")],
                    lambda x, y, z: [(x, y, z, "stripped_dark_oak_wood[axis=y]"), (x, y + 1, z, "candle[candles=3,lit=false]")],
                    lambda x, y, z: [(x, y, z, "spruce_slab[type=top]"), (x, y + 1, z, "lantern[hanging=false]")],
                    lambda x, y, z: [(x, y, z, "bookshelf")],
                    lambda x, y, z: [(x, y, z, f"{NS}:white_paper_lantern")],
                    lambda x, y, z: [(x, y, z, "chest[facing=south]")]])
    # the wing: a washitsu (tatami, the altar, a tansu; a bed for a grandparent when rolled)
    if f["wing"]:
        x0, z0, x1, z1, _ = boxes[1]
        for x in range(x0 + 1, x1):
            for z in range(z0 + 1, z1):
                p.set(x, 2, z, f"{NS}:tatami[axis={'z' if x % 2 else 'x'}]")
        place([(x0 + 1, 2, z0 + 1, "stripped_dark_oak_wood[axis=y]"), (x0 + 1, 3, z0 + 1, "candle[candles=3,lit=false]")])
        place([(x0 + 1, 2, z1 - 1, "barrel[facing=up]"), (x0 + 1, 3, z1 - 1, "potted_bamboo")])
        if f["extra_bed"]:
            head, foot = (x0 + 1, 2, z0 + 2), (x0 + 2, 2, z0 + 2)
            if place([(*head, "white_bed[facing=west,part=head]"), (*foot, "white_bed[facing=west,part=foot]")], bed=(head, foot)):
                p.marker("bed", head)

    p.marker("house_plaque", (px, 3, hz1 + 1), facing="south")
    p.marker("resident", resident, group="any", job="any")
    p.marker("door_anchor", (dx, 1, hz1 + 1))
    p.cutaway = [FLOORS[s] + 3 for s in range(n)]
    p.plaster(0, 1, 0, w - 1, p.size[1] - 1, d - 1, style, seed, street_z=hz1)
    if not ok():
        raise Unbuildable("walk broken")
    if f["mirror"]:
        mirror(p)
    return p


ROOFS_SLAB = {"grey": "deepslate_tile_slab", "green": "waxed_oxidized_cut_copper_slab",
              "orange": "waxed_cut_copper_slab", "teal": "waxed_weathered_cut_copper_slab"}
SWAP = {"facing=east": "facing=west", "facing=west": "facing=east", "hinge=left": "hinge=right", "hinge=right": "hinge=left"}
SWAP_RE = re.compile("|".join(SWAP))


def mirror(p):
    """Flip the plan east to west (states turned to match), markers with it."""
    w = p.size[0]

    p.blocks = {(w - 1 - x, y, z): SWAP_RE.sub(lambda m: SWAP[m[0]], s) for (x, y, z), s in p.blocks.items()}
    for m in p.markers:
        m["pos"][0] = w - 1 - m["pos"][0]


def street(seed, lots):
    """Homes for a row of (w, d) lots, so no form comes back within five plots (MASTER_PLAN §9)."""
    out, recent = [], []
    for i, (w, d) in enumerate(lots):
        s = seed * 1000 + i * 37
        for _ in range(50):                           # small lots have few forms: then the last roll stands
            plan, f = home(s, w, d)
            if form(f) not in recent[-4:]:
                break
            s += 1
        out.append((plan, f))
        recent.append(form(f))
    return out


# -- the reference sheet and the check -------------------------------------------------------------
ROWS = [[(9, 12), (10, 12), (8, 12), (11, 12), (9, 12), (12, 12), (10, 12), (11, 12)],
        [(10, 10), (9, 11), (11, 11), (8, 10), (13, 11), (9, 10), (10, 11), (12, 10)]]


def sheet():
    import preview as P
    out = HERE.parents[2] / "docs/renders/konoha/families"
    rows = [street(k + 1, lots) for k, lots in enumerate(ROWS)]
    scenes = []
    for row in rows:
        sc, x = P.Scene(), 0
        for plan, _ in row:
            for (bx, by, bz), s in plan.blocks.items():
                sc.put((x + bx, by, bz), s)
            for xx in range(plan.size[0] + 1):
                for z in range(plan.size[2], plan.size[2] + 5):
                    sc.put((x + xx, 0, z), "dirt_path" if 0 < z - plan.size[2] < 4 else "polished_andesite")
            x += plan.size[0] + 1
        scenes.append(sc)
    canvas = P.new_canvas(2400, 1560)
    for i, sc in enumerate(scenes):
        lo, hi = sc.bounds()
        sc.draw(canvas, 1200 * P.SS, (470 + 720 * i) * P.SS, 2050 / (hi[0] - lo[0]) * P.SS, yaw=-22, pitch=24)
    P.save_canvas(canvas, out / "home.png", "Home family: two streets of lots from the master plan",
                  "Top: lots 8 to 12 wide, 12 deep. Bottom: 10 to 11 deep. Each home a seed; no form repeats within five plots.")
    canvas = P.new_canvas(2400, 1560)
    sc = scenes[0]
    lo, hi = sc.bounds()
    for i, cut in enumerate((5, 9)):
        sc.draw(canvas, 1200 * P.SS, (480 + 720 * i) * P.SS, 2050 / (hi[0] - lo[0]) * P.SS, yaw=-22, pitch=42, cut_y=cut)
    P.save_canvas(canvas, out / "home_cutaway.png", "Home family: the top street cut open",
                  "Top: the ground floors (kitchen, dining, genkan, toilet). Bottom: the first floors (tatami, beds, tansu, desk).")
    for k, row in enumerate(rows):
        print(f"row {k + 1}:", " | ".join(f"{p.size[0]}x{p.size[2]} {f['n']}F {f['kind']} {f['wing'] or '-'} {f['porch']} "
                                          f"{f['wall']}/{f['roof_c']}" for p, f in row))
    print("wrote", out / "home.png", out / "home_cutaway.png")


def check(seeds=60):
    forms, built = set(), 0
    for w in range(8, 14):
        for d in range(9, 14):
            for s in range(seeds):
                p, f = home(s, w, d)
                bp = p.blueprint()
                assert len(bp["palette"]) <= 93, (p.id, len(bp["palette"]))
                beds = [m for m in p.markers if m["type"] == "bed"]
                assert len(beds) >= 2, (p.id, f)
                for m in beds:
                    assert base_name(p.get(*m["pos"])).endswith("_bed"), (p.id, m)
                (x, y, z), = [m["pos"] for m in p.markers if m["type"] == "house_plaque"]
                assert p.get(x, y, z) is None and p.get(x, y, z - 1) and p.get(x, y, z - 2) is None, (p.id, "plaque")
                (_, _, az), = [m["pos"] for m in p.markers if m["type"] == "door_anchor"]
                assert d - az <= 3, (p.id, "door too far from the street")
                forms.add(form(f))
                built += 1
    lots = [(w, 12) for w in (9, 10, 8, 11, 9)] * 6
    seq = [form(f) for _, f in street(7, lots)]
    assert all(seq[i] not in seq[max(0, i - 4):i] for i in range(len(seq))), seq
    street(3, [(8, 9)] * 8)                           # a lot with few forms still ends its street
    print(f"ok: {built} homes on lots 8-13 x 9-13, {len(forms)} forms, a 30-lot street without a repeat in five")


def write():
    """Write the blueprint of every home.WxD.SEED design the layout's plots use."""
    import layout
    designs = {pl.get("design", "") for pl in layout.load()["plots"]}
    for design in sorted(d for d in designs if d.startswith("home.")):
        _, size, seed = design.split(".")
        w, d = map(int, size.split("x"))
        home(int(seed), w, d)[0].write()


if __name__ == "__main__":
    check() if "--check" in sys.argv else write() if "--write" in sys.argv else sheet()
