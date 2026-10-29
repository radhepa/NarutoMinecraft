"""Choji Spikes: the Akimichi heir's mane, shoulder-length spikes that jut straight out to the sides
and back, a few short points on the forehead and spiky locks hanging in front of the ears."""
from anime import bangs, ring_shell, sidelocks, spike
from kit_akimichi import flick
from paint import scalp

META = {"name": "Choji Spikes", "gender": "unisex",
        "description": "Spikes jutting out to the sides and back, short forehead points, spiky ear locks."}

# Side spikes: (x, y, z, segments, tilt z); positive tilt sends the spike out to the right.
SIDES = [(-4.2, -6.4, -1.0, ((3, 2), (2, 2), (1, 1)), 96), (-4.2, -4.6, .8, ((3, 3), (2, 2), (1, 1)), 82),
         (-4.0, -3.0, 2.4, ((2, 2), (1, 2)), 64)]
# Back spikes: (x, y, segments, tilt x, splay z)
BACK = [(-2.4, -6.6, ((3, 3), (2, 2), (1, 1)), 66, 30), (0, -6.8, ((3, 3), (2, 2), (1, 1)), 70, 0),
        (2.4, -6.6, ((3, 3), (2, 2), (1, 1)), 66, -30), (-1.4, -4.0, ((3, 2), (2, 2), (1, 1)), 52, 18),
        (1.4, -4.0, ((3, 2), (2, 2), (1, 1)), 52, -18)]


def build(g):
    scalp(g, 6001, side_rows=6, back_rows=8, sideburn=2)
    ring_shell(g, 6002, side_rows=6, back_rows=8, ring_row=1)
    for i, (x, y, z, segs, rz) in enumerate(SIDES):
        flick(g, f"side_r_{i}", (x, y, z), (0, 0, rz), segs, 2, 6010 + i)
        flick(g, f"side_l_{i}", (-x, y, z), (0, 0, -rz), segs, 2, 6020 + i)
    for i, (x, y, segs, rx, rz) in enumerate(BACK):
        flick(g, f"nape_{i}", (x, y, 4.0), (rx, 0, rz), segs, 2, 6030 + i)
    for i, (x, z, rx, rz) in enumerate(((-2.2, -1.4, -14, -24), (0, -.4, -6, 0), (2.2, -1.4, -14, 24))):
        spike(g, f"crown_{i}", (x, -7.8, z), (rx, 0, rz), ((3, 2), (2, 1), (1, 1)), 2, 6040 + i)
    bangs(g, "fringe", [(-2.4, ((2, 2), (1, 1)), 22), (0, ((2, 2), (1, 1)), 0), (2.4, ((2, 2), (1, 1)), -22)], seed=6050)
    sidelocks(g, "ear", 6, seed=6060, x=4.35, z=-3.2, flare=10, width=2)
