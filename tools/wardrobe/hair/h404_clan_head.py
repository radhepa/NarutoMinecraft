"""Clan Head: the head of the main house's long hair, middle-parted and swept off the forehead,
two long locks falling to the chest and the length hanging straight past the shoulder blades."""
from anime import sidelocks
from kit_hyuga import back_sheet, crown, ear_panels, parted_fringe

META = {"name": "Clan Head", "gender": "unisex",
        "description": "Middle-parted, swept off the forehead, long locks to the chest, length past the shoulder blades."}


def build(g):
    crown(g, 4161, side_rows=7, back_rows=8, sideburn=1, part=3)
    back_sheet(g, "length", 11, 4165, tilt=-6)
    ear_panels(g, "side", 8, 4170, z0=-2, depth=6)
    sidelocks(g, "frame", 12, seed=4175, x=4.4, z=-3.4, flare=1, width=2)
    parted_fringe(g, "fringe", 4180, reach=1)
