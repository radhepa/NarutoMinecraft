"""Spring Spikes: short, bright spiky hair standing up all over like a young Kizashi's, a few short
points falling over the brow and sharp tufts behind the ears."""
from anime import back_fan, bangs, ring_shell, spike
from paint import scalp

META = {"name": "Spring Spikes", "gender": "unisex",
        "description": "Short spiky hair standing up all over, short brow points, tufts behind the ears."}

TUFT = ((3, 2), (2, 2), (1, 1))
CROWN = [(-2.4, -1.6, -30, 30), (0, -2.0, -40, 0), (2.4, -1.6, -30, -30), (-2.0, 1.4, 30, 34), (2.0, 1.4, 30, -34),
         (0, 2.4, 50, 0)]


def build(g):
    scalp(g, 19281, side_rows=4, back_rows=6, sideburn=2)
    ring_shell(g, 19282, side_rows=3, back_rows=5, ring_row=1)
    for i, (x, z, rx, rz) in enumerate(CROWN):
        spike(g, f"spike_{i}", (x, -7.8, z), (rx, 0, rz), TUFT, 2, 19285 + i * 3)
    bangs(g, "fringe", [(-2.6, ((2, 2), (1, 1)), 22), (0, ((2, 2), (1, 1)), -8), (2.6, ((2, 2), (1, 1)), -24)], seed=19290)
    back_fan(g, "nape", [(-2.6, ((2, 3), (1, 1)), 26, 16), (0, ((2, 3), (1, 1)), 0, 18), (2.6, ((2, 3), (1, 1)), -26, 16)],
             seed=19276)
