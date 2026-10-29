"""Mist Hime: a court-painter's hime cut. Long, straight hair to the waist, cheek-length side locks
cut in clean blunt blocks, and a light fringe that keeps the brows clear; one length of hair hanging
like a mist over the back."""
from anime import bangs, cel_box, curtain, ring_shell
from paint import scalp

META = {"name": "Mist Hime", "gender": "female",
        "description": "Waist-length straight hair, blunt cheek-length side locks, a light fringe."}


def build(g):
    scalp(g, 12680, side_rows=7, back_rows=8, sideburn=4, part=3)
    ring_shell(g, 12681, side_rows=7, back_rows=8, ring_row=1)
    curtain(g, "back", (0, -6.2, 4.6), (-6, 0, 0), 9, 15, hem=[(0, 9, 1)], seed=12682)
    for side, sign in (("right", -1), ("left", 1)):
        block = g.piece(f"hime_{side}", "HEAD", (-1, 0, -1), (2, 7, 2), pivot=(4.3 * sign, -7.4, -2.9))
        cel_box(block, 12690 + (sign > 0), ring=1)
        block.bottom.fill("H1")
        panel = g.piece(f"side_{side}", "HEAD", (-.5, 0, -2.5), (1, 9, 6), pivot=(4.6 * sign, -7.0, 1.2))
        cel_box(panel, 12694 + (sign > 0), ring=1)
    bangs(g, "fringe", [(-2.8, ((2, 2), (1, 1)), 6), (-1.3, ((2, 2),), 4), (.2, ((2, 2),), 0),
                        (1.7, ((2, 2),), -4), (3.0, ((2, 2), (1, 1)), -6)], seed=12700)
