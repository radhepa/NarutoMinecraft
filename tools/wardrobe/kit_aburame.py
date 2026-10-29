"""Aburame building blocks: the standing collar that hides the mouth, round and oval tinted lenses,
a deep hood, a hood worn down on the shoulders, and the kikaichu beetle and moth glyphs.

The clan hides its face: tall collars rise from the torso in front of the chin (a top may not paint
the head, so the collar is a ring of torso pieces around the lower face), and the eyes go behind
dark lenses worn as headwear.
"""
from __future__ import annotations

from paint import fabric, k, solid

# A kikaichu beetle seen from above, for decals at double resolution: '#' shell, '+' wing seam.
BEETLE = ["..#..#..",
          "...##...",
          ".######.",
          "###++###",
          ".##++##.",
          "###++###",
          ".##++##.",
          "..#..#.."]

# A resting moth: two broad wings with an eye spot each and a slender body down the middle.
MOTH = ["##.......##",
        "###.....###",
        "####.#.####",
        "#oo##+##oo#",
        "#oo##+##oo#",
        "####.+.####",
        ".###.+.###.",
        "..##...##..",
        "...#...#..."]


def glyph(face, rows, x0: int, y0: int, legend: dict):
    for y, row in enumerate(rows):
        for x, ch in enumerate(row):
            if ch in legend:
                face.set(x0 + x, y0 + y, legend[ch])


def high_collar(g, role: str = "P", texture: str = "weave", seed: int = 10600, base: int = 2, cover_mouth: bool = True,
                front_top: float = -2.2, back_top: float = -4.0, flare: float = 4):
    """A stiff standing collar around the lower head: a back wall, two side walls flaring out a
    little and, with `cover_mouth`, a front wall up to the nose that hides the mouth. Without it the
    collar stands open at the front, like a coat collar turned up."""
    walls = []
    back = g.piece("collar_back", "TORSO", (-5, back_top, 4.2), (10, int(1 - back_top), 1), rotation=(-6, 0, 0))
    walls.append(back)
    for side, sign in (("right", -1), ("left", 1)):
        x = -5.2 if sign < 0 else 4.2
        wall = g.piece(f"collar_{side}", "TORSO", (0, (front_top + back_top) / 2 - .5, -5.2 if cover_mouth else -3.0),
                       (1, int(1.5 - (front_top + back_top) / 2), 10 if cover_mouth else 8), pivot=(x, 0, 0),
                       rotation=(0, 0, flare * sign))
        walls.append(wall)
    if cover_mouth:
        front = g.piece("collar_front", "TORSO", (-5, front_top, -5.2), (10, int(1 - front_top), 1))
        walls.append(front)
    for i, w in enumerate(walls):
        solid(w, role, texture, seed + i, base, edge=False)
        for f in w.sides:
            f.hline(0, f.w - 1, 0, k(role, base + 1))
            f.hline(0, f.w - 1, f.h - 1, k(role, base - 1))
    if cover_mouth:
        # A fold down the middle where the collar closes, and its inner shadow along the top.
        front.front.vline(5, 1, front.h - 1, k(role, base - 1))
        front.top.fill(k(role, base - 2))
    return walls


def hood_down(g, role: str = "P", texture: str = "twill", seed: int = 10620, base: int = 2):
    """A deep hood worn down: a heavy fold of cloth lying on the shoulders behind the collar."""
    hood = g.piece("hood_down", "TORSO", (-4.5, -2.0, 0), (9, 4, 3), pivot=(0, 0, 2.6), rotation=(14, 0, 0))
    solid(hood, role, texture, seed, base)
    hood.top.fill(k(role, base - 2))   # the hood's dark inside
    for f in hood.sides:
        f.hline(0, f.w - 1, 0, k(role, base + 1))
    tip = g.piece("hood_point", "TORSO", (-1.5, 2, 0), (3, 2, 2), pivot=(0, 0, 2.6), rotation=(14, 0, 0))
    solid(tip, role, texture, seed + 1, base)
    return hood


def lenses(g, lens: str = "K", frame: str = "M", shape: str = "round", y: float = -3.3, z: float = -4.3,
           temples: bool = True):
    """Dark lenses over both eyes, each built from two crossed quarter-scale plates so it reads
    round (or oval, wider than tall), a bridge, and arms back along the head to the ears."""
    q = (.25, .25, .25)
    tall, wide = ((8, 12), (12, 8)) if shape == "round" else ((10, 10), (14, 6))
    for side, sign in (("right", -1), ("left", 1)):
        for name, (w, h) in (("tall", tall), ("wide", wide)):
            box = g.piece(f"lens_{side}_{name}", "HEAD", (-w / 2, -h / 2, -.5), (w, h, 1), pivot=(2.1 * sign, y, z),
                          scale=q)
            for f in box.faces:
                f.fill(k(frame, 2))
            f = box.front
            f.fill(k(lens, 1))
            if name == "tall":
                f.hline(0, w - 1, 0, k(frame, 3)), f.hline(0, w - 1, h - 1, k(frame, 1))
            else:
                f.vline(0, 0, h - 1, k(frame, 2)), f.vline(w - 1, 0, h - 1, k(frame, 2))
            f.hline(1, w - 2, 1 if name == "wide" else 2, k(lens, 2))
            # A glint in the upper outer corner.
            gx = 2 if sign < 0 else w - 4
            f.set(gx, 2, k(lens, 4)), f.set(gx + 1, 2, k(lens, 3)), f.set(gx, 3, k(lens, 3))
    bridge = g.piece("lens_bridge", "HEAD", (-2, -.5, -.5), (4, 1, 1), pivot=(0, y - .6, z), scale=q)
    for f in bridge.faces:
        f.fill(k(frame, 2))
    if temples:
        for side, sign in (("right", -1), ("left", 1)):
            arm = g.piece(f"lens_arm_{side}", "HEAD", (-.5, -.5, 0), (1, 1, 18), pivot=(4.15 * sign, y - .6, z),
                          scale=q)
            for f in arm.faces:
                f.fill(k(frame, 1))


def deep_hood(g, role: str = "P", texture: str = "twill", seed: int = 10640, base: int = 2, front_z: float = -4.9):
    """A deep hood pulled up over the head, rounded by a stepped crown, its opening shadowed."""
    top = g.piece("hood_top", "HEAD", (-4.5, -9.6, front_z), (9, 1, 10), inflate=.1)
    solid(top, role, texture, seed, base, edge=False)
    fabric(top.top, role, texture, seed, base + 1)
    top.front.fill(k(role, base + 1))
    crown = g.piece("hood_crown", "HEAD", (-3, -10.4, front_z + 2), (6, 1, 7))
    solid(crown, role, texture, seed + 1, base + 1, edge=False)
    for side, x in (("right", -5.7), ("left", 4.7)):
        wall = g.piece(f"hood_{side}", "HEAD", (x, -9, front_z), (1, 10, 10), inflate=.1)
        solid(wall, role, texture, seed + 2 + (x > 0), base)
        outer = wall.right if x < 0 else wall.left
        for xx in range(2, outer.w - 1, 4):
            outer.vline(xx, 1, outer.h - 1, k(role, base - 1))
        (wall.left if x < 0 else wall.right).fill(k(role, 0))
        wall.front.fill(k(role, base + 1))
    back = g.piece("hood_back", "HEAD", (-5.5, -9, 4.4), (11, 11, 1), inflate=.1)
    solid(back, role, texture, seed + 4, base)
    back.back.vline(5, 1, 10, k(role, base - 1))
    point = g.piece("hood_point", "HEAD", (-1.5, 0, 0), (3, 3, 1), pivot=(0, 1.8, 4.6), rotation=(12, 0, 0))
    solid(point, role, texture, seed + 5, base)
    # The shadow inside the brim, above the lenses.
    shade = g.piece("hood_shade", "HEAD", (-4.5, -8.6, front_z + .4), (9, 1, 1))
    for f in shade.faces:
        f.fill(k(role, 0))
