"""Fire Headband: a clan headband for training and festivals. A red cloth band tied round the brow
with the Sarutobi crest stitched at the front and long tails knotted at the back."""
from kit_sarutobi import crest
from paint import fabric, solid

META = {"name": "Fire Headband", "gender": "unisex",
        "description": "Red cloth headband with the Sarutobi crest at the brow and long tails at the back."}


def build(g):
    band = g.piece("band", "HEAD", (-4, -7.6, -4), (8, 1, 8), inflate=.6)
    solid(band, "A", "weave", 9921, 2, edge=False)
    patch = g.piece("crest", "HEAD", (-5, -5, -1), (10, 10, 1), pivot=(0, -7.0, -4.62), scale=(.3, .3, .3))
    for f in patch.faces:
        fabric(f, "A", "weave", 9922, 2)
    crest(patch.front, 0, 0, "S4", ground="A1")
    knot = g.piece("knot", "HEAD", (-1, -1, 0), (2, 2, 1), pivot=(0, -7.1, 4.6))
    solid(knot, "A", "weave", 9923, 2)
    for i, (x, rz) in enumerate(((-.6, 16), (.6, -12))):
        tail = g.piece(f"tail_{i}", "HEAD", (-.5, 0, 0), (1, 7, 1), pivot=(x, -6.4, 4.9), rotation=(20, 0, rz), motion="sway")
        solid(tail, "A", "weave", 9924 + i, 2)
        tail.back.set(0, 6, "A1")
