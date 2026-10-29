"""Root Mask: a blank porcelain plate with no animal and no ears, only narrow eye slits and a thin
red line down the brow, the mark of the division that does not exist."""
from masks import plate, strap

META = {"name": "Root Mask", "gender": "unisex", "covers_face": True, "hides_hair": ["fringe"],
        "description": "Blank white mask with narrow eye slits and one thin red line on the brow."}

MASK = ["4444444444444444",
        "3333333A33333333",
        "3333333A33333333",
        "3333333A33333333",
        "3333333333333333",
        "3333333333333333",
        "33KKKK3333KKKK33",
        "3333333333333333",
        "3333333333333333",
        "3333333333333333",
        "3333333333333333",
        "3333333333333333",
        "3333333333333333",
        "2333333333333332",
        "2222222222222222"]


def build(g):
    strap(g)
    plate(g, MASK, seed=261)
