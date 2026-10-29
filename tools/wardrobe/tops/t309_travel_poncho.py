"""Travel Poncho: an Uchiha on a long road, a dark cape over the shoulders falling to the hips with a
high collar clasped by a small fan pin, over a grey shirt with long sleeves."""
from kit import arm_bone, arm_x
from paint import cap, fabric, k, solid, strip_fabric

META = {
    "name": "Travel Poncho",
    "gender": "unisex",
    "description": "Dark hip-length cape with a high clasped collar and fan pin, over a long-sleeved shirt.",
    "tags": ["shinobi", "cloak", "uchiha"],
}


def cloth(face, seed, folds=3):
    fabric(face, "P", "twill", seed, 2)
    for x in range(1, face.w - 1, folds):
        face.vline(x, 1, face.h - 1, "P1")
    face.hline(0, face.w - 1, 0, "P3")
    face.hline(0, face.w - 1, face.h - 1, "P1")


def build(g):
    body = g.part("body")
    strip_fabric(body, "D", "weave", 3920, 2)
    cap(body, "D", seed=3920)
    body.strip.hline(0, body.strip.w - 1, 10, "L2")
    for side in ("right", "left"):
        arm = g.part(f"{side}_arm")
        strip_fabric(arm, "D", "weave", 3921, 2, 0, 11)
        fabric(arm.top, "D", "weave", 3921, 3)
        strip_fabric(arm, "K", "leather", 3922, 2, 8, 10)
        drape = g.piece(f"{side}_drape", arm_bone(side), (arm_x(side) - .5, -2.5, -2.5), (5, 5, 5))
        solid(drape, "P", "twill", 3923 + (side == "left"), 2)
        for face in drape.sides:
            cloth(face, 3925 + (side == "left"))
    yoke = g.piece("yoke", "TORSO", (-4.5, -.6, -2.6), (9, 3, 5))
    solid(yoke, "P", "twill", 3927, 2)
    for face in yoke.sides:
        face.hline(0, face.w - 1, 0, "P3")
    # The high clasped collar and its fan pin.
    collar = g.piece("collar", "TORSO", (-4.5, -2.2, -2.8), (9, 2, 5), inflate=.08)
    solid(collar, "P", "twill", 3928, 2)
    for face in collar.sides:
        face.hline(0, face.w - 1, 0, "P3")
    pin = g.piece("fan_pin", "TORSO", (-1, -1, 0), (2, 2, 1), pivot=(0, -.6, -3.1))
    for face in pin.faces:
        face.fill("S3")
    pin.front.set(0, 0, "A2"), pin.front.set(1, 0, "A2"), pin.front.set(0, 1, "S3"), pin.front.set(1, 1, "S2")
    back = g.piece("cape_back", "TORSO", (-5, 0, 0), (10, 11, 1), pivot=(0, 1.6, 2.5), motion="flap_back")
    solid(back, "P", "twill", 3929, 2)
    cloth(back.back, 3930)
    for side, x in (("right", -2.9), ("left", 2.9)):
        panel = g.piece(f"cape_front_{side}", "TORSO", (-1.5, 0, -.5), (3, 9, 1), pivot=(x, 2.2, -2.75), motion="flap_front")
        solid(panel, "P", "twill", 3931 + (x > 0), 2)
        cloth(panel.front, 3933 + (x > 0))
