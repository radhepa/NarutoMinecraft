"""Tide Spikes: short hair brushed up and back in a crest of soft spikes like a breaking wave, the
sides kept short and a couple of points falling to the brow."""
from anime import bangs, ring_shell, spike
from paint import scalp

META = {"name": "Tide Spikes", "gender": "unisex",
        "description": "Short hair brushed up and back in a crest of spikes like a breaking wave, short sides."}

BIG = ((3, 2), (2, 2), (1, 2))
MID = ((2, 2), (1, 2))
CREST = [(-1.6, -2.6, MID, -24, 8), (1.4, -2.4, MID, -22, -8), (-2.2, -.4, BIG, -8, 18), (0, -.2, BIG, -4, 0),
         (2.2, -.2, BIG, -8, -18), (-1.2, 2.0, BIG, 22, 10), (1.4, 2.2, BIG, 24, -10), (0, 3.6, MID, 48, 0)]


def build(g):
    scalp(g, 18181, side_rows=4, back_rows=7, sideburn=2)
    ring_shell(g, 18182, side_rows=3, back_rows=6, ring_row=1)
    for i, (x, z, segs, rx, rz) in enumerate(CREST):
        spike(g, f"crest_{i}", (x, -7.8, z), (rx, 0, rz), segs, 3, 18185 + i * 3)
    bangs(g, "fringe", [(-2.4, ((2, 2), (1, 1)), 22), (2.0, ((2, 1), (1, 1)), -12)], seed=18210)
