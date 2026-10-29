"""Knee Shorts: loose dark three-quarter shorts over mesh shins, a strap across the right thigh and
open-toe sandals: the young Nara's summer kit."""
from kit import leg_ring
from kit_nara import net
from kit_shinobi import sandals
from paint import fabric, solid, strip_fabric

META = {"name": "Knee Shorts", "gender": "unisex",
        "description": "Loose dark three-quarter shorts over mesh shins, a thigh strap, sandals.",
        "tags": ["shinobi", "genin"]}


def build(g):
    body = g.part("body")
    strip_fabric(body, "K", "twill", 5621, 3, 9, 11)
    body.strip.hline(0, body.strip.w - 1, 9, "K2")
    fabric(body.bottom, "K", "twill", 5621, 2)
    for side in ("right", "left"):
        leg = g.part(f"{side}_leg")
        strip_fabric(leg, "K", "twill", 5622 + (side == "left"), 3, 0, 6)
        fabric(leg.top, "K", "twill", 5622, 3)
        net(leg.strip, 0, 7, leg.strip.w - 1, 9)
    for ring in leg_ring(g, "hem", 6.0, "K", 3, (5, 1, 5), "twill", inflate=.1):
        for face in ring.sides:
            face.hline(0, face.w - 1, 0, "K4")
    sandals(g)
    strap = g.piece("thigh_strap", "RIGHT_LEG", (-2.45, 1.4, -2.45), (5, 1, 5))
    solid(strap, "L", "leather", 5624, 2, edge=False)
