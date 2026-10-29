"""Night Trousers: close black trousers for the night watch, steel-capped knee guards, white shin
wraps, a holster on the left thigh and navy open-toe sandals."""
from kit_shinobi import sandals, wraps
from paint import fabric, solid, strip_fabric

META = {"name": "Night Trousers", "gender": "unisex",
        "description": "Close black trousers, steel knee guards, white shin wraps, a left thigh holster, navy sandals.",
        "tags": ["shinobi"]}


def build(g):
    body = g.part("body")
    strip_fabric(body, "K", "twill", 11401, 3, 9, 11)
    body.strip.hline(0, body.strip.w - 1, 9, "K2")
    fabric(body.bottom, "K", "twill", 11401, 2)
    for side in ("right", "left"):
        leg = g.part(f"{side}_leg")
        strip_fabric(leg, "K", "twill", 11402 + (side == "left"), 3, 0, 6)
        fabric(leg.top, "K", "twill", 11402, 3)
        leg.front.vline(1 if side == "right" else 2, 1, 5, "K4")
    wraps(g, 7, 9)
    sandals(g)
    for side, bone in (("right", "RIGHT_LEG"), ("left", "LEFT_LEG")):
        guard = g.piece(f"{side}_knee_guard", bone, (-1.5, 5.2, -2.6), (3, 2, 1))
        solid(guard, "M", "plain", 11404, 1)
        guard.front.hline(0, 2, 0, "M2"), guard.front.set(1, 1, "M0")
    holster = g.piece("holster", "LEFT_LEG", (0, 0, 0), (1, 3, 2), pivot=(2.1, 1.2, -1.0))
    solid(holster, "L", "leather", 11405, 2)
    holster.left.set(0, 0, "M3"), holster.left.set(1, 0, "M2")
    strap = g.piece("holster_strap", "LEFT_LEG", (-2.45, 1.4, -2.45), (5, 1, 5))
    solid(strap, "L", "leather", 11406, 2, edge=False)
