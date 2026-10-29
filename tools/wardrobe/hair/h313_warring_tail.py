"""Warring Tail: a Warring States warrior's long spiky hair gathered loosely at the nape into a thick
jagged tail to the waist, with spiky crown points and long bangs framing the face."""
from anime import bangs, lock, ring_shell, sidelocks, spike, tie
from paint import scalp

META = {"name": "Warring Tail", "gender": "unisex",
        "description": "Spiky crown, long framing bangs and a thick jagged tail from the nape to the waist."}

CROWN = [(-2.6, -2.0, -20, -26), (0, -2.2, -14, 0), (2.6, -2.0, -20, 26), (-2.2, 1.0, 10, -34), (2.2, 1.0, 10, 34)]
# Jagged tail strands: (x offset, rz, segments)
TAIL = [(-.9, 5, ((2, 5), (2, 4), (1, 3))), (.9, -5, ((2, 5), (2, 4), (1, 3))), (0, 0, ((3, 5), (2, 6), (1, 4))),
        (-1.3, 12, ((2, 4), (1, 3))), (1.3, -12, ((2, 4), (1, 3)))]


def build(g):
    scalp(g, 3601, side_rows=6, back_rows=8, sideburn=3)
    ring_shell(g, 3602, side_rows=6, back_rows=8, ring_row=1)
    for i, (x, z, rx, rz) in enumerate(CROWN):
        spike(g, f"crown_spike_{i}", (x, -7.8, z), (rx, 0, rz), ((3, 3), (2, 2), (1, 1)), 3, 3610 + i)
    tie(g, "tie", (0, -2.2, 4.7), size=(4, 1, 2))
    for i, (x, rz, segs) in enumerate(TAIL):
        lock(g, f"tail_{i}", (x, -1.4, 4.9), (10, 0, rz), segs, 2, 3620 + i * 5, ring=None, motion="sway")
    bangs(g, "fringe", [(-2.4, ((2, 2), (1, 1)), 26), (0, ((2, 2), (1, 1)), 0), (2.4, ((2, 2), (1, 1)), -26)], seed=3650)
    sidelocks(g, "frame", 11, seed=3655, x=4.3, z=-3.6, flare=6, width=2)
