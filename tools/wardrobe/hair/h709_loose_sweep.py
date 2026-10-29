"""Loose Sweep: the long hair let down, a sleek sheet to the waist with a pointed hem, a deep side
part sweeping the fringe off the brow to the wearer's right, and long locks framing the face."""
from anime import bangs, cel_box, curtain, lock, ring_shell
from paint import scalp

META = {"name": "Loose Sweep", "gender": "unisex",
        "description": "Long hair let down to the waist, a deep side part, long face-framing locks."}


def build(g):
    scalp(g, 7801, side_rows=7, back_rows=8, sideburn=4, part=5)
    ring_shell(g, 7802, side_rows=7, back_rows=8, ring_row=1)
    curtain(g, "sheet", (0, -6.4, 4.6), (-6, 0, 0), 9, 15, hem=[(0, 3, 3), (3, 3, 4), (6, 3, 2)], seed=7810)
    for side, sign in (("right", -1), ("left", 1)):
        panel = g.piece(f"side_{side}", "HEAD", (-.5, 0, -3), (1, 10, 7), pivot=(4.6 * sign, -7, .8))
        cel_box(panel, 7820 + (sign > 0), ring=1)
    bangs(g, "fringe", [(-2.8, ((2, 2), (1, 1)), 26), (-1.2, ((3, 2), (2, 2)), 50), (.6, ((3, 2), (2, 1)), 56),
                        (2.4, ((2, 2), (1, 1)), 44)], seed=7830)
    lock(g, "frame_right", (-4.5, -7.6, -3.4), (0, 0, 3), ((2, 8), (2, 3), (1, 2)), 1, 7840)
    lock(g, "frame_left", (4.5, -7.6, -3.4), (0, 0, -3), ((2, 7), (1, 2)), 1, 7845)
