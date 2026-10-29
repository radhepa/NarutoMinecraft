"""Shin Spikes: after Shin, Sai's brother in Root: short dark hair brushed up and back from the
brow into soft spikes, short at the sides, a few points left falling at the temples."""
from anime import ring_shell, sidelocks, spike
from paint import scalp

META = {"name": "Shin Spikes", "gender": "unisex",
        "description": "Short hair brushed up and back into soft spikes, short sides, points at the temples."}

SPIKES = [(-2.6, -3.2, ((3, 2), (2, 1), (1, 1)), -40, -24), (0, -3.6, ((3, 2), (2, 2), (1, 1)), -46, 0),
          (2.6, -3.2, ((3, 2), (2, 1), (1, 1)), -40, 24), (-1.4, -.4, ((3, 2), (2, 1), (1, 1)), -52, -14),
          (1.4, -.4, ((3, 2), (2, 1), (1, 1)), -52, 14), (0, 2.4, ((3, 2), (2, 1), (1, 1)), -70, 0)]


def build(g):
    scalp(g, 13396, side_rows=3, back_rows=6, sideburn=2)
    ring_shell(g, 13397, side_rows=3, back_rows=6, ring_row=1)
    for i, (x, z, segs, rx, rz) in enumerate(SPIKES):
        spike(g, f"spike_{i}", (x, -7.8, z), (rx, 0, rz), segs, 3, 13398 + i)
    sidelocks(g, "temple", 4, seed=13405, x=4.3, z=-3.4, flare=4, width=1)
