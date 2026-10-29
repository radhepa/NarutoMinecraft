"""Wanderer Shag: the grown-out look of an Uchiha on the road, ragged layers to the nape, long bangs
past the chin on both sides, the left one longer, and a scruffy fringe."""
from anime import back_fan, bangs, ring_shell, sidelocks, lock
from paint import scalp

META = {"name": "Wanderer Shag", "gender": "unisex", "description": "Ragged layers to the nape, long uneven bangs past the chin, a scruffy fringe."}

BACK = [(-3.6, ((2, 5), (1, 2)), 14, 10), (-1.8, ((2, 6), (1, 2)), 6, 8), (0, ((2, 6), (1, 2)), 0, 6),
        (1.8, ((2, 6), (1, 2)), -6, 8), (3.6, ((2, 5), (1, 2)), -14, 10)]


def build(g):
    scalp(g, 3541, side_rows=6, back_rows=8, sideburn=3)
    ring_shell(g, 3542, side_rows=6, back_rows=8, ring_row=1)
    back_fan(g, "nape", BACK, seed=3545, z=4.4, motion="sway")
    for i, (x, z, rx, rz) in enumerate(((-2.4, -2.4, 70, -20), (0, -2.6, 74, 4), (2.4, -2.4, 70, 20))):
        lock(g, f"crown_{i}", (x, -8.2, z), (rx, 0, rz), ((3, 3), (2, 2)), 1, 3560 + i * 3)
    bangs(g, "fringe", [(-2.4, ((2, 2), (1, 1)), 24), (-.7, ((2, 2), (1, 1)), 10), (1.0, ((2, 2), (1, 1)), -12),
                        (2.6, ((2, 2), (1, 1)), -26)], seed=3570)
    lock(g, "bang_right", (-4.3, -7.6, -3.7), (0, 0, 4), ((2, 8), (1, 2)), 1, 3575)
    lock(g, "bang_left", (4.3, -7.6, -3.7), (0, 0, -3), ((2, 10), (1, 3)), 1, 3578)
    sidelocks(g, "sidelock", 7, seed=3580, x=4.45, z=-1.0, flare=10, width=2)
