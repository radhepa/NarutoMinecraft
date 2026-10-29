"""Side-Parted Long: long straight hair parted well off-centre, a heavy swept fringe falling over
one brow to the temple, one long lock in front of the shoulder and the length down the back."""
from anime import bangs, lock
from kit_hyuga import back_sheet, crown, ear_panels

META = {"name": "Side-Parted Long", "gender": "unisex",
        "description": "Off-centre part, a swept fringe over one brow, one long front lock, long back."}


def build(g):
    crown(g, 4201, side_rows=7, back_rows=8, sideburn=2, part=5)
    back_sheet(g, "length", 12, 4205, tilt=-5)
    ear_panels(g, "side", 8, 4210, z0=-2.5, depth=7)
    bangs(g, "sweep", [(1.4, ((3, 1), (2, 1)), 48), (-.4, ((3, 2), (2, 1)), 44), (-2.4, ((2, 2), (2, 1), (1, 1)), 34),
                       (2.9, ((2, 1), (1, 1)), -20)], seed=4215)
    lock(g, "front_lock", (-4.3, -7.6, -3.5), (0, 0, 3), ((2, 9), (2, 3), (1, 2)), 1, 4220, ring=1)
    lock(g, "temple_lock", (4.3, -7.6, -3.4), (0, 0, -2), ((1, 6), (1, 1)), 1, 4225, ring=1)
