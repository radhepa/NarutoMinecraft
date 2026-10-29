"""Low Ponytail: long straight dark hair parted in the middle, face-framing locks to the chin and the
length gathered low at the nape into a tie, falling to the middle of the back."""
from anime import bangs, cel_box, lock, ring_shell, sidelocks
from paint import scalp

META = {"name": "Low Ponytail", "gender": "unisex",
        "description": "Straight hair parted in the middle, face-framing locks, a low ponytail to mid-back."}


def build(g):
    scalp(g, 701, side_rows=6, back_rows=8, sideburn=4)
    ring_shell(g, 702, side_rows=6, back_rows=8, ring_row=1)
    bangs(g, "fringe", [(-2.7, ((2, 2), (1, 1)), 18), (-1.3, ((2, 1), (1, 1)), 28),
                        (1.3, ((2, 1), (1, 1)), -28), (2.7, ((2, 2), (1, 1)), -18)], seed=730)
    sidelocks(g, "frame", 9, seed=740, x=4.3, z=-3.4, flare=3, width=2)
    tie = g.piece("tie", "HEAD", (-1.5, 0, -1), (3, 1, 2), pivot=(0, -1.2, 4.7))
    cel_box(tie, 750, base=0, top_delta=0)
    lock(g, "ponytail", (0, -.2, 4.8), (-10, 0, 0), ((3, 4), (3, 4), (2, 3), (1, 1)), 2, 760, ring=None, motion="sway")
