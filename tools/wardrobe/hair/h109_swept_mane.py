"""Swept Mane: long hair parted far to one side, the fringe swept across the brow, the length down
the back and one long lock brought forward over the left shoulder."""
from anime import bangs, curtain, lock, ring_shell, sidelocks
from kit_senju import side_panels
from paint import scalp

META = {"name": "Swept Mane", "gender": "unisex",
        "description": "Side-parted long hair, fringe swept across the brow, one long lock over the left shoulder."}


def build(g):
    scalp(g, 1256, side_rows=7, back_rows=8, sideburn=4, part=1)
    ring_shell(g, 1257, side_rows=7, back_rows=8, ring_row=1)
    curtain(g, "curtain", (0, -6.2, 4.7), (-6, 0, 0), 9, 13, hem=[(0, 3, 2), (3, 3, 3), (6, 3, 2)], seed=1261)
    side_panels(g, "side", 9, 1266)
    bangs(g, "fringe", [(-3.0, ((2, 2), (1, 1)), 40), (-1.4, ((3, 2), (2, 1)), 52), (.6, ((3, 2), (2, 1)), 56),
                        (2.6, ((2, 2), (1, 1)), 44)], seed=1271)
    sidelocks(g, "frame", 8, seed=1276, x=4.3, z=-3.5, flare=2, width=2)
    # The long lock brought forward over the left shoulder.
    lock(g, "shoulder_lock", (4.4, -5.5, -2.6), (0, 0, -14), ((3, 5), (3, 5), (2, 3), (1, 2)), 2, 1281, motion="sway")
