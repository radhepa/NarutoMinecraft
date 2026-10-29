"""Side Sweep: short at the nape and over one ear, the longer top swept across to the other side and
falling in a long lock down the side of the face, outside the eye, to the jaw."""
from anime import bangs, lock, ring_shell, spike
from paint import scalp

META = {"name": "Side Sweep", "gender": "unisex",
        "description": "Short nape and one short side, the long top swept across into a jaw-length side lock."}

MID = ((3, 2), (2, 2), (1, 1))


def build(g):
    scalp(g, 25200, side_rows=4, back_rows=7, sideburn=1)
    ring_shell(g, 25201, side_rows=4, back_rows=6, ring_row=1)
    for i, (x, z, rx, rz) in enumerate(((-2.6, -2.2, 10, 64), (-.4, -1.6, 14, 58), (1.8, -1.0, 16, 50),
                                        (-1.6, 1.2, 30, 48), (1.0, 1.6, 34, 40))):
        spike(g, f"sweep_{i}", (x, -7.7, z), (rx, 0, rz), MID, 3, 25202 + i)
    bangs(g, "fringe", [(-1.6, ((3, 1), (2, 1)), 52), (.6, ((3, 2), (2, 1)), 48), (2.4, ((2, 2), (1, 1)), 30)],
          seed=25208)
    lock(g, "side_lock", (4.5, -7.8, -3.4), (0, 0, -4), ((3, 5), (2, 2), (1, 1)), 2, 25212, ring=1, motion="sway")
