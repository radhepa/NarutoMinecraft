"""Enma Tail: an invention after the Monkey King Enma. Long hair swept back from a short fringe
into a low tail at the nape, bound down its length by three cloth wraps like a monkey's tail."""
from anime import bangs, lock, ring_shell, sidelocks, tie
from paint import scalp

META = {"name": "Enma Tail", "gender": "unisex",
        "description": "Swept back into a long low tail bound down its length by three cloth wraps."}


def build(g):
    scalp(g, 9461, side_rows=6, back_rows=8, sideburn=3)
    ring_shell(g, 9462, side_rows=6, back_rows=8, ring_row=1)
    bangs(g, "fringe", [(-2.6, ((2, 2), (1, 1)), 22), (2.6, ((2, 2), (1, 1)), -22)], seed=9470)
    sidelocks(g, "frame", 6, seed=9475, x=4.3, z=-3.0, flare=6, width=2)
    pivot, rot = (0, -2.6, 4.6), (14, 0, 0)
    tie(g, "tail_tie", pivot, rot, (3, 1, 3), y=0, key="A2")
    lock(g, "tail", pivot, rot, ((3, 4), (3, 3), (2, 3), (2, 2), (1, 2)), 3, 9480, ring=None, motion="sway", y0=1)
    for i, y in enumerate((5.0, 8.0, 11.0)):
        tie(g, f"tail_wrap_{i}", pivot, rot, (4 if i < 2 else 3, 1, 4 if i < 2 else 3), y=y, key="S3", motion="sway")
