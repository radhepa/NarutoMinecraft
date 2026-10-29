"""Cropped Linen Trousers: loose summer trousers of crumpled linen cut off above the ankle, a tie
waist, worn barefoot in wooden geta."""
from kit_household import geta, trouser_legs, waist
from paint import solid

META = {"name": "Cropped Linen Trousers", "gender": "unisex",
        "description": "Loose crumpled-linen trousers cropped above the ankle, tie waist, wooden geta.",
        "tags": ["civilian", "casual", "trousers"]}


def build(g):
    body = waist(g, "S", "tweed", 37708, base=2, band="S1")
    body.front.set(2, 10, "S1"), body.front.set(5, 10, "S1")
    trouser_legs(g, "S", "tweed", 37709, rows=(0, 7))
    geta(g, strap="D2")
    for side, bone in (("right", "RIGHT_LEG"), ("left", "LEFT_LEG")):
        hem = g.piece(f"{side}_hem", bone, (-2.5, 6.4, -2.5), (5, 2, 5), inflate=.06)
        solid(hem, "S", "tweed", 37711 + (side == "left"), 2)
        for face in hem.sides:
            face.hline(0, face.w - 1, 1, "S1")
