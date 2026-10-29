"""Crimson Flare: shoulder-length wild hair whose waves kick outward at the ends, so the whole shape
flares like a bell below the ears: the clan's mane at its most untamed, for its young fighters."""
from anime import bangs
from kit_yuhi import wave_curtain, wave_fan, wave_lock, wave_shell
from paint import scalp

META = {"name": "Crimson Flare", "gender": "unisex",
        "description": "Shoulder-length wild wavy hair with the ends kicking outward, ragged fringe."}

FLICK = [(-4.4, ((3, 2), (2, 2), (1, 1)), 36, -6), (-2.0, ((3, 2), (2, 1), (1, 1)), 22, -14), (.4, ((3, 2), (2, 1), (1, 1)), -6, -16),
         (2.6, ((3, 2), (2, 1), (1, 1)), -26, -14), (4.6, ((3, 2), (2, 2), (1, 1)), -36, -6)]


def build(g):
    scalp(g, 14481, side_rows=7, back_rows=8, sideburn=1)
    wave_shell(g, 14482, side_rows=8, back_rows=8, ring_row=1)
    bangs(g, "fringe", [(-3.0, ((2, 2), (1, 1)), 26), (-1.5, ((2, 2), (1, 1)), 8), (.2, ((2, 1), (1, 1)), -10),
                        (1.7, ((2, 2), (1, 1)), -4), (3.0, ((2, 2), (1, 1)), -28)], seed=14490)
    end = wave_curtain(g, "mass", (0, -6.6, 4.7), (-6, 0, 0), [(10, 3), (11, 2)], seed=14500, depth=2, amp=.4)
    wave_fan(g, "flick", FLICK, seed=14505, z=4.7 - end * .1 + .3, y=-6.6 + end - 1.0, amp=.3)
    for side, sign in (("right", -1), ("left", 1)):
        wave_lock(g, f"side_{side}", (4.4 * sign, -7.4, .6), (0, 0, -16 * sign), ((2, 3), (3, 2), (3, 2)), 5,
                  14510 + (sign > 0), motion="sway", amp=.35, flip=sign > 0)
        wave_lock(g, f"flick_{side}", (5.2 * sign, -1.6, .6), (0, 0, -34 * sign), ((3, 2), (2, 2), (1, 1)), 4,
                  14513 + (sign > 0), ring=None, motion="sway", amp=.3, flip=sign > 0)
        wave_lock(g, f"frame_{side}", (4.3 * sign, -7.6, -3.3), (0, 0, -6 * sign), ((2, 3), (2, 2), (1, 2)), 1,
                  14516 + (sign > 0), amp=.3, flip=sign > 0)
