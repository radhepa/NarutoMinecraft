"""Brow Wrap: a plain white cloth bound once round the forehead and knotted at the back, the way the
branch house keeps the caged-bird seal out of sight."""
from paint import solid

META = {"name": "Brow Wrap", "gender": "unisex",
        "description": "White cloth bound round the forehead, knotted at the back, hiding the seal."}


def build(g):
    band = g.piece("band", "HEAD", (-4, -7.4, -4), (8, 1, 8), inflate=.62)
    solid(band, "S", "weave", 4981, 3, edge=False)
    for face in band.sides:
        for x in range(face.w):
            if x % 3 == 0:
                face.set(x, 0, "S2")
    knot = g.piece("knot", "HEAD", (-1, -1, 0), (2, 2, 1), pivot=(0, -6.6, 4.6))
    solid(knot, "S", "weave", 4982, 3)
    for i, (x, rz) in enumerate(((-.5, 12), (.5, -8))):
        tail = g.piece(f"tail_{i}", "HEAD", (-.5, 0, 0), (1, 4 - i, 1), pivot=(x, -6.0, 4.9), rotation=(20, 0, rz), motion="sway")
        solid(tail, "S", "weave", 4983 + i, 3)
