"""Sidelong Lock: slanting silver spikes with one long lock swept down the right side of the face to
the jaw, outside the eye, the way a protector worn aslant pushes the hair aside."""
from anime import bangs, lock, ring_shell, sidelocks, spike
from paint import scalp

META = {"name": "Sidelong Lock", "gender": "unisex",
        "description": "Slanting spikes and one long lock swept down the side of the face to the jaw."}

BIG = ((4, 3), (3, 2), (2, 2), (1, 1))
MID = ((3, 2), (2, 2), (1, 2))
CROWN = [(-2.0, -2.4, BIG, -16, 34), (.8, -2.4, MID, -12, 46), (2.8, -1.4, MID, -4, 64),
         (-2.4, .6, BIG, 8, 32), (.6, .8, BIG, 10, 44), (-.6, 3.0, MID, 36, 40)]


def build(g):
    scalp(g, 12301, side_rows=5, back_rows=8, sideburn=2)
    ring_shell(g, 12302, side_rows=5, back_rows=7, ring_row=1)
    for i, (x, z, segs, rx, rz) in enumerate(CROWN):
        spike(g, f"crown_spike_{i}", (x, -7.6, z), (rx, 0, rz), segs, 3, 12310 + i)
    bangs(g, "fringe", [(-1.4, ((3, 2), (2, 1), (1, 1)), 40), (.6, ((2, 2), (1, 1)), 30), (2.4, ((2, 1), (1, 1)), 20)],
          seed=12330)
    # The long lock falls in front of the right ear, outside the eye.
    lock(g, "long_lock", (-4.6, -7.8, -3.2), (0, 0, 6), ((3, 4), (2, 3), (1, 2)), 1, 12340, ring=1)
    lock(g, "sidelock_left", (4.4, -7.6, -2.4), (0, 0, 14), ((2, 3), (1, 2)), 1, 12345, ring=1)
    for i, (x, rz, rx) in enumerate(((-2.6, 22, 32), (0, 4, 40), (2.6, -18, 32))):
        lock(g, f"nape_{i}", (x, -3.6, 4.3), (rx, 0, rz), ((2, 2), (1, 2)), 1, 12350 + i * 5)
