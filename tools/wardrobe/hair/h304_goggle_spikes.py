"""Goggle Spikes: young Obito's short black crop, every spike standing straight up off the crown and
the front ones leaning forward over the brow, with short spiky sides and nape."""
from anime import lock, ring_shell, spike
from paint import scalp

META = {"name": "Goggle Spikes", "gender": "unisex", "description": "A short crop of upright spikes, the front ones leaning over the brow."}

SMALL = ((3, 2), (2, 2), (1, 1))
TALL = ((3, 3), (2, 2), (1, 1))
# (x, z, segments, rx, rz)
CROWN = [(-2.8, -2.8, SMALL, 22, -14), (-.9, -3.0, TALL, 26, -4), (1.0, -3.0, TALL, 26, 6), (2.8, -2.8, SMALL, 22, 14),
         (-2.6, -.4, TALL, 0, -22), (0, -.6, TALL, 4, 0), (2.6, -.4, TALL, 0, 22),
         (-2.0, 2.0, SMALL, -24, -18), (.4, 2.2, TALL, -28, 4), (2.6, 1.8, SMALL, -24, 20)]


def build(g):
    scalp(g, 3161, side_rows=4, back_rows=7, sideburn=2)
    ring_shell(g, 3162, side_rows=3, back_rows=6, ring_row=1)
    for i, (x, z, segs, rx, rz) in enumerate(CROWN):
        spike(g, f"crown_spike_{i}", (x, -7.7, z), (rx, 0, rz), segs, 2, 3170 + i)
    for i, (x, rz) in enumerate(((-4.4, 50), (4.4, -50))):
        spike(g, f"side_spike_{i}", (x, -6.4, -1.0), (0, 0, rz), ((2, 2), (1, 1)), 2, 3185 + i)
    for i, (x, rz, rx) in enumerate(((-2.4, 22, 30), (0, 0, 36), (2.4, -22, 30))):
        lock(g, f"nape_{i}", (x, -3.0, 4.3), (rx, 0, rz), ((2, 2), (1, 1)), 1, 3190 + i * 3)
