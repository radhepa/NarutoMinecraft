"""Lacquer Greaves: dark trousers with red lacquered shin guards (suneate) laced in gold over the
lower legs, leather knee straps and open-toe sandals."""
from kit_shinobi import sandals
from paint import fabric, solid, strip_fabric

META = {"name": "Lacquer Greaves", "gender": "unisex",
        "description": "Dark trousers, red lacquered shin guards laced in gold, leather straps, sandals.",
        "tags": ["shinobi", "armor", "akimichi"]}


def build(g):
    body = g.part("body")
    strip_fabric(body, "K", "twill", 6967, 2, 9, 11)
    fabric(body.bottom, "K", "twill", 6967, 1)
    for side in ("right", "left"):
        leg = g.part(f"{side}_leg")
        strip_fabric(leg, "K", "twill", 6968 + (side == "left"), 2, 0, 9)
        fabric(leg.top, "K", "twill", 6968, 2)
    sandals(g)
    for side, bone in (("right", "RIGHT_LEG"), ("left", "LEFT_LEG")):
        shin = g.piece(f"{side}_suneate", bone, (-2.5, 5.0, -2.6), (5, 5, 4), inflate=.12)
        solid(shin, "P", "smooth", 6970 + (side == "left"), 2, edge=False)
        for face in shin.sides:
            for y in (1, 3):
                face.hline(0, face.w - 1, y, "P1")
                for x in range(1, face.w, 2):
                    face.set(x, y, "A2")
            face.hline(0, face.w - 1, 0, "P3")
        strap = g.piece(f"{side}_knee_strap", bone, (-2.4, 4.0, -2.4), (5, 1, 5), inflate=.08)
        solid(strap, "L", "leather", 6972, 2, edge=False)
