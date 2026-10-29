"""Padded Trousers: thick quilted trousers stitched in channels, gathered into white shin wraps above
open-toe sandals, with a snack pouch strapped to the right thigh."""
from kit_akimichi import quilt, snack_pouch
from kit_shinobi import sandals, wraps
from paint import fabric, solid

META = {"name": "Padded Trousers", "gender": "unisex",
        "description": "Thick quilted trousers gathered into white wraps, a thigh snack pouch, sandals.",
        "tags": ["shinobi", "akimichi"]}


def build(g):
    body = g.part("body")
    for face in body.sides:
        quilt(face, "D", 6955, 2, 0, 9, face.w, 3)
    fabric(body.bottom, "D", "weave", 6955, 1)
    for side in ("right", "left"):
        leg = g.part(f"{side}_leg")
        for face in leg.sides:
            quilt(face, "D", 6956 + (side == "left"), 2, 0, 0, face.w, 6)
        fabric(leg.top, "D", "weave", 6956, 2)
    wraps(g)
    sandals(g)
    for side, bone in (("right", "RIGHT_LEG"), ("left", "LEFT_LEG")):
        puff = g.piece(f"{side}_blouse", bone, (-2.5, 4.4, -2.5), (5, 2, 5), inflate=.15)
        solid(puff, "D", "weave", 6958, 2)
        for face in puff.sides:
            face.hline(0, face.w - 1, 0, "D3")
    strap = g.piece("thigh_strap", "RIGHT_LEG", (-2.45, 1.2, -2.45), (5, 1, 5))
    solid(strap, "L", "leather", 6959, 2)
    snack_pouch(g, "thigh_snack", (-2.8, 1.4, -.6), role="A", size=(1, 3, 2), bone="RIGHT_LEG", seed=6960)
