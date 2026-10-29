"""Rolled Slacks: loose sand slacks rolled to mid-shin for wading the sea field, a navy cloth belt
knotted at the side and open-toe sandals."""
from kit import leg_ring
from kit_shinobi import sandals
from paint import fabric, solid, strip_fabric

META = {"name": "Rolled Slacks", "gender": "unisex",
        "description": "Loose sand slacks rolled to mid-shin, a navy cloth belt knotted at the side, sandals.",
        "tags": ["shinobi"]}


def build(g):
    body = g.part("body")
    strip_fabric(body, "S", "twill", 18681, 2, 9, 11)
    body.strip.hline(0, body.strip.w - 1, 9, "D2"), body.strip.hline(0, body.strip.w - 1, 10, "D1")
    fabric(body.bottom, "S", "twill", 18681, 1)
    for side in ("right", "left"):
        leg = g.part(f"{side}_leg")
        strip_fabric(leg, "S", "twill", 18682 + (side == "left"), 2, 0, 7)
        fabric(leg.top, "S", "twill", 18682, 2)
        leg.front.vline(1 if side == "right" else 2, 1, 6, "S1")
    for ring in leg_ring(g, "roll", 6.0, "S", 3, (5, 2, 5), "twill", inflate=.1):
        for face in ring.sides:
            face.hline(0, face.w - 1, 1, "S1")
    sandals(g)
    knot = g.piece("belt_knot", "TORSO", (-1, 0, -.5), (2, 3, 1), pivot=(3.0, 9.4, -2.7), rotation=(0, 0, -10))
    solid(knot, "D", "weave", 18684, 2)
