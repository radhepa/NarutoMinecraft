"""Eye Bandage: Danzo's head bandage: off-white bandage wound round the head low over the brow,
a broad turn dropping over the right temple and the outer corner of the right eye, knotted behind
with two short ends."""
from kit_shinobi import bandage
from paint import solid

META = {"name": "Eye Bandage", "gender": "unisex", "hides_hair": ["fringe", "frame", "ear", "temple"],
        "description": "Bandage wound low round the head, a broad turn over the right temple and eye corner, knotted behind."}


def build(g):
    band = g.piece("bandage", "HEAD", (-4, -7.1, -4), (8, 1, 8), inflate=.62)
    for f in band.faces:
        bandage(f, 0, 0, f.w - 1, f.h - 1)
    # The turn over the right side of the face, outside the eye opening: a front panel over the
    # temple and eye corner and the wrap round the side of the head behind it.
    front = g.piece("bandage_eye", "HEAD", (0, 0, 0), (2, 5, 1), pivot=(-4.9, -7.0, -4.75), scale=(.9, 1, 1))
    side = g.piece("bandage_side", "HEAD", (0, 0, 0), (1, 4, 5), pivot=(-4.75, -6.8, -4.2))
    for box in (front, side):
        for f in box.faces:
            bandage(f, 0, 0, f.w - 1, f.h - 1)
    front.front.hline(0, 1, 4, "S1")
    knot = g.piece("knot", "HEAD", (-1, -1, 0), (2, 2, 1), pivot=(.6, -6.6, 4.65))
    solid(knot, "S", "plain", 13900, 3)
    for i, (x, rz) in enumerate(((0, 16), (1.0, -12))):
        end = g.piece(f"end_{i}", "HEAD", (-.5, 0, 0), (1, 4, 1), pivot=(x, -5.9, 4.9), rotation=(20, 0, rz), motion="sway")
        solid(end, "S", "plain", 13901 + i, 3)
