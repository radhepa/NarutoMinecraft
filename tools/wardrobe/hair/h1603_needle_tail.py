"""Needle Tail: straight hair drawn back into a low ponytail at the nape, the tie skewered with a
senbon, a short parted fringe and loose locks left framing the face."""
from anime import bangs, lock, ring_shell, sidelocks, tie
from kit_shiranui import senbon
from paint import scalp

META = {"name": "Needle Tail", "gender": "unisex",
        "description": "Low ponytail at the nape skewered with a senbon, a short parted fringe, loose frame locks."}


def build(g):
    scalp(g, 16220, side_rows=5, back_rows=8, sideburn=2, part=3)
    ring_shell(g, 16221, side_rows=4, back_rows=7, ring_row=1)
    bangs(g, "fringe", [(-2.8, ((2, 2), (1, 1)), 22), (-1.2, ((2, 2),), 30), (1.2, ((2, 2),), -30),
                        (2.8, ((2, 2), (1, 1)), -22)], seed=16222)
    sidelocks(g, "frame", 6, seed=16230, x=4.3, z=-3.0, flare=4, width=1)
    lock(g, "tail", (0, -2.8, 4.7), (16, 0, 0), ((3, 3), (3, 3), (2, 3), (1, 2)), 2, 16240, ring=0, motion="sway")
    tie(g, "tail_tie", (0, -2.8, 4.7), (16, 0, 0), size=(4, 1, 3), y=.2, key="D1")
    senbon(g, "tail_pin", "HEAD", (-2.2, -3.4, 6.4), (0, 0, -58), length=16)
