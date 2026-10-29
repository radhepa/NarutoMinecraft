"""Butterfly Spikes: spikes swept up and back in two wing-shaped fans behind the crown, the way the
hair flares when the clan's butterfly chakra burns, with long spiked bangs at the sides."""
from anime import bangs, ring_shell, sidelocks, spike
from paint import scalp

META = {"name": "Butterfly Spikes", "gender": "unisex",
        "description": "Two wing-shaped fans of spikes swept up and back behind the crown, long side bangs."}


def build(g):
    scalp(g, 7301, side_rows=6, back_rows=8, sideburn=2)
    ring_shell(g, 7302, side_rows=6, back_rows=8, ring_row=1)
    for side, sign in (("right", -1), ("left", 1)):
        for i, (y, rx, rz, segs) in enumerate(((-7.4, -64, 30, ((3, 4), (2, 3), (1, 2))),
                                                (-6.0, -84, 50, ((3, 4), (2, 3), (1, 2))),
                                                (-4.4, -104, 66, ((3, 3), (2, 2), (1, 1))))):
            spike(g, f"wing_{side}_{i}", (1.8 * sign, y, 3.2), (rx, 0, rz * sign), segs, 2, 7310 + i + (sign > 0) * 5)
    spike(g, "crown_0", (0, -7.8, -1.4), (-24, 0, 0), ((3, 3), (2, 2), (1, 1)), 2, 7330)
    bangs(g, "fringe", [(-2.0, ((2, 2), (1, 1)), 16), (2.0, ((2, 2), (1, 1)), -16)], seed=7340)
    sidelocks(g, "bang", 8, seed=7350, x=4.3, z=-3.6, flare=4, width=2)
