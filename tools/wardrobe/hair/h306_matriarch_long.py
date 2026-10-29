"""Matriarch Long: Mikoto's sleek blue-black hair, parted in the middle with the bangs swept wide off
the brow, long side locks past the collarbone and one straight sheet to the waist."""
from anime import bangs, curtain, ring_shell, sidelocks
from anime import cel_box
from paint import scalp

META = {"name": "Matriarch Long", "gender": "unisex",
        "description": "Middle-parted bangs swept wide, long side locks past the collarbone, a straight sheet to the waist."}

HEM = [(0, 3, 2), (3, 3, 3), (6, 3, 2)]


def build(g):
    scalp(g, 3281, side_rows=7, back_rows=8, sideburn=1, part=3)
    ring_shell(g, 3282, side_rows=7, back_rows=8, ring_row=1)
    curtain(g, "curtain", (0, -6.2, 4.6), (-6, 0, 0), 9, 16, HEM, seed=3285)
    for side, sign in (("right", -1), ("left", 1)):
        panel = g.piece(f"side_{side}", "HEAD", (-.5, 0, -3), (1, 10, 6), pivot=(4.6 * sign, -7, 1.2))
        cel_box(panel, 3290 + (sign > 0), ring=1)
    bangs(g, "fringe", [(-2.8, ((2, 2), (1, 1)), 30), (-1.2, ((2, 1),), 40),
                        (1.2, ((2, 1),), -40), (2.8, ((2, 2), (1, 1)), -30)], seed=3295)
    sidelocks(g, "frame", 13, seed=3300, x=4.3, z=-3.4, flare=2, width=2)
