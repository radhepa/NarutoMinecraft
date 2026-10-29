"""Training Shorts: dark knee shorts for courtyard sparring, white tape wound from the shin to the
ankle, a kunai holster on the right thigh and navy open-toe sandals."""
from kit import leg_ring
from kit_shinobi import sandals, wraps
from paint import fabric, solid, strip_fabric

META = {"name": "Training Shorts", "gender": "unisex",
        "description": "Dark knee shorts, taped shins, a right thigh holster, navy sandals.", "tags": ["shinobi"]}


def build(g):
    body = g.part("body")
    strip_fabric(body, "D", "twill", 4901, 2, 9, 11)
    body.strip.hline(0, body.strip.w - 1, 9, "D1")
    fabric(body.bottom, "D", "twill", 4901, 1)
    for side in ("right", "left"):
        leg = g.part(f"{side}_leg")
        strip_fabric(leg, "D", "twill", 4902 + (side == "left"), 2, 0, 4)
        fabric(leg.top, "D", "twill", 4902, 2)
        leg.front.vline(1 if side == "right" else 2, 1, 4, "D1")
    for ring in leg_ring(g, "hem", 4.0, "D", 2, (5, 1, 5), "twill"):
        for face in ring.sides:
            face.hline(0, face.w - 1, 0, "D3")
    wraps(g, 6, 9)
    sandals(g)
    strap = g.piece("holster_strap", "RIGHT_LEG", (-2.45, 1.2, -2.45), (5, 1, 5))
    solid(strap, "L", "leather", 4904, 2)
    holster = g.piece("holster", "RIGHT_LEG", (0, 0, 0), (1, 3, 2), pivot=(-3.0, 1.0, -1.0))
    solid(holster, "K", "leather", 4905, 3)
    holster.right.set(0, 0, "M3"), holster.right.set(1, 0, "M2")
