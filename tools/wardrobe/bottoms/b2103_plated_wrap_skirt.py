"""Plated Wrap Skirt: a short rust-orange wrap skirt over close gunmetal leggings, its front panel
studded along the hem with steel rivets, steel shin guards and sandals."""
from kit import flaps, legs, waistband
from kit_hagane import shin_guards
from kit_shinobi import sandals

META = {"name": "Plated Wrap Skirt", "gender": "unisex",
        "description": "Short rust wrap skirt with a riveted hem over gunmetal leggings, steel shin guards, sandals.",
        "tags": ["shinobi", "skirt"]}


def build(g):
    waistband(g, "A", "weave", 21988, 2)
    legs(g, "D", "smooth", 21989, 2, rows=(0, 9), crease=False)
    front, back = flaps(g, "skirt", 4, "A", "weave", 21990, hem=None)
    for face in (front, back):
        face.hline(0, face.w - 1, 3, "M2")
        for x in (1, 4, 7):
            face.set(x, 3, "M4")
    front.vline(6, 1, 2, "A1")
    sandals(g)
    shin_guards(g, top=5.0, height=5, seed=21991)
