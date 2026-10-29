"""Tabi Trousers: close charcoal trousers tucked into the clan's soft-soled split-toe boots, padded
knees that kneel without a sound, a holster strapped to the right thigh and a dark sash at the waist."""
from kit import legs, waistband
from kit_tobari import split_toe_boots
from paint import solid

META = {"name": "Tabi Trousers", "gender": "unisex",
        "description": "Close charcoal trousers, padded knees, a thigh holster, soft split-toe boots to the shin.",
        "tags": ["shinobi"]}


def build(g):
    waistband(g, "D", "twill", 25600)
    legs(g, "D", "twill", 25601, rows=(0, 9))
    split_toe_boots(g, top=6, role="K")
    for side, bone in (("right", "RIGHT_LEG"), ("left", "LEFT_LEG")):
        pad = g.piece(f"{side}_knee_pad", bone, (-1.5, 4.0, -2.4), (3, 2, 1))
        solid(pad, "D", "quilt", 25603, 1, edge=False)
        pad.front.hline(0, 2, 0, "D2")
    holster = g.piece("holster", "RIGHT_LEG", (-1, 0, -1), (1, 3, 2), pivot=(-2.4, 1.2, 0))
    solid(holster, "L", "leather", 25604, 2)
    strap = g.piece("holster_strap", "RIGHT_LEG", (-2.45, 1.4, -2.45), (5, 1, 5))
    solid(strap, "L", "leather", 25605, 2, edge=False)
