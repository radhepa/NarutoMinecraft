"""Hashirama Mane: the First's long straight mane, dark and heavy to the middle of the back, a fringe
parted just off centre that stops at the brows, and long locks over the ears falling past the jaw."""
from anime import bangs, curtain, ring_shell, sidelocks
from kit_senju import side_panels
from paint import scalp

META = {"name": "Hashirama Mane", "gender": "unisex",
        "description": "Long straight mane to mid-back, off-centre parted fringe, long locks past the jaw."}


def build(g):
    scalp(g, 1000, side_rows=7, back_rows=8, sideburn=4, part=3)
    ring_shell(g, 1001, side_rows=7, back_rows=8, ring_row=1)
    curtain(g, "curtain", (0, -6.2, 4.7), (-6, 0, 0), 9, 15, hem=[(0, 3, 3), (3, 3, 2), (6, 3, 3)], seed=1005)
    side_panels(g, "side", 10, 1010)
    bangs(g, "fringe", [(-2.8, ((2, 2), (1, 1)), 14), (-1.0, ((2, 2), (1, 1)), 22),
                        (1.6, ((2, 2), (1, 1)), -24), (3.0, ((2, 2), (1, 1)), -12)], seed=1015)
    sidelocks(g, "frame", 11, seed=1020, x=4.3, z=-3.5, flare=3, width=2)
