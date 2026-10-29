"""Nejiri Hachimaki: the carpenter's twisted head wrap, a cream and indigo towel rolled into a rope and
tied tight round the brow, knotted at the front over the left temple with two stubby ends standing up."""
from paint import k, solid

META = {"name": "Nejiri Hachimaki", "gender": "unisex",
        "description": "A cream and indigo towel twisted into a rope, knotted over the left temple."}


def twist(face, phase: int = 0):
    face.paint(lambda x, y, cur: k("S" if (x + phase) % 4 < 2 else "D", 3 if (x + phase) % 2 else 2))


def build(g):
    band = g.piece("band", "HEAD", (-4, -7.6, -4), (8, 1, 8), inflate=.66)
    solid(band, "S", "weave", 22751, 3, edge=False)
    for i, face in enumerate(band.sides):
        twist(face, i)
    knot = g.piece("knot", "HEAD", (-1, -1, -1), (2, 2, 2), pivot=(2.6, -7.2, -4.4))
    solid(knot, "S", "weave", 22752, 3)
    for face in knot.sides:
        twist(face)
    for i, (x, rz) in enumerate(((2.0, -24), (3.2, 30))):
        end = g.piece(f"end_{i}", "HEAD", (-.5, -2, -.5), (1, 2, 1), pivot=(x, -7.9, -4.5), rotation=(-10, 0, rz))
        solid(end, "S" if i else "D", "weave", 22753 + i, 3 if i else 2)
