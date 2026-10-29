"""Wind-Tossed Tail: long hair caught at the nape in a cloth tie and thrown back in a heavy tail to
the middle of the back, loose wisps escaping at the temples and a rough fringe blown to one side."""
from anime import bangs, lock, ring_shell, sidelocks, tie
from paint import scalp

META = {"name": "Wind-Tossed Tail", "gender": "unisex",
        "description": "Long hair in a cloth-tied low tail to mid-back, loose temple wisps, a fringe blown to one side."}


def build(g):
    scalp(g, 35760, side_rows=6, back_rows=8, sideburn=3)
    ring_shell(g, 35761, side_rows=6, back_rows=8, ring_row=1)
    bangs(g, "fringe", [(-2.8, ((3, 2), (2, 1), (1, 1)), 34), (-.9, ((3, 2), (2, 1)), 36),
                        (1.2, ((2, 2), (1, 1)), 26), (3.0, ((2, 2), (1, 1)), 4)], seed=35762)
    sidelocks(g, "wisp", 7, seed=35764, x=4.4, z=-3.2, flare=14, width=1)
    tie(g, "tail_tie", (0, -2.0, 4.6), (10, 0, 0), (3, 2, 2), key="S3")
    lock(g, "tail", (0, -1.2, 4.9), (18, 0, 6), ((3, 4), (3, 4), (3, 3), (2, 3), (1, 2)), 2, 35766, ring=None,
         motion="sway")
    lock(g, "tail_stray", (.6, -1.0, 5.2), (34, 0, -18), ((2, 3), (1, 3)), 1, 35772, ring=None, motion="sway")
