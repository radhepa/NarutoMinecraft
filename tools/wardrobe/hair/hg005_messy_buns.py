"""Messy Buns: two round buns twisted up on top of the head, a few short ends poking out of each, with
a light fringe and loose wisps at the temples."""
from anime import bangs, cel_box, ring_shell, sidelocks, spike, tie
from paint import scalp

META = {"name": "Messy Buns", "gender": "female",
        "description": "Two round buns on top of the head with short ends poking out, a light fringe, temple wisps."}


def build(g):
    scalp(g, 31810, side_rows=5, back_rows=8, sideburn=2)
    ring_shell(g, 31811, side_rows=4, back_rows=8, ring_row=1)
    bangs(g, "fringe", [(-2.6, ((2, 2), (1, 1)), 20), (-.6, ((2, 2), (1, 1)), 10), (1.6, ((2, 2), (1, 1)), -16)],
          seed=31812)
    sidelocks(g, "wisp", 5, seed=31815, x=4.3, z=-3.4, flare=6, width=1)
    for side, sign in (("right", -1), ("left", 1)):
        x = 2.4 * sign
        tie(g, f"bun_tie_{side}", (x, -8.0, .6), (0, 0, -16 * sign), (3, 1, 3), key="A2")
        bun = g.piece(f"bun_{side}", "HEAD", (-2, -4, -2), (4, 3, 4), pivot=(x, -8.0, .6), rotation=(0, 0, -16 * sign))
        cel_box(bun, 31818 + (sign > 0), ring=0)
        cap = g.piece(f"bun_top_{side}", "HEAD", (-1.5, -5, -1.5), (3, 1, 3), pivot=(x, -8.0, .6), rotation=(0, 0, -16 * sign))
        cel_box(cap, 31820 + (sign > 0), top_delta=2)
        for i, (rx, rz) in enumerate(((-40, 30 * sign), (30, 60 * sign), (10, -20 * sign))):
            spike(g, f"bun_end_{side}_{i}", (x + .6 * sign, -11.0, .6), (rx, 0, rz), ((1, 2), (1, 1)), 1, 31822 + i * 2)
