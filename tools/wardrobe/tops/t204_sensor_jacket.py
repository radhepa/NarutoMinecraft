"""Sensor Jacket: a fitted long-sleeved top that zips to a high collar, cut short at the waist with a
dark belt, orange-cuffed sleeves and the small whirlpool on the left shoulder."""
from kit import belt, collar
from kit_uzumaki import crest_patch
from paint import cap, fabric, strip_fabric

META = {
    "name": "Sensor Jacket",
    "gender": "unisex",
    "description": "Fitted zip-up top with a high collar, dark belt, orange cuffs, a whirlpool on the shoulder.",
    "tags": ["shinobi", "genin"],
}


def build(g):
    body = g.part("body")
    strip_fabric(body, "P", "plain", 2240, 2, 0, 9)
    cap(body, "P", seed=2240)
    body.front.vline(3, 0, 9, "S3"), body.front.vline(4, 0, 9, "P1")
    for face in (body.front, body.back):
        face.vline(1, 3, 8, "P1"), face.vline(6, 3, 8, "P3")
    for side in ("right", "left"):
        arm = g.part(f"{side}_arm")
        strip_fabric(arm, "P", "plain", 2241 + (side == "left"), 2, 0, 10)
        fabric(arm.top, "P", "plain", 2241, 3)
        arm.strip.hline(0, arm.strip.w - 1, 9, "A2"), arm.strip.hline(0, arm.strip.w - 1, 10, "A3")
    neck = collar(g, "collar", "P", "plain", height=2, y=-1.4)
    neck.front.vline(4, 0, 1, "S3")
    belt(g, "belt", y=8.8, role="K", height=1, buckle="M")
    crest_patch(g, "left_crest", "LEFT_ARM", (3.05, .4, 0), size=6, ground="P2", ink="A2", outward="left")
