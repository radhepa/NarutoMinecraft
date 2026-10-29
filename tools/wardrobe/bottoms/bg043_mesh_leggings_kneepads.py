"""Mesh Leggings Kneepads: short fitted shorts over chain-mesh leggings to the ankle, padded knee
guards strapped on, and tall open-toe sandals."""
from kit import leg_ring
from kit_shinobi import mesh, sandals
from paint import fabric, solid, strip_fabric

META = {"name": "Mesh Leggings Kneepads", "gender": "unisex",
        "description": "Short shorts over ankle-length mesh leggings, strapped knee guards, sandals.",
        "tags": ["shinobi"]}


def build(g):
    body = g.part("body")
    strip_fabric(body, "P", "plain", 33440, 2, 9, 11)
    fabric(body.bottom, "P", "plain", 33440, 1)
    for side in ("right", "left"):
        leg = g.part(f"{side}_leg")
        strip_fabric(leg, "P", "plain", 33441, 2, 0, 1)
        fabric(leg.top, "P", "plain", 33441, 2)
        strip_fabric(leg, "K", "plain", 33442, 1, 2, 9)
        mesh(leg.strip, 0, 2, leg.strip.w - 1, 9, "K3")
        leg.strip.hline(0, 15, 1, "P1")
    sandals(g)
    for side, bone in (("right", "RIGHT_LEG"), ("left", "LEFT_LEG")):
        pad = g.piece(f"{side}_kneepad", bone, (-1.5, 0, -.5), (3, 3, 1), pivot=(0, 4.6, -2.2))
        solid(pad, "L", "leather", 33443, 2)
        pad.front.hline(0, 2, 0, "L3"), pad.front.set(1, 1, "M3")
    leg_ring(g, "knee_strap", 6.8, "L", 1, (5, 1, 5), "leather")
