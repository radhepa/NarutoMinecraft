#!/usr/bin/env python3
"""Tea house: the market street's shop-house, with an open front under an awning and noren.

Ground floor: an earth-floored shop (doma) open to the street across two bays, the noren hung
across the top of each, a striped awning over the front with paper lanterns at both ends, a counter
and tables inside, a raised tatami room at the back for guests who stay. Benches out front.
Upstairs: the owner's rooms behind a wooden lattice front (koshi). Orange tile gable roof.

The same program makes the market street's other small shops (KONOHA_BUILD.md, catalogue): the
arguments recolour it and swap the noren; a trade's fittings (shelves, crates, racks) replace the
tables. The two rival tea houses on one corner are two of these, one with the green awning.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from kit import NS, Plan  # noqa: E402


def build(wall="cream", roof="orange", awning="red", noren="tea") -> Plan:
    p = Plan("shop_tea_house", "Tea house (market shop-house)", (11, 14, 11), "shop",
             "A VF tavern by bounds (the Phase 0 hook): seats at the benches and tables; the owner lives upstairs")
    p.fill(0, 0, 0, 10, 0, 10, "dirt_path")
    p.fill(0, 0, 8, 10, 0, 10, "packed_mud")
    p.fill(1, 1, 1, 9, 1, 7, "stone_bricks")
    p.fill(2, 1, 2, 8, 1, 6, "packed_mud")                  # the earth floor of the shop
    p.walls(1, 1, 9, 7, 2, 8, wall)
    p.band(1, 1, 9, 7, 5, wall)
    p.fill(2, 5, 2, 8, 5, 6, "spruce_planks")
    # the open front: two bays between timber posts, a noren across the top of each
    p.clear(2, 2, 7, 8, 4, 7)
    p.fill(2, 1, 7, 8, 1, 7, "packed_mud")
    for x in (1, 5, 9):
        p.fill(x, 2, 7, x, 4, 7, "stripped_dark_oak_log[axis=y]")
    p.fill(2, 4, 7, 4, 4, 7, f"{NS}:{noren}_noren[facing=south]")
    p.fill(6, 4, 7, 8, 4, 7, f"{NS}:{noren}_noren[facing=south]")
    p.fill(1, 5, 8, 9, 5, 8, f"{NS}:{awning}_awning[facing=south]")
    p.set(1, 4, 8, f"{NS}:red_paper_lantern")
    p.set(9, 4, 8, f"{NS}:red_paper_lantern")
    # benches out front, and the low step
    p.fill(2, 1, 8, 8, 1, 8, "smooth_stone_slab[type=bottom]")
    for x in (2, 3, 7, 8):
        p.set(x, 1, 9, "spruce_slab[type=bottom]")
    # inside: counter on the left, two tables, a raised tatami room at the back
    p.fill(2, 2, 4, 3, 2, 4, "barrel[facing=up]")
    p.set(2, 2, 5, "smoker[facing=east]")
    for x, z in ((6, 5), (7, 4)):
        p.set(x, 2, z, "spruce_fence")
        p.set(x, 3, z, "spruce_slab[type=bottom]")
    p.fill(7, 2, 2, 8, 2, 3, "spruce_slab[type=top]")
    for x in range(7, 9):
        for z in (2, 3):
            p.set(x, 3, z, f"{NS}:tatami[axis=x]")
    p.set(8, 4, 2, f"{NS}:white_paper_lantern")
    # upstairs: lattice front of dark fences (koshi), paper windows on the other sides
    for x in (2, 3, 4, 6, 7, 8):
        p.fill(x, 6, 7, x, 7, 7, "dark_oak_fence")
    for x in (3, 7):
        p.window(x, 6, 1, 2)
    for z in (3, 5):
        p.window(1, 6, z, 2)
        p.window(9, 6, z, 2)
    p.window(1, 3, 3)
    p.window(9, 3, 3)
    # stair along the back wall to the owner's rooms, its last step the upper floor; a partition and a door at its
    # foot close it off from the open shop (VF floods rooms door to door, and residents path through a door on the level)
    p.fill(2, 2, 3, 6, 4, 3, "spruce_planks")
    p.fill(7, 2, 2, 7, 4, 2, "spruce_planks")
    p.door(6, 2, 3, "north")                                 # onto a landing: residents don't climb a step from a doorway
    for i, x in enumerate((5, 4, 3, 2)):
        p.set(x, 2 + i, 2, "spruce_stairs[facing=west,half=bottom]")
    p.clear(3, 5, 2, 4, 5, 2)
    p.fill(5, 6, 2, 5, 8, 2, "spruce_planks")
    p.set(8, 6, 3, "red_bed[facing=north,part=head]")
    p.set(8, 6, 4, "red_bed[facing=north,part=foot]")
    # the owner's rooms: a cooking corner past the partition, a low table, tea canisters on the tansu
    p.stove(6, 6, 2, "south")
    p.set(7, 6, 2, "water_cauldron[level=3]")
    p.counter(8, 6, 2, "south")
    p.low_table(6, 6, 5)
    for x in (5, 7):
        p.set(x, 6, 5, "red_carpet")
    p.tansu(2, 6, 6, "east", top="decorated_pot")
    p.set(3, 6, 6, "decorated_pot")
    p.set(8, 6, 6, f"{NS}:white_paper_lantern")
    p.gable_roof(1, 9, 1, 7, 9, roof, gable_style=wall)
    p.marker("tavern_bounds", (1, 1, 1), to=[9, 8, 9])
    for x in (2, 3, 7, 8):
        p.marker("seat", (x, 1, 9), facing="north")
    p.marker("seat", (5, 2, 5))
    p.marker("seat", (7, 2, 5))
    p.marker("resident", (3, 2, 5), group="civilian", job="tea_house")
    p.marker("bed", (8, 6, 3))
    p.marker("house_plaque", (5, 6, 4), facing="south")
    p.marker("door_anchor", (5, 1, 9))
    p.cutaway = [5, 9]
    return p


if __name__ == "__main__":
    build().write()
