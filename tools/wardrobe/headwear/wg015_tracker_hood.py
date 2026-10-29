"""Tracker Hood: the tracking unit's soft hood pulled up over the head, its opening drawn back
clear of the face so nothing narrows the eyes, the point hanging down behind."""
from paint import fabric, k, solid

META = {"name": "Tracker Hood", "gender": "unisex", "hides_hair": ["*"],
        "description": "A soft hood pulled up over the head, its opening clear of the face, the point behind."}


def build(g):
    top = g.piece("hood_top", "HEAD", (-4.5, -9.4, -4.4), (9, 1, 10), inflate=.1)
    solid(top, "P", "twill", 34980, 2, edge=False)
    fabric(top.top, "P", "twill", 34980, 3)
    top.front.fill(k("P", 3))
    crown = g.piece("hood_crown", "HEAD", (-3, -10.1, -2.6), (6, 1, 7))
    solid(crown, "P", "twill", 34981, 3, edge=False)
    for side, x in (("right", -5.5), ("left", 4.5)):
        wall = g.piece(f"hood_{side}", "HEAD", (x, -9, -4.4), (1, 9, 10), inflate=.1)
        solid(wall, "P", "twill", 34982 + (x > 0), 2)
        outer = wall.right if x < 0 else wall.left
        for xx in range(2, outer.w - 1, 3):
            outer.vline(xx, 1, outer.h - 1, k("P", 1))
        (wall.left if x < 0 else wall.right).fill(k("P", 0))
        wall.front.fill(k("P", 3))
    back = g.piece("hood_back", "HEAD", (-5.5, -9, 4.6), (11, 9, 1), inflate=.1)
    solid(back, "P", "twill", 34984, 2)
    back.back.vline(5, 1, 8, k("P", 1))
    point = g.piece("hood_point", "HEAD", (-1.5, 0, 0), (3, 4, 1), pivot=(0, -.4, 5.0), rotation=(16, 0, 0), motion="sway")
    solid(point, "P", "twill", 34985, 2)
