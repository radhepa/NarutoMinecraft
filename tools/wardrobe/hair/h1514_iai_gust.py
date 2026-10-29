"""Iai Gust: hair blown straight back as if by a fast draw, every lock streaming behind the head,
the brow left bare and a few points flicking out past the ears."""
from anime import lock, ring_shell, spike
from paint import scalp

META = {"name": "Iai Gust", "gender": "unisex",
        "description": "Hair streaming straight back as if from a fast draw, bare brow, points past the ears."}

STREAM = ((3, 3), (2, 2), (1, 2))
# (x, y, z, rx, rz): locks rooted across the crown, each laid back toward the nape.
BACK = [(-2.6, -8.0, -3.0, -62, -12), (0, -8.2, -3.2, -66, 0), (2.6, -8.0, -3.0, -62, 12),
        (-2.8, -7.8, .2, -76, -18), (0, -8.0, 0, -80, 0), (2.8, -7.8, .2, -76, 18)]


def build(g):
    scalp(g, 15350, side_rows=4, back_rows=8, sideburn=2)
    ring_shell(g, 15351, side_rows=4, back_rows=8, ring_row=1)
    for i, (x, y, z, rx, rz) in enumerate(BACK):
        spike(g, f"stream_{i}", (x, y, z), (rx, 0, rz), STREAM, 3, 15355 + i)
    for side, sign in (("right", -1), ("left", 1)):
        lock(g, f"flick_{side}", (4.3 * sign, -5.6, 1.0), (40, 0, -40 * sign), ((2, 2), (1, 2)), 1, 15365 + (sign > 0))
    for i, x in enumerate((-2.4, 0, 2.4)):
        lock(g, f"nape_{i}", (x, -2.0, 4.3), (50, 0, -x * 6), ((2, 3), (1, 2)), 1, 15370 + i)
