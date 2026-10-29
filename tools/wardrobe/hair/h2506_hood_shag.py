"""Hood Shag: a low, flat shag cut to sit under a hood, layered points lying close over the crown,
a ragged fringe to the brows and uneven locks over the ears and the nape."""
from anime import back_fan, bangs, ring_shell, sidelocks, spike
from paint import scalp

META = {"name": "Hood Shag", "gender": "unisex",
        "description": "Flat layered shag lying close to the crown, ragged brow fringe, uneven ear and nape locks."}

FLAT = ((3, 1), (2, 1), (1, 1))


def build(g):
    scalp(g, 25100, side_rows=6, back_rows=8, sideburn=3)
    ring_shell(g, 25101, side_rows=6, back_rows=8, ring_row=1)
    for i, (x, z, rx, rz) in enumerate(((-2.4, -1.6, -62, -10), (.4, -1.8, -66, 4), (2.6, -1.4, -60, 14),
                                        (-1.2, 1.0, -70, -8), (1.6, 1.0, -72, 10))):
        spike(g, f"layer_{i}", (x, -7.7, z), (rx, 0, rz), FLAT, 2, 25102 + i)
    bangs(g, "fringe", [(-3.0, ((2, 3), (1, 1)), 16), (-1.2, ((2, 2), (1, 1)), 6), (.6, ((2, 2), (1, 1)), -4),
                        (2.9, ((2, 2), (1, 1)), -12)], seed=25108)
    sidelocks(g, "ear", 6, seed=25112, x=4.4, z=-1.6, flare=8, width=2)
    back_fan(g, "nape", [(-3.0, ((3, 3), (2, 1), (1, 1)), 16, 12), (-.6, ((2, 4), (1, 1)), 4, 8),
                         (1.6, ((3, 3), (1, 2)), -8, 10), (3.1, ((2, 3), (1, 1)), -18, 14)], seed=25115)
