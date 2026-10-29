"""Cropped Flick: short and practical, cut close over the ears with a light fringe pushed to the
side and the nape left just long enough to kick up at the collar."""
from anime import back_fan, bangs, ring_shell
from kit_shiranui import flicks
from paint import scalp

META = {"name": "Cropped Flick", "gender": "unisex",
        "description": "Short crop close over the ears, a light side fringe, the nape kicking up at the collar."}


def build(g):
    scalp(g, 16400, side_rows=5, back_rows=7, sideburn=2, part=2)
    ring_shell(g, 16401, side_rows=4, back_rows=7, ring_row=1)
    bangs(g, "fringe", [(-2.8, ((2, 2), (1, 1)), 26), (-1.2, ((2, 2),), 32), (0.4, ((2, 2),), 36),
                        (2.2, ((2, 2),), 22)], seed=16402)
    back_fan(g, "nape", [(-2.4, ((3, 3), (2, 1)), 10, 10), (0, ((3, 4), (2, 1)), 0, 8), (2.4, ((3, 3), (2, 1)), -10, 10)],
             seed=16410)
    flicks(g, "nape_flick", -2.2, 16420, x=2.8, z=4.6, segments=((2, 2), (1, 1)), splay=30, back=True)
