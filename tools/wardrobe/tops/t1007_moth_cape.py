"""Moth Cape: a light, open look for a young Aburame, a fitted sleeveless top under a short
shoulder cape that spreads like a moth's wings, a moth with eye spots worked across the back,
and pale wraps on the forearms."""
from kit import arm_bone, arm_x
from kit_aburame import MOTH, glyph
from kit_shinobi import bandage
from paint import cap, fabric, k, solid, strip_fabric

META = {
    "name": "Moth Cape",
    "gender": "unisex",
    "description": "Sleeveless top under a short wing-shaped shoulder cape with a moth on the back, arm wraps.",
    "tags": ["shinobi", "aburame"],
}


def build(g):
    body = g.part("body")
    strip_fabric(body, "P", "weave", 10661, 2)
    cap(body, "P", seed=10661)
    body.front.set(3, 0, None), body.front.set(4, 0, None)
    body.front.set(2, 0, "P1"), body.front.set(5, 0, "P1")
    body.strip.hline(0, body.strip.w - 1, 11, "P1")
    for side in ("right", "left"):
        arm = g.part(f"{side}_arm")
        for face in arm.sides:
            bandage(face, 0, 7, face.w - 1, 11)
    # The cape: a yoke round the shoulders and a wide back panel that ends in two wing points.
    yoke = g.piece("cape_yoke", "TORSO", (-5, -.4, -2.6), (10, 2, 5))
    solid(yoke, "D", "twill", 10665, 2)
    for face in yoke.sides:
        face.hline(0, face.w - 1, 0, "D3")
    yoke.front.vline(4, 0, 1, "D0"), yoke.front.vline(5, 0, 1, "D0")
    yoke.front.set(4, 1, "M3")
    back = g.piece("cape_back", "TORSO", (-5.5, 0, 0), (11, 7, 1), pivot=(0, 1.4, 2.6), rotation=(6, 0, 0),
                   motion="flap_back")
    solid(back, "D", "twill", 10666, 2)
    glyph(back.back, MOTH, 0, 0, {"#": "S2", "o": "A2", "+": "D0"})
    for side, x in (("right", -3.5), ("left", 3.5)):
        point = g.piece(f"cape_wing_{side}", "TORSO", (-1.5, 0, 0), (3, 2, 1), pivot=(x, 8.4, 2.95),
                        rotation=(6, 0, 0), motion="flap_back")
        solid(point, "D", "twill", 10667, 2)
        point.back.hline(0, 2, 1, "D1")
    # The cape falls over each shoulder and swings with the arm.
    for side in ("right", "left"):
        drape = g.piece(f"cape_drape_{side}", arm_bone(side), (arm_x(side) - .5, -2.4, -2.5), (5, 4, 5))
        solid(drape, "D", "twill", 10668 + (side == "left"), 2)
        for face in drape.sides:
            face.hline(0, face.w - 1, 0, "D3")
            for x in range(1, face.w, 2):
                face.set(x, face.h - 1, "D1")
