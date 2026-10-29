"""Senju Brow Guard: the forehead guard of the Warring States years, before the village: a plain
steel plate on a red band, engraved with the split circle of the Senju, ends knotted at the back."""
from kit_senju import crest
from paint import fabric, solid

META = {"name": "Senju Brow Guard", "gender": "unisex",
        "description": "Plain steel brow plate with the Senju crest on a red band, knotted at the back."}


def build(g):
    band = g.piece("band", "HEAD", (-4, -7.6, -4), (8, 1, 8), inflate=.6)
    solid(band, "A", "weave", 1800, 2, edge=False)
    plate = g.piece("plate", "HEAD", (-9, -4, -2), (18, 8, 2), pivot=(0, -7.0, -4.62), scale=(1 / 3, 1 / 3, 1 / 3))
    for face in plate.faces:
        fabric(face, "M", "plain", 1801, 2)
    f = plate.front
    fabric(f, "M", "plain", 1802, 3)
    f.hline(0, 17, 0, "M4"), f.hline(0, 17, 7, "M1"), f.vline(0, 0, 7, "M2"), f.vline(17, 0, 7, "M1")
    crest(f, 5, 0, "M0", bar="M3")
    knot = g.piece("knot", "HEAD", (-1, -1, 0), (2, 2, 1), pivot=(0, -7.1, 4.6))
    solid(knot, "A", "weave", 1803, 2)
    for i, (x, rz) in enumerate(((-.6, 16), (.6, -12))):
        tail = g.piece(f"tail_{i}", "HEAD", (-.5, 0, 0), (1, 6, 1), pivot=(x, -6.4, 4.9), rotation=(22, 0, rz),
                       motion="sway")
        solid(tail, "A", "weave", 1804 + i, 2)
