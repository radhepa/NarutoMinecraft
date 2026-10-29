"""Kunoichi Shorts: snug dark shorts to mid-thigh with a rolled hem, a kunai holster over a white
thigh wrap on the right leg and navy open-toe sandals."""
from kit import leg_ring
from kit_shinobi import sandals
from paint import fabric, solid, strip_fabric

META = {"name": "Kunoichi Shorts", "gender": "unisex",
        "description": "Dark mid-thigh shorts, bandaged thigh holster, navy sandals.", "tags": ["shinobi"]}


def build(g):
    body = g.part("body")
    strip_fabric(body, "K", "plain", 110, 2, 9, 11)
    fabric(body.bottom, "K", "plain", 110, 1)
    for side in ("right", "left"):
        leg = g.part(f"{side}_leg")
        strip_fabric(leg, "K", "plain", 111 + (side == "left"), 2, 0, 3)
        fabric(leg.top, "K", "plain", 111, 2)
    for ring in leg_ring(g, "hem", 3.2, "K", 2, (5, 1, 5), "plain"):
        for face in ring.sides:
            face.hline(0, face.w - 1, 0, "K3")
    sandals(g)
    wrap = g.piece("thigh_wrap", "RIGHT_LEG", (-2.4, 4.2, -2.4), (5, 2, 5))
    solid(wrap, "S", "weave", 113, 3, edge=False)
    for face in wrap.sides:
        face.hline(0, face.w - 1, 1, "S2")
    holster = g.piece("holster", "RIGHT_LEG", (0, 0, 0), (1, 3, 2), pivot=(-3.0, 4.0, -1.0))
    solid(holster, "K", "leather", 114, 3)
    holster.right.set(0, 0, "M3"), holster.right.set(1, 0, "M2")
