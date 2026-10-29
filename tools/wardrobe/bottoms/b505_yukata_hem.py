"""Yukata Hem: the lower half of the Evening Yukata, falling straight to the ankle with the overlap
at the front, over wooden geta."""
from kit import footwear
from paint import fabric, strip_fabric

META = {"name": "Yukata Hem", "gender": "unisex",
        "description": "The yukata's skirt falling straight to the ankle, over wooden geta.",
        "tags": ["nara", "robe"], "locked_to": "t510_evening_yukata"}

SPRIGS = [(1, 2), (2, 7)]


def build(g):
    body = g.part("body")
    strip_fabric(body, "P", "weave", 5641, 2, 9, 11)
    fabric(body.bottom, "P", "weave", 5641, 1)
    for side in ("right", "left"):
        leg = g.part(f"{side}_leg")
        strip_fabric(leg, "P", "weave", 5642 + (side == "left"), 2, 0, 9)
        fabric(leg.top, "P", "weave", 5642, 2)
        for face in leg.sides:
            for x, y in SPRIGS:
                face.set(x, y, "A2"), face.set(x - 1, y - 1, "A2"), face.set(x + 1, y - 1, "A2")
        leg.strip.hline(0, leg.strip.w - 1, 9, "P1")
    # The overlap edge running down the front of the left leg.
    g.part("left_leg").front.vline(0, 0, 9, "S3")
    footwear(g, "clog", top=10, role="L", base=3, sole="K1")
