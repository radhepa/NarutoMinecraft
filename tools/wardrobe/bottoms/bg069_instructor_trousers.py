"""Instructor Trousers: everyday shinobi trousers with a kunai holster on the left thigh (the
teacher demonstrates with the right hand), short shin wraps and sandals."""
from kit_shinobi import sandals, wraps
from paint import fabric, solid, strip_fabric

META = {"name": "Instructor Trousers", "gender": "unisex",
        "description": "Shinobi trousers with a left-thigh holster, short shin wraps and sandals.",
        "tags": ["shinobi"]}


def build(g):
    body = g.part("body")
    strip_fabric(body, "D", "twill", 34560, 2, 9, 11)
    body.strip.hline(0, body.strip.w - 1, 9, "D1")
    fabric(body.bottom, "D", "twill", 34560, 1)
    for side, bone in (("right", "RIGHT_LEG"), ("left", "LEFT_LEG")):
        leg = g.part(f"{side}_leg")
        strip_fabric(leg, "D", "twill", 34561 + (side == "left"), 2, 0, 6)
        fabric(leg.top, "D", "twill", 34561, 2)
        puff = g.piece(f"{side}_blouse", bone, (-2.5, 5.6, -2.5), (5, 2, 5))
        solid(puff, "D", "twill", 34563, 2)
        for face in puff.sides:
            face.hline(0, face.w - 1, 0, "D3")
    wraps(g, 7, 9)
    sandals(g)
    strap = g.piece("holster_strap", "LEFT_LEG", (-2.45, 1.0, -2.45), (5, 1, 5))
    solid(strap, "L", "leather", 34564, 2)
    holster = g.piece("holster", "LEFT_LEG", (0, 0, 0), (1, 3, 2), pivot=(2.0, .8, -1.0))
    solid(holster, "K", "leather", 34565, 3)
    holster.left.set(0, 0, "M3"), holster.left.set(1, 0, "M2")
