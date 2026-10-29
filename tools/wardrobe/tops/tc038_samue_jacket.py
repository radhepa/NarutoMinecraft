"""Samue Jacket: the work jacket of potters, carpenters and temple caretakers, sturdy cotton crossed
over and tied at the side, a breast pocket for a pencil, long sleeves gathered into a band at the
wrist and a slit at each hip."""
from kit_household import arm_cloth, overlap
from paint import cap, solid, strip_fabric

META = {
    "name": "Samue Jacket",
    "gender": "unisex",
    "description": "Crossed cotton work jacket tied at the side, breast pocket with a pencil, banded wrists.",
    "tags": ["civilian", "work", "wrap"],
}


def build(g):
    body = g.part("body")
    strip_fabric(body, "P", "twill", 37240, 2)
    cap(body, "P", texture="twill", seed=37240)
    f = body.front
    overlap(f, "P3", "P0", rows=12)
    f.rect(5, 3, 2, 2, "P3"), f.hline(5, 6, 3, "P1"), f.set(6, 2, "L3"), f.set(6, 1, "K2")
    for face in (body.right, body.left):
        face.vline(1, 9, 11, "P0")
    body.strip.hline(0, body.strip.w - 1, 11, "P1")
    for arm in arm_cloth(g, "P", "twill", 37241, rows=(0, 9)):
        arm.strip.hline(0, arm.strip.w - 1, 9, "P1")
    for i, y in enumerate((4.6, 8.0)):
        tie = g.piece(f"tie_{i}", "TORSO", (-.5, 0, -.5), (1, 2, 1), pivot=(-3.0, y, -2.75), rotation=(0, 0, 10),
                      motion="sway")
        solid(tie, "P", "twill", 37244 + i, 1)
