"""Short Kimono Jacket: a hip-length jacket crossed left over right with a broad contrast collar band,
wide elbow-length sleeves that swing below the arm, and a cloth obi knotted at the side."""
from kit_academy import sash
from paint import cap, fabric, k, solid, strip_fabric

META = {
    "name": "Short Kimono Jacket",
    "gender": "unisex",
    "description": "Hip-length crossed jacket with a contrast collar band, wide elbow sleeves and a knotted obi.",
    "tags": ["shinobi", "genin", "wrap"],
}


def build(g):
    body = g.part("body")
    strip_fabric(body, "P", "weave", 31060, 2)
    cap(body, "P", texture="weave", seed=31060)
    f = body.front
    # The collar band runs from the left shoulder down to the right hip, an inner layer in the V.
    for y in range(9):
        x = max(0, 6 - y * 6 // 8)
        f.set(x, y, "S3")
        if x + 1 <= 7:
            f.set(x + 1, y, "S2")
        if x - 1 >= 0:
            f.set(x - 1, y, "P1")
    f.set(2, 0, "S3"), f.set(2, 1, "S2"), f.set(3, 1, "S1")
    for x in (3, 4, 5):
        f.set(x, 0, "K2")
    f.set(4, 1, "K2")
    body.back.hline(1, 6, 0, "S3")
    for face in (body.right, body.left):
        face.vline(2, 1, 11, "P1")
    for side in ("right", "left"):
        arm = g.part(f"{side}_arm")
        strip_fabric(arm, "P", "weave", 31061 + (side == "left"), 2, 0, 3)
        fabric(arm.top, "P", "weave", 31061, 3)
        # The wide sleeve: an open-ended box hanging round the upper arm, deeper below than above.
        x = -3.6 if side == "right" else -1.4
        sleeve = g.piece(f"{side}_kimono_sleeve", "RIGHT_ARM" if side == "right" else "LEFT_ARM",
                         (x, -2.4, -2.9), (5, 6, 6))
        solid(sleeve, "P", "weave", 31063 + (side == "left"), 2)
        for face in sleeve.sides:
            face.hline(0, face.w - 1, 5, "S3")
            face.vline(face.w - 1, 0, 4, k("P", 1))
        sleeve.bottom.fill("P0")
    sash(g, "A", 31066, y=8.6, knot_x=-2.8, tails=2)
