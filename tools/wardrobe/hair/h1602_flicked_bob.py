"""Flicked Bob: a smooth chin-length bob with the fringe swept off to one side and every end kicked
outward, the easy, unbothered cut of a family that never looks hurried."""
from anime import bangs, curtain, ring_shell
from kit_senju import side_panels
from kit_shiranui import flicks
from paint import scalp

META = {"name": "Flicked Bob", "gender": "unisex",
        "description": "Smooth chin-length bob, fringe swept to one side, the ends kicked outward."}


def build(g):
    scalp(g, 16180, side_rows=7, back_rows=8, sideburn=1, part=5)
    ring_shell(g, 16181, side_rows=7, back_rows=8, ring_row=1)
    side_panels(g, "frame", 6, 16182, top=-7.2, x=4.6, z0=-3, depth=7)
    flicks(g, "flick", -1.4, 16185, x=4.6, z=-2.6, segments=((2, 2), (1, 1)), splay=30)
    curtain(g, "fall", (0, -6.6, 4.6), (-3, 0, 0), 9, 6, seed=16190)
    flicks(g, "nape_flick", -.6, 16195, x=3.7, z=4.4, segments=((3, 2), (2, 1)), splay=30, back=True)
    bangs(g, "fringe", [(-3.0, ((2, 3), (1, 1)), 30), (-1.4, ((2, 2), (1, 1)), 36), (0.3, ((2, 2), (1, 1)), 40),
                        (2.0, ((2, 2),), 24), (3.2, ((2, 3),), -4)], seed=16200)
