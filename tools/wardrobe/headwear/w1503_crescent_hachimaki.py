"""Crescent Hachimaki: a plain indigo headband tied round the brow with a small silver crescent
sewn at the centre and long tails hanging from the knot at the back: the family's training band."""
from kit_gekko import crescent
from paint import solid

META = {"name": "Crescent Hachimaki", "gender": "unisex",
        "description": "Indigo headband with a silver crescent at the brow and long tails at the back."}


def build(g):
    band = g.piece("band", "HEAD", (-4, -7.6, -4), (8, 1, 8), inflate=.62)
    solid(band, "D", "weave", 15630, 2, edge=False)
    for face in band.sides:
        face.hline(0, 7, 0, "D2")
    crescent(g, "crescent", (0, -7.1, -4.7), bone="HEAD", role="D", base=2, mark="S4", face="front", flip=True)
    knot = g.piece("knot", "HEAD", (-1, -1, 0), (2, 2, 1), pivot=(0, -7.1, 4.65))
    solid(knot, "D", "weave", 15632, 2)
    for i, (x, rz) in enumerate(((-.6, 16), (.6, -12))):
        tail = g.piece(f"tail_{i}", "HEAD", (-.5, 0, 0), (1, 6, 1), pivot=(x, -6.4, 5.0), rotation=(18, 0, rz), motion="sway")
        solid(tail, "D", "weave", 15634 + i, 2)
