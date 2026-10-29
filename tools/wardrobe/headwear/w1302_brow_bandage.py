"""Brow Bandage: a plain off-white bandage wound round the forehead and knotted at the back,
two short ends hanging: the clan's mark of an old wound kept covered."""
from kit_shinobi import bandage
from paint import solid

META = {"name": "Brow Bandage", "gender": "unisex",
        "description": "Plain bandage wound round the forehead, knotted at the back with two short ends."}


def build(g):
    band = g.piece("bandage", "HEAD", (-4, -7.2, -4), (8, 1, 8), inflate=.62)
    for f in band.faces:
        bandage(f, 0, 0, f.w - 1, f.h - 1)
    knot = g.piece("knot", "HEAD", (-1, -1, 0), (2, 2, 1), pivot=(-.4, -6.5, 4.65))
    solid(knot, "S", "plain", 13920, 3)
    for i, (x, rz) in enumerate(((-.8, 18), (.2, -8))):
        end = g.piece(f"end_{i}", "HEAD", (-.5, 0, 0), (1, 4, 1), pivot=(x, -5.8, 4.9), rotation=(22, 0, rz), motion="sway")
        solid(end, "S", "plain", 13921 + i, 3)
