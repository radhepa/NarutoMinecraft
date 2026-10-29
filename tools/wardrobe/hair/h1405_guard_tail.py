"""Guard Tail: Mirai's messy layers tied back for a mission, a short wavy tail at the nape and loose
locks left free over the ears: the guard of a young Yuhi jonin."""
from anime import bangs, tie
from kit_yuhi import wave_lock, wave_shell
from paint import scalp

META = {"name": "Guard Tail", "gender": "unisex",
        "description": "Messy layered hair tied in a short wavy tail at the nape, loose locks over the ears."}


def build(g):
    scalp(g, 14161, side_rows=6, back_rows=8, sideburn=2)
    wave_shell(g, 14162, side_rows=6, back_rows=8, ring_row=1)
    bangs(g, "fringe", [(-2.9, ((2, 2), (1, 1)), 22), (-1.3, ((2, 1), (1, 1)), 12), (.4, ((2, 2), (1, 1)), -6),
                        (2.2, ((2, 1), (1, 1)), -20), (3.2, ((1, 2), (1, 1)), -30)], seed=14170)
    tie(g, "tie", (0, -2.0, 4.7), size=(3, 1, 2))
    wave_lock(g, "tail", (0, -1.4, 4.8), (14, 0, 0), ((3, 3), (3, 2), (2, 2), (1, 1)), 2, 14180, ring=None, motion="sway",
              amp=.4)
    for side, sign in (("right", -1), ("left", 1)):
        wave_lock(g, f"loose_{side}", (4.3 * sign, -7.6, -2.6), (0, 0, -8 * sign), ((2, 3), (2, 3), (1, 2)), 2,
                  14190 + (sign > 0), amp=.3, flip=sign > 0)
