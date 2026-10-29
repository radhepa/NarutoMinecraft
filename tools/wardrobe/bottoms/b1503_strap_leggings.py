"""Strap Leggings: close dark leggings for footwork, leather straps crossed down each shin like a
sword's cord, a holster on the right thigh and open-toe sandals."""
from kit import SIDES
from kit_shinobi import sandals
from paint import fabric, solid, strip_fabric

META = {"name": "Strap Leggings", "gender": "unisex",
        "description": "Close dark leggings, leather straps crossed down each shin, thigh holster, sandals.",
        "tags": ["shinobi"]}


def build(g):
    body = g.part("body")
    strip_fabric(body, "K", "smooth", 15530, 3, 9, 11)
    body.strip.hline(0, body.strip.w - 1, 9, "K4")
    fabric(body.bottom, "K", "smooth", 15530, 2)
    for side in SIDES:
        leg = g.part(f"{side}_leg")
        strip_fabric(leg, "K", "smooth", 15531 + (side == "left"), 3, 0, 9)
        fabric(leg.top, "K", "smooth", 15531, 3)
        # Cross-gartered straps: three turns round the shin, crossed in an X on the front.
        for y in (5, 7, 9):
            leg.strip.hline(0, leg.strip.w - 1, y, "L2")
        for y, (a, b) in zip((6, 8), ((1, 2), (1, 2))):
            leg.front.set(a, y, "L3"), leg.front.set(b, y, "L3")
    sandals(g)
    strap = g.piece("holster_strap", "RIGHT_LEG", (-2.45, 1.0, -2.45), (5, 1, 5))
    solid(strap, "L", "leather", 15535, 2)
    holster = g.piece("holster", "RIGHT_LEG", (0, 0, 0), (1, 3, 2), pivot=(-3.0, .8, -1.0))
    solid(holster, "L", "leather", 15536, 1)
    holster.right.set(0, 0, "M3"), holster.right.set(1, 0, "M2")
