"""ANBU Hawk Mask: a porcelain hawk with a hooked beak, heavy rust-colored brows and feather marks
sweeping back from wide eye slits and a crest stripe down the brow. Covers the face."""
from masks import beak, plate, strap

META = {"name": "ANBU Hawk Mask", "gender": "unisex", "covers_face": True, "hides_hair": ["fringe"],
        "description": "White hawk mask with a hooked beak, rust brows and feather marks."}

MASK = ["4444444444444444",
        "3333333AA3333333",
        "3333333AA3333333",
        "3333333AA3333333",
        "AAAAA333333AAAAA",
        "3AAAA333333AAAA3",
        "3KKKK333333KKKK3",
        "A3KKK333333KKK3A",
        "AA333333333333AA",
        "3AA3333333333AA3",
        "33AA33333333AA33",
        "3333333333333333",
        "3333333333333333",
        "2333333333333332",
        "2222222222222222"]


def build(g):
    strap(g)
    plate(g, MASK, seed=241)
    beak(g)
