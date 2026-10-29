"""Swordsman's Topknot: hair drawn up off the neck into a short folded knot on the crown, bound with
a cord, and a couple of loose strands left at the temples: kept out of the way of the blade."""
from anime import cel_box, lock, ring_shell, tie
from paint import scalp

META = {"name": "Swordsman's Topknot", "gender": "unisex",
        "description": "Hair drawn up into a short folded knot on the crown, bound with a cord, loose temple strands."}


def build(g):
    scalp(g, 15110, side_rows=4, back_rows=8, sideburn=2, part=None)
    ring_shell(g, 15111, side_rows=3, back_rows=7, ring_row=1)
    root = g.piece("knot_root", "HEAD", (-1.5, -2, -1.5), (3, 2, 3), pivot=(0, -8, .8))
    cel_box(root, 15112, top_delta=1)
    tie(g, "knot_cord", (0, -9.6, .8), size=(3, 1, 3), key="A2")
    # The folded tail: forward along the crown, then the tip turned back.
    lock(g, "knot_fold", (0, -10.4, .8), (-100, 0, 0), ((3, 3), (2, 1)), 2, 15115, ring=0)
    lock(g, "knot_tip", (0, -10.6, -1.5), (150, 0, 0), ((2, 2), (1, 1)), 2, 15118, ring=None)
    for side, sign in (("right", -1), ("left", 1)):
        lock(g, f"temple_{side}", (3.9 * sign, -7.4, -3.6), (0, 0, -4 * sign), ((1, 4), (1, 1)), 1, 15120 + (sign > 0))
