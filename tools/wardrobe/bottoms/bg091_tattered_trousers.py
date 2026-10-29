"""Tattered Trousers: old trousers worn through at the knee and frayed off above the ankle, a patch
on one thigh, bare ankles and straw sandals, a rope belt: a long way from home and not minding."""
from kit import legs, waistband
from kit_rugged import patch, ragged, straw_sandals

META = {"name": "Tattered Trousers", "gender": "unisex",
        "description": "Trousers frayed off above the ankle, worn through at the knee, a thigh patch, rope belt, sandals.",
        "tags": ["shinobi", "genin"]}


def build(g):
    body = waistband(g, "P", "twill", 35410, 2)
    body.strip.hline(0, body.strip.w - 1, 9, "L2")
    for leg in legs(g, "P", "twill", 35411, 2, rows=(0, 8), crease=False):
        leg.strip.hline(0, leg.strip.w - 1, 7, "P1")
        for face in leg.sides:
            ragged(face, 8, 35412 + face.x0, .5)
    for side in ("right", "left"):
        knee = g.part(f"{side}_leg").front
        knee.set(1, 4, None), knee.set(2, 4, None), knee.set(2, 5, None)
        knee.set(1, 3, "P0"), knee.set(3, 4, "P0")
    patch(g.part("left_leg").front, 0, 0, 3, 3, "S", 35415, 1)
    straw_sandals(g)
