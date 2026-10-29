"""Choza Mane: the clan head's long wild hair, a crown of spikes that sweeps straight back into a
mane of long pointed locks fanning down to the shoulder blades, and heavy spiked sideburns."""
from anime import back_fan, bangs, ring_shell, sidelocks, spike
from paint import scalp

META = {"name": "Choza Mane", "gender": "unisex",
        "description": "Spiky crown swept back into long fanned locks to the shoulder blades, spiked sideburns."}

# The mane: (x, segments, splay z, tilt x)
MANE = [(-3.6, ((2, 4), (2, 3), (1, 2)), 34, 18), (-2.2, ((3, 5), (2, 4), (1, 2)), 18, 14),
        (-.6, ((3, 6), (2, 4), (1, 2)), 6, 12), (1.0, ((3, 6), (2, 4), (1, 2)), -6, 12),
        (2.5, ((3, 5), (2, 4), (1, 2)), -18, 14), (3.8, ((2, 4), (2, 3), (1, 2)), -34, 18)]


def build(g):
    scalp(g, 6046, side_rows=7, back_rows=8, sideburn=1)
    ring_shell(g, 6046, side_rows=7, back_rows=8, ring_row=1)
    back_fan(g, "mane", MANE, seed=6052, z=4.3, motion="sway")
    for i, (x, z, rx, rz) in enumerate(((-2.6, -2.2, -40, -22), (0, -2.6, -46, 0), (2.6, -2.2, -40, 22),
                                        (-1.4, .4, -64, -10), (1.4, .4, -64, 10))):
        spike(g, f"crown_{i}", (x, -7.8, z), (rx, 0, rz), ((3, 3), (2, 2), (1, 2)), 2, 6059 + i)
    bangs(g, "fringe", [(-2.0, ((2, 2), (1, 1)), 18), (1.8, ((2, 2), (1, 1)), -18)], seed=6066)
    sidelocks(g, "sideburn", 7, seed=6073, x=4.4, z=-2.6, flare=14, width=3)
    sidelocks(g, "ear", 8, seed=6076, x=4.5, z=.4, flare=20, width=2)
