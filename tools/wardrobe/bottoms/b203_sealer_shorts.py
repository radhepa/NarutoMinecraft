"""Sealer Shorts: knee shorts with a garter of paper seal tags round the left thigh, a holster on the
right, white shin wraps and open-toe sandals."""
from kit_shinobi import sandals, wraps
from kit_uzumaki import seal_tags
from paint import fabric, solid, strip_fabric

META = {"name": "Sealer Shorts", "gender": "unisex",
        "description": "Knee shorts, a garter of seal tags on the left thigh, holster, shin wraps, sandals.",
        "tags": ["shinobi"]}


def build(g):
    body = g.part("body")
    strip_fabric(body, "D", "twill", 2420, 2, 9, 11)
    fabric(body.bottom, "D", "twill", 2420, 1)
    for side in ("right", "left"):
        leg = g.part(f"{side}_leg")
        strip_fabric(leg, "D", "twill", 2421 + (side == "left"), 2, 0, 4)
        fabric(leg.top, "D", "twill", 2421, 2)
        leg.strip.hline(0, leg.strip.w - 1, 4, "D1")
    wraps(g, 7, 9)
    sandals(g)
    garter = g.piece("tag_garter", "LEFT_LEG", (-2.5, 1.0, -2.5), (5, 2, 5))
    solid(garter, "L", "leather", 2423, 2, edge=False)
    for face in garter.sides:
        seal_tags(face, 0, 2, every=2, seed=2424)
    holster = g.piece("holster", "RIGHT_LEG", (0, 0, 0), (1, 3, 2), pivot=(-3.0, .8, -1.0))
    solid(holster, "K", "leather", 2425, 3)
    holster.right.set(0, 0, "M3"), holster.right.set(1, 0, "M2")
