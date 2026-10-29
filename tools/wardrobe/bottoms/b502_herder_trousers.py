"""Herder Trousers: sturdy forest trousers in leather-brown cloth, patched at the knees, tucked into
soft wrapped boots for the deer paddocks."""
from kit import footwear, leg_ring
from paint import fabric, k, strip_fabric

META = {"name": "Herder Trousers", "gender": "unisex",
        "description": "Sturdy brown trousers with patched knees tucked into soft wrapped boots.",
        "tags": ["shinobi", "work"]}


def build(g):
    body = g.part("body")
    strip_fabric(body, "L", "twill", 5611, 2, 9, 11)
    body.strip.hline(0, body.strip.w - 1, 9, "L1")
    fabric(body.bottom, "L", "twill", 5611, 1)
    for side in ("right", "left"):
        leg = g.part(f"{side}_leg")
        strip_fabric(leg, "L", "twill", 5612 + (side == "left"), 2, 0, 7)
        fabric(leg.top, "L", "twill", 5612, 2)
        # Knee patch.
        for y in (4, 5):
            for x in (1, 2):
                leg.front.set(x, y, k("D", 2))
        leg.front.set(0, 4, "L1"), leg.front.set(3, 5, "L1")
    footwear(g, "boot", top=8, role="K", base=2)
    for ring in leg_ring(g, "boot_cuff", 7.6, "K", 3, (5, 1, 5)):
        for face in ring.sides:
            for x in range(face.w):
                face.set(x, 0, "K3" if x % 2 else "K2")
