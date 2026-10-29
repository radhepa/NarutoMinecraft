"""Florist Bun: hair swept up off the neck into a round bun at the back of the crown, tied with a
ribbon and pinned with a blossom, short side-swept bangs and two loose strands at the temples,
the way the flower shop is worked in."""
from anime import bangs, cel_box, lock, ring_shell, tie
from kit_yamanaka import flower
from paint import scalp

META = {"name": "Florist Bun", "gender": "unisex",
        "description": "Round bun at the back of the crown with a ribbon and blossom, side-swept bangs, loose strands."}


def build(g):
    scalp(g, 7501, side_rows=4, back_rows=7, sideburn=2)
    ring_shell(g, 7502, side_rows=3, back_rows=6, ring_row=1)
    bun = g.piece("bun", "HEAD", (-2.5, -2.5, -1.5), (5, 5, 4), pivot=(0, -7.4, 5.2), rotation=(-30, 0, 0))
    cel_box(bun, 7510, ring=1, clump=2)
    knot = g.piece("bun_top", "HEAD", (-1.5, -1.5, -1), (3, 1, 3), pivot=(0, -9.6, 4.6), rotation=(-30, 0, 0))
    cel_box(knot, 7511, top_delta=1)
    tie(g, "ribbon", (0, -7.4, 5.2), (-30, 0, 0), (6, 1, 5), y=1.8, key="A2")
    flower(g, "pin", (2.9, -8.4, 4.8), rotation=(0, -60, 0), size=5)
    bangs(g, "fringe", [(-2.7, ((2, 2), (1, 1)), 34), (-.9, ((3, 2), (1, 1)), 44), (1.1, ((2, 2), (1, 1)), 40),
                        (2.9, ((2, 1),), -10)], seed=7520)
    for side, sign in (("right", -1), ("left", 1)):
        lock(g, f"strand_{side}", (4.4 * sign, -7.4, -3.2), (0, 0, -6 * sign), ((1, 6), (1, 2)), 1, 7530 + (sign > 0))
