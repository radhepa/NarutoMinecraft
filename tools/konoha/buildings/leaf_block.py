#!/usr/bin/env python3
"""Leaf apartment block: the four-storey walk-up of the residential district, and the player's
first home.

Twelve flats, three to a landing (a, b, c from west to east), opening onto an outdoor gallery on
the street side; the stair climbs the gallery's outer lane in flights that alternate ends. Every
flat has the same plan (docs/HOME.md §2 on branch home): a 6 x 6 main room with its window wall
and balcony door on the back (the layout turns the back to face the Hokage Rock), a 3 x 4
kitchenette, a 3 x 3 bathroom, a 2 x 1 genkan at the door and a 4 x 1 built-in closet. Walls
between rooms are one block, so a flat's interior is 10 x 8 with a ceiling of 3. A 4 x 2 balcony
outside the main room on the upper floors; a small fenced yard on the ground floor.

Flat 1a is the landlady's; 4b houses the family with the child upstairs; 3a is the Classic
player's flat and 2c a Varied candidate (kept free of residents). Each flat is a House Plaque
home; homes.json rows for the home session are written beside the blueprint.
"""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from kit import NS, OUT, WALLS, Plan  # noqa: E402

FLOORS = (1, 5, 9, 13)                 # floor slab heights; rooms are the three blocks above
FLAT_X = (1, 12, 23)                    # west inner x of flats a, b, c (10 wide each)
BACK, FRONT = 2, 11                     # back and front wall z; interior z 3..10
WALK, LANE, RAIL = 12, 13, 14           # the gallery
SPECIAL = {"1a": "landlady", "4b": "family_with_child", "3a": "player_classic", "2c": "player_candidate"}


def flat(p: Plan, x0: int, fy: int, fid: str, wall: str):
    """One flat. Local ix 0..9 east, iz 0..7 from the back wall toward the gallery."""
    X = lambda ix: x0 + ix
    Z = lambda iz: BACK + 1 + iz
    y1, y3 = fy + 1, fy + 3
    st = WALLS[wall]
    # partitions: the east strip (ix 6), bath | kitchen (iz 3 of the strip), main | genkan row (iz 6)
    p.fill(X(6), y1, Z(0), X(6), y3, Z(7), st["wall"])
    p.fill(X(7), y1, Z(3), X(9), y3, Z(3), st["wall"])
    p.fill(X(0), y1, Z(6), X(5), y3, Z(6), st["wall"])
    p.clear(X(1), y1, Z(6), X(1), y1 + 1, Z(6))            # genkan into the main room
    p.clear(X(6), y1, Z(4), X(6), y1 + 1, Z(4))            # main room into the kitchenette
    p.clear(X(8), y1, Z(3), X(8), y1 + 1, Z(3))            # kitchenette into the bathroom
    for ix in range(2, 6):                                  # the closet's sliding fronts
        p.shoji(X(ix), y1, Z(6), "south", dark=True)
    # floors: tatami in the main room, planks elsewhere, stone at the genkan
    for ix in range(6):
        for iz in range(6):
            p.set(X(ix), y1, Z(iz), f"{NS}:tatami[axis={'z' if ix % 2 else 'x'}]")
    p.fill(X(0), fy, Z(7), X(1), fy, Z(7), "polished_andesite")
    # front: the door into the genkan, a kitchen window; back: windows and the balcony door
    p.door(X(1), y1, FRONT, "north")
    p.window(X(8), fy + 2, FRONT)
    for ix in (0, 4, 5):
        p.window(X(ix), fy + 2, BACK)
    p.window(X(8), fy + 2, BACK)
    if fy > 1:
        p.door(X(2), y1, BACK, "south")
        p.fill(X(1), fy, 0, X(4), fy, 1, "spruce_slab[type=top]")
        for ix in range(1, 5):
            p.set(X(ix), y1, 0, "spruce_fence")
        p.set(X(1), y1, 1, "spruce_fence")
        p.set(X(4), y1, 1, "spruce_fence")
    else:
        p.door(X(2), y1, BACK, "south")
        for ix in range(0, 6):
            p.set(X(ix), y1, 0, "bamboo_fence")
    # fixtures (vanilla stand-ins until the kit's pieces land; the markers are what systems read)
    p.set(X(9), y1, Z(4), "smoker[facing=west]")            # stove: a Hearth & Harvest cooking pot
    p.set(X(9), y1, Z(5), "cauldron")                       # sink
    p.set(X(9), y1, Z(6), "barrel[facing=up]")              # counter
    p.set(X(8), y1, Z(0), "cauldron")                       # tub (ofuro)
    p.set(X(9), y1, Z(0), "cauldron")
    p.set(X(7), y1, Z(2), "cauldron")                       # washbasin, mirror above
    p.set(X(0), y1, Z(0), "blue_bed[facing=north,part=head]")
    p.set(X(0), y1, Z(1), "blue_bed[facing=north,part=foot]")
    p.set(X(5), y1 + 2, Z(0), f"{NS}:white_paper_lantern")
    # markers
    door = (X(1), y1, FRONT)
    p.marker("house_plaque", (X(0), fy + 2, Z(7)), facing="south", home=f"flat.leaf_block.{fid}")
    p.marker("mailbox", (X(2), fy + 2, WALK), facing="south", home=f"flat.leaf_block.{fid}")
    p.marker("bed", (X(0), y1, Z(0)))
    for kind, pos in (("anchor:bed", (X(0), y1, Z(0))), ("anchor:stove", (X(9), y1, Z(4))), ("anchor:sink", (X(9), y1, Z(5))),
                      ("anchor:mirror", (X(7), y1 + 1, Z(2))), ("anchor:closet", (X(3), y1, Z(5))), ("anchor:desk", (X(4), y1, Z(3))),
                      ("anchor:balcony_rail", (X(2), y1, 1)), ("anchor:visitor_wait", (X(1), y1, WALK))):
        p.marker(kind, pos, home=f"flat.leaf_block.{fid}")
    role = SPECIAL.get(fid)
    if role not in ("player_classic", "player_candidate"):
        p.marker("resident", (X(3), y1, Z(3)), group="any", job="any", **({"role": role} if role else {}))
    if role and role.startswith("player"):
        p.marker("candidate_flat", (X(3), y1, Z(3)), home=f"flat.leaf_block.{fid}", note=role)
    return {
        "id": f"flat.leaf_block.{fid}", "tier": "flat", "plaque": [X(0), fy + 2, Z(7)], "door": list(door),
        "mailbox": [X(2), fy + 2, WALK],
        "rooms": [{"id": "main", "w": 6, "d": 6, "h": 3, "at": [X(0), y1, Z(0)]},
                  {"id": "kitchenette", "w": 3, "d": 4, "h": 3, "at": [X(7), y1, Z(4)]},
                  {"id": "bathroom", "w": 3, "d": 3, "h": 3, "at": [X(7), y1, Z(0)]},
                  {"id": "genkan", "w": 2, "d": 1, "h": 3, "at": [X(0), y1, Z(7)]},
                  {"id": "closet", "w": 4, "d": 1, "h": 2, "at": [X(2), y1, Z(7)]}],
        "view": "hokage_rock (back, by layout rotation)",
        "balcony": {"w": 4, "d": 2, "at": [X(1), y1, 0], "outside_bounds": True} if fy > 1 else None,
        "yard": {"w": 6, "d": 2, "at": [X(0), y1, 0], "outside_bounds": True} if fy == 1 else None,
        "spawn": [X(1), y1, Z(7)],
        "role": role,
    }


def build(wall="cream") -> Plan:
    p = Plan("leaf_block", "Leaf apartment block (four storeys, twelve flats)", (35, 22, 15), "apartment",
             "Twelve House Plaque flats on three landings a floor; the player's flat is 3a")
    st = WALLS[wall]
    p.fill(0, 0, 0, 34, 0, 14, "dirt_path")
    p.fill(0, 0, 0, 33, 0, 1, "grass_block")
    p.fill(0, 1, BACK, 33, 1, FRONT, "stone_bricks")
    p.walls(0, BACK, 33, FRONT, 2, 16, wall)
    for x in (11, 22):
        p.fill(x, 2, BACK + 1, x, 16, FRONT - 1, st["wall"])
        p.fill(x, 2, BACK, x, 16, BACK, st["post"])
        p.fill(x, 2, FRONT, x, 16, FRONT, st["post"])
    for fy in FLOORS[1:]:
        p.fill(1, fy, BACK + 1, 32, fy, FRONT - 1, "spruce_planks")
        p.band(0, BACK, 33, FRONT, fy, wall)
    p.fill(1, 1, BACK + 1, 32, 1, FRONT - 1, "spruce_planks")
    p.flat_roof(0, 33, BACK, FRONT, 17, wall)
    p.band(0, BACK, 33, FRONT, 17, wall)
    homes = []
    for n, fy in enumerate(FLOORS, 1):
        for letter, x0 in zip("abc", FLAT_X):
            homes.append(flat(p, x0, fy, f"{n}{letter}", wall))
    # the gallery: walkway, stair lane, railing; posts at the party walls
    p.fill(0, 1, WALK, 33, 1, LANE, "stone_bricks")
    for fy in FLOORS[1:]:
        p.fill(0, fy, WALK, 33, fy, RAIL, "spruce_slab[type=top]")
        for x in range(34):
            p.set(x, fy + 1, RAIL, "spruce_fence")
    for x in (0, 11, 22, 33):
        p.fill(x, 1, RAIL, x, 16, RAIL, "stripped_spruce_log[axis=y]")
    p.fill(0, 17, WALK, 33, 17, RAIL, "smooth_stone_slab[type=bottom]")
    # flights in the stair lane, alternating ends: the street to 2, 2 to 3 (west), 3 to 4 (east)
    for a, b in ((1, 5), (9, 13)):
        p.clear(31, b, LANE, 33, b, LANE)
        for i, x in enumerate((33, 32, 31, 30)):
            p.set(x, a + 1 + i, LANE, "spruce_stairs[facing=west,half=bottom]")
    p.clear(0, 9, LANE, 2, 9, LANE)
    for i, x in enumerate((3, 2, 1, 0)):
        p.set(x, 6 + i, LANE, "spruce_stairs[facing=west,half=bottom]")
    # the roof's tanks
    for x in (4, 16, 28):
        p.water_tank(x, 18, 5, 3)
    p.water_tank(9, 18, 8, 1)
    p.marker("door_anchor", (34, 1, LANE))
    p.cutaway = [3, 11]
    OUT.mkdir(exist_ok=True)
    (OUT / "leaf_block.homes.json").write_text(json.dumps(
        {"note": "homes.json rows for the home session (branch home), in blueprint coordinates; "
                 "cells and keys are the home session's", "homes": homes}, indent=1) + "\n")
    return p


if __name__ == "__main__":
    build().write()
