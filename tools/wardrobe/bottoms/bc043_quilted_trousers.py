"""Quilted Trousers: the winter house trousers of the old and the cold, cotton padding stitched in
diamonds, gathered at the ankle over thick white tabi and zori."""
from kit_household import trouser_legs, waist, zori
from paint import solid

META = {"name": "Quilted Trousers", "gender": "unisex",
        "description": "Diamond-quilted padded winter trousers gathered at the ankle, white tabi and zori.",
        "tags": ["civilian", "trousers"]}


def build(g):
    waist(g, "D", "quilt", 37772, band="D1")
    trouser_legs(g, "D", "quilt", 37773, rows=(0, 9))
    zori(g, strap="A2")
    for side, bone in (("right", "RIGHT_LEG"), ("left", "LEFT_LEG")):
        pad = g.piece(f"{side}_padding", bone, (-2.5, .2, -2.5), (5, 8, 5), inflate=.1)
        solid(pad, "D", "quilt", 37775 + (side == "left"), 2)
        gather = g.piece(f"{side}_gather", bone, (-2.5, 8.6, -2.5), (5, 1, 5))
        solid(gather, "D", "rib", 37777, 1, edge=False)
