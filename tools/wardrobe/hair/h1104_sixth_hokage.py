"""Sixth Hokage: Kakashi in the Hokage years, the same slanting silver spikes worn a little shorter
and swept further back so the kage hat sits over them, neat sides and a clean nape."""
from anime import bangs, lock, ring_shell, sidelocks, spike
from paint import scalp

META = {"name": "Sixth Hokage", "gender": "unisex",
        "description": "Slanting silver spikes worn shorter and swept back, a few brow points, neat sides."}

BIG = ((4, 3), (3, 2), (2, 2), (1, 1))
MID = ((3, 2), (2, 2), (1, 2))
CROWN = [(-2.2, -2.2, MID, -4, 36), (.4, -2.4, BIG, 2, 40), (2.6, -1.6, MID, 4, 58),
         (-2.4, .6, BIG, 20, 34), (.4, .8, BIG, 22, 40), (2.6, 1.0, MID, 22, 56),
         (-1.0, 3.0, MID, 40, 36), (1.8, 3.0, MID, 42, 48)]


def build(g):
    scalp(g, 11301, side_rows=4, back_rows=8, sideburn=2)
    ring_shell(g, 11302, side_rows=4, back_rows=7, ring_row=1)
    for i, (x, z, segs, rx, rz) in enumerate(CROWN):
        spike(g, f"crown_spike_{i}", (x, -7.6, z), (rx, 0, rz), segs, 3, 11310 + i)
    bangs(g, "fringe", [(-2.4, ((2, 2), (1, 1)), 26), (-.4, ((2, 1), (1, 1)), 22)], seed=11330)
    sidelocks(g, "sidelock", 4, seed=11340, x=4.4, z=-2.2, flare=12, width=2)
    for i, (x, rz, rx) in enumerate(((-2.6, 20, 30), (0, 4, 36), (2.6, -16, 30))):
        lock(g, f"nape_{i}", (x, -3.8, 4.3), (rx, 0, rz), ((2, 2), (1, 1)), 1, 11350 + i * 5)
