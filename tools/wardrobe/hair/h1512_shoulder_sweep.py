"""Shoulder Sweep: long straight hair drawn over the right shoulder in one loose sheaf that falls
down the front to the ribs, the left side tucked back, a side-swept fringe."""
from anime import bangs, cel_box, lock, ring_shell, sidelocks
from paint import scalp

META = {"name": "Shoulder Sweep", "gender": "female",
        "description": "Long hair drawn over one shoulder to the ribs, the other side tucked back, side fringe."}


def build(g):
    scalp(g, 15300, side_rows=7, back_rows=8, sideburn=3)
    ring_shell(g, 15301, side_rows=7, back_rows=8, ring_row=1)
    back = g.piece("back", "HEAD", (-4.5, 0, -.5), (9, 5, 1), pivot=(0, -7.6, 4.6))
    cel_box(back, 15302, ring=1)
    # The sheaf leaves the nape on the right, crosses the shoulder and hangs down the chest.
    lock(g, "sheaf_root", (-3.4, -3.0, 3.0), (0, 40, 30), ((3, 4),), 3, 15305, ring=None)
    lock(g, "sheaf", (-4.6, -.6, -1.2), (-12, 0, 6), ((3, 6), (3, 4), (2, 2), (1, 1)), 2, 15308, ring=None,
         motion="sway")
    side = g.piece("side_right", "HEAD", (-.5, 0, -3), (1, 8, 7), pivot=(-4.6, -7, .6))
    cel_box(side, 15312, ring=1)
    bangs(g, "fringe", [(-3.0, ((3, 2), (2, 1), (1, 1)), 30), (-1.0, ((3, 2), (2, 1)), 42), (1.0, ((3, 1), (2, 1)), 52),
                        (3.0, ((2, 2), (1, 1)), -12)], seed=15315)
    lock(g, "frame_right", (-4.3, -7.6, -3.4), (0, 0, 3), ((2, 7), (1, 2)), 1, 15320)
