"""Warring Topknot: the samurai way of the clan's old soldiers. Hair pulled tight off the face and
tied on the crown in a knot with a short folded queue lying forward, and short sideburn locks."""
from anime import lock, ring_shell, tie
from kit_senju import bun
from paint import scalp

META = {"name": "Warring Topknot", "gender": "unisex",
        "description": "Hair drawn tight to a knot on the crown with a short queue folded forward, sideburn locks."}


def build(g):
    scalp(g, 1160, side_rows=4, back_rows=7, sideburn=3, part=None)
    ring_shell(g, 1161, side_rows=3, back_rows=6, ring_row=1)
    bun(g, "crown_knot", (0, -8.9, 1.4), (3, 2, 3), seed=1165)
    tie(g, "crown_tie", (0, -8.4, 1.4), size=(3, 1, 3), y=-.5)
    # The queue folds forward over the top of the head.
    lock(g, "crown_queue", (0, -9.6, 1.0), (-100, 0, 0), ((2, 3), (2, 1)), 2, 1170, ring=None)
    for side, sign in (("right", -1), ("left", 1)):
        lock(g, f"burn_{side}", (4.3 * sign, -6.4, -3.0), (0, 0, -2 * sign), ((1, 3), (1, 1)), 1, 1175 + (sign > 0))
