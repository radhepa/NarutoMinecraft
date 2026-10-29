"""Cropped Spikes: silver hair kept short for the field, a low crop of stubby spikes slanting to the
wearer's left, a bare brow and a tidy nape."""
from anime import lock, ring_shell, spike
from paint import scalp

META = {"name": "Cropped Spikes", "gender": "unisex",
        "description": "A short crop of stubby spikes slanting one way, bare brow, tidy nape."}

S = ((2, 2), (1, 1))
M = ((3, 1), (2, 1), (1, 1))
CROWN = [(-2.4, -2.4, M, -26, 30), (0, -2.6, M, -22, 40), (2.4, -2.2, S, -18, 56),
         (-2.6, .2, M, 4, 32), (0, .4, M, 6, 40), (2.6, .4, S, 6, 56), (-1.4, 2.8, S, 40, 34), (1.4, 2.8, S, 40, 46)]


def build(g):
    scalp(g, 12201, side_rows=3, back_rows=6, sideburn=2)
    ring_shell(g, 12202, side_rows=2, back_rows=5, ring_row=1)
    for i, (x, z, segs, rx, rz) in enumerate(CROWN):
        spike(g, f"crown_spike_{i}", (x, -7.6, z), (rx, 0, rz), segs, 2, 12210 + i)
    lock(g, "fringe_0", (-2.0, -8.55, -4.35), (-10, 0, 30), ((2, 2), (1, 1)), 1, 12230, ring=0)
