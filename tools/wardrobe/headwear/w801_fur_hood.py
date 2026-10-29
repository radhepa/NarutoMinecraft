"""Fur Hood: the jacket's hood pulled up over the head, cloth over the crown and down the back of the
neck, a thick ruff of pale fur round the face opening; hides the hair beneath."""
from kit_inuzuka import fur_box
from paint import fabric, solid

META = {"name": "Fur Hood", "gender": "unisex", "hides_hair": ["*"],
        "description": "A hood pulled up over the head with a thick ruff of fur round the face."}


def build(g):
    # Open at the face: a crown, a back and two sides that stop short of the brow line.
    crown = g.piece("hood_crown", "HEAD", (-4, -8, -4), (8, 2, 8), inflate=.75)
    solid(crown, "P", "plain", 8900, 2, edge=False)
    fabric(crown.top, "P", "plain", 8900, 3)
    back = g.piece("hood_back", "HEAD", (-4, -6, 3), (8, 8, 1), inflate=.75)
    solid(back, "P", "plain", 8901, 2)
    back.back.vline(3, 0, 7, "P1")
    for side, x in (("right", -4), ("left", 3)):
        panel = g.piece(f"hood_{side}", "HEAD", (x, -6, -2.4), (1, 8, 6), inflate=.75)
        solid(panel, "P", "plain", 8907 + (side == "left"), 2)
    # The fur ruff framing the face: a brow band and two cheek bands, open over the eyes and mouth.
    brow = g.piece("ruff_brow", "HEAD", (-5, -9.2, -5.2), (10, 2, 2))
    fur_box(brow, "S", 8902, 2)
    for side, x in (("right", -5.8), ("left", 3.8)):
        cheek = g.piece(f"ruff_{side}", "HEAD", (0, -7.6, -5.2), (2, 8, 2), pivot=(x, 0, 0))
        fur_box(cheek, "S", 8904 + (side == "left"), 2)
    chin = g.piece("ruff_chin", "HEAD", (-5, .2, -4.6), (10, 1, 2))
    fur_box(chin, "S", 8906, 2)
