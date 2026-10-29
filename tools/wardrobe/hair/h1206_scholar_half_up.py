"""Scholar's Half-Up: the upper half drawn back into a small round knot behind the crown, tied with a
cord, the rest falling straight to the shoulders. A centre part with soft bangs to the brows and
long face-framing strands: a calm, tidy look for a student of the brush."""
from anime import bangs, curtain, ring_shell, sidelocks, tie
from kit_kurama import bun
from paint import scalp

META = {"name": "Scholar's Half-Up", "gender": "unisex",
        "description": "Upper half tied in a small knot behind the crown, the rest straight to the shoulders."}


def build(g):
    scalp(g, 12200, side_rows=7, back_rows=8, sideburn=2, part=3)
    ring_shell(g, 12201, side_rows=7, back_rows=8, ring_row=1)
    curtain(g, "back", (0, -5.0, 4.6), (-6, 0, 0), 9, 8, hem=[(0, 2, 2), (3, 3, 2), (7, 2, 2)], seed=12202)
    tie(g, "cord", (0, -6.9, 4.7), (80, 0, 0), size=(2, 1, 2), key="A2")
    bun(g, "knot", (0, -7.0, 5.9), size=3, seed=12210)
    bangs(g, "fringe", [(-2.7, ((2, 2), (1, 1)), 14), (-1.2, ((2, 1), (1, 1)), 26),
                        (1.2, ((2, 1), (1, 1)), -26), (2.7, ((2, 2), (1, 1)), -14)], seed=12214)
    sidelocks(g, "frame", 9, seed=12226, x=4.3, z=-3.4, flare=2, width=1)
