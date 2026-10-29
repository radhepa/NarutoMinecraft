"""Kneepad Pants: full-length work trousers with padded guards strapped over the knees and short
canvas boots: the genin assigned every crawl through the undergrowth."""
from kit import footwear
from kit_academy import leg_cloth, waist, waist_pouch
from paint import solid

META = {"name": "Kneepad Pants", "gender": "unisex",
        "description": "Full-length trousers with padded knee guards and short canvas boots.",
        "tags": ["shinobi", "genin"]}


def build(g):
    waist(g, "D", "twill", 31625)
    for side, leg in zip(("right", "left"), leg_cloth(g, "D", "twill", 31626, (0, 9))):
        leg.front.vline(1 if side == "right" else 2, 1, 8, "D3")
    footwear(g, "boot", 8, "L", 2, sole="K1")
    for side, bone in (("right", "RIGHT_LEG"), ("left", "LEFT_LEG")):
        pad = g.piece(f"{side}_kneepad", bone, (-1.5, 0, 0), (3, 3, 1), pivot=(0, 4.0, -2.9))
        solid(pad, "K", "quilt", 31628, 2)
        pad.front.hline(0, 2, 0, "K3"), pad.front.set(1, 1, "K3")
        strap = g.piece(f"{side}_kneepad_strap", bone, (-2.4, 4.8, -2.4), (5, 1, 5), scale=(.98, 1, .98))
        solid(strap, "K", "plain", 31629, 1, edge=False)
    waist_pouch(g, 31630)
