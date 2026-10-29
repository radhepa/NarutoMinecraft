"""ANBU Wolf Mask: a porcelain wolf with a long muzzle, tall upright ears and blue markings over the
brows and down the cheeks. It covers the face and tucks the fringe under the strap."""
from masks import bump, ears, plate, strap

META = {"name": "ANBU Wolf Mask", "gender": "unisex", "covers_face": True, "hides_hair": ["fringe"],
        "description": "White wolf mask with a long muzzle, tall ears and blue brow and cheek markings."}

MASK = ["4444444444444444",
        "3333333333333333",
        "33AA33333333AA33",
        "333AA333333AA333",
        "3333AA3333AA3333",
        "3333333333333333",
        "3KKK33333333KKK3",
        "33KKK333333KKK33",
        "3333333333333333",
        "3A333333333333A3",
        "3AA3333333333AA3",
        "33AA33333333AA33",
        "3333333333333333",
        "2333333333333332",
        "2222222222222222"]
MUZZLE = ["33KK33",
          "333333",
          "3A33A3",
          "222222"]


def build(g):
    strap(g)
    plate(g, MASK, seed=211)
    muzzle = bump(g, "muzzle", MUZZLE, (6, 4, 6), (0, -3.6, -6.3), seed=212)
    muzzle.top.vline(2, 1, 5, "A2"), muzzle.top.vline(3, 1, 5, "A2")
    muzzle.top.hline(1, 4, 0, "K0")   # the nose at the tip
    ears(g, ((4, 2), (3, 2), (2, 1), (1, 1)), x=2.6, tilt=4, inner="A2")
