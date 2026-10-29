"""Twisted Tenugui: a cotton hand towel rolled tight and tied round the brow for hot work at the
stove or the anvil, knotted at the right temple with the two ends sticking out."""
from paint import k, solid

META = {"name": "Twisted Tenugui", "gender": "unisex",
        "description": "Cotton towel twisted tight round the brow, knotted at the right temple."}


def build(g):
    band = g.piece("band", "HEAD", (-4, -7.6, -4), (8, 1, 8), inflate=.62)
    solid(band, "S", "weave", 36910, 3, edge=False)
    for face in band.sides:
        face.paint(lambda x, y, cur: k("D", 2) if x % 3 == 0 else k("S", 3))
    knot = g.piece("knot", "HEAD", (-1, -1, -1), (2, 2, 2), pivot=(-4.6, -7.2, -2.6))
    solid(knot, "S", "weave", 36911, 3)
    knot.right.set(0, 0, k("D", 2)), knot.front.set(1, 1, k("D", 2))
    for i, (rz, ry) in enumerate(((-60, 20), (-30, -30))):
        end = g.piece(f"end_{i}", "HEAD", (-.5, 0, -.5), (1, 3, 1), pivot=(-5.0, -7.0, -2.4 + i), rotation=(0, ry, rz),
                      motion="sway")
        solid(end, "S", "weave", 36912 + i, 3)
        end.right.set(0, 2, k("D", 2))
