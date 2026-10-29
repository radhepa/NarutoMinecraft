"""Genin Track Pants: orange track pants with a white drawstring, cuffs rolled up over the shins,
a bandaged kunai holster on the right thigh and navy open-toe sandals."""
from kit import leg_ring
from kit_shinobi import sandals
from paint import fabric, solid, strip_fabric

META = {"name": "Genin Track Pants", "gender": "unisex",
        "description": "Orange track pants rolled at the shin, bandaged thigh holster, navy sandals.",
        "tags": ["shinobi", "genin"]}


def build(g):
    body = g.part("body")
    strip_fabric(body, "P", "plain", 90, 2, 9, 11)
    body.strip.hline(0, body.strip.w - 1, 9, "P3")
    fabric(body.bottom, "P", "plain", 90, 1)
    body.front.set(3, 10, "S3"), body.front.set(4, 10, "S3"), body.front.set(3, 11, "S2")
    for side in ("right", "left"):
        leg = g.part(f"{side}_leg")
        strip_fabric(leg, "P", "plain", 91 + (side == "left"), 2, 0, 9)
        fabric(leg.top, "P", "plain", 91, 2)
        leg.front.vline(1 if side == "right" else 2, 1, 7, "P1")
        # Bare shin between the rolled cuff and the sandal straps.
        leg.strip.hline(0, leg.strip.w - 1, 9, "P1")
    sandals(g)
    for ring in leg_ring(g, "cuff_roll", 7.6, "P", 2, (5, 2, 5), "weave"):
        for face in ring.sides:
            face.hline(0, face.w - 1, 0, "P3"), face.hline(0, face.w - 1, 1, "P1")
    wrap = g.piece("thigh_wrap", "RIGHT_LEG", (-2.45, 1.4, -2.45), (5, 2, 5))
    solid(wrap, "S", "plain", 93, 3, edge=False)
    for face in wrap.sides:
        face.hline(0, face.w - 1, 1, "S2")
    holster = g.piece("holster", "RIGHT_LEG", (0, 0, 0), (1, 3, 2), pivot=(-3.0, 1.2, -1.0))
    solid(holster, "K", "leather", 94, 3)
    holster.right.set(0, 0, "M3"), holster.right.set(1, 0, "M2")
