"""Seal Tag Band: a dark cloth band round the brow with paper seal tags tucked under it at both
temples and the back, ready to slap on a barrier stake, and short tails at the knot."""
from paint import solid

META = {"name": "Seal Tag Band", "gender": "unisex",
        "description": "Dark brow band with paper seal tags tucked in at the temples and back, short knot tails."}


def build(g):
    band = g.piece("band", "HEAD", (-4, -7.6, -4), (8, 1, 8), inflate=.62)
    solid(band, "K", "weave", 34970, 2, edge=False)
    for f in band.sides:
        f.set(f.w // 2, 0, "A2")
    for i, (pivot, rz, ry) in enumerate((((-4.75, -8.1, -1.6), 6, 0), ((4.75, -8.1, -1.0), -8, 0),
                                         ((-1.6, -8.1, 4.75), 4, 90), ((1.4, -8.1, 4.75), -6, 90))):
        tag = g.piece(f"tag_{i}", "HEAD", (0, 0, -.5), (1, 4, 1), pivot=pivot, rotation=(0, ry, rz))
        solid(tag, "S", "plain", 34971 + i, 4, edge=False)
        for f in tag.sides:
            f.set(0, 1, "K1"), f.set(0, 2, "A2")
    knot = g.piece("knot", "HEAD", (-1, -1, 0), (2, 2, 1), pivot=(0, -7.1, 4.75))
    solid(knot, "K", "weave", 34976, 2)
    for i, (x, rz) in enumerate(((-.6, 16), (.6, -12))):
        tail = g.piece(f"tail_{i}", "HEAD", (-.5, 0, 0), (1, 4, 1), pivot=(x, -6.4, 5.0), rotation=(18, 0, rz),
                       motion="sway")
        solid(tail, "K", "weave", 34977 + i, 2)
