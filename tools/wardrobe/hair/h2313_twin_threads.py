"""Twin Threads: two long thin tails tied behind the ears and hanging down over the shoulders like
paid-out threads, the rest smooth under a short fringe at the temples."""
from anime import lock, ring_shell, tie
from paint import scalp

META = {"name": "Twin Threads", "gender": "unisex",
        "description": "Two long thin tails tied behind the ears and hanging down like threads."}


def build(g):
    scalp(g, 23261, side_rows=5, back_rows=8, sideburn=2, part=3)
    ring_shell(g, 23262, side_rows=4, back_rows=8, ring_row=1)
    for side, sign in (("right", -1), ("left", 1)):
        pivot, tilt = (3.9 * sign, -4.2, 2.6), (10, 0, 8 * sign)
        tie(g, f"tail_tie_{side}", pivot, tilt, size=(2, 1, 2), y=-.4, key="A2", motion="sway")
        lock(g, f"tail_{side}", pivot, tilt, ((2, 4), (2, 4), (1, 3)), 2, 23265 + (sign > 0), motion="sway", y0=.6)
