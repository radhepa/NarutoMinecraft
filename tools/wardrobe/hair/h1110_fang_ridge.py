"""Fang Ridge: close-cut sides and a ridge of tall silver spikes down the middle of the head, every
one slanting to the wearer's left like a row of fangs."""
from anime import lock, ring_shell, sidelocks, spike
from paint import scalp

META = {"name": "Fang Ridge", "gender": "unisex",
        "description": "Close sides and a ridge of tall spikes down the middle, all slanting one way."}

TALL = ((3, 3), (2, 3), (1, 2))
RIDGE = [(-3.0, TALL, -34, 12), (-1.0, ((3, 3), (2, 3), (1, 2)), -12, 14), (1.0, ((3, 3), (2, 3), (1, 2)), 14, 14),
         (3.0, ((3, 2), (2, 2), (1, 2)), 40, 10)]


def build(g):
    scalp(g, 11901, side_rows=3, back_rows=7, sideburn=1)
    ring_shell(g, 11902, side_rows=2, back_rows=6, ring_row=1)
    for i, (z, segs, rx, rz) in enumerate(RIDGE):
        spike(g, f"crown_spike_{i}", (.4, -7.6, z), (rx, 0, rz), segs, 3, 11910 + i)
    lock(g, "fringe_0", (-.4, -8.55, -4.35), (-10, 0, 20), ((3, 2), (2, 1)), 1, 11930, ring=0)
    sidelocks(g, "sidelock", 3, seed=11940, x=4.4, z=-2.4, flare=8, width=1, taper=False)
    lock(g, "nape_0", (0, -3.6, 4.3), (40, 0, 0), ((2, 2), (1, 2)), 1, 11950)
