"""Wing Sweep: long straight hair worn loose, a deep side part sweeping a long lock down past the
right cheek and the length falling down the back in a pointed sheet: the clan's open-faced look."""
from anime import bangs, curtain, lock, ring_shell
from paint import scalp

META = {"name": "Wing Sweep", "gender": "unisex",
        "description": "Long loose hair, a deep side part sweeping one lock past the cheek, a pointed back sheet."}


def build(g):
    scalp(g, 10461, side_rows=7, back_rows=8, sideburn=4, part=5)
    ring_shell(g, 10462, side_rows=7, back_rows=8, ring_row=1)
    curtain(g, "length", (0, -6.2, 4.6), (-6, 0, 0), 9, 11, hem=((0, 3, 3), (3, 3, 2), (6, 3, 3)), seed=10470)
    # The swept lock: from the part across the brow and down outside the right cheek.
    lock(g, "sweep", (-4.4, -8.0, -4.3), (-6, 0, 8), ((2, 4), (2, 4), (1, 3)), 1, 10480, ring=0)
    lock(g, "frame_left", (4.35, -7.6, -3.2), (0, 0, -4), ((2, 8), (1, 2)), 1, 10485, ring=1)
    bangs(g, "fringe", [(-2.2, ((3, 2), (2, 1)), 52), (.6, ((3, 1), (2, 1)), 64), (2.8, ((2, 2), (1, 1)), -10)],
          seed=10490)
