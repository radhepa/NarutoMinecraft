"""Hound Tail: short slanting silver spikes and a stubby tail tied high at the back of the head with a
cloth wrap, sticking out and up like a ninja hound's tail."""
from anime import bangs, lock, ring_shell, sidelocks, spike, tie
from paint import scalp

META = {"name": "Hound Tail", "gender": "unisex",
        "description": "Short slanting spikes, a stubby spiky tail tied up at the back with a cloth wrap."}

MID = ((3, 2), (2, 2), (1, 1))
CROWN = [(-2.4, -2.2, MID, -18, 26), (.2, -2.4, ((4, 2), (3, 2), (2, 2), (1, 1)), -14, 34), (2.6, -1.8, MID, -10, 52),
         (-2.0, .6, MID, 10, 28), (1.0, .8, MID, 12, 44)]


def build(g):
    scalp(g, 11601, side_rows=5, back_rows=8, sideburn=2)
    ring_shell(g, 11602, side_rows=5, back_rows=7, ring_row=1)
    for i, (x, z, segs, rx, rz) in enumerate(CROWN):
        spike(g, f"crown_spike_{i}", (x, -7.6, z), (rx, 0, rz), segs, 3, 11610 + i)
    bangs(g, "fringe", [(-2.4, ((2, 2), (1, 1)), 22), (-.4, ((2, 2), (1, 1)), 14), (1.8, ((2, 1), (1, 1)), 6)],
          seed=11630)
    sidelocks(g, "sidelock", 5, seed=11640, x=4.4, z=-2.2, flare=12, width=2)
    # The tail sticks out backwards and curls up at the tip.
    tie(g, "tie", (0, -5.0, 4.3), (98, 0, 0), size=(3, 1, 3), key="D2")
    lock(g, "tail", (0, -5.0, 4.3), (98, 0, 0), ((3, 3), (3, 2), (2, 2), (1, 2)), 3, 11650, ring=None, y0=1.0,
         motion="sway")
    for i, (x, rz, rx) in enumerate(((-2.6, 22, 30), (2.6, -22, 30))):
        lock(g, f"nape_{i}", (x, -3.6, 4.3), (rx, 0, rz), ((2, 2), (1, 1)), 1, 11660 + i * 5)
