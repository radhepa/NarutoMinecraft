"""Padded Long Vest: a sleeveless padded coat falling open to the hips, stitched in long channels and
trimmed in pale binding, over a dark sleeveless undershirt; steel-plated forearm guards and wrapped
knuckles for blocking blades. A jonin who fights up close."""
from kit import arm_bone, arm_x
from kit_shinobi import bandage
from paint import fabric, k, solid, strip_fabric

META = {
    "name": "Padded Long Vest",
    "gender": "unisex",
    "description": "Open sleeveless padded coat to the hips with pale binding, a dark undershirt, steel forearm guards.",
    "tags": ["shinobi", "vest", "jonin"],
    "covers_waist": True,
}


def build(g):
    body, jacket = g.part("body"), g.part("jacket")
    strip_fabric(body, "K", "rib", 35160, 3)
    fabric(body.top, "K", "rib", 35160, 4)
    strip_fabric(jacket, "P", "plain", 35161, 2, 0, 11)
    fabric(jacket.top, "P", "plain", 35161, 3)
    for x in range(jacket.strip.w):
        if x % 3 == 0:
            jacket.strip.vline(x, 1, 11, "P1")
    f = jacket.front
    for y in range(12):
        f.set(3, y, None), f.set(4, y, None)
    f.vline(2, 0, 11, "S3"), f.vline(5, 0, 11, "S3")
    jacket.strip.hline(0, jacket.strip.w - 1, 11, "S2")
    for side in ("right", "left"):
        arm = g.part(f"{side}_arm")
        bandage(arm.strip, 0, 10, arm.strip.w - 1, 11)
        bandage(arm.bottom, 0, 0, arm.bottom.w - 1, arm.bottom.h - 1)
        guard = g.piece(f"{side}_forearm_guard", arm_bone(side), (arm_x(side) - .3, 4.2, -2.3), (4, 5, 4), inflate=.1)
        solid(guard, "L", "leather", 35162 + (side == "left"), 1)
        outer = guard.right if side == "right" else guard.left
        fabric(outer, "M", "plain", 35164, 3, 0, 1, 4, 3)
        outer.hline(0, 3, 1, "M4")
        for face in guard.sides:
            face.hline(0, face.w - 1, 0, k("L", 2))
    collar = g.piece("padded_collar", "TORSO", (-4.5, -1.2, -2.7), (9, 2, 5), inflate=.08)
    solid(collar, "P", "plain", 35165, 2)
    collar.front.hline(3, 5, 0, "S3"), collar.front.hline(3, 5, 1, "S2")
    for face in collar.sides:
        face.hline(0, face.w - 1, 0, "P3")
