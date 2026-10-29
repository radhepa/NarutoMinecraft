"""Hotaru Tail: Hotaru's hair, a soft fringe swept to the side above the brows, jaw-length locks
framing the face and the rest gathered in a short low tail at the nape, bound with a cloth tie."""
from anime import bangs, lock, ring_shell, sidelocks, tie
from paint import scalp

META = {"name": "Hotaru Tail", "gender": "unisex",
        "description": "Side-swept fringe, jaw-length face locks and a short low tail tied at the nape."}

PIVOT, TILT = (0, -3.4, 4.5), (16, 0, 0)


def build(g):
    scalp(g, 23021, side_rows=6, back_rows=8, sideburn=2)
    ring_shell(g, 23022, side_rows=5, back_rows=8, ring_row=1)
    bangs(g, "fringe", [(-3.1, ((2, 3), (1, 1)), 10), (-1.4, ((2, 2), (1, 1)), 24), (.6, ((2, 2), (1, 1)), 30),
                        (2.6, ((2, 2), (1, 1)), 34)], seed=23025)
    sidelocks(g, "frame", 7, seed=23030, x=4.3, z=-3.2, flare=5, width=2)
    tie(g, "tail_tie", PIVOT, TILT, size=(3, 1, 3), y=0.0, key="A2")
    lock(g, "tail", PIVOT, TILT, ((3, 3), (2, 2), (1, 1)), 2, 23035, y0=1.0)
