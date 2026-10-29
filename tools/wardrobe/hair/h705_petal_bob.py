"""Petal Bob: a sleek bob cut on a slant from the nape to the chin, a side-parted fringe swept off
the brow and a small blossom pinned above the right temple."""
from anime import bangs, cel_box, ring_shell
from kit_yamanaka import flower
from paint import scalp

META = {"name": "Petal Bob", "gender": "unisex",
        "description": "Slanted chin bob, side-parted fringe, a blossom pinned at the right temple."}


def build(g):
    scalp(g, 7401, side_rows=8, back_rows=8, sideburn=0, part=2)
    ring_shell(g, 7402, side_rows=8, back_rows=8, ring_row=1)
    for side, sign in (("right", -1), ("left", 1)):
        panel = g.piece(f"side_{side}", "HEAD", (-.5, 0, -3.5), (1, 8, 7), pivot=(4.6 * sign, -8, .3), rotation=(-6, 0, 0))
        cel_box(panel, 7410 + (sign > 0), ring=1)
        point = g.piece(f"side_{side}_point", "HEAD", (-.5, 8, -3.5), (1, 1, 3), pivot=(4.6 * sign, -8, .3), rotation=(-6, 0, 0))
        cel_box(point, 7412 + (sign > 0), top_delta=0)
    back = g.piece("back", "HEAD", (-4.5, 0, -.5), (9, 7, 1), pivot=(0, -7.6, 4.6), rotation=(-4, 0, 0))
    cel_box(back, 7414, ring=1)
    bangs(g, "fringe", [(-2.8, ((2, 2), (1, 1)), 30), (-1.0, ((3, 2), (2, 1)), 40), (1.0, ((3, 2), (1, 1)), 44),
                        (2.9, ((2, 2), (1, 1)), -12)], seed=7420)
    flower(g, "pin", (-5.25, -6.8, -2.0), rotation=(0, 90, 0), size=5)
