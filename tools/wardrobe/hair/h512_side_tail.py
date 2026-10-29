"""Side Tail: a relaxed side tail. The hair gathered loosely over the left ear into a short tail
that splits into stiff points over the shoulder, a soft side-parted fringe."""
from anime import bangs, lock, ring_shell, sidelocks, tie
from paint import scalp

META = {"name": "Side Tail", "gender": "unisex",
        "description": "Gathered low over the left ear in a short spiky tail, soft side-parted fringe."}


def build(g):
    scalp(g, 5701, side_rows=6, back_rows=8, sideburn=1, part=2)
    ring_shell(g, 5702, side_rows=6, back_rows=8, ring_row=1)
    pivot = (4.6, -3.6, 2.0)
    tie(g, "tie", pivot, (0, 0, -10), (2, 2, 3))
    for i, (segs, rx, rz) in enumerate(((((3, 3), (2, 2), (1, 2)), 10, -14), (((2, 3), (1, 2)), 34, -22),
                                        (((2, 3), (1, 2)), -16, -26), (((2, 2), (1, 1)), 6, -44))):
        lock(g, f"tail_{i}", (pivot[0], pivot[1] + 1.4, pivot[2]), (rx, 0, rz), segs, 2, 5710 + i * 5, ring=None,
             motion="sway")
    sidelocks(g, "frame", 7, seed=5740, x=4.35, z=-3.2, flare=3, width=2)
    bangs(g, "fringe", [(-2.9, ((3, 2), (2, 1), (1, 1)), 36), (-1.0, ((3, 2), (2, 1)), 42), (1.2, ((2, 2), (1, 1)), 34),
                        (3.0, ((2, 2),), -10)], seed=5750)
