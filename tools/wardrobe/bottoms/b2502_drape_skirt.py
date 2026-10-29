"""Drape Skirt: two tiers of pleated panels hung front and back over dark leggings, the upper tier
short and the lower to the knee, grey shin wraps and the clan's split-toe boots."""
from kit import flaps, legs, waistband
from kit_tobari import pleats, shin_wraps, split_toe_boots

META = {"name": "Drape Skirt", "gender": "unisex",
        "description": "Two tiers of pleated panels over dark leggings, grey shin wraps, split-toe boots.",
        "tags": ["shinobi", "skirt"]}


def build(g):
    waistband(g, "K", "twill", 25630)
    legs(g, "K", "plain", 25631, rows=(0, 9), crease=False)
    shin_wraps(g, 4, 6)
    split_toe_boots(g, top=7, role="K", tie=None)
    for face in flaps(g, "lower", 7, "P", "twill", 25633, top=10.6, slit=True):
        pleats(face, "P", step=2)
    for face in flaps(g, "upper", 3, "P", "twill", 25635, top=10.2, width=10, front_z=-3.05, back_z=2.05):
        pleats(face, "P", base=2, step=3)
