"""Thorn Braids: two loose braids brought forward over the shoulders, each tied off a hand's width
from the end so a wavy tuft springs free, under a soft parted fringe of waves."""
from anime import bangs, braid, tie
from kit_yuhi import wave_box, wave_lock, wave_shell
from paint import scalp

META = {"name": "Thorn Braids", "gender": "unisex",
        "description": "Two braids forward over the shoulders ending in wavy tufts, soft parted fringe."}


def build(g):
    scalp(g, 14441, side_rows=7, back_rows=8, sideburn=1, part=4)
    wave_shell(g, 14442, side_rows=7, back_rows=8, ring_row=1)
    bangs(g, "fringe", [(-2.8, ((2, 2), (1, 1)), 18), (-1.3, ((2, 1), (1, 1)), 30), (1.3, ((2, 1), (1, 1)), -30),
                        (2.8, ((2, 2), (1, 1)), -18)], seed=14450)
    for side, sign in (("right", -1), ("left", 1)):
        pivot, rot = (4.3 * sign, -4.6, -.6), (-14, 0, -6 * sign)
        root = g.piece(f"root_{side}", "HEAD", (-1.5, -3, -1.5), (3, 3, 3), pivot=pivot, rotation=rot)
        wave_box(root, 14455 + (sign > 0), ring=0)
        end = braid(g, f"braid_{side}", pivot, rot, links=4, width=3, seed=14460 + (sign > 0) * 9, motion="sway")
        tie(g, f"tie_{side}", pivot, rot, size=(2, 1, 2), y=end - 1.5, key="A2", motion="sway")
        wave_lock(g, f"tuft_{side}", pivot, rot, ((2, 2), (2, 1), (1, 1)), 2, 14470 + (sign > 0), ring=None, motion="sway",
                  amp=.4, y0=end - .5)
