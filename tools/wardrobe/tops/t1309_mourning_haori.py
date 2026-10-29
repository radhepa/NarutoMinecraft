"""Mourning Haori: the clan's formal black: a closed haori crossed over an off-white collar, wide
long sleeves, the crest in off-white on the back and on both breasts, falling to the knee: worn to
funerals and the council hall."""
from kit import arm_bone, arm_x, flaps
from kit_shimura import back_crest
from paint import cap, fabric, solid, strip_fabric

META = {
    "name": "Mourning Haori",
    "gender": "unisex",
    "description": "Closed black haori over an off-white collar, wide long sleeves, crests on the back and breasts, to the knee.",
    "tags": ["shinobi", "robe"],
    "covers_waist": True,
}


def build(g):
    body, jacket = g.part("body"), g.part("jacket")
    strip_fabric(body, "P", "velvet", 13660, 2)
    cap(body, "P", texture="velvet", seed=13660)
    strip_fabric(jacket, "P", "velvet", 13661, 2)
    cap(jacket, "P", texture="velvet", seed=13661)
    f = jacket.front
    # The off-white collar of the kimono beneath, crossed in a V at the throat.
    for x, y in ((2, 0), (3, 1), (5, 0), (4, 1), (3, 0), (4, 0)):
        f.set(x, y, "S3")
    f.set(2, 1, "S2"), f.set(5, 1, "S2")
    for y in range(2, 11):
        f.set(4, y, "P1")
    for x in (1, 6):
        f.set(x, 2, "S3")   # the small breast crests
    f.vline(4, 4, 5, "S3")  # the white tassel of the tie cords
    for side in ("right", "left"):
        arm, sleeve = g.part(f"{side}_arm"), g.part(f"{side}_sleeve")
        strip_fabric(arm, "P", "velvet", 13662, 2, 0, 10)
        fabric(arm.top, "P", "velvet", 13662, 3)
        strip_fabric(sleeve, "P", "velvet", 13663 + (side == "left"), 2, 0, 9)
        fabric(sleeve.top, "P", "velvet", 13663, 3)
        bag = g.piece(f"{side}_sleeve_bag", arm_bone(side), (arm_x(side) - .3, 3.0, -.5), (5, 8, 3), inflate=.05)
        solid(bag, "P", "velvet", 13665 + (side == "left"), 2)
    for face in flaps(g, "haori", 8, "P", "velvet", 13667, width=9, top=11.0, front_z=-2.85, back_z=1.85, hem="P1"):
        face.vline(4, 1, 7, "P1")
    back_crest(g, "P", ink="S3", y=1.2, z=2.3, texture="velvet")
