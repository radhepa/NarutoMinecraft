"""Fur-Wrapped Leggings: close dark leggings with strips of shaggy fur bound round the calves by
cross-tied thongs, soft leather boots underneath and a fur-trimmed belt pouch: northern trapper kit."""
from kit import legs, waistband
from kit_rugged import shag_box, soft_boots
from paint import solid

META = {"name": "Fur-Wrapped Leggings", "gender": "unisex",
        "description": "Close dark leggings with shaggy fur bound round the calves, soft leather boots, a belt pouch.",
        "tags": ["shinobi"]}


def build(g):
    waistband(g, "D", "knit", 35500, 2)
    legs(g, "D", "knit", 35501, 2, rows=(0, 9), crease=False)
    soft_boots(g, top=10, role="L")
    for side, bone in (("right", "RIGHT_LEG"), ("left", "LEFT_LEG")):
        fur = g.piece(f"{side}_calf_fur", bone, (-2.5, 5.6, -2.5), (5, 4, 5), inflate=.1)
        shag_box(fur, "S", 35502 + (side == "left"), 2)
        for y in (6.4, 8.4):
            thong = g.piece(f"{side}_thong_{int(y)}", bone, (-2.5, y, -2.5), (5, 1, 5), inflate=.2)
            for face in thong.faces:
                face.fill("L1")
            for face in thong.sides:
                face.set(face.w // 2, 0, "L3")
    belt = g.piece("waist_belt", "TORSO", (-4.6, 9.4, -2.6), (9, 1, 5), inflate=.1)
    solid(belt, "L", "leather", 35505, 1, edge=False)
    pouch = g.piece("waist_pouch", "TORSO", (0, 0, 0), (3, 2, 1), pivot=(.6, 10.0, -2.9))
    solid(pouch, "L", "leather", 35506, 2)
    trim = g.piece("waist_pouch_fur", "TORSO", (0, 0, 0), (3, 1, 1), pivot=(.6, 9.6, -3.0))
    shag_box(trim, "S", 35507, 2)
