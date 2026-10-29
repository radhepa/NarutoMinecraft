"""Slicked Back: an older guard's hair combed straight back off the forehead and kept long at the
nape, falling smooth to the collar, a single loose lock dropped by one temple."""
from anime import curtain, lock, ring_shell
from kit_shiranui import flicks
from paint import scalp

META = {"name": "Slicked Back", "gender": "unisex",
        "description": "Combed straight back off the forehead, long and smooth at the nape, one loose temple lock."}


def build(g):
    scalp(g, 16680, side_rows=5, back_rows=8, sideburn=3)
    hat = ring_shell(g, 16681, side_rows=4, back_rows=8, ring_row=0)
    hat.front.hline(0, 7, 0, "H3")
    curtain(g, "fall", (0, -6.4, 4.6), (-5, 0, 0), 9, 7, hem=[(0, 3, 1), (3, 3, 2), (6, 3, 1)], seed=16700)
    flicks(g, "nape_flick", .4, 16705, x=3.6, z=5.0, segments=((2, 2), (1, 1)), splay=30, back=True)
    lock(g, "frame_loose", (3.9, -7.8, -3.4), (-6, 0, -10), ((1, 4), (1, 2)), 1, 16710, ring=1)
