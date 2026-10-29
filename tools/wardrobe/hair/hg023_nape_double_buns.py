"""Nape Double Buns: the hair parted down the back and wound into two round buns low at the nape,
a short tail escaping beneath each, a soft side-swept fringe and fine locks at the temples."""
from anime import bangs, lock, ring_shell, sidelocks
from kit_kunoichi import round_bun
from paint import scalp

META = {"name": "Nape Double Buns", "gender": "female",
        "description": "Two round buns low at the nape with short tails beneath, a side-swept fringe."}


def build(g):
    scalp(g, 33830, side_rows=6, back_rows=8, sideburn=2, part=4)
    ring_shell(g, 33831, side_rows=6, back_rows=8, ring_row=1)
    g.part("hat").back.vline(3, 0, 7, "H1"), g.part("hat").back.vline(4, 0, 7, "H1")
    for side, sign in (("right", -1), ("left", 1)):
        pivot = (2.3 * sign, -3.0, 4.2)
        round_bun(g, f"bun_{side}", pivot, (0, 22 * sign, 0), size=4, seed=33832 + (sign > 0) * 3)
        lock(g, f"bun_{side}_tail", (2.3 * sign, -1.6, 5.2), (14, 0, -6 * sign), ((2, 3), (1, 2)), 1, 33838 + (sign > 0),
             ring=None, motion="sway")
    bangs(g, "fringe", [(-2.7, ((2, 2), (1, 1)), 30), (-1.0, ((3, 2), (2, 1)), 44), (1.0, ((3, 2), (1, 1)), 48),
                        (2.8, ((2, 2), (1, 1)), -14)], seed=33841)
    sidelocks(g, "frame", 6, seed=33846, x=4.3, z=-3.4, flare=4, width=1, taper=False)
