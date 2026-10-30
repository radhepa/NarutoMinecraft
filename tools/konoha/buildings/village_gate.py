#!/usr/bin/env python3
"""The main gate and the village wall.

`main_gate`, drawn from the anime's shots of the gate: two great timber pillars carry a white lintel
with the red Leaf mark on both faces and a dark wooden gable roof over an eleven-block opening. The
two pale green gate leaves stand swung back against the wall's inner face, the red あ on the west leaf
and ん on the east, read from the village side. The guards' booth sits inside to the east, and the wall
runs on from the pillars to both edges of the plot. Its street side (south before the paste turns it)
is the village side.

`village_wall`: one sixteen-block module of the wall the gate stands in: a stone base, a timber face
of planks between posts with a dark band, a walkway on top behind a parapet, lanterns on the inner
face. The layout lines modules up along the wall's run; sweep.py takes over for the curved full ring.

Scale: the opening is 17 blocks high, about nine times a player; the wall is 18.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from kit import NS, Plan  # noqa: E402

WALL_H = 18          # the walkway's height
DEPTH = 6            # the wall's thickness, z 3..8 in the gate, 0..5 in a module
LEAF = ["...###...",  # the Leaf mark: the spiral and the leaf's point to the lower left
        "..#...#..",
        ".#..#..#.",
        ".#..##.#.",
        "..#....#.",
        "####..#..",
        "..####..."]
A = ["..#...",            # あ, on the west leaf
     "######",
     "..#.#.",
     ".####.",
     "#.#..#",
     ".#..#."]
N = ["..#...",            # ん, on the east leaf
     "..#...",
     ".#....",
     ".##...",
     "#..#.#",
     "#..##."]


def wall(p, x0, x1, z0):
    """The wall's section from x0 to x1, z0..z0+5, inner face at z0+5 (the village side, south before the turn)."""
    z1 = z0 + DEPTH - 1
    for x in range(x0, x1 + 1):
        post = x % 4 == 0
        for z in range(z0, z1 + 1):
            face = z in (z0, z1)
            for y in range(1, WALL_H):
                if y <= 3:
                    s = "stone_bricks" if face else "cobblestone"
                elif not face:
                    s = "packed_mud"
                elif y == 9 or y == WALL_H - 1:
                    s = "stripped_dark_oak_log[axis=x]"
                else:
                    s = "stripped_spruce_log[axis=y]" if post else "spruce_planks"
                p.set(x, y, z, s)
            p.set(x, WALL_H, z, "spruce_planks")
        p.set(x, WALL_H + 1, z0, "dark_oak_planks" if x % 2 == 0 else "dark_oak_slab[type=bottom]")
        p.set(x, WALL_H + 1, z1, "spruce_fence")
        if x % 8 == 4:
            p.set(x, 7, z1 + 1, f"{NS}:white_paper_lantern")


def panel(p, x0, y0, z, rows, ink="red_concrete"):
    """A pattern on the x-y plane facing south: row 0 at the top, column 0 at x0."""
    for i, row in enumerate(rows):
        for j, ch in enumerate(row):
            if ch == "#":
                p.set(x0 + j, y0 + len(rows) - 1 - i, z, ink)


def gate() -> Plan:
    W, D = 41, 12
    p = Plan("main_gate", "Main gate", (W, 37, D), "landmark", "The great gate; the village side faces Main Street")
    p.fill(0, 0, 0, W - 1, 0, D - 1, "dirt_path")
    p.fill(15, 0, 0, 25, 0, D - 1, "packed_mud")
    wall(p, 0, 12, 3)
    wall(p, 28, W - 1, 3)
    # the pillars: stone footings, timber shafts two blocks square, from the ground to the roof
    for x0 in (13, 26):
        p.fill(x0, 1, 2, x0 + 1, 2, 9, "polished_andesite")
        p.fill(x0, 3, 3, x0 + 1, 27, 8, "stripped_spruce_log[axis=y]")
        for z in (3, 8):
            for x in (x0, x0 + 1):
                p.set(x, 3, z, "dark_oak_planks")
    # the lintel: white boards from pillar to pillar over the opening, the Leaf mark on both faces
    p.fill(15, 19, 3, 25, 27, 8, "spruce_planks")
    p.fill(12, 18, 2, 28, 18, 9, "stripped_dark_oak_log[axis=x]")
    p.fill(12, 28, 2, 28, 28, 9, "stripped_dark_oak_log[axis=x]")
    for z in (2, 9):
        p.fill(12, 19, z, 28, 27, z, "white_concrete")
        panel(p, 16, 20, z, LEAF)
    p.gable_roof(12, 28, 2, 10, 29, "wood", overhang=1, pitch="steep")
    # the gate leaves, six wide and seventeen high, as high as the opening, swung back against the wall's inner face
    for x0, glyph in ((7, A), (28, N)):
        p.fill(x0, 1, 9, x0 + 5, 17, 9, "lime_terracotta")
        for y in (1, 17):
            p.fill(x0, y, 9, x0 + 5, y, 9, "green_terracotta")
        panel(p, x0, 10, 9, glyph)
    # the guards' booth inside the gate, past the east leaf: a desk under a little roof
    p.fill(35, 1, 10, 39, 1, 10, "spruce_planks")
    p.fill(35, 2, 10, 39, 2, 10, "spruce_slab[type=bottom]")
    for x in (35, 39):
        p.fill(x, 1, 11, x, 3, 11, "spruce_fence")
    p.fill(35, 4, 10, 39, 4, 11, "dark_oak_slab[type=bottom]")
    p.set(36, 1, 11, "spruce_stairs[facing=north,half=bottom]")
    p.set(38, 1, 11, "spruce_stairs[facing=north,half=bottom]")
    for x in (14, 26):
        p.set(x, 1, 10, f"{NS}:stone_lantern[facing=south,half=lower]")
        p.set(x, 2, 10, f"{NS}:stone_lantern[facing=south,half=upper]")
    # shortcut: no guards yet, they need beds of their own; add them with the guards' barracks
    p.marker("door_anchor", (20, 1, D - 1))
    return p


def module() -> Plan:
    p = Plan("village_wall", "Village wall (sixteen-block module)", (16, WALL_H + 2, DEPTH + 1), "wall",
             "Line modules up along the wall's run; the inner face is south before the turn")
    wall(p, 0, 15, 0)
    return p


if __name__ == "__main__":
    gate().write()
    module().write()
