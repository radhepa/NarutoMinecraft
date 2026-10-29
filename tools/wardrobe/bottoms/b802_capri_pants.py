"""Capri Pants: the young tracker's dark three-quarter trousers ending at mid-calf, bare ankles and
open-toe sandals, a holster strapped to the right thigh and a red cord at the waist."""
from kit_shinobi import sandals
from paint import fabric, solid, strip_fabric

META = {"name": "Capri Pants", "gender": "unisex",
        "description": "Dark three-quarter trousers to mid-calf, bare ankles, sandals, a thigh holster.",
        "tags": ["shinobi"]}


def build(g):
    body = g.part("body")
    strip_fabric(body, "D", "twill", 8780, 2, 9, 11)
    body.strip.hline(0, body.strip.w - 1, 9, "A2")
    fabric(body.bottom, "D", "twill", 8780, 1)
    for side in ("right", "left"):
        leg = g.part(f"{side}_leg")
        strip_fabric(leg, "D", "twill", 8781 + (side == "left"), 2, 0, 7)
        fabric(leg.top, "D", "twill", 8781, 2)
        leg.strip.hline(0, leg.strip.w - 1, 7, "D1")
        leg.front.vline(1 if side == "right" else 2, 1, 6, "D3")
    sandals(g)
    for side, bone in (("right", "RIGHT_LEG"), ("left", "LEFT_LEG")):
        hem = g.piece(f"{side}_hem", bone, (-2.3, 6.6, -2.3), (4, 1, 4), inflate=.2)
        solid(hem, "D", "twill", 8783, 2)
    strap = g.piece("holster_strap", "RIGHT_LEG", (-2.45, 1.0, -2.45), (5, 1, 5))
    solid(strap, "K", "leather", 8784, 2)
    holster = g.piece("holster", "RIGHT_LEG", (0, 0, 0), (1, 3, 2), pivot=(-3.0, .8, -1.0))
    solid(holster, "K", "leather", 8785, 3)
    holster.right.set(0, 0, "M3"), holster.right.set(1, 0, "M2")
