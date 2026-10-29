"""Evening Yukata: a summer yukata for a quiet evening on the porch, wrapped left over right, wide
sleeves, a narrow obi, and a scatter of deer-antler sprigs dyed into the cloth."""
from kit import belt
from paint import cap, fabric, solid, strip_fabric

META = {
    "name": "Evening Yukata",
    "gender": "unisex",
    "description": "Summer yukata wrapped left over right, wide sleeves, narrow obi, antler-sprig print.",
    "tags": ["nara", "robe"],
    "covers_waist": True,
    "locked_to": "b505_yukata_hem",
}

SPRIGS = [(1, 3), (5, 6), (2, 9), (6, 1)]


def sprig(face, x, y):
    face.set(x, y, "A2"), face.set(x - 1, y - 1, "A2"), face.set(x + 1, y - 1, "A2")


def build(g):
    body = g.part("body")
    strip_fabric(body, "P", "weave", 5591, 2)
    cap(body, "P", seed=5591)
    for face in body.sides:
        for x, y in SPRIGS:
            if x + 1 < face.w:
                sprig(face, x, y)
    f = body.front
    for y in range(8):
        f.set(min(7, y + 1), y, "P0"), f.set(y, y, "S3") if y < 7 else None
    belt(g, "obi", y=7.6, role="K", height=2, buckle=None, inflate=.12)
    for side, bone in (("right", "RIGHT_ARM"), ("left", "LEFT_ARM")):
        arm = g.part(f"{side}_arm")
        strip_fabric(arm, "P", "weave", 5592 + (side == "left"), 2, 0, 6)
        fabric(arm.top, "P", "weave", 5592, 3)
        x0 = -3.0 if side == "right" else -1.0
        sleeve = g.piece(f"{side}_wide_sleeve", bone, (x0 - .5, 2.5, -2.5), (5, 6, 5), inflate=.05)
        solid(sleeve, "P", "weave", 5594 + (side == "left"), 2)
        for face in sleeve.sides:
            sprig(face, 2, 3)
        sleeve.bottom.fill("P0")
