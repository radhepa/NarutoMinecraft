"""Tide Skirt: a dark wrap skirt to the knee over fitted black leggings, front and back panels
hemmed in the pale wave, an accent sash and dark sandals."""
from kit import SIDES, flaps
from kit_namiashi import wave_band
from kit_shinobi import sandals
from paint import fabric, strip_fabric

META = {"name": "Tide Skirt", "gender": "female",
        "description": "Dark wrap skirt to the knee over black leggings, wave-hemmed panels, accent sash, sandals.",
        "tags": ["shinobi", "skirt"]}


def build(g):
    body = g.part("body")
    strip_fabric(body, "D", "weave", 20621, 2, 9, 11)
    body.strip.hline(0, body.strip.w - 1, 9, "A2"), body.strip.hline(0, body.strip.w - 1, 10, "A1")
    fabric(body.bottom, "D", "weave", 20621, 1)
    for side in SIDES:
        leg = g.part(f"{side}_leg")
        strip_fabric(leg, "K", "smooth", 20622 + (side == "left"), 3, 0, 9)
        fabric(leg.top, "K", "smooth", 20622, 3)
    for face in flaps(g, "skirt", 6, "D", "weave", 20623, width=9, top=11.0):
        wave_band(face, 4, "S", 2)
    sandals(g)
