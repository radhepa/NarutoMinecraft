"""Thorn Half-Up: the clan's waves half pinned up, the crown gathered into a small wound knot at the
back of the head and the rest left to ripple down past the shoulders."""
from anime import bangs, tie
from kit_yuhi import wave_box, wave_curtain, wave_fan, wave_lock, wave_shell
from paint import scalp

META = {"name": "Thorn Half-Up", "gender": "unisex",
        "description": "Wavy hair half up in a small knot at the crown, the rest rippling past the shoulders."}

HEM = [(-3.6, ((3, 3), (2, 2), (1, 1)), 14, -6), (-1.2, ((3, 3), (2, 2), (1, 1)), 4, -8), (1.2, ((3, 3), (2, 2), (1, 1)), -4, -8),
       (3.6, ((3, 3), (2, 2), (1, 1)), -14, -6)]


def build(g):
    scalp(g, 14201, side_rows=7, back_rows=8, sideburn=1)
    wave_shell(g, 14202, side_rows=8, back_rows=8, ring_row=1)
    bangs(g, "fringe", [(-2.8, ((2, 2), (1, 1)), 18), (-1.2, ((2, 1), (1, 1)), 28), (1.2, ((2, 1), (1, 1)), -28),
                        (2.8, ((2, 2), (1, 1)), -18)], seed=14210)
    knot = g.piece("knot", "HEAD", (-1.5, -1.5, -1), (3, 3, 2), pivot=(0, -6.6, 5.0))
    wave_box(knot, 14220, base=2, ring=0)
    tie(g, "knot_tie", (0, -6.6, 4.5), size=(2, 2, 1), y=-1)
    end = wave_curtain(g, "mass", (0, -5.6, 4.7), (-8, 0, 0), [(9, 3), (10, 3), (9, 2)], seed=14230, depth=2, amp=.35)
    wave_fan(g, "hem", HEM, seed=14240, z=4.7 - end * .14 + .3, y=-5.6 + end - 1.0, amp=.3)
    for side, sign in (("right", -1), ("left", 1)):
        wave_lock(g, f"side_{side}", (4.4 * sign, -7.4, 1.0), (0, 0, -10 * sign), ((2, 4), (2, 4), (2, 2), (1, 1)), 4,
                  14250 + (sign > 0), motion="sway", amp=.35, flip=sign > 0)
        wave_lock(g, f"frame_{side}", (4.3 * sign, -7.6, -3.3), (0, 0, -4 * sign), ((2, 4), (2, 3), (1, 2)), 1,
                  14254 + (sign > 0), amp=.3, flip=sign > 0)
