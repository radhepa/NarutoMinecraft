"""Kurenai Shoulder Waves: Kurenai in later years, her wild hair cut to the shoulders. The same ragged
fringe and rippling face-framing locks, the waves now ending in loose points on the shoulders."""
from anime import bangs
from kit_yuhi import wave_curtain, wave_fan, wave_lock, wave_shell
from paint import scalp

META = {"name": "Kurenai Shoulder Waves", "gender": "unisex",
        "description": "Wavy black hair cut to the shoulders, ragged fringe, rippling face-framing locks."}

HEM = [(-3.8, ((3, 2), (2, 2), (1, 1)), 18, -6), (-1.3, ((3, 3), (2, 1), (1, 1)), 6, -8), (1.3, ((3, 3), (2, 1), (1, 1)), -6, -8),
       (3.8, ((3, 2), (2, 2), (1, 1)), -18, -6)]


def build(g):
    scalp(g, 14041, side_rows=7, back_rows=8, sideburn=1)
    wave_shell(g, 14042, side_rows=8, back_rows=8, ring_row=1)
    bangs(g, "fringe", [(-3.0, ((2, 2), (1, 2)), 20), (-1.5, ((2, 2), (1, 1)), 12), (.1, ((2, 1), (1, 1)), -8),
                        (1.6, ((2, 2), (1, 1)), -14), (3.0, ((2, 2), (1, 1)), -24)], seed=14050)
    end = wave_curtain(g, "mass", (0, -6.6, 4.7), (-8, 0, 0), [(10, 3), (10, 2)], seed=14060, depth=2, amp=.35)
    wave_fan(g, "hem", HEM, seed=14070, z=4.7 - end * .14 + .3, y=-6.6 + end - 1.0, amp=.3)
    for side, sign in (("right", -1), ("left", 1)):
        wave_lock(g, f"side_{side}", (4.4 * sign, -7.6, 1.0), (0, 0, -12 * sign), ((2, 4), (3, 3), (2, 2), (1, 1)), 5,
                  14080 + (sign > 0), motion="sway", amp=.35, flip=sign > 0)
        wave_lock(g, f"frame_{side}", (4.3 * sign, -7.6, -3.2), (0, 0, -5 * sign), ((2, 3), (2, 3), (1, 2)), 2,
                  14084 + (sign > 0), amp=.35, flip=sign > 0)
