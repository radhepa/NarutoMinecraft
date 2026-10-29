"""Teacher's Tail: Unkai Kurama's grown-up look. The hair is combed straight back off a high
forehead with no fringe, lies close over the crown in broad swept locks and is tied at the nape in a
short, neat tail; short locks stand in front of the ears."""
from anime import lock, ring_shell, tie
from paint import scalp

META = {"name": "Teacher's Tail", "gender": "unisex",
        "description": "Combed straight back off the brow, broad swept crown, a short neat tail at the nape."}

# Broad locks laid back over the crown: (x, rz, length). rx near 90 lays a lock flat toward the back.
SWEPT = [(-2.9, 4, 7), (-1.0, 0, 8), (1.0, 0, 8), (2.9, -4, 7)]


def build(g):
    scalp(g, 12040, side_rows=5, back_rows=8, sideburn=2)
    ring_shell(g, 12041, side_rows=4, back_rows=7, ring_row=1)
    for i, (x, rz, n) in enumerate(SWEPT):
        lock(g, f"swept_{i}", (x, -8.6, -3.9), (84, 0, rz), ((2, n - 2), (2, 2)), 2, 12044 + i * 5, ring=0)
    for side, sign in (("right", -1), ("left", 1)):
        lock(g, f"temple_{side}", (4.35 * sign, -7.4, -2.6), (0, 0, -4 * sign), ((2, 4), (1, 1)), 1, 12060 + (sign > 0))
    tie(g, "tie", (0, -2.2, 4.5), (8, 0, 0), size=(3, 1, 2))
    lock(g, "tail", (0, -1.6, 4.6), (12, 0, 0), ((3, 2), (2, 3), (1, 1)), 2, 12066, ring=None, motion="sway")
