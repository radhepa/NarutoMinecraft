"""Half-Up Tail: the top half of long straight hair drawn back from the face and tied in a short
tail at the back of the crown, the rest left loose to the shoulder blades, with soft side bangs."""
from anime import lock, sidelocks
from kit_hyuga import back_sheet, crown, ear_panels, hair_tie, parted_fringe

META = {"name": "Half-Up Tail", "gender": "unisex",
        "description": "Top half tied in a short tail at the crown, the rest loose to the shoulder blades."}


def build(g):
    crown(g, 4361, side_rows=7, back_rows=8, sideburn=2)
    back_sheet(g, "length", 10, 4365, tilt=-6)
    ear_panels(g, "side", 8, 4370, z0=-2.5, depth=7)
    parted_fringe(g, "fringe", 4375, reach=2, part=-.5)
    sidelocks(g, "frame", 7, seed=4380, x=4.3, z=-3.6, flare=2, width=1)
    pivot = (0, -6.4, 5.4)
    hair_tie(g, "tie", pivot, (0, 0, 0), (3, 2, 2), key="A2", y=-1.2)
    lock(g, "tail", pivot, (2, 0, 0), ((3, 2), (3, 3), (2, 2), (1, 1)), 2, 4385, ring=None, motion="sway", y0=1)
