"""Vented Long Tunic: a straight long-sleeved tunic to mid-thigh, split high at both sides into a
front and a back panel, a narrow belt and a turned collar: plain, practical, worn by anyone."""
from kit import belt, collar, flaps, sleeves
from paint import cap, strip_fabric

META = {
    "name": "Vented Long Tunic",
    "gender": "unisex",
    "description": "Long-sleeved tunic to mid-thigh split at the sides, a narrow belt, a turned collar.",
    "tags": ["shinobi", "genin", "tunic"],
    "rejects": ["skirt"],
    "covers_waist": True,
}


def build(g):
    body = g.part("body")
    strip_fabric(body, "P", "twill", 33220, 2)
    cap(body, "P", texture="twill", seed=33220)
    body.front.vline(4, 1, 11, "P1")
    sleeves(g, "P", "twill", 33221, rows=(0, 9), cuff="P1")
    belt(g, "belt", y=9.2, role="K", height=1, buckle="M")
    for face in flaps(g, "panel", 5, "P", "twill", 33223, width=8, hem="P1", top=11.0, front_z=-2.6, back_z=1.6):
        face.vline(0, 1, 4, "P1")
    neck = collar(g, "collar", "P", "twill", height=1, y=-.8)
    neck.front.hline(3, 4, 0, "P0")
