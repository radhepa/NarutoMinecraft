"""Scarf Kid Spikes: Konohamaru as an Academy student. A shock of brown hair standing straight up
in tall spikes that fan out from the crown, short points at the brow and close-cropped sides."""
from anime import bangs, ring_shell, spike
from paint import scalp

META = {"name": "Scarf Kid Spikes", "gender": "unisex",
        "description": "Tall spikes standing straight up and fanning out from the crown, short brow points."}

TALL = ((3, 3), (3, 2), (2, 2), (1, 2))
MID = ((3, 2), (2, 2), (1, 2))
CROWN = [(0.0, -8.0, -.6, TALL, 0, 0),
         (-2.2, -8.0, -.8, TALL, -4, -16), (2.2, -8.0, -.8, TALL, -4, 16),
         (-3.4, -7.4, -1.4, MID, 6, -38), (3.4, -7.4, -1.4, MID, 6, 38),
         (-1.2, -8.0, 1.8, TALL, -20, -8), (1.2, -8.0, 1.8, TALL, -20, 8),
         (-2.8, -7.4, 2.8, MID, -38, -30), (2.8, -7.4, 2.8, MID, -38, 30),
         (0.0, -7.2, 3.4, MID, -50, 0)]


def build(g):
    scalp(g, 9161, side_rows=3, back_rows=6, sideburn=2)
    ring_shell(g, 9162, side_rows=3, back_rows=6, ring_row=1)
    for i, (x, y, z, segs, rx, rz) in enumerate(CROWN):
        spike(g, f"crown_{i}", (x, y, z), (rx, 0, rz), segs, 2, 9170 + i * 3)
    bangs(g, "fringe", [(-2.4, ((2, 1), (1, 1)), 14), (0.2, ((2, 1), (1, 1)), -4), (2.6, ((2, 1), (1, 1)), -16)], seed=9200)
