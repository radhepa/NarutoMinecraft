"""Blossom Kimono Skirt: the skirt of a spring visiting kimono, plain at the waist with blossoms
gathering thicker towards a hem banded in the accent, over white tabi and lacquered zori."""
from kit_household import skirt, sprigs, trouser_legs, waist, zori

META = {"name": "Blossom Kimono Skirt", "gender": "unisex",
        "description": "Ankle-length kimono skirt with blossoms thickening to an accent hem band, tabi and zori.",
        "tags": ["civilian", "kimono", "skirt"]}


def build(g):
    waist(g, "P", "velvet", 37692)
    trouser_legs(g, "P", "velvet", 37693, rows=(0, 9), base=1)
    zori(g, strap="A2", sole="K2")
    for face in skirt(g, "kimono", 11, "P", "velvet", 37695, hem="A2"):
        sprigs(face, "A3", "S4", step=4, seed=2, rows=range(5, 10))
        sprigs(face, "S3", "A3", step=5, seed=4, rows=range(2, 5), chance=.6)
        if face.name == "front":
            face.vline(3, 1, 10, "P1")
