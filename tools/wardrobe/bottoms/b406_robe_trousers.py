"""Robe Trousers: loose trousers in the robe's own off-white cloth, bloused into a band at the shin,
over black open-toe sandals: the matching legs of a jonin's robe and apron."""
from kit import leg_ring
from paint import fabric, strip_fabric

META = {"name": "Robe Trousers", "gender": "unisex",
        "description": "Loose off-white trousers matching the robe, banded at the shin, black sandals.",
        "tags": ["shinobi", "hyuga"]}


def build(g):
    body = g.part("body")
    strip_fabric(body, "P", "velvet", 4951, 2, 9, 11)
    body.strip.hline(0, body.strip.w - 1, 9, "P1")
    fabric(body.bottom, "P", "velvet", 4951, 1)
    for side in ("right", "left"):
        leg = g.part(f"{side}_leg")
        strip_fabric(leg, "P", "velvet", 4952 + (side == "left"), 2, 0, 9)
        fabric(leg.top, "P", "velvet", 4952, 2)
        leg.front.vline(1 if side == "right" else 2, 1, 6, "P1")
        # Black open-toe sandals.
        strip_fabric(leg, "K", "smooth", 4954, 2, 10, 11)
        leg.front.set(1, 11, None), leg.front.set(2, 11, None)
        leg.bottom.fill("K1")
        pants = g.part(f"{side}_pants")
        for face in pants.sides:
            face.hline(0, face.w - 1, 11, "K1")
        pants.front.set(1, 11, None), pants.front.set(2, 11, None)
        pants.bottom.fill("K0")
    for ring in leg_ring(g, "blouse", 6.6, "P", 2, (5, 2, 5), "velvet", inflate=.1):
        for face in ring.sides:
            face.hline(0, face.w - 1, 0, "P3"), face.hline(0, face.w - 1, 1, "P1")
