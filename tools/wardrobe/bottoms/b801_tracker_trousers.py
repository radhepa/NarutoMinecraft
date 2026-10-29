"""Tracker Trousers: charcoal trousers with patched knees for crawling through brush, bloused into
shin wraps over open-toe sandals, a kunai holster on the right thigh and a pouch at the back."""
from kit_shinobi import sandals, wraps
from paint import fabric, solid, strip_fabric

META = {"name": "Tracker Trousers", "gender": "unisex",
        "description": "Charcoal trousers with patched knees, shin wraps, a thigh holster and sandals.",
        "tags": ["shinobi"]}


def build(g):
    body = g.part("body")
    strip_fabric(body, "K", "twill", 8750, 3, 9, 11)
    body.strip.hline(0, body.strip.w - 1, 9, "K2")
    fabric(body.bottom, "K", "twill", 8750, 2)
    for side in ("right", "left"):
        leg = g.part(f"{side}_leg")
        strip_fabric(leg, "K", "twill", 8751 + (side == "left"), 3, 0, 5)
        fabric(leg.top, "K", "twill", 8751, 3)
        # A knee patch stitched over the front.
        leg.front.rect(0, 3, 4, 2, "K4")
        leg.front.hline(0, 3, 3, "K2")
    wraps(g, 6, 9)
    sandals(g)
    for side, bone in (("right", "RIGHT_LEG"), ("left", "LEFT_LEG")):
        puff = g.piece(f"{side}_blouse", bone, (-2.5, 4.8, -2.5), (5, 2, 5))
        solid(puff, "K", "twill", 8753, 3)
        for face in puff.sides:
            face.hline(0, face.w - 1, 0, "K4")
    strap = g.piece("holster_strap", "RIGHT_LEG", (-2.45, 1.0, -2.45), (5, 1, 5))
    solid(strap, "L", "leather", 8754, 2)
    holster = g.piece("holster", "RIGHT_LEG", (0, 0, 0), (1, 3, 2), pivot=(-3.0, .8, -1.0))
    solid(holster, "K", "leather", 8755, 2)
    holster.right.set(0, 0, "M3"), holster.right.set(1, 0, "M2")
    pouch = g.piece("waist_pouch", "TORSO", (0, 0, 0), (3, 2, 1), pivot=(-1.5, 9.4, 2.2))
    solid(pouch, "L", "leather", 8756, 2)
    pouch.back.hline(0, 2, 0, "L3")
