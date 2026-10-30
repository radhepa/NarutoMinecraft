#!/usr/bin/env python3
"""Large store: Main Street's two-storey stores, a showroom at the front and a workroom behind.

Ground floor, four blocks high: three bays to the street between timber posts, display windows on
a plinth in the side bays and the open entrance under the noren in the wide centre bay, the awning
above and the signboard on the upper wall (the weapon shop adds a shuriken sign on its roof). The showroom shows the trade's goods and has the
keeper's counter; a partition with a door closes off the workroom at the back, where a stair along
the back wall climbs into a closed well. Upstairs: the keeper's flat. Tile gable roof.

`trade` picks the fittings (KONOHA_BUILD.md, catalogue, "Large store"): the furniture shop with
its showroom and joinery bench, the weapon shop with its racks and the forge room, whose brick
chimney climbs through the roof.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from kit import NS, Plan  # noqa: E402

SHURIKEN = ["..#..",  # a four-point star with its hole
            ".###.",
            "##.##",
            ".###.",
            "..#.."]


def furniture(p: Plan):
    # the showroom: a tatami corner with a low table and cushions, shoji screens, lamps and a dresser
    for x in range(2, 7):
        for z in range(7, 11):
            p.set(x, 1, z, f"{NS}:tatami[axis=x]")
    p.set(4, 2, 8, "spruce_trapdoor[facing=south,half=bottom,open=false]")
    p.set(4, 2, 9, "spruce_trapdoor[facing=south,half=bottom,open=false]")
    for x, z in ((3, 8), (3, 9), (5, 8), (5, 9)):
        p.set(x, 2, z, "red_carpet")
    for z in (7, 9):
        p.shoji(7, 2, z, "east")
    p.set(2, 2, 6, "chest[facing=south]")
    p.set(3, 2, 6, "barrel[facing=south]")
    p.set(2, 3, 6, f"{NS}:white_paper_lantern")
    p.set(6, 2, 6, f"{NS}:stone_lantern[facing=south,half=lower]")
    p.set(6, 3, 6, f"{NS}:stone_lantern[facing=south,half=upper]")
    p.fill(12, 2, 6, 13, 2, 6, "bookshelf")                 # behind the counter, clear of the workroom door
    for x in (9, 10):
        p.set(x, 2, 9, "spruce_stairs[facing=west,half=bottom]")
    p.set(11, 2, 9, "spruce_fence")
    p.set(11, 3, 9, "spruce_pressure_plate")
    # the workroom: the joinery bench, a loom, the saw and stacked timber
    p.set(2, 2, 2, "crafting_table")
    p.set(3, 2, 2, "loom[facing=south]")
    p.set(4, 2, 2, "stonecutter[facing=south]")
    p.fill(2, 2, 4, 3, 3, 4, "stripped_spruce_log[axis=x]")
    p.set(5, 2, 4, "barrel[facing=up]")


def weapons(p: Plan):
    # the showroom: spear racks down the west wall, a grille of blades on the east, a whetstone and a target
    for z in range(6, 11):
        p.set(2, 2, z, "dark_oak_fence")
        if z % 2 == 0:
            p.fill(2, 3, z, 2, 4, z, "lightning_rod[facing=up]")
        else:
            p.set(2, 3, z, "iron_chain")
    p.fill(14, 3, 9, 14, 4, 10, "iron_bars")
    p.set(14, 2, 9, "barrel[facing=up]")
    p.set(14, 2, 10, "barrel[facing=up]")
    p.set(6, 2, 8, "grindstone[face=floor,facing=south]")
    p.set(12, 2, 10, "target")
    p.set(5, 2, 6, "anvil[facing=east]")
    # the forge room: the furnace under the brick chimney, the anvil, the quench tub and the smith's bench
    p.fill(2, 2, 2, 4, 2, 2, "bricks")
    p.set(3, 2, 2, "blast_furnace[facing=south]")
    p.fill(2, 3, 2, 4, 5, 2, "bricks")
    p.set(5, 2, 3, "anvil[facing=east]")
    p.set(2, 2, 4, "water_cauldron[level=3]")
    p.set(5, 2, 2, "smithing_table")
    p.set(6, 2, 2, "grindstone[face=floor,facing=south]")


TRADES = {"furniture": furniture, "weapons": weapons}


def build(id="shop_large", title="Large store", trade="furniture", wall="terracotta", roof="grey", awning="green",
          noren="indigo", bed="brown", job="furniture_shop", floor="spruce_planks") -> Plan:
    p = Plan(id, title, (17, 20, 13), "shop", f"The {title.lower()}: the keeper sells at the counter and lives upstairs")
    p.fill(0, 0, 0, 16, 0, 12, "dirt_path")
    p.fill(1, 0, 12, 15, 0, 12, "smooth_stone")
    p.fill(1, 1, 1, 15, 1, 11, "stone_bricks")
    p.fill(2, 1, 2, 14, 1, 10, floor)
    p.walls(1, 1, 15, 11, 2, 9, wall)
    p.band(1, 1, 15, 11, 6, wall)
    p.fill(2, 6, 2, 14, 6, 10, "spruce_planks")
    p.fill(2, 10, 2, 14, 10, 10, "spruce_planks")              # the attic floor closes the flat under the roof
    # the front: display windows in the side bays, the open entrance in the centre bay
    for x in (5, 11):
        p.fill(x, 2, 11, x, 5, 11, "stripped_dark_oak_log[axis=y]")
    for xa, xb in ((2, 4), (12, 14)):
        p.fill(xa, 2, 11, xb, 2, 11, "spruce_planks")
        p.fill(xa, 3, 11, xb, 5, 11, "white_stained_glass_pane")
    p.clear(6, 2, 11, 10, 5, 11)
    p.fill(6, 1, 11, 10, 1, 11, floor)
    p.fill(6, 5, 11, 10, 5, 11, f"{NS}:{noren}_noren[facing=south]")
    p.fill(1, 6, 12, 15, 6, 12, f"{NS}:{awning}_awning[facing=south]")
    p.set(1, 5, 12, f"{NS}:red_paper_lantern")
    p.set(15, 5, 12, f"{NS}:red_paper_lantern")
    # the signboard on the upper wall: a dark frame round a light board
    p.fill(5, 7, 12, 11, 9, 12, "dark_oak_planks")
    p.fill(6, 8, 12, 10, 8, 12, "birch_planks")
    # the keeper's counter in the showroom, the partition and door to the workroom
    p.fill(10, 2, 7, 13, 2, 7, "spruce_planks")
    p.fill(10, 3, 7, 13, 3, 7, "spruce_slab[type=bottom]")
    p.fill(2, 2, 5, 14, 5, 5, "spruce_planks")
    p.door(7, 2, 5, "south")
    for x in (4, 12):
        p.set(x, 5, 8, f"{NS}:white_paper_lantern")
    TRADES[trade](p)
    # the stair along the back wall of the closed workroom, its last step the upper floor, open into the flat
    for i, x in enumerate(range(8, 13)):
        p.set(x, 2 + i, 2, "spruce_stairs[facing=east,half=bottom]")
    p.clear(8, 6, 2, 11, 6, 2)
    # the keeper's flat: tatami, the bed by the east wall over the counter, a chest, a low table, lamps
    for x in range(2, 15):
        for z in range(2, 11):
            if not (7 <= x <= 12 and z == 2) and p.get(x, 6, z) and not p.get(x, 7, z):
                p.set(x, 7, z, f"{NS}:tatami[axis=x]")    # mats lie on the floor, level with the bed
    p.set(13, 7, 7, f"{bed}_bed[facing=north,part=head]")
    p.set(13, 7, 8, f"{bed}_bed[facing=north,part=foot]")
    p.set(14, 7, 7, "chest[facing=west]")
    for z in (7, 8):
        p.set(8, 7, z, "spruce_trapdoor[facing=south,half=bottom,open=false]")
    p.set(13, 9, 9, f"{NS}:white_paper_lantern")
    p.set(4, 9, 4, f"{NS}:white_paper_lantern")
    # the cooking run on the back wall, a rail along the stairwell, a tansu by the bed, the keeper's desk,
    # cushions round the table, and the trade's own corner (offcuts and a bench, or a whetstone)
    p.stove(4, 7, 2, "south")
    p.set(5, 7, 2, "water_cauldron[level=3]")
    p.counter(6, 7, 2, "south")
    p.fridge(7, 7, 2)
    p.tansu(2, 7, 2, "south", top="potted_azalea_bush")
    for x in range(8, 12):
        p.set(x, 7, 3, "spruce_fence")
    for x in (7, 9):
        for z in (7, 8):
            p.set(x, 7, z, "red_carpet")
    p.tansu(14, 7, 8, "west")
    p.desk(14, 7, 4)
    p.set(14, 7, 10, "potted_bamboo")
    if trade == "weapons":
        p.set(2, 7, 10, "grindstone[face=floor,facing=east]")
        p.set(3, 7, 10, "barrel[facing=up]")
    else:
        p.set(2, 7, 10, "crafting_table")
        p.set(3, 7, 10, "stripped_spruce_log[axis=x]")
    for x in (3, 13):
        p.window(x, 7, 11, 2)
    for z in (4, 8):
        p.window(1, 7, z, 2)
        p.window(15, 7, z, 2)
    for x in (5, 11):
        p.window(x, 7, 1, 2)
    p.window(1, 3, 7, 2)
    p.window(15, 3, 3, 2)
    p.gable_roof(1, 15, 1, 11, 10, roof, gable_style=wall)
    if trade == "weapons":
        for y in range(6, 16):
            p.set(3, y, 2, "bricks")
        # the roof sign standing on the front slope against the ridge: the shuriken on a white board
        p.fill(5, 13, 7, 11, 19, 7, "dark_oak_planks")
        for r, row in enumerate(SHURIKEN):
            for c, ch in enumerate(row):
                p.set(6 + c, 18 - r, 7, "black_concrete" if ch == "#" else "white_concrete")
    p.marker("resident", (11, 2, 6), group="civilian", job=job)
    p.marker("bed", (13, 7, 7))
    p.marker("house_plaque", (8, 8, 10), facing="north")
    p.marker("door_anchor", (8, 1, 12))
    p.cutaway = [6, 10]
    return p


if __name__ == "__main__":
    build("furniture_shop", "Furniture shop").write()
    build("weapon_shop", "Weapon shop", trade="weapons", wall="white", roof="grey", awning="red", noren="red",
          bed="red", job="weapon_shop", floor="polished_andesite").write()
