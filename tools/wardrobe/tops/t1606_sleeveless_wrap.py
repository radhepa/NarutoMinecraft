"""Sleeveless Wrap: a dusky crossover top without sleeves, closed by a steel-grey sash, mesh at the
throat, bandaged forearms and a senbon cuff on the right wrist: a genin learning the needle."""
from kit_shinobi import bandage, mesh
from kit_shiranui import wrist_holster
from paint import cap, solid, strip_fabric

META = {
    "name": "Sleeveless Wrap",
    "gender": "unisex",
    "description": "Sleeveless dusky crossover top, steel sash, mesh at the throat, a senbon cuff on the right wrist.",
    "tags": ["shinobi", "genin", "wrap"],
}


def build(g):
    body = g.part("body")
    strip_fabric(body, "D", "weave", 16810, 2)
    cap(body, "D", seed=16810)
    f = body.front
    mesh(f, 2, 0, 5, 1)
    for y in range(8):
        f.set(min(7, 2 + y), y, "D3")
        if y < 6:
            f.set(min(7, 3 + y), y, "D1")
    sash = g.piece("sash", "TORSO", (-4.6, 8.4, -2.6), (9, 2, 5), inflate=.06)
    solid(sash, "P", "weave", 16811, 2, edge=False)
    sash.front.set(6, 0, "P4"), sash.front.set(6, 1, "P0")
    for side in ("right", "left"):
        arm = g.part(f"{side}_arm")
        bandage(arm.strip, 0, 7, arm.strip.w - 1, 11)
    wrist_holster(g, "right", seed=16812, y=7.4)
