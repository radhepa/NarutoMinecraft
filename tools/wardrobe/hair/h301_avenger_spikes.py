"""Avenger Spikes: the older Uchiha duck tail, blue-black spikes layered flat out behind the head in
three tiers, long bangs to the chin on both sides and a short pointed fringe over the brows."""
from anime import bangs, lock, ring_shell, sidelocks, spike
from paint import scalp

META = {"name": "Avenger Spikes", "gender": "unisex",
        "description": "Chin-length bangs, short fringe points, spikes layered out behind the head like a duck tail."}

# Back spikes in three tiers: (x, y, z, segments, tilt back, splay)
BIG = ((4, 3), (3, 2), (2, 2), (1, 1))
MID = ((3, 3), (2, 2), (1, 1))
BACK = [(-2.6, -6.6, 3.0, BIG, -84, -22), (0, -7.0, 3.0, BIG, -80, 0), (2.6, -6.6, 3.0, BIG, -84, 22),
        (-2.8, -5.0, 3.8, MID, -98, -30), (0, -5.2, 3.9, BIG, -96, 0), (2.8, -5.0, 3.8, MID, -98, 30),
        (-1.6, -3.4, 4.0, MID, -116, -16), (1.6, -3.4, 4.0, MID, -116, 16), (0, -2.2, 4.0, ((2, 2), (1, 1)), -128, 0)]


def build(g):
    scalp(g, 3001, side_rows=5, back_rows=8, sideburn=2)
    ring_shell(g, 3002, side_rows=5, back_rows=8, ring_row=1)
    for i, (x, y, z, segs, rx, rz) in enumerate(BACK):
        spike(g, f"crown_back_{i}", (x, y, z), (rx, 0, rz), segs, 3, 3010 + i)
    for i, (x, z, rx, rz) in enumerate(((-2.2, -1.8, -14, -18), (.4, -1.4, -8, 8), (2.4, -1.0, -12, 20))):
        spike(g, f"crown_top_{i}", (x, -7.8, z), (rx, 0, rz), ((3, 2), (2, 1), (1, 1)), 2, 3020 + i)
    bangs(g, "fringe", [(-2.0, ((2, 2), (1, 1)), 22), (0, ((2, 2), (1, 1)), 4), (2.0, ((2, 2), (1, 1)), -22)], seed=3025)
    sidelocks(g, "bang", 10, seed=3030, x=4.3, z=-3.7, flare=4, width=2)
    sidelocks(g, "sidelock", 7, seed=3035, x=4.45, z=-1.0, flare=10, width=2)
