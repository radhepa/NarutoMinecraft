"""Half-Up Knot: the top half of the hair twisted into a small knot at the back of the crown and the
rest left hanging straight to the shoulders, a soft centre fringe and side locks tucked behind the ears."""
from anime import bangs, cel_box, curtain, ring_shell, tie
from paint import scalp

META = {"name": "Half-Up Knot", "gender": "unisex",
        "description": "Top half twisted into a small crown knot, the rest hanging straight to the shoulders."}


def build(g):
    scalp(g, 22201, side_rows=7, back_rows=8, sideburn=3)
    ring_shell(g, 22202, side_rows=7, back_rows=8, ring_row=1)
    knot = g.piece("knot", "HEAD", (-2, -1.5, -1.5), (4, 3, 3), pivot=(0, -7.2, 5.4), rotation=(-30, 0, 0))
    cel_box(knot, 22203, ring=0)
    tie(g, "knot_tie", (0, -7.2, 5.4), (-30, 0, 0), (4, 1, 3), y=1.4, key="A2")
    curtain(g, "fall", (0, -5.2, 4.3), (6, 0, 0), 8, 9, hem=((0, 2, 2), (2, 2, 3), (4, 2, 2), (6, 2, 3)), seed=22205)
    bangs(g, "fringe", [(-2.6, ((2, 2), (1, 1)), 20), (-.8, ((2, 2),), 10), (1.0, ((2, 2),), -12),
                        (2.7, ((2, 2), (1, 1)), -22)], seed=22212)
