"""Veiled Sweep: a deep side part with everything swept to one side, where a long lock falls past the
cheek to the chest like a half-drawn veil; the other side is cut short above the ear and the back
tapers to the nape. A genjutsu user's half-hidden look that still leaves both eyes clear."""
from anime import back_fan, cel_box, ring_shell
from kit_kurama import part_line, side_fringe, wave_lock
from paint import scalp

META = {"name": "Veiled Sweep", "gender": "unisex",
        "description": "Deep side part, a long lock falling past one cheek to the chest, the other side short."}


def build(g):
    scalp(g, 12560, side_rows=4, back_rows=7, sideburn=1, part=6)
    ring_shell(g, 12561, side_rows=4, back_rows=6, ring_row=1)
    part_line(g, 6)
    panel = g.piece("veil_side", "HEAD", (-.5, 0, -3.5), (1, 8, 7), pivot=(-4.6, -7.8, .4))
    cel_box(panel, 12564, ring=1)
    wave_lock(g, "veil", (-4.3, -7.8, -3.1), (0, 0, 4), ((3, 5), (3, 4), (2, 3), (2, 2), (1, 1)), 2, 12570, amp=.25)
    back_fan(g, "nape", [(-2.6, ((3, 2), (2, 1)), 20, 18), (0, ((3, 2), (2, 1)), 0, 20), (2.6, ((2, 2), (1, 1)), -24, 22)],
             seed=12590)
    side_fringe(g, "fringe", 12600, side=1, specs=[(-3.4, ((2, 2), (1, 1)), -6), (-1.8, ((3, 2), (2, 1)), -26),
                                                   (.2, ((3, 2), (2, 1)), -30), (2.2, ((2, 2), (1, 1)), -30)])
