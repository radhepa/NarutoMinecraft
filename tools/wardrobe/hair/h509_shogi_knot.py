"""Shogi Knot: a flat, five-sided knot pinned on the crown, cut square at the base and peaked at the
top like a shogi piece, the sides combed tight and short points at the temples."""
from anime import bangs, cel_box
from kit_nara import pulled_back

META = {"name": "Shogi Knot", "gender": "unisex",
        "description": "A flat five-sided knot on the crown shaped like a shogi piece, tight sides, temple points."}


def build(g):
    pulled_back(g, 5501, side_rows=4, back_rows=6, sideburn=2)
    pivot, tilt = (0, -8.0, 2.0), (-24, 0, 0)
    # The piece: a broad base, a narrower shoulder and a peak, standing on the crown.
    for i, (w, y, h) in enumerate(((5, -2, 2), (4, -4, 2), (2, -5, 1))):
        box = g.piece(f"knot_{i}", "HEAD", (-w / 2, y, -1), (w, h, 2), pivot=pivot, rotation=tilt)
        cel_box(box, 5510 + i * 3, base=2, top_delta=1)
    pin = g.piece("pin", "HEAD", (-3.5, -3.2, -.5), (7, 1, 1), pivot=pivot, rotation=tilt)
    for f in pin.faces:
        f.fill("M3")
    for f in pin.sides:
        f.set(0, 0, "M1"), f.set(f.w - 1, 0, "M1")
    bangs(g, "fringe", [(-3.0, ((2, 2), (1, 1)), 18), (3.0, ((2, 2), (1, 1)), -18)], seed=5530)
