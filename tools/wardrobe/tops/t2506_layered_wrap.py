"""Layered Wrap: a genin's wrap top crossed left over right, a short pleated capelet over the left
shoulder only, layered over it like a fold of curtain, a dark sash and grey wraps on both forearms."""
from kit import arm_bone, arm_x, neckline, sleeves
from kit_tobari import pleats, plain_body, sash
from paint import solid

META = {
    "name": "Layered Wrap",
    "gender": "unisex",
    "description": "Crossed wrap top, a short pleated capelet over the left shoulder, a sash, grey forearm wraps.",
    "tags": ["shinobi", "wrap", "genin"],
}


def build(g):
    body = plain_body(g, "P", "weave", 25450)
    f = body.front
    neckline(f, "v", "P")
    for y in range(0, 9):
        f.set(min(7, 2 + y // 2 + y // 3), y, "S3")
    for arm in sleeves(g, "P", "weave", 25451, rows=(0, 5), cuff="P1"):
        for y in range(6, 11):
            for x in range(arm.strip.w):
                arm.strip.set(x, y, "S2" if (x + 2 * y) % 4 == 0 else "S3")
    cape = g.piece("capelet", arm_bone("left"), (arm_x("left") - .6, -2.7, -2.6), (5, 5, 5), inflate=.15)
    solid(cape, "D", "twill", 25453, 2)
    for face in cape.sides:
        pleats(face, "D")
    yoke = g.piece("capelet_yoke", "TORSO", (0, 0, -2.6), (4, 3, 5), pivot=(.4, -.3, 0), inflate=.3)
    solid(yoke, "D", "twill", 25454, 2)
    for face in yoke.sides:
        pleats(face, "D")
    sash(g, "sash", "D", y=9.0, knot="left")
