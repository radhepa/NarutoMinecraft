#!/usr/bin/env python3
"""Ichiraku Ramen: the open ramen stand on Main Street, the cook's room above.

The stand: a light wood counter across the whole front, six stools on the street side under a
plank canopy, the ramen noren hung from the canopy's edge so a seated guest's head is behind it,
red paper lanterns at both ends. Behind the counter, on the same earth floor as the street, the
kitchen: the stock pots and stoves along the back wall, a prep counter, a stair up. Upstairs, the
cook's room behind a closed stair-well. Cream plaster, grey tile gable roof. VF tavern by bounds:
the stools are its seats.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from kit import NS, Plan  # noqa: E402

W = "cream"


def build() -> Plan:
    p = Plan("ichiraku", "Ichiraku Ramen", (12, 12, 12), "shop",
             "A VF tavern by bounds: six stools at the counter; the cook lives upstairs")
    p.fill(0, 0, 0, 11, 0, 11, "dirt_path")
    p.fill(1, 0, 8, 10, 0, 10, "smooth_stone")              # the paved strip the stools stand on
    p.fill(2, 0, 2, 9, 0, 6, "polished_andesite")           # the kitchen floor, flush with the street
    p.walls(1, 1, 10, 7, 1, 7, W)
    p.band(1, 1, 10, 7, 4, W)
    p.fill(2, 4, 2, 9, 4, 6, "spruce_planks")
    # the counter across the front, open above it to the band
    p.clear(2, 1, 7, 9, 3, 7)
    p.fill(2, 1, 7, 9, 1, 7, "birch_planks")
    for x in (1, 10):
        p.fill(x, 1, 7, x, 3, 7, "stripped_spruce_log[axis=y]")
    # the canopy, the noren under its edge, lanterns at the ends, stools on the street side
    p.fill(1, 4, 8, 10, 4, 9, "spruce_slab[type=top]")
    p.fill(2, 3, 9, 9, 3, 9, f"{NS}:ramen_noren[facing=south]")
    for x in (1, 10):
        p.set(x, 3, 9, f"{NS}:red_paper_lantern")
    for x in range(3, 9):
        p.set(x, 1, 8, "birch_slab[type=bottom]")
    # the kitchen: stoves, pots and barrels on the back wall, shelves above, a prep counter by the door
    for x, s in zip(range(2, 9), ("barrel[facing=up]", "smoker[facing=south]", "water_cauldron[level=3]", "furnace[facing=south]",
                                  "water_cauldron[level=3]", "smoker[facing=south]", "barrel[facing=up]")):
        p.set(x, 1, 2, s)
    p.fill(2, 3, 2, 8, 3, 2, "spruce_trapdoor[facing=south,half=top,open=false]")
    p.fill(2, 1, 3, 3, 1, 3, "spruce_slab[type=top]")
    p.set(5, 3, 4, f"{NS}:white_paper_lantern")
    p.window(1, 2, 4, 1)
    p.door(1, 1, 5, "west")
    # the stair up the east wall in a closed well, the door at its foot, its last step the upper floor, open into the cook's room
    p.fill(8, 1, 3, 8, 3, 6, "spruce_planks")
    p.fill(8, 2, 2, 8, 3, 2, "spruce_planks")                # over the end barrel
    p.fill(9, 2, 7, 9, 3, 7, "spruce_planks")                # the well's end over the counter
    p.door(8, 1, 6, "east")                                  # onto a landing: residents don't climb a step from a doorway
    for i, z in enumerate((5, 4, 3, 2)):
        p.set(9, 1 + i, z, "spruce_stairs[facing=north,half=bottom]")
    p.clear(9, 4, 3, 9, 4, 6)
    p.fill(8, 5, 2, 8, 7, 6, "spruce_planks")
    p.clear(8, 5, 2, 8, 6, 2)
    p.fill(9, 8, 2, 9, 8, 6, "spruce_planks")                # the well's ceiling, under the roof
    # the cook's room: tatami, the bed against the north wall, a chest, a lamp
    for x in range(2, 8):
        for z in range(2, 7):
            p.set(x, 5, z, f"{NS}:tatami[axis=x]")    # mats lie on the floor, level with the bed
    p.set(2, 5, 2, "white_bed[facing=north,part=head]")
    p.set(2, 5, 3, "white_bed[facing=north,part=foot]")
    p.set(3, 5, 2, "chest[facing=south]")
    p.set(7, 5, 6, f"{NS}:white_paper_lantern")
    # a low table with cushions, a tansu, the cook's own bowls on a shelf by the window
    for x in (4, 5):
        p.low_table(x, 5, 5)
        p.set(x, 5, 4, "red_carpet")
    p.tansu(2, 5, 6, "east", top="potted_fern")
    for x in (5, 6):
        p.set(x, 5, 6, "spruce_slab[type=top]")
        p.set(x, 6, 6, "flower_pot")
    for x in (3, 6):
        p.window(x, 5, 7, 2)
    p.window(1, 5, 4, 2)
    p.window(10, 6, 4)
    gable = p.gable_roof(1, 10, 1, 7, 8, "grey", gable_style=W)
    assert gable < 12
    # a bench and stacked barrels in the side alley
    p.fill(0, 1, 2, 0, 1, 3, "spruce_slab[type=bottom]")
    p.fill(11, 1, 2, 11, 2, 2, "barrel[facing=up]")
    p.marker("tavern_bounds", (1, 0, 1), to=[10, 4, 9])
    for x in range(3, 9):
        p.marker("seat", (x, 1, 8), facing="north")
    p.marker("resident", (5, 1, 4), group="civilian", job="ichiraku")
    p.marker("bed", (2, 5, 2))
    p.marker("house_plaque", (4, 6, 8), facing="south")     # outside on the front wall, the keeper's rooms behind it
    p.marker("door_anchor", (5, 1, 10))
    p.cutaway = [4]
    return p


if __name__ == "__main__":
    build().write()
