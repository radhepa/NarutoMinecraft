"""Long Shag: a heavy untamed curtain of hair to the middle of the back, the hem torn into points,
rough locks jutting out at the shoulders and a jagged fringe, worn loose for the hunt."""
from anime import bangs, curtain, lock, ring_shell, sidelocks
from kit_inuzuka import burst
from paint import scalp

META = {"name": "Long Shag", "gender": "unisex",
        "description": "A heavy loose curtain to mid-back with a torn hem, locks jutting at the shoulders."}

TOP = ((3, 2), (2, 2), (1, 1))
CROWN = [(-2.2, -1.6, TOP, 6, -30), (.4, -2.0, TOP, 10, 6), (2.4, -1.4, TOP, 4, 30), (-1.2, 1.2, TOP, -34, -18),
         (1.4, 1.4, TOP, -34, 18)]


def build(g):
    scalp(g, 8360, side_rows=8, back_rows=8, sideburn=0)
    ring_shell(g, 8361, side_rows=8, back_rows=8, ring_row=1)
    burst(g, "crown_tuft", CROWN, 8363)
    curtain(g, "length", (0, -7.6, 4.6), (8, 0, 0), 8, 13, hem=((0, 2, 3), (2, 2, 2), (4, 2, 4), (6, 2, 2)), seed=8370)
    for i, (x, rz) in enumerate(((-3.8, 12), (3.8, -12))):
        lock(g, f"flare_{i}", (x, -3.0, 3.0), (24, 0, rz), ((2, 4), (2, 2), (1, 2)), 2, 8375 + i, motion="sway")
    bangs(g, "fringe", [(-2.8, ((2, 3), (1, 1)), 18), (-1.2, ((2, 2), (1, 1)), 12), (.4, ((2, 2), (1, 1)), -4),
                        (2.0, ((2, 2), (1, 1)), -14)], seed=8378)
    sidelocks(g, "frame", 10, seed=8382, x=4.35, z=-3.4, flare=5, width=2)
    sidelocks(g, "sidelock", 9, seed=8385, x=4.5, z=-.2, flare=12, width=3)
