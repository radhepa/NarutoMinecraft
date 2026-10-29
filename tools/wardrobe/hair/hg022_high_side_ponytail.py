"""High Side Ponytail: the hair swept up and tied high above the left ear into a full tail that
falls past the shoulder, a fringe swept toward the tail and a short lock left by the right ear."""
from anime import bangs, cel_box, lock, ring_shell, tie
from paint import scalp

META = {"name": "High Side Ponytail", "gender": "unisex",
        "description": "A full tail tied high above the left ear, past the shoulder, a fringe swept to it."}

PIVOT, TILT = (4.6, -7.0, 1.6), (6, 0, -22)
TAIL = ((4, 3), (4, 4), (3, 4), (3, 3), (2, 2), (1, 2))


def build(g):
    scalp(g, 33815, side_rows=5, back_rows=7, sideburn=2)
    ring_shell(g, 33816, side_rows=5, back_rows=7, ring_row=1)
    root = g.piece("tail_root", "HEAD", (-1.5, -2, -1.5), (3, 3, 3), pivot=PIVOT, rotation=TILT)
    cel_box(root, 33817, ring=1)
    tie(g, "tie", PIVOT, TILT, (4, 1, 4), y=.4, key="A2")
    lock(g, "tail", PIVOT, TILT, TAIL, 3, 33818, ring=None, motion="sway", y0=1.4)
    bangs(g, "fringe", [(-2.8, ((2, 2), (1, 1)), -10), (-1.2, ((3, 2), (2, 1)), -30), (.6, ((3, 2), (1, 1)), -44),
                        (2.4, ((2, 2), (1, 1)), -50)], seed=33825)
    lock(g, "frame_right", (-4.4, -7.6, -3.3), (0, 0, 3), ((2, 5), (1, 2)), 1, 33829, ring=1)
