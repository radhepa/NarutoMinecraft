"""Uchiha High Collar: the clan's dark short-sleeved shirt with a tall open collar, the red-and-white
uchiwa crest across the back, and white arm warmers."""
from paint import cap, fabric, k, solid, strip_fabric

META = {
    "name": "Uchiha High Collar",
    "gender": "unisex",
    "description": "Dark navy high-collared shirt, Uchiha fan crest on the back, white arm warmers.",
    "tags": ["shinobi", "uchiha"],
}


def crest(face, x0: int, y0: int):
    """The uchiwa: a fan whose upper half is red and lower half white, outlined, on a white handle."""
    import math
    c, r = 4.5, 4.6
    for y in range(10):
        for x in range(10):
            d = math.hypot(x + .5 - 5, y + .5 - 5)
            if d > r:
                continue
            key = "A2" if y < 5 else "S3"
            if d > r - .9:
                key = "A1" if y < 5 else "S2"
            if y < 5 and x + y < 5:
                key = "A3" if d <= r - .9 else key
            face.set(x0 + x, y0 + y, key)
    for y in range(10, 15):
        face.set(x0 + 4, y0 + y, "S3"), face.set(x0 + 5, y0 + y, "S2")


def build(g):
    body, jacket = g.part("body"), g.part("jacket")
    strip_fabric(body, "P", "weave", 71, 2)
    cap(body, "P", seed=71)
    strip_fabric(jacket, "P", "weave", 72, 2, 9, 11)
    jacket.strip.hline(0, jacket.strip.w - 1, 11, "P1")
    f = body.front
    # A loose fold from each shoulder and a slight open neck.
    f.vline(2, 2, 9, "P1"), f.vline(5, 3, 9, "P1")
    f.set(3, 0, "P0"), f.set(4, 0, "P0")
    # The crest across the shoulders at double resolution.
    plate = g.piece("back_crest", "TORSO", (-5, 0, 0), (10, 16, 1), pivot=(0, 1.0, 2.05), scale=(.5, .5, .5))
    for face in plate.faces:
        fabric(face, "P", "weave", 73, 2)
    crest(plate.back, 0, 0)
    for side, bone in (("right", "RIGHT_ARM"), ("left", "LEFT_ARM")):
        arm, sleeve = g.part(f"{side}_arm"), g.part(f"{side}_sleeve")
        strip_fabric(arm, "P", "weave", 74, 2, 0, 3)
        fabric(arm.top, "P", "weave", 74, 3)
        strip_fabric(sleeve, "P", "weave", 75, 2, 0, 3)
        for face in sleeve.sides:
            face.hline(0, face.w - 1, 3, "P1")
        # Arm warmers from below the elbow to the wrist.
        for y in range(6, 11):
            for x in range(arm.strip.w):
                arm.strip.set(x, y, "S2" if y in (6, 10) else ("S3" if x % 2 else "S4"))
        ox = -3.0 if side == "right" else -1.0
        cuff = g.piece(f"{side}_warmer_cuff", bone, (ox - .3, 5.6, -2.3), (4, 1, 4), inflate=.12)
        solid(cuff, "S", "rib", 76, 3)
    # Tall open collar: back and two sides standing up around the neck.
    back = g.piece("collar_back", "TORSO", (-4.5, -2.6, 0), (9, 3, 1), pivot=(0, 0, 1.6), rotation=(-8, 0, 0))
    solid(back, "P", "weave", 77, 2)
    for face in back.sides:
        face.hline(0, face.w - 1, 0, "P3")
    for side, x, rz in (("right", -4.5, -6), ("left", 3.5, 6)):
        wing = g.piece(f"collar_{side}", "TORSO", (0, -2.6, -2.6), (1, 3, 4), pivot=(x, 0, 0), rotation=(0, 0, rz))
        solid(wing, "P", "weave", 78, 2)
        for face in wing.sides:
            face.hline(0, face.w - 1, 0, "P3")
