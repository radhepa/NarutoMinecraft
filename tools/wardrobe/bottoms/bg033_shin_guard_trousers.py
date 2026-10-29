"""Shin-Guard Trousers: field trousers bloused at the knee over long steel shin guards strapped from
knee to ankle, a holster on the right thigh and open-toe sandals."""
from kit_field import blouse, holster, trousers
from kit_shinobi import sandals, wraps
from paint import k, solid

META = {"name": "Shin-Guard Trousers", "gender": "unisex",
        "description": "Trousers bloused at the knee over long steel shin guards, a thigh holster and sandals.",
        "tags": ["shinobi"]}


def build(g):
    trousers(g, "D", 32640, length=4)
    wraps(g, 5, 9)
    sandals(g)
    blouse(g, "D", 32643, y=3.6)
    holster(g, "right", 32645)
    for side, bone in (("right", "RIGHT_LEG"), ("left", "LEFT_LEG")):
        guard = g.piece(f"{side}_shin_guard", bone, (-1.5, 0, -1), (3, 5, 1), pivot=(0, 5.6, -2.3))
        solid(guard, "M", "plain", 32649 + (side == "left"), 2)
        guard.front.hline(0, 2, 0, k("M", 4)), guard.front.vline(1, 1, 4, k("M", 3))
        for y in (6.2, 9.0):
            band = g.piece(f"{side}_guard_strap_{int(y)}", bone, (-2.45, y, -2.45), (5, 1, 5))
            solid(band, "K", "leather", 32651, 2, edge=False)
