"""Relaxed Shag: loose shoulder-length layers that were never really combed, a ragged middle part,
long uneven locks over the ears and the back cut in steps that flick out at every layer."""
from anime import back_fan, bangs, ring_shell, sidelocks
from kit_shiranui import flicks
from paint import scalp

META = {"name": "Relaxed Shag", "gender": "unisex",
        "description": "Loose shoulder-length layers, ragged middle part, the back cut in flicked steps."}


def build(g):
    scalp(g, 16300, side_rows=7, back_rows=8, sideburn=2, part=4)
    ring_shell(g, 16301, side_rows=7, back_rows=8, ring_row=1)
    bangs(g, "fringe", [(-3.0, ((2, 3), (1, 1)), 18), (-1.6, ((2, 2), (1, 1)), 10), (0.0, ((1, 2),), 0),
                        (1.6, ((2, 2), (1, 1)), -14), (3.0, ((2, 3), (1, 1)), -24)], seed=16302)
    sidelocks(g, "frame", 8, seed=16310, x=4.3, z=-2.9, flare=7, width=2)
    back_fan(g, "fall", [(-3.0, ((3, 4), (2, 2), (1, 1)), 18, 8), (-1.0, ((3, 6), (2, 2), (1, 1)), 4, 6),
                         (1.0, ((3, 5), (2, 2), (1, 1)), -6, 6), (3.0, ((3, 4), (2, 2), (1, 1)), -18, 8)], seed=16320)
    flicks(g, "layer_flick", -3.6, 16330, x=4.4, z=.4, segments=((2, 2), (1, 1)), splay=30)
    flicks(g, "nape_flick", .6, 16340, x=3.2, z=4.6, segments=((2, 2), (1, 1)), splay=30, back=True)
