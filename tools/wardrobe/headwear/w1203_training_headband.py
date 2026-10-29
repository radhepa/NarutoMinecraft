"""Training Headband: the plain brown cloth headband Yakumo wore while training with Kurenai, tied at
the back with two short tails."""
from paint import k, solid

META = {"name": "Training Headband", "gender": "unisex",
        "description": "Plain brown cloth headband tied at the back with two tails."}


def build(g):
    band = g.piece("band", "HEAD", (-4, -7.3, -4), (8, 1, 8), inflate=.72)
    solid(band, "L", "weave", 12970, 3, edge=False)
    for f in band.sides:
        f.hline(0, f.w - 1, 0, k("L", 3))
    knot = g.piece("knot", "HEAD", (-1, -1, 0), (2, 2, 1), pivot=(0, -7.1, 4.6))
    solid(knot, "L", "weave", 12971, 3)
    for i, (x, rz) in enumerate(((-.6, 16), (.6, -12))):
        tail = g.piece(f"tail_{i}", "HEAD", (-.5, 0, 0), (1, 4, 1), pivot=(x, -6.4, 4.9), rotation=(22, 0, rz), motion="sway")
        solid(tail, "L", "weave", 12972 + i, 3)
