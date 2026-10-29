#!/usr/bin/env python3
"""Apartment block: the three-storey walk-up where young shinobi and small households live.

Nine one-room flats, three to a floor, opening onto an outdoor gallery on the street side. The stair
climbs the gallery's outer lane: the first flight at the east end, the second at the west end, so
the gallery stays clear to every door. A flat roof with a parapet carries the block's round water
tanks. Cream plaster with a terracotta band at each floor line.

Every flat is a House Plaque home with one bed, so Village Friends homes it on its own; the paste
tool keeps the player's flat (one of these, per KONOHA_BUILD.md, "Candidate flats") free of
residents. Variants: wall style, the number of storeys (2 to 4), mirror.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from kit import NS, WALLS, Plan  # noqa: E402

FLOORS = (1, 5, 9)          # floor heights of the three storeys
FLATS = ((1, 3), (5, 7), (9, 11))  # inner x ranges of the three flats on each floor


def build(wall="cream") -> Plan:
    p = Plan("apartment_block", "Apartment block (three storeys, nine flats)", (14, 18, 11), "apartment",
             "Nine House Plaque flats with one bed each; 9 to 12 residents; one candidate flat for the player")
    st = WALLS[wall]
    p.fill(0, 0, 0, 13, 0, 10, "dirt_path")
    p.fill(0, 1, 0, 12, 1, 6, "stone_bricks")
    p.walls(0, 0, 12, 6, 2, 12, wall)
    for y in (5, 9):
        p.fill(1, y, 1, 11, y, 5, "spruce_planks")
        p.band(0, 0, 12, 6, y, wall)
    p.flat_roof(0, 12, 0, 6, 13, wall)
    p.band(0, 0, 12, 6, 13, wall)
    # party walls between the flats
    for x in (4, 8):
        p.fill(x, 2, 1, x, 12, 5, st["wall"])
    for fy in FLOORS:
        for (x0, x1), door_x in zip(FLATS, (2, 6, 10)):
            p.fill(x0, fy, 1, x1, fy, 5, "spruce_planks")
            p.door(door_x, fy + 1, 6, "north")
            p.window(x1, fy + 2, 6)
            p.window(door_x, fy + 2, 0)
            p.set(x0, fy + 1, 1, "blue_bed[facing=north,part=head]" if door_x != 6 else "red_bed[facing=north,part=head]")
            p.set(x0, fy + 1, 2, "blue_bed[facing=north,part=foot]" if door_x != 6 else "red_bed[facing=north,part=foot]")
            p.set(x1, fy + 1, 1, "chest[facing=south]")
            for x in range(x0 + 1, x1 + 1):
                for z in range(3, 6):
                    p.set(x, fy + 1, z, f"{NS}:tatami[axis={'z' if x % 2 else 'x'}]")
            p.set(x1, fy + 1, 3, f"{NS}:white_paper_lantern")
            p.marker("house_plaque", (door_x, fy + 2, 5), facing="south")
            p.marker("bed", (x0, fy + 1, 1))
            p.marker("resident", (door_x, fy + 1, 4), group="any", job="any")
    # the gallery: z 7 walkway, z 8 stair lane, z 9 railing, on posts
    for y in (5, 9):
        p.fill(0, y, 7, 12, y, 9, "spruce_slab[type=top]")
        for x in range(0, 13):
            p.set(x, y + 1, 9, "spruce_fence")
    for x in (0, 6, 12):
        p.fill(x, 1, 9, x, 12, 9, "stripped_spruce_log[axis=y]")
    p.fill(0, 13, 7, 12, 13, 9, "smooth_stone_slab[type=bottom]")  # the canopy over the top gallery
    # the ground-floor walkway, a step up from the street
    p.fill(0, 1, 7, 12, 1, 8, "stone_bricks")
    for x in (3, 4, 8, 9):
        p.set(x, 1, 9, "smooth_stone_slab[type=bottom]")
    # flight 1: the street up to the first gallery, climbing west at the east end
    p.clear(10, 5, 8, 12, 5, 8)
    for i, x in enumerate((13, 12, 11, 10, 9)):
        p.set(x, 1 + i, 8, "spruce_stairs[facing=west,half=bottom]")
    # flight 2: the first gallery up to the second, climbing west at the west end
    p.clear(1, 9, 8, 3, 9, 8)
    for i, x in enumerate((3, 2, 1, 0)):
        p.set(x, 6 + i, 8, "spruce_stairs[facing=west,half=bottom]")
    # roof: water tanks, a vent, and a ladder hatch from the top gallery
    p.water_tank(2, 14, 2, 3)
    p.water_tank(4, 14, 2, 1)
    p.water_tank(9, 14, 3, 2)
    p.set(7, 14, 4, "stone_brick_wall")
    p.set(11, 13, 5, "spruce_trapdoor[facing=south,half=top,open=false]")
    # a lantern by each flight, a potted plant by the doors
    p.set(5, 6, 7, "potted_azalea_bush")
    p.set(9, 10, 7, "potted_azalea_bush")
    p.set(1, 2, 7, "potted_azalea_bush")
    p.marker("door_anchor", (13, 1, 8))
    p.marker("candidate_flat", (6, 10, 4), note="top floor, middle flat: the Classic save's flat")
    p.cutaway = [3, 7]
    return p


if __name__ == "__main__":
    build().write()
