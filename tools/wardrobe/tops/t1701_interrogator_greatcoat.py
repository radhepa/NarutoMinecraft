"""Interrogator Greatcoat: Ibiki Morino's long black greatcoat worn open to the shin over the slate
uniform, a stiff standing collar, oxblood lining showing down the opening and heavy turned cuffs."""
from kit import arm_x, collar
from kit_morino import coat_skirts
from paint import cap, fabric, solid, strip_fabric

META = {
    "name": "Interrogator Greatcoat",
    "gender": "unisex",
    "description": "Long black greatcoat open to the shin over the slate uniform, standing collar, oxblood lining.",
    "tags": ["shinobi", "coat", "jonin"],
    "covers_waist": True,
}


def build(g):
    body, jacket = g.part("body"), g.part("jacket")
    strip_fabric(body, "S", "weave", 17201, 2)
    cap(body, "S", seed=17201)
    body.front.vline(3, 0, 11, "S1")
    body.strip.hline(0, body.strip.w - 1, 9, "K1")
    strip_fabric(jacket, "P", "twill", 17202, 2)
    cap(jacket, "P", texture="twill", seed=17202)
    # Worn open: the slate uniform shows between oxblood-lined fronts.
    for y in range(12):
        for x in (3, 4):
            jacket.front.clear(x, y)
        jacket.front.set(2, y, "A1"), jacket.front.set(5, y, "A1")
        jacket.front.set(1, y, "P1"), jacket.front.set(6, y, "P3")
    for side, bone in (("right", "RIGHT_ARM"), ("left", "LEFT_ARM")):
        arm, sleeve = g.part(f"{side}_arm"), g.part(f"{side}_sleeve")
        strip_fabric(arm, "P", "twill", 17203 + (side == "left"), 2, 0, 11)
        fabric(arm.top, "P", "twill", 17203, 3)
        strip_fabric(sleeve, "P", "twill", 17205, 2, 0, 8)
        fabric(sleeve.top, "P", "twill", 17205, 3)
        cuff = g.piece(f"{side}_cuff", bone, (arm_x(side) - .4, 8.4, -2.4), (5, 2, 5), inflate=.1)
        solid(cuff, "P", "twill", 17206, 1)
        for face in cuff.sides:
            face.hline(0, face.w - 1, 0, "P3")
    neck = collar(g, "collar", "P", "twill", height=3, y=-2.4, inflate=.12)
    neck.front.vline(4, 0, 2, "A1"), neck.front.vline(3, 0, 2, "A1")
    for face in (neck.right, neck.left, neck.back):
        face.hline(0, face.w - 1, 2, "P1")
    coat_skirts(g, "skirt", 9, "P", 17210, lining="A1", hem="P0")
