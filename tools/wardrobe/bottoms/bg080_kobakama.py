"""Kobakama: short pleated hakama to the knee over shins wound in pale wraps, with split-toe socks
and straw sandals: a sealer's or scholar's field dress."""
from kit import flaps
from kit_hyuga import hakama_legs, tabi
from kit_yamanaka import wrapped
from paint import fabric, k, strip_fabric

META = {"name": "Kobakama", "gender": "unisex",
        "description": "Short pleated hakama to the knee, wrapped shins, tabi and straw sandals.",
        "tags": ["shinobi", "hakama", "wrap"]}


def build(g):
    body = g.part("body")
    strip_fabric(body, "D", "twill", 34780, 2, 9, 11)
    fabric(body.bottom, "D", "twill", 34780, 1)
    for side in ("right", "left"):
        leg = g.part(f"{side}_leg")
        strip_fabric(leg, "D", "twill", 34781, 2, 0, 4)
        fabric(leg.top, "D", "twill", 34781, 2)
        wrapped(leg.strip, 0, 5, leg.strip.w - 1, 8, "S")
    tabi(g, "S", "K1", "D2")
    for box in hakama_legs(g, "hakama", "D", 34782, flare=7, length=5, top=.4):
        for face in box.sides:
            face.hline(0, face.w - 1, face.h - 1, k("D", 0))
    flaps(g, "waist_hakama", 4, "D", "twill", 34784, width=9, top=10.8, front_z=-2.8, back_z=1.8)
