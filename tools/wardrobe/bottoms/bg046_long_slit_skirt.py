"""Side Slit Long Skirt: a straight skirt to the ankle with slits high on both sides, fitted shorts
beneath, a narrow obi belt and soft flat shoes."""
from kit import belt, flaps, footwear
from paint import fabric, strip_fabric

META = {"name": "Side Slit Long Skirt", "gender": "female",
        "description": "Ankle-length skirt slit high at both sides, shorts beneath, narrow belt, flat shoes.",
        "tags": ["shinobi", "skirt"]}


def build(g):
    body = g.part("body")
    strip_fabric(body, "P", "smooth", 33500, 2, 9, 11)
    fabric(body.bottom, "P", "smooth", 33500, 1)
    for side in ("right", "left"):
        leg = g.part(f"{side}_leg")
        strip_fabric(leg, "K", "plain", 33501, 2, 0, 1)
        fabric(leg.top, "K", "plain", 33501, 2)
    footwear(g, "shoe", top=10, role="K", base=2)
    belt(g, "waist_band", y=9.2, role="A", height=1, buckle=None, inflate=.15)
    for face in flaps(g, "waist_skirt", 11, "P", "smooth", 33503, width=8, hem="P1", top=10.0, front_z=-2.9, back_z=1.9):
        face.vline(0, 1, 10, "P1"), face.vline(7, 1, 10, "P3"), face.vline(3, 3, 10, "P1")
