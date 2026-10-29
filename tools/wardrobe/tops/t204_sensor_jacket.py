"""Sensor Jacket: after Karin's: a fitted long-sleeved top that zips to a high collar, cropped above
the navel, with accent cuffs and the small whirlpool on the left shoulder."""
from kit import collar
from kit_uzumaki import crest_patch
from paint import cap, fabric, strip_fabric

META = {
    "name": "Sensor Jacket",
    "gender": "unisex",
    "description": "Fitted cropped zip-up top with a high collar, accent cuffs, a whirlpool on the shoulder.",
    "tags": ["shinobi", "genin"],
}


def build(g):
    body = g.part("body")
    strip_fabric(body, "P", "plain", 2240, 2, 0, 6)
    body.strip.hline(0, body.strip.w - 1, 6, "P1")
    cap(body, "P", seed=2240)
    body.front.vline(3, 0, 5, "S3"), body.front.vline(4, 0, 5, "P1")
    for face in (body.front, body.back):
        face.vline(1, 2, 5, "P1"), face.vline(6, 2, 5, "P3")
    for side in ("right", "left"):
        arm = g.part(f"{side}_arm")
        strip_fabric(arm, "P", "plain", 2241 + (side == "left"), 2, 0, 10)
        fabric(arm.top, "P", "plain", 2241, 3)
        arm.strip.hline(0, arm.strip.w - 1, 9, "A2"), arm.strip.hline(0, arm.strip.w - 1, 10, "A3")
    neck = collar(g, "collar", "P", "plain", height=2, y=-1.4)
    neck.front.vline(4, 0, 1, "S3")
    crest_patch(g, "left_crest", "LEFT_ARM", (3.05, .4, 0), size=6, ground="P2", ink="A2", outward="left")
