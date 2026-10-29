"""ANBU Fox Mask: a white porcelain fox mask with red markings and narrow eye slits, small pointed
ears over the brow and a black strap around the head. It covers the whole face."""
from masks import bump, ears, plate, strap

META = {"name": "ANBU Fox Mask", "gender": "unisex", "covers_face": True,
        "description": "White porcelain fox mask with red markings, eye slits and pointed ears."}

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
    strap(g)
    plate(g, MASK)
    bump(g, "snout", SNOUT, (4, 3, 2), (0, -2.6, -4.8))
    ears(g, ((3, 2), (1, 1)))
