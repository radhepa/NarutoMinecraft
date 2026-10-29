"""Silk Tail: everything drawn up into a high ponytail on the crown, smooth as reeled silk, bound with
a band of thread and falling long down the back."""
from anime import lock, ring_shell, sidelocks, tie
from paint import scalp

META = {"name": "Silk Tail", "gender": "unisex",
        "description": "Hair drawn up into a high thread-bound ponytail falling long down the back."}

PIVOT, TILT = (0, -7.4, 3.6), (20, 0, 0)


def build(g):
    scalp(g, 23201, side_rows=4, back_rows=8, sideburn=2)
    hat = ring_shell(g, 23202, side_rows=3, back_rows=8, ring_row=1)
    for x in range(0, 8, 2):
        hat.back.vline(x, 2, 7, "H1")
    tie(g, "tail_tie", PIVOT, TILT, size=(3, 2, 3), y=-1.0, key="A2", motion="sway")
    lock(g, "tail", PIVOT, TILT, ((3, 4), (3, 4), (2, 3), (1, 2)), 3, 23205, motion="sway", y0=1.0)
    sidelocks(g, "frame", 5, seed=23210, x=4.35, z=-3.2, flare=4, width=1)
