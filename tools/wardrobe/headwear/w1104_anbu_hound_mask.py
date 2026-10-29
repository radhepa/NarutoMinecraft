"""ANBU Hound Mask: Kakashi's mask from his ANBU years, a white hound with short pricked ears, a
blunt muzzle with a black nose, and red markings sweeping up over the eyes and down the cheeks."""
from masks import bump, ears, plate, strap

META = {"name": "ANBU Hound Mask", "gender": "unisex", "covers_face": True, "hides_hair": ["fringe"],
        "description": "White hound mask, short pricked ears, a blunt muzzle and red sweeping markings."}

MASK = ["4444444444444444",
        "3A33333333333A33",
        "3AA333333333AA33",
        "33AA3333333AA333",
        "333AA33333AA3333",
        "3333333333333333",
        "33KKK333333KKK33",
        "33KKKK3333KKKK33",
        "3333333333333333",
        "3AA3333333333AA3",
        "33A3333333333A33",
        "33AA33333333AA33",
        "3333333333333333",
        "2333333333333332",
        "2222222222222222"]
MUZZLE = ["3KKKK3",
          "33KK33",
          "3A33A3",
          "222222"]


def build(g):
    strap(g)
    plate(g, MASK, seed=11991)
    muzzle = bump(g, "muzzle", MUZZLE, (6, 4, 4), (0, -3.4, -5.6), seed=11992)
    muzzle.top.hline(1, 4, 0, "K0")
    ears(g, ((4, 2), (3, 1), (2, 1)), x=2.8, tilt=18, inner="A2")
