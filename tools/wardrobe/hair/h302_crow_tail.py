"""Crow Tail: Itachi's look. Long straight bangs parted in the middle and falling past the jaw, the
forehead clear, and the length gathered low at the nape in a short tail tied with a dark cord."""
from anime import bangs, cel_box, lock, ring_shell, sidelocks, tie
from paint import scalp

META = {"name": "Crow Tail", "gender": "unisex",
        "description": "Long middle-parted bangs past the jaw, a low tail tied at the nape to the shoulder blades."}


def build(g):
    scalp(g, 3041, side_rows=6, back_rows=8, sideburn=4, part=3)
    ring_shell(g, 3042, side_rows=6, back_rows=8, ring_row=1)
    bangs(g, "fringe", [(-2.9, ((2, 2), (1, 1)), 24), (-1.4, ((1, 2),), 34), (1.4, ((1, 2),), -34),
                        (2.9, ((2, 2), (1, 1)), -24)], seed=3045)
    sidelocks(g, "frame", 11, seed=3050, x=4.25, z=-3.6, flare=2, width=2)
    sidelocks(g, "under", 7, seed=3055, x=4.45, z=-1.6, flare=5, width=2)
    tie(g, "tie", (0, -1.4, 4.6), size=(3, 1, 2))
    root = g.piece("tail_root", "HEAD", (-1.5, 0, -1), (3, 2, 2), pivot=(0, -.6, 4.8), rotation=(8, 0, 0))
    cel_box(root, 3060, top_delta=0)
    lock(g, "tail", (0, 1.2, 5.0), (6, 0, 0), ((3, 3), (2, 3), (1, 2)), 2, 3062, ring=None, motion="sway")
