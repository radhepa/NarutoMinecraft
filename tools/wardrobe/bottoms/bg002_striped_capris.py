"""Striped Capris: three-quarter trousers ending at mid-shin, a contrast stripe down the outer seam
and a banded cuff, with open-toe sandals: the genin who outgrew last year's pair."""
from kit_academy import leg_cloth, side_stripe, waist
from kit_shinobi import sandals

META = {"name": "Striped Capris", "gender": "unisex",
        "description": "Mid-shin trousers with a contrast side stripe, banded cuffs and open-toe sandals.",
        "tags": ["shinobi", "genin"]}


def build(g):
    body = waist(g, "K", "twill", 31415, band="K3")
    body.front.set(3, 10, "S3"), body.front.set(4, 10, "S3")
    for side, leg in zip(("right", "left"), leg_cloth(g, "K", "twill", 31416, (0, 8))):
        side_stripe(leg, side, (0, 7), "S3")
        leg.strip.hline(0, leg.strip.w - 1, 8, "A2")
        leg.strip.hline(0, leg.strip.w - 1, 7, "K1")
        leg.front.vline(1 if side == "right" else 2, 1, 6, "K3")
    sandals(g)
