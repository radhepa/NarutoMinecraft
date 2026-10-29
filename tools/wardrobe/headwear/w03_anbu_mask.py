"""ANBU Mask: a white porcelain animal mask with red markings and narrow eye slits, small pointed
ears over the brow and a black strap around the head. It covers the whole face."""
from glyphs import stamp
from paint import fabric, solid

META = {"name": "ANBU Mask", "gender": "unisex", "covers_face": True,
        "description": "White porcelain animal mask with red markings, eye slits and pointed ears."}

# Double resolution, 16 x 15 texels over the 8 x 7.5 face.
MASK = ["4444444444444444",
        "333333AAAA333333",
        "3333333AA3333333",
        "3333333AA3333333",
        "3333333333333333",
        "3AA3333333333AA3",
        "3KKA33333333AKK3",
        "33KKK333333KKK33",
        "3333KK3333KK3333",
        "3333333333333333",
        "3A3A33333333A3A3",
        "3A3A33333333A3A3",
        "3333333333333333",
        "2333333333333332",
        "2222222222222222"]
SNOUT = ["3KK3",
         "3333",
         "2332"]


def build(g):
    strap = g.piece("strap", "HEAD", (-4, -5.4, -4), (8, 1, 8), inflate=.55)
    solid(strap, "K", "smooth", 171, 2, edge=False)
    face = g.piece("mask", "HEAD", (-8, 0, -1), (16, 15, 1), pivot=(0, -7.6, -4.3), scale=(.5, .5, .5))
    for f in face.faces:
        fabric(f, "S", "plain", 172, 2)
    stamp(face.front, MASK, 0, 0, {"4": "S4", "3": "S3", "2": "S2", "A": "A2", "K": "K0"})
    snout = g.piece("snout", "HEAD", (-2, 0, -2), (4, 3, 2), pivot=(0, -2.6, -4.8), scale=(.5, .5, .5))
    solid(snout, "S", "plain", 173, 3)
    stamp(snout.front, SNOUT, 0, 0, {"3": "S3", "2": "S2", "K": "K0"})
    for side, sign in (("right", -1), ("left", 1)):
        ear = g.piece(f"ear_{side}", "HEAD", (-1.5, -3, -1), (3, 3, 2), pivot=(2.6 * sign, -7.6, -4.4),
                      rotation=(0, 0, 14 * sign), scale=(.5, .5, .5))
        solid(ear, "S", "plain", 174, 3)
        stamp(ear.front, ["S3S", "3A3", "AAA"], 0, 0, {"S": "S3", "3": "S3", "A": "A2"})
