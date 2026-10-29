"""Shaggy Medic: a choppy, overgrown cut to the nape that nobody in the infirmary has time to trim,
uneven points all round, a few longer locks at the sides and a ragged fringe to the brows."""
from anime import back_fan, bangs, lock, ring_shell
from paint import scalp

META = {"name": "Shaggy Medic", "gender": "unisex",
        "description": "Choppy overgrown cut to the nape, uneven points, ragged fringe to the brows."}


def build(g):
    scalp(g, 24201, side_rows=6, back_rows=8, sideburn=2)
    ring_shell(g, 24202, side_rows=5, back_rows=8, ring_row=1)
    back_fan(g, "back", [(-3.0, ((2, 3), (1, 2)), 14, 8), (-1.2, ((3, 4), (2, 1)), 4, 6), (1.2, ((3, 3), (1, 2)), -6, 6),
                         (3.0, ((2, 4), (1, 1)), -14, 8)], seed=24205)
    for side, sign in (("right", -1), ("left", 1)):
        lock(g, f"side_{side}", (4.4 * sign, -7.4, -1.0), (0, 0, -10 * sign), ((2, 3), (1, 2)), 2, 24220 + (sign > 0))
        lock(g, f"cheek_{side}", (4.3 * sign, -7.6, -3.2), (0, 0, -16 * sign), ((1, 4),), 1, 24224 + (sign > 0))
    bangs(g, "fringe", [(-2.9, ((2, 2), (1, 1)), 20), (-1.2, ((2, 3),), -12), (.6, ((2, 2), (1, 1)), 18),
                        (2.4, ((2, 3),), -20), (3.4, ((1, 3),), -4)], seed=24230)
