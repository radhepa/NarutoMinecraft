"""Umanori Hakama: narrow riding hakama, divided and pleated, cut to the shin and tied over wrapped
ankles and open-toe sandals so the wearer can run in it."""
from kit import flaps
from kit_hyuga import hakama_legs
from kit_shinobi import sandals, wraps
from paint import fabric, k, strip_fabric

META = {"name": "Umanori Hakama", "gender": "unisex",
        "description": "Narrow divided hakama to the shin, wrapped ankles, sandals.",
        "tags": ["shinobi", "hakama"]}


def build(g):
    body = g.part("body")
    strip_fabric(body, "D", "twill", 34500, 2, 9, 11)
    fabric(body.bottom, "D", "twill", 34500, 1)
    for side in ("right", "left"):
        leg = g.part(f"{side}_leg")
        strip_fabric(leg, "D", "twill", 34501, 2, 0, 6)
        fabric(leg.top, "D", "twill", 34501, 2)
    wraps(g, 7, 9)
    sandals(g)
    for box in hakama_legs(g, "hakama", "D", 34502, flare=2, length=7, top=.4):
        for face in box.sides:
            face.hline(0, face.w - 1, face.h - 1, k("D", 0))
    flaps(g, "waist_hakama", 3, "D", "twill", 34504, width=9, top=10.8, front_z=-2.8, back_z=1.8)
