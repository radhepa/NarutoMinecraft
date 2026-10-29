"""Scout Shorts: knee shorts in the clan's dark cloth, grey shin wraps wound to the boot, soft
split-toe boots, and a knotted cord belt with a small pouch on the left hip."""
from kit import legs, waistband
from kit_tobari import shin_wraps, split_toe_boots
from paint import solid

META = {"name": "Scout Shorts", "gender": "unisex",
        "description": "Dark knee shorts, grey shin wraps, soft split-toe boots, a cord belt with a hip pouch.",
        "tags": ["shinobi", "genin"]}


def build(g):
    waistband(g, "D", "twill", 25660)
    legs(g, "D", "twill", 25661, rows=(0, 4))
    for side in ("right", "left"):
        g.part(f"{side}_leg").strip.hline(0, 15, 4, "D1")
    shin_wraps(g, 5, 7)
    split_toe_boots(g, top=8, role="K", tie=None)
    cord = g.piece("waist_cord", "TORSO", (-4.5, 0, -2.5), (9, 1, 5), pivot=(0, 9.4, 0), inflate=.3)
    for face in cord.faces:
        for x in range(face.w):
            for y in range(face.h):
                face.set(x, y, "S3" if (x + y) % 2 else "S2")
    pouch = g.piece("hip_pouch", "TORSO", (-1, 0, -1), (2, 2, 2), pivot=(3.9, 9.8, 0))
    solid(pouch, "L", "leather", 25663, 2)
