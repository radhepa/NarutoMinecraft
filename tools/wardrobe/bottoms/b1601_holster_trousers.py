"""Holster Trousers: dusky field trousers bloused into pale shin wraps, a leather holster on the
right thigh with senbon points standing out of it, open-toe sandals."""
from kit_shinobi import sandals, wraps
from kit_shiranui import thigh_holster
from paint import fabric, solid, strip_fabric

META = {"name": "Holster Trousers", "gender": "unisex",
        "description": "Dusky trousers bloused into shin wraps, a senbon holster on the right thigh, sandals.",
        "tags": ["shinobi"]}


def build(g):
    body = g.part("body")
    strip_fabric(body, "D", "twill", 16860, 2, 9, 11)
    body.strip.hline(0, body.strip.w - 1, 9, "D1")
    fabric(body.bottom, "D", "twill", 16860, 1)
    for side in ("right", "left"):
        leg = g.part(f"{side}_leg")
        strip_fabric(leg, "D", "twill", 16861 + (side == "left"), 2, 0, 6)
        fabric(leg.top, "D", "twill", 16861, 2)
        leg.front.vline(1 if side == "right" else 2, 1, 5, "D1")
    wraps(g, 7, 9)
    sandals(g)
    for side, bone in (("right", "RIGHT_LEG"), ("left", "LEFT_LEG")):
        puff = g.piece(f"{side}_blouse", bone, (-2.5, 5.4, -2.5), (5, 2, 5))
        solid(puff, "D", "twill", 16863, 2)
        for face in puff.sides:
            face.hline(0, face.w - 1, 0, "D3")
    thigh_holster(g, "right", seed=16864)
