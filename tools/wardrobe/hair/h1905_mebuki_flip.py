"""Mebuki Flip: the Haruno mother's hair, cut to the jaw with lifted volume at the crown, a deep side
fringe swept across the brow, and the ends flicked outward at both cheeks."""
from anime import cel_box, lock, ring_shell
from paint import scalp

META = {"name": "Mebuki Flip", "gender": "unisex",
        "description": "Jaw-length hair with crown volume, deep side fringe, ends flicked outward at the cheeks."}

SWEEP = [(-2.9, ((2, 2), (1, 1)), -16), (-1.4, ((3, 2), (2, 1)), -60), (.4, ((3, 2), (2, 1)), -62), (2.3, ((3, 2), (2, 1)), -48)]


def build(g):
    scalp(g, 19121, side_rows=7, back_rows=8, sideburn=0, part=2)
    ring_shell(g, 19122, side_rows=7, back_rows=8, ring_row=1)
    lift = g.piece("crown_lift", "HEAD", (-4, -1, -3.5), (8, 1, 7), pivot=(0, -8.2, .6), inflate=.3)
    cel_box(lift, 19123, base=3)
    for i, (x, segs, rz) in enumerate(SWEEP):
        lock(g, f"sweep_{i}", (x, -8.55, -4.35), (-10, 0, rz), segs, 1, 19125 + i * 7, ring=0)
    for side, sign in (("right", -1), ("left", 1)):
        panel = g.piece(f"side_{side}", "HEAD", (-.5, 0, -3.5), (1, 6, 7), pivot=(4.6 * sign, -8, .3))
        cel_box(panel, 19135 + (sign > 0), ring=1)
        flick = g.piece(f"flick_{side}", "HEAD", (-.5, 0, -3), (1, 3, 6), pivot=(4.6 * sign, -2.2, .3), rotation=(0, 0, -40 * sign))
        cel_box(flick, 19137 + (sign > 0), top_delta=0)
    back = g.piece("back", "HEAD", (-4.5, 0, -.5), (9, 6, 1), pivot=(0, -7.6, 4.6))
    cel_box(back, 19139, ring=1)
    flare = g.piece("back_flick", "HEAD", (-4.5, 0, -.5), (9, 3, 1), pivot=(0, -1.8, 4.6), rotation=(40, 0, 0))
    cel_box(flare, 19140, top_delta=0)
