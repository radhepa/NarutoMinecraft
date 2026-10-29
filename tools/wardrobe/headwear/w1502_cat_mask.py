"""Cat Mask: Yugao Uzuki's ANBU mask worn without a hood, white porcelain with a red stripe down the
brow and one across each cheek, almond eye slits, small ears, on a black strap, so the long hair
falls free behind it."""
from masks import ears, plate, strap

META = {"name": "Cat Mask", "gender": "unisex", "covers_face": True,
        "description": "White porcelain cat mask with three red stripes and almond slits, worn without a hood."}

MASK = ["4444444444444444",
        "3333333AA3333333",
        "3333333AA3333333",
        "3333333AA3333333",
        "3333333333333333",
        "3333333333333333",
        "33KKK333333KKK33",
        "333KKK3333KKK333",
        "3333333333333333",
        "3333333aa3333333",
        "AAAA33333333AAAA",
        "3333333333333333",
        "3333333333333333",
        "2333333333333332",
        "2222222222222222"]


def build(g):
    strap(g)
    plate(g, MASK, seed=15620)
    ears(g, ((4, 2), (2, 1), (1, 1)), x=2.8, tilt=10)
