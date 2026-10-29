"""Ink Bob: a sleek chin-length bob, cut level all round and curving in at the jaw, with a deep side
part and the fringe brushed across the brow in one stroke, like a single sweep of ink."""
from anime import cel_box, curtain, ring_shell
from kit_kurama import part_line, side_fringe
from paint import scalp

META = {"name": "Ink Bob", "gender": "unisex",
        "description": "Sleek chin-length bob curving in at the jaw, deep side part, one-stroke swept fringe."}


def build(g):
    scalp(g, 12160, side_rows=8, back_rows=8, sideburn=0, part=2)
    ring_shell(g, 12161, side_rows=7, back_rows=8, ring_row=1)
    part_line(g, 2)
    curtain(g, "back", (0, -7.2, 4.5), (-4, 0, 0), 9, 7, hem=[(1, 3, 1), (5, 3, 1)], seed=12162)
    for side, sign in (("right", -1), ("left", 1)):
        panel = g.piece(f"side_{side}", "HEAD", (-.5, 0, -3.5), (1, 7, 8), pivot=(4.6 * sign, -7.6, .2))
        cel_box(panel, 12170 + (sign > 0), ring=1)
        panel.bottom.fill("H0")
        panel.front.hline(0, 7, 6, "H1")
    side_fringe(g, "fringe", 12180, side=1)
