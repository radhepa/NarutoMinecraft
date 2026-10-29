"""Sensor Shorts: after Karin's: short black shorts over black thigh-high stockings and dark
open-toe sandals."""
from kit_shinobi import sandals
from paint import fabric, strip_fabric

META = {"name": "Sensor Shorts", "gender": "unisex",
        "description": "Short black shorts, black thigh-high stockings, sandals.", "tags": ["shinobi"]}


def build(g):
    body = g.part("body")
    strip_fabric(body, "K", "plain", 2460, 2, 8, 11)
    body.strip.hline(0, body.strip.w - 1, 8, "K3")
    fabric(body.bottom, "K", "plain", 2460, 1)
    for side in ("right", "left"):
        leg = g.part(f"{side}_leg")
        strip_fabric(leg, "K", "plain", 2461, 2, 0, 1)
        fabric(leg.top, "K", "plain", 2461, 2)
        leg.strip.hline(0, leg.strip.w - 1, 1, "K3")
        strip_fabric(leg, "K", "rib", 2462 + (side == "left"), 1, 3, 9)
        leg.strip.hline(0, leg.strip.w - 1, 3, "K2")
    sandals(g)
