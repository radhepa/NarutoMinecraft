"""Shaggy Shoulder: straight hair cut in long ragged layers to the shoulders, a choppy fringe that
stops at the brows and uneven locks splaying over the ears and nape."""
from anime import back_fan, bangs, sidelocks
from kit_hyuga import crown

META = {"name": "Shaggy Shoulder", "gender": "unisex",
        "description": "Ragged shoulder-length layers, a choppy brow fringe, uneven locks over ears and nape."}


def build(g):
    crown(g, 4521, side_rows=7, back_rows=8, sideburn=3)
    back_fan(g, "layer", [(-3.4, ((3, 5), (2, 3), (1, 1)), 14, 8), (-1.2, ((3, 6), (2, 3), (1, 1)), 4, 6),
                          (1.2, ((3, 5), (2, 4), (1, 1)), -4, 7), (3.4, ((3, 6), (2, 2), (1, 1)), -14, 8),
                          (0, ((4, 4), (3, 2)), 0, 14)], seed=4525, z=4.4, motion="sway")
    for side, sign in (("right", -1), ("left", 1)):
        back_fan(g, f"ear_{side}", [(4.0 * sign, ((2, 6), (2, 2), (1, 1)), -10 * sign, 0),
                                    (4.1 * sign, ((2, 5), (1, 2)), -16 * sign, 16)], seed=4535 + (sign > 0) * 5, z=1.6)
    bangs(g, "fringe", [(-2.9, ((2, 2), (1, 1)), 22), (-1.2, ((2, 1), (1, 1)), 12), (.6, ((2, 1), (1, 1)), -16),
                        (2.4, ((2, 2), (1, 1)), -24)], seed=4545)
    sidelocks(g, "frame", 8, seed=4550, x=4.3, z=-3.5, flare=4, width=2)
