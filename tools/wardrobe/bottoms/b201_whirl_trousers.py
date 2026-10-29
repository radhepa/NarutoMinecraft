"""Whirl Trousers: loose trousers bloused into shin wraps at a cuff banded in red waves, a seal-tag
pouch at the back of the waist and open-toe sandals."""
from kit_shinobi import sandals, wraps
from kit_uzumaki import waves
from paint import fabric, solid, strip_fabric

META = {"name": "Whirl Trousers", "gender": "unisex",
        "description": "Loose trousers bloused at a wave-banded cuff over shin wraps, tag pouch, sandals.",
        "tags": ["shinobi"]}


def build(g):
    body = g.part("body")
    strip_fabric(body, "D", "twill", 2400, 2, 9, 11)
    body.strip.hline(0, body.strip.w - 1, 9, "D1")
    fabric(body.bottom, "D", "twill", 2400, 1)
    for side in ("right", "left"):
        leg = g.part(f"{side}_leg")
        strip_fabric(leg, "D", "twill", 2401 + (side == "left"), 2, 0, 6)
        fabric(leg.top, "D", "twill", 2401, 2)
        leg.front.vline(1 if side == "right" else 2, 1, 5, "D1")
    wraps(g, 7, 9)
    sandals(g)
    for side, bone in (("right", "RIGHT_LEG"), ("left", "LEFT_LEG")):
        cuff = g.piece(f"{side}_cuff", bone, (-2.5, 5.0, -2.5), (5, 2, 5))
        solid(cuff, "D", "twill", 2403, 2)
        for face in cuff.sides:
            waves(face, 0, "A", 2)
    pouch = g.piece("waist_pouch", "TORSO", (0, 0, 0), (3, 2, 1), pivot=(-1.5, 9.4, 2.2))
    solid(pouch, "L", "leather", 2404, 2)
    pouch.back.hline(0, 2, 0, "S3"), pouch.back.set(1, 1, "A2")
