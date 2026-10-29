"""Kurenai Wild Mane: Kurenai Yuhi's untamed black hair, long and wavy to the upper back. A ragged
fringe to the brows, long rippling locks framing the face past the chin, a full cloud of hair over
the ears and one broad wavy mass down the back that breaks into flared points at the hem."""
from anime import bangs
from kit_yuhi import wave_curtain, wave_fan, wave_lock, wave_shell
from paint import scalp

META = {"name": "Kurenai Wild Mane", "gender": "unisex",
        "description": "Long untamed wavy hair to the upper back, ragged fringe, rippling face-framing locks."}

MASS_PIVOT, MASS_TILT = (0, -6.6, 4.7), (-9, 0, 0)
# The hem: wavy points hanging below the mass, the outer ones flaring out. (x, segments, rz, rx)
HEM = [(-4.4, ((3, 3), (2, 3), (1, 2)), 22, -6), (-2.0, ((3, 3), (2, 2), (1, 2)), 8, -8), (.4, ((3, 4), (2, 2), (1, 1)), -4, -8),
       (2.6, ((3, 3), (2, 2), (1, 2)), -10, -8), (4.6, ((3, 3), (2, 3), (1, 2)), -22, -6)]


def build(g):
    scalp(g, 14001, side_rows=7, back_rows=8, sideburn=1)
    wave_shell(g, 14002, side_rows=8, back_rows=8, ring_row=1)
    bangs(g, "fringe", [(-3.1, ((2, 2), (1, 2)), 22), (-1.7, ((2, 2), (1, 1)), 10), (-.2, ((2, 1), (1, 1)), -6),
                        (1.4, ((2, 2), (1, 1)), -16), (2.9, ((2, 2), (1, 2)), -26)], seed=14010)
    end = wave_curtain(g, "mass", MASS_PIVOT, MASS_TILT, [(10, 3), (11, 3), (11, 3)], seed=14020, depth=2, amp=.4)
    wave_fan(g, "hem", HEM, seed=14040, z=4.7 - end * .156 + .3, y=-6.6 + end * .988 - 1.0, amp=.35)
    # Cloud of hair over each ear, flaring out past the shoulders, and rippling face-framing locks.
    for side, sign in (("right", -1), ("left", 1)):
        wave_lock(g, f"side_{side}", (4.4 * sign, -7.6, 1.0), (0, 0, -14 * sign), ((2, 4), (3, 4), (3, 3), (2, 2), (1, 1)), 5,
                  14030 + (sign > 0), motion="sway", amp=.4, flip=sign > 0)
        wave_lock(g, f"frame_{side}", (4.3 * sign, -7.6, -3.2), (0, 0, -5 * sign), ((2, 4), (2, 3), (2, 2), (1, 2)), 2,
                  14034 + (sign > 0), amp=.35, flip=sign > 0)
