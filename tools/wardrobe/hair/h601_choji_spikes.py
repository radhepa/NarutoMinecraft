"""Choji Spikes: young Choji's hair (Part I), short brown spikes standing straight up off the crown
and flaring up and out at the sides above the headband, spiky tufts at the nape and short spiky
locks in front of the ears."""
from anime import bangs, ring_shell, sidelocks, spike
from kit_akimichi import flick
from paint import scalp

META = {"name": "Choji Spikes", "gender": "unisex",
        "description": "Short spikes standing straight up and flaring out at the sides, spiky nape and ear locks."}

# Side spikes: (x, y, z, segments, tilt z); a tilt past 90 sends the spike up and out to the right.
SIDES = [(-3.8, -7.4, -1.6, ((3, 3), (2, 2), (1, 1)), 148), (-4.1, -6.6, .8, ((3, 3), (2, 2), (1, 1)), 128),
         (-4.1, -5.0, 2.6, ((2, 2), (1, 2)), 104)]
# Back spikes: (x, y, segments, tilt x, splay z)
BACK = [(-2.4, -6.6, ((3, 3), (2, 2), (1, 1)), 66, 30), (0, -6.8, ((3, 3), (2, 2), (1, 1)), 70, 0),
        (2.4, -6.6, ((3, 3), (2, 2), (1, 1)), 66, -30), (-1.4, -4.0, ((3, 2), (2, 2), (1, 1)), 52, 18),
        (1.4, -4.0, ((3, 2), (2, 2), (1, 1)), 52, -18)]


def build(g):
    scalp(g, 6001, side_rows=6, back_rows=8, sideburn=2)
    ring_shell(g, 6001, side_rows=6, back_rows=8, ring_row=1)
    for i, (x, y, z, segs, rz) in enumerate(SIDES):
        flick(g, f"side_r_{i}", (x, y, z), (0, 0, rz), segs, 2, 6007 + i)
        flick(g, f"side_l_{i}", (-x, y, z), (0, 0, -rz), segs, 2, 6014 + i)
    for i, (x, y, segs, rx, rz) in enumerate(BACK):
        flick(g, f"nape_{i}", (x, y, 4.0), (rx, 0, rz), segs, 2, 6021 + i)
    for i, (x, z, rx, rz) in enumerate(((-2.2, -1.4, -10, -14), (0, -.6, -4, 0), (2.2, -1.4, -10, 14),
                                        (-1.2, 1.8, 8, -8), (1.2, 1.8, 8, 8))):
        spike(g, f"crown_{i}", (x, -7.8, z), (rx, 0, rz), ((3, 3), (2, 2), (1, 2)), 2, 6028 + i)
    bangs(g, "fringe", [(-2.4, ((2, 2), (1, 1)), 22), (0, ((2, 2), (1, 1)), 0), (2.4, ((2, 2), (1, 1)), -22)], seed=6035)
    sidelocks(g, "ear", 6, seed=6042, x=4.35, z=-3.2, flare=10, width=2)
