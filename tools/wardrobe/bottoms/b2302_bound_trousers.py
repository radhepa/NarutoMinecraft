"""Bound Trousers: dark umber trousers, the shins bound tight with ochre threads crossed over pale
wraps, and open-toe sandals: the guardians' patrol wear."""
from kit import legs, waistband
from kit_shinobi import sandals, wraps
from kit_tsuchigumo import threads

META = {"name": "Bound Trousers", "gender": "unisex",
        "description": "Dark umber trousers with thread-bound shins over pale wraps and open-toe sandals.",
        "tags": ["shinobi"]}


def build(g):
    waistband(g, "L", "twill", 23781)
    legs(g, "L", "twill", 23782, rows=(0, 5))
    wraps(g, 6, 9)
    for side in ("right", "left"):
        leg = g.part(f"{side}_leg")
        threads(leg.strip, 0, 6, leg.strip.w - 1, 9, "A1", step=5)
        leg.strip.hline(0, leg.strip.w - 1, 5, "L1")
    sandals(g)
