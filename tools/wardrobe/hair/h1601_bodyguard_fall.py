"""Bodyguard Fall: Genma Shiranui's straight light-brown hair, parted in the middle and falling to
the jaw from under the backward bandana, long face-framing locks whose ends flick out at the chin
and a collar-length fall at the back that kicks up at the nape."""
from anime import bangs, curtain, ring_shell, sidelocks
from kit_shiranui import flicks
from paint import scalp

META = {"name": "Bodyguard Fall", "gender": "unisex",
        "description": "Straight jaw-length hair parted in the middle, frame locks flicking out at the chin."}


def build(g):
    scalp(g, 16140, side_rows=7, back_rows=8, sideburn=1, part=3)
    ring_shell(g, 16141, side_rows=7, back_rows=8, ring_row=1)
    bangs(g, "fringe", [(-2.9, ((2, 3), (1, 1)), 20), (-1.3, ((2, 2), (1, 1)), 28), (1.3, ((2, 2), (1, 1)), -28),
                        (2.9, ((2, 3), (1, 1)), -20)], seed=16142)
    sidelocks(g, "frame", 7, seed=16150, x=4.3, z=-3.0, flare=3, width=2)
    flicks(g, "flick", -1.4, 16160, x=4.5, z=-3.0)
    curtain(g, "fall", (0, -6.6, 4.6), (-4, 0, 0), 9, 6, hem=[(0, 3, 2), (3, 3, 1), (6, 3, 2)], seed=16170)
    flicks(g, "nape_flick", -.8, 16175, x=3.6, z=4.3, back=True)
