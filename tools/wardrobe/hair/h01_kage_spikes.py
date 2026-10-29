"""Kage Spikes: bright, layered spikes like the Fourth's, with long jaw-length bangs framing the face.

Crown pieces start with "crown" so a kage hat can hide them; the bangs and sidelocks stay visible.
"""
from anime import bangs, cel_box, lock, ring_shell, sidelocks, spike
from paint import scalp

META = {"name": "Kage Spikes", "gender": "male", "description": "Layered spikes, jaw-length bangs and a spiky nape."}

# Crown spikes: (x, z, segments, tilt x, tilt z)
CROWN = [(-2.8, -2.6, ((3, 2), (2, 2), (1, 1)), -30, -26), (0, -3.0, ((3, 3), (2, 2), (1, 1)), -34, 0),
         (2.8, -2.6, ((3, 2), (2, 2), (1, 1)), -30, 26), (-3.2, .6, ((3, 2), (2, 2), (1, 1)), -6, -40),
         (3.2, .6, ((3, 2), (2, 2), (1, 1)), -6, 40), (-1.4, .4, ((3, 3), (2, 2), (1, 1)), 6, -12),
         (1.4, .4, ((3, 3), (2, 2), (1, 1)), 6, 12), (0, 2.8, ((3, 2), (2, 2), (1, 1)), 34, 0)]


def build(g):
    scalp(g, 201, side_rows=4, back_rows=8, sideburn=2)
    ring_shell(g, 202, side_rows=4, back_rows=7, ring_row=1)
    for i, (x, z, segs, rx, rz) in enumerate(CROWN):
        spike(g, f"crown_spike_{i}", (x, -7.8, z), (rx, 0, rz), segs, 2, 210 + i)
    # Short fringe points that stop above the brows, and long bangs outside the eyes.
    bangs(g, "fringe", [(-2.2, ((2, 2), (1, 1)), 14), (0.1, ((2, 2), (1, 1)), -6), (2.3, ((2, 2), (1, 1)), -16)], seed=230)
    sidelocks(g, "bang", 7, seed=240, x=4.35, z=-3.6, flare=6, width=2)
    sidelocks(g, "sidelock", 5, seed=250, x=4.4, z=-.6, flare=12, width=2)
    # Spiky nape fanning outward.
    for i, (x, rz, rx) in enumerate(((-3.0, 28, 30), (-1.0, 8, 38), (1.0, -8, 38), (3.0, -28, 30))):
        lock(g, f"nape_{i}", (x, -3.6, 4.3), (rx, 0, rz), ((2, 2), (1, 2)), 1, 260 + i * 5)
