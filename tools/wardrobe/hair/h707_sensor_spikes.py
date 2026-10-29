"""Sensor Spikes: short pale spikes all combed straight back from the brow and lying low along the
crown, close sides and a few nape points: a sensor's cut that keeps the headset clear."""
from anime import lock, ring_shell, spike
from paint import scalp

META = {"name": "Sensor Spikes", "gender": "unisex",
        "description": "Short spikes combed straight back, close sides, nape points, an open brow."}

BIG = ((3, 3), (2, 2), (1, 2))
SMALL = ((3, 2), (2, 2), (1, 1))
# (x, z, segments, rx, rz): low spikes leaning back over the crown.
CROWN = [(-2.6, -3.0, SMALL, -62, -10), (0, -3.2, BIG, -66, 0), (2.6, -3.0, SMALL, -62, 10),
         (-2.2, -.4, BIG, -74, -14), (.2, -.2, BIG, -76, 0), (2.4, -.4, BIG, -74, 14),
         (-1.4, 2.4, BIG, -96, -10), (1.4, 2.4, BIG, -96, 10)]


def build(g):
    scalp(g, 7601, side_rows=3, back_rows=7, sideburn=2)
    ring_shell(g, 7602, side_rows=3, back_rows=6, ring_row=1)
    for i, (x, z, segs, rx, rz) in enumerate(CROWN):
        spike(g, f"crown_{i}", (x, -7.7, z), (rx, 0, rz), segs, 3, 7610 + i)
    for i, (x, rz) in enumerate(((-2.6, 24), (0, 0), (2.6, -24))):
        lock(g, f"nape_{i}", (x, -3.2, 4.3), (40, 0, rz), ((2, 2), (1, 2)), 1, 7640 + i * 5)
