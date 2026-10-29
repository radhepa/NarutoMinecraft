"""Strap Trousers: loose slate field trousers with black straps round each thigh and shin, bloused
over short heavy boots."""
from kit import leg_ring, legs, waistband
from kit_morino import heavy_boots
from paint import solid

META = {"name": "Strap Trousers", "gender": "unisex",
        "description": "Loose slate trousers strapped at thigh and shin, bloused over short heavy boots.",
        "tags": ["shinobi"]}


def build(g):
    waistband(g, "S", "twill", 17421)
    legs(g, "S", "twill", 17422, rows=(0, 8))
    heavy_boots(g, top=8, seed=17424)
    for ring in leg_ring(g, "blouse", 6.8, "S", 2, size=(5, 2, 5)):
        for face in ring.sides:
            face.hline(0, face.w - 1, 0, "S3")
    for name, y in (("thigh_strap", 1.4), ("shin_strap", 5.2)):
        for ring in leg_ring(g, name, y, "K", 2, size=(5, 1, 5), texture="leather", inflate=.05):
            ring.front.set(2, 0, "M3")
    pouch = g.piece("waist_pouch", "TORSO", (0, 0, 0), (4, 2, 1), pivot=(-2.0, 9.4, 2.2))
    solid(pouch, "K", "leather", 17427, 2)
