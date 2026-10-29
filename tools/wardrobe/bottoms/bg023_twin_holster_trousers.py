"""Twin-Holster Trousers: dark trousers with a holster strapped to each thigh, bloused into shin wraps,
and a flat pouch at the back of the belt: the kunai specialist's pair."""
from kit_field import blouse, holster, pocket, trousers
from kit_shinobi import sandals, wraps

META = {"name": "Twin-Holster Trousers", "gender": "unisex",
        "description": "Dark bloused trousers with a holster on each thigh, shin wraps and a back belt pouch.",
        "tags": ["shinobi"]}


def build(g):
    trousers(g, "K", 32440)
    wraps(g)
    sandals(g)
    blouse(g, "K", 32443)
    holster(g, "right", 32445)
    holster(g, "left", 32449)
    pocket(g, "waist_pouch", (0, 9.4, 2.3), (4, 3, 2), "L", 32453, rotation=(0, 180, 0), scale=.75)
