"""Heiress Trousers: slim navy trousers cut off at the mid-calf, a white wrap at the right thigh
under a kunai holster, bare ankles and navy open-toe sandals."""
from kit import leg_ring
from kit_shinobi import sandals
from paint import fabric, solid, strip_fabric

META = {"name": "Heiress Trousers", "gender": "unisex",
        "description": "Slim navy trousers to mid-calf, a wrapped thigh holster, navy sandals.", "tags": ["shinobi"]}


def build(g):
    body = g.part("body")
    strip_fabric(body, "D", "twill", 4921, 2, 9, 11)
    body.strip.hline(0, body.strip.w - 1, 9, "D1")
    fabric(body.bottom, "D", "twill", 4921, 1)
    for side in ("right", "left"):
        leg = g.part(f"{side}_leg")
        strip_fabric(leg, "D", "twill", 4922 + (side == "left"), 2, 0, 8)
        fabric(leg.top, "D", "twill", 4922, 2)
        leg.strip.hline(0, leg.strip.w - 1, 8, "D1")
        leg.front.vline(1 if side == "right" else 2, 1, 7, "D3")
    for ring in leg_ring(g, "cuff", 8.0, "D", 2, (5, 1, 5), "twill"):
        for face in ring.sides:
            face.hline(0, face.w - 1, 0, "D3")
    sandals(g)
    wrap = g.piece("thigh_wrap", "RIGHT_LEG", (-2.4, 1.2, -2.4), (5, 2, 5))
    solid(wrap, "S", "weave", 4924, 3, edge=False)
    for face in wrap.sides:
        face.hline(0, face.w - 1, 1, "S2")
    holster = g.piece("holster", "RIGHT_LEG", (0, 0, 0), (1, 3, 2), pivot=(-3.0, 1.0, -1.0))
    solid(holster, "K", "leather", 4925, 3)
    holster.right.set(0, 0, "M3"), holster.right.set(1, 0, "M2")
