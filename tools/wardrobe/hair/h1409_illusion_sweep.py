"""Illusion Sweep: wavy hair to the collarbone with the fringe swept across in one long wave, like
a veil drawn aside, held clear of the eyes and spilling over the right ear."""
from anime import bangs
from kit_yuhi import wave_curtain, wave_fan, wave_lock, wave_shell
from paint import scalp

META = {"name": "Illusion Sweep", "gender": "unisex",
        "description": "Wavy hair to the collarbone, the fringe swept across in one long wave."}

HEM = [(-3.4, ((3, 2), (2, 2), (1, 1)), 12, -6), (-.8, ((3, 3), (2, 1), (1, 1)), 2, -8), (1.8, ((3, 2), (2, 2), (1, 1)), -8, -6),
       (3.8, ((2, 2), (1, 2)), -16, -6)]


def build(g):
    scalp(g, 14321, side_rows=7, back_rows=8, sideburn=1)
    wave_shell(g, 14322, side_rows=7, back_rows=8, ring_row=1)
    # The sweep: every fringe lock leans the same way, the outermost falling longest past the right ear.
    bangs(g, "fringe", [(3.1, ((2, 2), (1, 1)), 56), (1.7, ((2, 1), (1, 1)), 60), (.2, ((2, 1), (1, 1)), 64),
                        (-1.3, ((2, 1), (1, 1)), 68), (-2.8, ((2, 2), (1, 1)), 62)], seed=14330)
    wave_lock(g, "sweep_end", (-4.3, -7.2, -3.4), (0, 0, 10), ((2, 3), (2, 3), (2, 2), (1, 2)), 1, 14335, amp=.4)
    end = wave_curtain(g, "mass", (0, -6.6, 4.7), (-6, 0, 0), [(10, 3), (10, 3)], seed=14340, depth=2, amp=.35)
    wave_fan(g, "hem", HEM, seed=14350, z=4.7 - end * .1 + .3, y=-6.6 + end - 1.0, amp=.3)
    for side, sign in (("right", -1), ("left", 1)):
        wave_lock(g, f"side_{side}", (4.4 * sign, -7.4, 1.0), (0, 0, -10 * sign), ((2, 4), (2, 3), (2, 2), (1, 1)), 4,
                  14360 + (sign > 0), motion="sway", amp=.35, flip=sign > 0)
    wave_lock(g, "frame_left", (4.3, -7.6, -3.3), (0, 0, -4), ((2, 3), (2, 3), (1, 2)), 1, 14365, amp=.3, flip=True)
