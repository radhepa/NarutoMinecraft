"""Patchwork Haori: a hip-length haori mended so often it is more patch than coat, worn open over a
pale undershirt with wide elbow-length sleeves and a cord tied loosely across the chest."""
from kit import arm_bone, arm_x, neckline
from kit_rugged import patch
from paint import fabric, solid, strip_fabric

META = {
    "name": "Patchwork Haori",
    "gender": "unisex",
    "description": "Hip-length haori patched all over, worn open over a pale undershirt, wide sleeves, a chest cord.",
    "tags": ["shinobi", "haori", "coat", "chunin"],
    "covers_waist": True,
}

PATCHES = [("front", 0, 5, 3, 3, "S"), ("front", 5, 1, 3, 2, "A"), ("front", 6, 8, 2, 3, "L"),
           ("back", 1, 1, 3, 3, "L"), ("back", 4, 6, 3, 3, "A"), ("back", 0, 9, 2, 2, "S"),
           ("right", 1, 3, 2, 3, "A"), ("left", 1, 7, 3, 2, "S")]


def build(g):
    body, jacket = g.part("body"), g.part("jacket")
    strip_fabric(body, "S", "weave", 35170, 2)
    fabric(body.top, "S", "weave", 35170, 3)
    neckline(body.front, "round", "S")
    strip_fabric(jacket, "P", "weave", 35171, 2, 0, 11)
    fabric(jacket.top, "P", "weave", 35171, 3)
    for i, (face, x, y, w, h, role) in enumerate(PATCHES):
        patch(getattr(jacket, face), x, y, w, h, role, 35172 + i, 1 if role == "S" else 2)
    f = jacket.front
    for y in range(12):
        f.set(3, y, None), f.set(4, y, None)
    f.vline(2, 0, 11, "P0"), f.vline(5, 0, 11, "P0")
    jacket.strip.hline(0, jacket.strip.w - 1, 11, "P1")
    for side in ("right", "left"):
        arm = g.part(f"{side}_arm")
        strip_fabric(arm, "P", "weave", 35180, 2, 0, 3)
        fabric(arm.top, "P", "weave", 35180, 3)
        sleeve = g.piece(f"{side}_wide_sleeve", arm_bone(side), (arm_x(side) - .8, 1.6, -2.8), (5, 4, 6), inflate=.05)
        solid(sleeve, "P", "weave", 35181 + (side == "left"), 2)
        outer = sleeve.right if side == "right" else sleeve.left
        patch(outer, 1, 0, 3, 2, "L" if side == "right" else "S", 35183, 2)
        sleeve.bottom.fill("P0")
    cord = g.piece("chest_cord", "TORSO", (-1.5, 0, 0), (3, 1, 1), pivot=(0, 4.6, -2.9))
    for face in cord.faces:
        face.fill("A3")
    bob = g.piece("cord_knot", "TORSO", (0, 0, 0), (1, 2, 1), pivot=(.6, 4.6, -3.1), motion="flap_front")
    solid(bob, "A", "plain", 35184, 2)
