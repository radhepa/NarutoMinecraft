"""Wrapped Tail: long hair tied low at the nape and bound in cloth down its length the way the clan
bound it for battle, a soft parted fringe and long locks framing the face to the collarbone."""
from anime import bangs, lock, ring_shell, sidelocks, tie
from paint import scalp

META = {"name": "Wrapped Tail", "gender": "unisex",
        "description": "Long low tail bound in cloth at three places, parted fringe, long face-framing locks."}

PIVOT, TILT = (0, -1.8, 4.7), (-6, 0, 0)


def build(g):
    scalp(g, 1192, side_rows=6, back_rows=8, sideburn=4, part=4)
    ring_shell(g, 1193, side_rows=6, back_rows=8, ring_row=1)
    bangs(g, "fringe", [(-2.7, ((2, 2), (1, 1)), 18), (-.9, ((2, 2), (1, 1)), 30),
                        (1.5, ((2, 2), (1, 1)), -26), (2.9, ((2, 2), (1, 1)), -14)], seed=1207)
    sidelocks(g, "frame", 11, seed=1212, x=4.3, z=-3.4, flare=3, width=2)
    lock(g, "tail", PIVOT, TILT, ((3, 4), (3, 4), (3, 4), (2, 2), (1, 2)), 3, 1217, ring=None, motion="sway")
    for i, y in enumerate((0, 4, 8)):
        tie(g, f"tail_wrap_{i}", PIVOT, TILT, (3, 1, 3), y=y + .5, key="A2", motion="sway")
