"""Wrapped Legs: trousers bound in bandage from the knee to the ankle, crossed by two leather leg
straps, over split-toe socks and straw sandals."""
from kit_field import trousers
from kit_hyuga import tabi
from kit_shinobi import bandage
from paint import solid

META = {"name": "Wrapped Legs", "gender": "unisex",
        "description": "Trousers bandaged from knee to ankle, two leather leg straps, tabi and straw sandals.",
        "tags": ["shinobi"]}


def build(g):
    trousers(g, "D", 32460, length=4)
    for side in ("right", "left"):
        leg = g.part(f"{side}_leg")
        bandage(leg.strip, 0, 5, leg.strip.w - 1, 9)
        leg.strip.hline(0, leg.strip.w - 1, 5, "S4")
    tabi(g)
    for side, bone in (("right", "RIGHT_LEG"), ("left", "LEFT_LEG")):
        for i, y in enumerate((5.6, 8.2)):
            band = g.piece(f"{side}_leg_strap_{i}", bone, (-2.45, y, -2.45), (5, 1, 5))
            solid(band, "L", "leather", 32463 + i, 2, edge=False)
