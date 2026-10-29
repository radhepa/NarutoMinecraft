"""Clan Tunic: the long high-collared tunic of the Uchiha quarter, short sleeves trimmed in white,
a slim red sash, the skirt split at the sides to mid-thigh and the crest on the back."""
from kit import arm_bone, arm_x, belt, flaps
from kit_uchiha import back_crest, high_collar
from paint import cap, fabric, solid, strip_fabric

META = {
    "name": "Clan Tunic",
    "gender": "unisex",
    "description": "Long high-collared tunic, white-trimmed short sleeves, red sash, side-split skirt, crest on the back.",
    "tags": ["shinobi", "uchiha", "tunic"],
    "covers_waist": True,
}


def build(g):
    body = g.part("body")
    strip_fabric(body, "P", "weave", 3860, 2)
    cap(body, "P", seed=3860)
    f = body.front
    f.vline(2, 1, 7, "P1"), f.vline(5, 1, 7, "P1")
    f.set(3, 0, "S3"), f.set(4, 0, "S3")
    back_crest(g, "P", seed=3861)
    high_collar(g, "P", seed=3862, height=3, flare=4, trim="S3")
    belt(g, "sash", y=8.4, role="A", height=1, buckle=None, inflate=.1)
    for face in flaps(g, "tunic", 5, "P", "weave", 3864, width=9, hem="S3", top=10.6, front_z=-2.7, back_z=1.7):
        face.vline(0, 1, 4, "P1"), face.vline(8, 1, 4, "P1")
    for side in ("right", "left"):
        arm, sleeve = g.part(f"{side}_arm"), g.part(f"{side}_sleeve")
        strip_fabric(arm, "P", "weave", 3866, 2, 0, 3)
        fabric(arm.top, "P", "weave", 3866, 3)
        strip_fabric(sleeve, "P", "weave", 3867, 2, 0, 3)
        fabric(sleeve.top, "P", "weave", 3867, 3)
        trim = g.piece(f"{side}_sleeve_trim", arm_bone(side), (arm_x(side) - .4, 1.6, -2.4), (4, 1, 4), inflate=.15)
        solid(trim, "S", "weave", 3868, 3)
