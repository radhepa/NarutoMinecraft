"""Shackled Arm: Danzo with the robe thrown off his right side: the off-white high-collared kosode,
the right arm bare to the shoulder and bound in bandages under three heavy shackle bands, and the
grey robe bunched round the waist and hanging behind to the knee."""
from kit import belt, collar, flaps
from kit_shimura import bandaged_arm
from paint import cap, fabric, solid, strip_fabric

META = {
    "name": "Shackled Arm",
    "gender": "unisex",
    "description": "Off-white high-collared kosode, a bandaged right arm under three shackles, the grey robe bunched at the waist.",
    "tags": ["shinobi", "robe"],
    "covers_waist": True,
}


def build(g):
    body = g.part("body")
    strip_fabric(body, "S", "weave", 13520, 2)
    cap(body, "S", seed=13520)
    f = body.front
    for y in range(8):
        f.set(min(7, 2 + y // 2), y, "S1")
    # The right side of the kosode is slipped off the shoulder: bandages show over the right breast.
    for y in range(3):
        for x in range(0, 2 - y // 2):
            f.set(x, y, "S3" if (x + y) % 3 else "S2")
    bandaged_arm(g, "right", shackles=(1.4, 4.2, 7.0))
    arm, sleeve = g.part("left_arm"), g.part("left_sleeve")
    strip_fabric(arm, "S", "weave", 13521, 2, 0, 9)
    fabric(arm.top, "S", "weave", 13521, 3)
    strip_fabric(sleeve, "S", "weave", 13522, 2, 0, 8)
    fabric(sleeve.top, "S", "weave", 13522, 3)
    sleeve.strip.hline(0, sleeve.strip.w - 1, 8, "S1")
    neck = collar(g, "collar", "S", "weave", height=2, y=-1.7, inflate=.1)
    neck.front.vline(4, 0, 1, "S1")
    # The robe rolled round the waist, a loose fold on the right hip, its length hanging behind.
    roll = belt(g, "robe_roll", y=8.2, role="P", height=3, buckle=None, inflate=.2)
    for face in roll.sides:
        face.hline(0, face.w - 1, 1, "P1")
    fold = g.piece("robe_fold", "TORSO", (-1.5, 0, -1), (3, 5, 2), pivot=(-3.2, 10.0, -2.2), rotation=(0, 0, 8), motion="flap_front")
    solid(fold, "P", "twill", 13523, 2)
    fold.front.vline(1, 1, 4, "P1")
    back = g.piece("robe_back", "TORSO", (-4.5, 0, 0), (9, 9, 1), pivot=(0, 10.6, 2.0), motion="flap_back")
    solid(back, "P", "twill", 13524, 2)
    for x in (2, 4, 6):
        back.back.vline(x, 1, 8, "P1")
    flaps(g, "kosode", 3, "S", "weave", 13525, width=9, top=10.8, front_z=-2.8, back_z=1.8)
