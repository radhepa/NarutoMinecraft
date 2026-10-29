"""Lacquer Greaves: the legs of Choji's Part II armor, deep red bodysuit trousers with lacquered plates
over the thighs, shin guards (suneate) laced in gold, leather knee straps and open-toe sandals."""
from kit_shinobi import sandals
from paint import fabric, solid, strip_fabric

META = {"name": "Lacquer Greaves", "gender": "unisex",
        "description": "Deep red trousers, lacquered thigh plates and shin guards laced in gold, sandals.",
        "tags": ["shinobi", "armor", "akimichi"]}


def build(g):
    body = g.part("body")
    strip_fabric(body, "P", "twill", 6967, 1, 9, 11)
    fabric(body.bottom, "P", "twill", 6967, 0)
    for side in ("right", "left"):
        leg = g.part(f"{side}_leg")
        strip_fabric(leg, "P", "twill", 6968 + (side == "left"), 1, 0, 9)
        fabric(leg.top, "P", "twill", 6968, 1)
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
        thigh = g.piece(f"{side}_haidate", bone, (-2.5, .4, -2.8), (5, 3, 1), inflate=.15)
        solid(thigh, "P", "smooth", 6973, 2, edge=False)
        thigh.front.hline(0, 4, 0, "P3"), thigh.front.hline(0, 4, 2, "P1")
        thigh.front.set(1, 1, "A2"), thigh.front.set(3, 1, "A2")
        strap = g.piece(f"{side}_knee_strap", bone, (-2.4, 4.0, -2.4), (5, 1, 5), inflate=.08)
        solid(strap, "L", "leather", 6972, 2, edge=False)
