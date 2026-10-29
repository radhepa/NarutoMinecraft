"""Spider Band: a plum cloth band round the brow with the clan's earth spider on an ochre plate at
the front, knotted at the back with two trailing ends."""
from kit_tsuchigumo import SPIDER, glyph
from paint import fabric, k, solid

META = {"name": "Spider Band", "gender": "unisex",
        "description": "Plum brow band with the earth spider on an ochre plate, knotted at the back."}


def build(g):
    band = g.piece("band", "HEAD", (-4, -7.6, -4), (8, 1, 8), inflate=.6)
    solid(band, "P", "weave", 23931, 2, edge=False)
    plate = g.piece("plate", "HEAD", (-6, -5, -1), (12, 10, 1), pivot=(0, -7.1, -4.62), scale=(1 / 3, 1 / 3, 1 / 3))
    for face in plate.faces:
        fabric(face, "A", "plain", 23932, 2)
    p = plate.front
    p.hline(0, 11, 0, "A4"), p.hline(0, 11, 9, "A1"), p.vline(0, 0, 9, "A3"), p.vline(11, 0, 9, "A1")
    glyph(p, SPIDER, 1, 0, {"#": "P1", "+": "P1"})
    knot = g.piece("knot", "HEAD", (-1, -1, 0), (2, 2, 1), pivot=(0, -7.1, 4.6))
    solid(knot, "P", "weave", 23934, 2)
    for i, (x, rz) in enumerate(((-.6, 14), (.6, -10))):
        tail = g.piece(f"tail_{i}", "HEAD", (-.5, 0, 0), (1, 5, 1), pivot=(x, -6.4, 4.9), rotation=(22, 0, rz), motion="sway")
        solid(tail, "P", "weave", 23935 + i, 2)
        tail.back.set(0, 4, k("P", 1))
