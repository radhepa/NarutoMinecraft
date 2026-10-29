"""Scout Hood: the hooded mantle's hood pulled up for a night patrol, close over the brow and down
past the cheeks, with a dark muffler drawn up over the mouth beneath it so only the eyes show."""
from paint import fabric, k, solid

META = {"name": "Scout Hood", "gender": "unisex", "covers_mouth": True, "hides_hair": ["*"],
        "description": "A close hood pulled up over the brow and a dark muffler over the mouth, only the eyes showing."}

FRONT_Z = -4.7


def hood_cloth(face, seed, base=2):
    fabric(face, "P", "twill", seed, base)
    for x in range(2, face.w - 1, 3):
        face.vline(x, 1, face.h - 1, k("P", base - 1))


def build(g):
    top = g.piece("hood_top", "HEAD", (-4.5, -9.4, FRONT_Z), (9, 1, 10))
    solid(top, "P", "twill", 25820, 2, edge=False)
    top.front.fill("P3")
    crown = g.piece("hood_crown", "HEAD", (-3, -10.2, FRONT_Z + 2), (6, 1, 7))
    solid(crown, "P", "twill", 25821, 2, edge=False)
    for side, x in (("right", -5.5), ("left", 4.5)):
        wall = g.piece(f"hood_{side}", "HEAD", (x, -9, FRONT_Z), (1, 9, 10))
        solid(wall, "P", "twill", 25822 + (x > 0), 2)
        hood_cloth(wall.right if x < 0 else wall.left, 25824 + (x > 0))
        (wall.left if x < 0 else wall.right).fill("P0")
        wall.front.fill("P3")
    back = g.piece("hood_back", "HEAD", (-5.5, -9, 4.5), (11, 10, 1))
    solid(back, "P", "twill", 25826, 2)
    hood_cloth(back.back, 25827)
    point = g.piece("hood_point", "HEAD", (-1.5, 0, 0), (3, 2, 1), pivot=(0, 1.0, 4.7), rotation=(14, 0, 0))
    solid(point, "P", "twill", 25828, 2)
    shade = g.piece("hood_shade", "HEAD", (-4.5, -8.4, FRONT_Z + .4), (9, 1, 1))
    for f in shade.faces:
        f.fill("P0")
    muffler = g.piece("muffler", "HEAD", (-4.4, -1.6, -4.4), (9, 2, 9), pivot=(-.05, 0, -.05), inflate=.3)
    solid(muffler, "K", "knit", 25829, 2, edge=False)
    muffler.front.vline(4, 0, 1, "K1"), muffler.front.hline(0, 8, 0, "K3")
