"""Elder Mane: a long loose mane brushed straight back from a high brow, falling past the shoulders
in spiky points, with sideburn locks over the ears: the look of the clan's elders."""
from anime import back_fan, lock, ring_shell, spike
from paint import scalp

META = {"name": "Elder Mane", "gender": "unisex",
        "description": "Long loose spiky mane brushed back from the brow, past the shoulders, sideburn locks."}

FAN = [(-3.2, ((3, 4), (2, 4), (1, 2)), 14, 8), (-1.1, ((3, 5), (2, 4), (1, 3)), 4, 6), (1.1, ((3, 5), (2, 4), (1, 3)), -4, 6),
       (3.2, ((3, 4), (2, 4), (1, 2)), -14, 8), (0, ((3, 4), (2, 3), (1, 2)), 0, 20)]


def build(g):
    scalp(g, 7271, side_rows=6, back_rows=8, sideburn=3)
    ring_shell(g, 7272, side_rows=6, back_rows=8, ring_row=1)
    for i, (x, z, rx, rz) in enumerate(((-2.4, -2.6, -58, -12), (0, -2.8, -62, 0), (2.4, -2.6, -58, 12),
                                        (-1.4, .2, -74, -8), (1.4, .2, -74, 8))):
        spike(g, f"crown_{i}", (x, -7.8, z), (rx, 0, rz), ((3, 3), (2, 2), (1, 1)), 3, 7280 + i)
    back_fan(g, "mane", FAN, seed=7290, motion="sway")
    for side, sign in (("right", -1), ("left", 1)):
        lock(g, f"sideburn_{side}", (4.45 * sign, -7.0, -1.4), (0, 0, -8 * sign), ((2, 6), (1, 2)), 2, 7296 + (sign > 0))
