"""Wanderer's Tunic: a hip-length homespun tunic slit at the sides, sleeves rolled to the elbow, a
twisted rope belt knotted at the hip and darned patches on the chest and back: the clothes of a
shinobi who has been walking a long time."""
from kit import neckline, roll
from kit_rugged import patch, rope
from paint import fabric, strip_fabric

META = {
    "name": "Wanderer's Tunic",
    "gender": "unisex",
    "description": "Hip-length homespun tunic slit at the sides, rolled sleeves, a rope belt, darned patches.",
    "tags": ["shinobi", "genin", "tunic"],
    "covers_waist": True,
}


def build(g):
    body, jacket = g.part("body"), g.part("jacket")
    strip_fabric(body, "P", "tweed", 35120, 2)
    fabric(body.top, "P", "tweed", 35120, 3)
    neckline(body.front, "laced", "P")
    strip_fabric(jacket, "P", "tweed", 35121, 2, 9, 11)
    jacket.strip.hline(0, jacket.strip.w - 1, 11, "P1")
    for face in (jacket.right, jacket.left):
        face.vline(face.w // 2, 9, 11, None)
        face.vline(face.w // 2 - 1, 9, 11, "P0")
    patch(body.front, 4, 3, 3, 3, "S", 35122, 1)
    patch(body.back, 1, 5, 3, 2, "L", 35123)
    for side in ("right", "left"):
        arm = g.part(f"{side}_arm")
        strip_fabric(arm, "P", "tweed", 35124, 2, 0, 3)
        fabric(arm.top, "P", "tweed", 35124, 3)
    roll(g, "P", 1.4, base=2)
    rope(g, "rope_belt", y=8.8, role="S", base=2)
