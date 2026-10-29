"""Bandaged Combat Wrap: a sleeveless crossed wrap top, the right arm bandaged from shoulder to
knuckles, a single padded guard on the left shoulder, a broad dark sash and a tanto at the back."""
from kit_field import shirt
from kit_shinobi import bandage, tanto
from paint import k, solid

META = {
    "name": "Bandaged Combat Wrap",
    "gender": "unisex",
    "description": "Sleeveless crossed wrap top, a bandaged right arm, one shoulder guard, a dark sash and a tanto.",
    "tags": ["shinobi", "wrap", "jonin"],
}


def build(g):
    body = shirt(g, "P", 32380, sleeve=-1, texture="twill")
    f = body.front
    for y in range(8):
        x = 6 - y * 5 // 7
        f.set(x, y, "P0"), f.set(max(0, x - 1), y, "P3")
    for face in (body.front, body.back, body.right, body.left):
        face.hline(0, face.w - 1, 0, "P3")
    right = g.part("right_arm")
    bandage(right.strip, 0, 0, right.strip.w - 1, 10)
    bandage(right.top, 0, 0, 3, 3)
    guard = g.piece("left_shoulder_guard", "LEFT_ARM", (-1.6, -2.8, -2.6), (5, 4, 5), rotation=(0, 0, -8))
    solid(guard, "D", "smooth", 32382, 2)
    for face in guard.sides:
        face.hline(0, face.w - 1, 0, k("D", 3)), face.hline(0, face.w - 1, 2, k("D", 1))
    sash = g.piece("sash", "TORSO", (-4.5, 0, -2.5), (9, 3, 5), pivot=(0, 8.6, 0), inflate=.18)
    solid(sash, "D", "weave", 32383, 2, edge=False)
    for face in sash.sides:
        face.hline(0, face.w - 1, 0, k("D", 3))
    tanto(g, "tanto", pivot=(-3.0, 9.0, 2.7), rotation=(0, 0, -76), length=7)
