"""Wave Ponytail: the clan's waves pulled up into a high ponytail that ripples down to the shoulder
blades, a ragged fringe and short wavy locks left loose at the temples."""
from anime import bangs, tie
from kit_yuhi import wave_lock, wave_shell
from paint import scalp

META = {"name": "Wave Ponytail", "gender": "unisex",
        "description": "High wavy ponytail to the shoulder blades, ragged fringe, loose wavy temple locks."}


def build(g):
    scalp(g, 14401, side_rows=6, back_rows=8, sideburn=2)
    wave_shell(g, 14402, side_rows=6, back_rows=8, ring_row=1)
    bangs(g, "fringe", [(-2.9, ((2, 2), (1, 1)), 20), (-1.4, ((2, 1), (1, 1)), 10), (.2, ((2, 1), (1, 1)), -8),
                        (1.7, ((2, 2), (1, 1)), -16), (3.0, ((1, 2), (1, 1)), -26)], seed=14410)
    tie(g, "tie", (0, -7.2, 4.6), size=(3, 2, 2), y=-1)
    wave_lock(g, "tail", (0, -7.0, 5.0), (24, 0, 0), ((3, 3), (4, 3), (4, 3), (3, 3), (2, 2), (1, 1)), 3, 14430,
              ring=None, motion="sway", amp=.5)
    for side, sign in (("right", -1), ("left", 1)):
        wave_lock(g, f"temple_{side}", (4.3 * sign, -7.6, -3.2), (0, 0, -6 * sign), ((2, 3), (1, 3), (1, 1)), 1,
                  14440 + (sign > 0), amp=.35, flip=sign > 0)
