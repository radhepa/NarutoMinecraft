"""Strapped Leggings: snug knit leggings crossed by leather straps at the thigh and calf, a padded leather shin
guard on each leg and open-toe sandals: light enough for a long run."""
from kit_field import trousers
from kit_shinobi import sandals
from paint import k, solid

META = {"name": "Strapped Leggings", "gender": "unisex",
        "description": "Snug knit leggings with thigh and calf straps, leather shin guards and sandals.",
        "tags": ["shinobi"]}


def build(g):
    trousers(g, "D", 32620, texture="knit", length=9)
    sandals(g)
    for side, bone in (("right", "RIGHT_LEG"), ("left", "LEFT_LEG")):
        for i, y in enumerate((1.6, 3.0, 8.4)):
            band = g.piece(f"{side}_strap_{i}", bone, (-2.3, y, -2.3), (5, 1, 5), scale=(.96, 1, .96))
            solid(band, "L", "leather", 32623 + i, 2, edge=False)
        guard = g.piece(f"{side}_shin_guard", bone, (-1.5, 0, -1), (3, 4, 1), pivot=(0, 5.0, -2.2))
        solid(guard, "L", "leather", 32627 + (side == "right"), 2)
        guard.front.hline(0, 2, 0, k("L", 3)), guard.front.vline(1, 1, 3, k("L", 1)), guard.front.set(1, 0, "M3")
