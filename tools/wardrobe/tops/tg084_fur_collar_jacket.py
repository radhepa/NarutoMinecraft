"""Fur-Collar Jacket: a long-sleeved hip-length jacket of heavy twill closed with leather toggles, a
deep collar of shaggy fur round the neck, fur-cuffed wrists and a darned patch on the left elbow:
for the shinobi posted to the northern passes."""
from kit import arm_bone, arm_x, sleeves
from kit_rugged import patch, shag_box
from paint import fabric, solid, strip_fabric

META = {
    "name": "Fur-Collar Jacket",
    "gender": "unisex",
    "description": "Hip-length twill jacket with leather toggles, a shaggy fur collar, fur cuffs and an elbow patch.",
    "tags": ["shinobi", "jacket", "jonin"],
    "covers_waist": True,
}


def build(g):
    body, jacket = g.part("body"), g.part("jacket")
    strip_fabric(body, "P", "twill", 35040, 2)
    fabric(body.top, "P", "twill", 35040, 3)
    strip_fabric(jacket, "P", "twill", 35041, 2, 1, 11)
    f = jacket.front
    f.vline(4, 1, 11, "P0"), f.vline(3, 1, 11, "P3")
    for y in (3, 6, 9):
        f.set(3, y, "L3"), f.set(4, y, "L1"), f.set(5, y, "L2")
    jacket.strip.hline(0, jacket.strip.w - 1, 11, "P1")
    jacket.strip.hline(0, jacket.strip.w - 1, 10, "P3")
    sleeves(g, "P", "twill", 35042, 2, rows=(0, 9))
    for side in ("right", "left"):
        arm = g.part(f"{side}_arm")
        fabric(arm.bottom, "P", "twill", 35042, 1)
    patch(g.part("left_arm").left, 1, 3, 3, 3, "L", 35043)
    collar = g.piece("fur_collar", "TORSO", (-5, -1.4, -3), (10, 3, 6), inflate=.05)
    shag_box(collar, "S", 35044, 2)
    for side in ("right", "left"):
        cuff = g.piece(f"{side}_fur_cuff", arm_bone(side), (arm_x(side) - .5, 7.4, -2.5), (5, 2, 5))
        shag_box(cuff, "S", 35045 + (side == "left"), 2)
    pocket = g.piece("chest_pocket", "TORSO", (0, 0, 0), (2, 2, 1), pivot=(1.0, 3.0, -2.75))
    solid(pocket, "P", "twill", 35047, 2)
    pocket.front.hline(0, 1, 0, "P3")
