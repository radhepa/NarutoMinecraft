"""Blossom Braid: long hair worked into one thick braid down the back and tied with a cloth tie at
the end, a side-swept fringe and two loose locks framing the face."""
from anime import braid, lock, ring_shell, sidelocks, tie
from paint import scalp

META = {"name": "Blossom Braid", "gender": "unisex",
        "description": "One thick braid down the back tied with cloth, side-swept fringe, loose face-framing locks."}

SWEEP = [(3.0, ((2, 2), (1, 1)), 12), (1.6, ((3, 2), (1, 1)), 54), (-.2, ((3, 2), (1, 1)), 56), (-2.2, ((2, 2), (1, 1)), 40)]


def build(g):
    scalp(g, 19461, side_rows=6, back_rows=8, sideburn=1, part=5)
    ring_shell(g, 19462, side_rows=6, back_rows=8, ring_row=1)
    for i, (x, segs, rz) in enumerate(SWEEP):
        lock(g, f"sweep_{i}", (x, -8.55, -4.35), (-10, 0, rz), segs, 1, 19465 + i * 7, ring=0)
    sidelocks(g, "frame", 6, seed=19495, x=4.35, flare=3, width=1)
    end = braid(g, "braid", (0, -5.0, 4.6), (10, 0, 0), links=7, width=3, seed=19498)
    tie(g, "tie", (0, -5.0, 4.6), (10, 0, 0), (3, 1, 3), y=end - 2.6, key="A2", motion="sway")
