"""Medic Bob: the chin-length bob of a medical-nin, parted on the wearer's left with a long fringe
swept across and pinned off the eyes, the front locks curving in under the jaw."""
from anime import cel_box, lock, ring_shell
from paint import scalp

META = {"name": "Medic Bob", "gender": "unisex",
        "description": "Chin bob parted on the left, long swept fringe, front locks curving in at the jaw."}

SWEEP = [(2.8, ((2, 2), (1, 1)), 14), (1.3, ((3, 2), (2, 1)), 48), (-.5, ((3, 2), (2, 1)), 50), (-2.5, ((2, 2), (1, 1)), 30)]


def build(g):
    scalp(g, 19051, side_rows=8, back_rows=8, sideburn=0, part=5)
    ring_shell(g, 19052, side_rows=8, back_rows=8, ring_row=1)
    for i, (x, segs, rz) in enumerate(SWEEP):
        lock(g, f"sweep_{i}", (x, -8.55, -4.35), (-10, 0, rz), segs, 1, 19055 + i * 7, ring=0)
    for side, sign in (("right", -1), ("left", 1)):
        panel = g.piece(f"side_{side}", "HEAD", (-.5, 0, -3.5), (1, 7, 7), pivot=(4.6 * sign, -8, .3))
        cel_box(panel, 19065 + (sign > 0), ring=1)
        curl = g.piece(f"curl_{side}", "HEAD", (-.5, 0, -1), (1, 2, 2), pivot=(4.6 * sign, -1.2, -2.6), rotation=(0, 0, 28 * sign))
        cel_box(curl, 19067 + (sign > 0), top_delta=0)
    back = g.piece("back", "HEAD", (-4.5, 0, -.5), (9, 7, 1), pivot=(0, -7.6, 4.6))
    cel_box(back, 19069, ring=1)
    tuck = g.piece("tuck", "HEAD", (-4, 0, -.5), (8, 1, 1), pivot=(0, -.8, 4.1), rotation=(-30, 0, 0))
    cel_box(tuck, 19070, top_delta=0)
