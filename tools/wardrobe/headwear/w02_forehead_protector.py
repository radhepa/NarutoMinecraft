"""Forehead Protector: a navy cloth band tied at the back, with a steel plate engraved with the
Hidden Leaf mark. The plate is drawn at triple resolution so the mark reads."""
from glyphs import LEAF, stamp
from paint import fabric, k, solid

META = {"name": "Forehead Protector", "gender": "unisex",
        "description": "Navy band, riveted steel plate with the leaf mark, knot tails at the back."}


def build(g):
    band = g.piece("band", "HEAD", (-4, -7.6, -4), (8, 1, 8), inflate=.6)
    solid(band, "D", "weave", 61, 2, edge=False)
    # Steel plate: brushed face, bright top edge, rivets, the engraved mark.
    plate = g.piece("plate", "HEAD", (-9, -4, -2), (18, 8, 2), pivot=(0, -7.0, -4.62), scale=(1 / 3, 1 / 3, 1 / 3))
    for face in plate.faces:
        fabric(face, "M", "plain", 62, 2)
    f = plate.front
    fabric(f, "M", "plain", 63, 3)
    f.hline(0, 17, 0, "M4"), f.hline(0, 17, 7, "M1")
    f.vline(0, 0, 7, "M2"), f.vline(17, 0, 7, "M1")
    for x in (2, 15):
        f.set(x, 2, "M1"), f.set(x, 5, "M1")
    stamp(f, LEAF, 5, 0, {"#": "M0"})
    # Knot and tails.
    knot = g.piece("knot", "HEAD", (-1, -1, 0), (2, 2, 1), pivot=(0, -7.1, 4.6))
    solid(knot, "D", "weave", 64, 2)
    for i, (x, rz) in enumerate(((-.6, 14), (.6, -10))):
        tail = g.piece(f"tail_{i}", "HEAD", (-.5, 0, 0), (1, 5, 1), pivot=(x, -6.4, 4.9), rotation=(22, 0, rz), motion="sway")
        solid(tail, "D", "weave", 65 + i, 2)
        tail.back.set(0, 4, "D1")
