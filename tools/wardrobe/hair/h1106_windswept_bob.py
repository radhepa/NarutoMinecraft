"""Windswept Bob: chin-length silver hair cut in ragged points, short spikes on the crown slanting the
clan way, long framing locks to the jaw and a spiky fan over the nape."""
from anime import back_fan, bangs, ring_shell, sidelocks, spike
from paint import scalp

META = {"name": "Windswept Bob", "gender": "unisex",
        "description": "Chin-length ragged bob, short slanting crown spikes, jaw-length framing locks."}

SMALL = ((3, 2), (2, 2), (1, 1))
CROWN = [(-2.2, -2.0, SMALL, -14, 28), (.4, -2.2, SMALL, -10, 36), (2.6, -1.6, SMALL, -6, 52),
         (-1.8, .8, SMALL, 16, 30), (1.0, 1.0, SMALL, 18, 44)]


def build(g):
    scalp(g, 11501, side_rows=7, back_rows=8, sideburn=1)
    ring_shell(g, 11502, side_rows=7, back_rows=8, ring_row=1)
    for i, (x, z, segs, rx, rz) in enumerate(CROWN):
        spike(g, f"crown_spike_{i}", (x, -7.6, z), (rx, 0, rz), segs, 3, 11510 + i)
    bangs(g, "fringe", [(-2.7, ((3, 2), (2, 1), (1, 1)), 22), (-.8, ((2, 2), (1, 1)), 14), (1.0, ((2, 2), (1, 1)), 6),
                        (2.7, ((2, 2), (1, 1)), -14)], seed=11530)
    sidelocks(g, "frame", 9, seed=11540, x=4.3, z=-3.3, flare=4, width=2)
    sidelocks(g, "sidelock", 8, seed=11545, x=4.45, z=-.4, flare=6, width=3)
    back_fan(g, "nape", [(-3.0, ((3, 6), (2, 2), (1, 1)), 8, 6), (0, ((3, 7), (2, 1), (1, 1)), 0, 6),
                         (3.0, ((3, 6), (2, 2), (1, 1)), -8, 6)], seed=11550)
