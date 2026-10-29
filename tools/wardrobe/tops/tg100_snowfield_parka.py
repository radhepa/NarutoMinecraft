"""Snowfield Parka: a thick hip-length pullover parka with a fur-rimmed hood thrown back, a kangaroo
pocket across the belly, toggled at the throat and edged in fur at the cuffs: for the long watches
on the northern border."""
from kit import arm_bone, arm_x, sleeves
from kit_rugged import shag_box
from paint import fabric, solid, strip_fabric

META = {
    "name": "Snowfield Parka",
    "gender": "unisex",
    "description": "Thick pullover parka with a fur-rimmed hood thrown back, a belly pocket, toggles and fur cuffs.",
    "tags": ["shinobi", "coat", "jonin"],
    "covers_waist": True,
}


def build(g):
    body, jacket = g.part("body"), g.part("jacket")
    strip_fabric(body, "P", "twill", 35200, 2)
    fabric(body.top, "P", "twill", 35200, 3)
    strip_fabric(jacket, "P", "twill", 35201, 2, 0, 11)
    fabric(jacket.top, "P", "twill", 35201, 3)
    for face in jacket.sides:
        face.hline(0, face.w - 1, 11, "P1")
        face.hline(0, face.w - 1, 10, "P3")
    f = jacket.front
    for y in (1, 3):
        f.set(3, y, "L3"), f.set(4, y, "L1")
    f.vline(4, 0, 4, "P1")
    sleeves(g, "P", "twill", 35202, 2, rows=(0, 9))
    pocket = g.piece("belly_pocket", "TORSO", (-3, 0, 0), (6, 3, 1), pivot=(0, 6.6, -2.75))
    solid(pocket, "P", "twill", 35203, 2)
    pocket.front.vline(0, 0, 2, "P0"), pocket.front.vline(5, 0, 2, "P0"), pocket.front.hline(0, 5, 0, "P3")
    for side in ("right", "left"):
        cuff = g.piece(f"{side}_fur_cuff", arm_bone(side), (arm_x(side) - .5, 7.4, -2.5), (5, 2, 5))
        shag_box(cuff, "S", 35204 + (side == "left"), 2)
        arm = g.part(f"{side}_arm")
        fabric(arm.bottom, "P", "twill", 35202, 1)
    hood = g.piece("hood", "TORSO", (-4, 0, 0), (8, 5, 3), pivot=(0, -2.4, 2.8), rotation=(-14, 0, 0))
    solid(hood, "P", "twill", 35206, 2)
    hood.front.fill("P0")
    rim = g.piece("hood_fur", "TORSO", (-4.5, 0, 0), (9, 2, 4), pivot=(0, -3.0, 2.4), rotation=(-14, 0, 0))
    shag_box(rim, "S", 35207, 2)
