"""Shoulder Tail: the hair gathered low behind the left ear and brought forward over the shoulder in
a long tail, tied with a strip of painted cloth. A side part sweeps the fringe the other way."""
from anime import cel_box, lock, ring_shell, tie
from kit_kurama import part_line, side_fringe
from paint import scalp

META = {"name": "Shoulder Tail", "gender": "unisex",
        "description": "A low tail gathered behind the left ear, over the shoulder, tied with a cloth strip."}


def build(g):
    scalp(g, 12240, side_rows=7, back_rows=8, sideburn=2, part=5)
    ring_shell(g, 12241, side_rows=6, back_rows=8, ring_row=1)
    part_line(g, 5)
    # The length gathered behind the left ear.
    gather = g.piece("gather", "HEAD", (3.8, -3.0, -2.4), (1, 3, 6))
    cel_box(gather, 12246, ring=0)
    tie(g, "cloth", (4.1, .2, -2.8), size=(2, 1, 2), key="A2")
    lock(g, "tail", (4.1, .6, -2.8), (0, 0, -3), ((3, 4), (3, 3), (2, 3), (1, 2)), 2, 12250, ring=None, motion="sway")
    lock(g, "lock_right", (-4.35, -7.4, -3.0), (0, 0, 4), ((2, 5), (1, 2)), 1, 12256)
    side_fringe(g, "fringe", 12260, side=-1)
