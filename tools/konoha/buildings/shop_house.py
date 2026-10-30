#!/usr/bin/env python3
"""Shop-house: the Leaf's two-storey corner shop, the trade's goods set out on the street.

Ground floor: a wood-floored shop open to the street across two bays, the noren across the top of
each and the awning above; goods on a tiered stand along the front and on shelves down both side
walls, the counter at the back. A hanging kanban board stands out from the corner post. Upstairs:
the family's room behind square shuttered windows, a closed stair-well and door. Tile gable roof.

One program for the shop-houses of KONOHA_BUILD.md's catalogue: the arguments recolour it. Only
the grocer's goods so far; the Haruno store, barber and courier office bring theirs with their
districts.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from kit import NS, Plan  # noqa: E402

# the grocer's goods on the front stand (either side of the centre post) and on the side shelves (z 2..5), low then high
STAND = ["pumpkin", "melon", "hay_block", "melon", "pumpkin", "hay_block"]
SHELF = ["barrel[facing=up]", "composter[level=8]", "barrel[facing=up]", "dried_kelp_block"]
TOP = ["melon", "pumpkin", "hay_block", "barrel[facing=up]"]


def build(id="shop_house", title="Shop-house", wall="cream", roof="green", awning="green",
          noren="indigo", bed="green", job="grocer") -> Plan:
    p = Plan(id, title, (11, 13, 11), "shop", f"The {title.lower()}: the keeper sells from the counter and lives upstairs")
    p.fill(0, 0, 0, 10, 0, 10, "dirt_path")
    p.fill(1, 0, 8, 9, 0, 10, "smooth_stone")
    p.fill(1, 1, 1, 9, 1, 7, "stone_bricks")
    p.fill(2, 1, 2, 8, 1, 6, "spruce_planks")
    p.walls(1, 1, 9, 7, 2, 8, wall)
    p.band(1, 1, 9, 7, 5, wall)
    p.fill(2, 5, 2, 8, 5, 6, "spruce_planks")
    # the open front, two bays, noren and awning
    p.clear(2, 2, 7, 8, 4, 7)
    p.fill(2, 1, 7, 8, 1, 7, "spruce_planks")
    for x in (1, 5, 9):
        p.fill(x, 2, 7, x, 4, 7, "stripped_dark_oak_log[axis=y]")
    p.fill(2, 4, 7, 4, 4, 7, f"{NS}:{noren}_noren[facing=south]")
    p.fill(6, 4, 7, 8, 4, 7, f"{NS}:{noren}_noren[facing=south]")
    p.fill(1, 5, 8, 9, 5, 8, f"{NS}:{awning}_awning[facing=south]")
    # the stand along the front, the gap at the centre post
    for x, goods in zip((2, 3, 4, 6, 7, 8), STAND):
        p.set(x, 1, 8, goods)
    # side shelves: goods in a column of two at each wall, the keeper's counter at the back
    for z, (low, high) in zip(range(2, 6), zip(SHELF, TOP)):
        for x in (2, 8):
            if x == 2 or z >= 4:
                p.set(x, 2, z, low)
                p.set(x, 3, z, high)
    p.fill(4, 2, 5, 6, 2, 5, "spruce_planks")
    p.fill(4, 3, 5, 6, 3, 5, "spruce_slab[type=bottom]")
    p.set(5, 4, 5, f"{NS}:white_paper_lantern")
    # the kanban: a dark board hung from the eave by the corner post
    p.fill(10, 6, 8, 10, 7, 8, "dark_oak_planks")
    p.set(10, 8, 8, "iron_chain")
    # the stair along the back wall behind a partition, a door at its foot (VF floods rooms door to door, and
    # residents path through a door on the level), its last step the upper floor; the family's room
    p.fill(3, 2, 2, 3, 4, 2, "spruce_planks")
    p.fill(3, 2, 3, 8, 4, 3, "spruce_planks")
    p.door(4, 2, 3, "north")                                 # onto a landing: residents don't climb a step from a doorway
    for i, x in enumerate((5, 6, 7, 8)):
        p.set(x, 2 + i, 2, "spruce_stairs[facing=east,half=bottom]")
    p.clear(5, 5, 2, 7, 5, 2)
    p.fill(4, 6, 2, 4, 8, 2, "spruce_planks")
    for x in range(2, 9):
        for z in range(3 if x >= 5 else 2, 7):
            if not p.get(x, 6, z):
                p.set(x, 6, z, f"{NS}:tatami[axis=x]")    # mats lie on the floor, level with the bed
    p.set(2, 6, 2, f"{bed}_bed[facing=north,part=head]")
    p.set(2, 6, 3, f"{bed}_bed[facing=north,part=foot]")
    p.set(3, 6, 2, "chest[facing=south]")
    p.set(8, 6, 6, f"{NS}:white_paper_lantern")
    # the family's room: a cooking corner on the east wall, a low table, a tansu, the grocer's desk and ledgers
    p.stove(8, 6, 4, "west")
    p.counter(8, 6, 5, "west")
    for x in (4, 5):
        p.low_table(x, 6, 5)
    for x in (3, 6):
        p.set(x, 6, 5, "red_carpet")
    p.tansu(2, 6, 6, "east", top="potted_fern")
    p.desk(6, 6, 6)
    p.set(7, 6, 6, "bookshelf")
    # square windows with shutters: two at the front, one on each side upstairs, one on each side below
    for x in (3, 7):
        p.set(x, 7, 7, "white_stained_glass_pane")
        p.set(x - 1, 7, 8, "spruce_trapdoor[facing=south,half=bottom,open=true]")
        p.set(x + 1, 7, 8, "spruce_trapdoor[facing=south,half=bottom,open=true]")
    for x in (3, 7):
        p.window(x, 7, 1)
    for x in (1, 9):
        p.window(x, 7, 4)
        p.window(x, 3, 6)
    p.gable_roof(1, 9, 1, 7, 9, roof, gable_style=wall)
    p.marker("resident", (5, 2, 4), group="civilian", job=job)
    p.marker("bed", (2, 6, 2))
    p.marker("house_plaque", (4, 7, 6), facing="north")
    p.marker("door_anchor", (5, 1, 9))
    p.cutaway = [5, 9]
    return p


if __name__ == "__main__":
    build("grocer", "Grocer").write()
