"""Kunoichi Cut: the hair Sakura cut short with a kunai in the Forest of Death, ragged at the jaw,
parted in the centre with the locks falling away from the forehead and pointed tips at the cheeks."""
from anime import cel_box, lock, ring_shell
from paint import scalp

META = {"name": "Kunoichi Cut", "gender": "unisex",
        "description": "Ragged jaw-length cut, centre part, forehead open, pointed tips at the cheeks."}

FRINGE = [(-2.7, ((2, 2), (1, 1)), 14), (-1.3, ((2, 2), (1, 1)), 36), (1.3, ((2, 2), (1, 1)), -36),
          (2.7, ((2, 2), (1, 1)), -14)]
BACK = [(-3.0, 3, 7), (-1.0, 2, 8), (1.0, 2, 8), (3.0, 3, 7)]


def build(g):
    scalp(g, 19021, side_rows=7, back_rows=8, sideburn=1, part=3)
    ring_shell(g, 19022, side_rows=7, back_rows=8, ring_row=1)
    for i, (x, segs, rz) in enumerate(FRINGE):
        lock(g, f"fringe_{i}", (x, -8.55, -4.35), (-10, 0, rz), segs, 1, 19025 + i * 7, ring=0)
    for side, sign in (("right", -1), ("left", 1)):
        lock(g, f"cheek_{side}", (4.3 * sign, -7.6, -3.0), (0, 0, -6 * sign), ((2, 5), (2, 2), (1, 1)), 1, 19035 + (sign > 0))
        lock(g, f"jaw_{side}", (4.4 * sign, -7.4, .4), (0, 0, -10 * sign), ((2, 6), (1, 2)), 3, 19037 + (sign > 0))
    for i, (x, w, n) in enumerate(BACK):
        lock(g, f"back_{i}", (x, -7.6, 4.3), (8, 0, 0), ((w, n - 2), (max(1, w - 1), 2)), 1, 19040 + i * 3)
    shelf = g.piece("nape", "HEAD", (-4, 0, -.5), (8, 2, 1), pivot=(0, -1.8, 4.3))
    cel_box(shelf, 19048, top_delta=0)
