"""Easel Shag: a tousled, layered cut to the nape that looks slept-in at the easel, choppy locks
flicking out at the sides and back and a long fringe swept to one side."""
from anime import back_fan, ring_shell, sidelocks
from kit_kurama import part_line, side_fringe
from paint import scalp

META = {"name": "Easel Shag", "gender": "unisex",
        "description": "Tousled layers to the nape, choppy flicks at the sides and back, a swept fringe."}

S2 = ((2, 3), (1, 2))
S3 = ((3, 3), (2, 2), (1, 1))
BACK = [(-3.4, S2, 20, 10), (-1.8, S3, 8, 6), (0, S3, 0, 8), (1.8, S3, -8, 6), (3.4, S2, -20, 10),
        (-2.4, S2, 12, 22), (.2, S2, 0, 24), (2.6, S2, -12, 22)]


def build(g):
    scalp(g, 12420, side_rows=6, back_rows=8, sideburn=3, part=5)
    ring_shell(g, 12421, side_rows=5, back_rows=7, ring_row=1)
    part_line(g, 5)
    back_fan(g, "layer", BACK, seed=12424)
    sidelocks(g, "flick", 6, seed=12470, x=4.4, z=-2.4, flare=9, width=2)
    sidelocks(g, "flick_back", 5, seed=12480, x=4.4, z=.8, flare=14, width=2)
    side_fringe(g, "fringe", 12490, side=-1)
