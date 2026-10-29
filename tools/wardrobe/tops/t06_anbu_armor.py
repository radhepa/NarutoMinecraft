"""ANBU Armor: a black sleeveless undershirt under grey-white plated chest armor, long white arm
guards over black gloves, the red spiral tattoo on the left shoulder and a tanto across the back."""
from paint import cap, fabric, solid, strip_fabric

META = {
    "name": "ANBU Armor",
    "gender": "unisex",
    "description": "Grey-white plated chest armor over a black sleeveless shirt, white arm guards, a tanto.",
    "tags": ["shinobi", "armor"],
}

# The ANBU spiral, one texel per pixel on the outer face of the left upper arm.
TATTOO = ["AAA.",
          "A.A.",
          "A.AA"]


def build(g):
    body, jacket = g.part("body"), g.part("jacket")
    strip_fabric(body, "D", "weave", 151, 2)
    cap(body, "D", seed=151)
    # Chest armor: plates split by dark seams every three rows, bright top edges, open below the ribs.
    strip_fabric(jacket, "P", "plain", 152, 2, 0, 8)
    cap(jacket, "P", texture="plain", seed=152)
    for y in (3, 6):
        jacket.strip.hline(0, jacket.strip.w - 1, y - 1, "P1")
        jacket.strip.hline(0, jacket.strip.w - 1, y, "P3")
    jacket.strip.hline(0, jacket.strip.w - 1, 0, "P3")
    jacket.strip.hline(0, jacket.strip.w - 1, 8, "P0")
    jacket.front.vline(4, 0, 8, "P1")
    for face in (jacket.right, jacket.left):
        face.vline(1, 0, 8, "K1"), face.vline(2, 0, 8, "K2")   # the side straps
    # Black belt with a steel buckle.
    body.strip.hline(0, body.strip.w - 1, 9, "K1"), body.strip.hline(0, body.strip.w - 1, 10, "K2")
    body.front.set(3, 9, "M3"), body.front.set(4, 9, "M3"), body.front.set(3, 10, "M2"), body.front.set(4, 10, "M2")
    for side in ("right", "left"):
        arm, guard = g.part(f"{side}_arm"), g.part(f"{side}_sleeve")
        # Bare upper arm; the shirt edge on the shoulder, gloves below the guards.
        fabric(arm.top, "D", "weave", 153, 2)
        arm.strip.hline(0, arm.strip.w - 1, 0, "D2")
        strip_fabric(arm, "K", "smooth", 154, 2, 4, 11)
        fabric(arm.bottom, "K", "smooth", 154, 1)
        # Long guards from elbow to wrist: plain white plates with a seam and a steel stud.
        strip_fabric(guard, "S", "plain", 155 + (side == "left"), 2, 4, 9)
        guard.strip.hline(0, guard.strip.w - 1, 4, "S4")
        guard.strip.hline(0, guard.strip.w - 1, 7, "S1")
        guard.strip.hline(0, guard.strip.w - 1, 9, "S1")
        outer = guard.right if side == "right" else guard.left
        outer.set(1, 7, "M3"), outer.set(2, 7, "M3")
    left = g.part("left_arm").left
    for y, row in enumerate(TATTOO):
        for x, ch in enumerate(row):
            if ch == "A":
                left.set(x, 1 + y, "A2")
    # Tanto across the back: wrapped hilt over the right shoulder, steel guard, black sheath.
    tilt = (0, 0, -38)
    hilt = g.piece("tanto_hilt", "TORSO", (-.5, -4, -.5), (1, 4, 1), pivot=(-1.0, 4.6, 2.9), rotation=tilt)
    solid(hilt, "K", "smooth", 157, 2)
    for face in hilt.sides:
        for y in (0, 2):
            face.set(0, y, "S3")
    guard = g.piece("tanto_guard", "TORSO", (-1, 0, -1), (2, 1, 2), pivot=(-1.0, 4.6, 2.9), rotation=tilt)
    solid(guard, "M", "plain", 158, 3)
    sheath = g.piece("tanto_sheath", "TORSO", (-.5, 1, -.5), (1, 8, 1), pivot=(-1.0, 4.6, 2.9), rotation=tilt)
    solid(sheath, "K", "smooth", 159, 2)
    for face in sheath.sides:
        face.set(0, 7, "M2")
