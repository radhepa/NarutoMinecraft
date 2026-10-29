"""Medic Slacks: light slacks in the coat colour bloused into pale shin wraps, open-toe sandals and
a flat pouch of bandages at the back of the waist."""
from kit_shinobi import sandals, wraps
from paint import fabric, solid, strip_fabric

META = {"name": "Medic Slacks", "gender": "unisex",
        "description": "Light slacks bloused into shin wraps, sandals, a bandage pouch at the back.",
        "tags": ["shinobi"]}


def build(g):
    body = g.part("body")
    strip_fabric(body, "P", "smooth", 34420, 2, 9, 11)
    body.strip.hline(0, body.strip.w - 1, 9, "P1")
    fabric(body.bottom, "P", "smooth", 34420, 1)
    for side, bone in (("right", "RIGHT_LEG"), ("left", "LEFT_LEG")):
        leg = g.part(f"{side}_leg")
        strip_fabric(leg, "P", "smooth", 34421 + (side == "left"), 2, 0, 5)
        fabric(leg.top, "P", "smooth", 34421, 2)
        leg.front.vline(1 if side == "right" else 2, 0, 5, "P1")
        puff = g.piece(f"{side}_blouse", bone, (-2.5, 4.6, -2.5), (5, 2, 5))
        solid(puff, "P", "smooth", 34423, 2)
        for face in puff.sides:
            face.hline(0, face.w - 1, 0, "P3")
    wraps(g)
    sandals(g)
    pouch = g.piece("waist_pouch", "TORSO", (0, 0, 0), (4, 2, 1), pivot=(-2.0, 9.4, 2.2))
    solid(pouch, "S", "plain", 34425, 3)
    pouch.back.hline(0, 3, 0, "A2")
