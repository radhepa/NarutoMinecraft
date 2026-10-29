"""Sensei Spikes: Konohamaru grown up, as Team 7's sensei. A full, dense head of short spikes that
point every way from the crown, thick over the ears and at the nape, with a ragged fringe."""
from anime import bangs, ring_shell, sidelocks, spike
from paint import scalp

META = {"name": "Sensei Spikes", "gender": "unisex",
        "description": "Dense short spikes pointing every way, thick over the ears and nape, ragged fringe."}

S3 = ((3, 2), (2, 2), (1, 1))
S2 = ((3, 2), (2, 1), (1, 1))
CROWN = [(0.0, -8.0, -1.2, S3, 8, 0), (-2.4, -8.0, -1.4, S3, 4, -24), (2.4, -8.0, -1.4, S3, 4, 24),
         (-1.2, -8.0, 1.0, S3, -24, -12), (1.2, -8.0, 1.0, S3, -24, 12),
         (-3.2, -7.6, 1.4, S2, -24, -46), (3.2, -7.6, 1.4, S2, -24, 46),
         (-2.2, -7.0, 3.2, S3, -64, -26), (2.2, -7.0, 3.2, S3, -64, 26), (0.0, -6.6, 3.6, S3, -76, 0),
         (-3.8, -5.6, -.6, S2, -6, -78), (3.8, -5.6, -.6, S2, -6, 78),
         (-3.6, -4.8, 2.2, S2, -50, -70), (3.6, -4.8, 2.2, S2, -50, 70),
         (-1.6, -4.2, 3.9, S2, -112, -18), (1.6, -4.2, 3.9, S2, -112, 18)]


def build(g):
    scalp(g, 9211, side_rows=5, back_rows=8, sideburn=2)
    ring_shell(g, 9212, side_rows=5, back_rows=8, ring_row=1)
    for i, (x, y, z, segs, rx, rz) in enumerate(CROWN):
        spike(g, f"crown_{i}", (x, y, z), (rx, 0, rz), segs, 2, 9220 + i * 3)
    bangs(g, "fringe", [(-2.8, ((2, 2), (1, 1)), 22), (-1.0, ((2, 1), (1, 1)), 10), (1.0, ((2, 2), (1, 1)), -12),
                        (2.8, ((2, 2), (1, 1)), -24)], seed=9270)
    sidelocks(g, "frame", 4, seed=9280, x=4.3, z=-3.2, flare=10, width=2)
