"""Tobirama Spikes: short, stiff spikes swept up and back off a clear forehead, shorter spikes over
the ears and a ragged nape, the Second's cut. Nothing falls forward, so a protector sits clean."""
from anime import lock, ring_shell, spike
from paint import scalp

META = {"name": "Tobirama Spikes", "gender": "unisex",
        "description": "Short stiff spikes swept up and back from a clear forehead, spiky sides and nape."}

SHORT = ((3, 2), (2, 1), (1, 1))
TALL = ((3, 2), (2, 1), (1, 1))
# (x, y, z, segments, tilt back, splay)
LONG = ((3, 2), (2, 2), (1, 1))
CROWN = [(-2.2, -7.8, -3.0, TALL, -46, -12), (.4, -7.9, -3.2, LONG, -42, 4), (2.6, -7.8, -2.8, TALL, -48, 18),
         (-1.4, -7.9, -.6, LONG, -62, -14), (1.6, -7.9, -.4, LONG, -64, 14), (-2.8, -7.2, 2.0, TALL, -84, -28),
         (.2, -7.4, 2.4, LONG, -88, 0), (2.8, -7.2, 2.0, TALL, -84, 28)]


def build(g):
    scalp(g, 1032, side_rows=4, back_rows=7, sideburn=2)
    ring_shell(g, 1033, side_rows=3, back_rows=6, ring_row=1)
    for i, (x, y, z, segs, rx, rz) in enumerate(CROWN):
        spike(g, f"crown_spike_{i}", (x, y, z), (rx, 0, rz), segs, 2, 1037 + i)
    for side, sign in (("right", -1), ("left", 1)):
        spike(g, f"crown_side_{side}", (4.1 * sign, -6.2, 0), (-40, 0, 40 * sign), ((2, 2), (1, 1)), 2, 1047 + (sign > 0))
    for i, (x, rz, rx) in enumerate(((-2.6, 26, 40), (0, 0, 46), (2.6, -26, 40))):
        lock(g, f"nape_{i}", (x, -3.4, 4.3), (rx, 0, rz), ((2, 2), (1, 1)), 1, 1052 + i * 5)
