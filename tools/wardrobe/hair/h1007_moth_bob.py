"""Moth Bob: a chin-length bob parted in the middle, the side panels flaring out at the hem like
a resting moth's wings."""
from anime import bangs, cel_box, ring_shell
from paint import scalp

META = {"name": "Moth Bob", "gender": "unisex",
        "description": "Middle-parted chin-length bob, the side panels flaring out at the hem like wings."}


def build(g):
    scalp(g, 10191, side_rows=7, back_rows=8, sideburn=1, part=3)
    ring_shell(g, 10192, side_rows=8, back_rows=8, ring_row=1)
    for side, sign in (("right", -1), ("left", 1)):
        wing = g.piece(f"wing_{side}", "HEAD", (-.5, 0, -3.5), (1, 8, 7), pivot=(4.55 * sign, -7.4, .4),
                       rotation=(0, 0, -9 * sign))
        cel_box(wing, 10200 + (sign > 0), ring=1)
        tip = g.piece(f"wing_tip_{side}", "HEAD", (-.5, 8, -3.5), (1, 1, 3), pivot=(4.55 * sign, -7.4, .4),
                      rotation=(0, 0, -9 * sign))
        cel_box(tip, 10203 + (sign > 0), top_delta=0)
    back = g.piece("back_panel", "HEAD", (-4.5, 0, -.5), (9, 8, 1), pivot=(0, -7.0, 4.6), rotation=(6, 0, 0))
    cel_box(back, 10206, ring=1)
    bangs(g, "fringe", [(-2.6, ((2, 2), (1, 1)), 22), (-1.0, ((2, 1),), 30), (1.0, ((2, 1),), -30),
                        (2.6, ((2, 2), (1, 1)), -22)], seed=10210)
