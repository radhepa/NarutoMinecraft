"""Wisteria Travel Cloak: a long travelling cloak for the road between villages, a short shoulder
cape over it and a soft hood thrown back, clasped at the throat with a cord; wisteria sprays are
painted round the hem. Open in front over a plain dark shirt."""
from kit import arm_bone, arm_x
from kit_kurama import back_crest, wisteria_hem
from paint import cap, fabric, k, solid, strip_fabric

META = {
    "name": "Wisteria Travel Cloak",
    "gender": "unisex",
    "description": "Long open travelling cloak, a shoulder cape and a thrown-back hood, wisteria painted round the hem.",
    "tags": ["shinobi", "cloak"],
}

LENGTH = 17


def cloth(face, seed, base=2):
    fabric(face, "P", "twill", seed, base)
    for x in range(1, face.w - 1, 3):
        face.vline(x, 1, face.h - 1, k("P", base - 1))
    face.hline(0, face.w - 1, face.h - 1, k("P", base - 1))


def build(g):
    body = g.part("body")
    strip_fabric(body, "D", "weave", 12750, 2)
    cap(body, "D", seed=12750)
    body.front.vline(4, 1, 11, "D1")
    for side in ("right", "left"):
        arm = g.part(f"{side}_arm")
        strip_fabric(arm, "D", "weave", 12751, 2, 0, 10)
        fabric(arm.top, "D", "weave", 12751, 3)
        drape = g.piece(f"{side}_drape", arm_bone(side), (arm_x(side) - .5, -2.5, -2.5), (5, 8, 5))
        solid(drape, "P", "twill", 12752 + (side == "left"), 2)
        for face in drape.sides:
            cloth(face, 12754 + (side == "left"))
            face.hline(0, face.w - 1, 7, "S3")
    # The shoulder cape and the hood lying back on it.
    cape = g.piece("capelet", "TORSO", (-4.5, -.6, -2.7), (9, 5, 5), inflate=.1)
    solid(cape, "P", "twill", 12756, 2)
    for face in cape.sides:
        face.hline(0, face.w - 1, 0, "P3")
        face.hline(0, face.w - 1, 4, "S3")
    cape.front.vline(4, 0, 4, "P0")
    cape.front.set(3, 1, "A2"), cape.front.set(5, 1, "A2"), cape.front.set(4, 1, "A3")
    hood = g.piece("hood", "TORSO", (-3.5, 0, 0), (7, 4, 2), pivot=(0, -1.2, 2.2), rotation=(18, 0, 0))
    solid(hood, "P", "twill", 12757, 2)
    hood.top.fill("P1")
    for face in hood.sides:
        face.hline(0, face.w - 1, 0, "S3")
    back = g.piece("cloak_back", "TORSO", (-5, 0, 0), (10, LENGTH, 1), pivot=(0, 1.6, 2.6), motion="flap_back")
    solid(back, "P", "twill", 12758, 2)
    cloth(back.back, 12759)
    wisteria_hem(back.back, 12760, light="A3", dark="A2", stem="P1", step=2, y0=LENGTH - 8)
    back.back.hline(0, 9, LENGTH - 1, "S3")
    for side, x in (("right", -3.1), ("left", 3.1)):
        panel = g.piece(f"cloak_front_{side}", "TORSO", (-1.5, 0, -.5), (3, LENGTH - 3, 1), pivot=(x, 3.0, -2.8),
                        motion="flap_front")
        solid(panel, "P", "twill", 12761 + (x > 0), 2)
        cloth(panel.front, 12763 + (x > 0))
        wisteria_hem(panel.front, 12765 + (x > 0), light="A3", dark="A2", stem="P1", step=2, y0=LENGTH - 10)
        panel.front.hline(0, 2, LENGTH - 4, "S3")
    back_crest(g, role="P", ink="S3", pivot=(0, 4.2, 3.12), texture="twill")
