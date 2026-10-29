"""Half Up: straight shoulder-length hair with the top half gathered into a small tail at the back
of the crown, the rest left loose over the nape; parted bangs leave the brow clear."""
from anime import bangs, curtain, lock, ring_shell, sidelocks, tie
from paint import scalp

META = {"name": "Half Up", "gender": "unisex",
        "description": "Shoulder-length straight hair, the top half tied in a small tail, parted bangs."}


def build(g):
    scalp(g, 13429, side_rows=7, back_rows=8, sideburn=3)
    ring_shell(g, 13430, side_rows=7, back_rows=8, ring_row=1)
    curtain(g, "loose", (0, -4.6, 4.55), (-6, 0, 0), 9, 6, hem=[(0, 3, 2), (3, 3, 1), (6, 3, 2)], seed=13431)
    bangs(g, "fringe", [(-2.6, ((2, 2), (1, 1)), 18), (-1.1, ((2, 1), (1, 1)), 30),
                        (1.1, ((2, 1), (1, 1)), -30), (2.6, ((2, 2), (1, 1)), -18)], seed=13432)
    sidelocks(g, "frame", 8, seed=13433, x=4.35, z=-3.3, flare=3, width=2)
    tie(g, "tie", (0, -6.6, 4.6), (20, 0, 0), size=(2, 1, 2), key="K2")
    lock(g, "tail", (0, -6.1, 4.9), (24, 0, 0), ((2, 3), (2, 2), (1, 1)), 1, 13434, ring=None, motion="sway")
