"""Drooping Bells: short hair at the back and two long locks in front of the ears, each bound near
its end with a white cord so the tip flares out like a hanging bell, and a short fringe parted off
centre."""
from anime import bangs, cel_box, lock, ring_shell
from paint import scalp

META = {"name": "Drooping Bells", "gender": "unisex",
        "description": "Short at the back, two long front locks bound near the tips so they flare like bells."}


def build(g):
    scalp(g, 24051, side_rows=5, back_rows=6, sideburn=2, part=5)
    ring_shell(g, 24052, side_rows=4, back_rows=6, ring_row=1)
    bangs(g, "fringe", [(-2.8, ((2, 2), (1, 1)), 18), (-.9, ((3, 2), (1, 1)), 26), (1.3, ((2, 2), (1, 1)), 24),
                        (3.0, ((2, 2),), -8)], seed=24055)
    for side, sign in (("right", -1), ("left", 1)):
        x = 4.35 * sign
        lock(g, f"lock_{side}", (x, -7.6, -3.0), (0, 0, -2 * sign), ((2, 5),), 1, 24060 + (sign > 0), ring=1)
        band = g.piece(f"band_{side}", "HEAD", (-1, 5, -.5), (2, 1, 1), pivot=(x, -7.6, -3.0), rotation=(0, 0, -2 * sign),
                       inflate=.12)
        for f in band.faces:
            f.fill("S4")
        flare = g.piece(f"flare_{side}", "HEAD", (-1.5, 6, -1), (3, 2, 2), pivot=(x, -7.6, -3.0), rotation=(0, 0, -2 * sign))
        cel_box(flare, 24064 + (sign > 0), top_delta=0)
    nape = g.piece("nape", "HEAD", (-4, 0, -.5), (8, 2, 1), pivot=(0, -2.0, 4.4))
    cel_box(nape, 24068, top_delta=0)
