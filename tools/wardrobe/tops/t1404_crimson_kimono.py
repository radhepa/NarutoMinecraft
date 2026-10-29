"""Crimson Kimono: the red kimono Kurenai wore in her quiet years, wrapped left over right with an
ivory collar, a broad white obi tied with a crimson cord, long hanging sleeves and a knee-length
skirt; thorny stems are printed up from the hem."""
from kit import arm_x, belt, flaps
from kit_yuhi import thorn_vine
from paint import cap, fabric, k, solid, strip_fabric

META = {
    "name": "Crimson Kimono",
    "gender": "unisex",
    "description": "Red kimono, ivory collar, white obi with a crimson cord, long hanging sleeves, knee-length skirt.",
    "tags": ["robe", "wrap"],
    "covers_waist": True,
}


def build(g):
    body = g.part("body")
    strip_fabric(body, "P", "velvet", 14690, 2)
    cap(body, "P", texture="velvet", seed=14690)
    f = body.front
    for i in range(7):
        f.set(1 + i, i, "S3")
        if i < 6:
            f.set(2 + i, i, "P1")
    f.set(0, 0, "S3")
    obi = belt(g, "obi", y=7.0, role="S", height=3, buckle=None, inflate=.12)
    for face in obi.sides:
        face.hline(0, face.w - 1, 1, "A2")
    knot = g.piece("obi_knot", "TORSO", (-2, -1, 0), (4, 3, 2), pivot=(0, 8.5, 2.6))
    solid(knot, "S", "weave", 14691, 3)
    knot.back.hline(0, 3, 1, "A2")
    for face in flaps(g, "skirt", 7, "P", "velvet", 14692, width=9, top=10.0, front_z=-2.75, back_z=1.75):
        face.hline(0, face.w - 1, face.h - 1, "P1")
        thorn_vine(face, 1, 3, face.h - 2, "A")
        thorn_vine(face, 6, 4, face.h - 2, "A")
    for side, bone in (("right", "RIGHT_ARM"), ("left", "LEFT_ARM")):
        arm, sleeve = g.part(f"{side}_arm"), g.part(f"{side}_sleeve")
        strip_fabric(arm, "P", "velvet", 14693 + (side == "left"), 2, 0, 8)
        fabric(arm.top, "P", "velvet", 14695, 3)
        strip_fabric(sleeve, "P", "velvet", 14696, 2, 0, 6)
        fabric(sleeve.top, "P", "velvet", 14696, 3)
        # The long sleeve hanging below the forearm.
        drape = g.piece(f"{side}_drape", bone, (arm_x(side) - .4, 3.0, 1.0), (5, 7, 2), inflate=.05, motion="sway")
        solid(drape, "P", "velvet", 14697 + (side == "left"), 2)
        for face in drape.sides:
            face.hline(0, face.w - 1, face.h - 1, "S3")
    collar = g.piece("collar", "TORSO", (-4.5, -.9, -2.6), (9, 1, 5), inflate=.06)
    solid(collar, "S", "weave", 14699, 3)
