"""Crag Shorts: plum knee shorts with a rolled ochre hem and a web-line seam down the outside of the
leg, pale shin wraps and sandals for climbing the mountain paths."""
from kit import legs, waistband
from kit_shinobi import sandals, wraps
from paint import k

META = {"name": "Crag Shorts", "gender": "unisex",
        "description": "Plum knee shorts with a rolled ochre hem, pale shin wraps and sandals.", "tags": ["shinobi"]}


def build(g):
    waistband(g, "P", "twill", 23811)
    legs(g, "P", "twill", 23812, rows=(0, 4))
    for side in ("right", "left"):
        leg = g.part(f"{side}_leg")
        leg.strip.hline(0, leg.strip.w - 1, 4, "A2"), leg.strip.hline(0, leg.strip.w - 1, 3, "A3")
        outer = leg.right if side == "right" else leg.left
        for y in range(0, 3):
            outer.set(1 + (y % 2), y, k("P", 1))
    wraps(g, 5, 9)
    sandals(g)
