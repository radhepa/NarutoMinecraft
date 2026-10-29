"""Hound Buns: two rough buns high on the head with their ends left spiking out like perked ears,
a shaggy short back and a choppy fringe."""
from anime import back_fan, bangs, cel_box, ring_shell, sidelocks, spike
from paint import scalp

META = {"name": "Hound Buns", "gender": "unisex",
        "description": "Two rough buns high on the head with spiky ends like perked ears, a choppy fringe."}


def build(g):
    scalp(g, 8300, side_rows=5, back_rows=7, sideburn=2)
    ring_shell(g, 8301, side_rows=5, back_rows=6, ring_row=1)
    for i, (x, rz) in enumerate(((-2.6, -24), (2.6, 24))):
        bun = g.piece(f"crown_bun_{i}", "HEAD", (-1.5, -3, -1.5), (3, 3, 3), pivot=(x, -7.4, .6), rotation=(0, 0, rz))
        cel_box(bun, 8303 + i, base=2, ring=0)
        side = 1 if x > 0 else -1
        for j, (dz, rx, splay) in enumerate(((-.6, 22, 20), (.6, -22, 20), (0, 0, 50))):
            spike(g, f"crown_bun_{i}_spike_{j}", (x + side * .4, -10.0, .6 + dz), (rx, 0, rz + side * splay),
                  ((2, 2), (1, 1)), 2, 8306 + i * 4 + j)
    back_fan(g, "nape", [(-2.6, ((2, 3), (1, 1)), 18, 22), (0, ((3, 3), (2, 1), (1, 1)), 0, 16),
                         (2.6, ((2, 3), (1, 1)), -18, 22)], seed=8316)
    bangs(g, "fringe", [(-2.7, ((2, 2), (1, 1)), 20), (-.9, ((2, 2), (1, 1)), 10), (.9, ((2, 2), (1, 1)), -10),
                        (2.7, ((2, 2), (1, 1)), -20)], seed=8320)
    sidelocks(g, "sidelock", 7, seed=8325, x=4.35, z=-3.4, flare=6, width=2)
