"""Cargo Capris: loose cropped trousers ending below the knee with a buttoned pocket on each thigh,
cuffed hems and open-toe sandals; worn by anyone who needs the pockets."""
from kit import leg_ring, legs, waistband
from kit_shinobi import sandals
from paint import solid

META = {"name": "Cargo Capris", "gender": "unisex",
        "description": "Loose below-the-knee trousers with buttoned thigh pockets, cuffed hems, sandals.",
        "tags": ["shinobi", "casual"]}


def build(g):
    waistband(g, "D", "twill", 33660)
    legs(g, "D", "twill", 33661, rows=(0, 7))
    sandals(g)
    for side, bone, x in (("right", "RIGHT_LEG", -2.3), ("left", "LEFT_LEG", 1.3)):
        pocket = g.piece(f"{side}_pocket", bone, (0, 0, -1.5), (1, 3, 3), pivot=(x, 2.4, 0))
        solid(pocket, "D", "twill", 33662, 2)
        for face in pocket.sides:
            face.hline(0, face.w - 1, 0, "D3")
        (pocket.right if side == "right" else pocket.left).set(1, 1, "M3")
    for ring in leg_ring(g, "cuff", 7.2, "D", 3, (5, 1, 5), "twill"):
        for face in ring.sides:
            face.hline(0, face.w - 1, 0, "D3")
