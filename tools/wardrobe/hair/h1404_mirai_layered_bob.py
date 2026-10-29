"""Mirai Layered Bob: after Mirai Sarutobi, the Yuhi side of her look: short black hair in messy
layers to the jaw, a choppy fringe flicked to one side and wavy ends turning out at the nape."""
from anime import bangs
from kit_yuhi import wave_curtain, wave_fan, wave_lock, wave_shell
from paint import scalp

META = {"name": "Mirai Layered Bob", "gender": "unisex",
        "description": "Short messy layered bob to the jaw, choppy side-flicked fringe, wavy ends."}

ENDS = [(-3.6, ((2, 2), (1, 1)), 30, -10), (-1.4, ((2, 2), (1, 1)), 10, -12), (1.0, ((2, 2), (1, 1)), -10, -12),
        (3.4, ((2, 2), (1, 1)), -30, -10)]


def build(g):
    scalp(g, 14121, side_rows=7, back_rows=8, sideburn=1)
    wave_shell(g, 14122, side_rows=7, back_rows=8, ring_row=1)
    bangs(g, "fringe", [(-3.0, ((2, 2), (1, 1)), 30), (-1.5, ((2, 2), (1, 1)), 26), (.1, ((2, 1), (1, 1)), 18),
                        (1.7, ((2, 1), (1, 1)), 8), (3.0, ((2, 2), (1, 1)), -20)], seed=14130)
    end = wave_curtain(g, "nape", (0, -7.0, 4.6), (-4, 0, 0), [(9, 3), (9, 3)], seed=14140, depth=2, amp=.3)
    wave_fan(g, "ends", ENDS, seed=14150, y=-7.0 + end - .8, z=4.4, amp=.3)
    for side, sign in (("right", -1), ("left", 1)):
        wave_lock(g, f"side_{side}", (4.4 * sign, -7.6, .4), (0, 0, -8 * sign), ((2, 3), (2, 3), (1, 1)), 6,
                  14160 + (sign > 0), amp=.3, flip=sign > 0)
        wave_lock(g, f"frame_{side}", (4.3 * sign, -7.6, -3.3), (0, 0, -4 * sign), ((2, 3), (2, 2), (1, 2)), 1,
                  14164 + (sign > 0), amp=.3, flip=sign > 0)
