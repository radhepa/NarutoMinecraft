"""Fur Trapper Cap: a round cap of quilted cloth with a thick shaggy fur brim and fur ear flaps
hanging down beside the cheeks; hides the hair beneath."""
from kit_rugged import shag_box
from paint import fabric, solid

META = {"name": "Fur Trapper Cap", "gender": "unisex", "hides_hair": ["*"],
        "description": "Quilted round cap with a thick shaggy fur brim and fur ear flaps beside the cheeks."}


def build(g):
    crown = g.piece("cap_crown", "HEAD", (-4, -9, -4), (8, 3, 8), inflate=.65)
    solid(crown, "P", "quilt", 35890, 2, edge=False)
    fabric(crown.top, "P", "quilt", 35890, 3)
    brim = g.piece("cap_brim", "HEAD", (-5, -7.2, -5), (10, 2, 10))
    shag_box(brim, "L", 35891, 3)
    for side, x in (("right", -5.0), ("left", 4.0)):
        flap = g.piece(f"ear_flap_{side}", "HEAD", (0, 0, -2), (1, 5, 4), pivot=(x, -4.8, .4))
        shag_box(flap, "L", 35892 + (side == "left"), 3)
    back = g.piece("cap_back_flap", "HEAD", (-4, 0, 0), (8, 3, 1), pivot=(0, -4.8, 4.0))
    shag_box(back, "L", 35894, 3)
