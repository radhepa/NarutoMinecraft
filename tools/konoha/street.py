"""A sample street for the renders: the three prototype designs pasted side by side the way the
paste tool will place them from layout.json, with the street dressing roads.py will lay (packed
earth, stone kerbs, poles every twelve blocks with wires, a tree)."""
import json
from pathlib import Path

import preview as P

BLUEPRINTS = Path(__file__).with_name("blueprints")
NS = "narutominecraft:"
PLOTS = (("home_plaster_2f", 0), ("shop_tea_house", 12), ("leaf_block", 24))
LENGTH = 61


def paste(sc, name, ox, oz=0):
    bp = json.loads((BLUEPRINTS / f"{name}.json").read_text())
    for y, layer in enumerate(bp["layers"]):
        for z, row in enumerate(layer):
            for x, ch in enumerate(row):
                if ch != ".":
                    sc.put((ox + x, y, oz + z), bp["palette"][ch])


def scene():
    sc = P.Scene()
    for x in range(-2, LENGTH):
        for z in range(-1, 18):
            sc.put((x, 0, z), "grass_block")
        for z in range(11, 17):
            sc.put((x, 0, z), "dirt_path" if 12 <= z <= 15 else "cobblestone")
    for name, ox in PLOTS:
        paste(sc, name, ox)
    # poles at the street's north edge every twelve blocks, wires between
    poles = (-1, 11, 23, 35, 47, 59)
    for i, px in enumerate(poles):
        for y in range(1, 6):
            sc.put((px, y, 11), NS + "utility_pole[axis=z,part=pole]")
        sc.put((px, 6, 11), NS + ("utility_pole[axis=z,part=transformer]" if i == 1 else "utility_pole[axis=z,part=top]"))
        if i:
            a, b = poles[i - 1], px
            for x in range(a + 1, b):
                t = (x - a) / (b - a)
                sag = 2 if 0.3 < t < 0.7 else 1 if 0.12 < t < 0.88 else 0
                sc.put((x, 6, 11), NS + f"power_wire[axis=x,sag={sag}]")
    # a cherry tree in the gap between the home and the tea house, lanterns on the far kerb
    for y in range(1, 5):
        sc.put((11, y, 4), "oak_log")
    for x in range(9, 14):
        for z in range(2, 7):
            for y in range(4, 7):
                if abs(x - 11) + abs(z - 4) + abs(y - 5) <= 3:
                    if (x, y, z) != (11, 4, 4):
                        sc.put((x, y, z), "cherry_leaves")
    for x in (6, 18, 30, 42, 54):
        sc.put((x, 1, 16), NS + "stone_lantern[facing=north,half=lower]")
        sc.put((x, 2, 16), NS + "stone_lantern[facing=north,half=upper]")
    return sc
