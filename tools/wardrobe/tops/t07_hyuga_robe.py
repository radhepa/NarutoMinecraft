"""Hyuga Robe: the clan's long off-white robe, wrapped left over right with a trimmed collar, long
sleeves with wide cuffs, a dark sash with hanging ends, and a skirt to mid-thigh split at the sides."""
from kit import arm_x, belt, flaps
from paint import cap, fabric, solid, strip_fabric

META = {
    "name": "Hyuga Robe",
    "gender": "unisex",
    "description": "Long off-white wrapped robe, wide cuffs, dark sash, split skirt.",
    "tags": ["shinobi", "robe"],
    "covers_waist": True,
}


def build(g):
    body = g.part("body")
    strip_fabric(body, "P", "velvet", 181, 2)
    cap(body, "P", texture="velvet", seed=181)
    f = body.front
    # The wrap: a diagonal overlap edge from the right shoulder to the left hip, trimmed in lavender.
    for i in range(7):
        x = 1 + i
        if x <= 7:
            f.set(x, i, "A2")
            if x + 1 <= 7:
                f.set(x + 1, i, "P1")
    f.set(0, 0, "A2")
    f.vline(7, 6, 7, "P1")
    # Sash and its tied ends on the left hip.
    belt(g, "sash", y=7.6, role="D", height=2, buckle=None, inflate=.15)
    for i, (x, rz) in enumerate(((3.0, 6), (3.7, -8))):
        end = g.piece(f"sash_end_{i}", "TORSO", (-.5, 0, -.5), (1, 5 - i, 1), pivot=(x, 9.4, -2.75), rotation=(0, 0, rz),
                      motion="sway")
        solid(end, "D", "weave", 182 + i, 2)
    # The split skirt to mid-thigh.
    for face in flaps(g, "robe", 5, "P", "velvet", 184, width=9, hem="P1", top=11.0, front_z=-2.75, back_z=1.75):
        face.vline(0, 1, 4, "P1"), face.vline(8, 1, 4, "P1")
    # Long sleeves flaring into wide cuffs above the hands.
    for side, bone in (("right", "RIGHT_ARM"), ("left", "LEFT_ARM")):
        arm, sleeve = g.part(f"{side}_arm"), g.part(f"{side}_sleeve")
        strip_fabric(arm, "P", "velvet", 186 + (side == "left"), 2, 0, 9)
        fabric(arm.top, "P", "velvet", 186, 3)
        strip_fabric(sleeve, "P", "velvet", 188, 2, 0, 4)
        fabric(sleeve.top, "P", "velvet", 188, 3)
        cuff = g.piece(f"{side}_cuff", bone, (arm_x(side) - .5, 7.6, -2.5), (5, 2, 5), inflate=.1)
        solid(cuff, "P", "velvet", 189 + (side == "left"), 2)
        for face in cuff.sides:
            face.hline(0, face.w - 1, 0, "P3"), face.hline(0, face.w - 1, 1, "A2")
        cuff.bottom.fill("P0")
    # A soft standing collar.
    collar = g.piece("collar", "TORSO", (-4.5, -.9, -2.6), (9, 1, 5), inflate=.06)
    solid(collar, "P", "velvet", 191, 2)
    for face in collar.sides:
        face.hline(0, face.w - 1, 0, "A2")
