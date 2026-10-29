"""Nawaki Spikes: a boy's shock of short spikes pointing every way, a few fringe points that stop
well above the brows and two spikes standing up at the front like a rooster's comb."""
from anime import bangs, ring_shell, spike
from paint import scalp

META = {"name": "Nawaki Spikes", "gender": "unisex",
        "description": "A shock of short spikes in every direction, two standing at the front, brief fringe points."}

S = ((3, 2), (2, 2), (1, 1))
M = ((3, 3), (2, 2), (1, 2))
CROWN = [(-1.4, -7.8, -3.2, M, -12, -10), (1.4, -7.8, -3.2, M, -12, 12), (-3.0, -7.6, -1.6, S, -20, -46),
         (3.0, -7.6, -1.6, S, -20, 46), (0, -7.9, -.4, M, 6, 0), (-2.4, -7.8, 1.4, S, 26, -34),
         (2.4, -7.8, 1.4, S, 26, 34), (0, -7.6, 3.0, M, 50, 0), (-3.2, -6.0, 3.0, S, 60, -30),
         (3.2, -6.0, 3.0, S, 60, 30)]


def build(g):
    scalp(g, 1096, side_rows=4, back_rows=7, sideburn=2)
    ring_shell(g, 1097, side_rows=3, back_rows=6, ring_row=1)
    for i, (x, y, z, segs, rx, rz) in enumerate(CROWN):
        spike(g, f"crown_spike_{i}", (x, y, z), (rx * .7, 0, rz * .7), segs, 2, 1101 + i * 3)
    bangs(g, "fringe", [(-2.6, ((2, 1), (1, 1)), 22), (-.6, ((2, 1), (1, 1)), 8), (1.6, ((2, 1), (1, 1)), -18),
                        (3.0, ((2, 2), (1, 1)), -26)], seed=1116)
