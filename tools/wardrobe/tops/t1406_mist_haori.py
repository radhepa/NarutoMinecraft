"""Mist Haori: a genjutsu master's long haori in mist grey, open down the front over a dark inner
robe, its lower half traced with pale spirals of mist and its front edges lined in
crimson. Reaches the knee."""
from kit import arm_x
from kit_yuhi import mist_swirls
from paint import cap, fabric, k, solid, strip_fabric

META = {
    "name": "Mist Haori",
    "gender": "unisex",
    "description": "Long open mist-grey haori with pale mist spirals and crimson-lined edges, dark inner robe.",
    "tags": ["shinobi", "robe", "jonin"],
    "covers_waist": True,
}


def build(g):
    body, jacket = g.part("body"), g.part("jacket")
    strip_fabric(body, "K", "weave", 14750, 2)
    cap(body, "K", texture="weave", seed=14750)
    strip_fabric(jacket, "P", "velvet", 14751, 2, 0, 11)
    fabric(jacket.top, "P", "velvet", 14751, 3)
    for face in jacket.sides:
        mist_swirls(face, 0, 8, face.w - 1, 11, "P", 4)
    # Open front: the inner robe shows down the middle, the haori's edges lined in crimson.
    for y in range(12):
        for x in (3, 4):
            jacket.front.clear(x, y)
        jacket.front.set(2, y, "A2"), jacket.front.set(5, y, "A1")
    for name, xs in (("right", (-4.6, -1.4)), ("left", (1.4, 4.6))):
        x0, x1 = xs
        for part, z, motion, face_name in (("front", -2.85, "flap_front", "front"),):
            panel = g.piece(f"hem_{name}", "TORSO", (0, 0, 0), (3, 7, 1), pivot=(x0, 11.4, z), motion=motion)
            solid(panel, "P", "velvet", 14752 + (name == "left"), 2)
            mist_swirls(panel.front, 0, 0, 2, 6, "P", 4)
            panel.front.vline(2 if name == "right" else 0, 0, 6, "A2")
    back = g.piece("hem_back", "TORSO", (-4.5, 0, 0), (9, 7, 1), pivot=(0, 11.4, 1.85), motion="flap_back")
    solid(back, "P", "velvet", 14754, 2)
    mist_swirls(back.back, 0, 0, 8, 6, "P", 4)
    for side, bone in (("right", "RIGHT_ARM"), ("left", "LEFT_ARM")):
        arm, sleeve = g.part(f"{side}_arm"), g.part(f"{side}_sleeve")
        strip_fabric(arm, "P", "velvet", 14755 + (side == "left"), 2, 0, 9)
        fabric(arm.top, "P", "velvet", 14757, 3)
        strip_fabric(sleeve, "P", "velvet", 14758, 2, 0, 8)
        fabric(sleeve.top, "P", "velvet", 14758, 3)
        cuff = g.piece(f"{side}_cuff", bone, (arm_x(side) - .5, 7.4, -2.5), (5, 2, 5), inflate=.1)
        solid(cuff, "P", "velvet", 14759 + (side == "left"), 2)
        for face in cuff.sides:
            face.hline(0, face.w - 1, 1, "A2")
        cuff.bottom.fill("K1")
    collar = g.piece("collar", "TORSO", (-4.5, -.9, -2.6), (9, 1, 5), inflate=.08)
    solid(collar, "P", "velvet", 14761, 2)
    for face in collar.sides:
        face.hline(0, face.w - 1, 0, "A2")
