"""Cargo Shorts: slate knee-length shorts with a pocket on each thigh, white wraps around the shins,
a pouch at the back of the belt and navy open-toe sandals."""
from kit import leg_ring
from kit_shinobi import sandals, wraps
from paint import fabric, solid, strip_fabric

META = {"name": "Cargo Shorts", "gender": "unisex",
        "description": "Slate knee shorts with thigh pockets, shin wraps, a belt pouch, navy sandals.",
        "tags": ["shinobi", "genin"]}


def build(g):
    body = g.part("body")
    strip_fabric(body, "K", "twill", 281, 2, 9, 11)
    body.strip.hline(0, body.strip.w - 1, 9, "L2")
    fabric(body.bottom, "K", "twill", 281, 1)
    body.front.set(3, 9, "M3"), body.front.set(4, 9, "M3")
    for side in ("right", "left"):
        leg = g.part(f"{side}_leg")
        strip_fabric(leg, "K", "twill", 282 + (side == "left"), 2, 0, 5)
        fabric(leg.top, "K", "twill", 282, 2)
    for ring in leg_ring(g, "hem", 5.2, "K", 2, (5, 1, 5), "twill"):
        for face in ring.sides:
            face.hline(0, face.w - 1, 0, "K3")
    wraps(g, 6, 9)
    sandals(g)
    for side, bone, x in (("right", "RIGHT_LEG", -3.0), ("left", "LEFT_LEG", 2.0)):
        pocket = g.piece(f"{side}_cargo", bone, (0, 0, 0), (1, 3, 3), pivot=(x, 1.2, -1.5))
        solid(pocket, "K", "twill", 284, 3)
        outer = pocket.right if side == "right" else pocket.left
        outer.hline(0, 2, 0, "K1"), outer.set(1, 1, "M3")
    pouch = g.piece("waist_pouch", "TORSO", (0, 0, 0), (3, 2, 1), pivot=(-1.5, 9.4, 2.2))
    solid(pouch, "L", "leather", 285, 2)
    pouch.back.hline(0, 2, 0, "L3")
