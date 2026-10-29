"""Scout Tail: hair pulled back hard into a low ponytail and bound its whole length in a dark cloth
wrap so it cannot catch on branches, only a pointed tip left free, a few short points over the brow."""
from anime import bangs, lock, ring_shell, sidelocks, tie
from paint import scalp

META = {"name": "Scout Tail", "gender": "unisex",
        "description": "Low ponytail bound its length in a dark cloth wrap, pointed tip, short brow points."}

PIVOT, TILT = (0, -3.4, 4.5), (14, 0, 0)


def build(g):
    scalp(g, 25080, side_rows=5, back_rows=8, sideburn=2)
    ring_shell(g, 25081, side_rows=5, back_rows=8, ring_row=1)
    lock(g, "tail", PIVOT, TILT, ((3, 7), (2, 2), (1, 2)), 2, 25082, ring=None, motion="sway")
    for i, y in enumerate((.2, 2.2, 4.2)):
        tie(g, f"wrap_{i}", PIVOT, TILT, size=(4, 1, 3), y=y, key="K2", motion="sway")
    bangs(g, "fringe", [(-2.6, ((2, 2), (1, 1)), 18), (-.6, ((2, 1), (1, 1)), 8), (1.6, ((2, 2), (1, 1)), -12)],
          seed=25086)
    sidelocks(g, "ear", 5, seed=25089, x=4.4, z=-2.2, flare=8, width=1)
