"""Bandaged Trousers: grey trousers bloused into long off-white bandage wraps from the knee to the
ankle, the wraps of the clan that hides its wounds, a leather holster and open-toe sandals."""
from kit_shinobi import sandals, wraps
from paint import fabric, solid, strip_fabric

META = {"name": "Bandaged Trousers", "gender": "unisex",
        "description": "Grey trousers bloused into long off-white wraps from knee to ankle, a holster, sandals.",
        "tags": ["shinobi"]}


def build(g):
    body = g.part("body")
    strip_fabric(body, "P", "twill", 13840, 2, 9, 11)
    body.strip.hline(0, body.strip.w - 1, 9, "P1")
    fabric(body.bottom, "P", "twill", 13840, 1)
    for side in ("right", "left"):
        leg = g.part(f"{side}_leg")
        strip_fabric(leg, "P", "twill", 13841 + (side == "left"), 2, 0, 4)
        fabric(leg.top, "P", "twill", 13841, 2)
    wraps(g, top=5, bottom=9)
    sandals(g)
    for side, bone in (("right", "RIGHT_LEG"), ("left", "LEFT_LEG")):
        puff = g.piece(f"{side}_blouse", bone, (-2.5, 3.6, -2.5), (5, 2, 5))
        solid(puff, "P", "twill", 13843, 2)
        for face in puff.sides:
            face.hline(0, face.w - 1, 0, "P3")
    holster = g.piece("holster", "LEFT_LEG", (0, 0, 0), (1, 3, 2), pivot=(2.0, .8, -1.0))
    solid(holster, "L", "leather", 13844, 2)
    holster.left.set(1, 0, "M3")
