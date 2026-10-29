"""Sage Topknot: Indra's long hair drawn up into a knot high on the crown, a thick tail spilling from
it down the back, a short middle-parted fringe and long side locks framing the face."""
from anime import bangs, cel_box, lock, ring_shell, sidelocks, tie
from paint import scalp

META = {"name": "Sage Topknot", "gender": "unisex",
        "description": "A knot high on the crown spilling a long tail, a parted fringe and long framing locks."}


def build(g):
    scalp(g, 3501, side_rows=5, back_rows=7, sideburn=3, part=3)
    ring_shell(g, 3502, side_rows=4, back_rows=7, ring_row=1)
    knot = g.piece("knot", "HEAD", (-2, -3, -2), (4, 3, 4), pivot=(0, -8.0, 1.6))
    cel_box(knot, 3505, ring=1)
    tie(g, "tie", (0, -8.2, 1.6), size=(4, 1, 4), y=-.5)
    lock(g, "tail_fall", (0, -10.4, 2.6), (64, 0, 0), ((3, 3),), 2, 3510, ring=None)
    lock(g, "tail", (0, -9.0, 4.6), (12, 0, 0), ((3, 4), (3, 4), (2, 4), (1, 2)), 2, 3512, ring=None, motion="sway")
    bangs(g, "fringe", [(-2.6, ((2, 2), (1, 1)), 26), (-1.1, ((2, 1),), 34), (1.1, ((2, 1),), -34),
                        (2.6, ((2, 2), (1, 1)), -26)], seed=3520)
    sidelocks(g, "frame", 11, seed=3525, x=4.3, z=-3.5, flare=3, width=2)
