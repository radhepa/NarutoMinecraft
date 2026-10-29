"""Wrapped Trousers: dark loose shinobi trousers gathered below the knee by bandage wraps that bind
the shins down to navy open-toe sandals, a thin thorn stem stitched down the outer seam."""
from kit import legs, waistband
from kit_shinobi import sandals
from kit_yuhi import bandage_turns, thorn_vine

META = {"name": "Wrapped Trousers", "gender": "unisex",
        "description": "Dark trousers, shins bound in bandage wraps, thorn stem down the outer seam, navy sandals.",
        "tags": ["shinobi", "wrap"]}


def build(g):
    waistband(g, "D", "twill", 14910)
    for leg in legs(g, "D", "twill", 14911, rows=(0, 9)):
        bandage_turns(leg.strip, 0, 6, leg.strip.w - 1, 9, "S", 3)
    thorn_vine(g.part("right_leg").right, 1, 0, 5, "A")
    thorn_vine(g.part("left_leg").left, 1, 0, 5, "A")
    sandals(g)
