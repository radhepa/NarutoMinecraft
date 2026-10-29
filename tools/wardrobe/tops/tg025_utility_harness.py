"""Utility Harness: a long-sleeved field shirt under a leather harness, two straps over the shoulders
joined by a chest band, pouches clipped on at the chest and a belt with a buckle: no vest at all."""
from kit import belt
from kit_field import pocket, shirt, strap
from paint import solid

META = {
    "name": "Utility Harness",
    "gender": "unisex",
    "description": "Long-sleeved shirt under a leather shoulder harness with a chest band, clip pouches and a belt.",
    "tags": ["shinobi", "chunin"],
}


def build(g):
    shirt(g, "P", 32080, texture="twill")
    for i, x in enumerate((-2.3, 2.3)):
        strap(g, f"front_strap_{i}", (x, 4.6, -2.65), length=9, seed=32084 + i)
        strap(g, f"back_strap_{i}", (x, 4.6, 2.65), length=9, seed=32086 + i)
        over = g.piece(f"shoulder_strap_{i}", "TORSO", (-.5, -.5, -2.6), (1, 1, 5), pivot=(x, -.3, 0), inflate=.06)
        solid(over, "L", "leather", 32088 + i, 2, edge=False)
    band = g.piece("chest_band", "TORSO", (-4.5, 0, -2.5), (9, 1, 5), pivot=(0, 3.4, 0), inflate=.2)
    solid(band, "L", "leather", 32090, 2, edge=False)
    band.front.set(4, 0, "M3")
    pocket(g, "chest_pouch_0", (-2.3, 4.4, -2.9), (3, 4, 2), "L", 32091, snap="M3")
    pocket(g, "chest_pouch_1", (2.3, 4.4, -2.9), (3, 3, 2), "L", 32092, snap="M3")
    belt(g, "belt", y=9.6)
