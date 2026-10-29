"""Fur Wrap Shorts: hard-wearing knee shorts with a rough fur wrap bound round each calf like a
hunter's gaiters, bare knees, open-toe sandals and a pouch at the back of the belt."""
from kit_inuzuka import fur_box
from kit_shinobi import sandals
from paint import fabric, solid, strip_fabric

META = {"name": "Fur Wrap Shorts", "gender": "unisex",
        "description": "Knee shorts, fur wraps bound round the calves, bare knees, sandals, a belt pouch.",
        "tags": ["shinobi"]}


def build(g):
    body = g.part("body")
    strip_fabric(body, "L", "leather", 8840, 2, 9, 11)
    body.strip.hline(0, body.strip.w - 1, 9, "L3")
    fabric(body.bottom, "L", "leather", 8840, 1)
    for side in ("right", "left"):
        leg = g.part(f"{side}_leg")
        strip_fabric(leg, "L", "leather", 8841 + (side == "left"), 2, 0, 3)
        fabric(leg.top, "L", "leather", 8841, 2)
        leg.strip.hline(0, leg.strip.w - 1, 3, "L1")
    sandals(g)
    for side, bone in (("right", "RIGHT_LEG"), ("left", "LEFT_LEG")):
        wrap = g.piece(f"{side}_fur_wrap", bone, (-2.5, 6.0, -2.5), (5, 3, 5))
        fur_box(wrap, "S", 8843 + (side == "left"), 2)
        for face in wrap.sides:
            face.hline(0, face.w - 1, 1, "K2")
    pouch = g.piece("waist_pouch", "TORSO", (0, 0, 0), (3, 2, 1), pivot=(-1.5, 9.4, 2.2))
    solid(pouch, "K", "leather", 8846, 2)
    pouch.back.hline(0, 2, 0, "K3")
