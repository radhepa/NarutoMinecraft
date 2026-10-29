"""Apron Skirt Leggings: snug full-length leggings under an apron skirt of two panels, front and
back, open at the sides and banded in the accent, the shins bound in pale wraps."""
from kit import belt, flaps
from kit_kunoichi import shin_wrap
from paint import fabric, strip_fabric

META = {"name": "Apron Skirt Leggings", "gender": "unisex",
        "description": "Full leggings under a front-and-back apron skirt open at the sides, shin wraps.",
        "tags": ["shinobi", "skirt"]}


def build(g):
    body = g.part("body")
    strip_fabric(body, "K", "smooth", 33420, 2, 9, 11)
    fabric(body.bottom, "K", "smooth", 33420, 1)
    for side in ("right", "left"):
        leg = g.part(f"{side}_leg")
        strip_fabric(leg, "K", "smooth", 33421 + (side == "left"), 2, 0, 11)
        fabric(leg.top, "K", "smooth", 33421, 2)
        leg.bottom.fill("K0")
    shin_wrap(g, 7, 11)
    belt(g, "waist_band", y=9.3, role="A", height=1, buckle=None, inflate=.15)
    for face in flaps(g, "waist_apron", 7, "P", "weave", 33424, width=7, hem="A2", top=10.2, front_z=-2.9, back_z=1.9):
        face.hline(0, 6, 1, "P1")
