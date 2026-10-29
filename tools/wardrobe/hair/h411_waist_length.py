"""Waist-Length: the younger heiress's grown-out hair, straight and unbroken to the waist, parted
in the middle with long sidelocks falling to the collarbone and the forehead left open."""
from anime import sidelocks
from kit_hyuga import back_sheet, crown, ear_panels, parted_fringe

META = {"name": "Waist-Length", "gender": "unisex",
        "description": "Unbroken straight hair to the waist, middle part, sidelocks to the collarbone."}


def build(g):
    crown(g, 4441, side_rows=7, back_rows=8, sideburn=2, part=3)
    back_sheet(g, "length", 16, 4445, hem=[(0, 3, 1), (3, 3, 2), (6, 3, 1)], tilt=-4, pivot=(0, -6.0, 4.75))
    ear_panels(g, "side", 9, 4450, z0=-2.5, depth=7)
    sidelocks(g, "frame", 10, seed=4455, x=4.2, z=-3.6, flare=1, width=2, taper=False)
    parted_fringe(g, "fringe", 4460, reach=1)
