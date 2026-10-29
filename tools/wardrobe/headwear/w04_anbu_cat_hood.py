"""ANBU Cat Hood: a deep grey hood pulled forward over a porcelain cat mask with violet stripes,
almond eye slits, whiskers and tall pointed ears. Hides all hair and the face."""
from masks import ears, plate
from paint import fabric, k, solid

META = {"name": "ANBU Cat Hood", "gender": "unisex", "covers_face": True, "hides_hair": ["*"],
        "description": "Grey hood over a white cat mask with violet stripes, whiskers and tall ears."}

MASK = ["4444444444444444",
        "3333A33AA33A3333",
        "3333A33AA33A3333",
        "3333333333333333",
        "3333333333333333",
        "3333333333333333",
        "3AKK33333333KKA3",
        "33AKKK3333KKKA33",
        "3333KK3333KK3333",
        "3333333AA3333333",
        "AAA3333333333AAA",
        "333333A33A333333",
        "AAA3333333333AAA",
        "2333333333333332",
        "2222222222222222"]

FRONT_Z = -3.8   # the hood's opening sits just behind the mask


def hood_cloth(face, seed, base=2):
    fabric(face, "L", "twill", seed, base)
    for x in range(2, face.w - 1, 4):
        face.vline(x, 1, face.h - 1, k("L", base - 1))


def build(g):
    # Three slabs and a stepped crown, so the hood reads round rather than as a box.
    top = g.piece("hood_top", "HEAD", (-4.5, -10, FRONT_Z), (9, 1, 10))
    solid(top, "L", "twill", 191, 2, edge=False)
    fabric(top.top, "L", "twill", 191, 3)
    top.front.fill("L3")
    for side, x in (("right", -5.6), ("left", 4.6)):
        wall = g.piece(f"hood_{side}", "HEAD", (x, -9, FRONT_Z), (1, 10, 9))
        solid(wall, "L", "twill", 192 + (x > 0), 2)
        hood_cloth(wall.right if x < 0 else wall.left, 194 + (x > 0))
        (wall.left if x < 0 else wall.right).fill("L0")   # the shadowed inside
        wall.front.fill("L3")
    back = g.piece("hood_back", "HEAD", (-5.5, -9, 5), (11, 10, 1), inflate=.1)
    solid(back, "L", "twill", 196, 2)
    hood_cloth(back.back, 197)
    plate(g, MASK, seed=198)
    ears(g, ((4, 2), (3, 1), (2, 1), (1, 1)), x=2.4, tilt=10, inner="A2")
