"""Shaggy Crop: short ragged hair that sticks up and out in small spikes all over, a choppy fringe
and spiky tufts over the ears: easy to keep under a protector."""
from anime import bangs, ring_shell, spike
from kit_akimichi import flick
from paint import scalp

META = {"name": "Shaggy Crop", "gender": "unisex", "description": "Short ragged spikes all over, choppy fringe, spiky ear tufts."}


def build(g):
    scalp(g, 7001, side_rows=4, back_rows=7, sideburn=2)
    ring_shell(g, 7002, side_rows=4, back_rows=7, ring_row=1)
    for i, (x, z, rx, rz) in enumerate(((-2.6, -2.4, -24, -30), (0, -2.0, -20, 4), (2.6, -2.4, -24, 30),
                                        (-2.0, .8, 10, -24), (2.0, .8, 10, 24), (0, 2.6, 34, 0))):
        spike(g, f"crown_{i}", (x, -7.8, z), (rx, 0, rz), ((2, 2), (1, 1)), 2, 7010 + i)
    for side, sign in (("right", -1), ("left", 1)):
        for i, (y, z) in enumerate(((-5.8, -1.0), (-4.4, 1.4))):
            flick(g, f"ear_{side}_{i}", (4.1 * sign, y, z), (0, 0, -84 * sign), ((2, 2), (1, 1)), 1, 7020 + i + (sign > 0) * 3)
    for i, (x, rz) in enumerate(((-2.2, 30), (0, -26), (2.2, 30))):
        flick(g, f"nape_{i}", (x, -2.8, 4.1), (40, 0, rz), ((2, 2), (1, 1)), 1, 7030 + i)
    bangs(g, "fringe", [(-2.6, ((2, 2), (1, 1)), 26), (-.7, ((2, 2), (1, 1)), -8), (1.3, ((2, 2), (1, 1)), 20),
                        (2.8, ((2, 1), (1, 1)), -24)], seed=7040)
