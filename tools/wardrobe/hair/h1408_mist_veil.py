"""Mist Veil: the longest of the clan's manes, worn by its genjutsu elders: a middle part, long
rippling face-framing locks to the chest and a wide veil of waves falling to the waist."""
from anime import bangs
from kit_yuhi import wave_curtain, wave_fan, wave_lock, wave_shell
from paint import scalp

META = {"name": "Mist Veil", "gender": "unisex",
        "description": "Very long wavy hair to the waist, middle part, long rippling face-framing locks."}

HEM = [(-3.8, ((3, 3), (2, 2), (1, 2)), 10, -6), (-1.3, ((3, 3), (2, 3), (1, 1)), 3, -8), (1.3, ((3, 3), (2, 3), (1, 1)), -3, -8),
       (3.8, ((3, 3), (2, 2), (1, 2)), -10, -6)]


def build(g):
    scalp(g, 14281, side_rows=7, back_rows=8, sideburn=1, part=3)
    wave_shell(g, 14282, side_rows=8, back_rows=8, ring_row=1)
    bangs(g, "fringe", [(-2.7, ((2, 2), (1, 1)), 16), (-1.3, ((2, 1), (1, 1)), 30), (1.3, ((2, 1), (1, 1)), -30),
                        (2.7, ((2, 2), (1, 1)), -16)], seed=14290)
    end = wave_curtain(g, "veil", (0, -6.6, 4.7), (-7, 0, 0), [(10, 3), (10, 3), (10, 3), (10, 3)], seed=14300, depth=2,
                       amp=.4)
    wave_fan(g, "hem", HEM, seed=14310, z=4.7 - end * .122 + .3, y=-6.6 + end - 1.0, amp=.35)
    for side, sign in (("right", -1), ("left", 1)):
        wave_lock(g, f"side_{side}", (4.4 * sign, -7.4, 1.0), (0, 0, -8 * sign), ((2, 4), (2, 4), (2, 3), (1, 2)), 5,
                  14320 + (sign > 0), motion="sway", amp=.35, flip=sign > 0)
        wave_lock(g, f"frame_{side}", (4.3 * sign, -7.6, -3.3), (0, 0, -3 * sign), ((2, 4), (2, 4), (2, 3), (1, 2)), 1,
                  14324 + (sign > 0), amp=.35, flip=sign > 0)
