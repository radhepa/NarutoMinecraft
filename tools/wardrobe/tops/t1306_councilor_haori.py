"""Councilor Haori: the Shimura adviser's dress: a charcoal haori worn open over an off-white
kosode crossed at the throat, a dark sash showing between the lapels, wide hanging sleeves, and
the clan crest in off-white across the back; the haori falls to mid-thigh."""
from kit import arm_bone, arm_x, belt, flaps
from kit_shimura import back_crest
from paint import cap, fabric, solid, strip_fabric

META = {
    "name": "Councilor Haori",
    "gender": "unisex",
    "description": "Open charcoal haori over an off-white kosode, a dark sash, wide hanging sleeves, the clan crest on the back.",
    "tags": ["shinobi", "robe"],
    "covers_waist": True,
}


def build(g):
    body, jacket = g.part("body"), g.part("jacket")
    strip_fabric(body, "S", "weave", 13600, 2)
    cap(body, "S", seed=13600)
    for y in range(6):
        body.front.set(min(7, 2 + y), y, "S1")
    strip_fabric(jacket, "P", "weave", 13601, 2)
    cap(jacket, "P", seed=13601)
    f = jacket.front
    for y in range(12):
        for x in range(2, 6):
            f.clear(x, y)
        f.set(1, y, "P3"), f.set(6, y, "P1")
    belt(g, "sash", y=8.0, role="D", height=2, buckle=None, inflate=.08)
    # The haori's tie cords across the open front.
    cord = g.piece("himo", "TORSO", (-1, 0, 0), (2, 1, 1), pivot=(0, 4.0, -2.95))
    solid(cord, "D", "weave", 13602, 3, edge=False)
    for side in ("right", "left"):
        arm, sleeve = g.part(f"{side}_arm"), g.part(f"{side}_sleeve")
        strip_fabric(arm, "P", "weave", 13604, 2, 0, 9)
        fabric(arm.top, "P", "weave", 13604, 3)
        arm.strip.hline(0, arm.strip.w - 1, 9, "S2")
        strip_fabric(sleeve, "P", "weave", 13605 + (side == "left"), 2, 0, 8)
        fabric(sleeve.top, "P", "weave", 13605, 3)
        # The hanging pocket of the sleeve below the forearm.
        bag = g.piece(f"{side}_sleeve_bag", arm_bone(side), (arm_x(side) - .3, 4.0, -.5), (5, 6, 3), inflate=.05)
        solid(bag, "P", "weave", 13607 + (side == "left"), 2)
        bag.strip.hline(0, bag.strip.w - 1, 5, "P1")
    for face in flaps(g, "haori", 5, "P", "weave", 13609, width=9, top=11.2, front_z=-2.85, back_z=1.85, hem="P1"):
        face.vline(4, 1, 4, "P1")
    back_crest(g, "P", ink="S3", y=1.6, z=2.3)
