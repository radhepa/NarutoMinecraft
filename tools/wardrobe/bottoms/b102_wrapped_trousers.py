"""Wrapped Trousers: loose dark trousers bound from the knee to the ankle in cream gaiters laced up
the side, a knotted waist tie and dark sandals: the clan's marching wear."""
from kit_shinobi import sandals
from paint import fabric, k, solid, strip_fabric

META = {"name": "Wrapped Trousers", "gender": "unisex",
        "description": "Loose dark trousers, cream laced gaiters from knee to ankle, knotted waist tie, dark sandals.",
        "tags": ["shinobi"]}


def build(g):
    body = g.part("body")
    strip_fabric(body, "D", "twill", 1710, 2, 9, 11)
    body.strip.hline(0, body.strip.w - 1, 9, "D3")
    fabric(body.bottom, "D", "twill", 1710, 1)
    for side in ("right", "left"):
        leg = g.part(f"{side}_leg")
        strip_fabric(leg, "D", "twill", 1711 + (side == "left"), 2, 0, 5)
        fabric(leg.top, "D", "twill", 1711, 2)
        for y in range(6, 10):
            for x in range(leg.strip.w):
                leg.strip.set(x, y, k("S", 3 if (x + y) % 4 else 2))
        outer = leg.right if side == "right" else leg.left
        for y in range(6, 10):
            outer.set(1 if y % 2 else 2, y, "K2")
    sandals(g)
    for side, bone in (("right", "RIGHT_LEG"), ("left", "LEFT_LEG")):
        puff = g.piece(f"{side}_blouse", bone, (-2.5, 4.4, -2.5), (5, 2, 5))
        solid(puff, "D", "twill", 1713, 2)
        for face in puff.sides:
            face.hline(0, face.w - 1, 0, "D3")
    for i, (x, rz) in enumerate(((2.2, 10), (3.0, -8))):
        end = g.piece(f"waist_tie_{i}", "TORSO", (0, 0, 0), (1, 3, 1), pivot=(x, 10.4, -2.4), rotation=(0, 0, rz),
                      motion="sway")
        solid(end, "D", "twill", 1714 + i, 3)
