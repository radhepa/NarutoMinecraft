"""Cloth Tail: hair drawn back to a low tail at the nape and bound in a strip of indigo cloth wound
round it several times, the tail hanging between the shoulders; a short centre-parted fringe and
face-framing locks to the jaw."""
from anime import bangs, cel_box, lock, ring_shell, sidelocks
from paint import scalp, solid

META = {"name": "Cloth Tail", "gender": "unisex",
        "description": "A low tail wound in an indigo cloth strip, a parted fringe and jaw-length framing locks."}


def build(g):
    scalp(g, 22061, side_rows=6, back_rows=8, sideburn=3, part=4)
    ring_shell(g, 22062, side_rows=5, back_rows=8, ring_row=1)
    root = g.piece("tail_root", "HEAD", (-1.5, 0, -1), (3, 2, 2), pivot=(0, -2.4, 4.6), rotation=(-6, 0, 0))
    cel_box(root, 22063)
    wrap = g.piece("tail_wrap", "HEAD", (-1.5, 0, -1.5), (3, 3, 3), pivot=(0, -.6, 4.9), rotation=(10, 0, 0),
                   inflate=.05, motion="sway")
    solid(wrap, "D", "weave", 22064, 2, edge=False)
    for face in wrap.sides:
        face.hline(0, face.w - 1, 1, "D1")
    lock(g, "tail", (0, 2.2, 5.3), (14, 0, 0), ((3, 3), (2, 2), (1, 1)), 2, 22065, ring=None, motion="sway")
    bangs(g, "fringe", [(-2.6, ((2, 2), (1, 1)), 26), (-1.0, ((2, 1),), 34), (1.0, ((2, 1),), -34),
                        (2.6, ((2, 2), (1, 1)), -26)], seed=22070)
    sidelocks(g, "frame", 7, seed=22076, x=4.3, z=-3.2, flare=5, width=2)
