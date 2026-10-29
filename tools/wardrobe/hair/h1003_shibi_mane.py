"""Shibi Mane: Shibi's long, wild hair, spikes swept up off the brow and a mane of pointed locks
falling past the collar down the back and over the ears."""
from anime import back_fan, lock, ring_shell, spike
from paint import scalp

META = {"name": "Shibi Mane", "gender": "unisex",
        "description": "Spikes swept up off the brow and a mane of pointed locks down the back."}

TOP = [(-2.4, -2.6, -20, -22), (0, -2.8, -24, 0), (2.4, -2.6, -20, 22), (-1.4, .4, -46, -12), (1.4, .4, -46, 12)]
MANE = [(-4.0, ((3, 4), (2, 3), (1, 2)), 18, 10), (-2.0, ((3, 5), (2, 3), (1, 2)), 8, 14),
        (0, ((3, 6), (2, 3), (1, 2)), 0, 16), (2.0, ((3, 5), (2, 3), (1, 2)), -8, 14),
        (4.0, ((3, 4), (2, 3), (1, 2)), -18, 10)]


def build(g):
    scalp(g, 10061, side_rows=6, back_rows=8, sideburn=2)
    ring_shell(g, 10062, side_rows=6, back_rows=8, ring_row=1)
    for i, (x, z, rx, rz) in enumerate(TOP):
        spike(g, f"crown_spike_{i}", (x, -7.8, z), (rx, 0, rz), ((3, 3), (2, 2), (1, 1)), 3, 10070 + i)
    back_fan(g, "nape_mane", MANE, seed=10080, z=4.25, motion="sway")
    # Locks over each ear, behind the temple so the cheek stays clear.
    for side, sign in (("right", -1), ("left", 1)):
        lock(g, f"ear_lock_{side}", (4.45 * sign, -7.2, .8), (8, 0, -10 * sign), ((2, 5), (2, 2), (1, 1)), 3,
             10090 + (sign > 0), ring=1, motion="sway")
