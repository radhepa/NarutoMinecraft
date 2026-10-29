"""Forest Camo Trousers: field trousers blotched in leaf-shadow camouflage with a pocket on each
thigh, tucked into laced soft boots, a dark web belt: made for lying still in the undergrowth."""
from kit import belt, legs, waistband
from kit_rugged import camo, soft_boots
from paint import solid

META = {"name": "Forest Camo Trousers", "gender": "unisex",
        "description": "Camouflage field trousers with thigh pockets tucked into laced soft boots, a dark belt.",
        "tags": ["shinobi"]}


def build(g):
    body = waistband(g, "P", "weave", 35370, 2)
    camo(body.strip, 35371, 0, 10, None, 2)
    for leg in legs(g, "P", "weave", 35372, 2, rows=(0, 7), crease=False):
        camo(leg.strip, 35373, 0, 0, None, 8)
        camo(leg.top, 35373)
    soft_boots(g, top=8, role="L", laces="K1")
    for side, bone, x in (("right", "RIGHT_LEG", -3.0), ("left", "LEFT_LEG", 2.0)):
        pocket = g.piece(f"{side}_thigh_pocket", bone, (0, 0, 0), (1, 3, 3), pivot=(x, 1.4, -1.5))
        solid(pocket, "P", "weave", 35374, 2)
        outer = pocket.right if side == "right" else pocket.left
        outer.hline(0, 2, 0, "P3"), outer.set(1, 1, "L2")
    belt(g, "waist_belt", y=9.4, role="K", height=1, buckle="M")
