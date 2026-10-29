"""Half-Up Knot: the upper hair drawn back into a small knot behind the crown, the rest left long and
straight down the back, a fringe swept apart at the brow and fine locks framing the face."""
from anime import bangs, curtain, ring_shell, sidelocks
from kit_senju import bun, side_panels
from paint import scalp

META = {"name": "Half-Up Knot", "gender": "unisex",
        "description": "Upper hair in a small knot behind the crown, the rest long and straight, framing locks."}


def build(g):
    scalp(g, 1416, side_rows=7, back_rows=8, sideburn=4, part=4)
    ring_shell(g, 1417, side_rows=7, back_rows=8, ring_row=1)
    curtain(g, "curtain", (0, -5.6, 4.7), (-6, 0, 0), 9, 13, hem=[(1, 3, 2), (5, 3, 2)], seed=1421)
    side_panels(g, "side", 9, 1426)
    bun(g, "knot", (0, -6.6, 5.4), (3, 3, 2), seed=1431, wrap="A2")
    bangs(g, "fringe", [(-2.8, ((2, 2), (1, 1)), 22), (-1.2, ((2, 1), (1, 1)), 38),
                        (1.2, ((2, 1), (1, 1)), -38), (2.8, ((2, 2), (1, 1)), -22)], seed=1436)
    sidelocks(g, "frame", 10, seed=1441, x=4.3, z=-3.5, flare=2, width=1)
