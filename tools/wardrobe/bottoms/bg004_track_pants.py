"""Track Pants: full-length track pants with two stripes down each leg, a drawstring waist and elastic
ankle cuffs over low canvas shoes: the matching half of a tracksuit, or not."""
from kit import footwear
from kit_academy import leg_cloth, side_stripe, waist

META = {"name": "Track Pants", "gender": "unisex",
        "description": "Full-length track pants, two stripes down each leg, elastic cuffs and canvas shoes.",
        "tags": ["shinobi", "genin"]}


def build(g):
    body = waist(g, "D", "plain", 31445)
    body.front.set(3, 10, "S3"), body.front.set(4, 10, "S3"), body.front.set(4, 11, "S2")
    for side, leg in zip(("right", "left"), leg_cloth(g, "D", "plain", 31446, (0, 9))):
        side_stripe(leg, side, (0, 8), "S3", double="S2")
        leg.strip.hline(0, leg.strip.w - 1, 8, "D3")
        leg.strip.hline(0, leg.strip.w - 1, 9, "D1")
        leg.front.vline(1 if side == "right" else 2, 2, 7, "D1")
    footwear(g, "shoe", 10, "K", 2, toe="S3", sole="S2")
