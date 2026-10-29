"""Shadow Trousers: loose dark trousers bloused into the shin wraps, a kunai holster on the right
thigh, a shadow-black weapons pouch at the back and open-toe sandals."""
from kit_shinobi import sandals, wraps
from paint import fabric, solid, strip_fabric

META = {"name": "Shadow Trousers", "gender": "unisex",
        "description": "Loose dark trousers bloused into shin wraps, thigh holster, back pouch, sandals.",
        "tags": ["shinobi"]}


def build(g):
    body = g.part("body")
    strip_fabric(body, "D", "twill", 5601, 2, 9, 11)
    body.strip.hline(0, body.strip.w - 1, 9, "D1")
    fabric(body.bottom, "D", "twill", 5601, 1)
    for side in ("right", "left"):
        leg = g.part(f"{side}_leg")
        strip_fabric(leg, "D", "twill", 5602 + (side == "left"), 2, 0, 6)
        fabric(leg.top, "D", "twill", 5602, 2)
        leg.front.vline(1 if side == "right" else 2, 1, 5, "D1")
    wraps(g, 7, 9)
    sandals(g)
    for side, bone in (("right", "RIGHT_LEG"), ("left", "LEFT_LEG")):
        puff = g.piece(f"{side}_blouse", bone, (-2.5, 5.4, -2.5), (5, 2, 5))
        solid(puff, "D", "twill", 5604, 2)
        for face in puff.sides:
            face.hline(0, face.w - 1, 0, "D3")
    strap = g.piece("holster_strap", "RIGHT_LEG", (-2.45, 1.0, -2.45), (5, 1, 5))
    solid(strap, "K", "leather", 5605, 2)
    holster = g.piece("holster", "RIGHT_LEG", (0, 0, 0), (1, 3, 2), pivot=(-3.0, .8, -1.0))
    solid(holster, "K", "leather", 5606, 3)
    holster.right.set(0, 0, "M3")
    pouch = g.piece("waist_pouch", "TORSO", (0, 0, 0), (4, 2, 1), pivot=(-2.0, 9.4, 2.2))
    solid(pouch, "K", "leather", 5607, 2)
    pouch.back.hline(0, 3, 0, "K3")
