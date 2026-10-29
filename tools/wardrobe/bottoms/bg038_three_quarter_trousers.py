"""Three-Quarter Trousers: trousers cut off at mid-calf with darker patched knees and an accent stripe
down the outer seam, shin wraps below and open-toe sandals."""
from kit_field import trousers
from kit_shinobi import sandals, wraps
from paint import k

META = {"name": "Three-Quarter Trousers", "gender": "unisex",
        "description": "Mid-calf trousers with patched knees and an accent side stripe over shin wraps, sandals.",
        "tags": ["shinobi"]}


def build(g):
    trousers(g, "D", 32740, length=7)
    for side in ("right", "left"):
        leg = g.part(f"{side}_leg")
        leg.front.rect(0, 4, 4, 2, k("D", 1)), leg.front.hline(0, 3, 4, k("D", 0))
        outer = leg.right if side == "right" else leg.left
        outer.vline(1, 0, 7, k("A", 2))
        leg.strip.hline(0, leg.strip.w - 1, 7, k("D", 1))
    wraps(g, 8, 9)
    sandals(g)
