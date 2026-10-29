"""Leaf Spikes: a messy crown of anime spikes standing up over a forehead protector, with short
fringe points and spiky sides."""
from anime import bangs, lock, ring_shell, sidelocks, spike
from paint import scalp

META = {"name": "Leaf Spikes", "gender": "male", "description": "Tall messy spikes, short fringe points, spiky sides."}

BIG = ((4, 3), (3, 2), (2, 2), (1, 1))
CROWN = [(-2.6, -2.0, BIG, -18, -32), (0, -2.6, ((4, 4), (3, 2), (2, 2), (1, 1)), -24, 0), (2.6, -2.0, BIG, -18, 32),
         (-2.2, 1.2, BIG, 20, -26), (2.2, 1.2, BIG, 20, 26), (0, 2.8, BIG, 42, 0)]


def build(g):
    scalp(g, 301, side_rows=4, back_rows=8, sideburn=2)
    ring_shell(g, 302, side_rows=4, back_rows=7, ring_row=1)
    for i, (x, z, segs, rx, rz) in enumerate(CROWN):
        spike(g, f"crown_spike_{i}", (x, -7.7, z), (rx, 0, rz), segs, 3, 310 + i)
    bangs(g, "fringe", [(-2.6, ((2, 2), (1, 1)), 22), (-.4, ((2, 2), (1, 1)), 4), (1.9, ((2, 2), (1, 1)), -18)],
          seed=330)
    sidelocks(g, "sidelock", 4, seed=340, x=4.4, z=-2.2, flare=18, width=2)
    for i, (x, rz, rx) in enumerate(((-2.8, 30, 34), (0, 0, 44), (2.8, -30, 34))):
        lock(g, f"nape_{i}", (x, -3.8, 4.3), (rx, 0, rz), ((2, 2), (1, 2)), 1, 360 + i * 5)
