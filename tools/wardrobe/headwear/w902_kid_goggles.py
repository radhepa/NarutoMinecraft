"""Kid Goggles: Konohamaru's Academy goggles. Big round tinted lenses in a rubber frame pushed up
on the forehead and held by a broad strap round the head."""
from paint import fabric, k, solid

META = {"name": "Kid Goggles", "gender": "unisex", "hides_hair": ["fringe"],
        "description": "Big round tinted goggles pushed up on the forehead on a broad strap."}


def build(g):
    strap = g.piece("strap", "HEAD", (-4, -7.8, -4), (8, 1, 8), inflate=.62)
    solid(strap, "K", "smooth", 9911, 2, edge=False)
    for side, x in (("right", -2.2), ("left", 2.2)):
        frame = g.piece(f"goggle_{side}", "HEAD", (-1.5, -1.5, -1), (3, 3, 1), pivot=(x, -7.0, -4.7))
        solid(frame, "K", "smooth", 9912, 3)
        lens = frame.front
        fabric(lens, "D", "plain", 9913, 3)
        lens.set(0, 0, k("K", 3)), lens.set(2, 0, k("K", 3)), lens.set(0, 2, k("K", 3)), lens.set(2, 2, k("K", 3))
        lens.set(1, 1, k("D", 4))
    bridge = g.piece("bridge", "HEAD", (-.5, 0, 0), (1, 1, 1), pivot=(0, -7.2, -5.0))
    solid(bridge, "K", "smooth", 9914, 2)
