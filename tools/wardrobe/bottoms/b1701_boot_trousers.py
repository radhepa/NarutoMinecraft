"""Boot Trousers: straight dark slate trousers tucked into tall heavy black boots with two buckled
straps, a kunai holster strapped to the right thigh."""
from kit import legs, waistband
from kit_morino import heavy_boots
from paint import solid

META = {"name": "Boot Trousers", "gender": "unisex",
        "description": "Dark slate trousers tucked into tall buckled black boots, a thigh holster.",
        "tags": ["shinobi"]}


def build(g):
    waistband(g, "D", "twill", 17401)
    legs(g, "D", "twill", 17402, rows=(0, 6))
    heavy_boots(g, top=6, seed=17404)
    strap = g.piece("holster_strap", "RIGHT_LEG", (-2.45, 1.0, -2.45), (5, 1, 5))
    solid(strap, "K", "leather", 17406, 2)
    holster = g.piece("holster", "RIGHT_LEG", (0, 0, 0), (1, 3, 2), pivot=(-3.0, .8, -1.0))
    solid(holster, "K", "leather", 17407, 3)
    holster.right.set(0, 0, "M3")
