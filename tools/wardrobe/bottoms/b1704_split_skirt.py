"""Split Skirt: a long dark slate skirt to mid-calf, split high at both sides for the stride, over
black leggings and tall heavy boots."""
from kit import flaps, waistband
from kit_morino import heavy_boots
from paint import fabric, strip_fabric

META = {"name": "Split Skirt", "gender": "female",
        "description": "Long dark slate skirt split high at the sides over black leggings and tall heavy boots.",
        "tags": ["shinobi", "skirt"]}


def build(g):
    waistband(g, "D", "weave", 17431)
    for side in ("right", "left"):
        leg = g.part(f"{side}_leg")
        strip_fabric(leg, "K", "smooth", 17432 + (side == "left"), 2, 0, 5)
        fabric(leg.top, "K", "smooth", 17432, 2)
    heavy_boots(g, top=5, seed=17434)
    front, back = flaps(g, "skirt", 9, "D", "weave", 17436, hem="A1", top=11.2)
    front.vline(0, 1, 8, "D1"), front.vline(8, 1, 8, "D1")
