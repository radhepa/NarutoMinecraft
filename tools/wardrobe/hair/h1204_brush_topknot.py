"""Brush Topknot: everything gathered up into a round knot on the crown and pinned with a paint brush
pushed straight through it, the way a painter keeps hair out of the ink. Short wisps at the temples
and a light fringe stay down."""
from anime import bangs, lock, ring_shell, tie
from kit_kurama import brush_pin, bun
from paint import scalp

META = {"name": "Brush Topknot", "gender": "unisex",
        "description": "A round knot on the crown pinned through with a paint brush, temple wisps, a light fringe."}


def build(g):
    scalp(g, 12120, side_rows=4, back_rows=7, sideburn=2)
    ring_shell(g, 12121, side_rows=3, back_rows=6, ring_row=1)
    tie(g, "knot_tie", (0, -8.5, .6), size=(4, 1, 4))
    bun(g, "knot", (0, -9.9, .6), size=4, seed=12124)
    brush_pin(g, "brush", (-2.4, -10.4, .4), (0, 0, -100), length=11)
    bangs(g, "fringe", [(-2.6, ((2, 2), (1, 1)), 22), (-.4, ((2, 1),), 6), (1.8, ((2, 2), (1, 1)), -20)], seed=12130)
    for side, sign in (("right", -1), ("left", 1)):
        lock(g, f"wisp_{side}", (4.3 * sign, -7.4, -3.4), (0, 0, -6 * sign), ((1, 4), (1, 2)), 1, 12140 + (sign > 0))
