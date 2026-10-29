"""Caped Greatcoat: a black greatcoat closed to the throat under a short shoulder cape that falls
to the elbows, the cape edged in oxblood, the skirts long to the shin."""
from kit import collar
from kit_morino import coat_skirts
from paint import cap, fabric, solid, strip_fabric

META = {
    "name": "Caped Greatcoat",
    "gender": "unisex",
    "description": "Black greatcoat closed to the throat under an elbow-length shoulder cape edged in oxblood.",
    "tags": ["shinobi", "coat", "jonin"],
    "covers_waist": True,
}


def build(g):
    body, jacket = g.part("body"), g.part("jacket")
    strip_fabric(body, "P", "twill", 17271, 2)
    cap(body, "P", texture="twill", seed=17271)
    strip_fabric(jacket, "P", "twill", 17272, 2)
    cap(jacket, "P", texture="twill", seed=17272)
    jacket.front.vline(4, 0, 11, "P0")
    for y in (6, 8, 10):
        jacket.front.set(3, y, "M3")
    for side in ("right", "left"):
        arm, sleeve = g.part(f"{side}_arm"), g.part(f"{side}_sleeve")
        strip_fabric(arm, "P", "twill", 17273 + (side == "left"), 2, 0, 11)
        fabric(arm.top, "P", "twill", 17273, 3)
        strip_fabric(sleeve, "P", "twill", 17275, 2, 6, 10)
        sleeve.strip.hline(0, sleeve.strip.w - 1, 10, "P0")
    # The cape: a short mantle over the shoulders and upper arms.
    cape = g.piece("cape", "TORSO", (-8, -.2, -3), (16, 7, 6), inflate=.25)
    solid(cape, "P", "twill", 17276, 2)
    fabric(cape.top, "P", "twill", 17276, 3)
    for face in cape.sides:
        face.hline(0, face.w - 1, 6, "A1")
        face.hline(0, face.w - 1, 5, "P1")
    cape.front.vline(7, 0, 6, "P0"), cape.front.vline(8, 0, 6, "P3")
    cape.bottom.fill("P0")
    neck = collar(g, "collar", "P", "twill", height=2, y=-2.0, inflate=.35)
    neck.front.set(4, 1, "M3")
    coat_skirts(g, "skirt", 9, "P", 17280, hem="A1", open_front=False)
