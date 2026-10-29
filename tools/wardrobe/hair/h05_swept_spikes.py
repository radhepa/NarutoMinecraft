"""Swept Spikes: a tall shock of spikes all swept to one side, the way a gale left it, with short
spiky sides and nape points. No fringe, so a mask fits flat over the face."""
from anime import lock, ring_shell, sidelocks, spike
from paint import scalp

META = {"name": "Swept Spikes", "gender": "male", "description": "Tall spikes swept to one side, spiky sides and nape."}

BIG = ((3, 3), (2, 2), (1, 2))
TALL = ((4, 3), (3, 3), (2, 2), (1, 1))
# (x, z, segments, rx, rz): every crown spike leans the same way, to the wearer's left.
CROWN = [(-2.6, -2.0, BIG, -4, 48), (-.2, -2.2, TALL, -6, 52), (2.4, -1.8, BIG, -2, 62),
         (-2.4, .8, TALL, 14, 46), (.4, 1.0, TALL, 16, 54), (2.4, 1.2, BIG, 18, 64),
         (-1.0, 3.0, BIG, 34, 50), (1.6, 3.0, BIG, 34, 60)]


def build(g):
    scalp(g, 601, side_rows=4, back_rows=8, sideburn=2)
    ring_shell(g, 602, side_rows=4, back_rows=7, ring_row=1)
    for i, (x, z, segs, rx, rz) in enumerate(CROWN):
        spike(g, f"crown_spike_{i}", (x, -7.7, z), (rx, 0, rz), segs, 3, 610 + i)
    sidelocks(g, "sidelock", 4, seed=640, x=4.4, z=-2.2, flare=18, width=2)
    for i, (x, rz, rx) in enumerate(((-2.8, 30, 34), (0, 0, 44), (2.8, -30, 34))):
        lock(g, f"nape_{i}", (x, -3.8, 4.3), (rx, 0, rz), ((2, 2), (1, 2)), 1, 660 + i * 5)
