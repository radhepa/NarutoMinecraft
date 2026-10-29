"""Swordsman's Trousers: straight slate-navy trousers, black shin guards strapped over the lower leg
with steel studs, a leather sword belt with a scabbard loop on the left hip, open-toe sandals."""
from kit import SIDES, leg_bone
from kit_shinobi import sandals
from paint import fabric, solid, strip_fabric

META = {"name": "Swordsman's Trousers", "gender": "unisex",
        "description": "Straight navy trousers, strapped black shin guards with studs, a sword belt, sandals.",
        "tags": ["shinobi"]}


def build(g):
    body = g.part("body")
    strip_fabric(body, "D", "twill", 15520, 2, 9, 11)
    fabric(body.bottom, "D", "twill", 15520, 1)
    for side in SIDES:
        leg = g.part(f"{side}_leg")
        strip_fabric(leg, "D", "twill", 15521 + (side == "left"), 2, 0, 9)
        fabric(leg.top, "D", "twill", 15521, 2)
        leg.front.vline(1 if side == "right" else 2, 1, 5, "D3")
    sandals(g)
    for side in SIDES:
        guard = g.piece(f"{side}_shin_guard", leg_bone(side), (-2.3, 5.4, -2.3), (4, 4, 4), inflate=.2)
        solid(guard, "K", "leather", 15523 + (side == "left"), 2)
        for face in guard.sides:
            face.hline(0, face.w - 1, 0, "K3")
            face.hline(0, face.w - 1, 2, "L2")
        guard.front.set(1, 1, "M3"), guard.front.set(2, 1, "M3")
    belt = g.piece("waist_belt", "TORSO", (-4.6, 9.2, -2.6), (9, 1, 5), inflate=.1)
    solid(belt, "L", "leather", 15526, 2, edge=False)
    belt.front.set(4, 0, "M3")
    loop = g.piece("waist_scabbard_loop", "TORSO", (0, 0, -1), (1, 2, 2), pivot=(4.6, 9.2, 0))
    solid(loop, "L", "leather", 15527, 2)
    loop.left.hline(0, 1, 0, "M3")
