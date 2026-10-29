"""Cropped Trousers: loose charcoal trousers gathered just below the knee into a cloth band, white
tabi socks and straw sandals: house wear for the courtyard and the gate."""
from kit import leg_ring
from kit_hyuga import tabi
from paint import fabric, strip_fabric

META = {"name": "Cropped Trousers", "gender": "unisex",
        "description": "Loose charcoal trousers banded below the knee, white tabi, straw sandals.", "tags": ["shinobi", "hyuga"]}


def build(g):
    body = g.part("body")
    strip_fabric(body, "K", "plain", 4931, 3, 9, 11)
    body.strip.hline(0, body.strip.w - 1, 9, "K2")
    fabric(body.bottom, "K", "plain", 4931, 2)
    for side in ("right", "left"):
        leg = g.part(f"{side}_leg")
        strip_fabric(leg, "K", "plain", 4932 + (side == "left"), 3, 0, 6)
        fabric(leg.top, "K", "plain", 4932, 3)
        leg.front.vline(1 if side == "right" else 2, 1, 5, "K2")
        strip_fabric(leg, "S", "plain", 4934, 3, 7, 9)
    for ring in leg_ring(g, "gather", 4.4, "K", 3, (5, 2, 5), "plain", inflate=.1):
        for face in ring.sides:
            face.hline(0, face.w - 1, 1, "A2")
    tabi(g)
