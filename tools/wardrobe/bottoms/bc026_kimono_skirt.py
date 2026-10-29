"""Kimono Skirt: the lower half of an everyday kimono, falling straight to the ankle with the
over-panel's edge running down the front, a pale lining showing at the hem, white tabi and zori.
Worn under any tucked kimono top, it reads as the full garment."""
from kit_household import skirt, trouser_legs, waist, zori

META = {"name": "Kimono Skirt", "gender": "unisex",
        "description": "Straight ankle-length kimono skirt with the overlap at the front, pale hem lining, tabi and zori.",
        "tags": ["civilian", "kimono", "skirt"]}


def build(g):
    waist(g, "P", "weave", 37500)
    trouser_legs(g, "P", "weave", 37501, rows=(0, 9), base=1)
    zori(g, strap="A2")
    for face in skirt(g, "kimono", 11, "P", "weave", 37503, hem="S3"):
        if face.name == "front":
            face.vline(3, 1, 10, "P3"), face.vline(2, 1, 10, "P1")
