"""Elder Mane: the clan elders' waist-length wild hair, a broad sheet down the back breaking into
ragged points, spiky locks over the shoulders and a crown of spikes swept back."""
from anime import bangs, curtain, ring_shell, sidelocks, spike
from paint import scalp

META = {"name": "Elder Mane", "gender": "unisex",
        "description": "Long wild hair down the back in ragged points, spiky shoulder locks, swept-back crown."}


def build(g):
    scalp(g, 6801, side_rows=7, back_rows=8, sideburn=2)
    ring_shell(g, 6802, side_rows=7, back_rows=8, ring_row=1)
    curtain(g, "mane", (0, -6.4, 4.7), (-6, 0, 0), 10, 11, hem=((0, 2, 4), (2, 2, 2), (4, 2, 5), (6, 2, 3), (8, 2, 4)),
            seed=6810, depth=2)
    for i, (x, z, rx, rz) in enumerate(((-2.4, -2.0, -50, -18), (0, -2.4, -56, 0), (2.4, -2.0, -50, 18),
                                        (-1.4, 1.0, -74, -8), (1.4, 1.0, -74, 8))):
        spike(g, f"crown_{i}", (x, -7.8, z), (rx, 0, rz), ((3, 3), (2, 2), (1, 1)), 2, 6820 + i)
    bangs(g, "fringe", [(-2.4, ((2, 2), (1, 1)), 20), (2.4, ((2, 2), (1, 1)), -20)], seed=6830)
    sidelocks(g, "shoulder", 10, seed=6840, x=4.45, z=-2.2, flare=12, width=2)
    sidelocks(g, "ear", 8, seed=6845, x=4.55, z=.6, flare=18, width=2)
