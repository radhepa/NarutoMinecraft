"""Corduroy Trousers: autumn trousers in wale corduroy, straight legged with a turned cuff and
leather shoes, for teachers, clerks and the walk to the archive."""
from kit_household import trouser_legs, waist
from kit import footwear
from paint import solid

META = {"name": "Corduroy Trousers", "gender": "unisex",
        "description": "Straight wale-corduroy trousers with a turned cuff, leather shoes.",
        "tags": ["civilian", "casual", "trousers"]}


def build(g):
    waist(g, "D", "rib", 37756, band="L2")
    g.part("body").front.set(4, 9, "M3")
    trouser_legs(g, "D", "rib", 37757, rows=(0, 9))
    footwear(g, "shoe", top=10, role="L", base=2)
    for side, bone in (("right", "RIGHT_LEG"), ("left", "LEFT_LEG")):
        cuff = g.piece(f"{side}_cuff", bone, (-2.5, 8.6, -2.5), (5, 1, 5))
        solid(cuff, "D", "rib", 37759, 3, edge=False)
