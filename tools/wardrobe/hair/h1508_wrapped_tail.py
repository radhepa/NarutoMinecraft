"""Wrapped Tail: long hair gathered low at the nape and bound down its length with cloth, the way a
sword hilt is wrapped, ending in a loose brush below the shoulder blades. Parted fringe."""
from anime import bangs, lock, ring_shell, sidelocks, tie
from paint import scalp

META = {"name": "Wrapped Tail", "gender": "unisex",
        "description": "Low tail bound with cloth wraps down its length, a loose brush end, parted fringe."}

PIVOT, TILT = (0, -1.4, 4.7), (-8, 0, 0)


def build(g):
    scalp(g, 15200, side_rows=6, back_rows=8, sideburn=4, part=3)
    ring_shell(g, 15201, side_rows=6, back_rows=8, ring_row=1)
    lock(g, "tail", PIVOT, TILT, ((3, 3), (3, 3), (3, 3), (2, 2), (1, 1)), 2, 15205, ring=None, motion="sway")
    for i, y in enumerate((-.2, 2.6, 5.6)):
        tie(g, f"wrap_{i}", PIVOT, TILT, size=(4, 1, 3), y=y, key="D2", motion="sway")
    bangs(g, "fringe", [(-2.7, ((2, 2), (1, 1)), 18), (-1.2, ((2, 1),), 26), (1.2, ((2, 1),), -26),
                        (2.7, ((2, 2), (1, 1)), -18)], seed=15215)
    sidelocks(g, "frame", 7, seed=15220, x=4.3, z=-3.3, flare=4, width=1)
