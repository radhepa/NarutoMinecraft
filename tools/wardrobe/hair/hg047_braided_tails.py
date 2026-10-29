"""Braided Tails: hair parted in the middle and drawn back into two long three-strand braids that
hang behind the shoulders, bound at the ends with cord, a short split fringe at the brows."""
from anime import bangs, braid, ring_shell, tie
from paint import scalp

META = {"name": "Braided Tails", "gender": "unisex",
        "description": "Centre-parted hair in two long braids hanging behind the shoulders, cord ends, a short split fringe."}


def build(g):
    scalp(g, 35740, side_rows=6, back_rows=8, sideburn=3, part=3)
    ring_shell(g, 35741, side_rows=6, back_rows=8, ring_row=1)
    bangs(g, "fringe", [(-2.8, ((2, 2), (1, 1)), 22), (-1.2, ((2, 1), (1, 1)), 30),
                        (1.2, ((2, 1), (1, 1)), -30), (2.8, ((2, 2), (1, 1)), -22)], seed=35742)
    for side, sign in (("right", -1), ("left", 1)):
        pivot = (2.6 * sign, -2.6, 4.2)
        rot = (-14, 0, -8 * sign)
        tie(g, f"{side}_root_tie", pivot, rot, (3, 1, 3), y=-.6)
        end = braid(g, f"{side}_braid", pivot, rot, links=6, width=3, seed=35746 + (sign > 0) * 6)
        tie(g, f"{side}_end_cord", pivot, rot, (2, 1, 2), y=end - 3.0, key="L2", motion="sway")
