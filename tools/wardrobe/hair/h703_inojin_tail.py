"""Inojin Tail: short pale hair caught up in a small high tail, a long fringe swept across the brow
to the wearer's left that stops on the eye line, and short locks over the ears."""
from anime import cel_box, lock, ring_shell, sidelocks, tie
from paint import scalp

META = {"name": "Inojin Tail", "gender": "unisex",
        "description": "Small high tail, a long fringe swept over the left brow, short side locks."}

SWOOP = [(-3.0, ((2, 2), (1, 1)), -10), (-1.6, ((3, 2), (2, 2), (1, 1)), -56), (.2, ((3, 2), (2, 2)), -58),
         (1.9, ((2, 2), (1, 1)), -40)]


def build(g):
    scalp(g, 7201, side_rows=4, back_rows=7, sideburn=2)
    ring_shell(g, 7202, side_rows=4, back_rows=6, ring_row=1)
    for i, (x, segs, rz) in enumerate(SWOOP):
        lock(g, f"swoop_{i}", (x, -8.55, -4.35), (-10, 0, rz), segs, 1, 7210 + i * 13, ring=0)
    sidelocks(g, "frame", 5, seed=7240, x=4.4, z=-3.0, flare=6, width=2)
    tie(g, "tie", (0, -7.3, 4.3), (0, 0, 0), (2, 2, 2), y=-1)
    root = g.piece("tail_root", "HEAD", (-1.5, -2, 0), (3, 2, 3), pivot=(0, -7.5, 4.8), rotation=(30, 0, 0))
    cel_box(root, 7250, base=2)
    lock(g, "tail", (0, -7.6, 5.8), (46, 0, 0), ((3, 2), (3, 2), (2, 2), (1, 1)), 2, 7260, ring=None, motion="sway")
