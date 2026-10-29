"""Nawaki Goggles: a boy's flight goggles pushed up on the forehead, two round lenses in dark rims
on a cloth strap round the head, the way Tsunade's little brother wore them."""
from paint import fabric, k, solid

META = {"name": "Nawaki Goggles", "gender": "unisex",
        "description": "Goggles pushed up on the forehead: two lenses in dark rims on a strap round the head."}


def build(g):
    strap = g.piece("strap", "HEAD", (-4, -7.4, -4), (8, 1, 8), inflate=.6)
    solid(strap, "D", "weave", 1820, 2, edge=False)
    for i, x in enumerate((-2.2, 2.2)):
        rim = g.piece(f"lens_{i}", "HEAD", (-1.5, -1.5, -1), (3, 3, 1), pivot=(x, -6.9, -4.75))
        solid(rim, "K", "smooth", 1821 + i, 2, edge=False)
        f = rim.front
        fabric(f, "M", "smooth", 1823, 3, 1, 1, 1, 1)
        f.set(1, 1, k("M", 4))
    bridge = g.piece("bridge", "HEAD", (-1, 0, 0), (2, 1, 1), pivot=(0, -7.2, -4.75))
    solid(bridge, "K", "smooth", 1825, 2, edge=False)
