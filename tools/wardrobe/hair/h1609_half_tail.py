"""Half Tail: the top section caught up in a small tail at the back of the crown, the rest left
loose to the collar with the ends flicking out, parted locks framing the face."""
from anime import bangs, curtain, lock, ring_shell, sidelocks, tie
from kit_shiranui import flicks
from paint import scalp

META = {"name": "Half Tail", "gender": "unisex",
        "description": "Top section tied in a small crown tail, the rest loose to the collar, flicked ends."}


def build(g):
    scalp(g, 16480, side_rows=7, back_rows=8, sideburn=1, part=4)
    ring_shell(g, 16481, side_rows=7, back_rows=8, ring_row=1)
    bangs(g, "fringe", [(-2.9, ((2, 3), (1, 1)), 16), (-1.2, ((2, 2),), 24), (1.4, ((2, 2),), -26),
                        (3.0, ((2, 3), (1, 1)), -16)], seed=16482)
    sidelocks(g, "frame", 6, seed=16490, x=4.3, z=-3.0, flare=4, width=2)
    curtain(g, "fall", (0, -6.4, 4.6), (-4, 0, 0), 9, 6, hem=[(0, 3, 1), (3, 3, 2), (6, 3, 1)], seed=16500)
    flicks(g, "flick", -1.4, 16505, x=4.5, z=-2.4, segments=((2, 2), (1, 1)))
    lock(g, "crown_tail", (0, -7.2, 4.5), (34, 0, 0), ((2, 2), (2, 2), (1, 2)), 2, 16510, ring=0, motion="sway")
    tie(g, "crown_tie", (0, -7.2, 4.5), (34, 0, 0), size=(3, 1, 3), y=0, key="D2")
