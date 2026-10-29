#!/usr/bin/env python3
"""Two-storey plaster home: the commonest house of Konoha's residential streets.

Cream plaster on a stone base, timber corner posts, a terracotta band at the floor line, a green
tile gable roof with a kawara ridge, white paper windows, and a small front garden with a toro.
Inside: an earth-floored entry (genkan), a tatami living room behind shoji, a kitchen corner and a
stair; upstairs two tatami rooms with beds. Sleeps two to three (a civilian family or two shinobi).

Variants the paste tool rolls per plot: wall style (cream, white, terracotta), roof (green, grey,
orange), mirror, garden or none. Here: cream and green.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from kit import NS, Plan  # noqa: E402


def build(wall="cream", roof="green") -> Plan:
    p = Plan("home_plaster_2f", "Two-storey plaster home", (11, 14, 11), "home",
             "A House Plaque inside the door flood-fills the house; beds upstairs; 2-3 residents")
    # ground and garden
    p.fill(0, 0, 0, 10, 0, 10, "grass_block")
    p.fill(4, 0, 8, 6, 0, 10, "dirt_path")
    p.set(5, 0, 8, "smooth_stone")
    for x in range(0, 11):  # a low bamboo fence along the street with a gap for the path
        if x not in (4, 5, 6):
            p.set(x, 1, 10, "bamboo_fence")
    for z in range(8, 10):
        p.set(0, 1, z, "bamboo_fence")
        p.set(10, 1, z, "bamboo_fence")
    p.set(8, 1, 9, f"{NS}:mossy_stone_lantern[facing=west,half=lower]")
    p.set(8, 2, 9, f"{NS}:mossy_stone_lantern[facing=west,half=upper]")
    p.set(2, 1, 9, "potted_azalea_bush")
    p.set(1, 1, 8, "azalea_leaves")
    p.set(2, 1, 8, "azalea_leaves")
    # base, floors, walls
    p.fill(1, 1, 1, 9, 1, 7, "stone_bricks")
    p.fill(2, 1, 2, 8, 1, 6, "spruce_planks")
    p.walls(1, 1, 9, 7, 2, 8, wall)
    p.fill(2, 5, 2, 8, 5, 6, "spruce_planks")
    p.band(1, 1, 9, 7, 5, wall)
    # front: door with a little tiled canopy over it
    p.door(5, 2, 7, "north")
    p.fill(4, 1, 8, 6, 1, 8, "smooth_stone_slab[type=bottom]")
    p.set(5, 1, 8, "smooth_stone_slab[type=bottom]")
    for x in (4, 5, 6):
        p.set(x, 4, 8, "waxed_oxidized_cut_copper_slab[type=top]")
    p.window(2, 3, 7)
    p.window(3, 3, 7)
    p.window(7, 3, 7)
    p.window(8, 3, 7)
    for x in (2, 3, 7, 8):
        p.window(x, 6, 7, 2)
    for z in (3, 5):
        p.window(1, 3, z)
        p.window(9, 3, z)
        p.window(1, 6, z, 2)
        p.window(9, 6, z, 2)
    for x in (3, 7):
        p.window(x, 6, 1, 2)
        p.window(x, 3, 1)
    # ground floor inside: genkan (stone), living room on tatami behind shoji, kitchen corner
    p.fill(4, 1, 5, 6, 1, 6, "polished_andesite")
    for x in range(2, 9):
        for z in range(2, 5):
            if x <= 6:
                p.set(x, 2, z, f"{NS}:tatami[axis={'z' if x % 2 else 'x'}]")
    for x in (2, 3, 7):
        p.shoji(x, 2, 5, "south")
    p.set(8, 2, 2, "smoker[facing=south]")
    p.set(8, 2, 3, "cauldron")
    p.set(7, 2, 2, "barrel[facing=up]")
    # stair up along the east wall
    for i, z in enumerate((6, 5, 4)):
        p.set(8, 2 + i, z, "spruce_stairs[facing=north,half=bottom]")
    p.clear(8, 5, 3, 8, 5, 6)
    # upstairs: two tatami rooms split by a shoji wall
    for x in range(2, 8):
        for z in range(2, 7):
            p.set(x, 6, z, f"{NS}:tatami[axis={'z' if x % 2 else 'x'}]")
    p.clear(2, 6, 2, 7, 6, 2)
    p.set(2, 6, 2, "blue_bed[facing=south,part=head]")
    p.set(2, 6, 3, "blue_bed[facing=south,part=foot]")
    p.set(7, 6, 5, "red_bed[facing=west,part=foot]")
    p.set(6, 6, 5, "red_bed[facing=west,part=head]")
    for z in (2, 3):
        p.shoji(5, 6, z, "east")
    p.set(4, 6, 6, "chest[facing=north]")
    p.set(6, 6, 2, f"{NS}:white_paper_lantern")
    # roof: eaves at the top of the upper walls
    p.gable_roof(1, 9, 1, 7, 9, roof, gable_style=wall)
    # markers for the Village Friends homes, census and routines
    p.marker("house_plaque", (5, 3, 6), facing="south")
    p.marker("bed", (2, 6, 2))
    p.marker("bed", (7, 6, 5))
    p.marker("resident", (4, 2, 3), group="any", job="any")
    p.marker("door_anchor", (5, 1, 8))
    p.cutaway = [5, 9]
    return p


if __name__ == "__main__":
    build().write()
