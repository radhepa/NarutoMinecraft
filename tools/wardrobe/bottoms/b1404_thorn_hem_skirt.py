"""Thorn Hem Skirt: a long wrapped skirt to the shins, its hem bordered with a row of crimson thorns
and split at the front so it moves, over navy open-toe sandals."""
from kit import flaps, legs, waistband
from kit_shinobi import sandals
from kit_yuhi import thorn_band

META = {"name": "Thorn Hem Skirt", "gender": "female",
        "description": "Long wrap skirt to the shins with a thorn border, split at the front, navy sandals.",
        "tags": ["shinobi", "skirt", "wrap"]}


def build(g):
    waistband(g, "P", "plain", 14930)
    for leg in legs(g, "P", "plain", 14931, rows=(0, 8), crease=False):
        thorn_band(leg.strip, 8, "A")
    for face in flaps(g, "skirt", 9, "P", "plain", 14932, width=9, top=11.6, front_z=-2.9, back_z=1.9):
        thorn_band(face, face.h - 1, "A")
    sandals(g)
