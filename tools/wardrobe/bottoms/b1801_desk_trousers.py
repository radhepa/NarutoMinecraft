"""Desk Trousers: Iruka's warm navy shinobi trousers bloused into pale shin wraps, a kunai holster on
the right thigh, a small sand pouch at the back of the belt and open-toe sandals."""
from kit_shinobi import sandals, wraps
from paint import fabric, solid, strip_fabric

META = {"name": "Desk Trousers", "gender": "unisex",
        "description": "Navy trousers bloused into shin wraps, a thigh holster, a sand back pouch, sandals.",
        "tags": ["shinobi"]}


def build(g):
    body = g.part("body")
    strip_fabric(body, "D", "twill", 18601, 2, 9, 11)
    body.strip.hline(0, body.strip.w - 1, 9, "D3")
    fabric(body.bottom, "D", "twill", 18601, 1)
    for side in ("right", "left"):
        leg = g.part(f"{side}_leg")
        strip_fabric(leg, "D", "twill", 18602 + (side == "left"), 2, 0, 6)
        fabric(leg.top, "D", "twill", 18602, 2)
        leg.front.vline(1 if side == "right" else 2, 1, 5, "D1")
    wraps(g, 7, 9)
    sandals(g)
    strap = g.piece("holster_strap", "RIGHT_LEG", (-2.45, 1.0, -2.45), (5, 1, 5))
    solid(strap, "K", "leather", 18605, 2)
    holster = g.piece("holster", "RIGHT_LEG", (0, 0, 0), (1, 3, 2), pivot=(-3.0, .8, -1.0))
    solid(holster, "K", "leather", 18606, 3)
    holster.right.set(0, 0, "M3")
    pouch = g.piece("waist_pouch", "TORSO", (0, 0, 0), (4, 2, 1), pivot=(-2.0, 9.4, 2.2))
    solid(pouch, "S", "weave", 18607, 2)
    pouch.back.hline(0, 3, 0, "S3"), pouch.back.set(2, 1, "A2")
