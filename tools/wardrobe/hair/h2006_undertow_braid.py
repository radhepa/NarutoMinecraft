"""Undertow Braid: hair parted in the middle and drawn low to the nape into one braid that hangs
down the back off to the left, bound in ink-dark cord, a soft parted fringe to the brows."""
from anime import bangs, braid, ring_shell, tie
from paint import scalp

META = {"name": "Undertow Braid", "gender": "unisex",
        "description": "Middle-parted hair drawn into one low braid hanging down the back, off to the left."}

PIVOT, TILT = (2.0, -2.6, 4.7), (-4, 0, -4)


def build(g):
    scalp(g, 20181, side_rows=6, back_rows=8, sideburn=2, part=3)
    ring_shell(g, 20182, side_rows=6, back_rows=8, ring_row=1)
    tie(g, "root_tie", PIVOT, TILT, size=(3, 1, 3), y=-.2, key="K2")
    end = braid(g, "braid", PIVOT, TILT, links=5, width=3, seed=20185, y0=.8)
    tie(g, "tail_tie", PIVOT, TILT, size=(2, 1, 2), y=end - 2.6, key="K2", motion="sway")
    bangs(g, "fringe", [(-2.9, ((2, 3), (1, 1)), 12), (-1.1, ((2, 2), (1, 1)), 16), (1.1, ((2, 2), (1, 1)), -16),
                        (2.9, ((2, 3), (1, 1)), -12)], seed=20195)
