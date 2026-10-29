"""Ink Curtain: long straight black hair to the middle of the back with a heavy, blunt fringe cut
straight across at the brows and long side panels to the collarbone: a Root kunoichi's stillness."""
from anime import bangs, cel_box, curtain, ring_shell
from paint import scalp

META = {"name": "Ink Curtain", "gender": "unisex",
        "description": "Long straight hair to mid-back, a blunt fringe straight across the brows, long side panels."}


def build(g):
    scalp(g, 13462, side_rows=8, back_rows=8, sideburn=0)
    ring_shell(g, 13463, side_rows=8, back_rows=8, ring_row=1)
    curtain(g, "curtain", (0, -6.4, 4.6), (-7, 0, 0), 9, 12, hem=[(0, 3, 1), (3, 3, 2), (6, 3, 1)], seed=13464)
    for side, x in (("right", -4.65), ("left", 4.65)):
        panel = g.piece(f"panel_{side}", "HEAD", (-.5, 0, -4.1), (1, 11, 4), pivot=(x, -7.6, 0))
        cel_box(panel, 13465 + (x > 0), ring=1, clump=3)
    bar = g.piece("fringe_bar", "HEAD", (-4.5, -8.4, -4.6), (9, 2, 1))
    cel_box(bar, 13467, ring=0, clump=3)
    bangs(g, "fringe", [(x, ((2, 2),), 0) for x in (-3.2, -1.6, 0, 1.6, 3.2)], seed=13468)
