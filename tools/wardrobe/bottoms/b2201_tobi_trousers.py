"""Tobi Trousers: the scaffold builder's balloon trousers in indigo, cut very full through the thigh
and knee so they billow out, gathered tight at the shin into black split-toe jika-tabi."""
from kit import waistband
from kit_kinoshita import tabi
from paint import fabric, solid, strip_fabric

META = {"name": "Tobi Trousers", "gender": "unisex",
        "description": "Very full indigo balloon trousers gathered at the shin into black split-toe jika-tabi.",
        "tags": ["shinobi", "kinoshita", "work"]}


def build(g):
    waistband(g, "D", "twill", 22601)
    for side in ("right", "left"):
        leg = g.part(f"{side}_leg")
        strip_fabric(leg, "D", "twill", 22602 + (side == "left"), 2, 0, 7)
        fabric(leg.top, "D", "twill", 22602, 2)
    tabi(g, top=7)
    # The billow: one full drum of cloth from the hip to below the knee, pleated down its length.
    for side, bone in (("right", "RIGHT_LEG"), ("left", "LEFT_LEG")):
        drum = g.piece(f"{side}_billow", bone, (-2.5, .2, -2.5), (5, 6, 5), inflate=.3)
        solid(drum, "D", "twill", 22604, 2)
        for face in drum.sides:
            for x in range(1, face.w, 2):
                face.vline(x, 1, face.h - 1, "D1")
            face.hline(0, face.w - 1, 0, "D3")
        drum.bottom.fill("D0")
        cuff = g.piece(f"{side}_gather", bone, (-2.5, 6.2, -2.5), (5, 1, 5))
        solid(cuff, "D", "twill", 22606, 1, edge=False)
        for face in cuff.sides:
            for x in range(0, face.w, 2):
                face.set(x, 0, "D2")
