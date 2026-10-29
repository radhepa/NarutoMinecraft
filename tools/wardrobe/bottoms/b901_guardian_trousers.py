"""Guardian Trousers: Asuma's navy trousers bloused into white shin wraps, a kunai holster taped to
the right thigh, a tool pouch at the back of the belt and navy open-toe sandals."""
from kit_shinobi import sandals, wraps
from paint import fabric, solid, strip_fabric

META = {"name": "Guardian Trousers", "gender": "unisex",
        "description": "Navy trousers bloused into white shin wraps, taped thigh holster, belt pouch, sandals.",
        "tags": ["shinobi"]}


def build(g):
    body = g.part("body")
    strip_fabric(body, "D", "twill", 9600, 2, 9, 11)
    body.strip.hline(0, body.strip.w - 1, 9, "D1")
    fabric(body.bottom, "D", "twill", 9600, 1)
    for side in ("right", "left"):
        leg = g.part(f"{side}_leg")
        strip_fabric(leg, "D", "twill", 9601 + (side == "left"), 2, 0, 6)
        fabric(leg.top, "D", "twill", 9601, 2)
        leg.front.vline(1 if side == "right" else 2, 1, 5, "D3")
        leg.strip.hline(0, leg.strip.w - 1, 6, "D1")
    wraps(g, 7, 9)
    sandals(g)
    for side, bone in (("right", "RIGHT_LEG"), ("left", "LEFT_LEG")):
        puff = g.piece(f"{side}_blouse", bone, (-2.5, 5.4, -2.5), (5, 2, 5))
        solid(puff, "D", "twill", 9603, 2)
        for face in puff.sides:
            face.hline(0, face.w - 1, 0, "D3")
    tape = g.piece("thigh_tape", "RIGHT_LEG", (-2.45, 1.4, -2.45), (5, 2, 5))
    solid(tape, "S", "weave", 9604, 3, edge=False)
    for face in tape.sides:
        face.set(1, 0, "S2"), face.set(3, 1, "S2")
    holster = g.piece("holster", "RIGHT_LEG", (0, 0, 0), (1, 3, 2), pivot=(-3.05, 1.2, -1.0))
    solid(holster, "K", "leather", 9605, 3)
    holster.right.set(0, 0, "M3"), holster.right.set(1, 0, "M2")
    pouch = g.piece("waist_pouch", "TORSO", (0, 0, 0), (3, 2, 1), pivot=(-1.5, 9.4, 2.2))
    solid(pouch, "L", "leather", 9606, 2)
    pouch.back.hline(0, 2, 0, "L3")
