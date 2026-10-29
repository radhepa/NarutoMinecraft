"""Mesh Leggings: snug dark shorts over chain-mesh leggings to the shin, a kunai holster on the
left thigh and navy open-toe sandals."""
from kit import leg_ring
from kit_shinobi import mesh, sandals
from paint import fabric, solid, strip_fabric

META = {"name": "Mesh Leggings", "gender": "unisex",
        "description": "Dark shorts over chain-mesh leggings, a left thigh holster, navy sandals.", "tags": ["shinobi"]}


def build(g):
    body = g.part("body")
    strip_fabric(body, "K", "plain", 300, 2, 9, 11)
    fabric(body.bottom, "K", "plain", 300, 1)
    for side in ("right", "left"):
        leg = g.part(f"{side}_leg")
        strip_fabric(leg, "K", "plain", 301 + (side == "left"), 2, 0, 3)
        fabric(leg.top, "K", "plain", 301, 2)
        mesh(leg.strip, 0, 4, leg.strip.w - 1, 9, "K3")
        leg.strip.hline(0, leg.strip.w - 1, 9, "K1")
    for ring in leg_ring(g, "hem", 3.2, "K", 2, (5, 1, 5), "plain"):
        for face in ring.sides:
            face.hline(0, face.w - 1, 0, "K3")
    sandals(g)
    strap = g.piece("holster_strap", "LEFT_LEG", (-2.45, 1.4, -2.45), (5, 1, 5))
    solid(strap, "L", "leather", 303, 2)
    holster = g.piece("holster", "LEFT_LEG", (0, 0, 0), (1, 3, 2), pivot=(2.0, 1.2, -1.0))
    solid(holster, "K", "leather", 304, 3)
    holster.left.set(0, 0, "M3"), holster.left.set(1, 0, "M2")
