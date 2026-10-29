"""Loose Wisps: the grown-up strategist. The high pineapple tail, worn a little longer and messier,
with loose wisps escaping at the temples and the nape after a long night over the shogi board."""
from anime import lock, sidelocks
from kit_nara import pineapple, pulled_back

META = {"name": "Loose Wisps", "gender": "unisex",
        "description": "A longer, messier pineapple tail with loose wisps escaping at the temples and nape."}

LONG = ((3, 3), (3, 3), (2, 2), (1, 2))
SPIKES = [(LONG, -42, -6), (LONG, -58, -30), (LONG, -54, 22), (((3, 3), (2, 2), (1, 1)), -80, -4),
          (((3, 2), (2, 2), (1, 2)), -28, 40), (((3, 2), (2, 2), (1, 2)), -32, -42), (((2, 3), (1, 2)), -96, 18)]


def build(g):
    pulled_back(g, 5251, side_rows=4, back_rows=6, sideburn=3)
    pineapple(g, "tail", (0, -7.2, 4.3), SPIKES, seed=5260)
    sidelocks(g, "wisp", 6, seed=5280, x=4.35, z=-3.0, flare=9, width=1)
    lock(g, "stray", (-3.2, -8.5, -4.3), (-10, 0, 34), ((1, 2), (1, 1)), 1, 5290, ring=None)
    for i, (x, rz) in enumerate(((-2.4, 26), (2.0, -22))):
        lock(g, f"nape_{i}", (x, -2.2, 4.4), (22, 0, rz), ((1, 2), (1, 1)), 1, 5295 + i * 3, ring=None)
