"""Crest Zip Top: Sakura's Shippuden top, a sleeveless red tunic zipped from a short standing collar
to the waist with the white circle on the back, black fingerless gloves and rose elbow pads."""
from kit import arm_bone, arm_x
from kit_haruno import back_crest
from paint import cap, fabric, k, solid, strip_fabric

META = {
    "name": "Crest Zip Top",
    "gender": "unisex",
    "description": "Sleeveless red zip tunic with a short collar, circle crest on the back, black gloves, rose elbow pads.",
    "tags": ["shinobi"],
}


def build(g):
    body = g.part("body")
    strip_fabric(body, "P", "smooth", 19520, 2, 0, 9)
    fabric(body.top, "P", "smooth", 19520, 3)
    f = body.front
    f.vline(3, 1, 9, k("S", 2)), f.vline(4, 1, 9, k("P", 1)), f.set(3, 1, k("M", 4))
    f.vline(1, 3, 9, k("P", 1)), f.vline(6, 3, 9, k("P", 3))
    body.strip.hline(0, body.strip.w - 1, 9, k("P", 1))
    collar = g.piece("collar", "TORSO", (-2.5, -1.2, -2.4), (5, 1, 5), inflate=.1)
    solid(collar, "P", "smooth", 19521, 2, edge=False)
    collar.front.set(2, 0, k("S", 3))
    for side in ("right", "left"):
        arm = g.part(f"{side}_arm")
        arm.strip.hline(0, arm.strip.w - 1, 0, k("P", 2)), arm.top.fill(k("P", 3))
        strip_fabric(arm, "K", "leather", 19522, 2, 8, 11)
        arm.strip.hline(0, arm.strip.w - 1, 8, k("K", 3))
        fabric(arm.bottom, "K", "leather", 19522, 1)
        pad = g.piece(f"{side}_elbow_pad", arm_bone(side), (arm_x(side) - .3, 4.2, -2.3), (4, 2, 4), inflate=.08)
        solid(pad, "A", "smooth", 19523 + (side == "left"), 2, edge=False)
        for face in pad.sides:
            face.hline(0, face.w - 1, 0, k("A", 3))
    back_crest(g, "P", texture="smooth", seed=19525)
