#!/usr/bin/env python3
"""Streets from layout.json: one blueprint per street, tools/konoha/blueprints/street.<id>.json.

A street is an axis-aligned centre line with an odd width. Its ground layer is packed earth (dirt
path) between kerbs; main and ring streets carry a utility pole every twelve blocks on one kerb with
wires between, and a stone lantern every twelve on the other, offset by six. Poles and lanterns are
left out where another street meets the kerb, so every junction stays open. The paste tool lays each
street's [0, 0, 0] at the north-west corner of its run (layout.street_rect).
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import layout as L  # noqa: E402
from kit import NS, Plan  # noqa: E402

SURFACE = {"main": ("stone_bricks", "dirt_path"), "ring": ("stone_bricks", "dirt_path"),
           "lane": ("cobblestone", "dirt_path"), "alley": ("gravel", "dirt_path")}
POLES = {"main", "ring"}
STEP = 12


def build(street: dict, others: list[dict]) -> Plan:
    x0, z0, x1, z1 = L.street_rect(street)
    w, d = x1 - x0 + 1, z1 - z0 + 1
    along_x = street["from"][1] == street["to"][1]
    kerb, surface = SURFACE[street["class"]]
    p = Plan("street." + street["id"], street["name"], (w, 7, d), "street", f"{street['class']} street, {street['width']} wide")
    for x in range(w):
        for z in range(d):
            edge = (z in (0, d - 1)) if along_x else (x in (0, w - 1))
            p.set(x, 0, z, kerb if edge else surface)
    if street["class"] not in POLES:
        return p
    run = w if along_x else d

    def cell(i, far):  # the kerb cell i blocks along the run, on the near (north or west) or far kerb
        return (i, d - 1 if far else 0) if along_x else (w - 1 if far else 0, i)

    def open_(i, far):  # a pole or lantern here would stand in another street's mouth
        cx, cz = cell(i, far)
        return any(L.touches(L.street_rect(o), x0 + cx, z0 + cz) for o in others)

    poles = [i for i in range(0, run, STEP) if not open_(i, False)]
    cross = "z" if along_x else "x"
    for n, i in enumerate(poles):
        cx, cz = cell(i, False)
        for y in range(1, 6):
            p.set(cx, y, cz, f"{NS}:utility_pole[axis={cross},part=pole]")
        p.set(cx, 6, cz, f"{NS}:utility_pole[axis={cross},part={'transformer' if n % 4 == 1 else 'top'}]")
        if n:
            a = poles[n - 1]
            for j in range(a + 1, i):
                t = (j - a) / (i - a)
                sag = 2 if 0.3 < t < 0.7 else 1 if 0.12 < t < 0.88 else 0
                wx, wz = cell(j, False)
                p.set(wx, 6, wz, f"{NS}:power_wire[axis={'x' if along_x else 'z'},sag={sag}]")
    facing = "north" if along_x else "west"
    for i in range(STEP // 2, run, STEP):
        if open_(i, True):
            continue
        cx, cz = cell(i, True)
        p.set(cx, 1, cz, f"{NS}:stone_lantern[facing={facing},half=lower]")
        p.set(cx, 2, cz, f"{NS}:stone_lantern[facing={facing},half=upper]")
    return p


def main():
    lay = L.load()
    for s in lay["streets"]:
        build(s, [o for o in lay["streets"] if o is not s]).write()


if __name__ == "__main__":
    main()
