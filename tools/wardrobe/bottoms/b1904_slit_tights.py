"""Slit Tights: dark fitted tights to the ankle under a short split underskirt, a thin rose band at
the waist, and dark low boots, worn under a long qipao or on their own."""
from kit import footwear, legs
from paint import fabric, k, strip_fabric

META = {"name": "Slit Tights", "gender": "unisex",
        "description": "Dark fitted tights to the ankle, a thin rose waist band, dark low boots.",
        "tags": ["shinobi"]}


def build(g):
    body = g.part("body")
    strip_fabric(body, "K", "smooth", 19740, 3, 9, 11)
    fabric(body.bottom, "K", "smooth", 19740, 2)
    body.strip.hline(0, body.strip.w - 1, 9, k("A", 2))
    legs(g, "K", "smooth", 19741, 3, rows=(0, 8), crease=False)
    for side in ("right", "left"):
        leg = g.part(f"{side}_leg")
        leg.strip.hline(0, leg.strip.w - 1, 3, k("K", 2))
    footwear(g, "boot", top=9, role="K", base=2, sole="K0")
    for side in ("right", "left"):
        g.part(f"{side}_pants").front.hline(0, 3, 9, k("A", 2))
