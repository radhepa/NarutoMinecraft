"""Aburame Trousers: Shino's dusty brown trousers, loose to the shin and bound there with pale
wraps over open-toe sandals."""
from kit import legs, waistband
from kit_shinobi import sandals, wraps

META = {"name": "Aburame Trousers", "gender": "unisex",
        "description": "Loose dusty brown trousers bound at the shin with pale wraps, open-toe sandals.",
        "tags": ["shinobi"]}


def build(g):
    waistband(g, "D", "twill", 10801)
    legs(g, "D", "twill", 10802, rows=(0, 9))
    for side in ("right", "left"):
        leg, pants = g.part(f"{side}_leg"), g.part(f"{side}_pants")
        for face in pants.sides:   # the loose cloth bagging just above the wraps
            face.hline(0, face.w - 1, 5, "D3"), face.hline(0, face.w - 1, 6, "D1")
        leg.front.vline(1 if side == "right" else 2, 1, 5, "D1")
    wraps(g, 7, 9)
    sandals(g)
