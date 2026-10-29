"""Short Crop: hair cut close at the sides and nape with short, soft spikes on top and a brief
fringe that stops well above the brows, so it suits masks, hoods and face cloths."""
from anime import bangs, ring_shell, spike
from paint import scalp

META = {"name": "Short Crop", "gender": "unisex", "description": "Close sides and nape, short soft spikes on top, a brief fringe."}

TUFT = ((3, 2), (2, 1), (1, 1))
CROWN = [(-2.4, -1.8, TUFT, -14, -24), (0, -2.2, TUFT, -18, 4), (2.4, -1.6, TUFT, -12, 26),
         (-1.4, 1.2, TUFT, 18, -18), (1.6, 1.4, TUFT, 20, 20)]


def build(g):
    scalp(g, 801, side_rows=3, back_rows=6, sideburn=2)
    ring_shell(g, 802, side_rows=2, back_rows=5, ring_row=1)
    for i, (x, z, segs, rx, rz) in enumerate(CROWN):
        spike(g, f"crown_tuft_{i}", (x, -7.8, z), (rx, 0, rz), segs, 3, 810 + i)
    bangs(g, "fringe", [(-2.2, ((2, 1), (1, 1)), 18), (0, ((2, 1),), 0), (2.2, ((2, 1), (1, 1)), -18)], seed=830)
