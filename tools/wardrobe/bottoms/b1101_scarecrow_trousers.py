"""Scarecrow Trousers: Kakashi's navy trousers, taped closed at the shins with white tape, a kunai
holster over a bandage on the right thigh and navy open-toe sandals."""
from kit_shinobi import sandals
from paint import fabric, solid, strip_fabric

META = {"name": "Scarecrow Trousers", "gender": "unisex",
        "description": "Navy trousers taped at the shins, a holster over a bandaged right thigh, navy sandals.",
        "tags": ["shinobi"]}


def build(g):
    body = g.part("body")
    strip_fabric(body, "D", "twill", 11101, 2, 9, 11)
    body.strip.hline(0, body.strip.w - 1, 9, "D1")
    fabric(body.bottom, "D", "twill", 11101, 1)
    for side in ("right", "left"):
        leg = g.part(f"{side}_leg")
        strip_fabric(leg, "D", "twill", 11102 + (side == "left"), 2, 0, 9)
        fabric(leg.top, "D", "twill", 11102, 2)
        leg.front.vline(1 if side == "right" else 2, 1, 6, "D3")
        # White tape wound tight round the shin.
        for y in (7, 8):
            for x in range(leg.strip.w):
                leg.strip.set(x, y, "S2" if (x + y) % 4 == 0 else "S3")
        leg.strip.hline(0, leg.strip.w - 1, 9, "D1")
    sandals(g)
    wrap = g.piece("thigh_wrap", "RIGHT_LEG", (-2.45, 1.4, -2.45), (5, 2, 5))
    solid(wrap, "S", "weave", 11104, 3, edge=False)
    for face in wrap.sides:
        face.hline(0, face.w - 1, 1, "S2")
    holster = g.piece("holster", "RIGHT_LEG", (0, 0, 0), (1, 3, 2), pivot=(-3.0, 1.2, -1.0))
    solid(holster, "K", "leather", 11105, 3)
    holster.right.set(0, 0, "M3"), holster.right.set(1, 0, "M2")
    pouch = g.piece("waist_pouch", "TORSO", (0, 0, 0), (3, 2, 1), pivot=(-1.5, 9.4, 2.2))
    solid(pouch, "L", "leather", 11106, 2)
    pouch.back.hline(0, 2, 0, "L3")
