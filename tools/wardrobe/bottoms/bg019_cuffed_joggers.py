"""Cuffed Joggers: soft tapered joggers with deep ribbed ankle cuffs, a drawstring waist and high-top
canvas shoes: what the Academy wears for the long run round the village wall."""
from kit import footwear
from kit_academy import leg_cloth, ribbed, waist

META = {"name": "Cuffed Joggers", "gender": "unisex",
        "description": "Tapered joggers with ribbed ankle cuffs, a drawstring waist and high-top canvas shoes.",
        "tags": ["shinobi", "genin"]}


def build(g):
    body = waist(g, "K", "knit", 31670)
    body.front.set(3, 10, "S3"), body.front.set(4, 10, "S3")
    for side, leg in zip(("right", "left"), leg_cloth(g, "K", "knit", 31671, (0, 8))):
        ribbed(leg, (7, 8), "K", base=3)
        leg.front.vline(1 if side == "right" else 2, 2, 6, "K3")
    footwear(g, "shoe", 9, "S", 3, toe="S4", sole="K1")
    for side in ("right", "left"):
        pants = g.part(f"{side}_pants")
        for face in (pants.right, pants.left):
            face.hline(0, face.w - 1, 10, "A2")
