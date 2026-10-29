"""Blanket Poncho: a heavy woven blanket with a slit for the head, banded in the accent color and
fringed at the hem, hanging to the hips front and back and over the shoulders, a rolled cowl at the
neck and long undershirt sleeves: rain or dust, it keeps the road off."""
from kit import arm_bone, arm_x, sleeves
from paint import fabric, k, solid, strip_fabric

META = {
    "name": "Blanket Poncho",
    "gender": "unisex",
    "description": "Heavy banded blanket poncho to the hips with a fringed hem and a rolled cowl, over long sleeves.",
    "tags": ["shinobi", "cloak", "chunin"],
    "covers_waist": True,
}


def blanket(face, seed, top=0):
    """Woven blanket: twill ground with two accent bands and a pale pinstripe."""
    fabric(face, "P", "twill", seed, 2)
    for y in range(face.h):
        band = (y + top) % 7
        if band in (3, 4):
            face.hline(0, face.w - 1, y, "A2" if band == 3 else "A1")
        elif band == 6:
            face.hline(0, face.w - 1, y, "S2")
    face.hline(0, face.w - 1, 0, "P3")


def fringe(face):
    for x in range(face.w):
        face.set(x, face.h - 1, "S3" if x % 2 else "S1")


def build(g):
    body = g.part("body")
    strip_fabric(body, "D", "weave", 35050, 2)
    fabric(body.top, "D", "weave", 35050, 3)
    sleeves(g, "D", "weave", 35051, 2, rows=(0, 10), cuff="L2", cuff_row=10)
    for side in ("right", "left"):
        drape = g.piece(f"{side}_drape", arm_bone(side), (arm_x(side) - .5, -2.5, -2.5), (5, 6, 5))
        solid(drape, "P", "twill", 35052 + (side == "left"), 2)
        for face in drape.sides:
            blanket(face, 35054 + (side == "left"), top=1)
            fringe(face)
        drape.top.fill("P3")
    yoke = g.piece("yoke", "TORSO", (-4.5, -.6, -2.6), (9, 4, 5))
    solid(yoke, "P", "twill", 35056, 2)
    for face in yoke.sides:
        blanket(face, 35056, top=1)
    cowl = g.piece("cowl", "TORSO", (-4.5, -1.8, -2.8), (9, 2, 5), inflate=.1)
    solid(cowl, "P", "twill", 35057, 2)
    for face in cowl.sides:
        for x in range(face.w):
            face.set(x, 0, k("P", 3 if x % 2 else 2))
    for name, z, motion in (("front", -3.0, "flap_front"), ("back", 2.0, "flap_back")):
        panel = g.piece(f"poncho_{name}", "TORSO", (-5, 0, 0), (10, 10, 1), pivot=(0, 1.6, z), motion=motion)
        solid(panel, "P", "twill", 35058, 2)
        blanket(getattr(panel, name), 35058 + (name == "back"), top=2)
        fringe(getattr(panel, name))
