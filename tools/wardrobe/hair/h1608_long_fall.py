"""Long Fall: straight light-brown hair grown long and left loose, parted in the middle, long locks
over the shoulders at the front and a smooth sheet down the back to a pointed hem."""
from anime import bangs, curtain, ring_shell, sidelocks
from paint import scalp

META = {"name": "Long Fall", "gender": "unisex",
        "description": "Long straight hair parted in the middle, locks over the shoulders, a smooth sheet down the back."}


def build(g):
    scalp(g, 16440, side_rows=7, back_rows=8, sideburn=1, part=3)
    ring_shell(g, 16441, side_rows=7, back_rows=8, ring_row=1)
    bangs(g, "fringe", [(-2.9, ((2, 3), (1, 1)), 22), (-1.3, ((2, 2),), 30), (1.3, ((2, 2),), -30),
                        (2.9, ((2, 3), (1, 1)), -22)], seed=16442)
    sidelocks(g, "frame", 11, seed=16450, x=4.3, z=-3.0, flare=4, width=2)
    curtain(g, "fall", (0, -6.6, 4.6), (-6, 0, 0), 9, 13, hem=[(0, 3, 2), (3, 3, 3), (6, 3, 2)], seed=16460)
