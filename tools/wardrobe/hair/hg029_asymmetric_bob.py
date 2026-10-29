"""Asymmetric Bob: cut close over the right ear and nape, falling long on the left into a pointed
lock that reaches past the jaw, with a fringe swept across toward the long side."""
from anime import bangs, cel_box, lock, ring_shell
from paint import scalp

META = {"name": "Asymmetric Bob", "gender": "unisex",
        "description": "Close on the right, long on the left past the jaw, a fringe swept to the long side."}


def build(g):
    scalp(g, 33945, side_rows=4, back_rows=6, sideburn=1)
    ring_shell(g, 33946, side_rows=3, back_rows=6, ring_row=1)
    back = g.piece("back", "HEAD", (-4.5, 0, -.5), (9, 5, 1), pivot=(0, -7.6, 4.5), rotation=(-6, 0, -4))
    cel_box(back, 33947, ring=1)
    long_side = g.piece("side_left", "HEAD", (-.5, 0, -3.5), (1, 9, 7), pivot=(4.6, -8, .3), rotation=(-8, 0, 0))
    cel_box(long_side, 33948, ring=1)
    lock(g, "long_lock", (4.3, -7.6, -3.4), (0, 0, -4), ((2, 7), (2, 2), (1, 2)), 1, 33949, ring=1)
    bangs(g, "fringe", [(-2.8, ((2, 2), (1, 1)), -24), (-1.0, ((3, 2), (2, 1)), -40), (1.0, ((3, 2), (2, 1)), -46),
                        (2.8, ((2, 2), (1, 1)), -30)], seed=33952)
