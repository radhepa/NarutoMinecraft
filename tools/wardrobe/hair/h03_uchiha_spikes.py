"""Uchiha Spikes: blue-black anime hair, long bangs framing the face to the jaw and a crown of
spikes sweeping up and out behind the head."""
from anime import bangs, lock, ring_shell, sidelocks, spike
from paint import scalp

META = {"name": "Uchiha Spikes", "gender": "male",
        "description": "Jaw-length face-framing bangs, short fringe points, spikes swept up behind the head."}

# Back spikes: (x, y, z, segments, tilt back, splay)
BACK = [(-2.4, -6.6, 2.4, ((4, 3), (3, 2), (2, 2), (1, 1)), -64, -26),
        (0, -7.2, 2.6, ((4, 4), (3, 2), (2, 2), (1, 1)), -58, 0),
        (2.4, -6.6, 2.4, ((4, 3), (3, 2), (2, 2), (1, 1)), -64, 26),
        (-1.4, -4.8, 3.4, ((3, 3), (2, 2), (1, 1)), -82, -14),
        (1.4, -4.8, 3.4, ((3, 3), (2, 2), (1, 1)), -82, 14),
        (0, -3.4, 3.8, ((3, 2), (2, 2), (1, 1)), -96, 0)]


def build(g):
    scalp(g, 401, side_rows=5, back_rows=8, sideburn=2)
    ring_shell(g, 402, side_rows=5, back_rows=8, ring_row=1)
    for i, (x, y, z, segs, rx, rz) in enumerate(BACK):
        spike(g, f"crown_back_{i}", (x, y, z), (rx, 0, rz), segs, 3, 410 + i)
    for i, (x, z, rx, rz) in enumerate(((-2.0, -1.6, -16, -14), (1.6, -1.0, -10, 16))):
        spike(g, f"crown_top_{i}", (x, -7.8, z), (rx, 0, rz), ((3, 2), (2, 1), (1, 1)), 2, 420 + i)
    bangs(g, "fringe", [(-1.6, ((2, 2), (1, 1)), 18), (1.2, ((2, 2), (1, 1)), -12)], seed=430)
    sidelocks(g, "bang", 8, seed=440, x=4.3, z=-3.7, flare=3, width=2)
    sidelocks(g, "sidelock", 6, seed=450, x=4.45, z=-1.2, flare=8, width=2)
