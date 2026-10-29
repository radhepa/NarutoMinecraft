"""Sentinel Knot: hair pulled straight back off the face and bound in a small hard knot at the back
of the crown, its short end curling over, nothing loose to catch on a blade."""
from anime import cel_box, ring_shell
from kit_namiashi import wave_lock
from paint import scalp

META = {"name": "Sentinel Knot", "gender": "unisex",
        "description": "Hair pulled straight back into a small hard knot at the back of the crown, the end curling over."}


def build(g):
    scalp(g, 20221, side_rows=4, back_rows=8, sideburn=2)
    hat = ring_shell(g, 20222, side_rows=4, back_rows=8, ring_row=1)
    for x in (1, 3, 4, 6):
        hat.top.vline(x, 0, 7, "H1" if x in (3, 6) else "H3")
    knot = g.piece("knot", "HEAD", (-1.5, -1.5, -1.5), (3, 3, 3), pivot=(0, -7.6, 4.0), rotation=(-30, 0, 0))
    cel_box(knot, 20223)
    for f in knot.sides:
        f.hline(0, f.w - 1, 2, "K2")
    wave_lock(g, "knot_end", (0, -8.6, 4.6), (-150, 0, 0), [(((2, 2),), 0, 0), (((1, 2),), -50, 0)], depth=2, seed=20225)
