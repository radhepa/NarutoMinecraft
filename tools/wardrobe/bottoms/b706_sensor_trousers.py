"""Sensor Trousers: close dark trousers piped in aqua down the outer seam, a kunai holster on the
right thigh, steel-capped shin guards and navy open-toe sandals."""
from kit import legs
from kit_shinobi import sandals
from paint import fabric, solid, strip_fabric

META = {"name": "Sensor Trousers", "gender": "unisex",
        "description": "Dark trousers with aqua side piping, a thigh holster, shin guards, navy sandals.",
        "tags": ["shinobi", "armor"]}


def build(g):
    body = g.part("body")
    strip_fabric(body, "K", "twill", 7670, 2, 9, 11)
    body.strip.hline(0, body.strip.w - 1, 9, "K3")
    fabric(body.bottom, "K", "twill", 7670, 1)
    for leg in legs(g, "K", "twill", 7671, 2, rows=(0, 9), crease=False):
        leg.right.vline(1, 0, 9, "A2"), leg.left.vline(2, 0, 9, "A2")
    sandals(g)
    for side, bone in (("right", "RIGHT_LEG"), ("left", "LEFT_LEG")):
        guard = g.piece(f"{side}_shin_guard", bone, (-2.2, 5.6, -2.5), (4, 4, 1))
        solid(guard, "S", "smooth", 7672, 2)
        guard.front.hline(0, 3, 0, "M3"), guard.front.hline(0, 3, 3, "M2")
    holster = g.piece("holster", "RIGHT_LEG", (0, 0, 0), (1, 3, 2), pivot=(-3.0, 1.4, -1.0))
    solid(holster, "L", "leather", 7673, 2)
    holster.right.set(0, 0, "M3"), holster.right.set(1, 0, "M2")
    strap = g.piece("holster_strap", "RIGHT_LEG", (-2.45, 1.8, -2.45), (5, 1, 5))
    solid(strap, "L", "leather", 7674, 2)
