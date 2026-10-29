"""Tiered Skirt: a long summer skirt gathered in two flounced tiers, a seam of light at each tier,
worn with thong sandals to the festival grounds and the riverbank."""
from kit_household import skirt, trouser_legs, waist, zori

META = {"name": "Tiered Skirt", "gender": "female",
        "description": "Long summer skirt in two gathered tiers, thong sandals.",
        "tags": ["civilian", "skirt"]}


def gathers(face, rows=None):
    for y in rows or range(face.h):
        for x in range(0, face.w, 3):
            face.set(x, y, "P1")


def build(g):
    waist(g, "P", "plain", 37852, band="P1")
    trouser_legs(g, "P", "plain", 37853, rows=(0, 9), base=1)
    zori(g, sock="L3", strap="A2", sole="L2")
    for face in skirt(g, "skirt", 11, "P", "plain", 37855, hem="P1", base=2, pattern=gathers):
        face.hline(0, face.w - 1, 5, "P3"), face.hline(0, face.w - 1, 6, "P1")
