"""Hachimaki: a twisted white headband tied tight round the brow for a big effort, a red stripe down
its middle and the knot at the back with two short ends."""
from paint import k, solid

META = {"name": "Hachimaki", "gender": "unisex",
        "description": "Twisted white headband with a red stripe, knotted at the back."}


def build(g):
    band = g.piece("band", "HEAD", (-4, -7.4, -4), (8, 1, 8), inflate=.62)
    solid(band, "S", "weave", 6990, 3, edge=False)
    for face in band.sides:
        face.paint(lambda x, y, cur: k("S", 3 if x % 3 else 2))
        face.set(face.w // 2, 0, "A2")
    knot = g.piece("knot", "HEAD", (-1, -1, 0), (2, 2, 1), pivot=(0, -6.9, 4.7))
    solid(knot, "S", "weave", 6991, 3)
    for i, (x, rz) in enumerate(((-.6, 30), (.6, -26))):
        end = g.piece(f"end_{i}", "HEAD", (-.5, 0, 0), (1, 3, 1), pivot=(x, -6.2, 5.0), rotation=(20, 0, rz), motion="sway")
        solid(end, "S", "weave", 6992 + i, 3)
