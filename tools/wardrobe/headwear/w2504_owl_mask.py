"""ANBU Owl Mask: the night squads' porcelain owl, wide round eye discs ringed in amber like two
lanterns, a small hooked beak between them, short feathered ear tufts and grey brow feathers, worn
on a black strap."""
from masks import bump, ears, plate, strap

META = {"name": "ANBU Owl Mask", "gender": "unisex", "covers_face": True,
        "description": "White porcelain owl mask: amber-ringed round eye discs, a small hooked beak, short ear tufts."}

MASK = ["4444444444444444",
        "3223333333333223",
        "3332233333322333",
        "33aaaa3333aaaa33",
        "3a3333a33a3333a3",
        "a333333aa333333a",
        "a33KK333333KK33a",
        "a33KK333333KK33a",
        "a333333aa333333a",
        "3a3333a33a3333a3",
        "33aaaa3333aaaa33",
        "3333333333333333",
        "3332333333332333",
        "2333333333333332",
        "2222222222222222"]


def build(g):
    strap(g)
    plate(g, MASK, seed=25860)
    ears(g, ((3, 2), (2, 1), (1, 1)), x=3.0, tilt=22, inner=None, prefix="tuft")
    beak = bump(g, "beak", None, (2, 3, 2), (0, -3.6, -4.5), rotation=(-10, 0, 0), seed=25861)
    beak.front.hline(0, 1, 2, "S1"), beak.bottom.fill("K1")
