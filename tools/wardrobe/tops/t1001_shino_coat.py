"""Shino Coat: Shino's Part I jacket, grey-green and long-sleeved, zipped to a stiff standing collar
that rises past the chin to the nose, so nothing of the face shows but the lenses above it."""
from kit_aburame import BEETLE, glyph, high_collar
from paint import cap, fabric, k, solid, strip_fabric

META = {
    "name": "Shino Coat",
    "gender": "unisex",
    "description": "Grey-green long-sleeved jacket zipped to a standing collar that hides the mouth.",
    "tags": ["shinobi", "aburame", "coat"],
}


def build(g):
    body, jacket = g.part("body"), g.part("jacket")
    strip_fabric(body, "P", "smooth", 10501, 2)
    cap(body, "P", seed=10501)
    strip_fabric(jacket, "P", "smooth", 10502, 2)
    cap(jacket, "P", seed=10502)
    f = jacket.front
    f.vline(3, 0, 11, "P1"), f.vline(4, 0, 11, "M3")
    for face in jacket.sides:
        face.hline(0, face.w - 1, 10, k("P", 3)), face.hline(0, face.w - 1, 11, k("P", 1))
    # Two pockets low on the front, a seam from each shoulder.
    for x0 in (0, 5):
        f.hline(x0 + 1, x0 + 2, 7, "P3"), f.vline(x0 + (0 if x0 else 3), 7, 9, "P1")
    jacket.back.vline(2, 0, 9, "P1"), jacket.back.vline(5, 0, 9, "P1")
    # Long sleeves with a turned-back cuff.
    for side in ("right", "left"):
        arm, sleeve = g.part(f"{side}_arm"), g.part(f"{side}_sleeve")
        strip_fabric(arm, "P", "smooth", 10503, 2, 0, 11)
        fabric(arm.top, "P", "smooth", 10503, 3)
        strip_fabric(sleeve, "P", "smooth", 10504 + (side == "left"), 2, 0, 10)
        fabric(sleeve.top, "P", "smooth", 10504, 3)
        sleeve.strip.hline(0, sleeve.strip.w - 1, 9, "P3"), sleeve.strip.hline(0, sleeve.strip.w - 1, 10, "P1")
        outer = sleeve.right if side == "right" else sleeve.left
        outer.vline(2, 1, 8, "P1")
    high_collar(g, "P", "smooth", 10510)
    # The kikaichu stitched small on the left breast.
    badge = g.piece("beetle_badge", "TORSO", (0, 0, 0), (8, 8, 1), pivot=(1.1, 2.4, -2.8), scale=(.3, .3, .3))
    for face in badge.faces:
        fabric(face, "P", "smooth", 10520, 2)
    glyph(badge.front, BEETLE, 0, 0, {"#": "A2", "+": "A0"})
