"""Sprout Tail: the young Nara cut. A shorter, tighter pineapple sprouting from the crown, short
points of fringe at the temples and a soft nape."""
from anime import bangs, lock
from kit_nara import pineapple, pulled_back

META = {"name": "Sprout Tail", "gender": "unisex",
        "description": "A short tight pineapple sprout on the crown, short temple points, soft nape."}

SHORT = ((3, 2), (2, 2), (1, 1))
SPIKES = [(SHORT, -24, 0), (SHORT, -44, -26), (SHORT, -44, 26), (SHORT, -8, -36), (SHORT, -8, 36),
          (((2, 2), (1, 1)), -66, 0)]


def build(g):
    pulled_back(g, 5101, side_rows=4, back_rows=7, sideburn=2)
    pineapple(g, "tail", (0, -7.6, 3.4), SPIKES, seed=5110)
    bangs(g, "fringe", [(-3.0, ((2, 2), (1, 1)), 16), (3.0, ((2, 2), (1, 1)), -16)], seed=5130)
    for i, (x, rz) in enumerate(((-2.0, 18), (0, 0), (2.0, -18))):
        lock(g, f"nape_{i}", (x, -1.6, 4.3), (16, 0, rz), ((2, 1), (1, 1)), 1, 5140 + i * 3)
