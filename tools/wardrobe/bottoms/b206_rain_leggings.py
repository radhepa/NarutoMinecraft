"""Rain Leggings: snug dark leggings with plated shin guards strapped over them, a seal tag tucked
into the right thigh strap and open-toe sandals."""
from kit_shinobi import sandals
from paint import fabric, solid, strip_fabric

META = {"name": "Rain Leggings", "gender": "unisex",
        "description": "Snug dark leggings, strapped shin guards, a seal tag in the thigh strap, sandals.",
        "tags": ["shinobi"]}


def build(g):
    body = g.part("body")
    strip_fabric(body, "K", "rib", 2450, 2, 9, 11)
    fabric(body.bottom, "K", "rib", 2450, 1)
    for side in ("right", "left"):
        leg = g.part(f"{side}_leg")
        strip_fabric(leg, "K", "rib", 2451, 2, 0, 9)
        fabric(leg.top, "K", "rib", 2451, 2)
    sandals(g)
    for side, bone in (("right", "RIGHT_LEG"), ("left", "LEFT_LEG")):
        guard = g.piece(f"{side}_guard", bone, (-1.5, 5.4, -2.6), (3, 3, 1))
        solid(guard, "M", "plain", 2452, 3)
        guard.front.hline(0, 2, 0, "M4"), guard.front.vline(1, 1, 2, "M1")
        for y in (5.6, 8.0):
            strap = g.piece(f"{side}_strap_{int(y)}", bone, (-2.4, y, -2.4), (5, 1, 5))
            solid(strap, "L", "leather", 2453, 2, edge=False)
    strap = g.piece("thigh_strap", "RIGHT_LEG", (-2.45, 1.0, -2.45), (5, 1, 5))
    solid(strap, "L", "leather", 2454, 2, edge=False)
    tag = g.piece("thigh_tag", "RIGHT_LEG", (0, 0, 0), (1, 3, 1), pivot=(-3.0, 1.2, -1.5))
    solid(tag, "S", "plain", 2455, 3, edge=False)
    tag.right.set(0, 1, "K1"), tag.right.set(0, 2, "A2")
