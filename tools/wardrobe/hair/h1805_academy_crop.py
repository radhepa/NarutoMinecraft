"""Academy Crop: a short boyish crop for an Academy pupil, a spiky fringe stopping at the brows, a few
tufts sticking up on the crown and a short neat nape."""
from anime import bangs, ring_shell, spike
from paint import scalp

META = {"name": "Academy Crop", "gender": "unisex",
        "description": "Short tidy crop, a spiky fringe at the brows and a few tufts sticking up on the crown."}

TUFTS = [(-1.6, -1.0, -10, 18), (1.2, -.4, -6, -14), (0, 1.8, 18, 4), (-2.4, 2.4, 26, 26), (2.2, 2.6, 28, -24)]


def build(g):
    scalp(g, 18081, side_rows=4, back_rows=7, sideburn=2)
    ring_shell(g, 18082, side_rows=3, back_rows=6, ring_row=1)
    bangs(g, "fringe", [(-3.0, ((2, 2), (1, 1)), 20), (-1.4, ((2, 2), (1, 1)), 10), (.4, ((2, 2), (1, 1)), -4),
                        (2.2, ((2, 2), (1, 1)), -16), (3.2, ((1, 2),), -24)], seed=18084)
    for i, (x, z, rx, rz) in enumerate(TUFTS):
        spike(g, f"tuft_{i}", (x, -8.0, z), (rx, 0, rz), ((2, 1), (1, 1)), 2, 18090 + i * 3)
