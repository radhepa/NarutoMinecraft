"""Shino Spikes: Shino's Part I hair, short and dense, every spike standing up and raked back from
a bare hairline, so the round shades and the high collar own the face."""
from anime import ring_shell, spike
from paint import scalp

META = {"name": "Shino Spikes", "gender": "unisex",
        "description": "Short dense spikes standing up and raked back from a bare hairline."}

# (x, z, segments, tilt back, splay): three rows of spikes from the hairline to the crown.
SPIKES = [(-2.6, -2.8, ((3, 2), (2, 2), (1, 1)), -22, -20), (0, -3.0, ((3, 3), (2, 2), (1, 1)), -26, 0),
          (2.6, -2.8, ((3, 2), (2, 2), (1, 1)), -22, 20),
          (-2.8, .2, ((3, 3), (2, 2), (1, 1)), -40, -24), (0, -.2, ((4, 3), (3, 2), (1, 2)), -44, 0),
          (2.8, .2, ((3, 3), (2, 2), (1, 1)), -40, 24),
          (-1.6, 2.8, ((3, 2), (2, 2), (1, 1)), -66, -14), (1.6, 2.8, ((3, 2), (2, 2), (1, 1)), -66, 14)]


def build(g):
    scalp(g, 10001, side_rows=3, back_rows=6, sideburn=2)
    ring_shell(g, 10002, side_rows=2, back_rows=6, ring_row=1)
    for i, (x, z, segs, rx, rz) in enumerate(SPIKES):
        spike(g, f"crown_spike_{i}", (x, -7.8, z), (rx, 0, rz), segs, 3, 10010 + i)
