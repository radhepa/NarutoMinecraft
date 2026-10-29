"""Armory Trousers: heavy twill trousers with padded knees, a short blade sheathed on the right
thigh, shin wraps and sandals: the weapons master's working kit."""
from kit_shinobi import sandals, tanto, wraps
from paint import fabric, solid, strip_fabric

META = {"name": "Armory Trousers", "gender": "unisex",
        "description": "Heavy trousers with padded knees, a short blade on the right thigh, shin wraps, sandals.",
        "tags": ["shinobi"]}


def build(g):
    body = g.part("body")
    strip_fabric(body, "D", "twill", 34660, 2, 9, 11)
    body.strip.hline(0, body.strip.w - 1, 9, "D1")
    fabric(body.bottom, "D", "twill", 34660, 1)
    for side, bone in (("right", "RIGHT_LEG"), ("left", "LEFT_LEG")):
        leg = g.part(f"{side}_leg")
        strip_fabric(leg, "D", "twill", 34661 + (side == "left"), 2, 0, 6)
        fabric(leg.top, "D", "twill", 34661, 2)
        pad = g.piece(f"{side}_knee_pad", bone, (-1.5, 3.4, -2.8), (3, 3, 1))
        solid(pad, "L", "leather", 34663, 2)
        pad.front.hline(0, 2, 0, "L3"), pad.front.set(1, 1, "M3")
    wraps(g, 7, 9)
    sandals(g)
    strap = g.piece("thigh_strap", "RIGHT_LEG", (-2.45, 1.6, -2.45), (5, 1, 5))
    solid(strap, "L", "leather", 34665, 2, edge=False)
    tanto(g, "thigh_blade", pivot=(-2.9, 1.0, 0), rotation=(-14, 0, 0), bone="RIGHT_LEG", length=5)
