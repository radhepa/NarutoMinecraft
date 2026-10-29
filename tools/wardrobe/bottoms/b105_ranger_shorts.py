"""Ranger Shorts: knee-length shorts in the clan colour, cream leg wraps from the knee down, a rope
belt knotted at the hip and dark split-toe tabi boots for climbing trees."""
from paint import fabric, k, solid, strip_fabric

META = {"name": "Ranger Shorts", "gender": "unisex",
        "description": "Knee shorts, cream leg wraps, knotted rope belt, dark split-toe tabi boots.",
        "tags": ["shinobi", "genin"]}


def build(g):
    body = g.part("body")
    strip_fabric(body, "D", "twill", 1740, 2, 9, 11)
    fabric(body.bottom, "D", "twill", 1740, 1)
    for side in ("right", "left"):
        leg = g.part(f"{side}_leg")
        strip_fabric(leg, "D", "twill", 1741 + (side == "left"), 2, 0, 4)
        fabric(leg.top, "D", "twill", 1741, 2)
        leg.strip.hline(0, leg.strip.w - 1, 4, "D1")
        for y in range(5, 9):
            for x in range(leg.strip.w):
                leg.strip.set(x, y, k("S", 2 if (x + 2 * y) % 5 == 0 else 3))
        strip_fabric(leg, "K", "leather", 1743, 2, 9, 11)
        leg.strip.hline(0, leg.strip.w - 1, 9, "K3")
        leg.front.vline(1 if side == "right" else 2, 10, 11, "K0")
        leg.bottom.fill("K1")
    rope = g.piece("waist_rope", "TORSO", (-4.5, 0, -2.5), (9, 1, 5), pivot=(0, 9.4, 0), inflate=.32)
    for face in rope.faces:
        for x in range(face.w):
            for y in range(face.h):
                face.set(x, y, "L3" if (x + y) % 2 else "L2")
    for i, (x, rz) in enumerate(((-3.0, 8), (-2.2, -10))):
        end = g.piece(f"waist_rope_end_{i}", "TORSO", (0, 0, 0), (1, 3, 1), pivot=(x, 10.0, -2.9), rotation=(0, 0, rz),
                      motion="sway")
        solid(end, "L", "weave", 1744 + i, 2)
