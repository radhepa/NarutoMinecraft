"""Carpenter's Banten: the builder's dark hanten jacket, the collar bands lettered in white, a band
of stripes round the hem and the guild mark large on the back, closed with a sash, the steel
carpenter's square tucked in at the back."""
from kit import flaps
from kit_market import mark, sash, sleeves, stripes
from paint import cap, k, solid, strip_fabric

META = {
    "name": "Carpenter's Banten",
    "gender": "unisex",
    "description": "Dark hanten with lettered white collar bands, striped hem, a guild mark on the back and a carpenter's square.",
    "tags": ["civilian", "jacket", "work", "wrap"],
    "covers_waist": True,
}


def build(g):
    body = g.part("body")
    strip_fabric(body, "D", "twill", 36160, 2)
    cap(body, "D", texture="twill", seed=36160)
    f = body.front
    for i in range(9):
        x = min(7, 1 + i * 2 // 3)
        f.set(x, i, "S3"), f.set(min(7, x + 1), i, "S3")
        if i % 2:
            f.set(x, i, "K2")
    f.set(6, 0, "S3"), f.set(7, 0, "S3")
    mark(body.back, "kagi", 1, 1, "S3")
    sleeves(g, "D", "twill", 36161, rows=(0, 10))
    for face in flaps(g, "banten_hem", 3, "D", "twill", 36163, width=9, top=11.0, front_z=-3.0, back_z=2.0):
        stripes(face, "S3", 1, vertical=False, rows=[1])
        face.hline(0, 8, 2, k("D", 1))
    sash(g, "sash", "S", 36165, y=8.6, height=1, base=2, knot="back")
    blade = g.piece("square_long", "TORSO", (-.5, 0, -.5), (1, 7, 1), pivot=(2.6, 5.0, 2.7), rotation=(0, 0, 10),
                    scale=(.6, 1, .6))
    solid(blade, "M", "smooth", 36166, 3, edge=False)
    foot = g.piece("square_short", "TORSO", (0, -.5, -.5), (3, 1, 1), pivot=(3.8, 11.8, 2.7), rotation=(0, 0, 10),
                   scale=(1, .6, .6))
    solid(foot, "M", "smooth", 36167, 3, edge=False)
