"""Watchman Queue: hair drawn up tight from every side into a long thin tail from the back of the
crown, wrapped at the root and twice down its length in dark cloth, so it swings like a bell cord."""
from anime import bangs, lock, ring_shell, tie
from paint import scalp

META = {"name": "Watchman Queue", "gender": "unisex",
        "description": "Tight long thin tail from the back of the crown, wrapped three times in dark cloth."}

PIVOT, TILT = (0, -6.4, 4.6), (18, 0, 0)


def build(g):
    scalp(g, 25260, side_rows=4, back_rows=8, sideburn=1)
    ring_shell(g, 25261, side_rows=4, back_rows=8, ring_row=1)
    tie(g, "root_wrap", PIVOT, TILT, size=(3, 2, 3), y=-.6, key="K2")
    lock(g, "queue", PIVOT, TILT, ((2, 8), (2, 3), (1, 2)), 2, 25262, ring=None, motion="sway", y0=1.4)
    for i, y in enumerate((5.0, 9.0)):
        tie(g, f"wrap_{i}", PIVOT, TILT, size=(3, 1, 3), y=y, key="K2", motion="sway")
    bangs(g, "fringe", [(-2.4, ((2, 2), (1, 1)), 14), (2.4, ((2, 2), (1, 1)), -14)], seed=25266)
