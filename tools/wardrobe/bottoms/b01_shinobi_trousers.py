"""Shinobi Trousers: navy trousers bloused into white shin wraps, a thigh holster and open-toe sandals."""
from kit_shinobi import sandals, wraps
from paint import fabric, solid, strip_fabric

META = {"name": "Shinobi Trousers", "gender": "unisex",
        "description": "Navy trousers, white shin wraps, kunai holster on the right thigh, blue sandals.",
        "tags": ["shinobi"]}


def build(g):
    body = g.part("body")
    strip_fabric(body, "D", "twill", 40, 2, 9, 11)
    body.strip.hline(0, body.strip.w - 1, 9, "D1")
    fabric(body.bottom, "D", "twill", 40, 1)
    for side in ("right", "left"):
        leg = g.part(f"{side}_leg")
        strip_fabric(leg, "D", "twill", 42 + (side == "left"), 2, 0, 5)
        fabric(leg.top, "D", "twill", 42, 2)
        leg.strip.hline(0, leg.strip.w - 1, 5, "D1")
    wraps(g)
    sandals(g)
    # Trousers bloused over the top of the wraps.
    for side, bone in (("right", "RIGHT_LEG"), ("left", "LEFT_LEG")):
        puff = g.piece(f"{side}_blouse", bone, (-2.5, 4.6, -2.5), (5, 2, 5))
        solid(puff, "D", "twill", 44, 2)
        for face in puff.sides:
            face.hline(0, face.w - 1, 0, "D3")
    # Kunai holster strapped to the right thigh.
    strap = g.piece("holster_strap", "RIGHT_LEG", (-2.45, 1.0, -2.45), (5, 1, 5))
    solid(strap, "L", "leather", 45, 2)
    holster = g.piece("holster", "RIGHT_LEG", (0, 0, 0), (1, 3, 2), pivot=(-3.0, .8, -1.0))
    solid(holster, "K", "leather", 46, 3)
    holster.right.set(0, 0, "M3"), holster.right.set(1, 0, "M2")
    # Tool pouch at the back of the belt.
    pouch = g.piece("waist_pouch", "TORSO", (0, 0, 0), (3, 2, 1), pivot=(-1.5, 9.4, 2.2))
    solid(pouch, "L", "leather", 47, 2)
    pouch.back.hline(0, 2, 0, "L3")
