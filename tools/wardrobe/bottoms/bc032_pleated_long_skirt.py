"""Pleated Long Skirt: a mother's everyday skirt to the ankle, soft knife pleats all round from a
plain waistband, over soft cloth shoes."""
from kit_household import cloth_shoes, skirt, trouser_legs, waist

META = {"name": "Pleated Long Skirt", "gender": "female",
        "description": "Ankle-length knife-pleated skirt from a plain waistband, cloth shoes.",
        "tags": ["civilian", "skirt"]}


def pleats(face, rows=None):
    for y in rows or range(face.h):
        for x in range(1, face.w, 2):
            face.set(x, y, "D1")


def build(g):
    waist(g, "D", "plain", 37596, band="D3")
    trouser_legs(g, "D", "plain", 37597, rows=(0, 9), base=1)
    cloth_shoes(g, "K", 2)
    skirt(g, "skirt", 11, "D", "plain", 37599, hem="D1", pattern=pleats)
