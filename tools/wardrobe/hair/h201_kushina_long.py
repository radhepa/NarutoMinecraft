"""Kushina Long: very long straight red hair falling past the waist, a fringe of pointed strands
across the forehead, a long lock framing each side of the face to the chest, and a slim dark clip
holding the fringe back over the left temple."""
from anime import bangs, curtain, ring_shell, sidelocks
from anime import cel_box
from kit_uzumaki import clip
from paint import scalp

META = {"name": "Kushina Long", "gender": "female",
        "description": "Straight hair past the waist, pointed fringe, chest-length face locks, a dark side clip."}


def build(g):
    scalp(g, 2010, side_rows=7, back_rows=8, sideburn=4)
    ring_shell(g, 2011, side_rows=7, back_rows=8, ring_row=1)
    curtain(g, "curtain", (0, -6.2, 4.6), (-6, 0, 0), 9, 17, [(0, 3, 3), (3, 3, 4), (6, 3, 3)], seed=2012)
    for side, sign in (("right", -1), ("left", 1)):
        panel = g.piece(f"side_{side}", "HEAD", (-.5, 0, -3), (1, 12, 7), pivot=(4.6 * sign, -7, .7), motion="sway")
        cel_box(panel, 2013 + (sign > 0), ring=1)
    bangs(g, "fringe", [(-2.9, ((2, 2), (1, 1)), 14), (-1.5, ((2, 2), (1, 1)), 6), (0, ((2, 1), (1, 1)), -4),
                        (1.5, ((2, 2), (1, 1)), -14), (2.9, ((2, 2), (1, 1)), -22)], seed=2015)
    sidelocks(g, "frame", 15, seed=2016, x=4.3, z=-3.4, flare=3, width=2)
    clip(g, "clip", (3.0, -7.9, -4.75), (-10, 0, -40))
