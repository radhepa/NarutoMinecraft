"""Braid Crown: a braid drawn over the crown from ear to ear like a headband, keeping the fringe
off the face, and the rest of the hair loose and straight to the shoulder blades."""
import math

from anime import cel_box, ring_shell, sidelocks
from paint import k, scalp

META = {"name": "Braid Crown", "gender": "female",
        "description": "A braid across the crown from ear to ear, the rest loose to the shoulder blades."}


def build(g):
    scalp(g, 33850, side_rows=7, back_rows=8, sideburn=2)
    ring_shell(g, 33851, side_rows=7, back_rows=8, ring_row=None)
    # The crown braid: links set on an arc over the head from the right ear to the left.
    for i in range(7):
        a = math.radians(-78 + i * 26)
        link = g.piece(f"crown_braid_{i}", "HEAD", (-1, -1.2, -1.5), (2, 2, 3),
                       pivot=(4.5 * math.sin(a), -4.0 - 4.7 * math.cos(a), -1.7), rotation=(0, 0, math.degrees(a)))
        cel_box(link, 33975 + i, top_delta=1)
        for f in link.faces:
            for x2 in range(f.w):
                f.set(x2, (x2 + i) % 2, k("H", 3 if (x2 + i) % 2 == 0 else 1))
    sheet = g.piece("length", "HEAD", (-4.5, 0, -.5), (9, 10, 1), pivot=(0, -6.4, 4.6), rotation=(-7, 0, 0), motion="sway")
    cel_box(sheet, 33858, ring=1)
    for i, x in enumerate((-3.0, 0, 3.0)):
        tip = g.piece(f"length_tip_{i}", "HEAD", (x - 1.5, 10, -.5), (3, 2 - (i == 1), 1), pivot=(0, -6.4, 4.6),
                      rotation=(-7, 0, 0), motion="sway")
        cel_box(tip, 33859 + i, top_delta=0)
    for side, sign in (("right", -1), ("left", 1)):
        panel = g.piece(f"side_{side}", "HEAD", (-.5, 0, -3), (1, 8, 7), pivot=(4.6 * sign, -7.0, .7))
        cel_box(panel, 33862 + (sign > 0), ring=1)
    sidelocks(g, "frame", 7, seed=33864, x=4.3, z=-3.6, flare=3, width=1, taper=False)
