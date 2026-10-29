"""Warmer Shorts: dark knee shorts with a rolled hem over white leg warmers from the knee to the
ankle and navy open-toe sandals."""
from kit import leg_ring
from kit_shinobi import sandals
from paint import fabric, strip_fabric

META = {"name": "Warmer Shorts", "gender": "unisex",
        "description": "Dark knee shorts, white ribbed leg warmers to the ankle, navy sandals.", "tags": ["shinobi"]}


def build(g):
    body = g.part("body")
    strip_fabric(body, "K", "twill", 3978, 2, 9, 11)
    fabric(body.bottom, "K", "twill", 3978, 1)
    for side in ("right", "left"):
        leg = g.part(f"{side}_leg")
        strip_fabric(leg, "K", "twill", 3979 + (side == "left"), 2, 0, 4)
        fabric(leg.top, "K", "twill", 3979, 2)
        for y in range(6, 10):
            for x in range(leg.strip.w):
                leg.strip.set(x, y, "S2" if y == 9 else ("S3" if x % 2 else "S4"))
    for ring in leg_ring(g, "short_hem", 4.0, "K", 2, (5, 1, 5), "twill"):
        for face in ring.sides:
            face.hline(0, face.w - 1, 0, "K3")
    leg_ring(g, "warmer_top", 5.6, "S", 3, (5, 1, 5), "rib", inflate=.05)
    sandals(g)
