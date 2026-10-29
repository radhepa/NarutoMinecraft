"""Hime Cut: the heiress's cut, straight and heavy: a blunt fringe to the brows, square locks cut
level beside the jaw, and the length falling in one smooth sheet to the middle of the back."""
from kit_hyuga import back_sheet, blunt_fringe, crown, ear_panels, hime_locks

META = {"name": "Hime Cut", "gender": "female",
        "description": "Blunt fringe, jaw-length square side locks, a smooth sheet to mid-back."}


def build(g):
    crown(g, 4081, side_rows=7, back_rows=8, sideburn=2)
    back_sheet(g, "length", 13, 4085, hem=[(0, 9, 1)], tilt=-5)
    ear_panels(g, "side", 9, 4090, z0=-2.5, depth=7)
    hime_locks(g, "hime", 8, 4095, x=4.2, z=-3.5, width=2, flare=0)
    blunt_fringe(g, "fringe", 4100, length=3, tips=False)
