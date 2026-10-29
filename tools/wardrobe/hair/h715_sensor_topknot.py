"""Sensor Topknot: hair cropped close round the sides and nape and drawn up into a tight topknot on
the crown, bound in a cloth wrap, with short soft points over the brow."""
from anime import bangs, cel_box, lock, ring_shell, tie
from paint import scalp

META = {"name": "Sensor Topknot", "gender": "unisex",
        "description": "Close sides and nape, a tight wrapped topknot on the crown, short brow points."}


def build(g):
    scalp(g, 7371, side_rows=3, back_rows=6, sideburn=1)
    ring_shell(g, 7372, side_rows=2, back_rows=5, ring_row=1)
    base = g.piece("knot_base", "HEAD", (-2, -1, -2), (4, 1, 4), pivot=(0, -8.0, 1.0))
    cel_box(base, 7380, ring=0)
    tie(g, "wrap", (0, -9.0, 1.0), (0, 0, 0), (3, 2, 3), y=-1, key="P2")
    knot = g.piece("knot", "HEAD", (-1.5, -3, -1.5), (3, 3, 3), pivot=(0, -10.0, 1.0), rotation=(-10, 0, 0))
    cel_box(knot, 7385, ring=1)
    lock(g, "knot_tip", (0, -12.8, .6), (-160, 0, 0), ((2, 2), (1, 1)), 2, 7388)
    bangs(g, "fringe", [(-2.6, ((2, 1), (1, 1)), 24), (-.8, ((2, 1),), 10), (1.0, ((2, 1), (1, 1)), -14),
                        (2.7, ((2, 1),), -20)], seed=7390)
    for side, sign in (("right", -1), ("left", 1)):
        lock(g, f"temple_{side}", (4.35 * sign, -7.4, -2.8), (0, 0, -6 * sign), ((1, 3), (1, 1)), 1, 7395 + (sign > 0))
