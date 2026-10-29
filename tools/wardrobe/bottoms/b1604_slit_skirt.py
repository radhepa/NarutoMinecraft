"""Slit Skirt: a short dusky skirt over dark leggings, slit at the front, a senbon holster strapped
low on the right thigh below the hem and sandals."""
from kit import flaps
from kit_shinobi import sandals
from kit_shiranui import thigh_holster
from paint import fabric, strip_fabric

META = {"name": "Slit Skirt", "gender": "female",
        "description": "Short dusky skirt slit at the front over dark leggings, a low senbon holster, sandals.",
        "tags": ["shinobi", "skirt"]}


def build(g):
    body = g.part("body")
    strip_fabric(body, "D", "weave", 16882, 2, 9, 11)
    body.strip.hline(0, body.strip.w - 1, 9, "D3")
    fabric(body.bottom, "D", "weave", 16882, 1)
    for side in ("right", "left"):
        leg = g.part(f"{side}_leg")
        strip_fabric(leg, "K", "smooth", 16883 + (side == "left"), 2, 0, 9)
        fabric(leg.top, "K", "smooth", 16883, 2)
    sandals(g)
    front, back = flaps(g, "skirt", 5, "D", "weave", 16885, hem="D1", top=11.2)
    front.vline(4, 1, 4, "D0")
    thigh_holster(g, "right", seed=16887, y=3.0)
