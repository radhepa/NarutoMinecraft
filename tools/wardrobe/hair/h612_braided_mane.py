"""Braided Mane: a spiky crown swept back and the length worked into one thick braid down the back,
finished in a tuft, with short spiked sideburns."""
from anime import bangs, braid, cel_box, ring_shell, sidelocks, spike, tie
from paint import scalp

META = {"name": "Braided Mane", "gender": "unisex",
        "description": "A spiky swept-back crown and one thick braid down the back, spiked sideburns."}


def build(g):
    scalp(g, 6496, side_rows=6, back_rows=8, sideburn=2)
    ring_shell(g, 6496, side_rows=6, back_rows=8, ring_row=1)
    for i, (x, z, rx, rz) in enumerate(((-2.4, -2.2, -40, -24), (0, -2.6, -44, 0), (2.4, -2.2, -40, 24),
                                        (-1.6, .6, -64, -14), (1.6, .6, -64, 14))):
        spike(g, f"crown_{i}", (x, -7.8, z), (rx, 0, rz), ((3, 3), (2, 2), (1, 1)), 2, 6502 + i)
    root = g.piece("braid_root", "HEAD", (-2, 0, -1), (4, 2, 2), pivot=(0, -4.0, 4.6), rotation=(10, 0, 0))
    cel_box(root, 6509)
    tie(g, "braid_tie", (0, -2.0, 4.9), (10, 0, 0), size=(3, 1, 3), key="A2")
    braid(g, "braid", (0, -1.2, 5.0), (12, 0, 0), links=6, width=3, seed=6516)
    bangs(g, "fringe", [(-2.2, ((2, 2), (1, 1)), 22), (2.2, ((2, 2), (1, 1)), -22)], seed=6523)
    sidelocks(g, "sideburn", 6, seed=6530, x=4.4, z=-2.8, flare=14, width=2)
