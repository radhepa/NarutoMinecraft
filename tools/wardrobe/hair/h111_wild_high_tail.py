"""Wild High Tail: hair dragged up into a high tail on the crown that bursts into spiky points, rough
locks left over the ears and a short ragged fringe, a fighter's no-nonsense tie."""
from anime import bangs, cel_box, lock, ring_shell, sidelocks, spike
from paint import scalp

META = {"name": "Wild High Tail", "gender": "unisex",
        "description": "A high crown tail bursting into spiky points, rough side locks, short ragged fringe."}


def build(g):
    scalp(g, 1320, side_rows=5, back_rows=7, sideburn=3)
    ring_shell(g, 1321, side_rows=4, back_rows=6, ring_row=1)
    bangs(g, "fringe", [(-2.6, ((2, 2), (1, 1)), 26), (-.6, ((2, 1), (1, 1)), 12), (1.4, ((2, 1), (1, 1)), -14),
                        (3.0, ((2, 2), (1, 1)), -24)], seed=1335)
    sidelocks(g, "frame", 6, seed=1340, x=4.4, z=-3.2, flare=10, width=2)
    tie = g.piece("tie", "HEAD", (-1.5, -1, -1.5), (3, 2, 3), pivot=(0, -7.4, 3.6))
    cel_box(tie, 1345, base=0, top_delta=0)
    # The tail: a short root, then points bursting out and down.
    lock(g, "tail_root", (0, -8.2, 4.4), (40, 0, 0), ((4, 3),), 3, 1347, ring=None)
    for i, (rx, rz, segs) in enumerate(((34, 0, ((3, 4), (2, 3), (1, 2))), (22, -22, ((3, 3), (2, 3), (1, 1))),
                                        (22, 22, ((3, 3), (2, 3), (1, 1))), (12, -8, ((3, 5), (2, 4), (1, 2))),
                                        (12, 8, ((3, 5), (2, 4), (1, 2))))):
        lock(g, f"tail_point_{i}", (0, -6.8, 6.6), (rx, 0, rz), segs, 2, 1350 + i * 2, ring=None, motion="sway")
    spike(g, "crown_burst", (0, -8.6, 5.6), (-30, 0, 0), ((3, 2), (2, 1), (1, 1)), 2, 1360)
