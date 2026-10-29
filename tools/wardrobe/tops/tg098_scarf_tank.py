"""Long-Scarf Tank: a fitted sleeveless top under a long scarf wound once round the neck, its two
tails streaming down the back to the knees; leather wristbands and bandaged hands. A runner's outfit
for genin who move faster than their teammates."""
from kit import neckline
from kit_shinobi import bandage
from paint import fabric, k, solid, strip_fabric

META = {
    "name": "Long-Scarf Tank",
    "gender": "unisex",
    "description": "Fitted sleeveless top, a long scarf with two tails streaming to the knees, wristbands, wrapped hands.",
    "tags": ["shinobi", "genin"],
}


def build(g):
    body = g.part("body")
    strip_fabric(body, "P", "rib", 35185, 2, 0, 10)
    fabric(body.top, "P", "rib", 35185, 3)
    neckline(body.front, "square", "P")
    for face in (body.right, body.left):
        face.vline(0, 0, 10, "P1")
    body.strip.hline(0, body.strip.w - 1, 10, "P1")
    for side in ("right", "left"):
        arm = g.part(f"{side}_arm")
        strip_fabric(arm, "L", "leather", 35186, 2, 7, 8)
        arm.strip.hline(0, arm.strip.w - 1, 7, "L3")
        bandage(arm.strip, 0, 9, arm.strip.w - 1, 11)
        bandage(arm.bottom, 0, 0, arm.bottom.w - 1, arm.bottom.h - 1)
    ring = g.piece("scarf_ring", "TORSO", (-5, -.6, -3), (10, 2, 6), inflate=.05)
    solid(ring, "A", "knit", 35187, 2)
    for face in ring.sides:
        face.hline(0, face.w - 1, 0, k("A", 3))
    for i, (x, rz, n) in enumerate(((-1.2, 10, 15), (1.0, -6, 13))):
        tail = g.piece(f"scarf_tail_{i}", "TORSO", (-1, 0, 0), (2, n, 1), pivot=(x, 0.6, 3.1 + .1 * i),
                       rotation=(14 + 4 * i, 0, rz), motion="flap_back")
        solid(tail, "A", "knit", 35188 + i, 2)
        tail.back.hline(0, 1, n - 1, "A0"), tail.back.hline(0, 1, n - 3, "A3")
