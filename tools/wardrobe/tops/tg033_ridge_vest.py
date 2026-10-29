"""Ridge Vest: a jonin flak vest built up for the front line, padded shoulder guards over the sleeves,
a row of four pockets under the collar and a buckled strap round each side."""
from kit import SIDES, arm_bone, arm_x
from kit_field import collar, pocket, shirt, vest
from paint import k, solid

META = {
    "name": "Ridge Vest",
    "gender": "unisex",
    "description": "Padded zip vest with shoulder guards, four chest pockets and buckled side straps.",
    "tags": ["shinobi", "vest", "jonin"],
}


def build(g):
    shirt(g, "D", 32240)
    jacket = vest(g, "P", 32244, ribs=(4, 7, 10))
    for face in (jacket.right, jacket.left):
        face.hline(0, 3, 6, "L2")
    jacket.right.set(1, 6, "M3"), jacket.left.set(2, 6, "M3")
    collar(g, "collar", "P", 32245)
    for i, x in enumerate((-3.2, -1.6, 1.6, 3.2)):
        pocket(g, f"pocket_{i}", (x, 1.6, -2.3), (3, 4, 1), "P", 32246 + i)
    for side in SIDES:
        guard = g.piece(f"{side}_shoulder_guard", arm_bone(side), (arm_x(side) - .6, -2.7, -2.6), (5, 3, 5))
        solid(guard, "P", "plain", 32250 + (side == "left"), 2)
        for face in guard.sides:
            face.hline(0, face.w - 1, 0, k("P", 3)), face.hline(0, face.w - 1, 1, k("P", 1))
