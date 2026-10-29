"""Long Nape: short and tidy over the brow and ears, the back grown out in one straight sheet past
the collar to between the shoulder blades, cut blunt."""
from anime import bangs, curtain, ring_shell
from paint import scalp

META = {"name": "Long Nape", "gender": "unisex",
        "description": "Short over the brow and ears, the back grown long and straight between the shoulders."}


def build(g):
    scalp(g, 16600, side_rows=5, back_rows=8, sideburn=2, part=5)
    ring_shell(g, 16601, side_rows=4, back_rows=8, ring_row=1)
    bangs(g, "fringe", [(-2.8, ((2, 2),), 18), (-1.2, ((2, 2),), 26), (0.6, ((2, 2),), 30), (2.4, ((2, 2),), 16)],
          seed=16602)
    curtain(g, "fall", (0, -6.2, 4.6), (-8, 0, 0), 8, 11, hem=[(0, 8, 1)], seed=16610)
