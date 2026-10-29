"""Bound Leggings: fitted ink-dark leggings, long pale bindings wound from the ankle to the knee
and edged with the wave, split-toe tabi boots."""
from kit import SIDES, footwear
from kit_namiashi import wave_band
from kit_shinobi import bandage
from paint import fabric, strip_fabric

META = {"name": "Bound Leggings", "gender": "unisex",
        "description": "Fitted dark leggings, pale bindings from ankle to knee edged with the wave, tabi boots.",
        "tags": ["shinobi"]}


def build(g):
    body = g.part("body")
    strip_fabric(body, "K", "smooth", 20631, 3, 9, 11)
    body.strip.hline(0, body.strip.w - 1, 9, "D2")
    fabric(body.bottom, "K", "smooth", 20631, 2)
    for side in SIDES:
        leg = g.part(f"{side}_leg")
        strip_fabric(leg, "K", "smooth", 20632 + (side == "left"), 3, 0, 9)
        fabric(leg.top, "K", "smooth", 20632, 3)
        bandage(leg.strip, 0, 5, leg.strip.w - 1, 8)
        wave_band(leg.strip, 4, "S", 2, ground="K3")
    footwear(g, "boot", top=9, role="K", base=2, sole="K0")
    for side in SIDES:
        g.part(f"{side}_pants").front.vline(1, 9, 11, "K0")
