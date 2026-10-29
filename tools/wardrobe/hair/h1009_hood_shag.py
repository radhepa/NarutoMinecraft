"""Hood Shag: short, messy layers made to live under a hood, ragged points at the brow and a fan
of short spikes kicking out at the nape."""
from anime import back_fan, bangs, ring_shell, spike
from paint import scalp

META = {"name": "Hood Shag", "gender": "unisex",
        "description": "Short messy layers, ragged brow points and a fan of spikes kicking out at the nape."}

NAPE = [(-3.0, ((2, 3), (1, 1)), 30, 34), (-1.0, ((3, 3), (1, 2)), 10, 40), (1.0, ((3, 3), (1, 2)), -10, 40),
        (3.0, ((2, 3), (1, 1)), -30, 34)]


def build(g):
    scalp(g, 10251, side_rows=5, back_rows=7, sideburn=2)
    ring_shell(g, 10252, side_rows=5, back_rows=7, ring_row=1)
    for i, (x, z, rx, rz) in enumerate(((-2.2, -1.0, -6, -30), (1.0, -.4, 8, 22), (-.4, 1.8, -30, -6), (2.4, 2.0, -24, 34))):
        spike(g, f"tuft_{i}", (x, -7.8, z), (rx, 0, rz), ((3, 2), (2, 1), (1, 1)), 3, 10260 + i)
    back_fan(g, "nape", NAPE, seed=10270, z=4.3)
    bangs(g, "fringe", [(-2.8, ((2, 2), (1, 1)), 24), (-.8, ((2, 1), (1, 1)), 8), (1.4, ((2, 1), (1, 1)), -14),
                        (3.0, ((2, 2), (1, 1)), -26)], seed=10280)
