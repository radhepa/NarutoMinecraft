"""Bandaged Shorts: snug lavender shorts to mid-thigh with a purple hem, both shins wound in bandages
to the ankle above navy open-toe sandals."""
from kit import leg_ring
from kit_shinobi import sandals
from kit_yamanaka import wrapped
from paint import fabric, strip_fabric

META = {"name": "Bandaged Shorts", "gender": "unisex",
        "description": "Lavender mid-thigh shorts with a purple hem, bandaged shins, navy sandals.", "tags": ["shinobi"]}


def build(g):
    body = g.part("body")
    strip_fabric(body, "S", "plain", 7270, 2, 9, 11)
    body.strip.hline(0, body.strip.w - 1, 9, "P2")
    fabric(body.bottom, "S", "plain", 7270, 1)
    for side in ("right", "left"):
        leg = g.part(f"{side}_leg")
        strip_fabric(leg, "S", "plain", 7271 + (side == "left"), 2, 0, 3)
        fabric(leg.top, "S", "plain", 7271, 2)
        wrapped(leg.strip, 0, 6, leg.strip.w - 1, 9)
    for ring in leg_ring(g, "hem", 3.2, "P", 2, (5, 1, 5), "plain"):
        for face in ring.sides:
            face.hline(0, face.w - 1, 0, "P3")
    sandals(g)
