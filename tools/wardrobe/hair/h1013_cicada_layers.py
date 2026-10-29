"""Cicada Layers: shoulder-length hair cut in two tiers of pointed layers, the upper tier short
and spiky, the lower one long and straight to the collar."""
from anime import back_fan, bangs, lock, ring_shell
from paint import scalp

META = {"name": "Cicada Layers", "gender": "unisex",
        "description": "Shoulder-length hair in two tiers of pointed layers, brow-length fringe."}

UPPER = [(-3.4, ((2, 3), (1, 1)), 26, 30), (-1.2, ((3, 3), (1, 2)), 10, 34), (1.2, ((3, 3), (1, 2)), -10, 34),
         (3.4, ((2, 3), (1, 1)), -26, 30)]
LOWER = [(-3.0, ((3, 7), (2, 2), (1, 1)), 10, 6), (0, ((3, 8), (2, 2), (1, 1)), 0, 8),
         (3.0, ((3, 7), (2, 2), (1, 1)), -10, 6)]


def build(g):
    scalp(g, 10391, side_rows=6, back_rows=8, sideburn=3)
    ring_shell(g, 10392, side_rows=7, back_rows=8, ring_row=1)
    back_fan(g, "lower", LOWER, seed=10400, z=4.25, motion="sway")
    back_fan(g, "upper", UPPER, seed=10410, z=4.6)
    for side, sign in (("right", -1), ("left", 1)):
        lock(g, f"side_{side}", (4.45 * sign, -7.4, .4), (4, 0, -6 * sign), ((2, 7), (1, 2)), 4, 10420 + (sign > 0),
             ring=1, motion="sway")
    bangs(g, "fringe", [(-2.8, ((2, 2), (1, 1)), 18), (-.9, ((2, 2),), 10), (.9, ((2, 2),), -10),
                        (2.8, ((2, 2), (1, 1)), -18)], seed=10430)
