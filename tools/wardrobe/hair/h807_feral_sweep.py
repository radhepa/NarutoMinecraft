"""Feral Sweep: everything raked straight back as if from a dead run on all fours, long spikes
streaming off the back of the head, the forehead clear and two short wisps at the temples."""
from anime import lock, ring_shell, sidelocks
from kit_inuzuka import burst
from paint import scalp

META = {"name": "Feral Sweep", "gender": "unisex",
        "description": "Long spikes raked straight back off the head, a clear forehead, wisps at the temples."}

LONG = ((3, 3), (3, 2), (2, 2), (1, 2))
MID = ((3, 2), (2, 2), (1, 1))
CROWN = [(-2.4, -2.6, MID, -66, -14), (0, -2.8, LONG, -70, 0), (2.4, -2.6, MID, -66, 14), (-2.8, .2, LONG, -80, -22),
         (0, .2, LONG, -78, 0), (2.8, .2, LONG, -80, 22), (-1.6, 2.6, LONG, -96, -12), (1.6, 2.6, LONG, -96, 12)]


def build(g):
    scalp(g, 8181, side_rows=5, back_rows=8, sideburn=2)
    ring_shell(g, 8182, side_rows=5, back_rows=7, ring_row=1)
    burst(g, "crown_spike", CROWN, 8183, depth=3)
    sidelocks(g, "wisp", 4, seed=8192, x=4.4, z=-3.2, flare=20, width=1)
    for i, (x, rz) in enumerate(((-2.2, 14), (0, 0), (2.2, -14))):
        lock(g, f"nape_{i}", (x, -3.6, 4.3), (62, 0, rz), ((2, 3), (1, 2)), 1, 8196 + i * 5)
