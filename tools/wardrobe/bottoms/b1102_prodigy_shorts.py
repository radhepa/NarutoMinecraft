"""Prodigy Shorts: young Kakashi's dark knee shorts, a bandaged right thigh with a holster, bare shins
and navy open-toe sandals."""
from kit_shinobi import sandals
from paint import fabric, solid, strip_fabric

META = {"name": "Prodigy Shorts", "gender": "unisex",
        "description": "Dark knee shorts, a bandaged thigh with a holster, bare shins, navy sandals.",
        "tags": ["shinobi"]}


def build(g):
    body = g.part("body")
    strip_fabric(body, "K", "twill", 11201, 3, 9, 11)
    body.strip.hline(0, body.strip.w - 1, 9, "K2")
    fabric(body.bottom, "K", "twill", 11201, 2)
    for side in ("right", "left"):
        leg = g.part(f"{side}_leg")
        strip_fabric(leg, "K", "twill", 11202 + (side == "left"), 3, 0, 5)
        fabric(leg.top, "K", "twill", 11202, 3)
        leg.strip.hline(0, leg.strip.w - 1, 5, "K1")
        leg.front.vline(1 if side == "right" else 2, 1, 4, "K4")
    sandals(g)
    for side, bone in (("right", "RIGHT_LEG"), ("left", "LEFT_LEG")):
        hem = g.piece(f"{side}_hem", bone, (-2.3, 4.6, -2.3), (4, 1, 4), inflate=.2)
        solid(hem, "K", "twill", 11204, 3)
    wrap = g.piece("thigh_wrap", "RIGHT_LEG", (-2.5, 1.0, -2.5), (5, 2, 5))
    for face in wrap.faces:
        fabric(face, "S", "weave", 11205, 3)
    for face in wrap.sides:
        face.set(1, 0, "S2"), face.set(3, 1, "S2")
    holster = g.piece("holster", "RIGHT_LEG", (0, 0, 0), (1, 3, 2), pivot=(-3.1, 1.2, -1.0))
    solid(holster, "L", "leather", 11206, 2)
    holster.right.set(0, 0, "M3"), holster.right.set(1, 0, "M2")
