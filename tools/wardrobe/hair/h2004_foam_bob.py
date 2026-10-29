"""Foam Bob: a chin-length bob whose ends flick outward all round like foam thrown off a wave, a
short fringe parted off-centre at the brow."""
from anime import bangs, cel_box, lock, ring_shell
from paint import scalp

META = {"name": "Foam Bob", "gender": "unisex",
        "description": "Chin-length bob, the ends flicked outward all round, an off-centre parted fringe."}


def build(g):
    scalp(g, 20111, side_rows=8, back_rows=8, sideburn=0)
    ring_shell(g, 20112, side_rows=8, back_rows=8, ring_row=1)
    back = g.piece("bob_back", "HEAD", (-4.5, 0, -.5), (9, 8, 1), pivot=(0, -7.6, 4.6))
    cel_box(back, 20113, ring=1)
    for side, sign in (("right", -1), ("left", 1)):
        panel = g.piece(f"bob_{side}", "HEAD", (-.5, 0, -4), (1, 8, 8), pivot=(4.6 * sign, -7.6, .8))
        cel_box(panel, 20115 + (sign > 0), ring=1)
        for i, z in enumerate((-3.0, -.5, 2.0, 4.0)):
            lock(g, f"flick_{side}_{i}", (4.6 * sign, .2, z), (0, 0, -62 * sign), ((2, 2), (1, 1)), 1,
                 20120 + i + 4 * (sign > 0), ring=None)
    for i, x in enumerate((-3.0, -1.0, 1.0, 3.0)):
        lock(g, f"flick_back_{i}", (x, .2, 4.6), (62, 0, 0), ((2, 2), (1, 1)), 1, 20130 + i, ring=None)
    bangs(g, "fringe", [(-2.8, ((2, 2), (1, 1)), 18), (-1.2, ((2, 2), (1, 1)), 22), (.8, ((2, 2), (1, 1)), -12),
                        (2.7, ((2, 2), (1, 1)), -8)], seed=20140)
