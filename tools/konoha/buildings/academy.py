#!/usr/bin/env python3
"""Ninja Academy: the long two-storey school on Main Street, its plaza in front and its yard behind.

Drawn from the anime: a long tan building under a low orange tile roof, dark posts between rows of
windows, and the white disc with the red fire kanji over the entrance; the tree with its swing stands
on the plaza in front. The ground floor is three classrooms off a front corridor (desks in rows, a blackboard,
the teacher's lectern); upstairs, the library and a fourth classroom. Behind it the yard: target posts,
training logs. The workshop (the Academy supply counter's workbenches) stands
on the plaza's east side. The street side is south before the paste turns it.

Beta 1 dresses every room; the exam hall is dressed at Beta 3 (KONOHA_BUILD.md, landmarks).
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from kit import NS, Plan  # noqa: E402

W, H, D = 64, 20, 56
X0, X1, Z0, Z1 = 8, 55, 22, 42          # the school's walls
CX = 31                                  # the entrance's west block; the front is symmetric about 31.5
ROOMS = ((9, 22), (24, 39), (41, 54))     # ground-floor classrooms, x ranges


def classroom(p, xa, xb, y, za, zb):
    """Benches and desks facing a blackboard on the north wall, the teacher's podium and lectern in front, a lantern overhead."""
    c = (xa + xb) // 2
    p.fill(c - 3, y + 1, za, c + 3, y + 2, za, "black_concrete")
    p.fill(c - 4, y, za, c + 4, y, za + 2, "spruce_slab[type=bottom]")
    p.set(c, y + 1, za + 2, "lectern[facing=south]")
    for z in range(za + 5, zb, 3):
        for x in range(xa + 1, xb):
            if x != c:
                p.set(x, y, z, "spruce_slab[type=top]")
                p.set(x, y, z + 1, "spruce_stairs[facing=south,half=bottom]")
    p.set(c, y + 3, (za + zb) // 2, f"{NS}:white_paper_lantern")


def tree(p, x, z):
    """The Academy tree: an oak with a wide crown and a plank swing on its east branch."""
    p.fill(x, 1, z, x, 7, z, "oak_log[axis=y]")
    for dx in range(-4, 5):
        for dz in range(-4, 5):
            for y in range(6, 11):
                if dx * dx + dz * dz + (y - 8) ** 2 * 2 <= 20 and p.get(x + dx, y, z + dz) is None:
                    p.set(x + dx, y, z + dz, "oak_leaves[persistent=true]")
    p.fill(x + 1, 6, z, x + 3, 6, z, "oak_log[axis=x]")
    for dz in (-1, 1):
        p.fill(x + 3, 3, z + dz, x + 3, 5, z + dz, "oak_fence")
    p.fill(x + 3, 2, z - 1, x + 3, 2, z + 1, "oak_slab[type=top]")


def build() -> Plan:
    p = Plan("academy", "Ninja Academy", (W, H, D), "landmark",
             "Classrooms, library, yard, tree and workshop (Beta 1); the exam hall is dressed at Beta 3")
    # the ground: grass, the paved plaza in front, the yard behind, a fence round the plot open to the street
    p.fill(0, 0, 0, W - 1, 0, D - 1, "grass_block")
    p.fill(14, 0, 44, 49, 0, D - 1, "polished_andesite")
    for x in range(14, 50):
        for z in range(44, D):
            if (x + z) % 2 and not CX - 1 <= x <= CX + 2:
                p.set(x, 0, z, "smooth_stone")
    p.fill(CX - 1, 0, 43, CX + 2, 0, D - 1, "stone_bricks")
    p.fill(3, 0, 2, 60, 0, 19, "coarse_dirt")
    for x in range(W):
        p.set(x, 1, 0, "spruce_fence")
        if not 14 <= x <= 49:
            p.set(x, 1, D - 1, "spruce_fence")
    for z in range(D):
        p.set(0, 1, z, "spruce_fence")
        p.set(W - 1, 1, z, "spruce_fence")

    # the school: two storeys of tan plaster, floors at 1 and 6, a band at each floor line
    p.walls(X0, Z0, X1, Z1, 1, 11, "cream")
    p.fill(X0, 1, Z0, X1, 1, Z1, "stone_bricks")
    p.fill(X0 + 1, 1, Z0 + 1, X1 - 1, 1, Z1 - 1, "oak_planks")
    p.fill(X0 + 1, 6, Z0 + 1, X1 - 1, 6, Z1 - 1, "oak_planks")
    p.band(X0, Z0, X1, Z1, 6, "cream")
    p.band(X0, Z0, X1, Z1, 11, "cream")
    for y in (3, 8):
        for x in range(X0 + 2, X1 - 1):
            if x % 3 != 1 and not CX - 2 <= x <= CX + 3:
                p.window(x, y, Z0, 2)
                p.window(x, y, Z1, 2)
        for z in range(Z0 + 2, Z1 - 1, 3):
            p.window(X0, y, z, 2)
            p.window(X1, y, z, 2)
    for x in range(X0 + 6, X1 - 4, 8):
        p.fill(x, 2, Z1, x, 10, Z1, "stripped_dark_oak_log[axis=y]")
    p.gable_roof(X0, X1, Z0, Z1, 12, "orange", gable_style="cream")

    # the entrance: a four-wide opening, a tiled canopy on posts, lanterns either side, the fire sign above
    p.clear(CX - 1, 2, Z1, CX + 2, 4, Z1)
    for x in (CX - 2, CX + 3):
        p.fill(x, 2, Z1, x, 5, Z1, "stripped_dark_oak_log[axis=y]")
        p.fill(x, 1, Z1 + 2, x, 4, Z1 + 2, "stripped_dark_oak_log[axis=y]")
    p.fill(CX - 3, 5, Z1 + 1, CX + 4, 5, Z1 + 3, "waxed_cut_copper_slab[type=bottom]")
    for x in (CX - 4, CX + 5):
        p.set(x, 1, Z1 + 3, f"{NS}:stone_lantern[facing=south,half=lower]")
        p.set(x, 2, Z1 + 3, f"{NS}:stone_lantern[facing=south,half=upper]")
    p.fire_sign(CX, 15, Z1 + 1)

    # ground floor: a corridor along the front, three classrooms behind it, a doorway into each
    p.fill(X0 + 1, 2, 36, X1 - 1, 5, 36, "smooth_red_sandstone")
    for xa, xb in ROOMS[:2]:
        p.fill(xb + 1, 2, Z0 + 1, xb + 1, 5, 35, "smooth_red_sandstone")
    for xa, xb in ROOMS:
        c = (xa + xb) // 2
        p.clear(c - 1, 2, 36, c, 3, 36)
        p.shoji(c - 2, 2, 36)
        p.shoji(c + 1, 2, 36)
        classroom(p, xa, xb, 2, Z0 + 1, 35)
    for x in range(X0 + 4, X1 - 2, 8):
        p.set(x, 5, 39, f"{NS}:white_paper_lantern")
    for x in (X0 + 2, X1 - 2):
        p.set(x, 2, Z1 - 1, "potted_azalea_bush")
    # the stairs up, at the corridor's west end
    for i in range(4):
        p.set(X0 + 2 + i, 2 + i, 39, "spruce_stairs[facing=east,half=bottom]")
        p.clear(X0 + 2 + i, 6, 38, X0 + 2 + i, 6, 40)

    # upstairs: the library to the west, a classroom to the east
    p.fill(32, 7, Z0 + 1, 32, 10, Z1 - 1, "smooth_red_sandstone")
    p.clear(32, 7, 37, 32, 8, 38)
    for x in range(X0 + 4, 30, 3):
        p.fill(x, 7, Z0 + 2, x, 9, 33, "bookshelf")
    p.fill(18, 7, 37, 26, 7, 37, "spruce_slab[type=top]")
    for x in (18, 22, 26):
        p.set(x, 7, 38, "spruce_stairs[facing=south,half=bottom]")
    for x in (14, 24):
        p.set(x, 10, 36, f"{NS}:white_paper_lantern")
    classroom(p, 33, X1, 7, Z0 + 1, Z1 - 2)

    # the yard: a line of target posts, a circle of training logs
    for x in (8, 12, 16, 20, 24):
        p.set(x, 1, 4, "stripped_spruce_log[axis=y]")
        p.set(x, 2, 4, "target")
        p.marker("training_target", (x, 2, 4))
    for x, z in ((14, 11), (18, 11), (12, 14), (20, 14), (14, 17), (18, 17)):
        p.fill(x, 1, z, x, 2, z, "stripped_oak_log[axis=y]")
    for x in (4, 59):
        p.set(x, 1, 3, "hay_block[axis=y]")
        p.set(x, 1, 4, "hay_block[axis=y]")

    # the workshop on the plaza's east side: workbenches, barrels and a grindstone under a grey roof
    p.walls(51, 46, 61, 54, 1, 5, "cream")
    p.fill(52, 1, 47, 60, 1, 53, "spruce_planks")
    p.gable_roof(51, 61, 46, 54, 6, "grey", gable_style="cream")
    p.clear(51, 2, 49, 51, 3, 50)
    for z in range(47, 54, 2):
        p.window(61, 3, z, 2)
    for x in (53, 55, 57):
        p.set(x, 2, 47, "crafting_table")
    p.set(59, 2, 47, "grindstone[face=floor,facing=south]")
    for z in (51, 52, 53):
        p.set(60, 2, z, "barrel[facing=up]")
    p.set(56, 5, 50, f"{NS}:white_paper_lantern")
    # the swing tree on the plaza in front, in its own patch of grass
    p.fill(43, 0, 48, 45, 0, 50, "grass_block")
    tree(p, 44, 49)
    # the plaza's west side: benches under two planted trees
    for x0 in (4, 9):
        p.fill(x0, 1, 50, x0 + 2, 1, 50, "spruce_stairs[facing=north,half=bottom]")
    for x in (3, 12):
        p.fill(x, 1, 47, x, 3, 47, "oak_log[axis=y]")
        for dx in (-1, 0, 1):
            for dz in (-1, 0, 1):
                p.set(x + dx, 4, 47 + dz, "oak_leaves[persistent=true]")
        p.set(x, 5, 47, "oak_leaves[persistent=true]")

    p.marker("anchor:academy.grounds", (CX, 1, 50))
    p.marker("anchor:academy.yard", (16, 1, 9))
    p.marker("anchor:academy.library", (20, 7, 36))
    p.marker("door_anchor", (CX, 1, D - 1))
    p.cutaway = [5, 11]
    return p


if __name__ == "__main__":
    build().write()
