"""Streamer Headband: a bright cloth headband tied in a knot over the left temple, its two long ends
streaming out behind: worn for the Academy's sports day and then never taken off."""
from paint import k, solid

META = {"name": "Streamer Headband", "gender": "unisex",
        "description": "Bright cloth headband knotted over the left temple, two long ends streaming behind."}


def build(g):
    band = g.piece("band", "HEAD", (-4, -7.0, -4), (8, 1, 8), inflate=.68)
    solid(band, "A", "weave", 31320, 2, edge=False)
    for f in band.sides:
        f.hline(0, f.w - 1, 0, k("A", 3))
    knot = g.piece("knot", "HEAD", (0, -1, -1), (1, 2, 2), pivot=(4.7, -6.6, -1.4))
    solid(knot, "A", "weave", 31321, 3)
    for i, (n, ry, rx) in enumerate(((7, -24, 64), (5, -40, 48))):
        tail = g.piece(f"streamer_{i}", "HEAD", (0, 0, -.5), (1, n, 1), pivot=(4.9, -6.2, -1.0 + i * .6),
                       rotation=(rx, ry, -20), motion="sway")
        solid(tail, "A", "weave", 31322 + i, 2)
        tail.left.set(0, n - 1, k("A", 1))
