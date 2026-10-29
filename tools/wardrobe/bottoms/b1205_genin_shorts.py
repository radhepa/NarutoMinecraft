"""Kurama Genin Shorts: dark knee shorts with an accent stripe down the outer seam, white shin wraps,
a holster on the right thigh and open-toe sandals: plain enough to run in."""
from kit_shinobi import sandals, wraps
from paint import fabric, solid, strip_fabric

META = {"name": "Kurama Genin Shorts", "gender": "unisex",
        "description": "Dark knee shorts with an accent side stripe, white shin wraps, thigh holster, sandals.",
        "tags": ["shinobi", "genin"]}


def build(g):
    body = g.part("body")
    strip_fabric(body, "D", "twill", 12930, 2, 9, 11)
    body.strip.hline(0, body.strip.w - 1, 9, "D1")
    fabric(body.bottom, "D", "twill", 12930, 1)
    for side in ("right", "left"):
        leg = g.part(f"{side}_leg")
        strip_fabric(leg, "D", "twill", 12931 + (side == "left"), 2, 0, 4)
        fabric(leg.top, "D", "twill", 12931, 2)
        leg.strip.hline(0, leg.strip.w - 1, 4, "D1")
        outer = leg.right if side == "right" else leg.left
        outer.vline(1, 0, 4, "A2"), outer.vline(2, 0, 4, "A2")
    wraps(g, top=6, bottom=9)
    sandals(g)
    strap = g.piece("holster_strap", "RIGHT_LEG", (-2.45, 1.0, -2.45), (5, 1, 5))
    solid(strap, "L", "leather", 12933, 2)
    holster = g.piece("holster", "RIGHT_LEG", (0, 0, 0), (1, 3, 2), pivot=(-3.0, .8, -1.0))
    solid(holster, "K", "leather", 12934, 3)
    holster.right.set(0, 0, "M3"), holster.right.set(1, 0, "M2")
