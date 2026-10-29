"""Foundation Tail: after Fu of Root: long straight hair swept back from a clear brow, a short
fringe of points at the hairline, locks before the ears and the length tied high at the back of
the crown, falling past the shoulders."""
from anime import bangs, lock, ring_shell, sidelocks, tie
from paint import scalp

META = {"name": "Foundation Tail", "gender": "unisex",
        "description": "Long hair swept back from the brow and tied high at the crown, falling past the shoulders."}


def build(g):
    scalp(g, 13132, side_rows=5, back_rows=8, sideburn=3)
    ring_shell(g, 13133, side_rows=5, back_rows=8, ring_row=1)
    bangs(g, "fringe", [(-2.6, ((2, 2), (1, 1)), 22), (2.6, ((2, 2), (1, 1)), -22)], seed=13138)
    sidelocks(g, "frame", 7, seed=13144, x=4.35, z=-3.2, flare=3, width=1)
    tie(g, "tie", (0, -6.8, 4.5), (14, 0, 0), size=(3, 1, 3), key="A2")
    lock(g, "tail", (0, -6.3, 4.9), (16, 0, 0), ((3, 4), (3, 4), (3, 3), (2, 3), (1, 1)), 2, 13150, ring=None,
         motion="sway")
